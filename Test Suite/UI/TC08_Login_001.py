from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Util import Util
from Util import Framework
import requests

class Test:
    browser = ""

    def startTest(self):
        test_name = "Login_001 (UI)"

        # Initialize framework and log message
        fr = Framework.Framework()
        fr.log("====================================================================")
        fr.log(f"Starting execution for test: {self.test_name}")

        # Open browser and navigate to Register url
        url = Util.REGISTER_SITE_URL
        self.browser = fr.startBrowser(url)

        # Data that will be used to create the user
        user_email = fr.generateEmail()
        user_password = "123123"

        # Create a brand new account that will be used to log in