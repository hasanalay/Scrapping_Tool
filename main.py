from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time

# chrome driver kurulumu

browser = webdriver.Chrome()
link = 'https://www.sahibinden.com/arazi-suv-pickup-citroen-c3-aircross-1.5-bluehdi-feel'
browser.get(link)
time.sleep(2)

cars = browser.find_elements(by=By.CSS_SELECTOR, value='.searchResultsItem')
my_dict = {}
Cars_List = []
for car in cars:
    if car.get_attribute('data-id') is None:
        continue
    else:
        infos = car.find_elements(by=By.CSS_SELECTOR, value='.searchResultsAttributeValue')
        price = car.find_elements(by=By.CSS_SELECTOR, value='.searchResultsPriceValue')
        # print(infos[0].text, price[0].text)
    my_dict["model_year"] = f"{infos[0].text}"
    my_dict["price"] = f"{price[0].text}"

    Cars_List.append(my_dict)

print(f"Cars_List: ", Cars_List)
print(*Cars_List, sep='\n')
# Get all the values inside the dict.
# Cars[ {'year': '...', 'price': '..'},
#       {'year': '...', 'price': '..'},
#       {'year': '...', 'price': '..'}]
# şeklinde dict içine kaydedetmek gerekiyo
# tüm sayfaları birbirine append ile birleştirip tüm veriyi elde edip hepsini birleştirmeliyiz
# haftaya hazır halde geleceğiz.
# browser.find_element(by=By.CSS_SELECTOR, value='#searchResultsSearchForm > div > div.searchResultsRight > div.mtmdef.pageNavigator.pvdef.phdef > div.pageNavTable > ul > li:nth-child(2) > a').click()

# Find the page items like 1,2,3 pages
# gelen veriyi list of list olarak alıp csv olarak kaydedip regresyon modeli oluşturacağım.


time.sleep(2)
browser.close()
