from selenium.webdriver.common.by import By


class ProfilePageLocators:

    # Кнопка "Профиль"
    profile_tab = [By.XPATH, ".//a[text() = 'Профиль']"]
    # Кнопка "История заказов неактивная"
    history_tab = [By.XPATH, ".//a[text() = 'История заказов']"]
    # Кнопка "История заказов активная"
    history_tab_active = [By.XPATH, ".//a[contains(@class,  'Account_link_active__2opc9') and text() = 'История заказов']"]
    # Кнопка Выход
    logout_button = [By.XPATH, ".//button[text() = 'Выход']"]
    # Список заказов в разделе История заказов
    orders_history = [By.XPATH, ".//ul[@class = 'OrderHistory_profileList__374GU OrderHistory_list__KcLDB']"]
    # Номер первого заказа в разделе История заказов
    order_number = [By.XPATH, ".//ul[@class = 'OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[1]//p[@class = 'text text_type_digits-default']"]
