from base.page_base import PageBase
import allure


class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title
    
    @allure.step("Getting URL of the page")
    def get_page_URL(self):
        return self.driver.current_url
