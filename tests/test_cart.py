"""tests/test_cart.py -- Cart page test suite."""
import pytest
from pages.login_page     import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page      import CartPage
from utils.test_data      import Users


class TestCart:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.cart = CartPage(browser)
        lg = LoginPage(browser); inv = InventoryPage(browser)
        lg.navigate(); lg.login(**Users.STANDARD); lg.wait_for_url_to_contain("inventory")
        inv.add_item_to_cart(0); inv.go_to_cart(); lg.wait_for_url_to_contain("cart")

    def test_cart_contains_one_item(self):    assert self.cart.get_item_count() == 1
    def test_cart_item_name_not_empty(self):  assert self.cart.get_item_names()[0] != ""
    def test_cart_item_quantity_is_one(self): assert self.cart.get_item_quantity(0) == 1
    def test_remove_item_empties_cart(self):
        self.cart.remove_item(0); assert self.cart.get_item_count() == 0
    def test_checkout_button_navigates(self):
        self.cart.proceed_to_checkout(); self.cart.wait_for_url_to_contain("checkout-step-one")
    def test_continue_shopping_returns_to_inventory(self):
        self.cart.continue_shopping(); self.cart.wait_for_url_to_contain("inventory")
