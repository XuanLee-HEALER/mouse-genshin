from typing import List
from bs4 import BeautifulSoup, Tag


def getSoup(path) -> BeautifulSoup:
    with open(path, 'r') as f:
        return BeautifulSoup(f, features='html.parser')


def parseTBody(body: Tag) -> List[List[Tag]]:
    r = []
    trs = body.find_all('tr')
    for tr in trs:
        tds = [tr.find_all('td')]
        for td in tds:
            r.append(td)
    return r