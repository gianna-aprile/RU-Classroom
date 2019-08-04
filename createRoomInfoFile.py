from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#change my name to your username
driver_path = "/Users/giannaaprile/RUClassroom/chromedriver"
browser = webdriver.Chrome(driver_path)
f = open("spring2019rmInfo.txt", "w+")
rooms = open("spring2019.txt", "r")

lst = []

for line in rooms:
    try:
        split = line.split()
        roomName = split[7].split("-")[0]
        if roomName not in lst:
            lst.append(roomName)

    except:
        continue

browser.get("https://maps.rutgers.edu/#/?lat=40.2488462127653&lng=-74.70583984375003&sidebar=true&zoom=8")

for room in lst:
    time.sleep(2)
    searchBar = browser.find_element_by_xpath("""//*[@id="search"]""")
    searchBar.clear()
    searchBar.send_keys(room) 
    results = browser.find_elements_by_class_name("searchResult")
    
    found = 0
    for x in results:
        if x.find_element_by_class_name("search-result-abbr").text == room.upper():
            time.sleep(2)
            x.click()
            f.write(room + ' ' + browser.current_url+'\n')
            found = 1
            break
    
    if found == 0:
        browser.find_element_by_xpath("""//*[@id="rutgers-logo"]""").click()
        time.sleep(3)

    