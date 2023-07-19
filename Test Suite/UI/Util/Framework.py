from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
import string

class Framework:

    browser = ""

    def __init__(self):
        pass

    def log(self, text):
        print(text)
    
    # Function to start the browser in the desired URL.
    def startBrowser(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        sleep(3)
        return self.browser

    # Generate a valid 12 characters gmail email each time.
    def generateEmail(self):
        email = ''
        for x in range(12):
            email+=''.join(random.choice(string.ascii_lowercase))

        return email + "@gmail.com"

    def findElement(self, xpath):
        try:
            element = self.browser.find_element(By.XPATH)
            return True
        except Exception:
            return False

    def clickElement(self, xpath):
        try:
            element = self.browser.find_element(By.XPATH, xpath)
            element.click()

            return True
        except Exception as e:
            return str(e)
        
    def sendKeys(self, xpath, keys):
        element = self.findElement(xpath)
        if element:
            self.browser.find_element(By.XPATH, xpath).send_keys(keys)
            return True
        else:
            return False