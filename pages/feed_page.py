import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TIME_WAIT, Urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Авторизация')
    def click_login_btn(self):
        self.click_to_element(FeedPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Клик на кнопку "Личный кабинет" в шапке главной')
    def click_account_btn(self):
        self.click_to_element(FeedPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Клик по ингредиенту')
    def click_order(self):
        self.click_to_element(FeedPageLocators.ORDER_CSS)

    @allure.step('Проверка открытия попапа с деталями ингредиента')
    def is_order_popup_open(self):
        assert self.find_element(FeedPageLocators.ORDER_DETAILS_POPUP).is_displayed()

    @allure.step('Проверка, что открыта страница "Конструктор"')
    def is_constructor_page(self):
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.main_page))

    @allure.step('Проверка, что открыта страница "Лента заказов"')
    def is_orders_feed_page(self):
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.feed_page))

    @allure.step('Получение количества всего')
    def count_all(self):
        """Возвращает количество заказов выполненных за все время."""
        all_time_orders_element = self.find_element(FeedPageLocators.ALL_TIME_ORDERS_XPATH)
        return int(all_time_orders_element.text)

    @allure.step('Получение количества за сегодня')
    def count_today(self):
        """Возвращает количество заказов выполненных за сегодня."""
        today_orders_element = self.find_element(FeedPageLocators.TODAY_ORDERS_XPATH)
        return int(today_orders_element.text)

    @allure.step('Получение списка заказов')
    def check_user_orders(self):
        """Возвращает список номеров заказов."""
        # Ожидаем появления элементов на странице
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.USER_ORDERS)
        )

        order_elements = self.driver.find_elements(*FeedPageLocators.USER_ORDERS)
        assert len(order_elements) != 0

    @allure.step('Получение заказа')
    def get_order(self):
        # Ожидаем появления элементов на странице
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDER)
        )

        order_elements = self.driver.find_element(*FeedPageLocators.ORDER)
        return order_elements.text

    @allure.step('Получение списка активных заказов')
    def get_order_numbers(self):
        """Возвращает список номеров заказов."""
        # Ожидаем появления элементов на странице
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDER_NUMBERS_CSS_SELECTOR)
        )

        order_elements = self.driver.find_elements(*FeedPageLocators.ORDER_NUMBERS_CSS_SELECTOR)
        return [element.text.replace('0', '') for element in order_elements]
