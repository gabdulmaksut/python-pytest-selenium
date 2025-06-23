# UI Test Automation Framework with Pytest & Selenium 

This project demonstrates automated UI testing for Twitch.tv using Selenium WebDriver, Pytest, and Allure reporting.

---

## 🚀 Getting Started

Follow these steps to set up and run the UI test framework on your local machine.

### 1. Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+** (Highly recommended for compatibility)
* **`pip`** (Python package installer, usually comes with Python)
* **Web Browser:**
    * [Google Chrome](https://www.google.com/chrome/) (for Chrome tests)
* **WebDriver Executables:**
    * **ChromeDriver:** Automatically managed by `webdriver_manager`. You don't need to download it manually!

## 2. Clone the Repository

First, clone this repository to your local machine:

```
bash git clone https://github.com/gabdulmaksut/python-pytest-selenium
cd python-pytest-selenium
``` 
## 3. Create and Configure the .env File
For security and flexibility, sensitive data and environment-specific configurations are stored in a .env file. This file will not be committed to version control.

Create a new file named .env in the root directory of your project (where README.md is located).

Add your base URL and any other environment-specific variables needed for your tests. For example:

```
BASE_URL="https://www.twitch.tv/"
```

## 4. Create a Virtual Environment and Install Dependencies
It's highly recommended to use a Python virtual environment to manage project dependencies.
Create a virtual environment 
```
python -m venv venv
```

### Activate the virtual environment
On Windows (CMD):

```
.\venv\Scripts\activate
```

On macOS / Linux (Bash/Zsh):
``` 
source venv/bin/activate
```
### Install required Python packages
```
pip install -r requirements.txt

```

## 5. Run the Tests 🚀
Make sure your virtual environment is activated before running any tests.
Run all tests:
``` 
pytest tests/
```
Run with Allure reporting:
``` 
pytest --alluredir=reports/allure-results
```
Generate and view Allure report:
``` 
allure serve ./reports/allure-results
```

## Test Recording Example
Below is a demonstration of a test execution:
![test_record.gif](assets/test_record.gif)
