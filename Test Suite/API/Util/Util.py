REGISTER_API_URL = "https://juice-shop.herokuapp.com/api/Users/"
REGISTER_API_PAYLOAD = {
  "email": "",
  "password": "",
  "passwordRepeat": "",
  "securityQuestion": {
    "id": 1,
    "question": "Your eldest siblings middle name?",
    "createdAt": "2023-07-19T16:46:36.489Z",
    "updatedAt": "2023-07-19T16:46:36.489Z"
  },
  "securityAnswer": "123123"
}

LOGIN_API_URL = "https://juice-shop.herokuapp.com/rest/user/login"
LOGIN_API_PAYLOAD = {
    "email": "",
    "password": ""
}