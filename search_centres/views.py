import csv
import pandas as pd
from bs4 import BeautifulSoup
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    var = 0
    if(request.method == 'GET'):
        loc = request.GET.get('location')
        stype = request.GET.get('searchtype')
        l= loc
        print(stype)
        #options = Options()
        #options.add_argument("--headless")
        browser = webdriver.Chrome(executable_path='C://Users//nalib//Downloads//chromedriver_win32new//chromedriver.exe',)#options = options)
        url = "https://www.justdial.com/{}/{}/"
        u = url.format(loc, stype)
        fields = ['name', 'rating', 'address', 'links']
        print("hi")
        if(loc):
            browser.minimize_window()
            browser.get(u)
            browser.implicitly_wait(1000)
        
        page = browser.page_source
        soup = BeautifulSoup(page, 'html.parser')
        # print(soup)
        li = soup.find_all('li', class_="cntanr")
        with open("search_centres/yogacentres.csv", 'w', newline="",
                  encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerow(fields)

        names = []
        links = []
        ratings = []
        add = []
        for each in li:
            names.append(each.find('span', class_='lng_cont_name').text)
            link = each.find('a')
            links.append(link['href'])
            ratings.append(each.find('p', class_='newrtings').find('span').text)
            a = each.find('p', class_='address-info tme_adrssec')
            add.append(a.find('span', class_="cont_fl_addr").text)
        """print(names)
        print(links)
        print(ratings)
        print(add)"""
        rows = []
        for i in range(len(names)):
            row = [names[i], ratings[i], add[i], links[i]]
            rows.append(row)
        with open("search_centres/yogacentres.csv", 'a', newline="",
                  encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerows(rows)
        print(rows)
        browser.implicitly_wait(1000)
        browser.close()
        var = 1
        #loc = "Nellore"
        details = {'loc':loc,'searchtype':stype,'var':var}
        return render(request, 'search_centres/home.html',details)

def yoga_centres(request):

    df=pd.read_csv("search_centres/yogacentres.csv",encoding = "cp1252")
    clList=[pp for pp in df.keys()]
    allData=[]
    for i in range(df.shape[0]):
        temp=df.loc[i]
        allData.append(dict(temp))
        context= {'data':allData,'cl':clList}
    return render(request,'search_centres/centres.html',context)

