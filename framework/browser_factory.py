"""
framework/browser_factory.py
Factory class for creating WebDriver instances.
Supports Chrome, Firefox, Edge with optional headless execution.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service  import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service    import Service as EdgeService
from webdriver_manager.chrome    import ChromeDriverManager
from webdriver_manager.firefox   import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from framework.logger import get_logger

logger = get_logger(__name__)


class BrowserFactory:
    """Factory for Chrome, Firefox, and Edge WebDriver instances."""

    @staticmethod
    def get_driver(browser: str = "chrome", headless: bool = False):
        browser = browser.lower().strip()
        logger.info(f"Launching: {browser} | headless={headless}")
        if browser == "chrome":
            return BrowserFactory._chrome(headless)
        elif browser == "firefox":
            return BrowserFactory._firefox(headless)
        elif browser == "edge":
            return BrowserFactory._edge(headless)
        raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def _chrome(headless):
        opts = webdriver.ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-notifications")
        opts.add_argument("--no-sandbox")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

    @staticmethod
    def _firefox(headless):
        opts = webdriver.FirefoxOptions()
        if headless:
            opts.add_argument("--headless")
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)

    @staticmethod
    def _edge(headless):
        opts = webdriver.EdgeOptions()
        if headless:
            opts.add_argument("--headless=new")
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=opts)
