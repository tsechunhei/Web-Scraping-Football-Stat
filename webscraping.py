import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

option = ChromeOptions()
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"  # not waiting for the complete loading of the website
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=option, desired_capabilities=capa)
# driver.get('https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop')
# boll_id = []
# for i in range(20):
#     js = 'let xx=[];for(let i of document.querySelectorAll(".spielprofil_tooltip")){xx.push({id:i.id})} return xx'
#     boll = driver.execute_script(js)
#     boll_id += boll[:-5]
#     try:
#         driver.execute_script('document.querySelector("#yw2 > li.naechste-seite > a").click()')
#         time.sleep(3)
#     except:
#         break

boll_id = [
   

    {'id': '49499'},
    {'id': '44352'},

     {'id': '187587'}, {'id': '181136'},
    {'id': '146854'}, {'id': '141660'},
	 {'id': '346483'}, {'id': '341647'}, {'id': '340950'}, 

     ]

from selenium.webdriver.support import expected_conditions as EC

y = 1
for i in boll_id:
    y += 1
    print(y)
    url = 'https://www.transfermarkt.com/yuri-berchiche/profil/spieler/{}'.format(i['id'])
    try:
        driver.get(url)
    except:
        time.sleep(1)
        driver.get(url)
    wait = WebDriverWait(driver, 20)  # longest waiting time to be 20s
    try:
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div[8]/div/div[1]/div[4]/div[2]/span[1]")))
    except:
        pass
    i['NAME'] = ""
    i['Dateofbirth'] = ""
    i['Citizenship'] = ""
    i['Age'] = ""
    i['Height'] = ""
    i['Currentclub'] = ""
    i['Position'] = ""
    i['Foot'] = ""

    time.sleep(4)

    try:
        i['NAME'] = driver.execute_script(
            'return document.querySelector("#main > div:nth-child(12) > div > div.dataHeader.dataExtended > div.dataMain > div > div.dataName > h1").innerText')
    except:
        continue
    xx = driver.execute_script(
        'return document.querySelector("#main > div:nth-child(12) > div > div.dataHeader.dataExtended > div.dataContent > div > div:nth-child(1) > p:nth-child(1) > span.dataValue").innerText')
    i['Dateofbirth'] = xx.split("(")[0]
    i['Citizenship'] = driver.execute_script(
        'return document.querySelector("#main > div:nth-child(12) > div > div.dataHeader.dataExtended > div.dataContent > div > div:nth-child(1) > p:nth-child(3) > span.dataValue > span").innerText')
    i['Age'] = xx.split("(")[1][:-1]
    i['Height'] = driver.execute_script(
        'return document.querySelector("#main > div:nth-child(12) > div > div.dataHeader.dataExtended > div.dataContent > div > div:nth-child(2) > p:nth-child(1) > span.dataValue").innerText')
    while True:
        try:
            i['Currentclub'] = driver.execute_script(
                'return document.querySelectorAll(".vereinprofil_tooltip.tooltipstered")[2].innerText')
            break
        except:
            time.sleep(1)
            continue
    i['Position'] = driver.execute_script(
        'return document.querySelector("#main > div:nth-child(12) > div > div.dataHeader.dataExtended > div.dataContent > div > div:nth-child(2) > p:nth-child(2) > span.dataValue").innerText')
    i['Foot'] = driver.execute_script(
        'return document.querySelector("#main > div:nth-child(16) > div.large-8.columns > div:nth-child(2) > div.row.collapse > div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten > div.spielerdaten > table > tbody > tr:nth-child(8) > td").innerText')
    if i['Foot'] not in ['left', 'right','both']:
        try:
            i['Foot'] = driver.execute_script(
                'return document.querySelector("#main > div:nth-child(16) > div.large-8.columns > div:nth-child(2) > div.row.collapse > div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten > div.spielerdaten.min-height-audio > table > tbody > tr:nth-child(7) > td").innerText')
        except:
            i['Foot'] = driver.execute_script(
                'return document.querySelector("#main > div:nth-child(16) > div.large-8.columns > div:nth-child(2) > div.row.collapse > div.large-6.large-pull-6.small-12.columns.spielerdatenundfakten > div.spielerdaten > table > tbody > tr:nth-child(7) > td").innerText')
    time.sleep(1)
    print(1)


import pandas as pd
df = pd.DataFrame(boll_id)
df.to_csv('data.csv', index=False)

