from selenium.webdriver.common.by import By


class LocatorOrderPage:
    LOCATOR_ORDER_HEADER = (By.XPATH, ".//div[@class='Order_Header__BZXOb']")  # "Для кого самокат"
    LOCATOR_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")  # Поле для ввода имени
    LOCATOR_LASTNAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")  # Поле для ввода фамилии
    LOCATOR_ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле для ввода адреса
    LOCATOR_METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")  # Поле для ввода метро
    LOCATOR_PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле для ввода телефона
    LOCATOR_NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")  # кнопка 'Далее'
    LOCATOR_DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  # Поле для ввода даты
    LOCATOR_DATE_SELECT = (By.CLASS_NAME, 'react-datepicker__day--selected')  # Выбрать дату
    LOCATOR_COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")  # Поле для ввода комментария
    LOCATOR_SELECT = (By.XPATH, ".//div[@class='select-search__select']/*")  # Выбрать срок
    LOCATOR_DROPDOWN = (By.XPATH, ".//div[text()='* Срок аренды']")  # выпадающий список со сроками
    LOCATOR_DROPDOWN_MENU = (By.CLASS_NAME, 'Dropdown-menu')  # меню выпадающего списка
    LOCATOR_DROPDOWN_OPTION = (By.CLASS_NAME, 'Dropdown-option')  # элемент выпадающего списка
    LOCATOR_BLACK_COLOR = (By.ID, 'black')  # чекбокс "черный жемчуг"
    LOCATOR_GREY_COLOR = (By.ID, 'grey')  # чекбокс "серая безысходность"
    LOCATOR_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")  # кнопка заказать
    LOCATOR_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')  # кнопка куки
    LOCATOR_AGREE_BUTTON = (By.XPATH, ".//button[text()='Да']")  # кнопка куки
    LOCATOR_MODAL_HEADER = (By.XPATH, ".//div[text()='Заказ оформлен']")  # заголовок "Заказ оформлен"
