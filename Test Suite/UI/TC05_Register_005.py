from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Util import Util
from Util import Framework

class Test:
    test_name = ""
    browser = ""

    def __startBrowser__(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        sleep(3)

    def startTest(self):
        # Initialize framework and log message
        fr = Framework.Framework()
        fr.log("====================================================================")
        fr.log(f"Starting execution for test: {self.test_name}")