"""tests/test_actions.py -- ActionChains demonstrations.
Covers: hover, right-click, double-click, drag-drop, keyboard shortcuts.
"""
import pytest
from selenium.webdriver.common.by          import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys        import Keys
from framework.base_page import BasePage

BASE = "https://the-internet.herokuapp.com"


class TestActionChains:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver  = browser
        self.page    = BasePage(browser)
        self.actions = ActionChains(browser)

    def test_hover_reveals_caption(self):
        self.driver.get(f"{BASE}/hovers")
        figs = self.driver.find_elements(By.CLASS_NAME, "figure")
        self.actions.move_to_element(figs[0]).perform()
        caption = figs[0].find_element(By.CLASS_NAME, "figcaption")
        assert caption.is_displayed()

    def test_right_click_opens_context_menu(self):
        self.driver.get(f"{BASE}/context_menu")
        box = self.driver.find_element(By.ID, "hot-spot")
        self.actions.context_click(box).perform()
        text = self.page.accept_alert()
        assert "context menu" in text.lower()

    def test_double_click(self):
        self.driver.get(f"{BASE}/double_click")
        btn = self.driver.find_element(By.ID, "double-click")
        self.actions.double_click(btn).perform()
        assert self.driver.find_element(By.ID, "message").is_displayed()

    def test_drag_and_drop(self):
        self.driver.get(f"{BASE}/drag_and_drop")
        src = self.driver.find_element(By.ID, "column-a")
        tgt = self.driver.find_element(By.ID, "column-b")
        orig = src.find_element(By.TAG_NAME, "header").text
        self.actions.drag_and_drop(src, tgt).perform()
        after = self.driver.find_element(By.ID, "column-a").find_element(By.TAG_NAME, "header").text
        assert after != orig

    def test_keyboard_ctrl_a(self):
        self.driver.get(f"{BASE}/key_presses")
        inp = self.driver.find_element(By.ID, "target")
        inp.send_keys("Hello World")
        self.actions.click(inp).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        assert self.driver.find_element(By.ID, "result").is_displayed()
