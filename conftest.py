import os
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import WebDriverException

from data import Urls


@pytest.fixture(scope='function')
def driver():
    browser = os.getenv('BROWSER', 'firefox').lower()

    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")

        try:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        except WebDriverException:
            # Устанавливаем драйвер, если не удалось запустить
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        except WebDriverException:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get(Urls.main_page)

    yield driver
    driver.quit()
