import re
from bs4 import BeautifulSoup

with open('./heros/刻晴.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

    content = soup.find('div', class_='detail__content')
    heroDetail = content.find('div', class_='obc-tmp-character__property')
    heroDetailKeys = heroDetail.find_all('div',
                                         class_='obc-tmp-character__key')
    heroDetailValues = heroDetail.find_all('div',
                                           class_='obc-tmp-character__value')
    # for (k, v) in zip(heroDetailKeys, heroDetailValues):
    #     print(k.string, ' ', v.string)

    attrs = soup.find('ul', class_='obc-tmpl__switch-list')
    firstGrade = attrs.find('li', {'data-index': '0'}).find_all('tbody')
    materials = firstGrade[0]
    firstGradeAttr = firstGrade[1]
    attrKeys = firstGradeAttr.find_all('td', class_='h3')
    attrValues = firstGradeAttr.find_all('span')

    # for (k, v) in zip(attrKeys, attrValues):
    #     print(k.string, ' ', v.string)

    genius = soup.find('div', attrs={
        'data-part': 'skill'
    }).find('ul', class_='obc-tmpl__switch-list')
    g1 = genius.find('li')
    # g2 = g1.find_next('li')
    # 普通攻击
    commonAttack = r'(普通攻击\s[\u4e00-\u9fa5|，|。]+。)\s+(重击\s+[\u4e00-\u9fa5|，|。]+)\s+(下落攻击\s+[\u4e00-\u9fa5|，|。]+)'
    g1Name = g1.find('h3').find('span').string
    g1Desc = g1.find('pre').string.replace(',', '，')
    p = re.compile(commonAttack)
    attackList = []
    for g in p.finditer(g1Desc):
        attackList.append(g.group())
    g1Attr = g1.find('table')
    g1AttrTh = g1Attr.find('thead').find_all('th')
    g1AttrTr = g1Attr.find('tbody').find_all('tr')
    for td in g1AttrTh:
        print(td.string.strip(), end=' ')
    print()
    for tr in g1AttrTr:
        tds = tr.find_all('td')
        if tds[0].string.strip() != '升级材料':
            for td in tr:
                print(td.string.strip(), end=' ')
        print()

    life = soup.find('div', attrs={'data-part': 'life'}).find('table')
    lifeTh = life.find('thead').find_all('th')
    lifeTr = life.find('tbody').find_all('tr')
    for td in lifeTh:
        print(td.string.strip(), end=' ')
    print()
    for tr in lifeTr:
        tds = tr.find_all('td')
        for td in tr:
            if td.string:
                print(td.string.strip(), end=' ')
            elif td.find('span'):
                print(td.find('span').string, end=' ')
        print()

    main = soup.find_all('div',
                         attrs={
                             'data-part': 'main',
                             'data-tmpl': 'fold'
                         })
    # mainTitle = main.find('div', class_='obc-tmpl-fold__title')
    # mainDesc = main.find('div', class_='obc-tmpl__rich-text')
    for m in main:
        title = m.find('p').string.strip()
        if title == '角色名片':
            print(m.find('img'))
        elif title == '角色CV':
            for ap in m.find_all('p'):
                print(ap)
        elif title == '特殊料理':
            print(m.find('p'))
        elif title == '更多描述':
            for pp in m.find('div',
                             class_='obc-tmpl__paragraph-box').find_all('p'):
                print(pp)
        else:
            for pp in m.find('div',
                             class_='obc-tmpl__paragraph-box').find_all('p'):
                print(pp)