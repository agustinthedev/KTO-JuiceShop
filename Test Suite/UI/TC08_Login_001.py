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
        fr.log("Creating account in order to be used to verify log in.")
        register_url = Util.REGISTER_API_URL
        register_data = Util.REGISTER_API_PAYLOAD

        register_data["email"] = user_email
        register_data["password"] = user_password

        request = requests.post(url, json=register_data)
        status_code = request.status_code

        if status_code == 200 or status_code == 201:
            pass
        else:
            fr.log("Unable to create a brand new account using API, test failed.")
            fr.log("Stopping test.")
            fr.log("====================================================================")

            return fr.getReturnData(True, f"[✖] ({test_name}) Unable to create a brand new account using API, test failed.")
