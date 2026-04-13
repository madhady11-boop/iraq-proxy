import os

# كود سيرفر VMess احترافي للأيفون
with open("config.json", "w") as f:
    f.write('{"inbounds":[{"port":8443,"protocol":"vmess","settings":{"clients":[{"id":"88888888-8888-8888-8888-888888888888"}]},"streamSettings":{"network":"ws","wsSettings":{"path":"/ahmed"}}}],"outbounds":[{"protocol":"freedom"}]}')

print("🚀 VMess SERVER IS READY FOR IPHONE")
os.system("curl -L https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip -o v2ray.zip && unzip v2ray.zip && ./v2ray run -c config.json")
