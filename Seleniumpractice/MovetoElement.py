from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.implicitly_wait(10)
driver.get('https://www.spicejet.com/default.aspx')
driver.maximize_window()

actionChains = ActionChains(driver)
actionChains.move_to_element(driver.find_element(By.ID,'ctl00_HyperLinkLogin')).perform()
actionChains.move_to_element(driver.find_element(By.LINK_TEXT,'SpiceClub Members')).perform()
driver.find_element(By.LINK_TEXT,'Member Login').click()
time.sleep(15)
driver.find_element(By.ID,'ControlGroupLoginView_MemberLoginView2LoginView_TextBoxUserID').send_keys('4324234324')
#actionChains.send_keys_to_element(driver.find_element(By.ID,'ControlGroupLoginView_MemberLoginView2LoginView_TextBoxUserID'),'9845336821').perform()

time.sleep(10)
driver.quit()



