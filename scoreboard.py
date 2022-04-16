import pygame.font

class Scoreboard:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for scoring information
        self.text_color = (155, 155, 155)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: {:,}".format(rounded_score)
        lvl_str = "Level: {:}".format(self.stats.level)
        lives_str = "Lives: {:}".format(self.settings.ships_left)

        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.lvl_image = self.font.render(lvl_str, True, self.text_color, self.settings.bg_color)
        self.lives_image = self.font.render(lives_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        #Display level above the score
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.screen_rect.right - 20
        self.score_rect.top = (self.score_rect.top + 20)

        #Display lives below the score
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.screen_rect.right - 20
        self.lives_rect.top = (self.score_rect.top + 40)

    def draw_score(self):
        #Draw data to screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
