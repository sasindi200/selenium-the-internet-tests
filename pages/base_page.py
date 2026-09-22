from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = "https://the-internet.herokuapp.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, path=""):
        self.driver.get(f"{self.URL}/{path}")

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))