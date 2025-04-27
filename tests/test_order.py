import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

order_data = [
    ("Иван", "Иванов", "ул. Пушкина, 10", "Черкизовская", "89991234567", "25.05.2025", "Позвонить за 30 мин", "black"),
    ("Мария", "Петрова", "ул. Ленина, 5", "Таганская", "89997654321", "26.05.2025", "Оставить у консьержа", "grey"),
]

@pytest.mark.parametrize("name, surname, address, metro, phone, date, comment, color", order_data)
def test_order_scooter_from_top_button(driver, name, surname, address, metro, phone, date, comment, color):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_order_button_top()

    order_page = OrderPage(driver)
    order_page.fill_personal_info(name, surname, address, metro, phone)
    order_page.fill_rent_info(date, comment, color)

    assert order_page.is_success_modal_displayed(), "Модалка об успешном заказе не появилась"

@pytest.mark.parametrize("name, surname, address, metro, phone, date, comment, color", order_data)
def test_order_scooter_from_bottom_button(driver, name, surname, address, metro, phone, date, comment, color):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_order_button_bottom()

    order_page = OrderPage(driver)
    order_page.fill_personal_info(name, surname, address, metro, phone)
    order_page.fill_rent_info(date, comment, color)

    assert order_page.is_success_modal_displayed(), "Модалка об успешном заказе не появилась"