import playwright
import pytest
from playwright.sync_api import sync_playwright
from xyz_bank.pages.home_page import HomePage
from xyz_bank.pages.login_page import LoginPage
from xyz_bank.pages.account_page import AccountPage
import allure

from xyz_bank.pages.base_page import BasePage


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    page.goto(url="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    yield page
    page.close()

@pytest.fixture()
def home_page(page):
    return HomePage(page)

@pytest.fixture()
def login_page(home_page, page):
    home_page.click_login_btn()
    return LoginPage(page)

@pytest.fixture()
def account_page(login_page, page):
    login_page.login_choosing_name(name="Harry Potter")
    return AccountPage(page)


