import pytest
import time
import allure
from locators.locators import MainPageLocators, LogInLocators
from pages.phptravels.login_page import LogInPage
from tests.Login_Tests import conftest
from utils import functions

@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Login with valid data test")
    @allure.description("This is test of login with valid data")
    def test_login_passed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open()
        log_in_page.set_user_inputs("yhalbjzfkc@myinfoinc.com", "SuperAdmin@123")
        assert functions.wait_for_element_to_visible(self.driver,*MainPageLocators.profile_image)
        log_in_page.logout()
        time.sleep(2)
        assert self.driver.find_element(*LogInLocators.login_button).is_displayed()

    @allure.title("Login with invalid email test")
    @allure.description("This is test of login with invalid email")
    def test_login_failed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open()
        log_in_page.set_user_inputs("admin@domain.com", "wrong_pass")
        
        alert_err_toaster = self.driver.find_element(
            *LogInLocators.invalid_data_msg)
        assert functions.wait_for_element_to_visible(self.driver,*LogInLocators.invalid_data_msg)
        
        error_msg = "Either email or username is incorrect"
        assert error_msg in alert_err_toaster.text
