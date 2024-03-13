Feature: Test Scenarios for Search functionality

  Scenario: User can search for a python
    Given Open Google page
    When Input python into search field
    And Click on search icon
    Then Product results for python are shown

  Scenario Outline: User can search for a product
    Given Open Google page
    When Input <search_word> into search field
    And Click on search icon
    Then Product results for <product_result> are shown
    Examples:
    |search_product    |product_result
    |python            |python
    |cucumber          |cucumber
    |selenium          |selenium
