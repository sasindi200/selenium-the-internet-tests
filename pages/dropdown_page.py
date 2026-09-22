from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    dropdown = (By.ID, "dropdown")

    def open_dropdown(self):
        self.open("dropdown")

    def select_option_by_text(self, text):
        select = Select(self.driver.find_element(*self.dropdown))
        select.select_by_visible_text(text)

    def get_selected_option_text(self):
        select = Select(self.driver.find_element(*self.dropdown))
        return select.first_selected_option.text