import time

from selenium.webdriver import Keys
from time import sleep
from pages.base_page import Page
from selenium.webdriver.common.by import By



class MainMenu(Page):
 OFF_PLAN = (By.CSS_SELECTOR, "[class*='_1-link-menu w-inline-block']")
 TOTAL_PROJECTS = (By.CSS_SELECTOR, "[class='page-title off_plan']")
 FILTERS = (By.CSS_SELECTOR, "div[class*='filter-text']")
 def main_menu(self):
     self.wait_for_element(*self.OFF_PLAN)
     self.click(*self.OFF_PLAN)

 def verify_off_plan_page(self, expected_result):
     actual_text = self.find_element(*self.TOTAL_PROJECTS).text
     assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'

 def filter_menu(self):
     self.click(*self.FILTERS)



