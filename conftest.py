"""conftest.py -- Shared pytest fixtures."""
import pytest
from framework.browser_factory import BrowserFactory
from framework.logger import get_logger

logger = get_logger(__name__)

def pytest_addoption(parser):
    parser.addoption("--browser",  default="chrome")
    parser.addoption("--headless", action="store_true", default=False)

@pytest.fixture(scope="session")
def browser(request):
    b = request.config.getoption("--browser")
    h = request.config.getoption("--headless")
    logger.info(f"Session start | browser={b} headless={h}")
    driver = BrowserFactory.get_driver(browser=b, headless=h)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def reset_session(browser):
    browser.delete_all_cookies()
    yield
