from getch import _Getch
getch = _Getch()

while True:
    key_code = ord(getch())
    print(key_code)
    if key_code == 3: #if ctr-c
        break

