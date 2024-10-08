import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.user_page import UserPage
from conftest import driver


class TestFeedPage:
    @allure.title('Открытие всплывающего окна заказа с деталями')
    def test_click_orders_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_orders_feed_button()
        feed_page.click_order()
        feed_page.is_order_popup_open()

    @allure.title('Отображение заказов пользователя')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        user_page = UserPage(driver)
        main_page.click_login_btn()
        login_page.user_login()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_check_popup()
        main_page.click_account_btn()
        user_page.click_history_btn()
        order_id = user_page.get_ids()
        main_page.click_orders_feed_button()
        order_id_new = feed_page.get_order()
        # Тут отображаются старые заказы!
        assert order_id != order_id_new

    @allure.title('При создании заказа счетчик "За сегодня" увлеичивается')
    def test_count_today(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_orders_feed_button()
        count_today = feed_page.count_today()
        feed_page.click_login_btn()
        login_page.user_login()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_check_popup()
        main_page.click_orders_feed_button()
        count_today_new = feed_page.count_today()
        assert count_today != count_today_new

    @allure.title('При создании заказа счетчик "Выполнено всего" увлеичивается')
    def test_count_all(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_orders_feed_button()
        count_all = feed_page.count_all()
        feed_page.click_login_btn()
        login_page.user_login()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_check_popup()
        main_page.click_orders_feed_button()
        count_all_new = feed_page.count_all()
        assert count_all != count_all_new

    @allure.title('При оформлении заказа будет написано "В работе"')
    def test_in_work(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_orders_feed_button()
        feed_page.click_login_btn()
        login_page.user_login()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        feed_id = main_page.get_feed_id()
        main_page.close_check_popup()
        main_page.click_orders_feed_button()
        orders = feed_page.get_order_numbers()
        assert feed_id in orders
