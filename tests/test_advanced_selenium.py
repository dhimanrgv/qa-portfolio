"""tests/test_advanced_selenium.py -- Advanced Selenium techniques.
Target: https://the-internet.herokuapp.com
Covers: JS Alerts, Frames/iFrames, Multiple Windows/Tabs.
"""
import pytest
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from framework.base_page import BasePage

BASE = "https://the-internet.herokuapp.com"


class TestAlerts:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.page = BasePage(browser)

    def test_simple_alert_accept(self):
        self.page.driver.get(f"{BASE}/javascript_alerts")
        self.page.click((By.XPATH, "//button[text()='Click for JS Alert']"))
        text = self.page.accept_alert()
        assert "I am a JS Alert" in text

    def test_confirm_alert_accept(self):
        self.page.driver.get(f"{BASE}/javascript_alerts")
        self.page.click((By.XPATH, "//button[text()='Click for JS Confirm']"))
        self.page.accept_alert()
        assert "Ok" in self.page.get_text((By.ID, "result"))

    def test_confirm_alert_dismiss(self):
        self.page.driver.get(f"{BASE}/javascript_alerts")
        self.page.click((By.XPATH, "//button[text()='Click for JS Confirm']"))
        self.page.dismiss_alert()
        assert "Cancel" in self.page.get_text((By.ID, "result"))

    def test_prompt_alert_with_input(self):
        self.page.driver.get(f"{BASE}/javascript_alerts")
        self.page.click((By.XPATH, "//button[text()='Click for JS Prompt']"))
        self.page.type_in_alert("QA Test Input")
        assert "QA Test Input" in self.page.get_text((By.ID, "result"))


class TestFrames:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.page = BasePage(browser)

    def test_switch_to_iframe_and_type(self):
        self.page.driver.get(f"{BASE}/iframe")
        self.page.switch_to_frame((By.ID, "mce_0_ifr"))
        body = self.page.find((By.ID, "tinymce"))
        body.clear(); body.send_keys("Typed inside iFrame")
        assert body.text == "Typed inside iFrame"
        self.page.switch_to_default_content()

    def test_return_to_default_after_frame(self):
        self.page.driver.get(f"{BASE}/iframe")
        self.page.switch_to_frame((By.ID, "mce_0_ifr"))
        self.page.switch_to_default_content()
        assert self.page.is_visible((By.TAG_NAME, "h3"))

    def test_nested_frames(self):
        self.page.driver.get(f"{BASE}/nested_frames")
        self.page.switch_to_frame_by_index(0)
        self.page.switch_to_frame((By.XPATH, "//frame[@name='frame-left']"))
        assert "LEFT" in self.page.get_text((By.TAG_NAME, "body"))
        self.page.switch_to_default_content()


class TestWindows:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.page = BasePage(browser)

    def test_open_new_window_and_switch(self):
        self.page.driver.get(f"{BASE}/windows")
        original = self.page.driver.current_window_handle
        self.page.click((By.LINK_TEXT, "Click Here"))
        WebDriverWait(self.page.driver, 10).until(EC.number_of_windows_to_be(2))
        self.page.switch_to_new_window()
        assert "New Window" in self.page.driver.title
        self.page.close_current_window_and_switch_back()
