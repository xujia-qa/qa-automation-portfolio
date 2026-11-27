import requests

url = "https://httpbin.org/bearer"

# 第一步：不带 token 发请求
r1 = requests.get(url, timeout=10)
print("不带 Token:", r1.status_code)                 # 空 1

# 第二步：带上 token 发请求
headers = {"Authorization": "Bearer my-token-123"}  # 空 2
r2 = requests.get(url, headers=headers, timeout=10)
print("带 Token:", r2.status_code)
print("服务器认到的 token:", r2.json()["token"])  # 空 3