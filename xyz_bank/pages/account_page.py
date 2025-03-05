from xyz_bank.pages.base_page import BasePage
from xyz_bank.locators import account_page_locator as locator

class AccountPage(BasePage):

    def get_list_account_number(self):
        l_number = self.get_dropdown_options(locator=locator.ACCOUNT_NUMBER_SELECT)
        self.select_option(locator=locator.ACCOUNT_NUMBER_SELECT, option_text=l_number[1])
        return self.get_text(locator=locator.ACCOUNT_NUMBER)


    def account_action(self, button_locator: str, value: int):
        self.page.wait_for_timeout(500)
        self.click(locator=button_locator)
        self.fill(locator=locator.FIELD, text=str(value))
        self.click(locator=locator.ACTHION_BTN)
        self.page.wait_for_timeout(1500)

    def get_account_balance(self):
        return int(self.get_text(locator=locator.ACCOUNT_BALANCE))

    def get_action_msg_result(self):
        return self.get_text(locator=locator.ACTHION_MSG)