import pygame

pygame.init()

dis = pygame.display.set_mode((800,600))  # Размер окна
pygame.display.set_caption('Змейка')  # Заголовок

game_over = False  # Переменная, контролирующая статус игры.
# Пока False - игра продолжается.
x1 = 300 # Начальное положение змейки
y1 = 300
x1_change = 0  # Переменная, фиксирующая изменение положения змейки
y1_change = 0
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        # print(event)  Выводит все происходящие события в терминал
        if event.type == pygame.QUIT:  # Выход из игры при нажатии кнопки выхода
            game_over = True
        if event.type == pygame.KEYDOWN:  # Считывание направления движения
            # с клавиатуры
            if event.key == pygame.K_LEFT:  # Изменение положения змейки
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
    dis.fill('black')

    pygame.draw.rect(dis, 'blue', [x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()