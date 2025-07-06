import requests
from bs4 import BeautifulSoup

def parse_film_from_wiki(wiki_url):
    resp = requests.get(wiki_url)
    soup = BeautifulSoup(resp.text, "lxml")
    img = soup.find(class_="infobox-image").find(class_="mw-file-element").get("src")

    title = soup.find(class_="infobox-above").string
    if title == None:
        title = "title not found"
    title = title.replace("'", "''")
    return [title, wiki_url, img]
