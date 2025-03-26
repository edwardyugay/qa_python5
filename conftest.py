# conftest.py

import pytest
from selenium import webdriver

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


