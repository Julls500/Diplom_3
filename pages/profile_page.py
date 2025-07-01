from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
import allure
from data import Urls


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание видимости кнопки Профиль')
    def profile_tab_wait(self):
       self.wait_visibility_of_element(ProfilePageLocators.profile_tab)

    @allure.step('Проверка перехода на страницу Личный кабинет')
    def check_profile_page_transfer(self):
        self.profile_tab_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.PROFILE, f'Смена страницы не произошла: {current_url}'

    @allure.step('Ожидание кликабельности кнопки История заказов')
    def history_tab_wait(self):
        self.wait_clickability_of_element(ProfilePageLocators.history_tab)

    @allure.step('Клик по кнопке История заказов')
    def history_tab_click(self):
        self.history_tab_wait()
        self.click_on_element(ProfilePageLocators.history_tab)

    @allure.step('Ожидание активации кнопки История заказов')
    def history_tab_activation_wait(self):
        self.wait_presence_of_element(ProfilePageLocators.history_tab_active)

    @allure.step('Проверка перехода на страницу История заказов')
    def check_history_page_transfer(self):
        self.history_tab_activation_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.HISTORY, f'Смена страницы не произошла: {current_url}'

    @allure.step('Ожидание кликабельности кнопки Выход')
    def logout_button_wait(self):
        self.wait_clickability_of_element(ProfilePageLocators.logout_button)

    @allure.step('Клик по кнопке Выход')
    def logout_button_click(self):
        self.logout_button_wait()
        self.click_on_element(ProfilePageLocators.logout_button)

    @allure.step('Ожидание перехода со страницы Личный кабинет')
    def change_profile_link_wait(self):
        self.wait_link_changes(Urls.PROFILE)

    @allure.step('Проверка перехода на страницу Авторизации из Личного кабинета')
    def check_login_page_transfer(self):
        self.change_profile_link_wait()
        current_url = self.get_current_url()
        assert current_url == Urls.LOGIN, f'Смена страницы не произошла: {current_url}'

    @allure.step('Ожидение загрузки списка заказов')
    def order_history_wait(self):
        self.wait_visibility_of_element(ProfilePageLocators.orders_history)

    @allure.step('Переход на страницу История заказов в Личном кабинете')
    def transfer_to_history_page(self):
        self.profile_tab_wait()
        self.click_on_element(ProfilePageLocators.history_tab)
        self.order_history_wait()

    @allure.step('Получение номера заказа из Истории заказов в Личном кабинете')
    def get_history_page_order_number(self):
        return self.get_element_text(ProfilePageLocators.order_number)[2:]
