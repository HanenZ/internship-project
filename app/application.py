from pages.reelly_sign_up_page import ReellySignUp
from pages.reelly_sign_in_page import ReellyLogIn
from pages.main_menu_page import MainMenu
from pages.filters_page import Filters


class Application:

    def __init__(self, driver):
        self.reelly_sign_up_page = ReellySignUp(driver)
        self.reelly_sign_in_page = ReellyLogIn(driver)
        self.main_menu_page = MainMenu(driver)
        self.filters_page = Filters(driver)
