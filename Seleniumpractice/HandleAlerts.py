from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME,'proceed').click()

allert = driver.switch_to.alert
if allert.text != '':
    print(allert.text)

allert.accept()

time.sleep(3)
driver.quit()