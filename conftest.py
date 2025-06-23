import pytest
from typing import Generator
from selenium.webdriver.remote.webdriver import WebDriver
from utils.driver_factory import DriverFactory, MOBILE_DEVICES


def pytest_addoption(parser):
    """Add command-line options for test configuration"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (default: chrome)"
    )
    parser.addoption(
        "--mobile",
        action="store_true",
        default=False,
        help="Run tests in mobile emulation mode"
    )
    parser.addoption(
        "--device",
        action="store",
        default=None,
        help=f"Mobile device to emulate. Available devices: {list(MOBILE_DEVICES.keys())}"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


@pytest.fixture
def driver(request) -> Generator[WebDriver, None, None]:
    """
    Fixture to create and configure WebDriver instance

    Usage:
        pytest --browser=chrome --mobile --device=iPhone_12_Pro
        pytest --browser=chrome --headless
        pytest --browser=chrome --mobile  # Uses default mobile configuration
    """
    browser = request.config.getoption("--browser")
    is_mobile = request.config.getoption("--mobile")
    device_name = request.config.getoption("--device")
    is_headless = request.config.getoption("--headless")

    # Convert device option to actual device name
    if device_name:
        device_name = MOBILE_DEVICES.get(device_name)
        if not device_name:
            raise ValueError(f"Unknown device. Available devices: {list(MOBILE_DEVICES.keys())}")

    # Create driver instance
    driver = DriverFactory.create_driver(
        browser_type=browser,
        is_mobile=is_mobile,
        device_name=device_name,
        is_headless=is_headless
    )

    yield driver

    # Cleanup
    driver.quit()


@pytest.fixture
def mobile_driver(driver) -> WebDriver:
    """
    Fixture that ensures the driver is configured for mobile testing
    """
    if not driver.execute_script("return window.navigator.userAgent").lower().__contains__("mobile"):
        pytest.skip("This test requires mobile emulation mode. Use --mobile flag")
    return driver