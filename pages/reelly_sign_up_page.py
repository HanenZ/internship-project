from selenium.webdriver import Keys
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By


class ReellySignUp(Page):
    SIGN_IN = (By.CSS_SELECTOR, "[class='sing-in-text']")

    def sign_up(self):
        self.open('https://soft.reelly.io/sign-up')
        self.click(*self.SIGN_IN)
