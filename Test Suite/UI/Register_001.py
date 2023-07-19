from selenium import webdriver
from selenium.webdriver.common.by import By

class Test:
    browser = ""

    def openBrowser(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)

    def startTest(self):
        pass