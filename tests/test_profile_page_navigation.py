from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
import allure


class TestProfilePage:

    @allure.title('Успешный переход авторизованного пользователя на страницу Личный кабинет по клику на кнопку «Личный кабинет» в шапке сервиса.')
    @allure.description('Регистрация пользователя и добавление токенов авторизации в Loсal Storage фикстурой upload_tokens_to_session.'
                        ' Клик по кнопке «Личный кабинет» в шапке сервиса.'
                        ' Проверка перехода на страницу Личный кабинет.'
                        ' Удаление пользователя фикстурой и очистка Loсal Storage.')
    def test_profile_page_user_authorized_on_click_profile_button_profile_page_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.check_profile_page_transfer()

    @allure.title('Переход неавторизованного пользователя на страницу Авторизации по клику на кнопку «Личный кабинет» в шапке сервиса.')
    @allure.description('Клик по кнопке «Личный кабинет» в шапке сервиса.'
                        ' Проверка перехода на страницу Авторизации.')
    def test_profile_page_user_not_authorized_on_click_profile_button_login_page_opens(self, driver):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        login_page = LoginPage(driver)
        login_page.check_login_page_transfer()

    @allure.title('Успешный переход авторизованного пользователя в раздел История заказов по клику на кнопку «История заказов» в Личном кабинете.')
    @allure.description('Регистрация пользователя и добавление токенов авторизации в Loсal Storage фикстурой upload_tokens_to_session.'
                        ' Клик по кнопке «Личный кабинет» в шапке сервиса.'
                        ' Клик по кнопке «История заказов» в Личном кабинете.'
                        ' Проверка перехода в раздел История заказов.'
                        ' Удаление пользователя фикстурой и очистка Loсal Storage.')
    def test_profile_page_on_click_history_tab_history_page_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.history_tab_click()
        profile_page.check_history_page_transfer()

    @allure.title('Успешный выход авторизованного пользователя из системы и переход на страницу Авторизации по клику на кнопку «Выход» в Личном кабинете.')
    @allure.description('Регистрация пользователя и добавление токенов авторизации в Loсal Storage фикстурой upload_tokens_to_session.'
                        ' Клик по кнопке «Личный кабинет» в шапке сервиса.'
                        ' Клик по кнопке «Выход» в Личном кабинете.'
                        ' Проверка перехода на страницу Авторизации.'
                        ' Удаление пользователя фикстурой и очистка Loсal Storage.')
    def test_profile_page_on_click_logout_button_login_page_opens(self, driver, upload_tokens_to_session):
        header_page = HeaderPage(driver)
        header_page.profile_link_click()
        profile_page = ProfilePage(driver)
        profile_page.logout_button_click()
        profile_page.check_login_page_transfer()
