from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 100).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_clickability_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Заполнение поля')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получение текущей ссылки')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перейти на другую страницу')
    def change_url(self, url):
        self.driver.get(url)

    @allure.step('Получение значения класса элемента')
    def get_element_class(self, locator):
        element = self.driver.find_element(*locator)
        return  element.get_attribute("class")

    @allure.step('Ожидание появления элемента в DOM')
    def wait_presence_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Ожидание смены ссылки')
    def wait_link_changes(self, url):
        return WebDriverWait(self.driver, 6).until(expected_conditions.url_changes(url))

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Ожидание исчезновения элемента')
    def wait_element_disappear(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Поиск группы элементов')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Ожидание смены текста элемента на новый')
    def wait_elem_text_change(self, locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.none_of(
        expected_conditions.text_to_be_present_in_element(locator, text)))

    @allure.step('Обновить страницу')
    def refresh_page(self):
        self.driver.refresh()

    @allure.step('Ожидание смены значения элемента')
    def wait_elem_value_changes(self, locator, value):
        return WebDriverWait(self.driver, 6).until(expected_conditions.text_to_be_present_in_element(locator, value))

    @allure.step('Перетащить элемент')
    def drag_drop_element(self, source_locator, target_locator):
        if self.driver.name == 'firefox':
            source_element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(source_locator))
            target_element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(target_locator))
            self.driver.execute_script(
            "function createEvent(typeOfEvent) { " +
            "var event = document.createEvent('CustomEvent'); " +
            "event.initCustomEvent(typeOfEvent, true, true, null); " +
            "event.dataTransfer = { " +
            "data: {}, " +
            "setData: function(key, value) { this.data[key] = value; }, " +
            "getData: function(key) { return this.data[key]; } " +
            "}; " +
            "return event; " +
            "} " +
            "function dispatchEvent(element, typeOfEvent, event) { " +
            "if (element.dispatchEvent) { " +
            "element.dispatchEvent(event); " +
            "} else if (element.fireEvent) { " +
            "element.fireEvent('on' + typeOfEvent, event); " +
            "} " +
            "} " +
            "function simulateHTML5DragAndDrop(element, destination) { " +
            "var dragStartEvent = createEvent('dragstart'); " +
            "dispatchEvent(element, 'dragstart', dragStartEvent); " +
            "var dropEvent = createEvent('drop'); " +
            "dispatchEvent(destination, 'drop', dropEvent); " +
            "var dragEndEvent = createEvent('dragend'); " +
            "dispatchEvent(element, 'dragend', dragEndEvent); " +
            "} " +
            "simulateHTML5DragAndDrop(arguments[0], arguments[1]);",
            source_element,
            target_element
            )
        else:
            source_elem = self.driver.find_element(*source_locator)
            target_elem = self.driver.find_element(*target_locator)
            action_chains = ActionChains(self.driver)
            action_chains.drag_and_drop(source_elem, target_elem).perform()
