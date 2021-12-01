from bs4.dammit import encoding_res
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/Soham Gupta/Desktop/C-127/chromedriver_win32")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["NAME" , "DISTANCE" , 	"MASS" , "RADIUS"]
    star_data = []
    for i in range(0 , 458): 
        soup = BeautifulSoup(browser.page_source , "html.parser")
        for tr_tag in soup.find_all("tr" , attrs={"class" , "stars"}):
            td_tags = tr_tag.find_all("td")
            temp_list = []

            for index , td_tag in enumerate(td_tags):
                if index== 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")

            star_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]/td[2]/a').click()
    with open("stars.csv" , "w" )as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()

