import requests
url = 'http://books.toscrape.com/catalogue/page-1.html'
response = requests.get(url)
html_content = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
books = soup.find_all('article', class_='product_pod')

book_data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    book_data.append([title, price])

import csv
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])
    writer.writerows(book_data)
