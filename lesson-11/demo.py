from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run browser in headless mode
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--window-position=-1700,-200")

# Browser will remain open after the script ends
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.youtube.com/")

time.sleep(3)
search_input = driver.find_element(by=By.NAME, value='search_query')
search_input.send_keys('Python')
time.sleep(5)

btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Search"]')
btn.click()
