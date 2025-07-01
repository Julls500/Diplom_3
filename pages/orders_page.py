from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePage
import allure
from data import Urls


class OrdersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание появления заголовка Лента заказов')
    def orders_header_wait(self):
       self.wait_visibility_of_element(OrdersPageLocators.orders_line_header)

    @allure.step('Переход на страницу Лента заказов')
    def transfer_to_orders_page(self):
        self.change_url(Urls.ORDERS)
        self.orders_header_wait()

    @allure.step('Проверка перехода на страницу Лента заказов')
    def check_orders_page_transfer(self):
        self.orders_header_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.ORDERS, f'Смена страницы не произошла: {current_url}'

    @allure.step('Получение 5 последних заказов из Ленты заказов')
    def get_order_line_last_orders(self):
        return self.find_elements(OrdersPageLocators.last_orders)

    @allure.step('Получение списка номеров из списка элементов')
    def get_orders_nums_list(self, orders):
        order_nums = []
        for order in orders:
            order_nums.append(order.text[2:])
        return order_nums

    @allure.step('Получение списка номеров 5 последних заказов из Ленты заказов')
    def get_order_line_last_5_orders_nums_list(self):
        orders = self.get_order_line_last_orders()
        return self.get_orders_nums_list(orders)

    @allure.step('Проверка что заказ находится среди последних 5 заказов Ленты заказов')
    def check_order_present_in_last_5_orders_in_orders_line(self, order):
        last_5_orders = self.get_order_line_last_5_orders_nums_list()
        assert order in last_5_orders, f'Заказ {order} не найден среди последних 5 заказов {last_5_orders} в Ленте заказов.'

    @allure.step('Клик по последнему заказу из Ленты заказов')
    def last_order_click(self):
        self.click_on_element(OrdersPageLocators.last_order_number)

    @allure.step('Ожидание видимости окна с деталями заказа')
    def order_details_card_wait(self):
       self.wait_visibility_of_element(OrdersPageLocators.order_card)

    @allure.step('Открытие карточки последнего заказа')
    def last_order_card_open(self):
        self.last_order_click()
        self.order_details_card_wait()

    @allure.step('Проверка что номер и название заказа в карточке с деталями совпадает с заказом из Ленты заказов')
    def check_card_order_number_and_name(self):
        last_order_number = self.get_element_text(OrdersPageLocators.last_order_number)
        last_order_name = self.get_element_text(OrdersPageLocators.last_order_name)
        card_order_number = self.get_element_text(OrdersPageLocators.card_order_number)
        card_order_name = self.get_element_text(OrdersPageLocators.card_order_name)
        assert card_order_number == last_order_number and card_order_name == last_order_name, f'Детали заказа не совпадают: {card_order_number} {card_order_name} и {last_order_number} {last_order_name}.'

    @allure.step('Ожидание видимости счетчика "Выполнено за все время"')
    def all_orders_counter_wait(self):
       self.wait_visibility_of_element(OrdersPageLocators.all_orders_counter)

    @allure.step('Получение значения счетчика заказов "Выполнено за все время"')
    def get_all_orders(self):
        self.refresh_page()
        self.all_orders_counter_wait()
        return int(self.get_element_text(OrdersPageLocators.all_orders_counter))

    @allure.step('Проверка что счетчик заказов "Выполнено за все время" увеличился')
    def check_all_orders_counter_increased(self, all_orders_before):
        all_orders_after = self.get_all_orders()
        assert all_orders_after > all_orders_before, f'Счетчик изменился некорректно: c {all_orders_before} на {all_orders_after}.'

    @allure.step('Ожидание видимости счетчика "Выполнено за сегодня"')
    def today_orders_counter_wait(self):
       self.wait_visibility_of_element(OrdersPageLocators.today_orders_counter)

    @allure.step('Получение значения счетчика заказов "Выполнено за сегодня"')
    def get_today_orders(self):
        self.refresh_page()
        self.today_orders_counter_wait()
        return int(self.get_element_text(OrdersPageLocators.today_orders_counter))

    @allure.step('Проверка что счетчик заказов "Выполнено за сегодня" увеличился')
    def check_today_orders_counter_increased(self, today_orders_before):
        today_orders_after = self.get_today_orders()
        assert today_orders_after > today_orders_before, f'Счетчик изменился некорректно: c {today_orders_before} на {today_orders_after}.'

    @allure.step('Ожидание появления номера заказа в разделе "В работе"')
    def order_in_progress_wait(self, order):
        self.wait_presence_of_element(OrdersPageLocators.order_in_progress)
        self.wait_elem_value_changes(OrdersPageLocators.order_in_progress, order)

    @allure.step('Получение номера заказа из раздела "В работе"')
    def get_order_in_progress_number(self):
        return str(self.get_element_text(OrdersPageLocators.order_in_progress)[1:])

    @allure.step('Проверка что номер заказа в разделе "В работе" совпадает с созданным')
    def check_order_in_order_in_progress_section(self, order):
        self.refresh_page()
        self.order_in_progress_wait(order)
        order_in_progress = self.get_order_in_progress_number()
        assert order == order_in_progress, f'Заказ не появился в разделе "В работе": ожидалось {order}, получено {order_in_progress}.'
