with open("code.txt", "w", encoding="utf-8") as f:
    f.write("200\n")
    f.write("201\n")
    f.write("404\n")
    f.write("500\n")
print("写入完成")

def check_status(code):
    if 200 <= code <300:
        return "pass"
    return "fail"

with open ("code.txt","r", encoding="utf-8") as f:
    for line in f:
        print("原始行:", repr(line))
        code = int(line.strip())
        print("转成数字:",code, "->", check_status(code))
