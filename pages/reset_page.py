import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Urls, TIME_WAIT
from locators.reset_page_locators import ResetPageLocators
from pages.base_page import BasePage


class ResetPage(BasePage):
    @allure.step('Проверка ссылки "Восстановление пароля"')
    def assert_recover_page(self):
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.reset_page))

    @allure.step('Клик по иконке "Показать пароль"')
    def click_show_password_icon(self):
        self.click_to_element(ResetPageLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка, что поле пароля активно и подсвечено')
    def check_password_field_highlighted(self):
        # Явное ожидание для подтверждения добавления к элементу
        password_field_container = WebDriverWait(self.driver, TIME_WAIT).until(
            EC.presence_of_element_located(ResetPageLocators.PASSWORD_FIELD_CONTAINER)
        )
        assert "input__placeholder-focused" in password_field_container.get_attribute(
            "class")
