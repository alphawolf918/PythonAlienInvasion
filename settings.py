class Settings:
    #Stores all Settings for Alien Invasion

    def __init__(self):
        """Initialize game settings"""

        #Screen Settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.fullscreen = True

        #Ship Settings
        self.ship_size = 64

        #Bullet Settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        #Alien Settings
        self.alien_size = 32

        #Alien Fleet Settings
        self.fleet_drop_speed = 5

        #Level Settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Initialize the settings taht change throughout the game."""

        #Ship Settings
        self.ship_speed = 1.5
        self.ship_lives = 3

        #Bullet Settings
        self.bullet_speed = 3.0

        #Alien Settings
        self.alien_speed = 1.0
        self.alien_score = 10

        #Alien Fleet Settings
        self.fleet_direction = 1

    def increase_stats(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_score = int(self.alien_score * self.score_scale)
