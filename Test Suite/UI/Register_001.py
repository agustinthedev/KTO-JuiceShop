from selenium import webdriver
from selenium.webdriver.common.by import By
from Util import Util
from time import sleep
import random
import string

class Test:
    browser = ""

    def openBrowser(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        sleep(3)

    def generateEmail(self):
        email = ''
        for x in range(12):
            email+=''.join(random.choice(string.ascii_lowercase))

        return email + "@gmail.com"

    def startTest(self):
        url = Util.REGISTER_SITE_URL
        self.openBrowser(url)

        user_email = self.generateEmail()
        user_password = "1234567890"
        
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
        
        email_input = self.browser.find_element(By.XPATH, Util.EMAIL_FIELD_XPATH)
        email_input.send_keys(user_email)

        passwd_input = self.browser.find_element(By.XPATH, Util.PASSWD_FIELD_XPATH)
        passwd_input.send_keys(user_password)

        repeat_passwd_input = self.browser.find_element(By.XPATH, Util.REPEAT_PASSWD_FIELD_XPATH)
        repeat_passwd_input.send_keys(user_password)

        security_question_element = self.browser.find_element(By.XPATH, Util.SECURITY_QUESTION_ELEMENT_XPATH)
        security_question_element.click()
        sleep(2)

        security_question_answers_array = self.browser.find_elements(By.XPATH, Util.SECURITY_QUESTION_ANSWERS_XPATH)
        security_question_answers_array[0].click()

        security_question_answer_input = self.browser.find_element(By.XPATH, Util.SECURITY_QUESTION_ANSWER_XPATH)
        security_question_answer_input.send_keys("Test valid response")

        sleep(2)
        submit_button = self.browser.find_element(By.XPATH, Util.SUBMIT_BUTTON_XPATH)
        submit_button.click()
        sleep(2)

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


test = Test()
test.startTest()