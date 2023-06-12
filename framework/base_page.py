"""
framework/base_page.py  v1.1 -- refactored with full docstrings and type hints
Base class inherited by every Page Object.
Centralises WebDriverWait and all common Selenium interactions.
"""
import os
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions     import TimeoutException, StaleElementReferenceException
from framework.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    """Parent class for all Page Objects. Tests never call driver directly."""

    BASE_URL        = "https://www.saucedemo.com"
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver  = driver
        self.wait    = WebDriverWait(driver, self.DEFAULT_TIMEOUT,
                                     ignored_exceptions=[StaleElementReferenceException])
        self.actions = ActionChains(driver)

    # -- Navigation --------------------------------------------------
    def open(self, path: str = "") -> None:
        """Navigate to BASE_URL + path."""
        self.driver.get(f"{self.BASE_URL}{path}")

    def get_current_url(self) -> str: return self.driver.current_url
    def get_title(self) -> str:       return self.driver.title
    def refresh(self) -> None:        self.driver.refresh()

    # -- Element finders (explicit waits) ----------------------------
    def find(self, locator: tuple):
        """Wait for element to be present in DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator: tuple):
        """Wait for element to be visible AND clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator: tuple) -> list:
        """Return all matching elements."""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    # -- Interactions ------------------------------------------------
    def click(self, locator: tuple) -> None:
        self.find_clickable(locator).click()

    def type_text(self, locator: tuple, text: str, clear_first: bool = True) -> None:
        el = self.find(locator)
        if clear_first: el.clear()
        el.send_keys(text)

    def get_text(self, locator: tuple) -> str:      return self.find(locator).text
    def get_attribute(self, locator, attr) -> str:  return self.find(locator).get_attribute(attr)

    def js_click(self, locator: tuple) -> None:
        """JavaScript click -- useful when element is obscured by overlay."""
        self.driver.execute_script("arguments[0].click();", self.find(locator))

    def scroll_to_element(self, locator: tuple) -> None:
        """Scroll element into view using JavaScript."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.find(locator))

    # -- State checks ------------------------------------------------
    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    # -- Wait helpers ------------------------------------------------
    def wait_for_url_to_contain(self, text: str, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_for_text_in_element(self, locator: tuple, text: str) -> None:
        self.wait.until(EC.text_to_be_present_in_element(locator, text))

    # -- Alerts ------------------------------------------------------
    def accept_alert(self) -> str:
        alert = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.alert_is_present())
        text = alert.text; alert.accept(); return text

    def dismiss_alert(self) -> str:
        alert = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.alert_is_present())
        text = alert.text; alert.dismiss(); return text

    def type_in_alert(self, text: str) -> None:
        alert = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.alert_is_present())
        alert.send_keys(text); alert.accept()

    # -- Frames & iFrames --------------------------------------------
    def switch_to_frame(self, locator: tuple) -> None:
        self.driver.switch_to.frame(self.find(locator))

    def switch_to_frame_by_index(self, index: int) -> None:
        self.driver.switch_to.frame(index)

    def switch_to_default_content(self) -> None:
        self.driver.switch_to.default_content()

    # -- Windows & Tabs ----------------------------------------------
    def get_window_handles(self) -> list:       return self.driver.window_handles
    def switch_to_new_window(self) -> None:
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window_and_switch_back(self) -> None:
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    # -- Screenshots -------------------------------------------------
    def take_screenshot(self, filename: str = "screenshot.png") -> str:
        path = os.path.join("reports", filename)
        self.driver.save_screenshot(path)
        return path
