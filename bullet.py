from circleshape import *
from constants import *

class Bullet(CircleShape):
	def __init__(self,x,y):
		super().__init__(x,y,BULLET_RADIUS)
		self.velocity = pygame.Vector2(0, 0)

	def update(self, dt):
		self.position += self.velocity * dt

	def draw(self,screen):
		pygame.draw.circle(screen,"white",(self.position.x,self.position.y),self.radius,width=2) 