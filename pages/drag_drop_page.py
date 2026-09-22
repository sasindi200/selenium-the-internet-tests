from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class DragDropPage(BasePage):
    column_a = (By.ID, "column-a")
    column_b = (By.ID, "column-b")

    def open_drag_drop(self):
        self.open("drag_and_drop")

    def drag_a_to_b(self):
        source = self.driver.find_element(*self.column_a)
        target = self.driver.find_element(*self.column_b)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def get_column_a_text(self):
        return self.driver.find_element(*self.column_a).text

    def get_column_b_text(self):
        return self.driver.find_element(*self.column_b).text