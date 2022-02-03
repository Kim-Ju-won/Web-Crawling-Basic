import time

print(time.time())
print(time.localtime())

for i in range(10):
    print(i)
    time.sleep(1)

import requests
from bs4 import BeautifulSoup
from selenium import webdriver