from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_click_scooter_logo_navigates_to_main(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_order_button_top()
    main_page.click_scooter_logo()

    assert "qa-scooter.praktikum-services.ru" in driver.current_url, "Не перешли на главную страницу Самоката"

def test_click_yandex_logo_opens_dzen(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_yandex_logo()

    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 5).until(EC.url_contains("dzen.ru"))

    assert "dzen.ru" in driver.current_url, "Страница Дзена не открылась"