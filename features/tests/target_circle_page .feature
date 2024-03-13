

  Feature: Test Scenarios for 5 benefit boxes

  Scenario: User have 5 benefit boxes in Target Circle page
    Given Open the Target Circle page
    Then 5 benefit boxes are shown


  Scenario: User add Target product
    Given Open the Target Circle page
    When Search for M&M
    And Click on M&M product image
    And Confirm add in navigation side
    And Click on view cart check out
    Then Product M&M added should be in the cart