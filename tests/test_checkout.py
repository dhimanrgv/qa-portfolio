"""tests/test_checkout.py -- Checkout flow test suite."""
import pytest
from pages.login_page     import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page      import CartPage
from pages.checkout_page  import CheckoutPage
from utils.test_data      import Users, Messages, CheckoutInfo


class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.co = CheckoutPage(browser)
        lg = LoginPage(browser); inv = InventoryPage(browser); cart = CartPage(browser)
        lg.navigate(); lg.login(**Users.STANDARD); lg.wait_for_url_to_contain("inventory")
        inv.add_item_to_cart(0); inv.go_to_cart(); cart.proceed_to_checkout()
        self.co.wait_for_url_to_contain("checkout-step-one")

    @pytest.mark.negative
    def test_empty_firstname_shows_error(self):
        self.co.fill_info("", "Smith", "12345"); self.co.click_continue()
        assert Messages.FIRST_NAME_REQ in self.co.get_error_message()

    @pytest.mark.negative
    def test_empty_lastname_shows_error(self):
        self.co.fill_info("John", "", "12345"); self.co.click_continue()
        assert Messages.LAST_NAME_REQ in self.co.get_error_message()

    @pytest.mark.negative
    def test_empty_zipcode_shows_error(self):
        self.co.fill_info("John", "Smith", ""); self.co.click_continue()
        assert Messages.POSTAL_CODE_REQ in self.co.get_error_message()

    def test_valid_info_proceeds_to_step_two(self):
        self.co.fill_info(**CheckoutInfo.VALID); self.co.click_continue()
        self.co.wait_for_url_to_contain("checkout-step-two")

    def test_order_summary_shows_item_total(self):
        self.co.fill_info(**CheckoutInfo.VALID); self.co.click_continue()
        assert "$" in self.co.get_item_total()

    @pytest.mark.smoke
    def test_complete_order_shows_confirmation(self):
        self.co.fill_info(**CheckoutInfo.VALID); self.co.click_continue(); self.co.click_finish()
        self.co.wait_for_url_to_contain("checkout-complete")
        assert Messages.ORDER_CONFIRMED in self.co.get_confirmation_header()

    def test_cancel_returns_to_inventory(self):
        self.co.click_cancel(); self.co.wait_for_url_to_contain("inventory")
