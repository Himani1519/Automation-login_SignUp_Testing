from selenium.webdriver.common.by import By
from csv import DictReader

# Mainatin a sperate class for locators

class MainPageLocators(object):
   

    EMAIL_PATH = (By.ID, 'username')
    PASSWORD_PATH = (By.ID,'password')
    LOGIN_BUTTON = (By.CLASS_NAME,'MuiButton-label')
    CONTINUE_BUTTON = (By.ID, 'checkPhoneNumber')
    INVALID_LOGIN_MSG = (By.XPATH, '//p[contains(text(),"Your authentication information is incorrect. Please try again.")]')
    ERROR_MSG_ON_EMPTY_PASSWORD = (By.ID, 'password-helper-text')
    ERROR_MSG_ON_EMPTY_EMAIL = (By.ID, 'username-helper-text')
    FORGOT_PASSWORD = (By.XPATH, '//p[contains(text(),"Forgot password?")]')
    SEND_OTP = (By.CLASS_NAME,'MuiButton-label')
    FIRSTNAME = (By.ID,'firstName')
    LASTNAME = (By.ID,'lastName')
    EMAIL = (By.ID,'email')
    MOBILE = (By.ID,'mobile')
    PASSWORD = (By.ID,'password-1')
    CONFIRM_PASSWORD = (By.ID,'password-2')
    SIGNUP = (By.CLASS_NAME,'MuiButton-label')
    ACCOUNT_CREATE = (By.XPATH,'//p[contains(text(),"New Account? Sign Up!")]')
    SIGN_IN_PAGE = (By.XPATH,'//h1[contains(text(),"Create an Account")]')
    ERROR_MSG_ON_DIFFERENT_PASSWORD = (By.ID,'password-2-helper-text')
    ERROR_MSG_ON_EMPTY_FIRSTNAME = (By.ID,'firstName-helper-text')
    ERROR_MSG_ON_EMPTY_LASTNAME = (By.ID,'firstName-helper-text')
    ERROR_MSG_ON_EMPTY_MOBILENO = (By.ID,'mobile-helper-text')
    ERROR_MSG_ON_EMPTY_EMAILID = (By.ID,'email-helper-text')

   