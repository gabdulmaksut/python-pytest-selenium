# pages/base_page.py
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config
import allure
from utils.allure_decorator import allure_step

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)

    @allure_step("Navigate to URL: {url}")
    def go_to_url(self, url):
        """Navigate to the specified URL by appending it to the base URL"""
        self.driver.get(Config.BASE_URL+url)

    @allure_step("Find element")
    def find_element(self, by_locator):
        """Find an element on the page with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(by_locator))

    @allure_step("Check if element is in viewport")
    def is_element_in_viewport(self, element: WebElement) -> bool:
        """
        Checks if an element is currently visible in the viewport
        without scrolling to it

        Args:
            element: WebElement to check
        Returns:
            bool: True if an element is in viewport
        """
        return self.driver.execute_script("""
                 var elem = arguments[0];
                 var rect = elem.getBoundingClientRect();
                 return (
                     rect.top >= 0 &&
                     rect.left >= 0 &&
                     rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                     rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                 );
             """, element)

    @allure_step("Check if element is present")
    def is_element_present(self, by_locator):
        """Check if an element is present on the page"""
        try:
            self.wait.until(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    @allure_step("Wait for element to disappear")
    def wait_for_element_to_disappear(self, by_locator, timeout=10):
        """Wait for an element to disappear from the page"""
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(by_locator)
            )
            return True
        except Exception as e:
            allure.attach(str(e), name="Element did not disappear", attachment_type=allure.attachment_type.TEXT)
            return False

    @allure_step("Wait for element to appear")
    def wait_for_element(self, by_locator, timeout=10):
        """Wait for an element to appear on the page"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
        except TimeoutException:
            return None

    @allure_step("Enter text: {text}")
    def send_keys_to_element(self, by_locator, text):
        """Enter text into an element"""
        self.find_element(by_locator).send_keys(text)

    @allure_step("Scroll page by {scroll_amount} pixels")
    def scroll_page(self, scroll_amount=200):
        """
        Safely scroll the page by the specified amount
        Args:
            scroll_amount (int): Number of pixels to scroll vertically
        """
        try:
            script = "window.scrollTo(0, window.pageYOffset + arguments[0]);"
            self.driver.execute_script(script, scroll_amount)
        except:
            # If JavaScript scrolling fails, try an alternative method
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure_step("Get page height")
    def get_page_height(self):
        """Get the total height of the page"""
        return self.driver.execute_script("return document.documentElement.scrollHeight")

    @allure_step("Get current scroll position")
    def get_current_scroll_position(self):
        """Get the current scroll position"""
        return self.driver.execute_script("return window.pageYOffset")

    @allure_step("Handle modal if present")
    def handle_modal_if_present(self, modal_close_button, timeout=5):
        """
        Check for and close a modal if it appears within the specified timeout.
        Args:
            modal_close_button (tuple): Locator tuple (By.XX, "selector") for the modal close button
            timeout (int): Maximum time to wait for modal to appear, defaults to 5 seconds
        """
        try:
            # Wait for modal close button with shorter timeout
            close_button = self.wait_for_element(modal_close_button, timeout=timeout)
            if close_button and close_button.is_displayed():
                close_button.click()
                # Wait for modal to disappear
                self.wait_for_element_to_disappear(modal_close_button)
        except:
            # If no modal appears, just continue
            pass
