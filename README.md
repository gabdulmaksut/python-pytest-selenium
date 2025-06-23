# Twitch UI Test Automation Project

This project demonstrates automated UI testing for Twitch.tv using Selenium WebDriver, Pytest, and Allure reporting.

## Setup

1. Clone the repository:
```
bash git clone [https://github.com/gabdulmaksut/python-pytest-selenium](https://github.com/gabdulmaksut/python-pytest-selenium) cd python-pytest-selenium
``` 

2. Create and activate a virtual environment:
```
python3 -m venv venv 
source venv/bin/activate
``` 

3. Install dependencies:
```
pip install -r requirements.txt
```

## Running Tests
1. Run all tests:
``` 
pytest
```
1. Run with Allure reporting:
``` 
pytest --alluredir=reports/allure-results
```
1. Generate and view Allure report:
``` 
allure serve ./reports/allure-results
```

## Test Recording Example
Below is a demonstration of a test execution:
![test_record.gif](assets/test_record.gif)