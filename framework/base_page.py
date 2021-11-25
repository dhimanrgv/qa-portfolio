"""
framework/base_page.py  v1.0
Base class inherited by every Page Object.
Centralises WebDriverWait and all common Selenium interactions.
"""
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support     import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions     import TimeoutException, StaleElementReferenceException
from framework.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    BASE_URL        = "https://www.saucedemo.com"
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver  = driver
        self.wait    = WebDriverWait(driver, self.DEFAULT_TIMEOUT,
                                     ignored_exceptions=[StaleElementReferenceException])
        self.actions = ActionChains(driver)

    def open(self, path=""):
        self.driver.get(f"{self.BASE_URL}{path}")

    def get_current_url(self):   return self.driver.current_url
    def get_title(self):         return self.driver.title

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text, clear_first=True):
        el = self.find(locator)
        if clear_first: el.clear()
        el.send_keys(text)

    def get_text(self, locator):       return self.find(locator).text
    def get_attribute(self, locator, attr): return self.find(locator).get_attribute(attr)

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_url_to_contain(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def accept_alert(self):
        alert = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.alert_is_present())
        text  = alert.text; alert.accept(); return text

    def dismiss_alert(self):
        alert = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.alert_is_present())
        text  = alert.text; alert.dismiss(); return text

    def type_in_alert(self, text):
        alert = WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(EC.alert_is_present())
        alert.send_keys(text); alert.accept()

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(self.find(locator))

    def switch_to_frame_by_index(self, index):
        self.driver.switch_to.frame(index)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_window_handles(self):      return self.driver.window_handles
    def switch_to_new_window(self):    self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def take_screenshot(self, filename="screenshot.png"):
        path = os.path.join("reports", filename)
        self.driver.save_screenshot(path); return path
