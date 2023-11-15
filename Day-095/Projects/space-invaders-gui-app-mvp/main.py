import sys
import pygame


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders MVP")


class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 60
        self.speed = 5
        self.image = pygame.Surface((36, 24))
        self.image.fill(GREEN)

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < SCREEN_WIDTH - 36:
            self.x += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.5
        self.image = pygame.Surface((36, 24))
        self.image.fill(RED)

    def move(self):
        self.x += self.speed

    def drop_down(self):
        self.y += 24

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


def main_menu():
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        title_text = font.render("Space Invaders", True, WHITE)
        title_rect = title_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        )
        screen.blit(title_text, title_rect)

        play_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        pygame.draw.rect(screen, GREEN, play_button)

        play_text = font.render("Play", True, WHITE)
        play_rect = play_text.get_rect(center=play_button.center)
        screen.blit(play_text, play_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return


pygame.quit()
