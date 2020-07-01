import requests
import sys
import webbrowser
import bs4


def google_search(query):
    res = requests.get("https://google.com/search?q={}".format(query))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    linkElements = soup.select("a")
    # print(linkElements)
    # linkToOpen = min(5, len(linkElements))
    webbrowser.open("https://google.com" + linkElements[3].get('href'))

# google_search("hi")
query = "hi"
webbrowser.open("https://google.com/search?q={}".format(query))