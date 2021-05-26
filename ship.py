import pygame
from pygame.sprite import Sprite
#a = "F:\Python\Python_Basics\Alines_invasion\Images\ship.bmp"


b = "D:\Python\Phase 1\Alines_invasion\Images\ship.bmp"


class Ship(Sprite):
	
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position"""
		super(Ship, self).__init__()
		self.screen = screen
		# load the ship image and get its rect.
		self.image = pygame.image.load(b)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		
		# start each new ship at the botton center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# store a value fo rth ship's center.
		self.center = float(self.rect.centerx)
		
		# movement flag
		self.moving_right = False
		self.moving_left = False
	
	def blitme(self):
		"""Draw the ship at the current location."""
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		"""update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		# update rect object form self.center
		self.rect.centerx = self.center

	def center_ship(self):
		self.center = self.screen_rect.centerx