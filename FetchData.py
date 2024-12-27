import pickle
import uuid
from selenium import webdriver
from config import collection
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
from datetime import datetime
import time

ip_address_array = [
    "198.23.239.134:6540",
    "207.244.217.165:6712",
    "107.172.163.27:6543",
    "64.137.42.112:5157",
    "173.211.0.148:6641",
    "161.123.152.115:6360"
]

def fetch_trending_and_save_to_db():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    # Initialize the driver with the options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the home page (ensure this matches the domain of your cookies)
    driver.get("https://x.com/home")
    print(driver.current_url)

    # Step 2: Load cookies
    try:
        with open("cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            # Clean up cookie if required
            cookie.pop("expiry", None)  # Remove expiry if not valid
            if "domain" in cookie:
                cookie["domain"] = ".x.com"
            driver.add_cookie(cookie)
        print("Cookies loaded successfully.")
    except FileNotFoundError:
        print("Cookie file not found. Please log in manually and save cookies first.")
        driver.quit()
        return
    except Exception as e:
        print(f"Error while loading cookies: {str(e)}")
        driver.quit()
        return

    # Refresh the page to apply cookies
    driver.refresh()
    result = []
    # Step 3: Wait for trending topics to load
    try:
        # Wait for the trending section to be visible after refresh
        WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@aria-label, 'Timeline: Trending')]//span"))
        )

        # Fetch trending topics again after refresh
        elements = driver.find_elements(By.XPATH, "//div[contains(@aria-label, 'Timeline: Trending')]//span")
        driver.save_screenshot("debug_page.png")
        with open("debug_page.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

        document = []
        i = 0
        for element in elements:
            if "What’s happening" not in element.text and "Trending" not in element.text and "posts" not in element.text and "Show more" not in element.text:
                IpAddress = random.choice(ip_address_array)
                document.append({
                    "Trending": element.text,
                    "CreatedAt": datetime.now().time().strftime("%H:%M:%S"),
                    "IpAddress": IpAddress.split(":")[0]  # Use random.choice here
                })
                i += 1

        SEEn = set()
      
        for a in document:
            trend = a.get("Trending")
            if trend not in SEEn:
                result.append(a)
                SEEn.add(trend)

        for a in result:
            print(a)
        print(f"{len(result)} records to insert.")
        result_saved = collection.insert_many(result)
        print(f"{len(result_saved.inserted_ids)} records inserted successfully.")
    except Exception as e:
        print("Error while fetching trending topics:", str(e))

    # Step 4: Check if login was successful
    if "Log in" in driver.page_source:
        print("Login failed. Try saving cookies again.")
    else:
        print("Login successful.")
    
    # Close the browser
    driver.quit()
    return result
