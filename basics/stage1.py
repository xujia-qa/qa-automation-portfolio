name = "xujia"
age = 20
height = 1.65
is_student = True
print(type(name),type(age),type(height),type(is_student))
print(f"{name} 今年{age}岁,身高{height}")

codes = [200, 201, 400, 403, 404, 500]
print("第一个:", codes[0], "最后一个:", codes[-1], "长度:", len(codes))
print("切片 1:4 ->", codes[1:4])
codes.append(502)
print("追加后:", codes)

user = {"name": "xujia", "role": "qa", "level": 1}
print(user["name"])
print(user.get("city", "不存在"))
#user["city"] = "shanghai"
print(user)
for k, v in user.items():
    print(k, "=", v)

