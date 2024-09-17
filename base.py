import base64

with open('a.ico', 'rb') as file:
    icon_base64 = base64.b64encode(file.read()).decode('utf-8')

with open('icon_base64.txt', 'w') as file:
    file.write(icon_base64)