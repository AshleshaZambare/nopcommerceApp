from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    return driver

def pytest_metadata(metadata):
    metadata["Class"] ="Nop Commerce"
    metadata["URL"] = "https://automation.credence.in"

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Specify the browser name (chrome, firefox, etc.)")



