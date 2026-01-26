import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)

# Bird
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
gravity = 0.5
bird_movement = 0

# Pipes
pipe_width = 60
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(150, 400)
pipe_speed = 3

score = 0

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

def reset_game():
    global bird_y, bird_movement, pipe_x, pipe_height, score
    bird_y = HEIGHT // 2
    bird_movement = 0
    pipe_x = WIDTH
    pipe_height = random.randint(150, 400)
    score = 0

running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -8

    # Bird movement
    bird_movement += gravity
    bird_y += bird_movement

    # Pipe movement
    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(150, 400)
        score += 1

    # Draw bird
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Draw pipes
    top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(
        pipe_x,
        pipe_height + pipe_gap,
        pipe_width,
        HEIGHT
    )

    pygame.draw.rect(screen, GREEN, top_pipe)
    pygame.draw.rect(screen, GREEN, bottom_pipe)

    # Collision
    bird_rect = pygame.Rect(
        bird_x - bird_radius,
        bird_y - bird_radius,
        bird_radius * 2,
        bird_radius * 2
    )

    if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe) or bird_y > HEIGHT or bird_y < 0:
        reset_game()

    # Score
    draw_text(f"Score: {score}", 10, 10)

    pygame.display.update()
    clock.tick(60)
