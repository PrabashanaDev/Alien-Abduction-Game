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

  y_position = HEIGHT // 4
  for line in intro_text:
    text = FONT.render(line, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, y_position))
    screen.blit(text, text_rect)
    y_position += FONT_SIZE 

  pygame.display.flip()

  wait_for_key()

def wait_for_key():
  waiting = True
  while waiting:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        waiting == False

def show_text_on_screen(screen, text, font_size, y_position):
  font = pygame.font.Font(None, font_size)
  text_render = font.render(text, True, (255, 255, 255))
  text_rect = text_render.get_rect(center=(WIDTH // 2, y_position))
  screen.blit(text_render, text_rect)

def game_over_screen(screen):
  screen.fill((0, 0, 0))
  show_text_on_screen(screen, "Game Over", 50, HEIGHT // 3)
  show_text_on_screen(screen, f"Your final score: {score}", 30, HEIGHT // 2)
  show_text_on_screen(screen, "Press any key to exit...", 20, HEIGHT * 2 // 3)
  pygame.display.flip()
  wait_for_key()

def victory_screen(screen):
  screen.fill((0, 0, 0))
  show_text_on_screen(screen, "Congratulations!", 50, HEIGHT // 3)
  show_text_on_screen(screen, f"You've completed all levels with a score of {score}", 30, HEIGHT // 2)
  show_text_on_screen(screen, "Press any key to exit...", 20, HEIGHT * 2 // 3)
  pygame.display.flip()
  wait_for_key()
                      
ovni = pygame.image.load("ovni.png")
cow = pygame.image.load("cow.png")

ovni = pygame.transform.scale(ovni, (50, 50))
cow = pygame.transform.scale(cow, (40, 40))

pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
SHIP_GREEN = (0, 255, 0)
GRASS_GREEN  = (0, 100, 0)
STAR_COUNT = int(WIDTH * HEIGHT * 0.001)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
player_rect = pygame.Rect(WIDTH // 2 - 25, 10, 50, 50)
player_speed = 5

targets = []

score = 0
font = pygame.font.Font(None, 36)
space_pressed = False
stars = [{'x': random.randint(0, WIDTH), 'y': random.randint(0, HEIGHT), 'size': random.randint(1, 3), 'color': LIGHT_BLUE} for _ in range(STAR_COUNT)]

grass_rect = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)

current_level = 1
abduction_target = 10 
countdown_timer = 60
current_score = 0

target_spawn_counter = 0
TARGET_SPAWN_RATE = max(30, 120 - (current_level * 90))

level_colors = [
  LIGHT_BLUE,
  ORANGE,
  RED,
  YELLOW,
  GRAY,
  (0,255,0),
  (255,0,255),
  (0,255,255),
  (255,165,0),
  (128,0,128),
]


start_screen(screen)

running = True
game_started = False

#while running:
 # for event in pygame.event.get():