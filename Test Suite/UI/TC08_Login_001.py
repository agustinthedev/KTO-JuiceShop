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
        fr.log(f"Starting execution for test: {test_name}")

        # Open browser and navigate to Register url
        url = Util.LOGIN_SITE_URL
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

        request = requests.post(register_url, json=register_data)
        status_code = request.status_code

        if status_code == 200 or status_code == 201:
            fr.log("Account created successfully using API, trying to log in.")

            # Click Dismiss button
            fr.log("Clicking Dismiss button")
            try:
                self.browser.find_element(By.XPATH, Util.DISMISS_BUTTON_XPATH).click()
            except Exception:
                pass

            # Identify email input and write user email
            fr.log("Writing into email field")
            self.browser.find_element(By.XPATH, Util.LOGIN_EMAIL_INPUT_XPATH).send_keys(user_email)

            # Identify password input and write user password
            fr.log("Writing into password field")
            self.browser.find_element(By.XPATH, Util.LOGIN_PASSWD_INPUT_XPATH).send_keys(user_password)

            # Identify and click the Submit button
            sleep(2)
            fr.log("Clicking Log In button")
            self.browser.find_element(By.XPATH, Util.LOGIN_SUBMIT_BUTTON_XPATH).click()

            # Get current URL after clicking the Submit button. If URL is home page, login was successful
            sleep(3)
            current_url = self.browser.current_url

            if current_url == "https://juice-shop.herokuapp.com/#/search":
                fr.log("Test was able to log into the account correctly, test passed.")
                fr.log("Credentials used:")
                fr.log(f"    User email: {user_email}")
                fr.log(f"    User password: {user_password}")
                fr.log("Stopping test.")
                fr.log("====================================================================")

                return fr.getReturnData(True, f"[✔] ({test_name}) Test was able to log into the account correctly, test passed.")
            else:
                fr.log("Test wasn't able to log into the account created, test failed.")
                fr.log("Credentials used:")
                fr.log(f"    User email: {user_email}")
                fr.log(f"    User password: {user_password}")
                fr.log("Stopping test.")
                fr.log("====================================================================")

                return fr.getReturnData(False, f"[✖] ({test_name}) Test wasn't able to log into the account created, test failed.")

        else:
            fr.log("Unable to create a brand new account using API, test failed.")
            fr.log("Stopping test.")
            fr.log("====================================================================")

            return fr.getReturnData(False, f"[✖] ({test_name}) Unable to create a brand new account using API, test failed.")

test = Test()
test.startTest()