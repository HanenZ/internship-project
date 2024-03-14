from time import sleep
from selenium.webdriver.common.by import By

from behave import given, then, when


@given('Open the reelly main page')
def open_reelly_sign_up_page(context):
    context.app.reelly_sign_up_page.sign_up()


@then('Log in to the page')
def reelly_log_in_page(context):
    context.app.reelly_sign_in_page.Log_in()


@then('Click on “off plan” at the left side menu')
def click_on_off_plan_left_side_menu(context):
    context.app.main_menu_page.main_menu()


@then('Verify the right page opens')
def click_on_off_plan_left_side_menu(context):
    expected_result = 'Total projects'
    context.app.main_menu_page.verify_off_plan_page(expected_result)


@when('Filter by sale status of “Newly Launch”')
def filter_menu(context):
    context.app.main_menu_page.filter_menu()
    context.app.filters_page.newly_Launch()


@then('Verify each product contains the Newly Launch tag')
def Verify_each_product_has_newly_Launch_tag(context):
    context.app.filters_page.verif_newly_launch_tag()

