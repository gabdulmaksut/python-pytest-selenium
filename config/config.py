from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class Config:
    # Twitch credentials
    TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
    TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')

    # Test user credentials
    TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL')
    TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD')

    # Browser configuration
    BROWSER_TYPE = os.getenv('BROWSER_TYPE', 'chrome')
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    VIEWPORT_WIDTH = int(os.getenv('VIEWPORT_WIDTH', 375))
    VIEWPORT_HEIGHT = int(os.getenv('VIEWPORT_HEIGHT', 812))

    # Timeouts
    DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', 10))
    IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 5))

    # URLs
    BASE_URL = os.getenv('BASE_URL', 'https://www.twitch.tv')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.twitch.tv/helix')

    # Test environment
    ENV = os.getenv('ENV', 'development')
    SCREENSHOT_DIR = os.getenv('SCREENSHOT_DIR', './screenshots')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')