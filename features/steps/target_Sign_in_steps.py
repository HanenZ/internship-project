from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@then('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(6)


@when('click Sign In right side navigation menu')
def sign_in_right_side_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span").click()
    sleep(5)


@then('Sign In form opened')
def sign_in_form_opened(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class,'styles__AuthHeading')]/span").text
    assert 'Sign into your Target account' == actual_text, f"Expected 'Sign into your Target account' but got {actual_text}"

    print(actual_text)

    print('test case passed!')