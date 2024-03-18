from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# Setup
TEST_SYSTEM = "localhost:5000"
DRIVER_SERVICE = webdriver.FirefoxService()


class TestFlaskGui(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=DRIVER_SERVICE)
        self.driver.implicitly_wait(1)
        self.addCleanup(self.driver.quit)

    def test_sanity(self):
        """Assert that the app is accessible at the expected URL"""
        self.driver.get(TEST_SYSTEM)

    def test_givenAppHomepage_beforeUserTakesAction_thenDefaultGreeting(self):
        """Assert that homepage displays the default greeting"""
        d = self.driver
        d.get(TEST_SYSTEM)

        # Assert value of msg before user action
        message = d.find_element(by=By.ID, value="greeting")
        expected = "Hello there!"
        actual = message.text
        self.assertEqual(expected, actual)

    def test_givenAppHomepage_whenUserEntersName_thenIsGreeted(self):
        """Assert that greeting reflects a user's submitted name"""
        d = self.driver
        d.get(TEST_SYSTEM)

        # Get page elements
        name_input = d.find_element(by=By.NAME, value="name-input")
        submit_button = d.find_element(by=By.ID, value="name-submit")

        # Take action
        test_msg = "Test value with spaces"
        name_input.send_keys(test_msg)
        submit_button.click()

        # Assert value of msg after user interaction
        message = d.find_element(by=By.ID, value="greeting")
        expected = f"Hello {test_msg}!"
        actual = message.text
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()