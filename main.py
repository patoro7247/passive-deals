import os
import psycopg2
from dotenv import load_dotenv
import requests
import re
import json
import pprint
from bs4 import BeautifulSoup

load_dotenv()


conn = psycopg2.connect(dbname=os.getenv('PG_DATABASE'), 
user=os.getenv('PG_USER'), password=os.getenv('PG_PASSWORD'), host=os.getenv('PG_HOST'))

cur = conn.cursor()
cur.execute("SELECT * FROM users;")
result = cur.fetchone()

#print(result);
print(result[3]['keyWord']);



def parseCookieFile(cookiefile):
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies = {}
    with open (cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line):
                lineFields = line.strip().split('\t')
                #print(lineFields)
                cookies[lineFields[5]] = lineFields[6]
    return cookies

cookies = parseCookieFile('cookies.txt')
cookie_json = json.dumps(cookies)

#pprint.pprint(cookies)




url = "https://offerup.com/search?q={}&PRICE_MAX={}&DISTANCE=20&DELIVERY_FLAGS=p".format(
    result[3]['keyWord'], result[3]['maxPrice'], result[2])

#print(url)
#session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0'
}

page = requests.get(url, cookies=cookies, headers=headers)
#//print(pprint.pprint(page.text))
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())
