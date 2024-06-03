import urllib3
from bs4 import BeautifulSoup

def parse():
    url = 'https://omgtu.ru'
    http = urllib3.PoolManager(cert_reqs='CERT_NONE')  # Отключаем проверку сертификата
    response = http.request('GET', url)
    print(response.status)
    soup = BeautifulSoup(response.data, "html.parser")

    headlines = []
    blocks = soup.findAll('h3', class_='news-card__title')

    for block in blocks:
        headline = block.text
        headlines.append(headline)

    with open('headlines.txt', 'w') as file:
        for headline in headlines:
            file.write(headline + '\n')

if __name__ == '__main__':
    parse()
