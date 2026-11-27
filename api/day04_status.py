import requests

for code in [999, 201, 301, 400, 401, 403, 404, 500]:
    r = requests.get(f"http://httpbin.org/status/{code}", timeout=10)
    print(code, "->", r.status_code)


import requests

r = requests.get("https://httpbin.org/status/500", timeout=10)

# 空 1：打印状态码
print(r.status_code)

# 空 2：如果状态码是 500，打印"服务端错误"
if r.status_code == 500:
    print("服务端错误")