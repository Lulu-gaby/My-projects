import pygame
import random


pygame.init()

windows_size = (700, 500)
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption("Игра змейка")

cell_size = 15
fps = 10

speed = 5

# Цвета
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

class Snake:
    def __init__(self):
        self.body = [(5 * cell_size,5 * cell_size)]
        self.direction = (cell_size, 0)
        self.growing = False


    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if new_head[0] < 0 or new_head[0] >= windows_size[0] or new_head[1] < 0 or new_head[1] >= windows_size[1]:
            return True

        if not self.growing:
            self.body.pop()

        self.body.insert(0, new_head)
        self.growing = False

    def grow(self):
        self.growing = True

    def self_bump(self):
        head = self.body[0]
        return head in self.body[1:] or head in [obs.position for obs in obstacles]

    def set_direction(self, new_direction):
        self.direction = new_direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, green, pygame.Rect(segment[0], segment[1], cell_size, cell_size))

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return (random.randint(0, (windows_size[0] // cell_size) - 1) * cell_size,
                random.randint(0, (windows_size[1] // cell_size) - 1) * cell_size)

    def draw(self):
        pygame.draw.rect(screen, yellow, pygame.Rect(self.position[0], self.position[1], cell_size, cell_size))

class Obstacles:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return (random.randint(0, (windows_size[0] // cell_size) - 1) * cell_size,
                random.randint(0, (windows_size[1] // cell_size) - 1) * cell_size)

    def draw(self):
        pygame.draw.rect(screen, red, pygame.Rect(self.position[0], self.position[1], cell_size, cell_size))

def game_loop():
    snake = Snake()
    food = Food()
    obstacles = [Obstacles() for _ in range(5)]
    clock = pygame.time.Clock()
    run = True

    while run:
        screen.fill((34, 22, 46))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != (cell_size, 0):
                    snake.set_direction((-cell_size, 0))
                elif event.key == pygame.K_RIGHT and snake.direction != (-cell_size, 0):
                    snake.set_direction((cell_size, 0))
                elif event.key == pygame.K_UP and snake.direction != (0, cell_size):
                    snake.set_direction((0, -cell_size))
                elif event.key == pygame.K_DOWN and snake.direction != (0, -cell_size):
                    snake.set_direction((0, cell_size))

        if snake.move():  # Если змея выходит за пределы экрана
            print("Game Over!")
            run = False


        # Проверка столкновений
        if snake.self_bump(obstacles):
            run = False

        # Проверка на съедание еды
        if snake.body[0] == food.position:
            snake.grow()
            food = Food()


        snake.draw()
        food.draw()
        for obstacle in obstacles:
            obstacle.draw()

        pygame.display.flip()
        clock.tick(fps)

    game_loop()
    pygame.quit()
