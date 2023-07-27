from .Util import Util, Framework
import requests
import random
import string

class Test:
    def startTest(self):
        test_name = "Register_001 (API)"
        user_email = Framework.generateEmail()
        user_password = "1234567890"

        url = Util.REGISTER_API_URL
        data = Util.REGISTER_API_PAYLOAD
        data["email"] = user_email
        data["password"] = user_password
        data["passwordRepeat"] = user_password

        request = requests.post(url, json=data)
        status_code = request.status_code

        if status_code == 201:
            print("=================================================")
            print("New user created successfully")
            print("Credentials used:")
            print(f"    User email: {user_email}")
            print(f"    User password: {user_password}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(True, f"[✔] ({test_name}) User created successfully, test passed.")
        else:
            print("=================================================")
            print(f"Unable to create a new user using the URL: {url}")
            print(f"Status code: {status_code}")
            print(f"Data dictionary used: {data}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(False, f"[✖] ({test_name}) Unable to create a new user, test failed.")