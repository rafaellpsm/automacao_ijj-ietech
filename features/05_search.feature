Feature: search for the added product
    Scenario: product found

    Given Im on the product page down
    When I fill in the field with the product name
    Then The product is shown