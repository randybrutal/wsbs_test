# -*- coding: utf-8 -*-
import urllib,  bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

print('請設定儲存路徑:')
save=str(input())
print('請輸入網址:')
url=str(input())
print('是下載西斯版嗎?\n(1)是\t(2)否')
switch=int(input())
print('總共有幾則留言呢')
times=int(input())
print('停留秒數(sec)\n若網路不佳可以著量調長 原則上設定為1')
t=int(input())

browser = webdriver.Chrome()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
i=0

browser.get(url)                # 開啟網頁
browser.maximize_window()
time.sleep(3)
if switch==1:
    browser.find_element_by_class_name('Button_primary_3KkkP').click()
for i in range(0,int(times/30)+15):
    ActionChains(browser).key_down(Keys.END).key_up(Keys.END).perform()
    time.sleep(int(t))


html_doc = browser.page_source               # 取得資料
browser.quit();                # 關閉瀏覽器

soup = bs4.BeautifulSoup(html_doc, "lxml")               # 取得html原始碼
for link in soup.find_all('a'):              # 查找使用者輸入之目標
    c=link.get('href')
    if c!=None:
        q=c.find('jpg')
        p=c.find('http')
        if q!=-1 and p!=-1:
            r = urllib.request.Request(url=c, headers=headers)
            f = urllib.request.urlopen(r)
            data = f.read()
            with open(save+'/a'+str(i)+'.jpg', "wb") as code:
                code.write(data)
            i=i+1
            print(c)
for link in soup.find_all('img'):
    c=link.get('src')
    if c!=None:
        q=c.find('jpg')
        p=c.find('http')
        if q!=-1 and p!=-1:
            r = urllib.request.Request(url=c, headers=headers)
            f = urllib.request.urlopen(r)
            data = f.read()
            with open(save+'/'+str(i)+'.jpg', "wb") as code:
                code.write(data)
            i=i+1
            print(c)