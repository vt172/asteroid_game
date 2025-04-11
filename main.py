import pygame
from constants import *
from player import *

def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

	while True:

		screen.fill("black")

		player.draw(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		pygame.display.flip()

		clock.tick(60)
		dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()