from playwright.sync_api import Page
import playwright
from playwright.sync_api import sync_playwright
import allure

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url=url)

    def click(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        element.click()
        return True

    def fill(self, locator: str, text: str):
        element = self.page.wait_for_selector(selector=locator)
        element.fill(value=text)

    def get_text(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        return element.inner_text()

    def is_visible(self, locator: str):
        is_element = self.page.wait_for_selector(selector=locator)
        is_element.is_visible()
        if is_element:
            return True
        else:
            raise Exception("Элемент не отобразился на странице")

    def is_clickable(self,locator: str):
        is_element = self.page.wait_for_selector(selector=locator)
        if is_element:
            return True
        else:
            raise Exception("Элемент не кликабелен")

    # def is_disabled(self, locator: str):
    #     is_element = self.page.is_disabled(selector=locator)
    #     if is_element:
    #         return True
    #     else:
    #         raise Exception("Поле активно")

    def get_dropdown_options(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        options = element.query_selector_all("option")
        return [option.text_content() for option in options]

    def select_option(self, locator: str, option_text: str):
        element = self.page.wait_for_selector(selector=locator)
        element.select_option(option_text)

    # def make_screenshot(self, name="Скриншот ошибки"):
    #     screenshot = self.page.screenshot()
    #     allure.attach(name, screenshot, allure.attachment_type.PNG)


