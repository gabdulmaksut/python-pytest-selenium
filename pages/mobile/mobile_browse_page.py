from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.mobile.mobile_search_results_page import MobileSearchResultsPage
from utils.allure_decorator import allure_step


class MobileBrowsePage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search'][data-a-target='tw-input']")
    PAGE_URL = "/directory"
    CATEGORY_LINK = "a[href='/directory/category/{link}']"

    def __init__(self, driver):
        super().__init__(driver)

    @allure_step("Open Browse Page")
    def open(self):
        """Open Browse Page by navigating to the directory URL"""
        self.go_to_url(self.PAGE_URL)
        return self

    @allure_step("Enter search query: {query}")
    def enter_search_query(self, query):
        """Enter text into the search field and clear any existing text"""
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)

    @allure_step("Select category: {link}")
    def select_category(self, link):
        """Select a category from the available options by clicking on its link"""
        category_selector = self.CATEGORY_LINK.format(link=link)
        category_element = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, category_selector))
        )
        category_element.click()
        return MobileSearchResultsPage(self.driver)

