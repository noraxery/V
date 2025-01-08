from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {"profile.default_content_settings": {"images": 2}}
    chrome_options.add_experimental_option("prefs", chrome_prefs)
    return chrome_options


if __name__ == "__main__":
    try:
        # Initialize the Chrome driver with the specified options
        driver = webdriver.Chrome(options=set_chrome_options())
        
        # Navigate to the Mega.nz login page
        driver.get("https://mega.nz/login")
        
        # Wait for the page to load
        time.sleep(5)
        
        # Find the email input field and enter the email
        email_input = driver.find_element(By.ID, "login-name2")
        email_input.send_keys("typperxevery@gmail.com")
        
        # Find the password input field and enter the password
        password_input = driver.find_element(By.ID, "login-password2")
        password_input.send_keys("Nibtun2004@")
        
        # Find the login button and click it
        login_button = driver.find_element(By.CSS_SELECTOR, ".login-button > span")
        login_button.click()
        
        # Wait for the login process to complete
        time.sleep(5)
        
        # Print the URL of the new page after login
        print("URL after login: " + driver.current_url)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the browser is closed
        driver.quit()