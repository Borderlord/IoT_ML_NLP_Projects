from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
 
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('C:/Users/vikas yadav/Downloads/chromedriver.exe')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
# 