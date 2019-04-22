#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
language = "java"
#something = "inheritance-in-cpp"
#url = 'http://www.google.com/search?q='+something
if( language == "java"):
    something ="throw-in-java"
    url = 'https://www.javatpoint.com/'+something
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for header in soup.find_all('h1'):
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                print(nextNode.strip())
            if isinstance(nextNode, Tag):
                if nextNode.name == "h3":
                    break
                print(nextNode.get_text(strip=True).strip())
elif(language == "cpp"):
    something = "cpp-inheritance"
    url = 'https://www.javatpoint.com/'+something
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for header in soup.find_all('h1'):
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, NavigableString):
                print(nextNode.strip())
            if isinstance(nextNode, Tag):
                if nextNode.name == "h2":
                    break
                print(nextNode.get_text(strip=True).strip())
else:
    something = "numbers"
    url = 'https://www.programiz.com/python-programming/'+something
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

#page = requests.get(url)
#soup = BeautifulSoup(page.text, "html.parser")
#artist = soup.find(class_='onlycontentinner')
#print(soup.get_text())
#for para in artist.find_all('h1', recursive=True):
 #   print(para.text)
#print(artist.get_text())


#link = soup.find('cite').text
#print(link)
#res = requests.get(link)
#soup1 = BeautifulSoup(res.text,'html.parser')


#if( something == "inheritance-in-java"):
    #print("this")
#url = 'https://www.javatpoint.com/'+something
