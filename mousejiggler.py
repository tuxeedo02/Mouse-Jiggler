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
            duration=0.01
        )
        time.sleep(90)
    
def get_random_coords() -> []:
    """
    Returns a list of coordinates within 10 pixels of the current mouse position.
    """
    current_x, current_y = pyautogui.position()
    
    new_x = current_x + random.randint(-10, 10)
    new_y = current_y + random.randint(-10, 10)
    
    # Ensure the new coordinates are within the screen boundaries
    screen_width, screen_height = pyautogui.size()
    new_x = max(0, min(new_x, screen_width - 1))
    new_y = max(0, min(new_y, screen_height - 1))
    
    return [new_x, new_y]


if __name__ == "__main__":
    print('Press Ctrl-C to quit.')
    try:
        while True:
            #switch_screens()
            wiggle_mouse()
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n")
