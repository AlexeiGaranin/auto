from math import gamma
import pytest
import playwright
import time
from xyz_bank.locators import account_page_locator as locator



def test_account_page_loads(account_page):
    assert account_page.is_visible(locator=locator.LOGOUT_BTN), "Кнопка 'LOGOUT' не отображается на странице"

def test_logout(account_page):
    assert account_page.click(locator=locator.LOGOUT_BTN), "Кнопка 'LOGOUT' не была нажата"
    assert account_page.is_visible("//select[@id='userSelect']"), "Селектор 'Your Name' не отображается на странице"


def test_change_account_number(account_page):
    old_number = account_page.get_text(locator=locator.ACCOUNT_NUMBER)
    actual_number = account_page.get_list_account_number()
    expected_number = account_page.get_text(locator=locator.ACCOUNT_NUMBER)
    assert actual_number.strip() == expected_number.strip(), f"Изменили с {old_number}, на {actual_number}. А пришёл {expected_number}"


def test_withdrawn_more_than_balance(account_page):
    account_page.account_action(locator.WITHDRAWL_BIG_BTN, 5)
    actual = account_page.get_action_msg_result()
    expected = "Transaction Failed. You can not withdraw amount more than the balance."
    assert actual == expected, f"Тест ошибки ОР: {expected}, а пришёл ФР: {actual}"

def test_deposit(account_page):
    old_value = account_page.get_account_balance()
    deposit_amount = 10
    account_page.account_action(locator.DEPOSIT_BIG_BTN, deposit_amount)
    assert account_page.get_action_msg_result() == "Deposit Successful", "Сообщение об успешной операции не получено, или отличается от: Deposit Successful"
    expected_value = old_value + deposit_amount
    actual_value = account_page.get_account_balance()
    assert actual_value == expected_value, f"Изменили с {old_value}, на {actual_value}. А пришёл {expected_value}"

def test_withdrawn(account_page, page):
    account_page.account_action(locator.DEPOSIT_BIG_BTN, 10)
    old_value = account_page.get_account_balance()
    account_page.click(locator=locator.WITHDRAWL_BIG_BTN)
    withdrawn_amount = 2
    account_page.account_action(locator.WITHDRAWL_BIG_BTN, withdrawn_amount)
    assert account_page.get_action_msg_result() == "Transaction successful", "Сообщение об успешной операции не получено, или отличается от: Transaction successful"
    expected_value = old_value - withdrawn_amount
    actual_value = account_page.get_account_balance()
    assert actual_value == expected_value, f"Изменили с {old_value}, на {actual_value}. А пришёл {expected_value}"

def test_transactions(account_page, page):
    deposit_amount = 10
    account_page.account_action(locator.DEPOSIT_BIG_BTN, deposit_amount)
    account_page.click(locator=locator.WITHDRAWL_BIG_BTN)
    withdrawn_amount = 2
    account_page.account_action(locator.WITHDRAWL_BIG_BTN, withdrawn_amount)
    account_page.click(locator=locator.TRANSACTIONS_BIG_BTN)
    expected_amount_credit = int(account_page.get_text("//tr[@id='anchor0']/td[2]"))
    expected_amount_debit = int(account_page.get_text("//tr[@id='anchor1']/td[2]"))
    assert deposit_amount == expected_amount_credit, f"Изменили на {deposit_amount}, а в таблице {expected_amount_credit}"
    assert account_page.get_text("//tr[@id='anchor0']/td[3]") == "Credit", "Ожидали операцию Credit, а в таблице иное значение"
    assert withdrawn_amount == expected_amount_debit, f"Изменили на {withdrawn_amount}, а в таблице {expected_amount_debit}"
    assert account_page.get_text("//tr[@id='anchor1']/td[3]") == "Debit", "Ожидали операцию Debit, а в таблице иное значение"

def test_transactions_reset(account_page, page):
    account_page.account_action(locator.DEPOSIT_BIG_BTN, 10)
    account_page.click(locator=locator.TRANSACTIONS_BIG_BTN)
    old_record = account_page.is_visible("//tr[@id='anchor0']")
    account_page.click(locator=locator.RESET_BTN)
    new_record = page.is_visible("//tr[@id='anchor0']")
    assert old_record != new_record, "После нажатия на Reset ожидали полную очистку, но был найдена запись таблицы"
    account_page.click(locator=locator.BACK_BTN)
    assert 0 == account_page.get_account_balance(), "Ожидали 0, а пришло другое значение"

def test_go_home_from_account(account_page, login_page):
    assert login_page.home_click(), "При переходе по нажатию кнопку Home произошла ошибка"






