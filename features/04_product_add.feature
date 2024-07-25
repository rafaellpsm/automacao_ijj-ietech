Feature: add a new product
    Scenario: new product added successfully

    Given Im on the product page again
    When I click on the add product button again
    And I fill in all the necessary fields again
    And I click on the register product button again
    Then the new product is registered successfully