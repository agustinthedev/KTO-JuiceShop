from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import random
import string

class Framework:

    browser = ""

    def __init__(self):
        pass

    def log(self, text):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        message = f"{now} {text}"
        print(message)

        with open("logs.txt", "a") as file:
            file.write(message + "\n")

    
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