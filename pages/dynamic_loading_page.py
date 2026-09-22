from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    start_button = (By.CSS_SELECTOR, "#start button")
    finish_text = (By.ID, "finish")

    def open_example(self, example_num):
        self.open(f"dynamic_loading/{example_num}")

    def start(self):
        self.driver.find_element(*self.start_button).click()

    def get_finish_text(self):
        return self.wait_visible(self.finish_text).text