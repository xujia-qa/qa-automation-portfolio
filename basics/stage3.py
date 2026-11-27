def check_status(code):
    if 200 <= code <300:
        return "pass"
    return "fail"


print(check_status(200))
print(check_status(404))
print(check_status(500))
