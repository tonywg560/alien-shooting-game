class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game unmoving settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		#ship settings
		self.ship_limit = 3

		#Alien settings
		self.fleet_drop_speed = 8

		#bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 5

		#Leveling difficulty
		self.speedup_scale = 1.25
		#scoring increase per level
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""initialize settings that alter throughout the game"""
		self.ship_speed = 1.25
		self.bullet_speed = 1
		self.alien_speed = 0.5

		#score for an alien hit
		self.alien_points = 1

		#fleet_direction of 1 represents right, -1 means left
		self.fleet_direction = 1

	def increase_speed(self):
		"""increase speed settings and scores"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		