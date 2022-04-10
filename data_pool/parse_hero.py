# 抽取所有角色信息
import itertools
import re
from turtle import rt
from bs4 import BeautifulSoup, Tag
from soup_handle import getSoup, parseTBody


def parseHero(path: str):
    soup = getSoup(path)

    baseInfo = getBaseInfo(soup)
    # print(baseInfo)
    baseAttr = fixBaseAttr(getBaseAttr(soup))
    # print(baseAttr)
    geniues = getGeniues(soup)
    print(geniues)


def getBaseInfo(soup: BeautifulSoup) -> dict:
    r = {}
    content = soup.find('div', class_='detail__content')
    heroDetail = content.find('div', class_='obc-tmp-character__property')
    heroDetailKeys = heroDetail.find_all('div',
                                         class_='obc-tmp-character__key')
    heroDetailValues = heroDetail.find_all('div',
                                           class_='obc-tmp-character__value')
    for (k, v) in zip(heroDetailKeys, heroDetailValues):
        r[k.string.strip()] = v.string.strip()

    return r


# 初始属性
# 20级属性
# 20级突破属性
# 40级属性
# 40级突破属性
# 50级属性
# 50级突破属性
# 60级属性
# 60级突破属性
# 70级属性
# 70级突破属性
# 80级属性
# 80级突破属性
# 90级属性
def fixBaseAttr(baseAttr: dict) -> dict:
    r = {}
    for attr in baseAttr.keys():
        if attr == 'g1':
            materialNum = {}
            ms = baseAttr[attr]['突破材料']
            for (mk, mv) in ms.items():
                materialNum[mk] = int(mv)
            r['突破材料'] = materialNum
            initAttr = baseAttr[attr]
            r['初始属性'] = {
                '攻击方式': initAttr['攻击方式'],
                '攻击力': initAttr['攻击力'],
                '生命值': initAttr['生命值'],
                '暴击率': initAttr['暴击率'],
                '暴击伤害': initAttr['暴击伤害'],
                '元素精通': initAttr['元素精通'],
                '元素充能': initAttr['元素充能'],
                '防御力': initAttr['防御力'],
                '治疗加成': initAttr['治疗加成'],
                '受治疗加成': initAttr['受治疗加成'],
            }
        elif attr < 'g8':
            curAttr = baseAttr[attr]
            if attr == 'g2':
                r['20级属性'] = {
                    '攻击力': curAttr['突破前攻击力（初始武器）'],
                    '生命值': curAttr['突破前生命值'],
                    '暴击伤害': curAttr['突破前暴击伤害'],
                    '防御力': curAttr['突破前防御力'],
                }
                r['20级突破后属性'] = {
                    '攻击力': curAttr['突破后攻击力（初始武器）'],
                    '生命值': curAttr['突破后生命值'],
                    '暴击伤害': curAttr['突破后暴击伤害'],
                    '防御力': curAttr['突破后防御力'],
                }
                if '新天赋解锁' in curAttr.keys():
                    r['20级解锁天赋'] = curAttr['新天赋解锁']
            elif attr == 'g3':
                r['40级属性'] = {
                    '攻击力': curAttr['突破前攻击力（初始武器）'],
                    '生命值': curAttr['突破前生命值'],
                    '暴击伤害': curAttr['突破前暴击伤害'],
                    '防御力': curAttr['突破前防御力'],
                }
                r['40级突破后属性'] = {
                    '攻击力': curAttr['突破后攻击力（初始武器）'],
                    '生命值': curAttr['突破后生命值'],
                    '暴击伤害': curAttr['突破后暴击伤害'],
                    '防御力': curAttr['突破后防御力'],
                }
                if '新天赋解锁' in curAttr.keys():
                    r['40级解锁天赋'] = curAttr['新天赋解锁']
            elif attr == 'g4':
                r['50级属性'] = {
                    '攻击力': curAttr['突破前攻击力（初始武器）'],
                    '生命值': curAttr['突破前生命值'],
                    '暴击伤害': curAttr['突破前暴击伤害'],
                    '防御力': curAttr['突破前防御力'],
                }
                r['50级突破后属性'] = {
                    '攻击力': curAttr['突破后攻击力（初始武器）'],
                    '生命值': curAttr['突破后生命值'],
                    '暴击伤害': curAttr['突破后暴击伤害'],
                    '防御力': curAttr['突破后防御力'],
                }
                if '新天赋解锁' in curAttr.keys():
                    r['50级解锁天赋'] = curAttr['新天赋解锁']
            elif attr == 'g5':
                r['60级属性'] = {
                    '攻击力': curAttr['突破前攻击力（初始武器）'],
                    '生命值': curAttr['突破前生命值'],
                    '暴击伤害': curAttr['突破前暴击伤害'],
                    '防御力': curAttr['突破前防御力'],
                }
                r['60级突破后属性'] = {
                    '攻击力': curAttr['突破后攻击力（初始武器）'],
                    '生命值': curAttr['突破后生命值'],
                    '暴击伤害': curAttr['突破后暴击伤害'],
                    '防御力': curAttr['突破后防御力'],
                }
                if '新天赋解锁' in curAttr.keys():
                    r['60级解锁天赋'] = curAttr['新天赋解锁']
            elif attr == 'g6':
                r['70级属性'] = {
                    '攻击力': curAttr['突破前攻击力（初始武器）'],
                    '生命值': curAttr['突破前生命值'],
                    '暴击伤害': curAttr['突破前暴击伤害'],
                    '防御力': curAttr['突破前防御力'],
                }
                r['70级突破后属性'] = {
                    '攻击力': curAttr['突破后攻击力（初始武器）'],
                    '生命值': curAttr['突破后生命值'],
                    '暴击伤害': curAttr['突破后暴击伤害'],
                    '防御力': curAttr['突破后防御力'],
                }
                if '新天赋解锁' in curAttr.keys():
                    r['70级解锁天赋'] = curAttr['新天赋解锁']
            elif attr == 'g7':
                r['80级属性'] = {
                    '攻击力': curAttr['突破前攻击力（初始武器）'],
                    '生命值': curAttr['突破前生命值'],
                    '暴击伤害': curAttr['突破前暴击伤害'],
                    '防御力': curAttr['突破前防御力'],
                }
                r['80级突破后属性'] = {
                    '攻击力': curAttr['突破后攻击力（初始武器）'],
                    '生命值': curAttr['突破后生命值'],
                    '暴击伤害': curAttr['突破后暴击伤害'],
                    '防御力': curAttr['突破后防御力'],
                }
                if '新天赋解锁' in curAttr.keys():
                    r['80级解锁天赋'] = curAttr['新天赋解锁']
        else:
            curAttr = baseAttr[attr]
            r['90级属性'] = {
                '攻击力': curAttr['攻击力（初始武器）'],
                '生命值': curAttr['生命值'],
                '暴击伤害': curAttr['暴击伤害'],
                '防御力': curAttr['防御力'],
            }

    return r


