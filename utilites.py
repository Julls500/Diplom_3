from selenium import webdriver


class WebdriverFactory:

    @staticmethod
    def get_webdriver(browser):
        if browser == 'firefox':
            return webdriver.Firefox()
        elif browser == 'chrome':
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser}")