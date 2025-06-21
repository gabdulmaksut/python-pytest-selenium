# Twitch UI Test Automation Project

This project demonstrates automated UI testing for Twitch.tv using Selenium WebDriver, Pytest, and Allure reporting.

## Project Structure
```
python-pytest-selenium/ 
├── tests/ 
│ └── ui/ 
│ └── test_twitch_search.py 
├── pages/ 
│ └── twitch_home_page.py 
│ └── twitch_search_results_page.py 
├── utils/ 
│ └── driver_factory.py 
│ └── common_actions.py 
├── config/ 
│ └── settings.py 
├── conftest.py ├
── requirements.txt 
└── README.md
``` 

## Setup

1. Clone the repository:
```
bash git clone <repository-url> cd python-pytest-selenium
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

4. Install Allure (optional, for reporting):
- On macOS: `brew install allure`
- On Linux: Follow [Allure installation guide](https://docs.qameta.io/allure/#_installing_a_commandline)

## Running Tests

1. Run all tests:
```
bash pytest
``` 

2. Run with Allure reporting:
```
bash pytest --alluredir=allure-results
``` 

3. Generate and view Allure report:
```
bash allure generate allure-results --clean allure open allure-report
``` 

## Features

- Page Object Model (POM) design pattern
- Mobile device emulation
- Explicit waits for better stability
- Screenshot capture on test failure
- Allure reporting integration
- Common utilities for modal handling and scrolling

## Best Practices

- Uses explicit waits instead of implicit waits where possible
- Implements proper page object pattern
- Handles common UI interactions in utility classes
- Includes proper error handling and reporting
- Follows Python coding standards

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
```