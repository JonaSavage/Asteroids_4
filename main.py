# Disable "Hello from the pygame community" message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Run main.py: uv run main.py

import pygame
from constants import *

def main():
    print("Starting Asteroids...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen Height: {SCREEN_HEIGHT}")
    print()


if __name__ == "__main__":
    main()
