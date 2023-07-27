from Util import Util, Framework
import requests
import random
import string

class Test:
    def startTest(self):
        test_name = "Register_006 (API)"
        user_email = ""
        user_password = "123123"

        url = Util.REGISTER_API_URL
        data = Util.REGISTER_API_PAYLOAD
        data["email"] = user_email
        data["password"] = user_password
        data["passwordRepeat"] = user_password

        request = requests.post(url, json=data)
        status_code = request.status_code

        if status_code == 201 or status_code == 200:
            print("=================================================")
            print("It was possible to create a new user using empty email field, test failed.")
            print("Credentials used:")
            print(f"    User email: {user_email}")
            print(f"    User password: {user_password}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(False, f"[✖] ({test_name}) It was possible to create a new user using empty email field, test failed.")
        else:
            print("=================================================")
            print(f"Unable to create a new user using empty email field, test passed.")
            print(f"Status code: {status_code} || Request URL: {url}")
            print("Credentials used:")
            print(f"    User email: {user_email}")
            print(f"    User password: {user_password}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(True, f"[✔] ({test_name}) Unable to create a new user using empty email field, test passed.")
        
test = Test()
test.startTest()