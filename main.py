import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	asteroidfield = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = (updatables,)
	Bullet.containers = (bullets,updatables,drawables)

	asteroid_field = AsteroidField()

	player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

	while True:

		screen.fill("black")

		updatables.update(dt)

		for asteroid in asteroids:
			if player.is_colliding(asteroid):
				print("Game over!")
				sys.exit()
			for bullet in bullets:
				if bullet.is_colliding(asteroid):
					bullet.kill()
					asteroid.split()
			else:
				pass

		for drawable in drawables:
			drawable.draw(screen)
		



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		pygame.display.flip()

		dt = clock.tick(50)/1000

if __name__ == "__main__":
    main()