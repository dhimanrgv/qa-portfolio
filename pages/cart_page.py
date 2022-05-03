"""pages/cart_page.py -- Page Object for SauceDemo shopping cart."""
from selenium.webdriver.common.by import By
from framework.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS      = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES      = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES     = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITIES = (By.CLASS_NAME, "cart_quantity")
    REMOVE_BUTTONS  = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_BTN    = (By.ID, "continue-shopping")

    def navigate(self):              self.open("/cart.html")
    def get_item_names(self):        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]
    def get_item_count(self):        return len(self.driver.find_elements(*self.CART_ITEMS))
    def get_item_quantity(self, i=0):
        return int(self.driver.find_elements(*self.ITEM_QUANTITIES)[i].text)
    def remove_item(self, i=0):
        self.driver.find_elements(*self.REMOVE_BUTTONS)[i].click()
    def proceed_to_checkout(self):   self.click(self.CHECKOUT_BUTTON)
    def continue_shopping(self):     self.click(self.CONTINUE_BTN)
