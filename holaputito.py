import pygame
import random

pygame.init()

# Definir constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
WHITE = (255, 255, 255)

# Inicializar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Definir las formas de las piezas de Tetris
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1],
     [0, 1, 0]],      # T
    [[1, 1, 1],
     [1, 0, 0]],      # L
    [[1, 1, 1],
     [0, 0, 1]],      # J
    [[1, 1],
     [1, 1]],         # O
    [[1, 1, 0],
     [0, 1, 1]],      # S
    [[0, 1, 1],
     [1, 1, 0]]       # Z
]

# Inicializar variables
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 0.5
current_piece = None
x, y = 5, 0

# Función para generar una nueva pieza
def new_piece():
    global current_piece, x, y
    shape = random.choice(SHAPES)
    current_piece = {'shape': shape, 'rotation': 0, 'x': x, 'y': y}

# Función para dibujar la cuadrícula
def draw_grid():
    for i in range(0, SCREEN_WIDTH, 30):
        pygame.draw.line(screen, WHITE, (i, 0), (i, SCREEN_HEIGHT))
    for j in range(0, SCREEN_HEIGHT, 30):
        pygame.draw.line(screen, WHITE, (0, j), (SCREEN_WIDTH, j))

# Función principal del juego
def main():
    global fall_time
    new_piece()

    while True:
        for event in pygame.event.get():print("Hola numdo")
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # Mover la pieza hacia la izquierda
        if keys[pygame.K_LEFT]:
            current_piece['x'] -= 1
            if current_piece['x'] < 0:
                current_piece['x'] = 0
            if check_collision():
                current_piece['x'] += 1

        # Mover la pieza hacia la derecha
        if keys[pygame.K_RIGHT]:
            current_piece['x'] += 1
            if current_piece['x'] > 9 - len(current_piece['shape'][0]):
                current_piece['x'] = 9 - len(current_piece['shape'][0])
            if check_collision():
                current_piece['x'] -= 1

        # Rotar la pieza
        if keys[pygame.K_UP]:
            current_piece['rotation'] = (current_piece['rotation'] + 1) % len(current_piece['shape'])
            if check_collision():
                current_piece['rotation'] = (current_piece['rotation'] - 1) % len(current_piece['shape'])

        # Hacer que la pieza caiga hacia abajo
        fall_time += clock.get_rawtime()
        if fall_time > fall_speed * 1000:
            current_piece['y'] += 1
            if current_piece['y'] > 19 - len(current_piece['shape']):
                current_piece['y'] = 19 - len(current_piece['shape'])
            if check_collision():
                current_piece['y'] -= 1
                merge_piece()
                new_piece()
            fall_time = 0

        # Dibujar en la pantalla
        screen.fill((0, 0, 0))
        draw_grid()
        draw_piece()
        pygame.display.update()
        clock.tick(30)

# Función para verificar colisiones con la cuadrícula y las piezas existentes
def check_collision():
    for y, row in enumerate(current_piece['shape'][current_piece['rotation']]):
        for x, cell in enumerate(row):
            if cell:
                if x + current_piece['x'] < 0 or x + current_piece['x'] > 9 or y + current_piece['y'] > 19:
                    return True
                if grid[y + current_piece['y']][x + current_piece['x']]:
                    return True
    return False

# Función para unir la pieza a la cuadrícula cuando se detiene
def merge_piece():
    for y, row in enumerate(current_piece['shape'][current_piece['rotation']]):
        for x, cell in enumerate(row):
            if cell:
                grid[y + current_piece['y']][x + current_piece['x']] = 1

# Función para dibujar la pieza en la pantalla
def draw_piece():
    shape_to_draw = current_piece['shape'][current_piece['rotation']]
    for y, row in enumerate(shape_to_draw):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, WHITE, (current_piece['x'] * 30 + x * 30, current_piece['y'] * 30 + y * 30, 30, 30))

# Inicializar la cuadrícula
grid = [[0 for _ in range(10)] for _ in range(20)]

if __name__ == '__main__':
    main()

