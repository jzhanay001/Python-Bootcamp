#HTML tag for web scripting
import requests # module to make http/https requests
import html5lib # a small parser package for html-5
from bs4 import BeautifulSoup

amazon_url="https://www.amazon.com/HP-Touchscreen-Computer-Quard-Core-802-11ac/dp/B082PZVZB7/ref=sr_1_2_sspa?keywords=laptop&qid=1579030389&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMVdON0FWQ0RWMk0mZW5jcnlwdGVkSWQ9QTAzNjIwNDgyNUZFWlpWWVpaUk5HJmVuY3J5cHRlZEFkSWQ9QTA1MDAxMDAxRkMyWkZMM0lWMzhNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
agent_header={
    "User-Agent":agent

}

amazon_page=requests.get(amazon_url,headers=agent_header)

#print(type(amazon_page))
soup=BeautifulSoup(amazon_page.content, "html5lib")

price_span=str(soup.find(id="priceblock_ourprice"))

print(price_span)


price = ""
for char in price_span:
    if char.isdigit() is True:
        price+=char
    if char == ".":
        price += char

print(price)
price=float(price)
max_price=800

if price <= max_price:
    print("buy it")
else:
    print("NOt now")

time.sleep(86400) runs once a day
