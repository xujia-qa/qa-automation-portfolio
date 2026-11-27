import requests

# ① GET：参数放 URL
r1 = requests.get("https://httpbin.org/get", params={"name": "xujia", "age": 20}, timeout=10)
print("GET 方法:", r1.json()["method"])
print("GET 参数:", r1.json()["args"])

# ② POST：参数放 body
r2 = requests.post("https://httpbin.org/post", json={"name": "xujia", "age": 20}, timeout=10)
print("POST 方法:", r2.json()["method"])
print("POST 参数:", r2.json()["json"])

#取返回值的固定套路：
#python
#r.json()["某个键"]
#r.json() 把文本变字典，["键"] 取值——以后所有接口测试都是这个动作。

#1.为什么 GET 那段取的是 ["args"]，POST 取的是 ["json"]？
#答案:
#服务器把“URL 参数”和“body 参数”分开放，httpbin 用 args 和 json 两个键区分。
#2.为什么 GET 的 20 变成了 '20'，POST 的没变？
#答案:
#URL 只能是文本，数字拼进去就成字符串；JSON 支持数字类型，能原样保留。