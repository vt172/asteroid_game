import pygame
from constants import *
from player import *

def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updatables, drawables)

	player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

	while True:

		screen.fill("black")

		for drawable in drawables:
			drawable.draw(screen)
		updatables.update(dt)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.display.flip()

		clock.tick(60)
		dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()