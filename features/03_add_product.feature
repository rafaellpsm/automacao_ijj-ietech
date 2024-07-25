Feature: add a product
    Scenario: product added successfully

    Given Im on the product page
    When I click on the add product button
    And I fill in all the necessary fields
    And I click on the register product button
    Then the product is registered successfully