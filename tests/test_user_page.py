import allure

from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.user_page import UserPage


class TestUserPage:
    @allure.title('Проверка перехода в личный кабинет, выход из аккаунта')
    def test_login(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        user_page = UserPage(driver)

        main_page.click_login_btn()
        login_page.user_login()
        main_page.click_account_btn()
        user_page.click_history_btn()
        user_page.click_logout_btn()
        login_page.assert_forgot_page()
