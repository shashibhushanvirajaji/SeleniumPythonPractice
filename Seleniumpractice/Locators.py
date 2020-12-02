from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://portal.medibuddy.in/Home.aspx')
driver.maximize_window()

tags = driver.find_elements(By.TAG_NAME,'a')
print(len(tags))
for tagname in tags:
    print(tagname.text + '  ' + tagname.get_attribute('href'))

# driver.find_element_by_name('USERID').send_keys('shashyu')
# driver.find_element(By.NAME,'PASSWORD').send_keys('adsfewrew')
# print(driver.title)
# print(driver.current_url)

time.sleep(3)
driver.quit()



