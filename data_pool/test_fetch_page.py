import http.client

baseUrl = 'bbs.mihoyo.com'

allMap = '/ys/obc/channel/map'
hero = '/189'

conn = http.client.HTTPSConnection(baseUrl, timeout=10)

conn.connect()
conn.request('GET', allMap + hero)
resp = conn.getresponse()
if resp.status == 302:
    resp.read()
    headers = resp.getheaders()
    redirectUrl = ''
    for k, v in headers:
        if k == 'Location':
            redirectUrl = v
            break
    conn.request('GET', redirectUrl)
    resp = conn.getresponse()
    print(resp.status, resp.reason)
    data = resp.read()
    with open('./pages', 'w') as f:
        f.write(bytes.decode(data))
else:
    print(resp.status, resp.reason)
    data = resp.read()
    print(data)
conn.close()
