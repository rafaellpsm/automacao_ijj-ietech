Feature: creating a new account
    Scenario: Account registered successfully

    Given I must be on the registration page
    When I fill out the account creation form
    And I click on the create account button
    Then the account will be created successfully