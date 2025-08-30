#!/usr/bin/env python
# coding: utf8

from typing import Any
import ctypes
import platform

# Windows support
if platform.system() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7) # Windows console mode for input handle

# Foreground colors
def reset(text: Any) -> str:
    return f"\033[0m{text}\033[0m"

def black(text: Any) -> str:
    return f"\033[30m{text}\033[0m"

def red(text: Any) -> str:
    return f"\033[31m{text}\033[0m"

def green(text: Any) -> str:
    return f"\033[32m{text}\033[0m"

def yellow(text: Any) -> str:
    return f"\033[33m{text}\033[0m"

def blue(text: Any) -> str:
    return f"\033[34m{text}\033[0m"

def magenta(text: Any) -> str:
    return f"\033[35m{text}\033[0m"

def cyan(text: Any) -> str:
    return f"\033[36m{text}\033[0m"

def white(text: Any) -> str:
    return f"\033[37m{text}\033[0m"

def bright_black(text: Any) -> str:
    return f"\033[90m{text}\033[0m"

def bright_red(text: Any) -> str:
    return f"\033[91m{text}\033[0m"

def bright_green(text: Any) -> str:
    return f"\033[92m{text}\033[0m"

def bright_yellow(text: Any) -> str:
    return f"\033[93m{text}\033[0m"

def bright_blue(text: Any) -> str:
    return f"\033[94m{text}\033[0m"

def bright_magenta(text: Any) -> str:
    return f"\033[95m{text}\033[0m"

def bright_cyan(text: Any) -> str:
    return f"\033[96m{text}\033[0m"

def bright_white(text: Any) -> str:
    return f"\033[97m{text}\033[0m"

# Background colors
def bg_black(text: Any) -> str:
    return f"\033[40m{text}\033[0m"

def bg_red(text: Any) -> str:
    return f"\033[41m{text}\033[0m"

def bg_green(text: Any) -> str:
    return f"\033[42m{text}\033[0m"

def bg_yellow(text: Any) -> str:
    return f"\033[43m{text}\033[0m"

def bg_blue(text: Any) -> str:
    return f"\033[44m{text}\033[0m"

def bg_magenta(text: Any) -> str:
    return f"\033[45m{text}\033[0m"

def bg_cyan(text: Any) -> str:
    return f"\033[46m{text}\033[0m"

def bg_white(text: Any) -> str:
    return f"\033[47m{text}\033[0m"

def bg_bright_black(text: Any) -> str:
    return f"\033[100m{text}\033[0m"

def bg_bright_red(text: Any) -> str:
    return f"\033[101m{text}\033[0m"

def bg_bright_green(text: Any) -> str:
    return f"\033[102m{text}\033[0m"

def bg_bright_yellow(text: Any) -> str:
    return f"\033[103m{text}\033[0m"

def bg_bright_blue(text: Any) -> str:
    return f"\033[104m{text}\033[0m"

def bg_bright_magenta(text: Any) -> str:
    return f"\033[105m{text}\033[0m"

def bg_bright_cyan(text: Any) -> str:
    return f"\033[106m{text}\033[0m"

def bg_bright_white(text: Any) -> str:
    return f"\033[107m{text}\033[0m"

# Text styles
def bold(text: Any) -> str:
    return f"\033[1m{text}\033[0m"

def dim(text: Any) -> str:
    return f"\033[2m{text}\033[0m"

def italic(text: Any) -> str:
    return f"\033[3m{text}\033[0m"

def underline(text: Any) -> str:
    return f"\033[4m{text}\033[0m"

def blink(text: Any) -> str:
    return f"\033[5m{text}\033[0m"

def reverse(text: Any) -> str:
    return f"\033[7m{text}\033[0m"

def hidden(text: Any) -> str:
    return f"\033[8m{text}\033[0m"

def strike(text: Any) -> str:
    return f"\033[9m{text}\033[0m"

# Other
def tab(text: Any, n: int = 1) -> str:
    return '\t' * n + str(text)

def newline(text: Any, n: int = 1) -> str:
    return '\n' * n + str(text)

def c_return(text: Any) -> str:
    return f"\r{text}"
