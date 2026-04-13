import os

# كود يشغل سيرفر "تخفي" بورت 8443
config = '{"inbounds":[{"port":8443,"protocol":"vmess","settings":{"clients":[{"id":"88888888-8888-8888-8888-888888888888"}]},"streamSettings":{"network":"ws"}}],"outbounds":[{"protocol":"freedom"}]}'
with open("config.json", "w") as f: f.write(config)

os.system("curl -L https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip -o v.zip && unzip v.zip")
print("🚀 CLOAK SERVER READY")
os.system("./v2ray run -c config.json")
