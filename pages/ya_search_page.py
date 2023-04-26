import allure

from locators.ya_page_locators import LocatorYaPage
from pages.base_page import BasePage


class YaSearchPage(BasePage):

    @allure.step('Получить элемент Сейчас в СМИ')
    def get_element_nav_bar(self):
        return self.find_element(LocatorYaPage.LOCATOR_NAV_BAR)
