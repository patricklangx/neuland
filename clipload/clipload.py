#!/usr/bin/env python
# coding: utf8

import sys
import pyperclip
import random
import string
import argparse

def main(length: int):
    try:
        chars = int(length)
        rand_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=chars))
        pyperclip.copy(rand_string)
    except ValueError as e:
        sys.exit("[ERROR] The passed length argument is not a valid integer.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=int, help='Character length of the payload to be generated.')  
    args = parser.parse_args()
    
    main(args.l)

