# Practice 2:

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

# Open Target website
driver.get('https://www.target.com/')

#  Click SignIn button
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

#  Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span").click()
sleep(5)

# Verify SignIn page opened

actual_text = driver.find_element(By.XPATH, "//h1[contains(@class,'styles__AuthHeading')]").text
assert 'Sign into your Target account' in actual_text

print(actual_text)

driver.find_element(By.XPATH, "//button[@type='submit']")

print('test case passed!')