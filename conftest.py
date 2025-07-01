import pytest
from api_client import User, Order
import allure
from utilites import WebdriverFactory
from data import Urls

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@allure.step('Создание драйвера.')
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser)
    driver.maximize_window()
    driver.get(Urls.URL_SERVICE)
    yield driver
    driver.quit()

@allure.step('Создание тестового юзера.')
@pytest.fixture
def user():
    user = User.register()
    yield user
    User.delete(user.get("accessToken"))

@allure.step('Создание заказа.')
@pytest.fixture
def submit_order(user):
    Order.submit_order(user)

@allure.step('Добавление токенов авторизации в LocalStorage и очистка даных после теста.')
@pytest.fixture
def upload_tokens_to_session(driver, user):
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'accessToken',
                          user['accessToken'])
    driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", 'refreshToken',
                          user['refreshToken'])
    driver.refresh()
    yield
    driver.execute_script("window.localStorage.clear();")
    driver.delete_all_cookies()
