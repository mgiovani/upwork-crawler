import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

url_login = 'https://www.upwork.com/ab/account-security/login'
username = os.getenv('UPWORK_USERNAME')
password = os.getenv('UPWORK_PASSWORD')
secret_answer = os.getenv('UPWORK_SECRET_ANSWER')

driver = webdriver.Chrome()
driver.get(url_login)
elem = driver.find_element_by_id('login_username')
elem.send_keys(username)
elem.send_keys(Keys.RETURN)
elem.clear()
max_waiting_time = 5  # seconds
wait = WebDriverWait(driver, max_waiting_time)
elem = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'login_password')))
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
driver.close()
