import requests
import execjs
import re
import json
from jsonpath_ng.ext import parse
import datetime

# 所有 url
index_url = 'http://x.nuaa.edu.cn/login'
login_url = 'http://x.nuaa.edu.cn/https/77726476706e69737468656265737421f1e2559434357a467b1ac7a28d54227b848842e5509e/authserver/login'
halview_url = 'http://x.nuaa.edu.cn/http/77726476706e69737468656265737421f5ff40902b63265e6b0988e29d51367b068b/v2/reserve/hallView?id=15'
main_url = 'http://x.nuaa.edu.cn/http/77726476706e69737468656265737421f5ff40902b63265e6b0988e29d51367b068b/api/login/main?redirect_url=http%3A%2F%2Fehall3.nuaa.edu.cn%2Fv2%2Freserve%2FhallView%3Fid%3D15'
list_url = 'http://x.nuaa.edu.cn/http/77726476706e69737468656265737421f5ff40902b63265e6b0988e29d51367b068b/site/reservation/list?vpn-12-o1-ehall3.nuaa.edu.cn&hall_id=15&time={}&resource_name='.format(datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z')
reserve_url = 'http://x.nuaa.edu.cn/http/77726476706e69737468656265737421f5ff40902b63265e6b0988e29d51367b068b/site/reservation/launch?vpn-12-o1-ehall3.nuaa.edu.cn'

# 所有 headers
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'x.nuaa.edu.cn',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
login_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'x.nuaa.edu.cn',
    'Origin': 'http://x.nuaa.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://x.nuaa.edu.cn/https/77726476706e69737468656265737421f1e2559434357a467b1ac7a28d54227b848842e5509e/authserver/login?service=http%3A%2F%2Fx.nuaa.edu.cn%2Flogin%3Fcas_login%3Dtrue',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
halview_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'x.nuaa.edu.cn',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36    ',
}
main_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'x.nuaa.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://x.nuaa.edu.cn/http/77726476706e69737468656265737421f5ff40902b63265e6b0988e29d51367b068b/v2/reserve/hallView?id=15',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}
list_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'x.nuaa.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://x.nuaa.edu.cn/http/77726476706e69737468656265737421f5ff40902b63265e6b0988e29d51367b068b/v2/reserve/hallView?id=15',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
reserve_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'x.nuaa.edu.cn',
    'Origin': 'http://x.nuaa.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://x.nuaa.edu.cn/http/77726476706e69737468656265737421f5ff40902b63265e6b0988e29d51367b068b/v2/reserve/reserveDetail?id=20',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# 其它全局变量
session = requests.session()
raw_json=''
user_info = None

def getEncryptedPwd(pwd,key):
    with open('getEncPwd.js',mode='r',encoding='utf-8') as f:
        JScode = f.read()

    ctx = execjs.compile(JScode)
    encPwd = ctx.call('getEncPwd',pwd,key)
    # print(encPwd)
    return encPwd

def login(name,pwd):
    global session
    global raw_json

    response = session.get(headers=headers, url= index_url).text    

    # 获取 execution 值
    execution = re.findall('<input type="hidden" name="execution" value="(.*?)"',response)[0]

    # 获取 pwdEncryptSalt, 也就是AES加密的 key
    key = re.findall('<input type="hidden" id="pwdEncryptSalt" value="(.*?)"',response)[0]

    # 获取加密后的密码
    encPwd = getEncryptedPwd(pwd,key)

    login_formdata = {
        'captcha': '',
        '_eventId': 'submit',
        'cllt': 'userNameLogin',
        'lt':'',
        'username':str(name),
        'password':str(encPwd),
        'execution':execution,
    }
    login_params = {
        'service': 'http://x.nuaa.edu.cn/login?cas_login=true'
    }
    response = session.post(url=login_url, headers=login_headers, params=login_params, data=login_formdata)

    with open('test.html',mode='w',encoding='utf-8') as f:
        f.write(response.text)
    print('login:',response.status_code)

    # 继续访问 halView 页面
    hal_response = session.get(url=halview_url,headers=halview_headers)
    with open('halview.html',mode='w',encoding='utf-8') as f:
        f.write(hal_response.text)
    print('hal:',hal_response.status_code)

    # 继续访问 main 页面，最后会重定位到新的 halview 页面
    main_response = session.get(url=main_url,headers=main_headers)
    with open('main_response.html',mode='w',encoding='utf-8') as f:
        f.write(main_response.text)
    print('main_url:',main_response.status_code)

    # 获取包含体育场馆场地信息的 json 数据
    list_response = session.get(url=list_url,headers=list_headers)
    print('list:',list_response.status_code)

    # 把数据保存到全局变量中
    raw_json = json.loads(list_response.text)
    return raw_json

# 客户端不需要这个 reserve 函数，以后会删除的
def reserve():
    global session

    # 开始从 json 中取值，最后提交预约请求时候需要
    resource_id_json_expr = parse("$..list[?(@.name=='（将军路校区）体育馆羽毛球场')].id")
    resource_id = resource_id_json_expr.find(raw_json)[0].value
    #print(resource_id)

    data_json_expr = parse("$..list[?(@.name=='（将军路校区）体育馆羽毛球场')]..table.*[?(@.abscissa=='1号' & @.yaxis=='08:00-09:00')]")
    data = data_json_expr.find(raw_json)[0].value

    date = data['date']
    period = data['time_id']
    sub_resource_id = data['sub_id']

    reserve_formdata = {
        'resource_id': resource_id, 
        'code': '',
        'remarks': '',
        'deduct_num': '',
        'data': str([{
                        "date":date,
                        "period":period,
                        "sub_resource_id":sub_resource_id
                }]), 
    }

    # 提交预约请求
    reserve_response = session.post(url=reserve_url,headers=reserve_headers,data=reserve_formdata)
    print('reserve:',reserve_response.status_code)

# if __name__ == '__main__':
#     login('031820520','xxx')
#     reserve()

