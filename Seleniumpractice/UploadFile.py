from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element(By.NAME,'upfile').send_keys('')

