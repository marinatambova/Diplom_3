from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from locators.forgot_page_locators import ForgotPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class ForgotPage(BasePage):
    @allure.step('Проверка ссылки "Забыли пароль"')
    def assert_forgot_page(self):
        assert WebDriverWait(self.driver, 10).until(EC.url_to_be(Urls.recover_page))

    @allure.step('Ввод email')
    def enter_email(self, email):
        email_field = self.driver.find_element(*ForgotPageLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    @allure.step('Клик по кнопке восстановить')
    def click_recover_button(self):
        recover_button = self.driver.find_element(*ForgotPageLocators.RECOVER_BUTTON)
        recover_button.click()

    @allure.step('Восстановление пароля для email')
    def recover_password(self, email):
        self.enter_email(email)
        self.click_recover_button()
