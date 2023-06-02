import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

serv = Service("C:\webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
time.sleep(2)

nom = driver.find_element(By.XPATH, value="//*[@id='userName']")
nom.send_keys("felipe")
time.sleep(5)

driver.quit()

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver2 = webdriver.Firefox(executable_path='C:\webdriver\geckodriver.exe')
driver2.maximize_window()
driver2.get("https://demoqa.com/text-box")

nom2 = driver2.find_element(By.XPATH, value="//*[@id='userName']")
nom2.send_keys("Juan Felipe")
time.sleep(5)

driver2.quit()
