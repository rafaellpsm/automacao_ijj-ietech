from behave import given,when,then
from selenium.webdriver.common.by import By
import requests
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@given(u'Im on the product page down')
def page_product(context):
    browser_title = context.browser.title
    assert "Joga Junto" in browser_title, "title not found"
    time.sleep(2)
    
@when(u'I fill in the field with the product name')
def search_product_fill(context):
    name_product_search = context.browser.find_element(By.CLASS_NAME, "search")
    name_product_search.send_keys("Camiseta do Chico")
    time.sleep(3)
    
@then(u'The product is shown')
def search_product_sucess(context):
    answer = requests.get("https://projetofinal.jogajuntoinstituto.org/products")
    if answer.status_code == 200 or answer.status_code == 201:
        with open('answer_requests_product.txt', 'w') as file:
            file.write(f"The status of the search request was: {answer.status_code}")