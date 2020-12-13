from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import *
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# Page objects are covered in this file
with open('data.csv', 'r') as read_obj: 
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        email = row['EMAIL']
        password = row['PASSWORD']
        invalid_password = row['INVALIDPASSWORD']
        invalid_email = row['INVALIDEMAIL']
        special_character = row['SPECIALCHARCTER']
        email_uppercase = row['EMAILUPPERCASE']
        password_uppercase = row['PASSWORDUPPERCASE']
        invalid_password_1 = row['INVALIDPASSWORD_1']
        valid_firstname = row['VALID_FIRSTNAME']
        valid_lastname = row['VALID_LASTNAME']
        valid_mobileno = row['VALID_MOBILENO']
        valid_emailId = row['VALID_EMAILID']
        valid_password = row['VALID_PASSWORD']
        valid_confirmPassword = row['VALID_CONFIRMPASSWORD']
        invalid_mobileno = row['INVALID_MOBILENO']
        invalid_emailId = row['INVALID_EMAILID']
        invalid_password = row['INVALID_PASSWORD']
        specialCharacter_MobileNo = row['INVALID_MOBILENO_1']

class MainPage(BasePage):
 
    
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  

    def enter_mailid(self):
        self.find_element(*self.locator.EMAIL_PATH).send_keys(email)

    def enter_password(self):
        self.find_element(*self.locator.PASSWORD_PATH).send_keys(password)

        time.sleep(5)

    def click_login_button(self):
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()


    def enter_invalidEmailId(self):
        self.find_element(*self.locator.EMAIL_PATH).send_keys(invalid_email)

    def enter_invalidPassword(self):
        self.find_element(*self.locator.PASSWORD_PATH).send_keys(invalid_password)

    def enter_uppercasePassword(self):
        self.find_element(*self.locator.EMAIL_PATH).send_keys(password_uppercase)

    def enter_uppercaseEmail(self):
        self.find_element(*self.locator.EMAIL_PATH).send_keys(email_uppercase)

    def enter_specialCharacterIn_email(self):
        self.find_element(*self.locator.EMAIL_PATH).send_keys(special_character)

    def enter_specialCharactersIn_password(self):
        self.find_element(*self.locator.EMAIL_PATH).send_keys(special_character)

    
    def enter_invalidPassword_1(self):
        self.find_element(*self.locator.EMAIL_PATH).send_keys(invalid_password_1)


    def check_msg_invalidLogin(self):
        return self.find_element(*self.locator.INVALID_LOGIN_MSG).text

    def check_msg_onEmptyPassword(self):
        return self.find_element(*self.locator.ERROR_MSG_ON_EMPTY_PASSWORD).text


    def check_msg_onEmptyEmail(self):
        return self.find_element(*self.locator.ERROR_MSG_ON_EMPTY_EMAIL).text

    def check_forgotPassword_functionality(self):
        self.find_element(*self.locator.FORGOT_PASSWORD).click()

    def check_sendOTP(self):
        self.find_element(*self.locator.SEND_OTP).click()

    def check_accountSignIn(self):
        self.find_element(*self.locator.ACCOUNT_CREATE).click()


    def enter_validFirstName(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.FIRSTNAME).send_keys(valid_firstname)
    
    def enter_validLastName(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.LASTNAME).send_keys(valid_lastname)


    def enter_validMobileNo(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.MOBILE).send_keys(valid_mobileno)


    def enter_validEmailID(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.EMAIL).send_keys(valid_emailId)


    def enter_validPassword(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.PASSWORD).send_keys(valid_password)

    def enter_validConfirmPassword(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.CONFIRM_PASSWORD).send_keys(valid_confirmPassword)

    def click_signInButton(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.SIGNUP).click()


    def enter_alreadyUsed_emailID(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.EMAIL).send_keys(email)


    def enter_alreadyUsed_password(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def enter_alredayUsedConfirmPassword(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.CONFIRM_PASSWORD).send_keys(password)

    def Sign_In_Page(self):
        return self.find_element(*self.locator.SIGN_IN_PAGE).text

    def enter_invalid_mobileno(self):
        self.find_element(*self.locator.MOBILE).send_keys(invalid_mobileno)


    def enter_invalid_EmailID(self):
        self.find_element(*self.locator.EMAIL).send_keys(invalid_emailId)

    def enter_inavlid_confirm_Password(self):
        self.find_element(*self.locator.CONFIRM_PASSWORD).send_keys(invalid_password)

    def enter_specialCharcaterFirstName(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.FIRSTNAME).send_keys(special_character)
    
    def enter_specialCharacterLastname(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.LASTNAME).send_keys(special_character)

    def enter_specialChracterInMobileNo(self):
        self.driver.implicitly_wait(4)
        self.find_element(*self.locator.MOBILE).send_keys(specialCharacter_MobileNo)


    def check_msg_emptyFirstName(self):
        return self.find_element(*self.locator.ERROR_MSG_ON_EMPTY_FIRSTNAME).text

    def check_msg_emptyLastName(self):
        return self.find_element(*self.locator.ERROR_MSG_ON_EMPTY_LASTNAME).text

    def check_msg_emptyMobileno(self):
        return self.find_element(*self.locator.ERROR_MSG_ON_EMPTY_MOBILENO).text


    def check_msg_emptyEmail(self):
        return self.find_element(*self.locator.ERROR_MSG_ON_EMPTY_EMAIL).text

    def check_msg_differntPassword(self):
        return self.find_element(*self.locator.ERROR_MSG_ON_DIFFERENT_PASSWORD).text
    


    
