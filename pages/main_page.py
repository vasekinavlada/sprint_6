from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_faq_question(self, index):
        question = self.driver.find_elements(*MainPageLocators.FAQ_QUESTIONS)[index]
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    def is_faq_answer_visible(self, index):
        try:
            answer = self.driver.find_elements(*MainPageLocators.FAQ_ANSWERS)[index]
            return answer.is_displayed()
        except IndexError:
            return False

    def click_order_button_top(self):
        order_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_TOP)
        )
        order_button.click()

    def click_order_button_bottom(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",
            self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM))
        order_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)
        )
        order_button.click()

    def click_scooter_logo(self):
        logo = self.driver.find_element(*MainPageLocators.SCOOTER_LOGO)
        logo.click()

    def click_yandex_logo(self):
        logo = self.driver.find_element(*MainPageLocators.YANDEX_LOGO)
        logo.click()