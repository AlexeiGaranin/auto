from xyz_bank.pages.base_page import BasePage
from xyz_bank.locators import home_page_locators as locator
import allure

class HomePage(BasePage):


    def click_login_btn(self):
        try:
            self.click(locator=locator.CUSTOMER_LOGIN_BTN)
            return True
        except Exception:
            return False

    def click_manager_btn(self):
        try:
            self.click(locator=locator.BANK_MANAGER_LOGIN_BTN)
            return True
        except Exception:
            return False

