from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "http://127.0.0.1:8000/logandsign"

VALID_USERNAME = "mirandacharles780@gmail.com"
VALID_PASSWORD = "mirandacharles780@gmail.com"

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

testValid_login()
testInvalid_Login()