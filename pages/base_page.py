import time

from selenium.common import ElementClickInterceptedException, UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        try:
            self.driver.find_element(*locator).click()
        except ElementClickInterceptedException:
            # Прокрутите страницу до элемента
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(3)  # небольшая пауза после прокрутки
            element.click()
        except UnexpectedAlertPresentException:
            # Обработка всплывающего окна, если оно появилось
            alert = self.driver.switch_to.alert
            alert.dismiss()  # или alert.accept(), в зависимости от ситуации
            self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    def set_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def scroll(self, locator):
        element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_url(self):
        return self.driver.current_url

    def wait_navigating_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
