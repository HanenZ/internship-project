Feature: Test Scenarios for filter functionality

    Scenario: User can filter by sale status Newly Launch
    Given Open the reelly main page
    Then Log in to the page
    And Click on “off plan” at the left side menu
    Then Verify the right page opens
    When Filter by sale status of “Newly Launch”
    Then Verify each product contains the Newly Launch tag