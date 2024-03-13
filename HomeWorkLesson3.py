from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 1. Find the most optimal locators

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
# Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# Your name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
# Email
driver.find_element(By.CSS_SELECTOR, '#ap_email')
# Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')
# Passwords must be at least 6 characters.
driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be at least 6 characters.')]")
# Re-enter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Continue
driver.find_element(By.CSS_SELECTOR, '#continue')
# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")
# Privacy Notice.
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")
# Sign in
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')


