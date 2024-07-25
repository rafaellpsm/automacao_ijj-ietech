from selenium.webdriver import Firefox
import time
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
import os

fake = Faker('pt_BR')
def generate_fake_email():
    return fake.email()

def generate_fake_password():
    return fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)



def before_all(context):
    context.browser = Firefox()
    context.browser.get("https://projetofinal.jogajuntoinstituto.org")
    context.fake_email = generate_fake_email()
    context.fake_password = generate_fake_password()
    context.actions = ActionChains(context.browser)

def after_all(context):
    time.sleep(5)
    context.browser.quit()