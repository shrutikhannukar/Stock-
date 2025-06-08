from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  # Useful if running in Linux containers or Jenkins
    options.add_argument('--disable-dev-shm-usage')  # Prevent some Chrome crashes

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://13.201.166.12:8000")
        time.sleep(2)  # Wait for page to load fully
        print("Page Title is:", driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

