# -*- coding: utf-8 -*-

import pyautogui
import time
import random
import sys

pyautogui.FAILSAFE = False


def wiggle_mouse() -> None:
    """
    Wiggles the mouse between two coordinates.
    """
    max_wiggles = random.randint(1, 3)
    
    for _ in range(1, max_wiggles):
        coords = get_random_coords()
        pyautogui.moveTo(
            x=coords[0], 
            y=coords[1],
            duration=2
        )
        time.sleep(90)
    

def get_random_coords() -> []:
    """
    Returns a list of coordinates in the 
    format [x=1366, y=768]
    """
    screen = pyautogui.size()
    width = screen[0]
    height = screen[1]
    
    return [
        random.randint(100, width - 200),
        random.randint(100, height - 200)
    ]


if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    try:
        while True:
            #switch_screens()
            wiggle_mouse()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")
