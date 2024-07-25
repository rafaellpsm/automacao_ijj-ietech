from selenium.webdriver import Firefox
from behave import given,when,then
from selenium.webdriver.common.by import By
import requests
import time

@given(u'I must be on the registration page')
def click_new_register(context):
    browser_title = context.browser.title
    assert "Joga Junto" in browser_title, "titulo nao encontrado"
    time.sleep(2)
    btn_register = context.browser.find_element(By.XPATH,"/html/body/div/main/form/div[6]/span[2]/a")
    btn_register.click()
    time.sleep(2)

@when(u'I fill out the account creation form')
def fill_new_register(context):
    context.browser.find_element(By.NAME, "email").send_keys(context.fake_email)
    time.sleep(1)
    context.browser.find_element(By.NAME, "password").send_keys(context.fake_password)
    time.sleep(1)
    context.browser.find_element(By.NAME, "confirmPassword").send_keys(context.fake_password)
    time.sleep(2)

@when(u'I click on the create account button')
def submit_new_register(context):
    btn_create = context.browser.find_element(By.XPATH," /html/body/div/div/form/button")
    btn_create.submit()
   
@then(u'the account will be created successfully')
def new_register_sucess(context):
    answer = requests.get("https://projetofinal.jogajuntoinstituto.org/register")
    if answer.status_code == 200 or answer.status_code == 201:
        time.sleep(3)
        btn_enter = context.browser.find_element(By.XPATH, "/html/body/div/div/form/span/a")
        btn_enter.click()
    time.sleep(3)