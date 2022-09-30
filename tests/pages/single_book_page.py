import time

from selenium.webdriver.common.by import By

from config.config import TestData
from pages.base_page import BasePage


class SingleBookPage(BasePage):
    """By locators"""
    EDIT_BUTTON = By.XPATH, "//a[contains(@class, 'MuiButton-containedSuccess')]"
    DELETE_BUTTON = By.XPATH, "//button[contains(@class, 'MuiButton-containedError')]"
    CONFIRMATION_BUTTON = By.XPATH, "//button[contains(. ,'Yes, delete it!')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f'{TestData.BASE_URL}/books/view/{TestData.BOOK_ID}')

    def is_edit_button_redirecting_correctly(self):
        self.do_click(self.EDIT_BUTTON)
        return self.get_current_url()

    def do_delete_book(self):
        self.do_click(self.DELETE_BUTTON)
        time.sleep(0.5)

        self.do_click(self.CONFIRMATION_BUTTON)
        time.sleep(0.5)

        return self.get_current_url()
