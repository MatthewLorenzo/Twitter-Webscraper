import selenium
import time
from selenium import webdriver



PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = "https://twitter.com/mattlorenzo_"
driver = webdriver.Chrome(PATH)
driver.get(URL)


# nba_woj = "https://twitter.com/wojespn"
# nba_shams = "https://twitter.com/ShamsCharania"
# nfl_schefter = "https://twitter.com/AdamSchefter"
# nfl_rappaport = "https://twitter.com/RapSheet"
