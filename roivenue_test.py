import requests
from bs4 import BeautifulSoup

skapiec_url = 'https://www.skapiec.pl/ogrod.html'
eshop_urls = []

# Scrape the first 10 pages
for page_number in range(1, 11):
    url = f'{skapiec_url}?page={page_number}'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Find the URLs of eShops
    product_links = soup.find_all('a', class_='button button--primary button--md button--fw-500 product-box-narrow__button product-box-narrow__button--shop')
    for link in product_links:
        eshop_url = link.get('href')
        eshop_urls.append((page_number, eshop_url))

# Save the unique eShop URLs along with the page number to a file
with open('eshop_urls.txt', 'w') as file:
    for page_number, url in eshop_urls:
        file.write(f'Page {page_number}: {url}\n')
