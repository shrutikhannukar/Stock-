from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import tempfile
import shutil

def main():
    options = Options()
    options.binary_location = "/opt/google/chrome/google-chrome"  # Correct Chrome binary path
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    temp_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={temp_dir}')

    service = Service(executable_path='/usr/bin/chromedriver')  # ChromeDriver path

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://13.201.166.12:8000")
        print("Initial Page Title:", driver.title)

        # Auto-refresh loop: 5 times every 10 seconds
        for i in range(5):
            time.sleep(10)
            driver.refresh()
            print(f"Refreshed {i+1} times - Title: {driver.title}")

    finally:
        driver.quit()
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
