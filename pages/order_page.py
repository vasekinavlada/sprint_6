from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_personal_info(self, name, surname, address, metro, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

        self.driver.find_element(*OrderPageLocators.INPUT_METRO).click()
        metro_options = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(OrderPageLocators.METRO_LIST)
        )
        for option in metro_options:
            if metro.lower() in option.text.lower():
                option.click()
                break

        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    def fill_rent_info(self, date, comment, color):
        self.driver.find_element(*OrderPageLocators.INPUT_DATE).send_keys(date)
        self.driver.find_element(*OrderPageLocators.DROPDOWN_RENT_TIME).click()
        self.driver.find_element(*OrderPageLocators.RENT_TIME_ONE_DAY).click()

        if color == "black":
            self.driver.find_element(*OrderPageLocators.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*OrderPageLocators.COLOR_GREY).click()

        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_CONFIRM_ORDER)
        ).click()

    def is_success_modal_displayed(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)
        ).is_displayed()