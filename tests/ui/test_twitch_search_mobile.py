import pytest
import allure

from pages.common_elements.navigation_mobile import NavigationMobile
from pages.mobile.mobile_home_page import MobileHomePage


@allure.feature("Stream Search")
@allure.story("Mobile search and viewing StarCraft II streamer")
class TestMobileTwitchSearch:
    @pytest.mark.mobile
    @pytest.mark.parametrize("search_query, category_link", [
        ("StarCraft II", "starcraft-ii"),
    ])
    @allure.title("Test searching for streamer '{search_query}' and selecting '{expected_streamer_keyword}' on mobile version")
    def test_mobile_starcraft_search_and_select_streamer(self, driver, search_query, category_link):
        # Initialize Page Objects
        home_page = MobileHomePage(driver)
        navigation = NavigationMobile(driver)

        # Actions (Steps)
        home_page.open()
        browse_page = navigation.click_browse()
        browse_page.enter_search_query(search_query)
        search_results_page = browse_page.select_category(category_link)
        search_results_page.scroll_results(2)
        streamer_page = search_results_page.select_first_visible_on_screen_streamer()
        streamer_page.take_screenshot()

        # Assertion
        assert streamer_page.is_page_fully_loaded(), "Page did not load completely"
