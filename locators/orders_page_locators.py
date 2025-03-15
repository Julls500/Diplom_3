from selenium.webdriver.common.by import By


class OrdersPageLocators:

    # Заголовок Кнопка "Лента заказов"
    orders_line_header = [By.XPATH, ".//h1[text()='Лента заказов']"]
    #5 последних заказов в списке заказов
    last_orders = [By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[position()<6]//p[@class='text text_type_digits-default']"]
    # Номер последнего заказа в списке заказов
    last_order_number = [By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[1]//p[@class='text text_type_digits-default']"]
    # Название последнего заказа в списке заказов
    last_order_name = [By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[1]//h2"]
    #Всплывающее окно с деталями заказа
    order_card = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]
    # Номер заказа в карточке с деталями заказа
    card_order_number = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//p[@class = 'text text_type_digits-default mb-10 mt-5']"]
    # Название заказа в карточке с деталями заказа
    card_order_name = [By.XPATH, ".//section[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//h2"]
    # Счетчик "Выполнено за все время"
    all_orders_counter = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"]
    # Счетчик "Выполнено за сегодня"
    today_orders_counter = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"]
    # Номер заказа в разделе "В работе"
    order_in_progress = [By.XPATH, ".//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class = 'text text_type_digits-default mb-2']"]
