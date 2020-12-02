from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.amazon.in/')

time.sleep(2)
driver.find_element(By.LINK_TEXT,'Mobiles').click()
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()