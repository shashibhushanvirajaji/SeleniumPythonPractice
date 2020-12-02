from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
driver.maximize_window()
#
# def selectValuesFromDropdown(element, value):
#     select = Select(element)
#     select.select_by_visible_text(value)
#
# employee = driver.find_element(By.NAME, 'NoOfEmployees')
# industry =  driver.find_element(By.CSS_SELECTOR,'#Form_submitForm_Industry')
# selectValuesFromDropdown(employee,'2,501 - 3,000')
# selectValuesFromDropdown(industry,'Computer / Technology - Reseller (inc VAR)')

# with out select method

countryoptions = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')
print(len(countryoptions))
for country in countryoptions:
    if country.text == 'India':
        country.click()
        break

time.sleep(10)
driver.quit()
