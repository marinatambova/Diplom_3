"""
Локаторы страницы пользователя
"""
from selenium.webdriver.common.by import By


class UserPageLocators:
    """
    Локаторы элементов на странице пользователя
    """
    ORDER_HISTORY_BLOCK = By.XPATH, "//a[contains(text(), 'История заказов')]"
    LOGOUT_BUTTON = By.XPATH, "//button[contains(text(), 'Выход')]"
    ORDERS = By.CLASS_NAME, 'text_type_digits-default'
