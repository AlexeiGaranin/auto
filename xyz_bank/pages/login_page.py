import allure

from xyz_bank.pages.base_page import BasePage
from xyz_bank.locators import login_page_locators as locator

class LoginPage(BasePage):

    def login_choosing_name(self,  name: str):
        with allure.step("Выбор имени в селекторе 'Your Name'"):
            self.select_option(locator=locator.YOUR_NAME_SELECTOR, option_text=name)
            if self.click(locator=locator.LOGIN_BTN):
                return True
            else:
                return False


    def home_click(self):
        with allure.step("Нажатие на кнопку 'Home' и проверка отображения кнопок на странице 'Home'"):
            self.click(locator=locator.HOME_BTN)
            if self.is_visible(locator="//button[text()='Customer Login']") and self.is_visible("//button[text()='Bank Manager Login']"):
                return True
            else:
                return False
