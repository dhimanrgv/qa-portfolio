"""tests/test_inventory.py -- Inventory page test suite."""
import pytest
from pages.login_page     import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data      import Users, Products


class TestInventory:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.inv = InventoryPage(browser)
        lg = LoginPage(browser); lg.navigate(); lg.login(**Users.STANDARD)
        lg.wait_for_url_to_contain("inventory")

    def test_six_products_displayed(self):
        assert self.inv.get_product_count() == Products.TOTAL_COUNT

    def test_all_prices_positive(self):
        assert all(p > 0 for p in self.inv.get_all_prices())

    def test_sort_a_to_z(self):
        self.inv.sort_products("az")
        n = self.inv.get_all_product_names()
        assert n == sorted(n)

    def test_sort_z_to_a(self):
        self.inv.sort_products("za")
        n = self.inv.get_all_product_names()
        assert n == sorted(n, reverse=True)

    def test_sort_price_low_to_high(self):
        self.inv.sort_products("lohi")
        p = self.inv.get_all_prices()
        assert p == sorted(p)

    def test_sort_price_high_to_low(self):
        self.inv.sort_products("hilo")
        p = self.inv.get_all_prices()
        assert p == sorted(p, reverse=True)

    def test_add_one_item_updates_badge(self):
        self.inv.add_item_to_cart(0)
        assert self.inv.get_cart_count() == 1

    def test_add_all_items_updates_badge(self):
        self.inv.add_all_items_to_cart()
        assert self.inv.get_cart_count() == 6
