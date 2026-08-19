from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    FORGOT_PASSWORD_BUTTON = (By.CLASS_NAME, "openForgotBtn")
    FORGOT_EMAIL_INPUT = (By.ID, "forgot-email")
    FORGOT_SUBMIT_BUTTON = (By.CLASS_NAME, "modal-submit-btn")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.submit_login()

    def submit_login(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def request_password_reset(self, email):
        self.wait.until(EC.element_to_be_clickable(self.FORGOT_PASSWORD_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.FORGOT_EMAIL_INPUT)).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.FORGOT_SUBMIT_BUTTON)).click()
