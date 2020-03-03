import requests

from bs4 import BeautifulSoup as bs



bottom = "https://www.imdb.com/chart/bottom"
top = "https://www.imdb.com/chart/top"

def getList(chart_url):
    r = requests.get(chart_url)
    if r.status_code != 200:
        raise requests.HTTPError(f"Error Code: {r.status_code} ; {r.text}")

    soup = bs(r.text, "lxml")
    links = set(map(lambda x: x.get('href',''), soup.find_all('a')))
    valid_links = list(filter(lambda x: x.startswith('/title/'), links))
    #print(valid_links, len(valid_links))
    return valid_links


def getReviews(title, ratin=10):
    url = f"https://www.imdb.com{title}reviews?sort=helpfulnessScore&dir=desc&ratingFilter={ratin}"
    r = requests.get(url)
    soup = bs(r.text, "lxml")
    reviews = soup.find_all("div", class_="content")
    reviews = list(map(lambda x: x.div.text, reviews))
    #reviews_s = soup.select(".content > div")
    #print(f"{len(reviews)}: \n\n{reviews}")
    return reviews


    

