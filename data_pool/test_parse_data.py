import imp
import os
from time import sleep
from bs4 import BeautifulSoup as bs
import http.client

from test_selenium import getDriver

with open('./pages.html', 'r') as f:

    def downloadImg(url, path, basePath):
        if not os.path.exists(basePath):
            os.mkdir(basePath)
        with open(path, 'wb') as f:
            baseUrl = url[8:url.index('com') + 3]
            reqUrl = url[url.index('com') + 3:]
            # print(baseUrl, reqUrl)
            conn = http.client.HTTPSConnection(baseUrl)
            conn.connect()
            conn.request('GET', reqUrl)
            resp = conn.getresponse()
            print(resp.status, resp.reason)
            f.write(resp.read())
            conn.close

    def downloadData(url, path, basePath):
        if not os.path.exists(basePath):
            os.mkdir(basePath)
        rootUrl = 'https://bbs.mihoyo.com'
        driver = getDriver()
        with open(path, 'w') as f:
            driver.get(rootUrl + url)
            f.write(driver.page_source)
            driver.quit()

    downloadList = []
    soup = bs(f, 'html.parser')

    avatars = soup.find_all('div', class_='collection-avatar')
    # print(avatars[0])
    heroAvatars = avatars[0]
    eles = heroAvatars.find_all('a')
    for ele in eles:
        dataUrl = ele['href']
        avatarUrl = ele.find('div',
                             class_='collection-avatar__icon')['data-src']
        if avatarUrl.find('png') != -1:
            splitPoint = avatarUrl.index('png')
        elif avatarUrl.find('jpg') != -1:
            splitPoint = avatarUrl.index('jpg')
        avatarUrl = avatarUrl[:splitPoint + 3]
        # print(avatarUrl)
        name = ele.find('div', class_='collection-avatar__title').string
        # heroAvatarMap[name] = avatarUrl
        downloadList.append(' '.join([name, avatarUrl, dataUrl]))

    imgBasePath = './avatars/'
    dataBasePath = './heros/'

    for l in downloadList:
        (name, avatar, data) = l.split(' ')
        imgPath = imgBasePath + name + avatar[-4:]
        dataPath = dataBasePath + name + '.html'
        # downloadImg(avatar, imgPath, imgBasePath)
        downloadData(data, dataPath, dataBasePath)
        sleep(3)
