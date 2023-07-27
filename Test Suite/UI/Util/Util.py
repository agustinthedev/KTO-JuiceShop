REGISTER_SITE_URL = "https://juice-shop.herokuapp.com/#/register"
LOGIN_SITE_URL = "https://juice-shop.herokuapp.com/#/login"


# REGISTER ITEMS
DISMISS_BUTTON_XPATH = "//span[text()='Dismiss']"
REGISTRATION_FORM_DIV_XPATH = "//div[@id='registration-form']"

EMAIL_FIELD_XPATH = "//input[@id='emailControl']"
PASSWD_FIELD_XPATH = "//input[@id='passwordControl']"
REPEAT_PASSWD_FIELD_XPATH = "//input[@id='repeatPasswordControl']"
SHOW_PASSWD_ADVICE_XPATH = "//input[@id='mat-slide-toggle-1-input']"

SECURITY_QUESTION_ELEMENT_XPATH = "//*[@name='securityQuestion']"
SECURITY_QUESTION_ANSWERS_XPATH = "//span[@class='mat-option-text']"

SECURITY_QUESTION_ANSWER_XPATH = "//input[@id='securityAnswerControl']"

SUBMIT_BUTTON_XPATH = "//button[@id='registerButton']"

# LOGIN ITEMS
LOGIN_EMAIL_INPUT_XPATH = "//input[@id='email']"
LOGIN_PASSWD_INPUT_XPATH = "//input[@id='password']"

LOGIN_SUBMIT_BUTTON_XPATH = "//button[@id='loginButton']"

# API ITEMS

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