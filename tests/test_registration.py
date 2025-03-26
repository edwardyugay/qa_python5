# tests/test_registration.py

import pytest
from selenium.webdriver.common.by import By
from conftest import wait_for_element
from locators import LINK_REGISTRATION, INPUT_NAME, INPUT_EMAIL, INPUT_PASSWORD, BUTTON_REGISTER, ERROR_PASSWORD, \
    BUTTON_PERSONAL_ACCOUNT
from helper import generate_email, generate_password

BASE_URL = "https://stellarburgers.nomoreparties.site"


def test_successful_registration(driver):
    driver.get(BASE_URL)
    # Ждем появления ссылки "Регистрация" и кликаем по ней
    reg_link = wait_for_element(driver, By.LINK_TEXT, LINK_REGISTRATION[1])
    reg_link.click()

    # Ждем появления полей ввода в форме регистрации
    name_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_NAME[1])
    email_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_EMAIL[1])
    password_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_PASSWORD[1])

    # Генерация уникальных данных для регистрации
    test_name = "TestName"
    test_surname = "TestSurname"
    cohort = "1999"
    email = generate_email(test_name, test_surname, cohort)
    password = generate_password(8)

    name_field.send_keys(test_name)
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Ждем появления и клика по кнопке регистрации
    register_button = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_REGISTER[1])
    register_button.click()

    # Ждем появления кнопки "Личный кабинет" – подтверждение успешной регистрации
    personal_account = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_PERSONAL_ACCOUNT[1])
    assert personal_account.is_displayed()


def test_invalid_password_registration(driver):
    driver.get(BASE_URL)
    reg_link = wait_for_element(driver, By.LINK_TEXT, LINK_REGISTRATION[1])
    reg_link.click()

    name_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_NAME[1])
    email_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_EMAIL[1])
    password_field = wait_for_element(driver, By.CSS_SELECTOR, INPUT_PASSWORD[1])

    test_name = "TestName"
    test_surname = "TestSurname"
    cohort = "1999"
    email = generate_email(test_name, test_surname, cohort)
    # Используем пароль меньше 6 символов для проверки ошибки
    password = "12345"

    name_field.send_keys(test_name)
    email_field.send_keys(email)
    password_field.send_keys(password)

    register_button = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_REGISTER[1])
    register_button.click()

    # Ждем появления сообщения об ошибке
    error_msg = wait_for_element(driver, By.CSS_SELECTOR, ERROR_PASSWORD[1])
    assert error_msg.is_displayed()

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


@pytest.mark.parametrize("section_locator, section_name", [
    (SECTION_BUNS[1], "Булки"),
    (SECTION_SAUCES[1], "Соусы"),
    (SECTION_FILLINGS[1], "Начинки")
])
def test_constructor_section(driver, section_locator, section_name):
    driver.get(BASE_URL)
    # Ждем и кликаем по кнопке "Конструктор"
    constructor_button = wait_for_element(driver, By.CSS_SELECTOR, BUTTON_CONSTRUCTOR[1])
    constructor_button.click()
    # Ожидаем, пока раздел станет видимым
    section = wait_for_element(driver, By.CSS_SELECTOR, section_locator)
    assert section.is_displayed(), f"Раздел '{section_name}' не отображается"
