import pygame
import random
import sys

def start_screen(screen):
  WIDTH, HEIGHT = 800, 600
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  FONT_SIZE = 30

  FONT = pygame.font.Font("NONE", FONT_SIZE)

  SCREEN.fill(BLACK)

  intro_text [
    "Welcome to the game!",
    "You will be playing as a spaceship",
    "-----------------------------------",
    "Use the arrow keys to move",
    "Press SPACE to shoot",
    "Press ESC to quit",
    "-----------------------------------",
    "Press any key to start"
  ]