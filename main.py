import pygame
from player import Player
from database import Database
from settings import WIDTH, HEIGHT, WHITE, FPS

# Инициализация pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Шрифт
font = pygame.font.Font(None, 36)

# ФПС
clock = pygame.time.Clock()

# Подключение к базе данных
db = Database("game_scores.db")

# Создание игрока
player = Player("Player1")

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление экрана
    screen.fill(WHITE)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

# Закрытие базы данных и завершение Pygame
db.close()
pygame.quit()
