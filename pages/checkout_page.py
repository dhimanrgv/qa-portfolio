"""pages/checkout_page.py -- Page Object for checkout flow."""
from selenium.webdriver.common.by import By
from framework.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME     = (By.ID, "first-name")
    LAST_NAME      = (By.ID, "last-name")
    POSTAL_CODE    = (By.ID, "postal-code")
    CONTINUE_BTN   = (By.ID, "continue")
    CANCEL_BTN     = (By.ID, "cancel")
    ERROR_MESSAGE  = (By.CSS_SELECTOR, "[data-test='error']")
    FINISH_BTN     = (By.ID, "finish")
    ITEM_TOTAL     = (By.CLASS_NAME, "summary_subtotal_label")
    CONFIRM_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN  = (By.ID, "back-to-products")

    def navigate_step_one(self):             self.open("/checkout-step-one.html")
    def fill_info(self, first, last, zip_code):
        self.type_text(self.FIRST_NAME,  first)
        self.type_text(self.LAST_NAME,   last)
        self.type_text(self.POSTAL_CODE, zip_code)
    def click_continue(self):                self.click(self.CONTINUE_BTN)
    def click_finish(self):                  self.click(self.FINISH_BTN)
    def click_cancel(self):                  self.click(self.CANCEL_BTN)
    def get_error_message(self):             return self.get_text(self.ERROR_MESSAGE)
    def is_error_displayed(self):            return self.is_visible(self.ERROR_MESSAGE)
    def get_item_total(self):                return self.get_text(self.ITEM_TOTAL)
    def get_confirmation_header(self):       return self.get_text(self.CONFIRM_HEADER)
    def go_back_home(self):                  self.click(self.BACK_HOME_BTN)
