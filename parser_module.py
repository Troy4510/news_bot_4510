from bs4 import BeautifulSoup
import requests


def go(url):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, 'lxml')
    result = []
    news = soup.find_all('a', class_='cell-list__item-link color-font-hover-only')
    print(f'news found: {len(news)}')

    for new in news:
        time1 = new.find('div', class_="cell-info__date").text
        name1 = new.get('title')
        link1 = new.get('href')
        if len(time1) <= 5: #берём только сегодняшние
            result.append([time1,name1,link1])
    
    return result

    
if __name__ == "__main__":
    #parser(url)
    pass