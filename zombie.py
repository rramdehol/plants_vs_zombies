import pygame;
from pygame.sprite import Sprite;
from random import randint;

class Zombie(Sprite):
	def __init__(self, screen, game_settings):
		super(Zombie, self).__init__();
		self.speed = game_settings.zombie_speed;
		self.health = game_settings.zombie_health;
		self.image = pygame.image.load('./images/Crazyzombie.gif');
		self.image = pygame.transform.scale(self.image,(127,148));
		self.rect = self.image.get_rect();
		self.screen = screen;
		self.screen_rect = screen.get_rect();
		self.rect.centery = self.screen_rect.centery;
		self.rect.right = self.screen_rect.right;
		self.x = float(self.rect.x);
		self.yard_row = randint(0,4);
		game_settings.zombie_in_row[self.yard_row] += 1;

		# rand_int = randint(0,45);
		# i=0;
		# print rand_int;
		# for square in squares:
		# 	if i == rand_int:
		# 		bot_coords = square.rect.bottom;
		# 		self.yard_row = square.row_number;
		# 		break;
		# 	i+=1;
		self.rect.centery = game_settings.squares['rows'][self.yard_row];
		

		# self.rec.botton = bot_coords;
		# self.rect.right = self.screen_rect.right;


	def update_me(self):
		self.x -= self.speed*1;
		self.rect.x = self.x;
	def draw_me(self):
		self.screen.blit(self.image, self.rect);
	def hit(self, damage):
		self.health	-= damage;
