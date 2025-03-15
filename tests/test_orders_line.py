from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage
from pages.orders_page import OrdersPage
from api_client import Order
import allure


class TestOrdersLine:

    @allure.title('Появление всплывающего окна с деталями заказа при клике на заказ в Ленте заказов.')
    @allure.description('Клик на последний заказ в Ленте заказов, и проверка что окно с деталями открылось и детали заказа совпадает с выбранным.')
    def test_orders_line_on_click_order_in_line_order_details_card_opens(self, driver):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        orders_page.last_order_card_open()
        orders_page.check_card_order_number_and_name()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов».')
    @allure.description('Для теста регистрируется пользователь фикстурой user и добавляются токены авторизации в Loсal Storage фикстурой upload_tokens_to_session.'
                        ' Создается заказ пользователя через API.'
                        ' Далее переход на страницу История заказов в Личном кабинете и получение номера заказа из истории.'
                        ' Переход на страницу Лента заказов, и проверка что заказ с таким номером находится среди 5 последних заказов в Ленте заказов.'
                        ' После теста пользователь удаляется фикстурой и очищается Loсal Storage.')
    def test_orders_line_profile_history_orders_present_in_orders_line(self, driver, user, upload_tokens_to_session):
        Order.submit_order(user)
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.transfer_to_history_page()
        order = profile_page.get_history_page_order_number()
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        orders_page.check_order_present_in_last_5_orders_in_orders_line(order)

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается.')
    @allure.description('Для теста регистрируется пользователь фикстурой user и добавляются токены авторизации в Loсal Storage фикстурой upload_tokens_to_session.'
                        ' Открываем страницу Лента заказов и сохраняем значение счетчика "Выполнено за всё время".'
                        ' Создается заказ пользователя через API.'
                        ' Проверяем, что счетчик "Выполнено за всё время" увеличился.'
                        ' После теста пользователь удаляется фикстурой и очищается Loсal Storage.')
    def test_orders_line_order_created_all_orders_counter_increases(self, driver, user, upload_tokens_to_session):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        all_orders_before = orders_page.get_all_orders()
        Order.submit_order(user)
        orders_page.check_all_orders_counter_increased(all_orders_before)

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается.')
    @allure.description('Для теста регистрируется пользователь фикстурой user и добавляются токены авторизации в Loсal Storage фикстурой upload_tokens_to_session.'
                        ' Открываем страницу Лента заказов и сохраняем значение счетчика "Выполнено за сегодня".'
                        ' Создается заказ пользователя через API.'
                        ' Проверяем,что счетчик "Выполнено за сегодня" увеличился.'
                        ' После теста пользователь удаляется фикстурой и очищается Loсal Storage.')
    def test_orders_line_order_created_today_orders_counter_increases(self, driver, user, upload_tokens_to_session):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        today_orders_before = orders_page.get_today_orders()
        Order.submit_order(user)
        orders_page.check_today_orders_counter_increased(today_orders_before)

    @allure.title('После оформления заказа его номер появляется в разделе "В работе".')
    @allure.description('Для теста регистрируется пользователь фикстурой user и добавляются токены авторизации в Loсal Storage фикстурой upload_tokens_to_session.'
                        ' Открываем страницу Лента заказов.'
                        ' Создаем заказ пользователя через API и получаем его номер.'
                        ' Проверяем, что номер заказа появился в разделе "В работе".'
                        ' После теста пользователь удаляется фикстурой и очищается Loсal Storage.')
    def test_orders_line_order_created_order_appears_in_orders_in_progress_section(self, driver, user, upload_tokens_to_session):
        orders_page = OrdersPage(driver)
        orders_page.transfer_to_orders_page()
        order = Order.submit_order(user)
        orders_page.check_order_in_order_in_progress_section(order)
