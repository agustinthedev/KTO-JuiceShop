from selenium import webdriver
from selenium.webdriver.common.by import By
from Util import Util
from time import sleep
import random
import string
from Util import Framework

class Test:
    browser = ""

    # Function to start the browser in the desired URL.
    def __startBrowser__(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        sleep(3)

    # Main structure for test
    def startTest(self):
        fr = Framework.Framework()

        # Open browser and navigate to Register url
        url = Util.REGISTER_SITE_URL
        self.__startBrowser__(url)
        

        # Data that will be used to create the user
        user_email = fr.generateEmail()
        user_password = "1234567890"
        
        # Try to click the 'Dismiss' button. If not able to, check if registration form element is present, if YES, continue, if NOT, stop test.
        try:
            dismiss_button = self.browser.find_element(By.XPATH, Util.DISMISS_BUTTON_XPATH)
            dismiss_button.click()

            print("Clicking Dismiss button.")
        except Exception as e:
            print("Unable to click Dismiss button. Identifying if other elements are present in order to continue or stop the test.")
            
            try:
                self.browser.find_element(By.XPATH, Util.REGISTRATION_FORM_DIV_XPATH)

                print("Registration Form DIV element present, continuing.")
            except Exception as e:
                print("Unable to find Registration Form DIV element, stopping the test.")
                return False
        
        
        # Identify email input and write user email
        email_input = self.browser.find_element(By.XPATH, Util.EMAIL_FIELD_XPATH)
        email_input.send_keys(user_email)
        
        # Identify password input and write user password
        passwd_input = self.browser.find_element(By.XPATH, Util.PASSWD_FIELD_XPATH)
        passwd_input.send_keys(user_password)

        # Identify repeat password input and write user password again
        repeat_passwd_input = self.browser.find_element(By.XPATH, Util.REPEAT_PASSWD_FIELD_XPATH)
        repeat_passwd_input.send_keys(user_password)

        # Identify security questions element and click it so all options inside dropdown become clickable
        security_question_element = self.browser.find_element(By.XPATH, Util.SECURITY_QUESTION_ELEMENT_XPATH)
        security_question_element.click()
        sleep(2)

        # Identify and click security answer option from dropdown
        security_question_answers_array = self.browser.find_elements(By.XPATH, Util.SECURITY_QUESTION_ANSWERS_XPATH)
        security_question_answers_array[0].click()

        # Identify security question answer inpout and provide a valid response
        security_question_answer_input = self.browser.find_element(By.XPATH, Util.SECURITY_QUESTION_ANSWER_XPATH)
        security_question_answer_input.send_keys("Test valid response")
        sleep(2)

        # Identify and click the Submit button
        submit_button = self.browser.find_element(By.XPATH, Util.SUBMIT_BUTTON_XPATH)
        submit_button.click()
        sleep(2)

        # Get current URL after clicking the Submit button. If URL is login page, registration was successful
        
        current_url = self.browser.current_url

        if current_url == "https://juice-shop.herokuapp.com/#/login":
            print("=======================================================================")
            print("Login page reached, registration was successful.")
            print("Credentials used:")
            print(f"    User email: {user_email}")
            print(f"    User password: {user_password}")
            print("Stopping test.")
            print("=======================================================================")
            return True
        else:
            print("=======================================================================")
            print("Login page not reached, issue detected.")
            print("Stopping test.")
            print("=======================================================================")
            return False
        

'''
TO DO: Remove calls
'''
test = Test()
test.startTest()