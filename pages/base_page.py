from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger



class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)


    def open(self, url):
        # logger.info(f'Opening url {url}...')
        self.driver.get(url)

    def find_element(self, *locator):
        # logger.info(f'Searching for element {locator}...')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        # logger.info(f'Clicking on for element {locator}...')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles  # [window1, window2]
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)

    def wait_for_element(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))
