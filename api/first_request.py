import requests

url = "https://httpbin.org/get"
resp = requests.get(url, timeout=10)

print("状态码:", resp.status_code)
print("实际 URL:", resp.url)
print(resp.text[:300])