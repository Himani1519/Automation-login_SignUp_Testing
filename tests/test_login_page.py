import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains


class TestLoginPage(BaseTest):
    # login with validPassword and invalid Email
    def test_loginPage_validpassword_invalidEmail(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        Pass_username = page.enter_invalidEmailId()
        time.sleep(10)
        Pass_password = page.enter_password()
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'

    # login with invalid password and valid email
    def test_loginPage_Invalidpassword_validEmail(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        Pass_username = page.enter_mailid()
        time.sleep(10)
        Pass_password = page.enter_invalidPassword()
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'


    # login with valid email and password in uppercase
    def test_loginPage_UppercasePassword_uppercaseEmail(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        Pass_username = page.enter_uppercaseEmail()
        time.sleep(10)
        Pass_password = page.enter_uppercasePassword()
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'

    # login with special characters in password
    def test_loginPage_specialCharacterIn_Password(self):
        print("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        Pass_username = page.enter_uppercaseEmail()
        time.sleep(10)
        Pass_password = page.enter_specialCharactersIn_password()
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'

    # login with special characters in email
    def test_loginPage_specialCharacterIn_email(self):
        print("\n" + str(test_cases(4)))
        page = MainPage(self.driver)
        Pass_username = page.enter_specialCharacterIn_email()
        time.sleep(10)
        Pass_password = page.enter_password()
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'


    # login with invalid password
    def test_loginPage_invalidPassword(self):
        print("\n" + str(test_cases(5)))
        page = MainPage(self.driver)
        Pass_username = page.enter_mailid()
        time.sleep(10)
        Pass_password = page.enter_invalidPassword_1()
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'


    # login wittout passing email and password
    def test_loginPage_passing_empty_Value(self):
        print("\n" + str(test_cases(6)))
        page = MainPage(self.driver)
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'


    # verify the invalid login msg
    def test_invalid_msg(self):
        print("\n" + str(test_cases(7)))
        page = MainPage(self.driver)
        Pass_username = page.enter_mailid()
        time.sleep(10)
        Pass_password = page.enter_invalidPassword()
        Click_login = page.click_login_button()
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'
        time.sleep(10)
        error_msg = page.check_msg_invalidLogin()
        assert error_msg == "Your authentication information is incorrect. Please try again."

    # login with password only
    def test_loginWith_enterPasswordOnly(self):
        print("\n" + str(test_cases(8)))
        page = MainPage(self.driver)
        Pass_password = page.enter_password()
        Click_login = page.click_login_button()
        time.sleep(10)
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'
        time.sleep(4)
        email_error_msg = page.check_msg_onEmptyEmail()
        assert email_error_msg == "Please Enter Your Email / Phone Number"

    # login with email only
    def test_loginWith_enterEmailOnly(self):
        print("\n" + str(test_cases(9)))
        page = MainPage(self.driver)
        Pass_password = page.enter_mailid()
        Click_login = page.click_login_button()
        time.sleep(10)
        LoginPage_url = self.driver.current_url
        assert LoginPage_url == 'https://staging-auth.azent.com/login'
        password_error_msg = page.check_msg_onEmptyPassword()
        assert password_error_msg == "Please Enter Your Password"

    # check forgot password functionality
    def test_forgotPassword(self):
        print("\n" + str(test_cases(10)))
        page = MainPage(self.driver)
        time.sleep(10)
        forgot_password = page.check_forgotPassword_functionality()    
        time.sleep(10)

    # check if send otp is working
    def test_send_otp(self):
        print("\n" + str(test_cases(11)))
        page = MainPage(self.driver)
        time.sleep(10)
        forgot_password = page.check_forgotPassword_functionality()   
        Pass_username = page.enter_mailid()
        time.sleep(10) 
        send_otp_onMail = page.check_sendOTP()
        time.sleep(5)

    # login with valid credentials
    def test_loginPage_validpassword_validEmail(self):
        print("\n" + str(test_cases(12)))
        page = MainPage(self.driver)
        Pass_username = page.enter_mailid()
        time.sleep(10)
        Pass_password = page.enter_password()
        Click_login = page.click_login_button()
        time.sleep(5)
        HomePage_url = self.driver.current_url
        assert HomePage_url == 'https://staging-website.azent.com/'


        