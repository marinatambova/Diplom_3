"""
Локаторы страницы восстановления пароля
"""
from selenium.webdriver.common.by import By


class ResetPageLocators:
    """
    Локаторы элементов на странице восстановления пароля
    """
    LOGIN_BTN_PAGE = By.XPATH, "//button[normalize-space()='Войти в аккаунт']"
    PASSWORD_FIELD = By.CSS_SELECTOR, "input[type='password'][name='Введите новый пароль']"
    SHOW_PASSWORD_ICON = By.CSS_SELECTOR, "div.input__icon.input__icon-action"
    PASSWORD_FIELD_CONTAINER = By.CLASS_NAME, "input__placeholder"
