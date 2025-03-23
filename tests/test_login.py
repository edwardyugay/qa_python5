# tests/test_login.py

import pytest
from selenium.webdriver.common.by import By
from conftest import wait_for_element
from locators import BUTTON_LOGIN, BUTTON_PERSONAL_ACCOUNT, INPUT_EMAIL, INPUT_PASSWORD, LINK_LOGIN_FROM_REG, \
    LINK_LOGIN_FROM_RECOVERY

BASE_URL = "https://stellarburgers.nomoreparties.site"
TEST_EMAIL = "registered_user@example.com"
TEST_PASSWORD = "correctpassword"


def test_login_from_main_page(driver):
    driver.get(BASE_URL)
    # Ждем появления кнопки "Войти в аккаунт" и кликаем по ней
    login_button = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_LOGIN[1])
    login_button.click()

    # Ждем появления полей ввода и вводим данные
    email_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_EMAIL[1])
    password_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_PASSWORD[1])
    email_field.send_keys(TEST_EMAIL)
    password_field.send_keys(TEST_PASSWORD)

    # Ждем появления кнопки отправки (предположим, селектор "button.login-submit")
    submit_button = wait_for_element(driver, By.CSS_SELECTOR, "button.login-submit")
    submit_button.click()

    # Проверяем, что после входа отображается "Личный кабинет"
    assert "Личный кабинет" in driver.page_source


def test_login_from_personal_account(driver):
    driver.get(BASE_URL)
    # Ждем и кликаем по ссылке "Личный кабинет"
    personal_account = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_PERSONAL_ACCOUNT[1])
    personal_account.click()

    email_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_EMAIL[1])
    password_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_PASSWORD[1])
    email_field.send_keys(TEST_EMAIL)
    password_field.send_keys(TEST_PASSWORD)

    submit_button = wait_for_element(driver, By.CSS_SELECTOR, "button.login-submit")
    submit_button.click()

    assert "Личный кабинет" in driver.page_source


def test_login_from_registration_form(driver):
    driver.get(BASE_URL)
    # Переход на страницу регистрации
    reg_link = wait_for_element(driver, By.LINK_TEXT, "Регистрация")
    reg_link.click()

    # Ждем появления кнопки "Войти" в форме регистрации и кликаем по ней
    login_via_reg_button = wait_for_element(driver, By.LINK_TEXT, LINK_LOGIN_FROM_REG[1])
    login_via_reg_button.click()

    email_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_EMAIL[1])
    password_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_PASSWORD[1])
    email_field.send_keys(TEST_EMAIL)
    password_field.send_keys(TEST_PASSWORD)

    submit_button = wait_for_element(driver, By.CSS_SELECTOR, "button.login-submit")
    submit_button.click()

    assert "Личный кабинет" in driver.page_source


def test_login_from_password_recovery_form(driver):
    driver.get(BASE_URL)
    # Переход на страницу восстановления пароля
    recovery_link = wait_for_element(driver, By.LINK_TEXT, "Восстановить пароль")
    recovery_link.click()

    # Ждем появления кнопки "Войти" в форме восстановления и кликаем по ней
    login_via_recovery_button = wait_for_element(driver, By.LINK_TEXT, LINK_LOGIN_FROM_RECOVERY[1])
    login_via_recovery_button.click()

    email_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_EMAIL[1])
    password_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_PASSWORD[1])
    email_field.send_keys(TEST_EMAIL)
    password_field.send_keys(TEST_PASSWORD)

    submit_button = wait_for_element(driver, By.CSS_SELECTOR, "button.login-submit")
    submit_button.click()

    assert "Личный кабинет" in driver.page_source
