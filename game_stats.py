class GameStats:
    #Track stats for Alien Invasion

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.score = 0
        self.reset_stats()

    def reset_stats(self):
        #Initialize stats that can change during the game
        self.ships_left = self.settings.ship_lives
        self.level = 1
        self.score = 0

    def increase_level(self):
        self.level += 1
        print("Level Reached: " + str(self.level))

        if self.level % 5 == 0:
            self.ships_left += 1
            print("New ship life received!")

    def increase_score(self):
        self.score += self.settings.alien_hit_score
