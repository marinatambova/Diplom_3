import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TIME_WAIT, Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Авторизация')
    def click_login_btn(self):
        self.click_to_element(MainPageLocators.GO_LOGIN)

    @allure.step('Клик на кнопку "Личный кабинет" в шапке главной')
    def click_account_btn(self):
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Клик на "Конструктор"')
    def click_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на "Лента заказов"')
    def click_orders_feed_button(self):
        self.click_to_element(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT)

    @allure.step('Проверка открытия попапа с деталями ингредиента')
    def is_ingredient_popup_open(self):
        assert self.find_element(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Проверка закрытия попапа с деталями ингредиента')
    def is_ingredient_popup_close(self):
        elements = self.driver.find_elements(*MainPageLocators.INGREDIENT_DETAILS_POPUP)
        assert len(elements) == 0

    @allure.step('Открытие попапа с ингредиентом')
    def open_ingredient_popup(self):
        self.click_ingredient()

    @allure.step('Закрытие попапа с ингредиентом')
    def close_ingredient_popup(self):
        self.click_to_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step('Закрытие попапа с заказом')
    def close_check_popup(self):
        self.click_to_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        source_element = self.find_element(MainPageLocators.BREAD_CSS)
        target_element = self.find_element(MainPageLocators.TARGET_CSS)

        # ActionChains некорректно работает с перетаскиванием элементов
        f = open("./scripts/drag_and_drop.js", "r")
        javascript = f.read()
        f.close()
        self.driver.execute_script(javascript, source_element, target_element)

    @allure.step('Оформление заказа')
    def place_order(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Проверка успешного оформления заказа')
    def is_order_placed(self):
        assert self.find_element(MainPageLocators.ORDER_SUCCESS_POPUP).is_displayed()

    @allure.step('Проверка, что открыта страница "Конструктор"')
    def is_constructor_page(self):
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.main_page))

    @allure.step('Проверка, что открыта страница "Лента заказов"')
    def is_orders_feed_page(self):
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.feed_page))

    @allure.step('Получение id заказа')
    def get_feed_id(self):
        """Возвращает текст заголовка модального окна."""
        # Ожидаем, пока текст элемента не станет равен "9999"
        WebDriverWait(self.driver, 30).until(
            lambda driver: driver.find_element(*MainPageLocators.MODAL_TITLE_CSS_SELECTOR).text != "9999"
        )
        # Возвращаем текст элемента после выполнения условия ожидания
        modal_title_element = self.driver.find_element(*MainPageLocators.MODAL_TITLE_CSS_SELECTOR)
        return modal_title_element.text

    @allure.step('Проверка, что изменилась цена')
    def check_price(self):
        count_element = self.find_element(MainPageLocators.COUNTER_CSS)
        count_text = count_element.text
        assert count_text != "0"
