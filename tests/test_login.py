from pages.login_page import LoginPage


BASE_URL = "http://127.0.0.1:8000/logandsign"

VALID_USERNAME = "mirandacharles780@gmail.com"
VALID_PASSWORD = "mirandacharles780@gmail.com"
INVALID_USERNAME = "hehehe@gmail.com"


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

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
