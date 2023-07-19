from selenium import webdriver
from selenium.webdriver.common.by import By
from Util import Util
from time import sleep

class Test:
    browser = ""

    def openBrowser(self, url):
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        sleep(3)

    def startTest(self):
        url = Util.REGISTER_SITE_URL
        self.openBrowser(url)
        
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

        sleep(10)


test = Test()
test.startTest()