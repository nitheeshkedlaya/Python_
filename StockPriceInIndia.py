import requests
from bs4 import BeautifulSoup
import re
import webbrowser

stock=input("Please enter name of the stock  ")

page = requests.get("https://www.google.dz/search?q="+stock+"+share+price")
soup = BeautifulSoup(page.content,"lxml")

links = soup.findAll("a")
x=[]

for link in  soup.find_all("a",href=re.compile("(?<=/url\\?q=)(htt.*://.*)")):
     #print (re.split(":(?=http)",link["href"].replace("/url?q=","")))
     x.append(re.split(":(?=http)",link["href"].replace("/url?q=","")))

url=str(x[0])

unnes="[']'"

for char in unnes:
    url=url.replace(char,'')


webbrowser.open(url)
res=requests.get(url)

icesoup = BeautifulSoup(res.text,features='html.parser')


price_box=icesoup.find('span',attrs={'class','txt15B nse_span_price_wrap hidden-xs'})

price=price_box.text

name_box=icesoup.find('h1',attrs={'class','pcstname'})
name=name_box.text

print("Price of the share "+name+" is "+price)


