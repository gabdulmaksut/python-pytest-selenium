from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage
from pages.mobile.mobile_streamer_page import MobileStreamerPage
from utils.allure_decorator import allure_step


class MobileSearchResultsPage(BasePage):
    # Locators
    STREAMER_LINK = (By.CSS_SELECTOR, "article a[href*='/'][href$='/home']")
    STREAMER_AVATAR = (By.CSS_SELECTOR, ".tw-avatar img.tw-image-avatar")

    def __init__(self, driver):
        super().__init__(driver)

    @allure_step("Scroll through search results")
    def scroll_results(self, max_scrolls=3):
        """
        Scroll through the search results page to load more content
        Args:
            max_scrolls (int): Maximum number of scroll attempts
        """
        scroll_count = 0
        last_height = self.get_page_height()

        while scroll_count < max_scrolls:
            self.scroll_page(2000)
            time.sleep(1)  # Short pause to allow content to load
            new_height = self.get_page_height()
            if new_height == last_height:
                break

            last_height = new_height
            scroll_count += 1

    @allure_step("Select first visible streamer")
    def select_first_visible_on_screen_streamer(self):
        """
        Selects the first streamer that is currently visible in the viewport
        without scrolling to it
        Raises:
            TimeoutException: If no visible streamer is found
        """
        # Get all streamer elements
        streamers = self.driver.find_elements(*self.STREAMER_LINK)

        # Find the first visible streamer
        visible_streamer = None
        for streamer in streamers:
            if self.is_element_in_viewport(streamer):
                visible_streamer = streamer
                break

        if visible_streamer is None:
            raise TimeoutException("No visible streamers found on screen")

        # Click the first visible streamer
        visible_streamer.click()
        return MobileStreamerPage(self.driver)
