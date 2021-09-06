from bs4 import BeautifulSoup

import requests
import urllib.request
import shutil

base_url = 'https://www.emploidakar.com/jm-ajax/get_listings?page='
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}
response = requests.get(base_url, headers=header).json()

soup = BeautifulSoup(response.get('html'), 'html.parser')

page_max = response.get('max_num_pages')
print('Max number of page is:', page_max)

links = set({'  /',
            'https://www.emploidakar.com/offre-demploi/ingenieur-devops-3/'})

# for page in range(1, page_max):
#     url = base_url + str(page)
#     print('scraping page', page, 'at url', url)
#     response = requests.get(url, headers=header).json()
#     soup = BeautifulSoup(response.get('html'), 'html.parser')
#     items = soup.find_all('a')
#     for i in items:
#         links.add(i['href'])

# print(links)


for link in links:
    print(link)
    response = requests.get(link, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find('ul', class_='job-listing-meta meta')
    li = items.find(class_=False)
    keyword = li.find('a')
    print(li)
