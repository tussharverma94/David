import selenium, requests, bs4, webbrowser

def youtube_search(query, number_of_link_to_open = 1):
    res = requests.get("https://www.youtube.com/search?q={}".format(query))
    res.raise_for_status()
    webbrowser.open("https://www.youtube.com/search?q={}".format(query))
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    link_elements = soup.select('a')
    num_link_to_open = min(5, len(link_elements))
    print(num_link_to_open)
    for i in range(num_link_to_open):
        webbrowser.open("https://www.youtube.com"+link_elements[i].get('href'))

query = "hi"
youtube_search(query)