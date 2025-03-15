from selenium.webdriver.common.by import By


class HeaderPageLocators:

    # Кнопка "Личный кабинет"
    user_account_link = [By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX' and @href='/account']"]
    # Кнопка "Конструктор"
    constructor = [By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX' and @href='/']"]
    # Кнопка "Лента заказов"
    orders_line = [By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX' and @href='/feed']"]
