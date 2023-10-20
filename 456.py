from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
text1 = browser.find_element(By.NAME, 'firstname').send_keys('1')
text2 = browser.find_element(By.NAME, 'lastname').send_keys('2')
text3 = browser.find_element(By.NAME, 'email').send_keys('3')
element = browser.find_element(By.ID, 'file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '111.txt')
element.send_keys(file_path)
sbm_btn = browser.find_element(By.XPATH, '/html/body/div/form/button').click()
time.sleep(5)


