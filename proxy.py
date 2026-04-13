import os

# تحميل أداة MTProxy الاحترافية
print("📥 Installing MTProxy...")
os.system("curl -L https://github.com/9seconds/mtg/releases/latest/download/mtg-2.1.7-linux-amd64.tar.gz -o mtg.tar.gz && tar -xvf mtg.tar.gz")

# تشغيل البروكسي (بورت 8443 مع سر سري)
print("🚀 MTProto is Starting...")
# السر هو: ee00000000000000000000000000000000676f6f676c652e636f6d
os.system("./mtg-2.1.7-linux-amd64/mtg run ee00000000000000000000000000000000676f6f676c652e636f6d -b 0.0.0.0:8443")
