#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

def confirm():
    inputagain = True
    while inputagain is True:
        print("\nProceed (y/n):")
        sys.path.append(str(__projectdir__ / Path('submodules/py-getch/getch')))
        from getch import getch
        inputted = getch()
        if inputted == "y":
            inputagain = False
        elif inputted == 'n':
            sys.exit(1)
        else:
            inputagain = True
            print('Input one of the available letters.')
