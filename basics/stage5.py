def check_status(code):
    """2xx 返回 pass, 其余 fail; 非数字返回 invalid"""
    try:
        code = int(code)                 #尝试转成整数，可能失败
    except (TypeError, ValueError):      #转不了（None / "abc"）就接住
        return "inbalid"                 #不崩，返回 invaild

    if 200 <=code <300:
        return "pass"
    return "fail"

cases = [200, "201", 404, "abc", None]
for c in cases:
    print(repr(c), "->", check_status(c))