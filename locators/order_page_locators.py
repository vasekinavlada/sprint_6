from selenium.webdriver.common.by import By

class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CLASS_NAME, "select-search__input")
    METRO_LIST = (By.CLASS_NAME, "select-search__option")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Далее')]")

    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_RENT_TIME = (By.CLASS_NAME, "Dropdown-control")
    RENT_TIME_ONE_DAY = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='сутки']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "//button[contains(text(),'Заказать')]")
    BUTTON_CONFIRM_ORDER = (By.XPATH, "//button[contains(text(),'Да')]")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")