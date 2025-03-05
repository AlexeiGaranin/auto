import pytest
import playwright
import time
from xyz_bank.locators import login_page_locators as locator
import allure

@allure.feature('Login page')
@allure.story('Загрузка страницы')
def test_login_page_loads(login_page):
    allure.dynamic.title("Проверка загрузки страницы login page")
    with allure.step("Отображение селектора 'Your Name'"):
        assert login_page.is_visible(locator=locator.YOUR_NAME_SELECTOR), "Селектор 'Your Name' не отображается на странице"

@allure.feature('Login page')
@allure.story('Основная функциональность страницы')
def test_login_hp(login_page):
    allure.dynamic.title("Проверка авторизации hp")
    assert login_page.login_choosing_name("Harry Potter"), "Возникла ошибка при авторизации"
    with allure.step("Отображением кнопки 'Log out'"):
        assert login_page.is_visible("//button[text()='Logout']"), "Кнопка 'Logout' не была найдена на странице"

@allure.feature('Login page')
@allure.story('Основная функциональность страницы')
def test_go_home_from_login(login_page):
    allure.dynamic.title("Проверка перехода по кнопке 'Home'")
    assert login_page.home_click(), "При переходе по нажатию кнопку Home произошла ошибка"


@allure.feature('Login page')
@allure.story('Основная функциональность страницы')
def test_login_btn_hidin(login_page, page):
    allure.dynamic.title("Проверка скрытия элемента кнопки 'Log in'")
    with allure.step("Выбор пользователя из выпадающего списка 'Your Name'"):
        login_page.select_option(locator=locator.YOUR_NAME_SELECTOR, option_text="Harry Potter")
    with allure.step("Выбор пустого значения из выпадающего списка 'Your Name'"):
        login_page.select_option(locator=locator.YOUR_NAME_SELECTOR, option_text="")
    with allure.step("Проверка, что кнопка 'Log in' не отображается на странице"):
        assert page.is_hidden(locator.LOGIN_BTN) == True, "Кнопка 'Log in' не спряталась"
