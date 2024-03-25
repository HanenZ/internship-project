import time

from selenium.webdriver import Keys
from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By


class Filters(Page):
    NEWLY_LAUNCHED = (By.CSS_SELECTOR, "div[wized='priorityStatusNewlyLaunched']")
    NEWLY_LAUNCHED_TAG = (By.CSS_SELECTOR, "[class*='commision_box']")
    LISTINGS = (By.CSS_SELECTOR, "[class='project-image']")

    def newly_Launch(self):
        self.wait_for_element(*self.NEWLY_LAUNCHED)
        self.click(*self.NEWLY_LAUNCHED)

    def verif_newly_launch_tag(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        actual_text = self.find_element(*self.NEWLY_LAUNCHED_TAG).text
        all_products = self.find_elements(*self.LISTINGS)

        for product in all_products:
            actual_tag = product.find_element(*self.NEWLY_LAUNCHED_TAG).text
            expected_tag = "Newly Launched"
            # print(actual_tag)
            # print(expected_tag)
            print(f"Actual tag: {actual_tag}")
            print(f"Expected tag: {expected_tag}")

            assert expected_tag in actual_tag, f'Expected word {expected_tag} not in {actual_tag}'
