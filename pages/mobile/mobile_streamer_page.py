import os
import time

from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage
from utils.allure_decorator import allure_step


class MobileStreamerPage(BasePage):
    MAIN_CONTENT = (By.ID, "page-main-content-wrapper")
    LOADER = (By.CLASS_NAME, "tw-loading-spinner")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".modal-close-button")
    PAGE_CONTENT = (By.TAG_NAME, "article")

    @allure_step("Wait for streamer page to fully load")
    def wait_for_page_load(self):
        """
        Wait for the streamer page to be fully loaded by waiting for the loading spinner
        to disappear and handling any modal that might appear
        """
        self.wait_for_element_to_disappear(self.LOADER)
        self.handle_modal_if_present(self.MODAL_CLOSE_BUTTON)

    @allure_step("Take screenshot of current streamer page")
    def take_screenshot(self):
        """
        Take a screenshot of the current streamer page and attach it to the Allure report.
        Saves the screenshot in the allure_screenshots directory with a unique name based
        on the streamer's URL and timestamp.
        
        Returns:
            str: Path to the saved screenshot file, or None if screenshot capture failed
        """
        self.wait_for_page_load()
        name = self.driver.current_url.split("/")[-1]

        try:
            # Create a screenshots directory if it doesn't exist
            screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                         'allure_screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)

            # Generate filename with timestamp
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)

            # Take and save a screenshot
            self.driver.save_screenshot(filepath)

            # Attach to Allure report
            with open(filepath, 'rb') as screenshot:
                allure.attach(
                    screenshot.read(),
                    name=name,
                    attachment_type=allure.attachment_type.PNG
                )

            return filepath
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
            return None

    @allure_step("Check if page content is fully loaded")
    def is_page_fully_loaded(self):
        """
        Checks if the page is fully loaded by verifying the presence of article elements
        in the DOM, which indicates that the main content has been successfully loaded.

        Returns:
            bool: True if the page is fully loaded (article elements are present), False otherwise
        """
        return self.is_element_present(self.PAGE_CONTENT)
