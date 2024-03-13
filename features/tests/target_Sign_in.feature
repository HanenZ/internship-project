# Created by zoghl at 2/6/2024
Feature: Test Scenarios for verify Logged out user can access Sign In


  Scenario: Logged out user can access Sign In
    Given Open Target main page
    Then Click Sign in
    When click Sign In right side navigation menu
    Then Sign In form opened


