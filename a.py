import os
ADDLESS = os.environ['token']
print("アドレス:", ADDLESS)

if os.environ["test"]:
    print("あ")
else:
    print("い")