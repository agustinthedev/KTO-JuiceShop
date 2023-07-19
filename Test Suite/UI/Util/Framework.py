from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

class Framework:

    browser = ""

    def __init__(self):
        pass

    def startBrowser(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        return self.browser

    def generateEmail(self):
        pass

    def findElement(self, xpath):
        pass

    def clickElement(self, xpath):
        pass