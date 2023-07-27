from Util import Util, Framework
import requests
import random
import string

class Test:
    def startTest(self):
        test_name = "Register_002 (API)"
        user_email = "test123@example"
        user_password = "1234567890"

        url = Util.REGISTER_API_URL
        data = Util.REGISTER_API_PAYLOAD
        data["email"] = user_email
        data["password"] = user_password
        data["passwordRepeat"] = user_password

        request = requests.post(url, json=data)
        status_code = request.status_code

        if status_code == 201 or status_code == 200:
            print("=================================================")
            print("It was possible to create a new user using an invalid email address.")
            print("Credentials used:")
            print(f"    User email: {user_email}")
            print(f"    User password: {user_password}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(False, f"[✖] ({test_name}) User created successfully using invalid email address, test failed.")
        else:
            print("=================================================")
            print(f"Unable to create a new user using the URL: {url}.")
            print(f"Status code: {status_code}")
            print("Credentials used:")
            print(f"    User email: {user_email}")
            print(f"    User password: {user_password}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(True, f"[✔] ({test_name}) Unable to create a new user using invalid email address, test passed.")
        
test = Test()
test.startTest()