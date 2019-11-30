import database
import menu

import pygame
import pytmx
import random
import sys

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		self.display = pygame.Surface((600, 400))
		pygame.display.set_caption('The Freak Hunter')
		self.dlgt = 50
		self.FPS = 60

		self.sound = False
		self.pressed = pygame.key.get_pressed()
		self.font = pygame.font.SysFont("calibri", 30)
		self.map = pytmx.load_pygame('Maps/city.tmx')
		self.cam_x = 0
		self.cam_y = 0

		self.en = []
		self.en.append(database.FREAKS[0])
		self.en[0]['HP'] = self.en[0]['MAXHP']
		self.en[0]['SPRITE']=pygame.image.load('Sprites/' + (self.en[0]['NAME']).lower() + '_stand.png')
		self.en.append(database.FREAKS[0])
		self.en[1]['HP'] = self.en[0]['MAXHP']
		self.en[1]['SPRITE']=pygame.image.load('Sprites/' + (self.en[1]['NAME']).lower() + '_stand.png')

		self.dlg = ''
		self.battle = False
		self.btime = 10
		self.inventory = False
		self.phone = 0
		self.winbar = 0
		self.turn = -1
		self.opt = 0
		self.mnu = 1
		self.aimx = 300
		self.player_barhp=[]
		self.pp=[]
		x=0
		for i in database.PLAYER:
			print(i)
			self.player_barhp.append(i['MAXHP'])
			self.pp.append([])
			for j in database.EQUIPMENT[x]:
				try:self.pp[x].append(j[1]['CAPACITY'])
				except:pass
			self.pp[x].append(0)
			self.pp[x].append(0)
			x+=1
		print(self.pp)
		self.player_rect = pygame.Rect(100,100,10,16)
		self.player_spd = 3
		self.player_sprite = [pygame.image.load('Sprites/hero_walkD_0.png')]
		self.player_gif = 1
		self.player_mov = False
		self.player_color = (100, 100, 100)

		self.en_rect = pygame.Rect(100,100,10,16)
		self.en_hp = 7
		self.en_xp = 10
		self.en_attack = 3

		pygame.mixer.music.load('Music/City.mp3')
		if self.sound == True: pygame.mixer.music.play(-1)

	def enemy(self, frk):
		if self.en_rect.x < self.player_rect.x: self.en_rect.x+=2
		if self.en_rect.x > self.player_rect.x: self.en_rect.x-=2
		if self.en_rect.y < self.player_rect.y: self.en_rect.y+=2
		if self.en_rect.y > self.player_rect.y: self.en_rect.y-=2

		if self.colide(self.en_rect, self.player_rect) == True:
			self.patt=[]
			self.pagi=[]
			self.tatt=[]
			self.tagi=[]
			for i in database.PLAYER:
				self.patt.append(i['ATTACK'][i['LEVEL']])
				self.pagi.append(i['AGILITY'][i['LEVEL']])
				self.tatt.append(0)
				self.tagi.append(0)
			self.battle = True
			while self.winbar<100:
				self.winbar += 5
				self.update()
				self.draw()
			self.dialog([self.en[0]['NAME'] + ' aparece!!']); self.turn=0

		self.display.blit(pygame.image.load('Sprites/' + (self.en[frk]['NAME']).lower() + '_mini.png'), (self.en_rect.x, self.en_rect.y))

	def colide(self, i1, i2):
		if i1.x > i2.x and i1.x < i2.x + i2.width or i1.x + i1.width > i2.x and i1.x + i1.width < i2.x + i2.width:
			if i1.y > i2.y and i1.y < i2.y + i2.height or i1.y + i1.height > i2.y and i1.y + i1.height < i2.y + i2.height:
				return True
			else: return False
		else: return False

	def events(self):
		#EXIT GAME
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			#BATTLE OPTIONS
			if self.battle == True:
				self.pressed = pygame.key.get_pressed()

				if self.mnu == 2:
					if self.pressed[pygame.K_SPACE]:
						self.turn += 1
						self.mnu = 1
						if self.turn == len(database.PLAYER):
							self.fight()
				elif self.mnu == 1:
					if self.pressed[pygame.K_UP]: self.opt -=1
					if self.pressed[pygame.K_DOWN]: self.opt +=1
				
					if self.opt < 0: self.opt = 0
					if self.opt > 1: self.opt = 1

					if self.pressed[pygame.K_SPACE]:
						if self.opt < 4:
							self.mnu = 2
						elif self.opt == 4:
							self.turn += 1
							if self.turn == len(database.PLAYER):
								self.fight()

			#MENU OPTIONS
			if self.pressed[pygame.K_RETURN]: self.inventory = not self.inventory
			if self.pressed[pygame.K_BACKSPACE]: self.phone += 1

		#PLAYER MOVEMENT
		if self.battle == False:
			self.player_mov = True
			self.pressed = pygame.key.get_pressed()
			if self.pressed[pygame.K_UP]: self.player_rect.y -= self.player_spd; self.player_sprite = [ pygame.image.load('Sprites/hero_walkU_0.png'), pygame.image.load('Sprites/hero_walkU_1.png'), pygame.image.load('Sprites/hero_walkU_2.png'), pygame.image.load('Sprites/hero_walkU_3.png') ]
			elif self.pressed[pygame.K_DOWN]: self.player_rect.y += self.player_spd; self.player_sprite = [ pygame.image.load('Sprites/hero_walkD_0.png'), pygame.image.load('Sprites/hero_walkD_1.png'), pygame.image.load('Sprites/hero_walkD_2.png'), pygame.image.load('Sprites/hero_walkD_3.png') ]
			elif self.pressed[pygame.K_LEFT]: self.player_rect.x -= self.player_spd; self.player_sprite = [ pygame.image.load('Sprites/hero_walkL_0.png'), pygame.image.load('Sprites/hero_walkL_1.png'), pygame.image.load('Sprites/hero_walkL_2.png'), pygame.image.load('Sprites/hero_walkL_3.png') ]
			elif self.pressed[pygame.K_RIGHT]: self.player_rect.x += self.player_spd; self.player_sprite = [ pygame.image.load('Sprites/hero_walkR_0.png'), pygame.image.load('Sprites/hero_walkR_1.png'), pygame.image.load('Sprites/hero_walkR_2.png'), pygame.image.load('Sprites/hero_walkR_3.png') ]
			else: self.player_mov = False

	def dialog(self, txt):
		dlg = ''
		ind = 0
		self.draw()
		for l in txt:
			for i in l:
				dlg+=i
				self.screen.blit(self.font.render(dlg, True, (200, 200, 200)), (250, 30 + ind))
				pygame.display.update()
				pygame.display.flip()
				pygame.time.Clock().tick(self.dlgt)
			self.wait()
			ind += 30
			dlg = ''

	def wait(self):
		waiting = True
		while waiting == True:
			pygame.time.Clock().tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					waiting = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYUP:
					waiting = False

	def fight(self):
		#PLAYERS TURN
		self.dialog([''])
		self.turn=0
		self.mnu = 3
		for i in database.PLAYER:
			if self.opt < 4:
				if self.pp[self.turn][self.opt] > 0:
					self.pp[self.turn][self.opt] -= 1
					if self.aimx > 299 and self.aimx < 351:
						dmg = int(random.randint(database.EQUIPMENT[self.turn][self.opt][1]['DAMAGE'] - 2, database.EQUIPMENT[self.turn][self.opt][1]['DAMAGE'] + 2))
						self.en[self.turn]['SPRITE']=pygame.image.load('Sprites/' + (self.en[self.turn]['NAME']).lower() + '_damage.png')
						self.dialog([self.en[self.turn]['NAME'] + ' tomou ' + str(dmg) + ' de dano'])
						self.en[self.turn]['HP'] -= dmg
					else: self.dialog(['errou...'])
				else:self.dialog(['Você não tem munição!'])

			elif self.opt == 4:
				self.dialog([self.PLAYER[self.turn]['NAME'] + ' está em guarda'])

		#CHECK WIN - LEVEL UP
		if self.en[self.turn]['HP'] <= 0:
			self.dialog([self.en[self.turn]['NAME'] + ' foi derrotado'])
			pygame.mixer.Sound('SFX/victory.ogg').play()
			while self.winbar<210:
				self.winbar += 5
				self.update()
				self.draw()
			self.dialog(['VITÓRIA'])
			database.PLAYER[self.turn]['XP'] += self.en_xp
			if database.PLAYER[self.turn]['XP'] >= database.PLAYER[self.turn]['MAXXP']:
				database.PLAYER[self.turn]['LEVEL'] += 1
				database.PLAYER[self.turn]['XP'] = 1
				database.PLAYER[self.turn]['MAXXP'] *= 2
				self.dialog(['SUBIU PARA O NÍVEL ' + str(database.PLAYER[self.turn]['LEVEL'])])
			self.turn = 0
			self.battle = False
			while self.winbar>0:
				self.winbar -= 5
				self.update()
				self.draw()

		#ENEMIES TURN
		else:
			for i in self.en:
				ht=database.PLAYER[self.turn]['HEALTH']
				if ht==0:print('normal')
				if ht==1:print('poison')
				opt=int(random.randint(0,4))
				if opt>3:opt=3
				act=self.en[self.turn]['HABILITIES'][opt]
				dd=self.en[self.turn]['NAME'] + ' usa ' + act[0]
				self.en[self.turn]['SPRITE']=pygame.image.load('Sprites/' + (self.en[self.turn]['NAME']).lower() + '_attack.png')

				if act[3]==1:
					if act[2]<0:
						database.PLAYER[self.turn]['HP']+=act[2]
						self.dialog([dd, database.PLAYER[self.turn]['NAME'] + ' tomou ' + str(act[2]) + ' de dano'])
					elif act[2]>0:
						self.en[self.turn]['HP']+=act[2]
				elif act[3]==2:
					if act[2]<0:
						if self.tatt[self.turn]<2:
							self.patt[self.turn]+=act[2]
							self.dialog([dd, database.PLAYER[self.turn]['NAME'] + ' perdeu ' + str(act[2]) + ' de ATAQUE'])
							self.tatt[self.turn]+=1
					elif act[2]>0:
						act[2]+=act[2]
				elif act[3]==3:
					if act[2]<0:
						if self.tagi[self.turn]<2:
							self.pagi[self.turn]+=act[2]
							self.dialog([dd, database.PLAYER[self.turn]['NAME'] + ' perdeu ' + str(act[2]) + ' de AGILIDADE'])
							self.tagi[self.turn]+=1
					elif act[2]>0:
						self.en[self.turn]['AGILITY']+=act[2]
				elif act[3]==4:	
					database.PLAYER[self.turn]['HEALTH']=act[2]
					if act[2]==1:self.dialog([dd, database.PLAYER[self.turn]['NAME'] + ' foi envenenado'])
					if act[2]==2:self.dialog([dd, database.PLAYER[self.turn]['NAME'] + ' está com náusea'])

				if database.PLAYER[self.turn]['HP'] <= 0:
					self.dialog([database.PLAYER[self.turn]['NAME'] + ' desmaiou...', 'você perdeu'])
					self.turn = 0
					self.battle = False
					database.PLAYER[self.turn]['HP'] = database.PLAYER[self.turn]['MAXHP']

				self.en[self.turn]['SPRITE']=pygame.image.load('Sprites/' + (self.en[self.turn]['NAME']).lower() + '_stand.png')
			self.turn = 0
			self.mnu = 1
		self.aimx+=40

	def draw(self):
		self.display.fill((0, 0, 200))

		#BATTLE
		if self.battle == True:
			self.display.blit(pygame.image.load('Backgrounds/mountains.png'), (0, 160))
			enx=0
			for i in self.en:
				self.display.blit(i['SPRITE'], (300+enx, 180))
				enx+=80

			#BLACK BARS
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

			#PLAYER BARS
			if self.winbar==100:
				if self.turn < len(database.PLAYER) and self.turn!=-1:
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,10,100,20))
					while float(self.player_barhp[self.turn]) > float(database.PLAYER[self.turn]['HP']):
						self.player_barhp[self.turn] -= database.PLAYER[self.turn]['RESISTANCE'][database.PLAYER[self.turn]['LEVEL']]
						if self.player_barhp[self.turn]>0:pygame.draw.rect(self.display, (255, 255, 0), pygame.Rect(10,10,int(100/(database.PLAYER[self.turn]['MAXHP']/self.player_barhp[self.turn])),20))
					if database.PLAYER[self.turn]['HP']>0:pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(10,10,int(100/(database.PLAYER[self.turn]['MAXHP']/database.PLAYER[self.turn]['HP'])),20))

					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,40,100,20))
					if self.pp[self.turn][self.opt]>0:pygame.draw.rect(self.display, (0, 100, 255), pygame.Rect(10,40,int(100/(database.EQUIPMENT[self.turn][self.opt][1]['CAPACITY']/self.pp[self.turn][self.opt])),20))

					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,70,100,20))
					if database.PLAYER[self.turn]['XP']>0:pygame.draw.rect(self.display, (0, 255, 100), pygame.Rect(10,70,int(100/(database.PLAYER[self.turn]['MAXXP']/database.PLAYER[self.turn]['XP'])),20))

				#ENEMIES BARS
				y=0
				for i  in self.en:
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10+y,310,100,20))
					if i['HP']>0:pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(10+y,310,int(100/(i['MAXHP']/i['HP'])),20))
					y+=110
			
			if self.turn < len(database.PLAYER) and self.turn!=-1:
				#OPTIONS
				if self.mnu == 1:
					self.display.blit(self.font.render(database.PLAYER[self.turn]['NAME'], True, (200, 200, 200)), (150, 10))
					if self.opt == 0: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][0][0], True, (255, 255, 100)), (150, 20))
					else: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][0][0], True, (200, 200, 200)), (150, 20))
					if self.opt == 1: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][1][0], True, (255, 255, 100)), (150, 50))
					else: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][1][0], True, (200, 200, 200)), (150, 50))
					if self.opt == 2: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][2][0], True, (255, 255, 100)), (300, 20))
					else: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][2][0], True, (200, 200, 200)), (300, 20))
					if self.opt == 3: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][3][0], True, (255, 255, 100)), (300, 50))
					else: self.display.blit(self.font.render(database.EQUIPMENT[self.turn][3][0], True, (200, 200, 200)), (300, 50))

				#AIM BAR
				elif self.mnu == 2:
					if self.opt < 4:
						self.aimx += 12 - database.PLAYER[self.turn]['AGILITY'][database.PLAYER[self.turn]['LEVEL']]
						if self.aimx > 400 - database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]: self.aimx = 100 + database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]
						self.display.blit(pygame.image.load('Sprites/aim.png'), (self.aimx, 200))

		#MAP
		elif self.battle == False:
			for x in range(0, 22):
				for y in range(0, 15):
					self.display.blit(self.map.get_tile_image(x, y, 0), (x*30-self.cam_x, y*30-self.cam_y))

			pygame.draw.rect(self.display, (255, 0, 0), self.player_rect)

			#OBJECTS
			self.display.blit(self.player_sprite[self.player_gif//len(self.player_sprite)], (self.player_rect.x-self.cam_x, self.player_rect.y-self.cam_y))
			if self.en[0]['HP']>0:self.enemy(0)

		#INVENTORY
		if self.inventory == True:
			inv = menu.Inventory()
			inv.show(0,self.display)

		#PHONE
		if self.phone > 0:
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(200,30,200,290))
			pygame.draw.rect(self.display, (0, 0, 255), pygame.Rect(210,60,180,220))

		if self.phone == 1:
			self.display.blit(pygame.image.load('Sprites/ph_maps.png'), (230, 80))
			self.display.blit(pygame.image.load('Sprites/ph_call.png'), (265, 80))
			self.display.blit(pygame.image.load('Sprites/ph_mail.png'), (300, 80))
			self.display.blit(pygame.image.load('Sprites/ph_news.png'), (230, 120))
			self.display.blit(pygame.image.load('Sprites/ph_radi.png'), (265, 120))
			self.display.blit(pygame.image.load('Sprites/ph_camr.png'), (300, 120))
			self.display.blit(pygame.image.load('Sprites/ph_best.png'), (230, 160))
			self.display.blit(pygame.image.load('Sprites/ph_task.png'), (265, 160))
			self.display.blit(pygame.image.load('Sprites/ph_stts.png'), (300, 160))
			self.display.blit(pygame.image.load('Sprites/ph_sett.png'), (230, 200))
			self.display.blit(pygame.image.load('Sprites/ph_help.png'), (265, 200))
			self.display.blit(pygame.image.load('Sprites/ph_save.png'), (300, 200))

		elif self.phone ==2:
			pass

		elif self.phone ==3:
			pass
		
		elif self.phone ==4:
			pass
		
		elif self.phone ==5:
			pass
		
		elif self.phone ==6:
			pass
		
		elif self.phone ==7:
			pass
		
		elif self.phone ==8:
			pass
		
		elif self.phone ==9:
			pass
		
		elif self.phone ==10:
			pass
		
		elif self.phone ==11:
			pass
		
		elif self.phone ==12:
			pass

		#BLACK BARS
		if self.battle == False:
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

		#CAMERA
		self.cam_x += self.player_rect.x - self.cam_x - 300
		self.cam_y += self.player_rect.y - self.cam_y - 200

		self.screen.blit(pygame.transform.scale(self.display, (1200, 800)), (0, 0))

	def update(self):
		#ANIMATION
		if self.player_mov == True:
			self.player_gif +=1
			if self.player_gif == 60//len(self.player_sprite): self.player_gif = 0
		else: self.player_gif = 0

		pygame.display.update()
		pygame.display.flip()

	def run(self):
		pygame.time.Clock().tick(self.FPS)
		self.events()
		self.update()
		self.draw()

g = Game()
while True:
	g.run()