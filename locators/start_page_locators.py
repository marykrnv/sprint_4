from selenium.webdriver.common.by import By


class LocatorStartPage:
    LOCATOR_QUESTIONS = (By.XPATH, ".//div[contains(text(),'Вопросы о важном')]")  # "Вопросы о важном"

    LOCATOR_PRICE_BUTTON = (By.ID, "accordion__heading-0")  # Сколько это стоит? И как оплатить?
    LOCATOR_SEVERAL_SCOOTERS_BUTTON = (By.ID, "accordion__heading-1")  # Хочу сразу несколько самокатов! Так можно?
    LOCATOR_TIME_RENT_BUTTON = (By.ID, "accordion__heading-2")  # Как рассчитывается время аренды?
    LOCATOR_RENT_TODAY_BUTTON = (By.ID, "accordion__heading-3")  # Можно ли заказать самокат прямо на сегодня?
    LOCATOR_EXTEND_RETURN_BUTTON = (By.ID, "accordion__heading-4")  # Можно ли продлить заказ или вернуть самокат раньше?
    LOCATOR_CHARGING_BUTTON = (By.ID, "accordion__heading-5")  # Вы привозите зарядку вместе с самокатом?
    LOCATOR_CANCEL_BUTTON = (By.ID, "accordion__heading-6")  # Можно ли отменить заказ?
    LOCATOR_MKAD_BUTTON = (By.ID, "accordion__heading-7")  # Я жизу за МКАДом, привезёте?

    LOCATOR_PRICE_TEXT = (By.ID, "accordion__panel-0")  # Ответ: Сколько это стоит? И как оплатить?
    LOCATOR_SEVERAL_SCOOTERS_TEXT = (By.ID, "accordion__panel-1")  # Ответ: Хочу сразу несколько самокатов! Так можно?
    LOCATOR_TIME_RENT_TEXT = (By.ID, "accordion__panel-2")  # Ответ: Как рассчитывается время аренды?
    LOCATOR_RENT_TODAY_TEXT = (By.ID, "accordion__panel-3")  # Ответ: Можно ли заказать самокат прямо на сегодня?
    LOCATOR_EXTEND_RETURN_TEXT = (By.ID, "accordion__panel-4")  # Ответ: Можно ли продлить заказ или вернуть самокат раньше?
    LOCATOR_CHARGING_TEXT = (By.ID, "accordion__panel-5")  # Ответ: Вы привозите зарядку вместе с самокатом?
    LOCATOR_CANCEL_TEXT = (By.ID, "accordion__panel-6")  # Ответ: Можно ли отменить заказ?
    LOCATOR_MKAD_TEXT = (By.ID, "accordion__panel-7")  # Ответ: Я жизу за МКАДом, привезёте?

    LOCATOR_HEADER_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")  # Кнопка Заказать в хедере
    LOCATOR_HOW_IT_WORKS_ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка Заказать в блоке 'Как это работает'
    LOCATOR_MAIN_HEADER = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")  # заголовок 'Самокат'
