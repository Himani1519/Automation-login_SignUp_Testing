import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains


class TestSignInPage(BaseTest):
  
    # create account with already used details
    def test_signIn_with_Already_createdAccount(self):
        print("\n" + str(test_cases(13)))
        page = MainPage(self.driver)
        time.sleep(10)
        click_createAccount = page.check_accountSignIn()
        enter_firstname = page.enter_validFirstName()
        enter_lastname = page.enter_validLastName()
        enter_mobileno = page.enter_validMobileNo()
        enter_emailId = page.enter_alreadyUsed_emailID()
        enter_password = page.enter_alreadyUsed_password()
        enter_confirmPassword = page.enter_alredayUsedConfirmPassword()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        SignInPage_url = self.driver.current_url
        assert SignInPage_url == 'https://staging-auth.azent.com/signup'

    # pass invalid mobileNo and invalid emailID
    def test_signIn_InvalidDetails(self):
        print("\n" + str(test_cases(14)))
        page = MainPage(self.driver)
        click_createAccount = page.check_accountSignIn()
        time.sleep(10)
        enter_mobileno = page.enter_invalid_mobileno()
        enter_emailId = page.enter_invalid_EmailID()
        enter_firstname = page.enter_validFirstName()
        time.sleep(10)
        enter_lastname = page.enter_validLastName()
        enter_password = page.enter_validPassword()
        enter_confirmPassword = page.enter_validConfirmPassword()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        SignInPage_url = self.driver.current_url
        assert SignInPage_url == 'https://staging-auth.azent.com/signup'

    # Pass two different password in confirm password and password and rest details are unique
    def test_signIn_InvalidDetails_1(self):
        print("\n" + str(test_cases(15)))
        page = MainPage(self.driver)
        time.sleep(10)
        click_createAccount = page.check_accountSignIn()
        enter_firstname = page.enter_validFirstName()
        enter_lastname = page.enter_validLastName()
        enter_mobileno = page.enter_validMobileNo()
        enter_emailId = page.enter_validEmailID()
        enter_password = page.enter_validPassword()
        enter_confirmPassword = page.enter_inavlid_confirm_Password()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        error_msgOn_confirmPassword = page.check_msg_differntPassword()
        assert error_msgOn_confirmPassword == "Your Passwords Don't Match"
        SignInPage_url = self.driver.current_url
        assert SignInPage_url == 'https://staging-auth.azent.com/signup'

    # create account passing all details as empty
    def test_signIn_InvalidDetails_2(self):
        print("\n" + str(test_cases(16)))
        page = MainPage(self.driver)
        time.sleep(10)
        click_createAccount = page.check_accountSignIn()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        SignInPage_url = self.driver.current_url
        error_msgOn_emptyLastname = page.check_msg_emptyFirstName()
        assert error_msgOn_emptyLastname == 'Please Enter Your First Name'
        error_msgOn_emptyLastname = page.check_msg_emptyLastName()
        assert error_msgOn_emptyLastname == 'Please Enter Your Last Name'
        error_msgOn_emptyEmailID = page.check_msg_onEmptyEmail()
        assert error_msgOn_emptyEmailID == 'Please Enter Your Email'
        error_msgOn_MobileNO = page.check_msg_emptyMobileno()
        assert error_msgOn_MobileNO == 'Please Enter Your Phone Number'
        error_msgOn_emptyPassword = page.check_msg_onEmptyPassword()
        assert error_msgOn_emptyPassword == 'Please Enter Your New Password'
        assert SignInPage_url == 'https://staging-auth.azent.com/signup'



    # create account passing lastname as empty
    def test_signIn_InvalidDetails_2(self):
        print("\n" + str(test_cases(17)))
        page = MainPage(self.driver)
        time.sleep(10)
        click_createAccount = page.check_accountSignIn()
        enter_firstname = page.enter_validFirstName()
        enter_mobileno = page.enter_validMobileNo()
        enter_emailId = page.enter_validEmailID()
        enter_password = page.enter_validPassword()
        enter_confirmPassword = page.enter_validConfirmPassword()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        SignInPage_url = self.driver.current_url
        Error_msg_on_EmptyLastName = page.check_msg_emptyLastName()
        assert Error_msg_on_EmptyLastName == "Please Enter Your Last Name"
        assert SignInPage_url == 'https://staging-auth.azent.com/signup'

    # create account passing special characters in firstName and lastName
    def test_signIn_InvalidDetails_2(self):
        print("\n" + str(test_cases(18)))
        page = MainPage(self.driver)
        time.sleep(10)
        click_createAccount = page.check_accountSignIn()
        enter_firstname = page.enter_validFirstName()
        enter_mobileno = page.enter_validMobileNo()
        enter_emailId = page.enter_validEmailID()
        enter_password = page.enter_validPassword()
        enter_confirmPassword = page.enter_validConfirmPassword()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        SignInPage_url = self.driver.current_url
        assert SignInPage_url == 'https://staging-auth.azent.com/signup'


    # create account passing special characters in mobileno
    def test_signIn_InvalidDetails_2(self):
        print("\n" + str(test_cases(19)))
        page = MainPage(self.driver)
        time.sleep(10)
        click_createAccount = page.check_accountSignIn()
        enter_firstname = page.enter_validFirstName()
        enter_mobileno = page.enter_specialChracterInMobileNo()
        enter_emailId = page.enter_validEmailID()
        enter_password = page.enter_validPassword()
        enter_confirmPassword = page.enter_validConfirmPassword()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        SignInPage_url = self.driver.current_url
        assert SignInPage_url == 'https://staging-auth.azent.com/signup'
    
    # create account with valid Details
    def test_signIn_with_validDetails(self):
        print("\n" + str(test_cases(20)))
        page = MainPage(self.driver)
        time.sleep(10)
        click_createAccount = page.check_accountSignIn()
        enter_firstname = page.enter_validFirstName()
        enter_lastname = page.enter_validLastName()
        enter_mobileno = page.enter_validMobileNo()
        enter_emailId = page.enter_validEmailID()
        enter_password = page.enter_validPassword()
        enter_confirmPassword = page.enter_validConfirmPassword()
        click_signIn = page.click_signInButton()
        time.sleep(10)
        SignInPage_url = self.driver.current_url
        assert SignInPage_url != 'https://staging-auth.azent.com/signup'
        


        