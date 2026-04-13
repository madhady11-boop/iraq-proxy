import os
import time

# 1. تحميل المحرك وتجهيزه
print("📥 Downloading Engine...")
os.system("curl -L https://github.com/v2fly/v2ray-core/releases/latest/download/v2ray-linux-64.zip -o v2ray.zip && unzip -o v2ray.zip")

# 2. كتابة الإعدادات مع مسار واضح
print("📝 Writing Config...")
config = """
{
  "inbounds": [{
    "port": 8443,
    "protocol": "vmess",
    "settings": {"clients": [{"id": "88888888-8888-8888-8888-888888888888"}]},
    "streamSettings": {"network": "ws", "wsSettings": {"path": "/ahmed"}}
  }],
  "outbounds": [{"protocol": "freedom"}]
}
"""
with open("config.json", "w") as f:
    f.write(config)

# 3. تشغيل السيرفر
print("🚀 Server is Starting...")
os.system("./v2ray run -c config.json")
