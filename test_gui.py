from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

import unittest


# Setup
TEST_SYSTEM = "http://localhost:5000"
DRIVER_SERVICE = ChromiumService(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        )


class TestFlaskGui(unittest.TestCase):
    def setUp(self):
        """Create the webdriver"""
        driver_options = ChromiumOptions()
        driver_options.add_argument("--headless=new")
        self.driver = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                options=driver_options
                )
        self.driver.implicitly_wait(1)
        self.addCleanup(self.driver.quit)

    def test_sanity(self):
        """Assert that the app is accessible at the expected URL"""
        self.driver.get(TEST_SYSTEM)

    def test_givenAppHomepage_thenLinkToOrderReportExists(self):
        """Assert that a link to the Order report exists"""
        d = self.driver
        d.get(TEST_SYSTEM)

        # Assert that the link to the order report ends in 'report'
        order_report_link = d.find_element(by=By.LINK_TEXT,
                                           value="Order report")
        link_href_attr = order_report_link.get_attribute("href")
        self.assertTrue(link_href_attr.endswith("report"))


if __name__ == "__main__":
    unittest.main()
