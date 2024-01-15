import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
tile_size = 100
grid_size = 4
grid_margin = 10
window_size = (grid_size * tile_size + (grid_size + 1) * grid_margin, grid_size * tile_size + (grid_size + 1) * grid_margin)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('2048 Game')

# Цвета
colors = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    # добавьте цвета для других значений
}

# Инициализация игрового поля
grid = [[0] * grid_size for _ in range(grid_size)]

def add_tile():
    empty_cells = [(x, y) for x in range(grid_size) for y in range(grid_size) if grid[x][y] == 0]
    if empty_cells:
        x, y = random.choice(empty_cells)
        grid[x][y] = 2 if random.random() < 0.9 else 4

def draw():
    screen.fill((187, 173, 160))
    for x in range(grid_size):
        for y in range(grid_size):
            value = grid[x][y]
            color = colors[value]
            rect = pygame.Rect((grid_margin + y * (tile_size + grid_margin), grid_margin + x * (tile_size + grid_margin)), (tile_size, tile_size))
            pygame.draw.rect(screen, color, rect)
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

    pygame.display.flip()

# Основной игровой цикл
add_tile()
add_tile()
draw()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Обработка движения вверх
                pass
            elif event.key == pygame.K_DOWN:
                # Обработка движения вниз
                pass
            elif event.key == pygame.K_LEFT:
                # Обработка движения влево
                pass
            elif event.key == pygame.K_RIGHT:
                # Обработка движения вправо
                pass

    # Обновление отображения после каждого действия
    draw()

pygame.quit() 
