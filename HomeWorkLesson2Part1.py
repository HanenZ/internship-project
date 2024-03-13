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

# Practice 1:
# first line is Create locators and second is search strategy  for each element:


# Search Amazon logo
driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")
# $x("//a[@class='a-link-nav-icon']")

# Search Email field
driver.find_element(By.XPATH, "//input[@type='email']")
# $x("//input[@type='email']")

# Search Continue button
driver.find_element(By.XPATH, "//input[@id='continue']")
# $x("//input[@id='continue']")

# Search Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use')]")
# $x("//a[contains(@href,'ap_signin_notification_condition_of_use')]")

# Search Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]")
# $x("//a[contains(@href,'ap_signin_notification_privacy_notice')]")

# Search Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# $x("//span[@class='a-expander-prompt']")

# Search Forgot your password link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
# $x("//a[@id='auth-fpp-link-bottom']")

# Search Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
# $x("//a[@id='ap-other-signin-issues-link']")

# Search Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
# $x("//a[@id='createAccountSubmit']")