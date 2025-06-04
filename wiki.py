import requests
from bs4 import BeautifulSoup

def parse_film_info():

    """
    Return list with films data. every film data is list with:  [film№,  wiki-url,   film-image, film-title]
    """
    try:
        with open("films-links.txt") as flims_links:
            tmp = flims_links.read()                    #открыл и прочитал документ с ссылками на вики статьи о фильмах
    except:
        try:
            with open("/home/ObscureObscure/mysite/static/films-links.txt") as flims_links:
                tmp = flims_links.read() 
        except:
            with open("C:/Users/admin/Desktop/my-web-app/static/films-links.txt") as flims_links:
                tmp = flims_links.read() 


    lines_list= tmp.split()         #список с str ссылками  на статьи
    counter = 0                     
    films_data = []                 #список для записи данных о фильмах

    for i in range(len(lines_list)):
        counter += 1                #номер фильма в списке (начиная с 1)
        url = lines_list[i]         #ссылка на фильм
        resp = requests.get(url)    #resp.text вернет html код страницы в формате str                       
        soup = BeautifulSoup(resp.text, "lxml")      #суп объект из которого можно вытянуть инфу с википедии

        img = soup.find(class_="infobox-image").find(class_="mw-file-element").get("src")
        title = soup.find(class_="infobox-above").string

        films_data.append(["film_№" + str(counter), url, img, title])
    return  (films_data)
