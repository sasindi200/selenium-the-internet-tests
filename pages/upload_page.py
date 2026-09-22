from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UploadPage(BasePage):
    file_input = (By.ID, "file-upload")
    upload_button = (By.ID, "file-submit")
    uploaded_filename = (By.ID, "uploaded-files")

    def open_upload(self):
        self.open("upload")

    def upload_file(self, file_path):
        self.driver.find_element(*self.file_input).send_keys(file_path)
        self.driver.find_element(*self.upload_button).click()

    def get_uploaded_filename(self):
        return self.wait_visible(self.uploaded_filename).text