raw = "tm{jdw,g,{@GPM@q/@w,G/M,{b"

for i in range(128):
    flag = ""
    for c in raw:
        flag += chr(ord(c) ^ i)

    if "krdu" in flag:
        print(flag)
        break
