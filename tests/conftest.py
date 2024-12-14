from selene import browser
from selenium import webdriver
import pytest
import allure


@pytest.fixture(autouse=True)
def setting():
    with  allure.step("Задаем параметры браузера"):
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.driver_options = driver_options
        browser.config.window_height = 2560
        browser.config.window_width = 1440
    with  allure.step("Открываем главную страницу github"):
        browser.open("https://github.com")

        yield

    with  allure.step("Закрываем браузер"):
        browser.quit()


