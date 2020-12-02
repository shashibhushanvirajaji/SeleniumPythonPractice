from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time
browser = 'chrome'

if browser=='chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser=='firefox':
    driver = webdriver.Chrome(executable_path=GeckoDriverManager().install())
else:
    print('please give proper browser')

driver.get('http://demowebshop.tricentis.com/')
print(driver.title)
time.sleep(5)
driver.quit()
