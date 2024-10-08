import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.user_page_locators import UserPageLocators
from pages.base_page import BasePage


class UserPage(BasePage):
    @allure.step('Переход в раздел "История заказов"')
    def click_history_btn(self):
        self.click_to_element(UserPageLocators.ORDER_HISTORY_BLOCK)

    @allure.step('Выход из аккаунта')
    def click_logout_btn(self):
        self.click_to_element(UserPageLocators.LOGOUT_BUTTON)

    @allure.step('Получение заказов')
    def get_ids(self):

        # Ожидаем появления элементов на странице
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(UserPageLocators.ORDERS)
        )

        order_element = self.driver.find_element(*UserPageLocators.ORDERS)
        return order_element.text
