from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\svirajaj\OneDrive - Capgemini\\Documents\\drivers\\chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
#listofLinks =  driver.find_elements_by_tag_name('a')
#listofLinks =  driver.find_elements(By.TAG_NAME,'a')
#print(len(listofLinks))
#for link in listofLinks:
#    print(link.text)
print("title of the page ->"+driver.title)
assert 'Demo Web Shop',driver.title

driver.quit()