import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sprites/person.png')
        self.rect = pygame.Rect(100, 100, 100, 100)

    def update(self, *args):
        self.image = pygame.transform.scale(self.image, (100, 100))
        pass

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Primeiro jogo lafaum')

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

rodando = True

def draw():
    playerGroup.draw(screen)

def update():
    playerGroup.update()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    update()
    draw()
    pygame.display.update()
