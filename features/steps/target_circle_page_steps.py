from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BENEFIT_BOXES = (By.CSS_SELECTOR, "li[class*=styles__BenefitCard]")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
PRODUCT_IMG = (By.CSS_SELECTOR, "div[class*='ProductCardImage__PicturePrimary']")
ADD_CART_NAV = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor']")
VIEW_CART = (By.CSS_SELECTOR, "a[href='/cart']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "div[data-test='cartItem-title']")


@given('Open the Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle/')


@then('5 benefit boxes are shown')
def benefit_boxes_shown(context):
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == 5, f'Expected 5 benefit_boxes, but got {len(benefit_boxes)}'
    print(len(benefit_boxes))


@when('Click on M&M product image')
def click_on_add_to_cart(context):
    context.driver.find_element(*PRODUCT_IMG).click()
    context.wait.until(EC.presence_of_element_located(PRODUCT_IMG), message='PRODUCT_IMG didnt appear')


@when('Confirm add in navigation side')
def confirm_add(context):
    context.driver.find_element(*ADD_CART_NAV).click()
    context.wait.until(EC.presence_of_element_located(ADD_CART_NAV), message='Side nav did not open')


@when('Click on view cart check out')
def click_on_view_cart(context):
    context.driver.find_element(*VIEW_CART).click()
    sleep(2)


@then('Product {expected_result} added should be in the cart')
def product_added_in_cart(context, expected_result):
    actual_result = context.driver.find_element(*PRODUCT_TITLE).text
    assert expected_result in actual_result, f'Expected {expected_result} but got {actual_result}'
