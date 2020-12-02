from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('------------------ set up ----------------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/')

    yield
    print('------------ tear down-------------')
    driver.quit()

@pytest.mark.usefixtures('init_driver')
def test_googleTitle():
    assert driver.title == 'Google'

@pytest.mark.usefixtures('init_driver')
def test_googleTUrl():
    assert driver.current_url == 'https://www.google.com/'
