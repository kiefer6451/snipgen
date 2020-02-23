from getch import _Getch
getch = _Getch()

while True:
    key_code = ord(getch())
    print(key_code)

