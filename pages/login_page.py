from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    flash_message = (By.CSS_SELECTOR, "#flash")

    def open_login(self):
        self.open("login")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

    def get_flash_text(self):
        return self.wait_visible(self.flash_message).text

    def wait_for_secure_url(self):
        self.wait.until(EC.url_contains("secure"))