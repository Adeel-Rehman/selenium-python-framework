import pytest
import allure

from pages.Arbitr.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("Home page - smoke test")
    @allure.description("Check if home page of Arbitr has correct title & is showing username and password fields")
    def test_homepage_title(self):
        homepage = HomePage(self.driver)
        homepage.open()
        assert("Arbitr" in homepage.get_page_title())
        assert("/login" in homepage.get_page_URL())
