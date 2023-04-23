import allure

from pages.base_page import BasePage
from locators.ya_page_locators import LocatorYaPage


class YaSearchPage(BasePage):

    @allure.feature('Получить элемент Сейчас в СМИ')
    def get_element_nav_bar(self):
        return self.find_element(LocatorYaPage.LOCATOR_NAV_BAR)

    @allure.feature('Закрыть модальное окно')
    def click_on_x(self):
        return self.click_on_button(LocatorYaPage.LOCATOR_X)
