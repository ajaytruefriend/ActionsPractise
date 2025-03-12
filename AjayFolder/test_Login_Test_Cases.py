import pytest

from PageObjects.HomePage import Home_Page


@pytest.mark.usefixtures("driver")
class TestLoginCases:
    @pytest.mark.regression
    def test_TC01_login_with_valid_username_and_password(self,driver):
        homepage=Home_Page(driver)
        homepage.enter_username('problem_user')
        homepage.enter_password('secret_sauce')
        homepage.click_on_login_button()
        actual_title = driver.title
        assert actual_title == 'Swag Labs', f"title is not matching: actual title is {actual_title} expected title is 'Swag Labs'"
        print(f"TC passed {actual_title} = Swag Labs")

    @pytest.mark.parametrize("username,password,error_message",
                             [("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out."),
                              ("invalid_user","secret_sauce","Epic sadface: Username and password do not match any user in this service")])
    def test_TC02_login_with__Invalid_username_and__Invalid_password(self,driver,username,password,error_message):
        homepage=Home_Page(driver)
        homepage.enter_username(username)
        homepage.enter_password(password)
        homepage.click_on_login_button()
        actual_error_message=homepage.verify_error_message()
        assert actual_error_message == error_message, f"TC failed {actual_error_message} != {error_message}"
        print(f"TC passed {actual_error_message} = '{error_message}'")
