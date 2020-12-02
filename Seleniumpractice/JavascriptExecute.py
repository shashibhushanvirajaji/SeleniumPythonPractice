from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.amazon.in/')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") #scrolling to botton of the page

ele = driver.find_element(By.XPATH,"//a[text()='Australia']")
driver.execute_script("arguments[0].style.border = '3px solid white';", ele) #highlighting an  element
time.sleep(5)

#driver.execute_script("window.scrollTo(0,document.body.scrollToView)") #scrolling to top of the page
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)") #scrolling to top of the page
time.sleep(3)

element = driver.find_element(By.XPATH,"//span[text()='Best Sellers in Clothing & Accessories']")
driver.execute_script("arguments[0].scrollIntoView(true)",element)

time.sleep(5)
driver.quit()