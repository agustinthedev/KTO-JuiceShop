import random
import string

def getReturnData(passed, message):
    data = {}
    data["passed"] = passed
    data["message"] = message

    return data

def generateEmail():
        email = ''
        for x in range(12):
            email+=''.join(random.choice(string.ascii_lowercase))

        return email + "@gmail.com"