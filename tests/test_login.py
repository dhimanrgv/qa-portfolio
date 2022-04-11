"""tests/test_login.py -- Login test suite."""
import pytest
from pages.login_page    import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data     import Users, Messages


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser)
        self.inventory  = InventoryPage(browser)
        self.login_page.navigate()

    @pytest.mark.smoke
    def test_valid_login_redirects_to_inventory(self):
        self.login_page.login(**Users.STANDARD)
        self.login_page.wait_for_url_to_contain("inventory")
        assert "inventory.html" in self.login_page.get_current_url()

    @pytest.mark.smoke
    def test_inventory_page_title_after_login(self):
        self.login_page.login(**Users.STANDARD)
        assert self.inventory.get_page_title() == "Products"

    @pytest.mark.negative
    def test_locked_out_user_shows_error(self):
        self.login_page.login(**Users.LOCKED_OUT)
        assert Messages.LOCKED_OUT_ERROR in self.login_page.get_error_message()

    @pytest.mark.negative
    def test_empty_username_shows_error(self):
        self.login_page.login(username="", password="secret_sauce")
        assert Messages.EMPTY_USER_ERROR in self.login_page.get_error_message()

    @pytest.mark.negative
    def test_empty_password_shows_error(self):
        self.login_page.login(username="standard_user", password="")
        assert Messages.EMPTY_PASS_ERROR in self.login_page.get_error_message()

    @pytest.mark.negative
    def test_wrong_password_shows_error(self):
        self.login_page.login(username="standard_user", password="wrongpass")
        assert self.login_page.is_error_displayed()

    def test_error_can_be_dismissed(self):
        self.login_page.login(**Users.LOCKED_OUT)
        self.login_page.dismiss_error()
        assert not self.login_page.is_error_displayed()

    def test_page_title_is_correct(self):
        assert "Swag Labs" in self.login_page.get_title()

    @pytest.mark.parametrize("creds", [Users.STANDARD, Users.PROBLEM, Users.PERFORMANCE])
    def test_multiple_valid_users_can_login(self, creds):
        self.login_page.navigate()
        self.login_page.login(**creds)
        self.login_page.wait_for_url_to_contain("inventory")
        assert "inventory.html" in self.login_page.get_current_url()
        self.inventory.logout()
