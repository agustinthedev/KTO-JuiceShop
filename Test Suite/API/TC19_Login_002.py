from Util import Util, Framework
import requests
import random
import string

class Test:
    def startTest(self):
        test_name = "Login_001 (API)"
        user_email = "justatest@testest.net"
        user_password = "1234567890"

        url = Util.LOGIN_API_URL
        data = Util.LOGIN_API_PAYLOAD
        data["email"] = user_email
        data["password"] = user_password

        request = requests.post(url, json=data)
        status_code = request.status_code

        if status_code == 201 or status_code == 200:
            print("=================================================")
            print(f"It was possible to log in using a non-existent email, test failed.")
            print(f"    User email: {user_email}")
            print(f"    User password: {user_password}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(False, f"[✖] ({test_name}) It was possible to log in using a non-existent email, test failed.")

        else:
            print("=================================================")
            print(f"Unable to log in using a non-existent email, test passed.")
            print(f"Status code: {status_code} || Request URL: {url}")
            print(f"Data dictionary used: {data}")
            print("Stopping test.")
            print("=================================================")

            return Framework.getReturnData(True, f"[✔] ({test_name}) Unable to log in using a non-existent email, test passed.")
    
test = Test()
test.startTest()