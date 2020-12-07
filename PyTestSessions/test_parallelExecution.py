import  pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_amazon_title():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.amazon.in/')
    assert driver.title == 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'
    driver.quit()

def test_google_title():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.google.com/')
    assert driver.title == 'Google'
    driver.quit()

def test_facebook_title():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.facebook.com/')
    driver.get_screenshot_as_file()
    assert driver.title == 'Facebook – log in or sign up'
    driver.quit()

def test_whatsapp_title():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.whatsapp.com/')
    assert driver.title == 'WhatsApp'
    driver.quit()
