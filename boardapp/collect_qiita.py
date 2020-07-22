import http.client
import json
from .models import Qiita

def collect_qiita():
    conn = http.client.HTTPSConnection("qiita.com", 443)
    conn.request("GET", "/api/v2/tags?page=1&per_page=20&sort=count")
    res = conn.getresponse()
    print(res.status, res.reason)
    data = res.read().decode("utf-8")
    # 文字列からJSON オブジェクトへでコード
    jsonstr = json.loads(data)
    conn.close()
    #上位１０位まで格納
    qiita_db = Qiita.objects.all()
    qiita_db.delete()
    for num in range(10):
        Qiita.objects.create(
        followers_count = jsonstr[num]['followers_count'],
        icon_url = jsonstr[num]['icon_url'],
        items = jsonstr[num]['id'],
        items_count = jsonstr[num]['items_count']
        )