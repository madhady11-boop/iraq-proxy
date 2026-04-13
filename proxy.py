import os

# هذا الكود يثبت ويشغل سيرفر VLESS بسيط
os.system("curl -L https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip -o v2ray.zip && unzip v2ray.zip")
with open("config.json", "w") as f:
    f.write('{"inbounds":[{"port":8443,"protocol":"vless","settings":{"clients":[{"id":"88888888-8888-8888-8888-888888888888"}],"decryption":"none"},"streamSettings":{"network":"ws"}}],"outbounds":[{"protocol":"freedom"}]}')

print("🚀 VLESS SERVER IS READY")
os.system("./v2ray run -c config.json")
