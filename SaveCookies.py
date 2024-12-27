# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# import pickle
# def save_cookies():
#     driver = webdriver.Chrome()
#     driver.get("https://x.com/login")

# # Perform login manually or via automation
#     time.sleep(50)  # Wait for manual login

# # Save cookies to a file
#     with open("proxy.pkl" , "wb") as file:
#         pickle.dump()
#     with open("cookies.pkl", "wb") as file:
#        pickle.dump(driver.get_cookies(), file)
#     driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle
import random
ip_address_array = [
    "198.23.239.134:6540",
    "207.244.217.165:6712",
    "107.172.163.27:6543",
    "64.137.42.112:5157",
    "173.211.0.148:6641",
    "161.123.152.115:6360"
]

def Random(ip):
    proxy = random.choice(ip)
    return proxy
def save_cookies():
    # Define the proxy URL
    prox_url = Random(ip_address_array)
    proxy_url = f"http://{prox_url}"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={proxy_url}')
    # Setup the WebDriver service
    service = Service(ChromeDriverManager().install())

    # Initialize the driver with the options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the login page
    try:
        driver.get("https://x.com/login")
        print(driver.page_source)
        print("Page loaded successfully.")
        
    except Exception as e:
        print(f"Error loading page: {e}")
        driver.quit()
        return

    # Wait for manual login
    print("Please log in manually")
    print(proxy_url)
    time.sleep(100)
    # Save cookies to a file
    try:
        cookies = driver.get_cookies()
        for cookie in cookies:
           if "domain" in cookie:
               cookie["domain"] = ".x.com"  # Set the domain explicitly

        with open("cookies.pkl", "wb") as file:
            pickle.dump(cookies, file)
        print("Cookies saved successfully.")
    except Exception as e:
        print(f"Error saving cookies: {str(e)}")

    driver.quit()
