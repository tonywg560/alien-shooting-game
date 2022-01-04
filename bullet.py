import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" Class to manage bullets fired"""

	def __init__(self, ai_game):
		"""Create a bullet object at ships current position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		#Create a bullet rect at (0,0) then set correct position
		self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		#Store bullet position as decimal
		self.y = float(self.rect.y)

	def update(self):
		"""move bullet up screen"""
		#update decimal position of bullet
		self.y -= self.settings.bullet_speed
		#update the rect position
		self.rect.y = self.y 

	def draw_bullet(self):
		"""draw bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect) 