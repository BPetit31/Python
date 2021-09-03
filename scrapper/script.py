# Regroupe les fonctions et variables utilisées pour scrapper bing
# Microsoft Rewards via Selenium
from login import *
import json, random, time, os, sys
import requests
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys

# Ouvrir le fichier local words.txt et créer une liste des 85 mots
with open(os.path.join(sys.path[0], 'words.txt'), 'r+') as f:
    words = f.read()
    w = words.split()

def wait_for(sec = 3):
    time.sleep(sec)

driver = webdriver.Edge(executable_path="C:\\Users\\bpeti\\Desktop\\Toulouse Dev-IA\\C#\\Python\\scrapper\\edgedriver_win64\\msedgedriver.exe")
url_base = 'https://www.bing.com/?scope=web&mkt=fr-FR'
driver.get(url_base)
wait_for(6)

# login_live(driver, "", "")
# wait_for()

for num, word in enumerate(w):
    if num <= 31:
        research_conf = driver.find_element_by_id('sb_form_q')
        research_conf.clear()
        research_conf.send_keys(word)
        research_conf.send_keys(Keys.RETURN)
        print('{0}. URL : {1}'.format(str(num + 1), url_base + word))
        wait_for(1)
driver.close()