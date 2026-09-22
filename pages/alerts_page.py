from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlertsPage(BasePage):
    js_alert_button = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    js_confirm_button = (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    result_text = (By.ID, "result")

    def open_alerts(self):
        self.open("javascript_alerts")

    def trigger_alert(self):
        self.driver.find_element(*self.js_alert_button).click()

    def trigger_confirm(self):
        self.driver.find_element(*self.js_confirm_button).click()

    def accept_alert(self):
        self.wait.until(lambda d: d.switch_to.alert)
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.wait.until(lambda d: d.switch_to.alert)
        self.driver.switch_to.alert.dismiss()

    def get_result_text(self):
        return self.wait_visible(self.result_text).text