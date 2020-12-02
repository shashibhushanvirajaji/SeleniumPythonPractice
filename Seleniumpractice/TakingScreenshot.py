from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.headless = True    # Option 1 : to execute script in headless
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument('--headless')  # Option 2: to execute script in headless
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#driver.maximize_window()
driver.get('https://www.amazon.in/')
driver.get_screenshot_as_file('amazon.png')

''' taking full screen shot''' # to take the full screen shot, execute in headless mode

# S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
# driver.set_window_size(S('Width'), S('Height'))
# driver.find_element_by_tag_name('body').screenshot('fullscreen.png')

time.sleep(3)
driver.quit()
