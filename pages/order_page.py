import allure

from locators.base_locators import LocatorBase
from locators.order_page_locators import LocatorOrderPage
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Проверить заголовок страницы')
    def check_order_header(self):
        return self.find_element(LocatorOrderPage.LOCATOR_ORDER_HEADER)

    @allure.step('Ввести имя')
    def enter_name(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_NAME_INPUT, text)

    @allure.step('Ввести фамилию')
    def enter_lastname(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_LASTNAME_INPUT, text)

    @allure.step('Ввести адрес')
    def enter_address(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_ADDRESS_INPUT, text)

    @allure.step('Ввести метро')
    def enter_metro(self, text):
        self.enter_text(LocatorOrderPage.LOCATOR_METRO_INPUT, text)
        return self.click_on_button(LocatorOrderPage.LOCATOR_SELECT)

    @allure.step('Ввести номер телефона')
    def enter_phone(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_PHONE_INPUT, text)

    @allure.step('Нажать кнопку Далее')
    def click_on_next_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_NEXT_BUTTON)

    @allure.step('Ввести персональные данные')
    def enter_pers_data(self, name, lastname, address, metro, phone):
        self.enter_name(name)
        self.enter_lastname(lastname)
        self.enter_address(address)
        self.enter_metro(metro)
        self.enter_phone(phone)
        self.click_on_next_button()

    @allure.step('Ввести дату')
    def enter_date(self, text):
        self.enter_text(LocatorOrderPage.LOCATOR_DATE_INPUT, text)
        return self.click_on_button(LocatorOrderPage.LOCATOR_DATE_SELECT)

    @allure.step('Ввести комментарий')
    def enter_comment(self, text):
        return self.enter_text(LocatorOrderPage.LOCATOR_COMMENT_INPUT, text)

    @allure.step('Ввести период')
    def choose_rental_period(self, period):
        self.click_on_button(LocatorOrderPage.LOCATOR_DROPDOWN)
        self.find_element(LocatorOrderPage.LOCATOR_DROPDOWN_MENU)
        elements = self.find_elements(LocatorOrderPage.LOCATOR_DROPDOWN_OPTION)
        element = [el for el in elements if el.text == period]
        self.click_on_button(element[0])

    @allure.step('Выбрать цвет самоката')
    def choose_color(self, color):
        if color == 'черный жемчуг':
            return self.click_on_button(LocatorOrderPage.LOCATOR_BLACK_COLOR)
        elif color == 'серая безысходность':
            return self.click_on_button(LocatorOrderPage.LOCATOR_GREY_COLOR)

    @allure.step('Нажать кнопку Заказать')
    def click_on_order_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_ORDER_BUTTON)

    @allure.step('Ввести дополнительные данные')
    def enter_order_data(self, date, period, color, comment):
        self.enter_date(date)
        self.choose_rental_period(period)
        self.choose_color(color)
        self.enter_comment(comment)
        self.click_on_order_button()

    @allure.step('Закрыть плашку с куки')
    def click_on_cookie_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_COOKIE_BUTTON)

    @allure.step('Нажать кнопку Да')
    def click_on_agree_button(self):
        return self.click_on_button(LocatorOrderPage.LOCATOR_AGREE_BUTTON)

    @allure.step('Проверить заголовок модального окна')
    def check_modal_header(self):
        return self.find_element(LocatorOrderPage.LOCATOR_MODAL_HEADER)

    @allure.step('Перейти на главную страницу самоката')
    def click_on_samokat(self):
        return self.click_on_button(LocatorBase.LOCATOR_SAMOKAT_BUTTON)

    @allure.step('Перейти на главную страницу Яндекса')
    def click_on_ya(self):
        return self.click_on_button(LocatorBase.LOCATOR_YA_BUTTON)
