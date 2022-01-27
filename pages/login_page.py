"""pages/login_page.py -- Page Object for SauceDemo login screen."""
from selenium.webdriver.common.by import By
from framework.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT  = (By.ID, "user-name")
    PASSWORD_INPUT  = (By.ID, "password")
    LOGIN_BUTTON    = (By.ID, "login-button")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_CLOSE_BTN = (By.CSS_SELECTOR, ".error-button")

    def navigate(self):                    self.open("/")
    def enter_username(self, u):           self.type_text(self.USERNAME_INPUT, u)
    def enter_password(self, p):           self.type_text(self.PASSWORD_INPUT, p)
    def click_login(self):                 self.click(self.LOGIN_BUTTON)
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    def get_error_message(self):           return self.get_text(self.ERROR_MESSAGE)
    def is_error_displayed(self):          return self.is_visible(self.ERROR_MESSAGE)
    def dismiss_error(self):               self.click(self.ERROR_CLOSE_BTN)
