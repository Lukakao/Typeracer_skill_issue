from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import random

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get("https://play.typeracer.com/")
first = False
while not first:
    try:
        b1 = driver.find_element(By.XPATH, '//div[@id="gwt-uid-1"]')
        b2 = b1.find_element(By.TAG_NAME, 'a')
        b2.click()
        first = True
    except:
        time.sleep(0.5)
te = [] 
first = False
time.sleep(3)
while not first:
    count = 0
    textos = driver.find_elements(By.XPATH, '//span[@unselectable="on"]')
    for t in textos:
        s = t.text
        print(s)
        for x in range(0, len(s)):
            te.append(s[x])
            first = True
        count+=1
        if(count==2): te.append(" ")

ready = False

first = False
ganemState = None
while not first:
    try:
        ganemState = driver.find_element(By.XPATH, '//div[@class="gameStatusLabel"]')
        first = True
    except:
        print(gugugugagg)
first = False
textbox = None
while not first:
    try:
        textbox = driver.find_element(By.XPATH, '//input[@type="text"]')
        first = True
    except:
        print(gugugugagg)

print(te)
while not ready:
    if (ganemState.text == 'The race is on! Type the text below:'):
        ready = True
        print(ganemState.text)
        
print("boaa")

for l in te:
    textbox.send_keys(l)
    time.sleep(random.randint(0,100)*0.0001+0.05)


time.sleep(10000)