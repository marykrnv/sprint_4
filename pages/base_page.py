from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def go_to_web(self, path=''):
        return self.driver.get(f'{self.base_url}{path}')

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f"No element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                      message=f"No element by locator {locator}")

    def is_clickable(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def enter_text(self, locator, text):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(text)
        return search_field

    def click_on_button(self, locator):
        search_button = self.is_clickable(locator)
        search_button.click()
        return search_button

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
