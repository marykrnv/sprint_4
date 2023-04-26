from selenium.webdriver.common.by import By


class LocatorBase:
    LOCATOR_SAMOKAT_BUTTON = (By.XPATH, ".//a[@href='/']")
    LOCATOR_YA_BUTTON = (By.XPATH, ".//a[@href='//yandex.ru']")
