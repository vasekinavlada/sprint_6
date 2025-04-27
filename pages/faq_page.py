from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class FAQPage:
    def __init__(self, driver):
        self.driver = driver

    def click_question(self, index):
        question = self.driver.find_element(By.ID, f"accordion__heading-{index}")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        ActionChains(self.driver).move_to_element(question).perform()
        question.click()

    def is_answer_displayed(self, index):
        answer = self.driver.find_element(By.ID, f"accordion__panel-{index}")
        return answer.is_displayed()

    def get_answer_text(self, index):
        answer = self.driver.find_element(By.ID, f"accordion__panel-{index}")
        return answer.text