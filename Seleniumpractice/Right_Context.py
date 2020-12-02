from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.implicitly_wait(10)
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()

actionChains = ActionChains(driver)
actionChains.context_click(driver.find_element(By.CSS_SELECTOR,'.context-menu-one.btn')).perform()


time.sleep(5)
driver.quit()