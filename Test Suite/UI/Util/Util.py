REGISTER_SITE_URL = "https://juice-shop.herokuapp.com/#/register"
LOGIN_SITE_URL = "https://juice-shop.herokuapp.com/#/login"

DISMISS_BUTTON_XPATH = "//span[text()='Dismiss']"
REGISTRATION_FORM_DIV_XPATH = "//div[@id='registration-form']"

EMAIL_FIELD_XPATH = "//input[@id='emailControl']"
PASSWD_FIELD_XPATH = "//input[@id='passwordControl']"
REPEAT_PASSWD_FIELD_XPATH = "//input[@id='repeatPasswordControl']"
SHOW_PASSWD_ADVICE_XPATH = "//input[@id='mat-slide-toggle-1-input']"

SECURITY_QUESTION_ELEMENT_XPATH = "//*[@name='securityQuestion']"
SECURITY_QUESTION_ANSWERS_XPATH = "//span[@class='mat-option-text']"

SECURITY_QUESTION_ANSWER_XPATH = "//input[@id='securityAnswerControl']"

'''
0: Your eldest sibling middle name?
1: Mother's maiden name?
2: Mother's birth date? (MM/DD/YY)
3: Father's birth date? (MM/DD/YY)
4: Maternal grandmother's first name?
5: Paternal grandmother's first name?
6: Name of your favorite pet?
7: Last name of dentist when you were a teenager?
8: Your ZIP/Postal code when you were a teenager?
9: Company your first work for as an adult?
10: Your favorite book?
11: Your favorite movie?
12: Number of one of your customer or ID cards?
13: What's your favorite place to go hiking?

'''

SUBMIT_BUTTON_XPATH = "//button[@id='registerButton']"