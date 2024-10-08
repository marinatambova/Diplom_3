"""
Локаторы страницы восстановления пароля
"""
from selenium.webdriver.common.by import By


class ForgotPageLocators:
    """
    Локаторы элементов на странице "Забыл пароль"
    """
    LOGIN_BTN_PAGE = By.XPATH, "//button[normalize-space()='Войти в аккаунт']"
    EMAIL_FIELD = (By.XPATH, "//input[@type='text'][@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__') and contains(text(), 'Восстановить')]")
