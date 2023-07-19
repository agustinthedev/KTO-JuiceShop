from selenium import webdriver
from selenium.webdriver.common.by import By
from Util import Util
from time import sleep

class Test:
    browser = ""

    def openBrowser(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)

    def startTest(self):
        url = Util.REGISTER_SITE_URL
        self.openBrowser(url)
        sleep(10)


test = Test()
test.startTest()