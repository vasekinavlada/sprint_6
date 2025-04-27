import pytest
from pages.faq_page import FAQPage

faq_data = [
    (0, "Сколько это стоит? И как оплатить?"),
    (1, "Хочу сразу несколько самокатов! Так можно?"),
    (2, "Как рассчитывается время аренды?"),
    (3, "Можно ли заказать самокат прямо на сегодня?"),
    (4, "Можно ли продлить заказ или вернуть самокат раньше?"),
    (5, "Вы привозите зарядку вместе с самокатом?"),
    (6, "Можно ли отменить заказ?"),
    (7, "Я живу за МКАДом, привезёте?"),
]


@pytest.mark.parametrize("index, expected_text", faq_data)
def test_faq_question_expand_and_collapse(driver, index, expected_text):
    page = FAQPage(driver)
    driver.get('https://qa-scooter.praktikum-services.ru/')

        # Клик — открыть ответ
    page.click_question(index)
    assert page.is_answer_displayed(index), f"Ответ на вопрос {index} не открылся."
    assert expected_text in page.get_answer_text(index), f"Ответ текста не совпадает для вопроса {index}."

        # Клик — закрыть ответ
    page.click_question(index)
    assert not page.is_answer_displayed(index), f"Ответ на вопрос {index} не закрылся."