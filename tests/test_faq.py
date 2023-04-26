import allure
import pytest

from locators.start_page_locators import LocatorStartPage
from pages.start_page import StartPage

test_cases = [
    ('LOCATOR_PRICE_BUTTON', 'LOCATOR_PRICE_TEXT',
     'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
    ('LOCATOR_SEVERAL_SCOOTERS_BUTTON', 'LOCATOR_SEVERAL_SCOOTERS_TEXT',
     'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
     'можете просто сделать несколько заказов — один за другим.'),
    ('LOCATOR_TIME_RENT_BUTTON', 'LOCATOR_TIME_RENT_TEXT',
     'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
     'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
     'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
    ('LOCATOR_RENT_TODAY_BUTTON', 'LOCATOR_RENT_TODAY_TEXT',
     'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
    ('LOCATOR_EXTEND_RETURN_BUTTON', 'LOCATOR_EXTEND_RETURN_TEXT',
     'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
    ('LOCATOR_CHARGING_BUTTON', 'LOCATOR_CHARGING_TEXT',
     'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
     'кататься без передышек и во сне. Зарядка не понадобится.'),
    ('LOCATOR_CANCEL_BUTTON', 'LOCATOR_CANCEL_TEXT',
     'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
    ('LOCATOR_MKAD_BUTTON', 'LOCATOR_MKAD_TEXT',
     'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
]


class TestStartPage:

    @allure.title('Проверка ответа на вопрос')
    @pytest.mark.parametrize(
        argnames=['button_locator', 'text_locator', 'expected_result'],
        argvalues=test_cases)
    def test_check_answer(self, driver, button_locator, text_locator, expected_result):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(getattr(LocatorStartPage(), button_locator))
        text = start_page.get_text(getattr(LocatorStartPage(), text_locator))

        assert text == expected_result, f'Ожидаемый результат: {expected_result}, Полученный результат: {text}'
