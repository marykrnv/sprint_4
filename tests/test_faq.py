import allure

from locators.start_page_locators import LocatorStartPage
from pages.start_page import StartPage


class TestStartPage:

    @staticmethod
    @allure.title('Проверка ответа на вопрос Сколько это стоит? И как оплатить?')
    def test_check_answer_price(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_PRICE_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_PRICE_TEXT)

        assert text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @staticmethod
    @allure.title('Проверка ответа на вопрос Хочу сразу несколько самокатов! Так можно?')
    def test_check_answer_several_scooter(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_SEVERAL_SCOOTERS_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_SEVERAL_SCOOTERS_TEXT)

        assert text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, ' \
                       'можете просто сделать несколько заказов — один за другим.'

    @staticmethod
    @allure.title('Проверка ответа на вопрос Как рассчитывается время аренды?')
    def test_check_answer_time_rent(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_TIME_RENT_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_TIME_RENT_TEXT)

        assert text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
                       'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                       'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @staticmethod
    @allure.title('Проверка ответа на вопрос Можно ли заказать самокат прямо на сегодня?')
    def test_check_answer_rent_today(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_RENT_TODAY_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_RENT_TODAY_TEXT)

        assert text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @staticmethod
    @allure.title('Проверка ответа на вопрос Можно ли продлить заказ или вернуть самокат раньше?')
    def test_check_answer_extend_return(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_EXTEND_RETURN_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_EXTEND_RETURN_TEXT)

        assert text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому ' \
                       'номеру 1010.'

    @staticmethod
    @allure.title('Проверка ответа на вопрос Вы привозите зарядку вместе с самокатом?')
    def test_check_answer_charging(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_CHARGING_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_CHARGING_TEXT)

        assert text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете ' \
                       'кататься без передышек и во сне. Зарядка не понадобится.'

    @staticmethod
    @allure.title('Проверка ответа на вопрос Можно ли отменить заказ?')
    def test_check_answer_cancel(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_CANCEL_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_CANCEL_TEXT)

        assert text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. ' \
                       'Все же свои.'

    @staticmethod
    @allure.title('Проверка ответа на вопрос Я жизу за МКАДом, привезёте?')
    def test_check_answer_mkad(driver):
        start_page = StartPage(driver)
        start_page.go_to_web()
        start_page.scroll_to_questions()
        start_page.click_on_accordion_button(LocatorStartPage.LOCATOR_MKAD_BUTTON)
        text = start_page.get_text(LocatorStartPage.LOCATOR_MKAD_TEXT)

        assert text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
