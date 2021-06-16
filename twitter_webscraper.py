import selenium
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

twitter_link = "https://twitter.com/"

twitter_handle = input("Whose Twitter do you want to see?")

twitter_url = twitter_link + twitter_handle

driver = webdriver.Chrome(PATH)
driver.get(twitter_url)



