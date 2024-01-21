Feature: Trojmiasto.pl Search
  As a user, I want to search for information on trojmiasto.pl so that I can find relevant cultural events.

  Scenario: Search for cultural events on trojmiasto.pl
    Given I am on the trojmiasto.pl homepage
    When I search for "kultura"
    Then the search results should be displayed
