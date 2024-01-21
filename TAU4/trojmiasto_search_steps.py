from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the trojmiasto.pl homepage')
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.get("https://www.trojmiasto.pl")

@when('I search for "{query}"')
def step_impl(context, query):
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.NAME, "string"))
    )
    search_box.clear()
    search_box.send_keys(query)
    search_button = context.driver.find_element(By.CLASS_NAME, "button--secondary")
    search_button.click()

@then('the search results should be displayed')
def step_impl(context):
    # This can be enhanced with a more specific check for search results.
    assert "kultura" in context.driver.page_source
    context.driver.quit()
