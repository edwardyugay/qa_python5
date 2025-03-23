# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser.lower() == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        driver_instance = webdriver.Chrome()
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Тип браузера: chrome или firefox")

def wait_for_element(driver, by, locator, timeout=10):
    """
    Ждет появления элемента на странице до timeout секунд.
    :param driver: экземпляр WebDriver
    :param by: способ поиска (например, "xpath")
    :param locator: значение локатора
    :param timeout: время ожидания (по умолчанию 10 секунд)
    :return: найденный элемент или выбросит TimeoutException
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, locator)))
