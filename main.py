# Disable "Hello from the pygame community" message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Run main.py: uv run main.py

import pygame

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("This is to test if I have to use my PAT again.")
    print("One more time.")


if __name__ == "__main__":
    main()
