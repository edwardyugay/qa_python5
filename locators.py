# locators.py

# Заголовок страницы «Соберите бургер» (используется, например, на странице конструктора)
HEADER = ("xpath", "//h1[text()='Соберите бургер']")

# Кнопка "Войти в аккаунт" – ищем кнопку по её тексту
BUTTON_LOGIN = ("xpath", "//button[contains(text(), 'Войти в аккаунт')]")

# Ссылка для перехода на страницу регистрации
LINK_REGISTRATION = ("xpath", "//a[text()='Регистрация']")

# Поле ввода "Имя" в форме регистрации
INPUT_NAME = ("xpath", "//input[@name='name']")

# Поле ввода "Email" в формах регистрации/входа
INPUT_EMAIL = ("xpath", "//input[@name='email']")

# Поле ввода "Пароль" в формах регистрации/входа
INPUT_PASSWORD = ("xpath", "//input[@name='password']")

# Кнопка "Зарегистрироваться"
BUTTON_REGISTER = ("xpath", "//button[contains(text(), 'Зарегистрироваться')]")

# Сообщение об ошибке для некорректного пароля (проверьте точный текст ошибки на сайте)
ERROR_PASSWORD = ("xpath", "//p[contains(text(), 'Некорректный пароль')]")

# Ссылка "Личный кабинет"
BUTTON_PERSONAL_ACCOUNT = ("xpath", "//a[contains(text(), 'Личный кабинет')]")

# Кнопка "Конструктор"
BUTTON_CONSTRUCTOR = ("xpath", "//a[contains(text(), 'Конструктор')]")

# Логотип Stellar Burgers (ищем ссылку, в классе которой содержится слово 'logo')
LOGO = ("xpath", "//a[contains(@class, 'logo')]")

# Кнопка "Выйти" в личном кабинете
BUTTON_LOGOUT = ("xpath", "//button[contains(text(), 'Выйти')]")

# Элементы раздела "Конструктор" – вкладки с названиями разделов
SECTION_BUNS = ("xpath", "//span[text()='Булки']")
SECTION_SAUCES = ("xpath", "//span[text()='Соусы']")
SECTION_FILLINGS = ("xpath", "//span[text()='Начинки']")

# Ссылка "Войти" в формах регистрации или восстановления пароля
LINK_LOGIN_FROM_REG = ("xpath", "//a[text()='Войти']")
LINK_LOGIN_FROM_RECOVERY = ("xpath", "//a[text()='Войти']")
