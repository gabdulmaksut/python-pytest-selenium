
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.mobile.mobile_browse_page import MobileBrowsePage
from pages.mobile.mobile_home_page import MobileHomePage


class NavigationMobile(BasePage):
    # Mobile navigation bar locators
    NAV_HOME = (By.CSS_SELECTOR, "a[href='/']")
    NAV_BROWSE = (By.CSS_SELECTOR, "a[href='/directory']")
    NAV_ACTIVITY = (By.CSS_SELECTOR, "a[href='/activity']")
    NAV_PROFILE = (By.CSS_SELECTOR, "a[href='/home']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_home(self):
        """Click the home navigation button"""
        home_button = self.find_element(self.NAV_HOME)
        home_button.click()
        return MobileHomePage(self.driver)

    def click_browse(self):
        """Click the browse navigation button"""
        browse_button = self.find_element(self.NAV_BROWSE)
        browse_button.click()
        return MobileBrowsePage(self.driver)
