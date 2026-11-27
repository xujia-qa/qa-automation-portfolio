codes = [200, 301, 400, 500]

for code in codes:
    if 200 <= code < 300:
        print(code, "2xx 成功")
    if 300 <= code < 400:
        print(code, "3xx 重定向")
    elif 400 <= code <500:
        print(code, "4xx 客户端错误")
    else:
        print(code, "5xx 服务端错误")
