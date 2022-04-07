import requests
import time

api_key = "qUOm0nOReG0fjos1WfGUUpJuucktj9"

off = f"https://iotdomu.cz/api/device/624aad2bff79ba00130591e2/thing/segment0?property=power&value=false"
on = f"https://iotdomu.cz/api/device/624aad2bff79ba00130591e2/thing/segment0?property=power&value=true"

blue = "63,81,181"
green = "76,175,80"


def send_action(action: str):
    return requests.post(
        f"{action}&api_key={api_key}")

def change_color(color: str):
    action = f"https://iotdomu.cz/api/device/624aad2bff79ba00130591e2/thing/segment0?property=color&value={color}"

    return send_action(action)

r = send_action(on)
print("status code: ",r.status_code)
print("response obj:",r)

time.sleep(4)
r = send_action(off)
time.sleep(4)

change_color(blue)
time.sleep(4)
change_color(green)
