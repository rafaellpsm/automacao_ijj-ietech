from behave import given,when,then
from selenium.webdriver.common.by import By
import requests
import time


@given(u'Im on the login page')
def page_login(context):
    browser_title = context.browser.title
    assert "Joga Junto" in browser_title, "title not found"
    time.sleep(2)
    
@when(u'I fill in the fields with the correct credentials')
def fill_login_form(context):
    time.sleep(1)
    context.browser.find_element(By.NAME, "email").send_keys(context.fake_email)
    time.sleep(1)
    context.browser.find_element(By.NAME, "password").send_keys(context.fake_password)
    time.sleep(2)

@when(u'I click on the sign in button')
def submit_login(context):
    btn_login = context.browser.find_element(By.XPATH, "/html/body/div/main/form/button")
    btn_login.submit()
    time.sleep(2)

@then(u'I successfully logged into the account')
def login_sucess(context):
    answer = requests.get("https://projetofinal.jogajuntoinstituto.org/")
    if answer.status_code == 200 or answer.status_code == 201:
        with open('answer_requests.txt', 'w') as file:
            file.write(f"The status of the login request was: {answer.status_code}")   