Feature: Amazon Product Search
  As a user, I want to search for products on Amazon so that I can find items I'm interested in.

  Scenario: Search for a product on Amazon
    Given I open the Amazon page
    When I search for "Echo Dot"
    Then I should see search results for "Echo Dot"
