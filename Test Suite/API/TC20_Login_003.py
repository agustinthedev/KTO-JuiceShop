from .Util import Util, Framework
import requests
import random
import string

class Test:
    def startTest(self):
        test_name = "Login_003 (API)"
        user_email = Framework.generateEmail()
        user_password = "1234567890"

        url = Util.REGISTER_API_URL
        data = Util.REGISTER_API_PAYLOAD
        data["email"] = user_email
        data["password"] = user_password
        data["passwordRepeat"] = user_password

        request = requests.post(url, json=data)
        status_code = request.status_code

        if status_code == 201 or status_code == 200:
            print(f"Brand new user created successfully, proceeding to use it to log in.")

            login_url = Util.LOGIN_API_URL
            login_data = Util.LOGIN_API_PAYLOAD

            login_data["email"] = user_email
            login_data["password"] = "wrongpassword123123"

            login_request = requests.post(login_url, json=login_data)
            login_status_code = login_request.status_code

            if login_status_code == 201 or login_status_code == 200:
                print("=================================================")
                print(f"It was possible to log in using an incorrect password, test failed.")
                print(f"    User email: {user_email}")
                print(f"    User password: {login_data['password']}")
                print("Stopping test.")
                print("=================================================")

                return Framework.getReturnData(False, f"[✖] ({test_name}) It was possible to log in using an incorrect password, test failed.")
            else:
                print("=================================================")
                print(f"Unable to log in using an incorrect password, test passed.")
                print(f"    User email: {user_email}")
                print(f"    User password: {login_data['password']}")
                print("Stopping test.")
                print("=================================================")

                return Framework.getReturnData(True, f"[✔] ({test_name}) Unable to log in using an incorrect password, test passed.")

        else:
            print("=================================================")
            print(f"Unable to create a new user using in order to use it in the test, test failed.")
            print(f"Status code: {status_code} || URL: {url}")
            print(f"Data dictionary used: {data}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(False, f"[✖] ({test_name}) Unable to create a new user using in order to use it in the test, test failed.")