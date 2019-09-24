import re
import requests


START_PAGES = ['']
LEVELS_DOWN_RABBIT_HOLE = 8


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Upgrade-Insecure-Requests': '1'}


r = requests.get('http://us1.westsideofdawn.com/hello', headers=HEADERS)

print('HEADERS:')
print(r.headers)
print()
print('Content:')
print(r.content)


def worker(depth = 0):
    while True:
        page = q.get()
        if page is None:
            break


with open('out.html', 'w') as f:
    f.write(str(r.content))

