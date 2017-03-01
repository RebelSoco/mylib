# Easy color printing to console


from __future__ import print_function
import platform


if platform.system() == "Windows":
    from colorama import Fore, Style, init
    init()
else:
    from colorama import Fore, Style


def blue(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.BLUE + Style.BRIGHT + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.BLUE + Style.BRIGHT + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.BLUE + Style.BRIGHT + string + Style.RESET_ALL)


def darkblue(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.BLUE + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.BLUE + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.BLUE + string + Style.RESET_ALL)


def cyan(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.CYAN + Style.BRIGHT + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.CYAN + Style.BRIGHT + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.CYAN + Style.BRIGHT + string + Style.RESET_ALL)


def darkcyan(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.CYAN + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.CYAN + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.CYAN + string + Style.RESET_ALL)


def green(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.GREEN + Style.BRIGHT + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.GREEN + Style.BRIGHT + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.GREEN + Style.BRIGHT + string + Style.RESET_ALL)


def darkgreen(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.GREEN + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.GREEN + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.GREEN + string + Style.RESET_ALL)


def magenta(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.MAGENTA + Style.BRIGHT + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.MAGENTA + Style.BRIGHT + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.MAGENTA + Style.BRIGHT + string + Style.RESET_ALL)


def purple(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.MAGENTA + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.MAGENTA + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.MAGENTA + string + Style.RESET_ALL)


def red(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.RED + Style.BRIGHT + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.RED + Style.BRIGHT + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.RED + Style.BRIGHT + string + Style.RESET_ALL)


def darkred(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.RED + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.RED + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.RED + string + Style.RESET_ALL)


def yellow(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.YELLOW + Style.BRIGHT + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.YELLOW + Style.BRIGHT + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.YELLOW + Style.BRIGHT + string + Style.RESET_ALL)


def orange(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.YELLOW + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.YELLOW + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.YELLOW + string + Style.RESET_ALL)


def white(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.WHITE + Style.BRIGHT + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.WHITE + Style.BRIGHT + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.WHITE + Style.BRIGHT + string + Style.RESET_ALL)


def gray(*args, **kwargs):
    string = ''.join(args)
    if kwargs:
        for key, value in kwargs.items():
            if key == 'end':
                print(Fore.WHITE + Style.DIM + string + Style.RESET_ALL, end=value)
            elif key == 'sep':
                print('sep is broken')
                print(Fore.WHITE + Style.DIM + string + Style.RESET_ALL, sep=value)       
    else:
        print(Fore.WHITE + Style.DIM + string + Style.RESET_ALL)