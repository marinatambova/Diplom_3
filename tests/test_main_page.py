import allure

from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Переход по клику на "Конструктор"')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        main_page.is_constructor_page()

    @allure.title('Переход по клику на "Лента заказов"')
    def test_click_orders_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_feed_button()
        main_page.is_orders_feed_page()

    @allure.title('Тест на клик по ингредиенту')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.is_ingredient_popup_open()

    @allure.title('Тест закрытия модального окна')
    def test_close_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_ingredient_popup()
        main_page.close_ingredient_popup()
        main_page.is_ingredient_popup_close()

    @allure.title('Тест добавления ингредиента в заказ')
    def test_add_ingredient_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        main_page.check_price()

    @allure.title('Тест оформления заказа')
    def test_place_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_login_btn()
        login_page.user_login()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.is_order_placed()