def getBaseAttr(soup: BeautifulSoup) -> dict:

    def commonAttrPattern(attr: Tag) -> dict:
        g = {}
        gradeSecondAttr = attr.find_all('tbody')
        rushMaterial = gradeSecondAttr[0]
        secondGradeAttr = gradeSecondAttr[1]
        materialsTitle = rushMaterial.find('td', class_='h3').string.strip()
        materialNums = {}
        materialsMap = rushMaterial.find('ul').find_all('li')
        for l in materialsMap:
            materialName = l.find('span', class_='obc-tmpl__icon-text')
            materialNum = l.find('span', class_='obc-tmpl__icon-num')
            if materialName and materialNum and materialName.string and materialNum.string:
                materialNums[materialName.string.strip(
                )] = materialNum.string.strip().replace('*', '')
        g[materialsTitle] = materialNums
        infos = parseTBody(secondGradeAttr)
        ks, vs = [], []
        flattenInfos = [i for info in infos for i in info]
        for fInfo in flattenInfos:
            if fInfo.string:
                ks.append(fInfo.string.strip())
            elif fInfo.find('span'):
                txt = fInfo.find('span').string.strip()
                vs.append(txt)
        for (k, v) in zip(ks, vs):
            g[k] = v
        return g

    attrs = soup.find('ul', class_='obc-tmpl__switch-list')

    r = {}

    g1 = {}

    initGrade = attrs.find('li', {'data-index': '0'})
    i = 0
    while initGrade:
        r[f'g{i+1}'] = commonAttrPattern(initGrade)
        i += 1
        initGrade = initGrade.find_next_sibling('li', {'data-index': f'{i}'})

    return r


def getGeniues(soup: BeautifulSoup) -> dict:
    r = {}
    geniues = soup.find('div', attrs={
        'data-part': 'skill'
    }).find('ul', class_='obc-tmpl__switch-list').find('li')

    while geniues:
        geniuesName = geniues.find('h3').find('span').string.strip()
        if geniuesName.find('普通攻击') > -1:
            geniuesDesc = geniues.find('pre').string.strip().replace(',', '，')
            attrSpec = parseTBody(geniues.find('tbody'))
            attrDetail = {}
            for attr in attrSpec:
                for idx, a in enumerate(attr):
                    if idx == 0:
                        attrDetail[a.string.strip()] = {}
                    else:
                        if a.string:
                            attrDetail[attr[0].string.strip(
                            )][f'LV{idx}'] = a.string.strip()
                        else:
                            breakMaterials = []
                            ms = a.find_all('div',
                                            class_='obc-tmpl__icon-text-num')
                            materialMap = {}
                            for m in ms:
                                spans = m.find_all('span')
                                if len(spans) > 0:
                                    materialMap[spans[0].string.strip(
                                    )] = spans[1].string.strip().replace(
                                        '*', '') if len(spans) > 1 else ''
                                    breakMaterials.append(materialMap)
                            attrDetail[attr[0].string.strip(
                            )][f'LV{idx}'] = breakMaterials
            r[geniuesName] = {
                '天赋名称': geniuesName,
                '天赋描述': geniuesDesc,
                '详细属性': attrDetail
            }
        geniues = geniues.find_next_sibling('li')
    return r


parseHero('./heros/刻晴.html')