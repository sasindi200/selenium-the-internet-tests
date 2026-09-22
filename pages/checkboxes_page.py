from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    checkboxes = (By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    def open_checkboxes(self):
        self.open("checkboxes")

    def get_checkboxes(self):
        return self.driver.find_elements(*self.checkboxes)

    def toggle_checkbox(self, index):
        self.get_checkboxes()[index].click()

    def is_checked(self, index):
        return self.get_checkboxes()[index].is_selected()