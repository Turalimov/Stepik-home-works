from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("http://suninjuly.github.io/execute_script.html")
num1 = browser.find_element(By.ID, "num1")
number1 = num1.text
num2 = browser.find_element(By.ID, 'num2')
number2 = num2.text
x = int(number1)+int(number2)
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(x))
sbm_btn = browser.find_element(By.XPATH, '/html/body/div/form/button').click()
time.sleep(10)
