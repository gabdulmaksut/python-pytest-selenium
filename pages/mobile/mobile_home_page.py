
from pages.base_page import BasePage
from utils.allure_decorator import allure_step


class MobileHomePage(BasePage):
    PAGE_URL = "/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure_step("Open Twitch mobile homepage")
    def open(self):
        """Open Twitch homepage by navigating to the base URL"""
        self.go_to_url(self.PAGE_URL)
        return self