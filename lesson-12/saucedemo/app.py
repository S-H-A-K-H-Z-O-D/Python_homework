from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

url = 'https://www.saucedemo.com/'
login = 'standard_user'
password = 'secret_sauce'

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run browser in headless mode
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--window-position=-1700,-200")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

login_field = driver.find_element(By.ID, 'user-name')
login_field.send_keys(login)

password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)

submit_field = driver.find_element(By.ID, 'login-button')
submit_field.click()


