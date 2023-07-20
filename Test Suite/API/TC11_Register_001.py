from Util import Util
import requests
import random
import string

class Test:
    def generateEmail(self):
        email = ''
        for x in range(12):
            email+=''.join(random.choice(string.ascii_lowercase))

        return email + "@gmail.com"
    
    def startTest(self):
        user_email = self.generateEmail()
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

            return True
        else:
            print("=================================================")
            print(f"Unable to create a new user using the URL: {url}")
            print(f"Status code: {status_code}")
            print(f"Data dictionary used: {data}")
            print("Stopping test.")
            print("=================================================")

            return False
    
test = Test()
test.startTest()