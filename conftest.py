import pytest
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()
