import selenium
import time
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

nba_woj = "https://twitter.com/wojespn"
nba_shams = "https://twitter.com/ShamsCharania"
nfl_schefter = "https://twitter.com/AdamSchefter"
nfl_rappaport = "https://twitter.com/RapSheet"


driver = webdriver.Chrome(PATH)

driver.get(nba_woj)
time.sleep(1)
driver.execute_script("window.open(' ');")

driver.get(nba_shams)
time.sleep(1)
driver.execute_script("window.open(' ');")

driver.get(nfl_schefter)
time.sleep(1)
driver.execute_script("window.open(' ');")

driver.get(nfl_rappaport)



