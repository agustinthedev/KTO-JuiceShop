import random
import string
from datetime import datetime

# Creates a dictionary with the specified data, logs the message and returns the dictionary
def getReturnData(passed, message):
    data = {}
    data["passed"] = passed
    data["message"] = message
    
    log(message)

    return data

# Generates and returns a valid random 12-characters email each time it's called
def generateEmail():
        email = ''
        for x in range(12):
            email+=''.join(random.choice(string.ascii_lowercase))

        return email + "@gmail.com"

# Logs message to console and also appends it to logs.txt file
def log(text):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    message = f"{now} {text}"
    print(message)

    with open("logs.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")