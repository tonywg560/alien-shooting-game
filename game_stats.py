class GameStats:
	"""tract stats for game"""

	def __init__(self, ai_game):
		"""init statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		#Make game inactive initailly
		self.game_active = False 

		#High score storing
		self.high_score = 0 
		#set level


	def reset_stats(self):
		"""init statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit 
		self.score = 0
		self.level = 1
