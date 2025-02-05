from bs4 import BeautifulSoup
import requests

sites = {
    "news": {
        "english": "https://www.bbc.com/news",
        "italian": "https://www.repubblica.it/italia/",
        "spanish": "https://elpais.com",
    },
    "cinema": {
        "english": "https://www.imdb.com/news/movie/",
        "italian": "https://cineuropa.org/it/",
        "spanish": "https://www.fotogramas.es/",
    },
    "sports": {
        "english": "https://www.espn.com",
        "italian": "https://www.repubblica.it/sport/",
        "spanish": "https://www.marca.com",
    },
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
} 

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
})

def scrape_cineuropa(url):
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url, headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []

        for article in soup.find_all('div', class_='article clear-block news', limit=5):
            title_tag = article.find('h2', class_='clear-float').find('a')
            title = title_tag.get_text(strip=False) if title_tag else None
            print('Title', title)
            link = title_tag['href'] if title_tag and title_tag.has_attr('href') else None

            image_tag = article.find('div', class_='box-foto-article').find('img', src=True)
            image = image_tag['src'] if image_tag else None
            print('image', image)

            if title and link:
                articles.append({
                    "title": title,
                    "url": f"https://cineuropa.org/{link}",  
                    "image": f"https://cineuropa.org/{image}" if image else None,
                })

        return articles
    except Exception as e:
        return {"error": str(e)}

def scrape_fotogramas(url):
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url, headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []

        for article in soup.find_all('a', class_='css-kxu6hh', limit=5):
            link = article['href'] if article.has_attr('href') else None

            image_tag = article.find('img', src=True)
            image = image_tag['src'] if image_tag else None

            title_tag = article.find('span', class_='css-1rusrk')
            title = title_tag.get_text(strip=True) if title_tag else None

            if title and link:
                full_link = link if link.startswith('http') else f"https://www.fotogramas.es/{link}"
                articles.append({
                    "title": title,
                    "url": full_link,
                    "image": image
                })

        return articles
    except Exception as e:
        return {"error": str(e)}

def scrape_imdb(url):
    try:
        print(f"Fetching data from: {url}")
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []

        for container in soup.find_all('div', class_='sc-52810589-5', limit=5):

            image_tag = container.find('img', class_='ipc-image')
            image = image_tag['src'] if image_tag else None

            description_tag = container.find('div', class_='ipc-html-content-inner-div')
            description = description_tag.get_text(strip=True) if description_tag else None

            link_tag = container.find('a', class_='ipc-link')
            link = link_tag['href'] if link_tag and link_tag.has_attr('href') else None
            if link and not link.startswith('http'):
                link = f"https://www.imdb.com/{link}" 

            if image and description and link:
                articles.append({
                    "title": description,
                    "url": link,
                    "image": image,
                })

        return articles
    except Exception as e:
        return {"error": str(e)}
    
def scrape_repubblica(url):
    try:
        print(f"Fetching data from: {url}")
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []

        for article in soup.find_all('article', class_='entry'):
            title_tag = article.find('h2', class_='entry__title')
            title = title_tag.get_text(strip=True) if title_tag else None

            link_tag = title_tag.find('a') if title_tag else None
            link = link_tag['href'] if link_tag and link_tag.has_attr('href') else None

            image_tag = article.find('figure', class_='entry__media').find('img')
            image = image_tag['src'] if image_tag else None

            author_tag = article.find('span', class_='entry__author')
            author = author_tag.get_text(strip=True) if author_tag else None

            if title and link:
                articles.append({
                    "title": title,
                    "url": link,
                    "image": image,
                })

        return articles

    except Exception as e:
        return {"error": str(e)}

def scrape_repubblica_sports(url):
    try:
        print(f"Fetching data from: {url}")
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []

        for article in soup.find_all('article', class_='entry'):
            title_tag = article.find('h2', class_='entry__title')
            title = title_tag.get_text(strip=True) if title_tag else None

            link_tag = title_tag.find('a') if title_tag else None
            link = link_tag['href'] if link_tag and link_tag.has_attr('href') else None

            figure_tag = article.find('figure', class_='entry__media')
            image_tag = figure_tag.find('img') if figure_tag else None
            image = image_tag['src'] if image_tag else None

            overtitle_tag = article.find('span', class_='entry__overtitle')
            overtitle = overtitle_tag.get_text(strip=True) if overtitle_tag else None

            author_tag = article.find('span', class_='entry__author')
            author = author_tag.get_text(strip=True) if author_tag else None
        
            if title and link:
                articles.append({
                    "title": title,
                    "url": link,
                    "image": image,
                })

        return articles

    except Exception as e:
        return {"error": str(e)}