from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WindowsPage(BasePage):
    new_window_link = (By.CSS_SELECTOR, "a[href='/windows/new']")

    def open_windows(self):
        self.open("windows")

    def click_new_window(self):
        self.driver.find_element(*self.new_window_link).click()

    def switch_to_new_window(self):
        original = self.driver.current_window_handle
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != original:
                self.driver.switch_to.window(handle)
                break

    def get_new_window_title(self):
        return self.driver.title