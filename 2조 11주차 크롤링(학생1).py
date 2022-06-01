#국내도서 종합 베스트셀러
import requests
from bs4 import BeautifulSoup

url = "http://www.yes24.com/24/category/bestseller" #Yes24 사이트 불러오기
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
books = soup.select("ol > li")

book_info = [] #각 책 정보별로 리스트를 지정해서 넣기 위해 모든 정보를 다 넣을 리스트 지정
for book in books:
    book_name = book.select("p > a")[2].text #책 제목
    book_price = book.select("p.price > strong")[0].text #책 가격

    book_info.append([book_name, book_price])

print(book_info)

#학생1의 역할