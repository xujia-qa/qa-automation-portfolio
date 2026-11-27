import json
import requests

# ---------- 1. 打印整棵树，确认类型 ----------
r1 = requests.get("https://httpbin.org/get", timeout=10)
d1 = r1.json()
print("1) 类型:", type(d1))
print("1) 第一层键:", list(d1.keys()))

# ---------- 2. 取第一层字段 ----------
print("2) url:", d1["url"])
print("2) method:", d1["method"])

# ---------- 3. 取两层嵌套 ----------
r2 = requests.get("https://httpbin.org/get", params={"name": "xujia"}, timeout=10)
d2 = r2.json()
print("3) args.name:", d2["args"]["name"])
print("3) headers.User-Agent:", d2["headers"]["User-Agent"])

# ---------- 4. 取数组元素（用 /json，不是 /post） ----------
r3 = requests.get("https://httpbin.org/json", timeout=10)
d3 = r3.json()
print("4) slide 数量:", len(d3["slideshow"]["slides"]))
print("4) 第 0 个 title:", d3["slideshow"]["slides"][0]["title"])

# ---------- 5. POST 参数在 json 键 ----------
r4 = requests.post(
    "https://httpbin.org/post",
    json={"username": "xujia", "age": 20},
    timeout=10,
)
d4 = r4.json()
print("5) POST json:", d4["json"])
print("5) username:", d4["json"]["username"])