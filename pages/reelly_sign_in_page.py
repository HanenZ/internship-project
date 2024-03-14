from selenium.webdriver import Keys
from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By


class ReellyLogIn(Page):
    EMAIL = (By.CSS_SELECTOR, "[name='email-2']")
    PASSWORD = (By.CSS_SELECTOR, "[name='Password']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[class*='login-button']")

    def Log_in(self):
        # self.driver.find_element(*self.EMAIL).send_keys('zoghlami_hanen@yahoo.fr')
        self.input_text('zoghlami_hanen@yahoo.fr', *self.EMAIL)
        self.driver.find_element(*self.PASSWORD).send_keys('Mayaadam2018.')
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
