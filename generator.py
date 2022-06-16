import random
import string

num = int(input("何個作成しますか"))

for i in range(num):
    url="https://discord.gift/"
    code = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(16)))
    print(url + code)
