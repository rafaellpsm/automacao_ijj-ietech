Feature: login
    Scenario: login successfully

    Given Im on the login page
    When I fill in the fields with the correct credentials
    And I click on the sign in button 
    Then I successfully logged into the account