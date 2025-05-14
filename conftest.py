"""conftest.py v2 -- supports --browser and --headless CLI flags."""
import pytest
from framework.browser_factory import BrowserFactory
from framework.logger import get_logger

logger = get_logger(__name__)

def pytest_addoption(parser):
    parser.addoption("--browser",  default="chrome", help="chrome | firefox | edge")
    parser.addoption("--headless", action="store_true", default=False)

@pytest.fixture(scope="session")
def browser(request):
    b = request.config.getoption("--browser")
    h = request.config.getoption("--headless")
    logger.info(f"=== Session Start | browser={b} headless={h} ===")
    driver = BrowserFactory.get_driver(browser=b, headless=h)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    logger.info("=== Session Complete -- closing browser ===")
    driver.quit()

@pytest.fixture(autouse=True)
def reset_session(browser):
    """Clear cookies before every test for a clean state."""
    browser.delete_all_cookies()
    yield

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com"
