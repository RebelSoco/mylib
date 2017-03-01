# returns key pressed, used for text menus


from platform import system


if system() == 'Windows':
    from msvcrt import getch
else:
    raise Exception('Windows Only')


def get():
    key = ord(getch())
    return chr(key)