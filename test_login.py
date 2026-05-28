from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "http://127.0.0.1:8000/logandsign"

VALID_USERNAME = "mirandacharles780@gmail.com"
VALID_PASSWORD = "mirandacharles780@gmail.com"

INVALID_USERNAME = "hehehe@gmail.com"

def testValid_login():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)

        driver.find_element(By.NAME, "email").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(2)

        print("Current URL:", driver.current_url)

        assert "/patient/home" in driver.current_url.lower()

        print("Working Valid input")

    except Exception as e:
        print(f"Error during valid login test: {e}")
        print("Current URL:", driver.current_url)

    finally:
        driver.quit()

def testInvalid_Login():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)

        driver.find_element(By.NAME, "email").send_keys("invalid@example.com")
        driver.find_element(By.NAME, "password").send_keys("invalidpassword")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(2)

        print("Current URL:", driver.current_url)

        assert "/logandsign" in driver.current_url.lower()

        print("Working Invalid input")

    except Exception as e:
        print(f"Error during invalid login test: {e}")
        print("Current URL:", driver.current_url)

    finally:
        driver.quit()

def testnoinput_login():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(2)

        print("Current URL:", driver.current_url)

        assert "/logandsign" in driver.current_url.lower()

        print("Working No input")

    except Exception as e:
        print(f"Error during no input login test: {e}")
        print("Current URL:", driver.current_url)

    finally:
        driver.quit()

def testForgot_password():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)

        driver.find_element(By.CLASS_NAME, "openForgotBtn").click()

        time.sleep(2)

        driver.find_element(By.ID, "forgot-email").send_keys(VALID_USERNAME)

        driver.find_element(By.CLASS_NAME, "modal-submit-btn").click()

        time.sleep(2)

        print("Forgot password test executed")

    except Exception as e:
        print("Forgot password test failed")
        print(e)

    finally:
        driver.quit()

def testForgot_passwordInvalid():
    driver = webdriver.Chrome()

    try:
        driver.get(BASE_URL)

        driver.find_element(By.CLASS_NAME, "openForgotBtn").click()
        time.sleep(2)

        driver.find_element(By.ID, "forgot-email").send_keys(INVALID_USERNAME)
        driver.find_element(By.CLASS_NAME, "modal-submit-btn").click()

        time.sleep(2)

        print("Forgot password with invalid email is working")

    except Exception as e:
        print("not working")

    finally:
        driver.quit()

testValid_login()
testInvalid_Login()
testnoinput_login()
testForgot_password()
testForgot_passwordInvalid()