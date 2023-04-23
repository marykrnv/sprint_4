import allure

from pages.base_page import BasePage
from locators.start_page_locators import LocatorStartPage


class StartPage(BasePage):

    @allure.feature('Раскрыть ответ на вопрос')
    def click_on_accordion_button(self, locator):
        return self.click_on_button(locator)

    @allure.feature('Нажать на кнопку Заказать в хедере')
    def click_on_header_order_button(self):
        return self.click_on_button(LocatorStartPage.LOCATOR_HEADER_ORDER_BUTTON)

    @allure.feature('Нажать на кнопку Заказать в блоке Как это работает')
    def click_on_how_it_work_order_button(self):
        return self.click_on_button(LocatorStartPage.LOCATOR_HOW_IT_WORKS_ORDER_BUTTON)

    @allure.feature('Получить текст')
    def get_text(self, locator):
        search_element = self.find_element(locator)
        return search_element.text

    @allure.feature('Прокрутить до блока с вопросами')
    def scroll_to_questions(self):
        self.scroll_to_element(LocatorStartPage.LOCATOR_QUESTIONS)

    @allure.feature('Прокрутить до блока Как это работает')
    def scroll_to_how_it_works(self):
        self.scroll_to_element(LocatorStartPage.LOCATOR_HOW_IT_WORKS_ORDER_BUTTON)

    @allure.feature('Проверить заголовок')
    def check_main_header(self):
        return self.find_element(LocatorStartPage.LOCATOR_MAIN_HEADER)
