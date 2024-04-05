'''
n = input ("input a number")
sum = 0
for i in range(int(n)):
   sum += i+1
print("1 to n = ", sum)
'''
'''
x = "hello"
sum = eval("x")
print ("sum = ", sum)
'''

'''
print(input("input "))
'''
'''
import jieba
print(jieba.lcut("中国是一个伟大的国家"))
'''

'''
def getText():
    txt = open("Ham.txt", "r").read()
    txt = txt.lower()
    for ch in '!"&#@%$*':
        txt =txt.replace(ch, " ")
    return txt
hamtxt = getText()

words = hamtxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
'''

import requests
from bs4 import BeautifulSoup
allUniv = []

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def fillUnivList(soup):
     data = soup.find_all('tr')
     for tr in data:
         ltd = tr.find_all('td')
         if len(ltd)==0:
             continue
         singleUniv = []
         for td in ltd:
             singleUniv.append(td.string)
         allUniv.append(singleUniv)


def printUnivList(num):
     print("{:^4}{:^10}".format("排名","总分"))
     for i in range(num):
        u = allUniv[i]
        print("{:^4}{:^10}".format(u[0],u[4]))

def main(num):
    url = 'https://www.shanghairanking.cn/rankings/bcur/202311.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    fillUnivList(soup)
    printUnivList(num)

main(10)
































