#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import urllib.parse as urlparse
language = "java"


if( language == "java"):
    something ="polymorphism"
    url = 'http://www.google.com/search?q=' + something
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        if "www.javatpoint.com" in str(link):
            stri = str(link.get('href'))
            break
    data = stri.split("&")
    parsed = urlparse.urlparse(data[0])
    h = urlparse.parse_qs(parsed.query)['q']
    page1 = requests.get(h[0])
    soup1 = BeautifulSoup(page1.text, "html.parser")

    for header in soup1.find_all('h1'):
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
    url = 'http://www.google.com/search?q=' + something
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        if "www.javatpoint.com" in str(link):
            stri = str(link.get('href'))
            break
    data = stri.split("&")
    parsed = urlparse.urlparse(data[0])
    h = urlparse.parse_qs(parsed.query)['q']
    page1 = requests.get(h[0])
    soup1 = BeautifulSoup(page1.text, "html.parser")
    for header in soup1.find_all('h1'):
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
elif(language == "python"):
    something = "numbers in python "
    url = 'http://www.google.com/search?q=' + something
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("a")

    for link in links:
        if "www.programiz.com" in str(link):
            print(link.get('href'))
            stri = str(link.get('href'))
            break
    data = stri.split("&")
    print(data[0])
    parsed = urlparse.urlparse(data[0])
    h = urlparse.parse_qs(parsed.query)['q']
    print(h[0])
    page1 = requests.get(h[0])
    soup1 = BeautifulSoup(page1.text, "html.parser")

    for header in soup1.find_all('h1'):
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
    print("invalid")

