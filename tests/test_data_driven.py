"""
tests/test_data_driven.py
Data-Driven Testing using Excel files via openpyxl.
Falls back to inline data if .xlsx file is not present.
"""
import pytest, os
from pages.login_page     import LoginPage
from pages.inventory_page import InventoryPage
from utils.excel_reader   import ExcelReader
from framework.logger     import get_logger

logger = get_logger(__name__)

EXCEL_FILE = os.path.join(os.path.dirname(__file__), "..", "test-data", "login_data.xlsx")


def load_login_data():
    if os.path.exists(EXCEL_FILE):
        with ExcelReader(EXCEL_FILE) as r:
            return r.get_all_rows("LoginTests")
    logger.warning("Excel file not found -- using inline fallback data.")
    return [
        {"username": "standard_user",          "password": "secret_sauce",  "expected_result": "pass"},
        {"username": "locked_out_user",         "password": "secret_sauce",  "expected_result": "fail"},
        {"username": "problem_user",            "password": "secret_sauce",  "expected_result": "pass"},
        {"username": "performance_glitch_user", "password": "secret_sauce",  "expected_result": "pass"},
        {"username": "",                        "password": "secret_sauce",  "expected_result": "fail"},
        {"username": "standard_user",           "password": "",              "expected_result": "fail"},
    ]


class TestDataDrivenLogin:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser)
        self.inventory  = InventoryPage(browser)
        self.login_page.navigate()

    @pytest.mark.datadriven
    @pytest.mark.parametrize("row", load_login_data())
    def test_login_with_data(self, row):
        username = str(row.get("username") or "")
        password = str(row.get("password") or "")
        expected = str(row.get("expected_result", "pass")).lower().strip()
        self.login_page.login(username, password)
        if expected == "pass":
            self.login_page.wait_for_url_to_contain("inventory")
            assert "inventory.html" in self.login_page.get_current_url()
            self.inventory.logout()
        else:
            assert self.login_page.is_error_displayed()
