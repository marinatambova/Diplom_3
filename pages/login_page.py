import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import UserData, TIME_WAIT, Urls
from locators.login_page_locators import LoginPageLocators as LL
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_reset_btn(self):
        self.click_to_element(LL.RESET_BTN_PAGE)

    @allure.step('Авторизация пользователя')
    def user_login(self):
        # Заполнение формы авторизации и вход
        email, password = UserData.email, UserData.password

        email_input = WebDriverWait(self.driver, TIME_WAIT).until(
            EC.visibility_of_element_located(LL.EMAIL_FIELD)
        )
        email_input.send_keys(email)
        password_input = WebDriverWait(self.driver, TIME_WAIT).until(
            EC.visibility_of_element_located(LL.PASSWORD_FIELD)
        )
        password_input.send_keys(password)
        submit_button = self.driver.find_element(*LL.LOGIN_BUTTON)
        submit_button.click()

    @allure.step('Проверка ссылки "Логин"')
    def assert_forgot_page(self):
        assert WebDriverWait(self.driver, 10).until(EC.url_to_be(Urls.login_page))
