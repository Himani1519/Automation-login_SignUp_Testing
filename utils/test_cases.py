# seperate class for test cases in array


def test_cases(number):
    return testCases[number]


testCases = [
    # [test case no, description]
    ['Test_Case1', 'In Login page, ogin with validPassword and invalid Email'],
    ['Test_Case2', 'In Login page, login with invalid password and valid email'],
    ['Test_Case3', 'In Login page, login with valid email and password in uppercase'],
    ['Test_Case4', 'In Login page, login with special characters in password'],
    ['Test_Case5', 'In Login page, login with special characters in email'],
    ['Test_Case6', 'In Login page, login with invalid password'],
    ['Test_Case7', 'In Login page , login wittout passing email and password '],
    ['Test_Case8', 'In Login page,  verify the invalid login msg'],
    ['Test_Case9', 'In Login page, login with password only'],
    ['Test_Case10', 'In Login page, login with email only'],
    ['Test_Case11', 'In Login page, check forgot password functionality'],
    ['Test_Case12', 'In Login page, check if send otp is working'],
    ['Test_Case13', 'In Login page, login with valid credentials'],
    ['Test_Case14', 'In SignIn page , create account with already used details'],
    ['Test_Case15', 'In SignIn page , pass invalid mobileNo and invalid emailID'],
    ['Test_Case16', 'In SignIn page , Pass two different password in confirm password and password and rest details are unique'],
    ['Test_Case17', 'In SignIn page , create account passing all details as empty'],
    ['Test_Case18', 'In SignIn page , create account passing lastname as empty'],
    ['Test_Case19', 'In SignIn page , create account passing special characters in firstName and lastName'],
    ['Test_Case20', 'In SignIn page , create account passing special characters in mobileno'],
    ['Test_Case21', 'In SignIn page , create account with valid Details'],


]
