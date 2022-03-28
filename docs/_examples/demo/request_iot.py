import requests
import time


token = "n2z7NYrlDaGBQ832nNt9H4yWoBWZv5"

off = f"https://iotdomu.cz/api/device/61953025b24812001397e845/thing/led?property=power&value=false&api_key={token}"
on = f"https://iotdomu.cz/api/device/61953025b24812001397e845/thing/led?property=power&value=true&api_key={token}"

blue = "f5cf65"
green = "fffc00"


def change_color(hex_color: str):
    requests.post(
        f"https://iotdomu.cz/api/device/61953025b24812001397e845/thing/led?property=color&value=%23{hex_color}&api_key={token}")


r = requests.post(off)
print(r.status_code)
print(r.headers)
print(r.text)
print(r)

time.sleep(4)
r = requests.post(on)
time.sleep(4)

change_color(blue)
time.sleep(4)
change_color(green)
