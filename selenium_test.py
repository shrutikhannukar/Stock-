from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import tempfile

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # ✅ Use a unique temporary user-data-dir to avoid profile conflicts
    temp_profile_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={temp_profile_dir}')

    # ✅ Use WebDriverManager for ChromeDriver compatibility
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("http://13.201.166.12:8000")
        time.sleep(2)
        print("Page Title is:", driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
