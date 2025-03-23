# tests/test_navigation.py

import pytest
from selenium.webdriver.common.by import By
from conftest import wait_for_element
from locators import BUTTON_PERSONAL_ACCOUNT, BUTTON_CONSTRUCTOR, LOGO, BUTTON_LOGOUT, SECTION_BUNS, SECTION_SAUCES, SECTION_FILLINGS

BASE_URL = "https://stellarburgers.nomoreparties.site"
TEST_EMAIL = "registered_user@example.com"
TEST_PASSWORD = "correctpassword"

def login(driver):
    """
    Вспомогательная функция для авторизации пользователя.
    Предполагается, что используется кнопка "Войти в аккаунт" и форма входа.
    """
    driver.get(BASE_URL)
    login_button = wait_for_element(driver, By.CSS_SELECTOR, "button.login-btn")
    login_button.click()
    email_field = wait_for_element(driver, By.CSS_SELECTOR, "input[name='email']")
    password_field = wait_for_element(driver, By.CSS_SELECTOR, "input[name='password']")
    email_field.send_keys(TEST_EMAIL)
    password_field.send_keys(TEST_PASSWORD)
    submit_button = wait_for_element(driver, By.CSS_SELECTOR, "button.login-submit")
    submit_button.click()

def test_personal_account_transition(driver):
    login(driver)
    # Ждем и кликаем по кнопке "Личный кабинет"
    personal_account = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_PERSONAL_ACCOUNT[1])
    personal_account.click()
    # Проверяем, что на странице присутствует текст "Профиль"
    assert "Профиль" in driver.page_source

def test_constructor_navigation_from_personal_account(driver):
    login(driver)
    personal_account = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_PERSONAL_ACCOUNT[1])
    personal_account.click()
    # Ждем появления и кликаем по кнопке "Конструктор"
    constructor_button = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_CONSTRUCTOR[1])
    constructor_button.click()
    assert "Соберите бургер" in driver.page_source

def test_constructor_navigation_via_logo(driver):
    login(driver)
    personal_account = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_PERSONAL_ACCOUNT[1])
    personal_account.click()
    # Ждем появления логотипа и кликаем по нему
    logo = wait_for_element(driver, By.CSS_SELECTOR, LOGO[1])
    logo.click()
    assert "Соберите бургер" in driver.page_source

def test_logout(driver):
    login(driver)
    # Ждем и кликаем по кнопке "Выйти"
    logout_button = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_LOGOUT[1])
    logout_button.click()
    # Проверяем, что на странице отображается "Войти"
    assert "Войти" in driver.page_source

def test_constructor_sections(driver):
    driver.get(BASE_URL)
    # Ждем и кликаем по кнопке "Конструктор"
    constructor_button = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_CONSTRUCTOR[1])
    constructor_button.click()
    # Ждем появления разделов: «Булки», «Соусы», «Начинки»
    buns_section = wait_for_element(driver, By.CSS_SELECTOR, SECTION_BUNS[1])
    sauces_section = wait_for_element(driver, By.CSS_SELECTOR, SECTION_SAUCES[1])
    fillings_section = wait_for_element(driver, By.CSS_SELECTOR, SECTION_FILLINGS[1])
    assert buns_section.is_displayed()
    assert sauces_section.is_displayed()
    assert fillings_section.is_displayed()
