'''USERNAME = "bsuser_ut2xjm"
ACCESS_KEY = "MV8BaUyEnCpxqfcGsCAc"'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
import time

USERNAME = "bsuser_ut2xjm"
ACCESS_KEY = "MV8BaUyEnCpxqfcGsCAc"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub"

def run_test(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.set_capability("browserName", "Chrome")
        options.set_capability("browserVersion", "latest")

    elif browser_name == "safari":
        options = SafariOptions()
        options.set_capability("browserName", "Safari")
        options.set_capability("browserVersion", "latest")

    options.set_capability("bstack:options", {
        "os": "OS X",
        "osVersion": "Ventura",
        "projectName": "SQAT Assignment 6",
        "buildName": "Cross Browser Test",
        "sessionName": f"Login Test on {browser_name}",
        "seleniumVersion": "4.21.0"
    })

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(2)

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(3)

        assert "Secure Area" in driver.page_source
        print(f"✅ Test passed on {browser_name}")

    except Exception as e:
        print(f"❌ Test failed on {browser_name}: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_test("chrome")
    run_test("safari")
