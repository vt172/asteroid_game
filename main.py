import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	asteroidfield = pygame.sprite.Group()

	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = (updatables,)

	asteroid_field = AsteroidField()

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

		dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()