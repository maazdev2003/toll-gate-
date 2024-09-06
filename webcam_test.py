import pygame # type: ignore
import pygame.mixer # type: ignore
import sys
import math
import time
import random

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CAR_WIDTH, CAR_HEIGHT = 200, 100
CAR_SPEED = 3
SIGNAL_WIDTH, SIGNAL_HEIGHT = 30, 90
MAX_RAIN_DROPS = 100
MAX_SNOWFLAKES = 100

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Toll Collecting System')

# Load background image
try:
    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Error loading background image: {e}")
    background_image = None

# Load car image with error handling
try:
    car_image = pygame.image.load('car.png')
    car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))
except pygame.error as e:
    print(f"Error loading car image: {e}")
    car_image = None

# Load car engine sound effect
try:
    car_engine_sound = pygame.mixer.Sound('car_engine.wav')
except pygame.error as e:
    print(f"Error loading car engine sound: {e}")
    car_engine_sound = None

# Barrier properties
barrier_closed = True
barrier_length = 230
barrier_angle = 0
barrier_rotation_speed = 2
barrier_pivot = (WIDTH // 2 - 60, HEIGHT - 300)

# Traffic signal properties
signal_x = WIDTH // 2 - SIGNAL_WIDTH // 2 - 80
signal_y = HEIGHT - 330
signal_rect = pygame.Rect(signal_x, signal_y, SIGNAL_WIDTH, SIGNAL_HEIGHT)

# Car properties
car_rect = pygame.Rect(WIDTH // 2 - CAR_WIDTH // 2, HEIGHT - 150, CAR_WIDTH, CAR_HEIGHT)

# Font for displaying text
font = pygame.font.SysFont(None, 36)

# Initial toll amount
toll_amount = 0

# Car count
car_count = 0

# Raindrop properties
raindrops = []
for _ in range(MAX_RAIN_DROPS):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, 0)
    speed = random.randint(5, 15)
    raindrops.append([x, y, speed])

# Snowflake properties
snowflakes = []
for _ in range(MAX_SNOWFLAKES):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, 0)
    speed = random.randint(1, 5)
    snowflakes.append([x, y, speed])

# Weather type
weather = "rain"  # Default weather is rain

# Play toll collection sound
def play_toll_collection_sound():
    if car_engine_sound:
        car_engine_sound.play()

def draw_barrier():
    # Draw the barrier
    barrier_end = (
        barrier_pivot[0] + barrier_length * math.cos(math.radians(barrier_angle)),
        barrier_pivot[1] - barrier_length * math.sin(math.radians(barrier_angle))
    )
    pygame.draw.line(window, BLACK, barrier_pivot, barrier_end, 5)

def draw_traffic_signal():
    pygame.draw.rect(window, BLACK, signal_rect)
    red_light = pygame.Rect(signal_x + 5, signal_y + 5, SIGNAL_WIDTH - 10, 20)
    pygame.draw.rect(window, RED if barrier_closed else BLACK, red_light)
    green_light = pygame.Rect(signal_x + 5, signal_y + 65, SIGNAL_WIDTH - 10, 20)
    pygame.draw.rect(window, GREEN if not barrier_closed else BLACK, green_light)

def draw_car():
    if car_image:
        window.blit(car_image, car_rect.topleft)
    else:
        pygame.draw.rect(window, RED, car_rect)

def display_toll_amount():
    toll_text = font.render(f'Toll Collected: ${toll_amount}', True, BLACK)
    window.blit(toll_text, (10, 10))

def display_car_count():
    car_count_text = font.render(f'Cars Entered: {car_count}', True, BLACK)
    window.blit(car_count_text, (10, 50))

def draw_rain():
    for raindrop in raindrops:
        pygame.draw.line(window, BLACK, (raindrop[0], raindrop[1]), (raindrop[0], raindrop[1] + 5), 2)

def draw_snow():
    for snowflake in snowflakes:
        pygame.draw.circle(window, WHITE, (snowflake[0], snowflake[1]), 3)

def move_rain():
    for raindrop in raindrops:
        raindrop[1] += raindrop[2]
        if raindrop[1] > HEIGHT:
            raindrop[1] = 0
            raindrop[0] = random.randint(0, WIDTH)

def move_snow():
    for snowflake in snowflakes:
        snowflake[1] += snowflake[2]
        if snowflake[1] > HEIGHT:
            snowflake[1] = 0
            snowflake[0] = random.randint(0, WIDTH)

def animate_barrier():
    global barrier_angle
    if barrier_closed:
        if barrier_angle > 0:
            barrier_angle -= barrier_rotation_speed
    else:
        if barrier_angle < 90:
            barrier_angle += barrier_rotation_speed

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Check if car is moving
    car_moving = any(keys[key] for key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])
    
    if car_moving and not barrier_closed:
        if keys[pygame.K_LEFT] and car_rect.left > 0:
            car_rect.x -= CAR_SPEED
        if keys[pygame.K_RIGHT] and car_rect.right < WIDTH:
            car_rect.x += CAR_SPEED
        if keys[pygame.K_UP] and car_rect.top > 0:
            car_rect.y -= CAR_SPEED
        if keys[pygame.K_DOWN] and car_rect.bottom < HEIGHT:
            car_rect.y += CAR_SPEED

        if car_engine_sound and not pygame.mixer.get_busy():
            car_engine_sound.play()
    else:
        if car_engine_sound:
            car_engine_sound.stop()

    # Control the barrier manually
    if keys[pygame.K_c]:
        barrier_closed = True
    if keys[pygame.K_o]:
        barrier_closed = False

    # Control the weather
    if keys[pygame.K_1]:
        weather = "rain"
    if keys[pygame.K_2]:
        weather = "snow"

    # Animate the barrier
    animate_barrier()

    # Check if car reached the toll gate and barrier is open
    if car_rect.colliderect(pygame.Rect(WIDTH // 2 - 75, HEIGHT - 360, 150, 30)) and not barrier_closed and barrier_angle == 90:
        toll_amount += 10  # Collect toll
        car_count += 1  # Increment car count
        play_toll_collection_sound()  # Play toll collection sound
        barrier_closed = True  # Close the barrier
        car_rect.y = HEIGHT - 150  # Reset car position

    # Fill the background
    if background_image:
        window.blit(background_image, (0, 0))
    else:
        window.fill(WHITE)

    # Draw elements
    draw_barrier()
    draw_traffic_signal()
    draw_car()
    
    # Draw weather
    if weather == "rain":
        draw_rain()
        move_rain()
    elif weather == "snow":
        draw_snow()
        move_snow()
    
    # Display toll amount and car count
    display_toll_amount()
    display_car_count()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
