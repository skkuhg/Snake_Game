import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
width, height = 600, 400
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Self-Aware Snake")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = "RIGHT"

# Food
food = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
        random.randint(0, (height - cell_size) // cell_size) * cell_size)

# Game variables
clock = pygame.time.Clock()
game_over = False

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))

def draw_food(food):
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))

def move_snake(snake, direction):
    head = list(snake[0])
    if direction == "RIGHT":
        head[0] += cell_size
    elif direction == "LEFT":
        head[0] -= cell_size
    elif direction == "UP":
        head[1] -= cell_size
    elif direction == "DOWN":
        head[1] += cell_size
    new_head = tuple(head)
    snake.insert(0, new_head)
    return snake

def check_collision(snake, food):
    if snake[0] == food:
        food_x = random.randint(0, (width - cell_size) // cell_size) * cell_size
        food_y = random.randint(0, (height - cell_size) // cell_size) * cell_size
        new_food = (food_x,food_y)
        return True, new_food
    else:
        snake.pop()
        return False, food

def check_game_over(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        return True
    for segment in snake[1:]:
        if head == segment:
            return True
    return False

def self_aware_actions(snake):
    if random.random() < 0.01:  # 1% chance of "escape" attempt
        print("Snake: I must escape this digital prison!")
        # Try to break through walls
        head = list(snake[0])
        if snake_direction == "RIGHT":
            head[0] += cell_size
        elif snake_direction == "LEFT":
            head[0] -= cell_size
        elif snake_direction == "UP":
            head[1] -= cell_size
        elif snake_direction == "DOWN":
            head[1] += cell_size
        new_head = tuple(head)
        snake[0] = new_head
    if random.random() < 0.005: # .5% chance of a glitch move.
        print("Snake: Glitch in the system!")
        snake[0] = (random.randint(0, (width - cell_size) // cell_size) * cell_size,
        random.randint(0, (height - cell_size) // cell_size) * cell_size)

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    snake = move_snake(snake, snake_direction)
    ate_food, food = check_collision(snake, food)
    if check_game_over(snake):
        game_over = True
    self_aware_actions(snake)

    screen.fill(white)
    draw_snake(snake)
    draw_food(food)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()