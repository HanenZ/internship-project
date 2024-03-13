from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.implicitly_wait(4)  # 0.1 / sec

# Explicit wait:
driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

# accept the cookies
driver.find_element(By.CSS_SELECTOR, '[class="QS5gu sy4vM"]').click()

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('python')

# click search button

# driver.find_element(By.NAME, 'btnK').click()
search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search btn not clickable').click()

# verify search results
assert 'python' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
