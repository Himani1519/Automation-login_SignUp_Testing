import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import sys
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

class BaseTest(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')  
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome(executable_path= r'/home/himani/Documents/python-webui-testing/tests/chrome/chromedriver_linux64 (2)/chromedriver')
       
        # self.driver = webdriver.Firefox()
        self.driver.get("https://staging-auth.azent.com/login")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)
