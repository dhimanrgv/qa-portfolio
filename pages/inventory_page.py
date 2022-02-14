"""pages/inventory_page.py -- Page Object for SauceDemo inventory page."""
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.ui  import Select
from framework.base_page import BasePage


class InventoryPage(BasePage):
    PRODUCT_TITLE       = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS       = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES       = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES      = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN       = (By.CLASS_NAME, "product_sort_container")
    CART_ICON           = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE          = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    BURGER_MENU         = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK         = (By.ID, "logout_sidebar_link")

    def navigate(self):          self.open("/inventory.html")
    def get_page_title(self):    return self.get_text(self.PRODUCT_TITLE)
    def get_product_count(self): return len(self.driver.find_elements(*self.PRODUCT_ITEMS))
    def get_all_product_names(self):
        return [el.text for el in self.find_all(self.PRODUCT_NAMES)]
    def get_all_prices(self):
        return [float(el.text.replace("$","")) for el in self.find_all(self.PRODUCT_PRICES)]
    def sort_products(self, option):
        Select(self.find(self.SORT_DROPDOWN)).select_by_value(option)
    def add_item_to_cart(self, index=0):
        self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)[index].click()
    def add_all_items_to_cart(self):
        for btn in self.driver.find_elements(*self.ADD_TO_CART_BUTTONS): btn.click()
    def get_cart_count(self):
        return int(self.get_text(self.CART_BADGE)) if self.is_visible(self.CART_BADGE, 3) else 0
    def go_to_cart(self):        self.click(self.CART_ICON)
    def logout(self):
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)
