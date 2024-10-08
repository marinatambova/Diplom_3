import allure

from conftest import driver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from pages.reset_page import ResetPage
from data import DataResetPage


class TestRecoverPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить"')
    def test_navigate_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        reset_page = ForgotPage(driver)
        main_page.click_login_btn()
        login_page.click_reset_btn()
        reset_page.assert_forgot_page()

    @allure.title('Проверка ввода почты и нажатия по кнопке "Восстановить"')
    def test_input_and_click(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_page = ForgotPage(driver)
        reset_page = ResetPage(driver)
        main_page.click_login_btn()
        login_page.click_reset_btn()
        forgot_page.recover_password(DataResetPage.email)
        reset_page.assert_recover_page()

    @allure.title('Проверка клика по кнопке "Показать пароль"')
    def test_show_pass(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_page = ForgotPage(driver)
        reset_page = ResetPage(driver)
        main_page.click_login_btn()
        login_page.click_reset_btn()
        forgot_page.recover_password(DataResetPage.email)
        reset_page.click_show_password_icon()
        reset_page.check_password_field_highlighted()
