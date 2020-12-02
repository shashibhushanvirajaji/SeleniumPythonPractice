from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('https://www.amazon.in/')
wait = WebDriverWait(driver,10)
#wait.until(ec.presence_of_element_located((By.LINK_TEXT,'Mobiles'))).click()
wait.until(ec.title_contains('Online Shopping'))
print(driver.title)
time.sleep(3)
driver.quit()




