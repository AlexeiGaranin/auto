import allure
import pytest
import playwright
import time
from xyz_bank.locators import home_page_locators as locator

@allure.feature('Home page')
@allure.story('Загрузка страницы')
def test_home_page_loads(home_page):
    allure.dynamic.title("Проверка загрузки страницы login page")
    with allure.step("Отображение кнопки 'Customer Login'"):
        assert home_page.is_visible(locator=locator.CUSTOMER_LOGIN_BTN), "Кнопка 'CUSTOMER_LOGIN_BTN' не отображается на странице"
    with allure.step("Отображение кнопки 'Bank Manager Login'"):
        assert home_page.is_visible(locator=locator.BANK_MANAGER_LOGIN_BTN), "Кнопка 'BANK_MANAGER_LOGIN_BTN' не отображается на странице"

@allure.feature('Home page')
@allure.story('Основная функциональность страницы')
def test_navigation_to_login_page(home_page):
    allure.dynamic.title("Проверка перехода и загрузки страницы login page")
    with allure.step("Нажатие кнопки 'Customer Login'"):
        assert home_page.click_login_btn(), "Кнопка 'CUSTOMER_LOGIN_BTN' не была нажата"
    with allure.step("Отображение селектора 'Your Name'"):
        assert home_page.is_visible("//select[@id='userSelect']"), "Селектор 'Your Name' не отображается на странице"


@allure.feature('Home page')
@allure.story('Основная функциональность страницы')
def test_navigation_to_manager_page(home_page):
    allure.dynamic.title("Проверка перехода и загрузки страницы manager page")
    with allure.step("Нажатие кнопки 'Customer Login'"):
        assert home_page.click_manager_btn(), "Кнопка 'Bank Manager Login' не была нажата"
    with allure.step("Отображение кнопки 'Add Customer'"):
        assert home_page.is_visible("//button[contains(text(), 'Add Customer')]"), "Кнопка 'Add Customer' не отображается на странице"

