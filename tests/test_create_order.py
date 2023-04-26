import allure
import pytest

from pages.order_page import OrderPage
from pages.start_page import StartPage
from pages.ya_search_page import YaSearchPage


class TestOrderPage:

    @allure.title('Нажать кнопку «Заказать» в хедере')
    def test_go_to_order_page_on_header_order_button(self, driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.click_on_header_order_button()
        order_page = OrderPage(driver)
        header = order_page.check_order_header()

        assert header.text == 'Для кого самокат', f'Фактический результат: {header.text}'

    @allure.title('Нажать кнопку «Заказать» в блоке "Как это работает"')
    def test_go_to_order_page_on_how_it_work_order_button(self, driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_how_it_works()
        start_page.click_on_how_it_work_order_button()
        order_page = OrderPage(driver)
        header = order_page.check_order_header()

        assert header.text == 'Для кого самокат', f'Фактический результат: {header.text}'

    @allure.title('Заполнить форму заказа. Проверить, что появилось всплывающее окно с сообщением об успешном создании'
                  ' заказа')
    @pytest.mark.parametrize(
        argnames=['name', 'lastname', 'address', 'metro', 'phone', 'date', 'period', 'color', 'comment',
                  'expected_result'],
        argvalues=[('Ольга', 'Ким', 'ул. Митинская, д. 9', 'Митино', '99999999999', '27.10.2023', 'сутки',
                    'черный жемчуг', 'Тест', 'Заказ оформлен'),
                   ('Сергей', 'Фокс', 'ул. Фрунзе, д. 9', 'Фрунзенская', '99997777777', '17.4.2023', 'двое суток',
                    'серая безысходность', 'Тестовый тест', 'Заказ оформлен'),
                   ])
    def test_create_new_order(self, driver, name, lastname, address, metro, phone, date, period, color, comment,
                              expected_result):
        order_page = OrderPage(driver)
        order_page.go_to_web('order')
        order_page.click_on_cookie_button()
        order_page.enter_pers_data(name, lastname, address, metro, phone)
        order_page.enter_order_data(date, period, color, comment)
        order_page.click_on_agree_button()
        header = order_page.check_modal_header()

        assert expected_result in header.text, \
            f'Ожидаемый результат: {expected_result}, Полученный результат: {header.text}'

    @allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_go_to_main_page_from_order_page(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_web('order')
        order_page.click_on_samokat()
        start_page = StartPage(driver)
        header = start_page.check_main_header()

        assert 'Самокат' in header.text, f'Фактический результат: {header.text}'

    @allure.title('Проверить: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    def test_go_to_ya_page_from_order_page(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_web('order')
        order_page.click_on_ya()
        ya_page = YaSearchPage(driver)
        element = ya_page.get_element_nav_bar()

        assert 'Сейчас в СМИ' in element.text, f'Фактический результат: {element.text}'
