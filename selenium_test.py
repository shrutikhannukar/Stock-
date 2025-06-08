from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import time

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Create a temporary directory for user data to avoid conflicts
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={user_data_dir}')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://13.201.166.12:8000")
        time.sleep(2)
        print("Page Title is:", driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
