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

    # Generate a valid 12 characters gmail email each time.
    def generateEmail(self):
        email = ''
        for x in range(12):
            email+=''.join(random.choice(string.ascii_lowercase))

        return email + "@gmail.com"

    def findElement(self, xpath):
        pass

    def clickElement(self, xpath):
        pass