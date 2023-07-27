from selenium import webdriver
from selenium.webdriver.common.by import By
from Util import Util
from time import sleep
import random
import string
from Util import Framework

class Test:
    browser = ""

    # Main structure for test
    def startTest(self):
        test_name = "Register_004 (UI)"

        # Initialize framework and log message
        fr = Framework.Framework()
        fr.log("====================================================================")
        fr.log(f"Starting execution for test: {test_name}")

        # Open browser and navigate to Register url
        url = Util.REGISTER_SITE_URL
        self.browser = fr.startBrowser(url)
        

        # Data that will be used to create the user
        user_email = fr.generateEmail()
        user_password = "1234567890"
        repeat_user_password = "123123123"
        
        # Try to click the 'Dismiss' button. If not able to, check if registration form element is present, if YES, continue, if NOT, stop test.
        try:
            dismiss_button = self.browser.find_element(By.XPATH, Util.DISMISS_BUTTON_XPATH)
            dismiss_button.click()

            fr.log("Clicking Dismiss button.")
        except Exception as e:
            fr.log("Unable to click Dismiss button. Identifying if other elements are present in order to continue or stop the test.")
            
            try:
                self.browser.find_element(By.XPATH, Util.REGISTRATION_FORM_DIV_XPATH)

                fr.log("Registration Form DIV element present, continuing.")
            except Exception as e:
                fr.log("Unable to find Registration Form DIV element, stopping the test.")
                
                return fr.getReturnData(False, f"[✖] ({test_name}) Unable to find Registration Form DIV element, stopping the test.")
        
        
        # Identify email input and write user email
        fr.log("Writing into email input field")
        email_input = self.browser.find_element(By.XPATH, Util.EMAIL_FIELD_XPATH).send_keys(user_email)
        
        # Identify password input and write user password
        fr.log("Writing into password field")
        passwd_input = self.browser.find_element(By.XPATH, Util.PASSWD_FIELD_XPATH).send_keys(user_password)

        # Identify repeat password input and write user password again
        fr.log("Writing into repeat password field")
        repeat_passwd_input = self.browser.find_element(By.XPATH, Util.REPEAT_PASSWD_FIELD_XPATH).send_keys(repeat_user_password)

        # Identify security questions element and click it so all options inside dropdown become clickable
        fr.log("Clicking security question element")
        security_question_element = self.browser.find_element(By.XPATH, Util.SECURITY_QUESTION_ELEMENT_XPATH).click()

        # Identify and click security answer option from dropdown
        fr.log("Clicking the first option for security questions")
        security_question_answers_array = self.browser.find_elements(By.XPATH, Util.SECURITY_QUESTION_ANSWERS_XPATH)[0].click()

        # Identify security question answer inpout and provide a valid response
        fr.log("Writing response of security question into field")
        security_question_answer_input = self.browser.find_element(By.XPATH, Util.SECURITY_QUESTION_ANSWER_XPATH).send_keys("Test valid response")

        # Identify and click the Submit button
        fr.log("Clicking submit button")
        submit_button = self.browser.find_element(By.XPATH, Util.SUBMIT_BUTTON_XPATH).click()

        # Get current URL after clicking the Submit button. If URL is login page, registration was successful
        sleep(3)
        current_url = self.browser.current_url

        if current_url == "https://juice-shop.herokuapp.com/#/login":
            fr.log("Test was able to create an account using non-matching passwords, test failed.")
            fr.log("Credentials used:")
            fr.log(f"    User email: {user_email}")
            fr.log(f"    User password: {user_password}")
            fr.log("Stopping test.")
            fr.log("====================================================================")

            return fr.getReturnData(False, f"[✖] ({test_name}) Test was able to create an account using non-matching passwords, test failed.")
        else:
            fr.log("Login page not reached, assuming no account was created using non-matching passwords, test passed.")
            fr.log("Stopping test.")
            fr.log("====================================================================")
            
            return fr.getReturnData(True, f"[✔] ({test_name}) Login page not reached, assuming no account was created using non-matching passwords, test passed.")