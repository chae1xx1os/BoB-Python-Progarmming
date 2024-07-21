import pygame
from pygame.locals import *
import random

# Star 클래스 정의
class Star:
    def __init__(self, screen, screenSize, index):
        self.screen = screen
        self.screenSize = screenSize
        self.init_star(index)
    
    def init_star(self, index):
        self.x = random.randint(0, self.screenSize[0])
        self.y = random.randint(0, self.screenSize[1])
        self.speed = random.random() * 2 + 1
        self.size = random.randint(1, 3)
        self.color = (255, 255, 255)
        self.index = index

    def move(self):
        self.y += self.speed
        if self.y > self.screenSize[1]:
            self.y = 0
            self.x = random.randint(0, self.screenSize[0])

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.size)

# Pygame 초기화
pygame.init()

# 화면 설정
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize)

# 스타 생성
stars = [Star(screen, screenSize, i) for i in range(100)]

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))  # 배경 색상 설정

    for star in stars:
        star.move()
        star.draw()

    pygame.display.flip()

pygame.quit()
