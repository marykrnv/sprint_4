import allure

from pages.base_page import BasePage
from locators.order_page_locators import LocatorOrderPage
from locators.base_locators import LocatorBase


class OrderPage(BasePage):

    @allure.feature('Проверить заголовок страницы')
    def check_order_header(self):
        return self.find_element(LocatorOrderPage.LOCATOR_ORDER_HEADER)

    @allure.feature('Ввести имя')
    def enter_name(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_NAME_INPUT, text)

    @allure.feature('Ввести фамилию')
    def enter_lastname(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_LASTNAME_INPUT, text)

    @allure.feature('Ввести адрес')
    def enter_address(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_ADDRESS_INPUT, text)

    @allure.feature('Ввести метро')
    def enter_metro(self, text):
        self.enter_text(LocatorOrderPage.LOCATOR_METRO_INPUT, text)
        return self.click_on_button(LocatorOrderPage.LOCATOR_SELECT)

    @allure.feature('Ввести номер телефона')
    def enter_phone(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_PHONE_INPUT, text)

    @allure.feature('Нажать кнопку Далее')
    def click_on_next_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_NEXT_BUTTON)

    @allure.feature('Ввести персональные данные')
    def enter_pers_data(self, name, lastname, address, metro, phone):
        self.enter_name(name)
        self.enter_lastname(lastname)
        self.enter_address(address)
        self.enter_metro(metro)
        self.enter_phone(phone)
        self.click_on_next_button()

    @allure.feature('Ввести дату')
    def enter_date(self, text):
        self.enter_text(LocatorOrderPage.LOCATOR_DATE_INPUT, text)
        return self.click_on_button(LocatorOrderPage.LOCATOR_DATE_SELECT)

    @allure.feature('Ввести комментарий')
    def enter_comment(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_COMMENT_INPUT, text)

    @allure.feature('Ввести период')
    def choose_rental_period(self, period):
        self.click_on_button(LocatorOrderPage.LOCATOR_DROPDOWN)
        self.find_element(LocatorOrderPage.LOCATOR_DROPDOWN_MENU)
        elements = self.find_elements(LocatorOrderPage.LOCATOR_DROPDOWN_OPTION)
        element = [el for el in elements if el.text == period]
        self.click_on_button(element[0])

    @allure.feature('Выбрать цвет самоката')
    def choose_color(self, color):
        if color == 'черный жемчуг':
            return self.click_on_button(LocatorOrderPage.LOCATOR_BLACK_COLOR)
        elif color == 'серая безысходность':
            return self.click_on_button(LocatorOrderPage.LOCATOR_GREY_COLOR)

    @allure.feature('Нажать кнопку Заказать')
    def click_on_order_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_ORDER_BUTTON)

    @allure.feature('Ввести дополнительные данные')
    def enter_order_data(self, date, period, color, comment):
        self.enter_date(date)
        self.choose_rental_period(period)
        self.choose_color(color)
        self.enter_comment(comment)
        self.click_on_order_button()

    @allure.feature('Закрыть плашку с куки')
    def click_on_cookie_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_COOKIE_BUTTON)

    @allure.feature('Нажать кнопку Да')
    def click_on_agree_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_AGREE_BUTTON)

    @allure.feature('Проверить заголовок модального окна')
    def check_modal_header(self):
        return self.find_element(LocatorOrderPage.LOCATOR_MODAL_HEADER)

    @allure.feature('Перейти на главную страницу самоката')
    def click_on_samokat(self):
        return self.click_on_button(LocatorBase.LOCATOR_SAMOKAT_BUTTON)

    @allure.feature('Перейти на главную страницу Яндекса')
    def click_on_ya(self):
        return self.click_on_button(LocatorBase.LOCATOR_YA_BUTTON)
