from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddRemovePage(BasePage):
    add_button = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    delete_buttons = (By.CSS_SELECTOR, ".added-manually")

    def open_add_remove(self):
        self.open("add_remove_elements/")

    def add_element(self):
        self.driver.find_element(*self.add_button).click()

    def get_delete_button_count(self):
        return len(self.driver.find_elements(*self.delete_buttons))

    def delete_first_element(self):
        self.driver.find_elements(*self.delete_buttons)[0].click()