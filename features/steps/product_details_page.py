from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
COLOR_OPTIONS_PRODUCT = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR_PRODUCT = (By.CSS_SELECTOR, "div[class*='styles__CellVariationHeaderWrapper']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    #context.wait.until(EC.url_contains('{product_id}'))


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Cream']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors[:3]:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        selected_color = selected_color.split('\n')[1]  # Black
        actual_colors.append(selected_color)
        # print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click through colors of the product')
def click_and_verify_colors_product(context):
    expected_colors_product = ['Black', 'Deep Olive', 'White']
    actual_colors_product = []

    colors = context.driver.find_elements(*COLOR_OPTIONS_PRODUCT)  # [webelement1, webelement2, webelement3]
    for color in colors[:3]:
        color.click()

        selected_color_product = context.driver.find_element(*SELECTED_COLOR_PRODUCT).text.split('\n')[1]
        actual_colors_product.append(selected_color_product)
        print(actual_colors_product)

    assert expected_colors_product == actual_colors_product, f'Expected {expected_colors_product} did not match actual {actual_colors_product}'