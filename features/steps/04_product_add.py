from behave import given,when,then
from selenium.webdriver.common.by import By
import requests
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@given(u'Im on the product page again')
def page_product(context):
    browser_title = context.browser.title
    assert "Joga Junto" in browser_title, "title not found"
    time.sleep(2)
        
@when(u'I click on the add product button again')
def create_product_btn(context):
    btn_add = context.browser.find_element(By.CSS_SELECTOR, "[aria-controls='radix-6']")
    btn_add.click()
    time.sleep(2)
    
@when(u'I fill in all the necessary fields again')
def create_product_fill(context):
    name_product = context.browser.find_element(By.NAME, "name")
    name_product.send_keys("Chuteira CR7")
    time.sleep(1)

    ds_product = context.browser.find_element(By.NAME, "description")
    ds_product.send_keys("A Chuteira do Melhor do Mundo!")
    time.sleep(1)

    product_category = context.browser.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[2]")
    product_category.click()
    time.sleep(1)

    product_price = context.browser.find_element(By.NAME, "price")
    product_price.send_keys("1000,00")
    time.sleep(1)

    upload_element = context.browser.find_element(By.NAME, "image")
    upload_element.send_keys(os.getcwd() + "\\assets\\chuteira.jpeg")
    time.sleep(2)

    shipment_price = context.browser.find_element(By.NAME, "shipment")
    shipment_price.send_keys("24,98")
    time.sleep(1)
    
@when(u'I click on the register product button again')
def create_product_complete(context):
    submit_product = context.browser.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/button")
    submit_product.click()
    time.sleep(1)
    context.actions.send_keys(Keys.ESCAPE).perform()
    context.actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(3)

    
@then(u'the new product is registered successfully')
def create_product_sucess(context):
    answer = requests.get("https://projetofinal.jogajuntoinstituto.org/products")
    if answer.status_code == 200 or answer.status_code == 201:
        with open('answer_requests_product.txt', 'w') as file:
            file.write(f"The status of the create request was: {answer.status_code}")