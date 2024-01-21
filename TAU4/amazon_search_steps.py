from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('I open the Amazon page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.amazon.com")

@when('I search for "{item}"')
def step_impl(context, item):
    search_box = context.driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)

@then('I should see search results for "{item}"')
def step_impl(context, item):
    time.sleep(2)  # Ideally use explicit wait here
    assert item in context.driver.page_source
    context.driver.quit()
