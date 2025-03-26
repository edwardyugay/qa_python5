# helper.py

from faker import Faker
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




fake = Faker()

def generate_email(name: str = None, surname: str = None, cohort: str = None, domain: str = "yandex.ru") -> str:
    """
    Генерирует email в формате: имя_фамилия_номерКогорты_XXX@домен.
    Если имя, фамилия или когорта не переданы, используются случайные данные.
    Пример: test_testov_1999_123@yandex.ru
    """
    if name is None:
        name = fake.first_name()
    if surname is None:
        surname = fake.last_name()
    if cohort is None:
        cohort = str(random.randint(1990, 2025))
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{name.lower()}_{surname.lower()}_{cohort}_{random_digits}@{domain}"
    return email

def generate_password(length: int = 8) -> str:
    """
    Генерирует пароль длиной length символов.
    Минимальная длина пароля — 6 символов.
    """
    if length < 6:
        length = 6
    return fake.password(length=length, special_chars=False, digits=True, upper_case=True, lower_case=True)

def wait_for_visible_element(driver, by, locator, timeout=10):
    """
    Ждет, пока элемент станет видимым на странице.
    
    :param driver: экземпляр WebDriver
    :param by: способ поиска (например, "xpath")
    :param locator: значение локатора
    :param timeout: время ожидания (по умолчанию 10 секунд)
    :return: найденный и видимый элемент или выбросит TimeoutException
    """
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
