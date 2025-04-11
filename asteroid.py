from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x,y,radius)

	def draw(self,screen):
		pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,width=2)

	def update(self,dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill() # Because this method is only called when an asteroid dies.

		if self.radius<=ASTEROID_MIN_RADIUS:
			return
		
		# Initilializing new asteroids
		random_angle = random.uniform(20,50)
		print(random_angle)
		velocity1 = self.velocity.rotate(random_angle)*1.2
		velocity2 = self.velocity.rotate(-random_angle)*1.2
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		smaller_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
		smaller_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)

		smaller_asteroid1.velocity = velocity1
		smaller_asteroid2.velocity = velocity2




