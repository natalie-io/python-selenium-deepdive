import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # instantiate a chrome options object so you can set the size and headless preference
        chromeOptions = Options()
        # chrome_options.add_argument("--headless")
        chromeOptions.add_argument("--window-size=1920x1080")
        # download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
        # current directory
        chromeDriver = os.getcwd() + "\\chromedriver.exe"
        # go to Google and click the I'm Feeling Lucky button
        self.driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path=chromeDriver)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

