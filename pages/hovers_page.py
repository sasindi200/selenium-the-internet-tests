from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class HoversPage(BasePage):
    figures = (By.CSS_SELECTOR, ".figure")

    def open_hovers(self):
        self.open("hovers")

    def hover_over(self, index):
        figure = self.driver.find_elements(*self.figures)[index]
        ActionChains(self.driver).move_to_element(figure).perform()
        return figure

    def get_caption_text(self, figure):
        caption = figure.find_element(By.CSS_SELECTOR, ".figcaption h5")
        return caption.text

    def get_profile_link_text(self, figure):
        link = figure.find_element(By.CSS_SELECTOR, ".figcaption a")
        return link.text