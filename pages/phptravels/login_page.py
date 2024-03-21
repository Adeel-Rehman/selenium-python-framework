import allure
from selenium.webdriver.common.keys import Keys
from locators.locators import LogInLocators
from base.page_base import PageBase
from selenium.webdriver.common.action_chains import ActionChains

from utils import functions 

class LogInPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Expanding profile menu")
    def expand_profile_menu(self):
        self.driver.find_element(*LogInLocators.user_profile_menu).click()

    @allure.step("Opening login page")
    def open_login_page(self):
        self.driver.get(*LogInLocators.login_link)

    @allure.step("Login with email: '1'")
    def set_user_inputs(self, email, password):
        self.driver.find_element(*LogInLocators.email_input).click()
        self.driver.find_element(*LogInLocators.email_input).send_keys(email)
        self.driver.find_element(*LogInLocators.password_input).click()
        self.driver.find_element(
            *LogInLocators.password_input).send_keys(password, Keys.ENTER)

    @allure.step("Logout")
    def logout(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*LogInLocators.user_profile_menu))
        hover.perform()
        logout_btn = self.driver.find_element(*LogInLocators.logout_link)
        self.driver.execute_script("arguments[0].click();",logout_btn)
        # functions.wait_for_element_to_visible(self.driver,logout_btn)
        # logout_btn.click()
