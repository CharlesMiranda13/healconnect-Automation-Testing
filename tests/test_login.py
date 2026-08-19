import os
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/logandsign")
VALID_USERNAME = os.getenv("TEST_USER_EMAIL", "testuser@healconnect.local")
VALID_PASSWORD = os.getenv("TEST_USER_PASSWORD", "TestPassword123!")
INVALID_USERNAME = "invalid_user@example.com"

def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.url_contains("/patient/home")
    )

    assert "/patient/home" in driver.current_url.lower()


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login("invalid@example.com", "invalidpassword")

    assert "/logandsign" in driver.current_url.lower()


def test_no_input_login(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.submit_login()

    assert "/logandsign" in driver.current_url.lower()


def test_forgot_password(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.request_password_reset(VALID_USERNAME)

    assert "/logandsign" in driver.current_url.lower()


def test_forgot_password_invalid_email(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.request_password_reset(INVALID_USERNAME)

    assert "/logandsign" in driver.current_url.lower()
