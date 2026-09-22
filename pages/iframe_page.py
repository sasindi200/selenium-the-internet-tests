from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class IframePage(BasePage):
    iframe = (By.ID, "mce_0_ifr")
    editor_body = (By.ID, "tinymce")

    def open_iframe(self):
        self.open("iframe")

    def clear_and_type(self, text):
        self.driver.switch_to.frame(self.driver.find_element(*self.iframe))
        body = self.wait_visible(self.editor_body)
        self.driver.execute_script(
            "arguments[0].innerHTML = arguments[1];", body, f"<p>{text}</p>"
        )
        self.driver.switch_to.default_content()

    def get_editor_text(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.iframe))
        text = self.driver.find_element(*self.editor_body).text
        self.driver.switch_to.default_content()
        return text