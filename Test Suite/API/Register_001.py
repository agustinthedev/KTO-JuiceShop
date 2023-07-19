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
        url = Util.REGISTER_API_URL
        data = Util.REGISTER_API_PAYLOAD
        data["email"] = self.generateEmail()
        data["password"] = "1234567890"
        data["passwordRepeat"] = "1234567890"

        request = requests.post(url, json=data)
        print(request.status_code)
    
test = Test()
test.startTest()