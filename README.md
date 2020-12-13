# Azent Education automated test  

* This project can be used for automation testing of few scenarios on basis of Page Object Model

## Project Folder Structure


* **pages** - It contains base_page.py and main_page.py class.
base_page.py - This Base class is serving basic attributes for every single page inherited from page class, it includes basic functionality and intialization of driver.
main_page.py - All the page objects are covered in these file, it is derived from base_page class and conyains all methods to execute steps.

* **tests** - base_test.py, test_login_page.py and test_signIn_page.py contains actual tests, it uses the page class object to initiating drivers and functions to run tests.

* **utils** - locators.py - This class conatins all the locators to run the test.
test_cases.py - In these, class test cases description are written and utilizing them in test_login_page.py and test_signIn_page.py class as an array.

## Prerequisites

* Python 3
* Selenium
* Pytest
* unittest — Unit testing framework
* Chrome (Version 79)

## Installation and Usage

### *To run all tests*:
* python3 -m unittest 

### *To run a class*:
* python3 -m unittest tests.test_signIn_page

### *To run a method*:
* python3 -m unittest tests.test_signIn_page.TestSignInPage.test_signIn_InvalidDetails