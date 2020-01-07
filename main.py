# -*- coding: utf-8 -*-
class Settings:
	def __init__(self):
		file = open('settings.db','r')
		self.lang = file.readline()[0:-1]
		self.sfx = float(file.readline()[0:-1])
		self.msc = float(file.readline()[0:-1])
		self.up = file.readline()[0:-1]
		self.down = file.readline()[0:-1]
		self.left = file.readline()[0:-1]
		self.right = file.readline()[0:-1]
		self.act = file.readline()[0:-1]
		self.phone = file.readline()[0:-1]
		self.inventory = file.readline()[0:-1]
		self.speed = int(file.readline()[0:-1])
		self.color = file.readline()
		file.close()

s = Settings()
if s.lang == 'PT': import database_PT as database
if s.lang == 'EN': import database_EN as database

import menu

import pygame
import pytmx
import random
import webbrowser
import sys

class Game:
	def __init__(self):
		#GAME SETTINGS
		pygame.init()
		pygame.display.set_caption('Mutation Purge')
		pygame.display.set_icon(pygame.image.load('Icon.png'))
		self.screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
		self.display = pygame.Surface((600, 400))
		self.displayzw = 600
		self.displayzh = 400
		self.displayx = 0
		self.displayy = 0
		self.FPS = 60
		self.sound = False
		self.mininfo = pygame.font.Font('Fonts/pixel-font.ttf', 25)
		self.monotype = pygame.font.Font('Fonts/monotype.ttf', 15)
		self.cam = pygame.Rect(0,0,self.displayzw,self.displayzh)
		self.driving = 0
		self.dridir = 0

		self.sett = Settings()

		#MIXER
		pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
		self.ch_sfx = pygame.mixer.Channel(0)
		self.ch_sfx.set_volume(self.sett.sfx)
		self.ch_msc = pygame.mixer.Channel(1)
		self.ch_msc.set_volume(self.sett.msc)
		self.ch_ton = pygame.mixer.Channel(2)
		self.ch_ton.set_volume(self.sett.sfx)
		self.ch_sfx.play(pygame.mixer.Sound('SFX/save.wav'))

		#BATTLE VARIABLES
		self.dlg = []
		self.dlgfa = 500
		self.dmginfo = ''
		self.dmgy = 200
		self.dmgcol = (255,0,0)
		self.equip = []
		self.battle = False
		self.btime = 100
		self.bbg = ''
		self.hits = 0
		self.tdmg = 0
		self.hpl = 0
		self.tbt = 0
		self.turn = -1
		self.aim = pygame.Rect(300,200,30,30)
		self.pp = []
		self.barhp = []
		self.barhpl = []
		self.barpp = []
		self.barxp = []
		x=0
		for i in database.PLAYER:
			self.equip.append(0)
			self.pp.append([])
			self.barpp.append([])
			self.barhp.append(int(100/(i['MAXHP']/i['HP'])))
			self.barhpl.append(100)
			if i['XP'] > 0: self.barxp.append(int(100/(i['MAXXP']/i['XP'])))
			else: self.barxp.append(0)
			for j in database.EQUIPMENT[x]:
				try:
					self.pp[x].append(j[1]['CAPACITY'])
					self.barpp[x].append(str(j[1]['CAPACITY']))
				except:pass
			self.pp[x].append(0)
			self.pp[x].append(0)
			self.barpp[x].append(0)
			self.barpp[x].append(0)
			x+=1
		self.direction = True

		#MENU VARIABLES
		self.phn = menu.Phone()
		self.inv = menu.Inventory()
		self.opt = 1
		self.lopt = 0
		self.mnu = 1
		self.inventory = False
		self.invfade = 170
		self.phone = 0
		self.phofa = 400
		self.shp = False
		self.basket = []
		self.products = [database.ITEMS[10].copy(),database.ITEMS[12].copy(),database.ITEMS[5].copy(),database.ITEMS[17].copy(),database.ITEMS[22].copy(),database.ITEMS[45].copy(),database.ITEMS[50].copy(),database.ITEMS[61].copy(),database.ITEMS[64].copy()]
		self.winbar = 210
		self.fm = 0
		self.msc = 0
		self.signal = 0
		self.nottxt = ''
		self.notcol = (0,0,0)
		self.notx = 0

		#PLAYER VARIABLES
		self.player_rect = pygame.Rect(database.PX,database.PY,10,16)
		self.player_spd = 3
		self.player_sprite = database.SPRITES['DOWN_Sid']
		self.player_gif = 1
		self.player_mov = False
		self.player_color = (100, 100, 100)

		#LOADING MAP
		self.en = []
		self.foe = []
		self.npcs = []
		self.vehicles = []
		self.shops = []
		self.portals = []
		self.chests = []
		self.rendermap()
		self.transiction(False, 0)

	def enemy(self, en):
		if self.colide(self.en[en]['RECT'], self.cam) and self.battle == False:
			if self.en[en]['RECT'].x - self.cam.x < self.player_rect.x - self.cam.x: self.en[en]['RECT'].x += 3
			if self.en[en]['RECT'].x - self.cam.x > self.player_rect.x - self.cam.x: self.en[en]['RECT'].x -= 3
			if self.en[en]['RECT'].y - self.cam.y < self.player_rect.y - self.cam.y: self.en[en]['RECT'].y += 3
			if self.en[en]['RECT'].y - self.cam.y > self.player_rect.y - self.cam.y: self.en[en]['RECT'].y -= 3

		if self.colide(self.en[en]['RECT'], self.player_rect) == True and self.winbar == 0:
			if self.en[en]['FIGHTING'] == False:
				self.foe.append(self.en[en])
				self.en[en]['FIGHTING'] = True
				if len(self.foe) == 1: self.fight()

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/' + (self.en[0]['NAME']).lower() + '_mini.png'), (self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y))

	def npc(self, x, y, ndg):
		rect = pygame.Rect(x,y,60,60)
		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[pygame.K_SPACE]:
					if self.dlgfa > 0:
						if isinstance(ndg, int): self.dialog(database.DIALOGS['NPC_'+str(ndg)][0].copy())
						else: self.dialog(database.DIALOGS[ndg][0].copy())

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/npc.png'), (rect.x+30-self.cam.x, rect.y+30-self.cam.y))

	def vehicle(self, x, y, vh):
		rect = pygame.Rect(x,y,60,60)
		if self.driving == int(vh[-1]) + 1: rect = self.player_rect

		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[pygame.K_SPACE] and self.driving == 0:
					trigger = True
					self.driving = int(vh[-1]) + 1
					self.displayzw = 1200
					self.displayzh = 800
					print(self.cam)
					self.display = pygame.Surface((1200, 800))

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/' + vh + '_walkL.png'), (rect.x+30-self.cam.x, rect.y+30-self.cam.y))

	def shop(self, x, y, w, h, t):
		if t == 0: rect = pygame.Rect(x,y,w,h)
		if t > 0: rect = pygame.Rect(x,y,60,60)

		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[pygame.K_SPACE]:
					if t == 1 and self.basket == []:
						self.dialog(database.DIALOGS['CASHIER'][0].copy())
					else:
						self.shp = True
						self.lopt = 0
						self.opt = 1
						self.mnu = t
						if t == 2: database.ATM = str(database.ATM)

		if self.battle == False:
			if t == 0: pygame.draw.rect(self.display, (200, 0, 0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
			if t > 0: self.display.blit(pygame.image.load('Sprites/npc.png'), (rect.x - self.cam.x, rect.y - self.cam.y))

	def chest(self, x, y, rwd):
		rect = pygame.Rect(x,y,60,60)
		mask = pygame.Rect(x,y,30,30)
		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[pygame.K_SPACE]:
					self.dialog(['Você achou '+rwd])
					menu.Inventory().add(rwd)
		if self.colide(self.player_rect, mask) == True:
			self.player_spd = 0

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/chest.png'), (rect.x+30-self.cam.x, rect.y+30-self.cam.y))

	def portal(self, x, y, px, py, mp):
		rect = pygame.Rect(x,y,20,40)
		if self.colide(self.player_rect, rect) == True and self.winbar == 0:
			self.ch_sfx.play(pygame.mixer.Sound('SFX/door_open.wav'))
			self.transiction(True, 210)
			self.player_rect.x = px
			self.player_rect.y = py
			database.MAP = mp
			self.rendermap()
			self.transiction(False, 0)
			self.ch_sfx.play(pygame.mixer.Sound('SFX/door_close.wav'))

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/door.png'), (rect.x-self.cam.x, rect.y-self.cam.y))

	def colide(self, i1, i2):
		if self.driving == 0:
			if i1.x - self.cam.x > i2.x - self.cam.x and i1.x - self.cam.x < i2.x - self.cam.x + i2.width or i1.x - self.cam.x + i1.width > i2.x - self.cam.x and i1.x - self.cam.x + i1.width < i2.x - self.cam.x + i2.width:
				if i1.y - self.cam.y > i2.y - self.cam.y and i1.y - self.cam.y < i2.y - self.cam.y + i2.height or i1.y - self.cam.y + i1.height > i2.y - self.cam.y and i1.y - self.cam.y + i1.height < i2.y - self.cam.y + i2.height:
					return True
				else: return False
			else: return False
		else: return False

	def events(self):
		#EXIT GAME
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			self.pressed = pygame.key.get_pressed()
			if self.pressed[pygame.K_DELETE]:
				self.__init__()

			#BATTLE OPTIONS
			if self.battle == True:
				self.pressed = pygame.key.get_pressed()
				if self.turn == len(database.PLAYER): self.fight()

				if self.mnu == 2:
					#DEBUG
					if self.pressed[pygame.K_UP]: database.PLAYER[self.turn]['LEVEL'] += 1

					if self.pressed[pygame.K_SPACE]:
						self.fight()
						self.turn += 1
						self.mnu = 1
						if self.turn == len(database.PLAYER): self.fight()
						if database.PLAYER[self.turn]['HP'] <= 0: self.turn += 1; self.mnu = 1

				elif self.mnu == 1:
					if self.pressed[pygame.K_LEFT]: self.equip[self.turn] -=1
					if self.pressed[pygame.K_RIGHT]: self.equip[self.turn] +=1
				
					if self.equip[self.turn] < 0: self.equip[self.turn] = 7
					if self.equip[self.turn] > 7: self.equip[self.turn] = 0

					if self.pressed[pygame.K_SPACE]:
						if self.equip[self.turn] < 4:
							if self.pp[self.turn][self.equip[self.turn]] > 0:
								self.mnu = 2
							else:
								self.dialog(['Você não tem munição!'])
						elif self.equip[self.turn] == 4:
							self.mnu = 2
						elif self.equip[self.turn] == 5:
							self.fight()
						elif self.equip[self.turn] == 6:
							self.pres[self.turn] += 3
							self.dialog([database.PLAYER[self.turn]['NAME'] + ' está em guarda'])
							self.turn += 1
							if self.turn == len(database.PLAYER): self.fight()
						elif self.equip[self.turn] == 7:
							self.fight()
							if self.turn != -1:
								self.turn = len(database.PLAYER)
								self.fight()

			#SHOP OPTIONS
			if self.shp == True:
				if self.pressed[pygame.K_LEFT]: self.opt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
				if self.pressed[pygame.K_RIGHT]: self.opt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
				if self.pressed[pygame.K_UP]: self.lopt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
				if self.pressed[pygame.K_DOWN]: self.lopt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

				if self.mnu == 0:
					if self.pressed[pygame.K_SPACE]:
						if self.lopt < len(self.products):
							for i in range(self.opt): self.basket.append(self.products[self.lopt].copy())
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))
						else:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 1
					if self.lopt < 0: self.lopt = 0
					if self.lopt > len(self.products): self.lopt = len(self.products)

				if self.mnu == 1:
					if self.pressed[pygame.K_SPACE]:
						if self.lopt < len(self.basket):
							self.ch_sfx.play(pygame.mixer.Sound('SFX/buy.wav'))
							for i in self.basket:
								bb = False
								for j in database.INVENTORY[0]:
									for x in j:
										if x == '_':
											bb = True
								if bb == True:
									database.MONEY -= i[2]
									self.basket.remove(i)
									self.inv.add(i[0])
						else:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 1
					if self.lopt < 0: self.lopt = len(self.basket) + 1
					if self.lopt > len(self.basket) + 1: self.lopt = 0

				if self.mnu == 2:
					if self.pressed[pygame.K_SPACE]:
						if self.lopt == 0:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))
							self.mn = 12
						elif self.lopt == 1:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))
							self.mn = 13
						elif self.lopt == 2:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))
							self.mn = 0
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 1
					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

				if self.mnu == 12:
					if self.pressed[pygame.K_SPACE]:
						self.ch_sfx.play(pygame.mixer.Sound('SFX/cash_get.wav'))
						self.mn = 12

					if self.opt < 0: self.opt = len(database.ATM)
					if self.opt > len(database.ATM): self.opt = 0
					if self.lopt < 0: self.lopt = 9
					if self.lopt > 9: self.lopt = 0

					database.ATM[self.opt] = self.lopt

			#INVENTORY OPTIONS
			if self.pressed[pygame.K_RETURN] and self.phone == 0:
				self.inventory = not self.inventory
				if self.inventory == False:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/inventory_close.wav'))
					self.invfade = 0
				if self.inventory == True:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/inventory_open.wav'))
					self.opt = 0
					self.lopt = 1
					self.mnu = 0

			if self.inventory == True:
				if self.mnu == 0:
					if self.pressed[pygame.K_LEFT]: self.opt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[pygame.K_RIGHT]: self.opt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[pygame.K_UP]: self.lopt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
					if self.pressed[pygame.K_DOWN]: self.lopt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

					if self.pressed[pygame.K_SPACE]:
						self.mnu += 1
						self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))

					if self.opt < 0: self.opt = 0
					if self.lopt < 1: self.lopt = 1

				elif self.mnu == 1:
					if self.pressed[pygame.K_UP]: self.mnu -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
					if self.pressed[pygame.K_DOWN]: self.mnu +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

					if self.pressed[pygame.K_SPACE]:
						if self.mnu == 1:
							if database.INVENTORY[0][self.lopt][self.opt][3] == 9:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/heal.wav'))
								database.PLAYER[0]['HP'] += database.INVENTORY[0][self.lopt][self.opt][4]
								self.inv.drop(self.opt, self.lopt)
								self.mnu = 0

						if self.mnu == 2:
							ii = self.opt
							ij = self.lopt
							iinv = 0
							self.mnu = 4
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))
						if self.mnu == 3:
							self.inv.drop(self.opt, self.lopt)
							self.mnu = 0
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))

					if self.mnu < 1: self.mnu = 3
					if self.mnu > 3: self.mnu = 1

				elif self.mnu == 4:
					if self.pressed[pygame.K_LEFT]: self.opt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[pygame.K_RIGHT]: self.opt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[pygame.K_UP]: self.lopt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
					if self.pressed[pygame.K_DOWN]: self.lopt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

					if self.pressed[pygame.K_SPACE]:
						self.inv.move(ii,ij,inv,self.opt,self.lopt,1)
						self.mnu = 1

					if self.opt < 0: self.opt = 0
					if self.lopt < 1: self.opt = 1

			#PHONE OPTIONS
			if self.pressed[pygame.K_BACKSPACE] and self.inventory == False:
				if self.phone == 0 or self.phone > 1:
					if self.phone == 0: self.opt = 0; self.lopt = 0
					if self.phone == 2: self.opt = 0; self.lopt = 0
					if self.phone == 3: self.opt = 1; self.lopt = 0
					if self.phone == 4: self.opt = 2; self.lopt = 0
					if self.phone == 5: self.opt = 0; self.lopt = 1
					if self.phone == 6: self.opt = 1; self.lopt = 1
					if self.phone == 7: self.opt = 2; self.lopt = 1
					if self.phone == 8: self.opt = 0; self.lopt = 2
					if self.phone == 9: self.opt = 1; self.lopt = 2
					if self.phone == 10: self.opt = 2; self.lopt = 2
					if self.phone == 11: self.opt = 0; self.lopt = 3
					if self.phone == 12: self.opt = 1; self.lopt = 3
					if self.phone == 13: self.opt = 2; self.lopt = 3
					if self.phone == 14: self.opt = 0; self.lopt = 4
					if self.phone == 15: self.opt = 1; self.lopt = 4
					if self.phone == 16: self.opt = 2; self.lopt = 4
					self.phone = 1
					self.mnu = 0
				elif self.phone == 1:
					self.phone = 0
					self.opt = 0
					self.lopt = 0

			if self.phone > 0:
				if self.phone == 1:
					if self.pressed[pygame.K_UP]: self.lopt -=1
					if self.pressed[pygame.K_DOWN]: self.lopt +=1
					if self.pressed[pygame.K_LEFT]: self.opt -=1
					if self.pressed[pygame.K_RIGHT]: self.opt +=1

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = 4
					if self.lopt > 4: self.lopt = 0

					if self.pressed[pygame.K_SPACE]:
						if self.lopt == 0:
							if self.opt == 0: self.phone = 2; self.opt = round(self.player_rect.x/30); self.lopt = round(self.player_rect.x/30); self.mnu = 375
							elif self.opt == 1: self.phone = 3
							elif self.opt == 2: self.phone = 4
						elif self.lopt == 1:
							if self.opt == 0: self.phone = 5
							elif self.opt == 1: self.phone = 6
							elif self.opt == 2: self.phone = 7
						elif self.lopt == 2:
							if self.opt == 0: self.phone = 8
							elif self.opt == 1: self.phone = 9
							elif self.opt == 2: self.phone = 10
						elif self.lopt == 3:
							if self.opt == 0: self.phone = 11
							elif self.opt == 1: self.phone = 12
							elif self.opt == 2: self.phone = 13
						elif self.lopt == 4:
							if self.opt == 0: self.phone = 14
							elif self.opt == 1: self.phone = 15
							elif self.opt == 2: self.phone = 16
						self.opt = 0
						self.lopt = 0
						self.mnu = 0

				elif self.phone == 3:
					if self.mnu == 0:
						if self.pressed[pygame.K_UP]: self.lopt -=1
						if self.pressed[pygame.K_DOWN]: self.lopt +=1
						if self.pressed[pygame.K_LEFT]: self.opt -=1; self.lopt = 0
						if self.pressed[pygame.K_RIGHT]: self.opt +=1; self.lopt = 0

					if self.pressed[pygame.K_SPACE]:
						if self.mnu == 0:
							self.mnu = 1
							pygame.time.wait(round(random.randint(10,200)))
							self.dialog(self.phn.call(str(database.CONTACTS[self.lopt][1]),0,False,False))

						elif self.mnu == 1: self.mnu = 0

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = len(database.CONTACTS) - 1
					if self.lopt > len(database.CONTACTS) - 1: self.lopt = 0

				elif self.phone == 4 and self.signal > 0:
					if self.mnu == 0:
						if self.pressed[pygame.K_UP]: self.lopt -=1
						if self.pressed[pygame.K_DOWN]: self.lopt +=1
						if self.pressed[pygame.K_LEFT]: self.opt -=1; self.lopt = 0
						if self.pressed[pygame.K_RIGHT]: self.opt +=1; self.lopt = 0

					if self.pressed[pygame.K_SPACE] and self.signal > 0:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0:
							if self.opt == 0: self.phn.e_unread[self.lopt][3] = True
							if self.opt == 2: database.EMAILS[self.lopt][3] = True
							self.mnu = 0

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = 3
					if self.lopt > 3: self.lopt = 0

				elif self.phone == 5 and self.signal > 0:
					if self.mnu == 0:
						if self.pressed[pygame.K_UP]: self.lopt -=1
						if self.pressed[pygame.K_DOWN]: self.lopt +=1

					if self.pressed[pygame.K_SPACE]:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.lopt < 0: self.lopt = 3
					if self.lopt > 3: self.lopt = 0

				elif self.phone == 6:
					if self.pressed[pygame.K_UP]: self.lopt -=1
					if self.pressed[pygame.K_DOWN]: self.lopt +=1

					if self.lopt < 0: self.lopt = len(database.RADIO[str(round(self.fm/10))]) - 1
					if self.lopt > len(database.RADIO[str(round(self.fm/10))]) - 1: self.lopt = 0

					if self.pressed[pygame.K_SPACE]:
						pygame.mixer.music.load('Songs/FM_' + str(round(self.fm/10)) + '/' + database.RADIO[str(round(self.fm/10))][self.lopt])
						pygame.mixer.music.play(-1)

				elif self.phone == 8 and self.signal > 0:
					if self.pressed[pygame.K_UP]: self.lopt -=1
					if self.pressed[pygame.K_DOWN]: self.lopt +=1

					if self.pressed[pygame.K_SPACE]:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.mnu == 0:
						if self.lopt < 0: self.lopt = len(database.BESTIARY) - 1
						if self.lopt > len(database.BESTIARY) - 1: self.lopt = 0

					if self.mnu > 0:
						if self.pressed[pygame.K_LEFT]: self.mnu = 1
						if self.pressed[pygame.K_RIGHT]: self.mnu = 2

						if self.lopt < 0: self.lopt = 3
						if self.lopt > 3: self.lopt = 0

				elif self.phone == 9:
					if self.pressed[pygame.K_UP]: self.lopt -=1
					if self.pressed[pygame.K_DOWN]: self.lopt +=1
					if self.pressed[pygame.K_LEFT]: self.opt -=1
					if self.pressed[pygame.K_RIGHT]: self.opt +=1

					if self.pressed[pygame.K_SPACE]:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu == 1:
							if self.opt == 0: self.phn.t_unmark[self.lopt][3] = True
							if self.opt == 2: database.TASKS[self.lopt][3] = True
							self.mnu = 0

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = 3
					if self.lopt > 3: self.lopt = 0

				elif self.phone == 10:
					if self.pressed[pygame.K_LEFT]: self.opt -=1
					if self.pressed[pygame.K_RIGHT]: self.opt +=1

					if self.opt < 0: self.opt = len(database.PLAYER) - 1
					if self.opt > len(database.PLAYER) - 1: self.opt = 0

				elif self.phone == 13:
					if self.mnu == 0:
						if self.pressed[pygame.K_UP]: self.lopt -=1
						if self.pressed[pygame.K_DOWN]: self.lopt +=1

					if self.pressed[pygame.K_SPACE]:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.lopt < 0: self.lopt = len(database.MANUAL) - 1
					if self.lopt > len(database.MANUAL) - 1: self.lopt = 0

				elif self.phone == 15:
					if self.pressed[pygame.K_UP]: self.lopt -=1
					if self.pressed[pygame.K_DOWN]: self.lopt +=1

					if self.lopt < 0: self.lopt = 0
					if self.lopt > 1: self.lopt = 1

					if self.pressed[pygame.K_SPACE]:
						if self.lopt == 0:
							webbrowser.get('windows-default').open('twitter.com/kaixtr')
						if self.lopt == 1:
							webbrowser.get('windows-default').open('github.com/kaixtr')

				elif self.phone == 16 and self.signal > 0:
					if self.pressed[pygame.K_UP]: self.lopt -=1
					if self.pressed[pygame.K_DOWN]: self.lopt +=1

					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

					if self.pressed[pygame.K_SPACE] and self.signal > 0:
						self.ch_sfx.play(pygame.mixer.Sound('SFX/save.wav'))
						database.PX = self.player_rect.x
						database.PY = self.player_rect.y
						database.save_game(self.lopt + 1)


			'''if self.driving > 0:
				if self.pressed[pygame.K_LEFT]: self.dridir += 1
				if self.pressed[pygame.K_RIGHT]: self.dridir -= 1'''

		if self.phone == 2:
			if self.pressed[pygame.K_UP]: self.lopt -= 3
			if self.pressed[pygame.K_DOWN]: self.lopt += 3
			if self.pressed[pygame.K_LEFT]: self.opt -= 3
			if self.pressed[pygame.K_RIGHT]: self.opt += 3
			if self.pressed[pygame.K_SPACE]: self.mnu +=5
			if self.pressed[pygame.K_RETURN]: self.mnu -=5

			if self.opt < -self.map.width: self.opt = -self.map.width
			if self.opt > self.map.width: self.opt = self.map.width
			if self.lopt < -self.map.height: self.lopt = -self.map.height
			if self.lopt > self.map.height: self.lopt = self.map.height
			if self.mnu < 100: self.mnu = 100
			if self.mnu > 500: self.mnu = 500

		elif self.phone == 4:
			if self.mnu > 0:
				if self.pressed[pygame.K_UP]: self.mnu -=1
				if self.pressed[pygame.K_DOWN]: self.mnu +=1

				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 5:
			if self.mnu > 0:
				if self.pressed[pygame.K_UP]: self.mnu -=1
				if self.pressed[pygame.K_DOWN]: self.mnu +=1

				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 6:
			if self.pressed[pygame.K_LEFT]: self.fm -=1; self.lopt = 0
			if self.pressed[pygame.K_RIGHT]: self.fm +=1; self.lopt = 0

			if self.fm < 0: self.fm = 180
			if self.fm > 180: self.fm = 0

		elif self.phone == 13:
			if self.mnu > 0:
				if self.pressed[pygame.K_UP]: self.mnu -=1
				if self.pressed[pygame.K_DOWN]: self.mnu +=1
						
				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		#PLAYER MOVEMENT
		if self.battle == False and self.inventory == False and self.phone == 0:
			self.player_mov = False
			self.pressed = pygame.key.get_pressed()
			if self.driving == 0:
				if self.pressed[pygame.K_UP]: self.player_mov = True; self.player_rect.y -= self.player_spd; self.player_sprite = database.SPRITES['UP_Sid']
				elif self.pressed[pygame.K_DOWN]: self.player_mov = True; self.player_rect.y += self.player_spd; self.player_sprite = database.SPRITES['DOWN_Sid']
				if self.pressed[pygame.K_LEFT]: self.player_mov = True; self.player_rect.x -= self.player_spd; self.player_sprite = database.SPRITES['LEFT_Sid']
				elif self.pressed[pygame.K_RIGHT]: self.player_mov = True; self.player_rect.x += self.player_spd; self.player_sprite = database.SPRITES['RIGHT_Sid']
				if self.pressed[pygame.K_SPACE]: self.player_spd = 6
				else: self.player_spd = 3

			#DRIVING MOVEMENT
			if self.driving > 0:
				if database.GAS > 0:
					if self.pressed[pygame.K_UP]: self.player_mov = True; self.dridir = 0
					elif self.pressed[pygame.K_DOWN]: self.player_mov = True; self.dridir = 1
					elif self.pressed[pygame.K_LEFT]: self.player_mov = True; self.dridir = 2
					elif self.pressed[pygame.K_RIGHT]: self.player_mov = True; self.dridir = 3
					else: self.player_mov = False

				if self.dridir == 0: self.player_rect.y -= self.player_spd; self.player_sprite = database.SPRITES['UP_Sid']
				elif self.dridir == 1: self.player_rect.y += self.player_spd; self.player_sprite = database.SPRITES['DOWN_Sid']
				elif self.dridir == 2: self.player_rect.x -= self.player_spd; self.player_sprite = database.SPRITES['LEFT_Sid']
				elif self.dridir == 3: self.player_rect.x += self.player_spd; self.player_sprite = database.SPRITES['RIGHT_Sid']

				if self.pressed[pygame.K_SPACE]:
					if self.player_mov == True:
						if self.player_spd < self.vehicles[self.driving - 1]['SPEED'] and database.GAS > 0.0:
							self.player_spd += self.vehicles[self.driving - 1]['ACCELERATION']
						database.GAS -= self.vehicles[self.driving - 1]['GAS']
					else: self.player_spd -= self.vehicles[self.driving - 1]['ACCELERATION']
				else: self.player_spd -= self.vehicles[self.driving - 1]['ACCELERATION']

				if database.GAS < 1.0: self.player_mov = False

				if self.player_spd < 0: self.player_spd = 0
				if self.dridir < 0: self.dridir = 3
				if self.dridir > 3: self.dridir = 0

	def dialog(self, tx):
		self.dlg = []
		self.lopt = 0
		txt = tx
		tid = 0
		did = 0

		while self.dlgfa > 0:
			self.dlgfa -= 50
			self.draw()
			self.update()
			pygame.time.wait(2)

		while tid < len(txt):
			self.dlg.append('')
			print(txt)
			print(tid)
			if isinstance(txt[tid], str):
				for i in txt[tid]:
					self.ch_sfx.stop()
					self.ch_sfx.play(pygame.mixer.Sound('SFX/voice_mid.wav'))
					self.dlg[did] += i
					self.draw()
					self.update()
					pygame.time.wait(self.sett.speed)
				self.wait()
				did += 1
			else:
				if txt[tid] == 0:
					self.dlg = []

				elif txt[tid][0] == 0:
					self.inv.add(txt[tid][1])
					database.MONEY -= txt[tid][2]
					self.ch_sfx.play(pygame.mixer.Sound('SFX/item_get.wav'))
					self.notification('Adquiriu ' + txt[tid][1],(255, 255, 255))
					self.dlg = []

				elif txt[tid][0] == 1:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/notification.wav'))
					self.notification('Marcador adicionado',(140, 255, 253))
					self.dlg = []

				elif txt[tid][0] == 2:
					if txt[tid][1] != 'stop':
						self.ch_sfx.play(pygame.mixer.Sound('SFX/calling.wav'),-1)
						self.ch_ton.play(pygame.mixer.Sound('SFX/ringtone_1.ogg'))
						tw = 0
						cl = False
						while tw < 2000 and cl == False:
							pygame.time.wait(10)
							for event in pygame.event.get():
								if event.type == pygame.KEYUP:
									cl = True
							tw += 1
						self.ch_sfx.stop()
						self.ch_ton.stop()
						self.ch_sfx.play(pygame.mixer.Sound('SFX/equip.wav'))
						if cl == True:
							self.phone = 3
							self.mn = 1
							txt.insert(tid + 1, [2,'stop'])
							txt.insert(tid + 1, 0)
							for i in self.phn.call(str(database.CONTACTS[txt[tid][1]][1]),0,False,False)[-1:0:-1]:
								txt.insert(tid + 1, i)
							self.dlg = []
					else:
						self.phone = 0
						self.mn = 0
						self.dlg = []

				elif txt[tid][0] == 3:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/notification.wav'))
					database.INBOX.append(database.EMAILS[txt[tid][1]])
					self.notification('Novo email',(255, 221, 0))
					self.dlg = []

				elif txt[tid][0] == 4:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/notification.wav'))
					database.TASKS.append([txt[tid][1], False])
					self.notification('Nova tarefa disponível',(255, 123, 0))
					self.dlg = []

				elif txt[tid][0] == 5:
					f = database.FREAKS[txt[tid][1]].copy()
					f['DATE'] = str(database.DATE[0]) + '/' + str(database.DATE[1])
					i = len(database.BESTIARY) + 1
					if i < 10: i = '00' + str(i)
					elif i < 40: i = '0' + str(i)
					f['ID'] = i
					database.BESTIARY.append(f)
					self.ch_sfx.play(pygame.mixer.Sound('SFX/notification.wav'))
					self.notification(f['NAME'] + ' registrada',(134, 0, 211))
					self.dlg = []

				elif txt[tid][0] == 6:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/achievement.wav'))
					database.ACHIEVEMENTS[txt[tid][1]][2] = True
					self.notification(database.ACHIEVEMENTS[txt[tid][1]][0],(255, 191, 0))
					self.dlg = []

				elif txt[tid][0] == 7:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/notification.wav'))
					self.notification('Subiu de posição!',(56, 255, 0))
					self.dlg = []

				elif txt[tid][0] == 8:
					did += 1

				elif txt[tid][0] == 9:
					self.dlgfa = 500
					tm = 0
					'''while tm < txt[tid][1]:
						self.draw()
						self.update()
						pygame.time.wait(10)
						tm += 1'''
					pygame.time.wait(txt[tid][1])
					self.dlgfa = 0
					self.dlg = []

				elif txt[tid][0] == 10:
					self.dlg = []
					for j in txt[tid][1:]:
						self.dlg.append(j[0])
					self.diopt(len(txt[tid][1:]))
					for j in txt[tid][self.lopt][-1:0:-1]:
						txt.insert(tid + 1, j)
					self.lopt = 0
					self.dlg = []

				elif txt[tid][0] == 11:
					self.dlg = []
					tid += txt[tid][1]

				elif txt[tid][0] == 12:
					self.dlg = []
					tid -= txt[tid][1]

				elif txt[tid][0] == 13:
					for i in txt[tid][1:]:
						fo = database.FREAKS[i].copy()
						fo['SPRITE'] = pygame.image.load('Sprites/' + (fo['NAME']).lower() + '_stand.png')
						fo['MASK'] = pygame.Rect(230,180,44,85)
						self.foe.append(fo)
					self.dlg = []
					txt = []
					tid = 0
					self.fight()
				did = -1

			tid += 1

		self.dlg = []

		while self.dlgfa < 500:
			self.dlgfa += 50
			self.draw()
			self.update()
			pygame.time.wait(2)

	def diopt(self, ln):
		self.lopt = 1
		trigger = True
		self.draw()
		self.update()
		while trigger:
			for event in pygame.event.get():
				pygame.time.Clock().tick(60)
				self.draw()
				self.update()
				self.pressed = pygame.key.get_pressed()
				if self.pressed[pygame.K_UP]:
					if self.lopt > 1: self.lopt -= 1
				if self.pressed[pygame.K_DOWN]:
					if self.lopt < ln: self.lopt += 1
				if self.pressed[pygame.K_SPACE]:
					trigger = False
					break
				if event.type == pygame.QUIT:
					waiting = False
					pygame.quit()
					sys.exit()

	def wait(self):
		waiting = True
		while waiting == True:
			self.draw()
			self.update()
			pygame.time.Clock().tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					waiting = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYUP:
					waiting = False

	def transiction(self, fade, limit):
		if fade == False:
			while self.winbar > limit:
				self.winbar -= 5
				self.update()
				self.draw()
		else:
			while self.winbar < limit:
				self.winbar += 5
				self.update()
				self.draw()

	def fight(self):
		#BATTLE START
		if self.turn == -1:
			print('ENTERING...')
			self.ch_sfx.play(pygame.mixer.Sound('SFX/battle_foe.wav'))
			for i in range(8):
				pygame.time.wait(10)
				self.draw()
				self.update()
			self.bbg = pygame.image.load('Backgrounds/mountains.png')
			self.player_mov = False
			self.patt=[]
			self.pagi=[]
			self.pres=[]
			self.tatt=[]
			self.tagi=[]
			self.opt = 0
			self.mnu = 1
			for i in database.PLAYER:
				self.patt.append(i['ATTACK'][i['LEVEL']])
				self.pagi.append(i['AGILITY'][i['LEVEL']])
				self.pres.append(i['RESISTANCE'][i['LEVEL']])
				self.tatt.append(0)
				self.tagi.append(0)
			enx = 0
			while enx < len(self.foe):
				self.foe[enx]['MASK'].x += enx * 80
				enx += 1
			self.battle = True
			self.transiction(True, 100)
			self.dialog([self.en[0]['NAME'] + database.BATTLE[0]])
			self.turn = 0

		#PLAYERS TURN
		elif self.turn < len(database.PLAYER):
			self.mnu = 3
			if self.equip[self.turn] < 4:
				self.pp[self.turn][self.equip[self.turn]] -= 1
				gottem = False
				for i in self.foe:
					if self.colide(self.aim, i['MASK']):
						gottem = True
						dmg = int(random.randint(database.EQUIPMENT[self.turn][self.equip[self.turn]][1]['DAMAGE'] - 2, database.EQUIPMENT[self.turn][self.equip[self.turn]][1]['DAMAGE'] + 2)) - i['RESISTANCE']
						i['SPRITE'] = pygame.image.load('Sprites/' + (i['NAME']).lower() + '_damage.png')
						if dmg > 0:
							if dmg == database.EQUIPMENT[self.turn][self.equip[self.turn]][1]['DAMAGE'] + 2 - i['RESISTANCE']:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/critical.wav'))
								self.shake(10, i)
								self.infohit(database.BATTLE[3], (200, 0, 0))
							else:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/hit.wav'))
								self.shake(10, i)
								self.infohit(str(dmg), (200, 0, 0))
							i['SPRITE'] = pygame.image.load('Sprites/' + (i['NAME']).lower() + '_stand.png')
							i['HP'] -= dmg
							self.hits += 1
							self.tdmg += dmg
						else: self.infohit(database.BATTLE[5], (255, 255, 255))

						#CHECK WIN - LEVEL UP
						if i['HP'] <= 0:
							fade = 255
							i['SPRITE'].convert_alpha()
							while fade > 0:
								self.draw()
								self.update()
								fade -= 5
								i['SPRITE'].set_alpha(fade)
								pygame.time.wait(10)
						dth = 0
						for d in self.foe:
							if d['HP'] <= 0: dth += 1
						if dth == len(self.foe):
							self.ch_ton.play(pygame.mixer.Sound('SFX/victory.ogg'))
							self.transiction(True, 210)
							self.tbt += round(self.btime/10)
							xp = int(((self.hits*self.tdmg)-self.hpl+self.tbt)/len(database.PLAYER))
							self.dialog([database.BATTLE[6],database.BATTLE[7] + str(self.hits),database.BATTLE[8] + str(self.tdmg),database.BATTLE[9] + str(self.hpl),database.BATTLE[10]+str(self.tbt),database.BATTLE[11] + str(len(database.PLAYER)),'= ' + str(xp)+database.BATTLE[12]])
							for i in range(len(database.PLAYER)):
								database.PLAYER[i]['XP'] += xp
								plux = int(100/(database.PLAYER[i]['MAXXP']/xp))
							while self.barxp[0] < plux:
								self.draw()
								self.update()
								for i in range(len(database.PLAYER)):
									self.barxp[i] += 1
									if self.barxp[i] >= 100:
										self.barxp[i] = 0
										database.PLAYER[i]['LEVEL'] += 1
										database.PLAYER[i]['XP'] = 0
										database.PLAYER[i]['MAXXP'] *= 2
										plux = 0
										self.dialog([database.BATTLE[13] + str(database.PLAYER[i]['LEVEL'])])
								database.SCENE = 1
								pygame.time.wait(10)
							self.wait()
							self.turn = -1
							self.hits = 0
							self.tdmg = 0
							self.hpl = 0
							self.tbt = 0
							self.foe = []
							self.btime = 100
							self.battle = False
							self.transiction(False, 0)
						self.mnu = 0
				if gottem == False:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/miss.wav'))
					self.infohit(database.BATTLE[4], (200, 200, 200))
				#if self.pp[self.turn][self.equip] > 0: self.barpp[self.turn][self.opt] = int(100/(database.EQUIPMENT[self.turn][self.opt][1]['CAPACITY']/self.pp[self.turn][self.opt]))
				#else: self.barpp[self.turn][self.opt] = 0
			elif self.equip[self.turn] == 4:
				self.dialog([database.DIALOGS])

			elif self.equip[self.turn] == 5:
				if self.foe[0]['TYPE'] not in ('humanoid','psychic'):
					self.dialog([database.DIALOGS['IRRATIONAL']])

			elif self.equip[self.turn] == 7:
				self.dialog([database.PLAYER[self.turn]['NAME'] + database.BATTLE[14]])
				run = round(random.randint(0,100))
				if run > 49:
					self.dialog([database.BATTLE[16]])
					self.transiction(True, 210)
					self.turn = -1
					self.mnu = 0
					self.hits = 0
					self.tdmg = 0
					self.hpl = 0
					self.tbt = 0
					self.battle = False
					self.opt = 1
					self.player_mov = True
					self.player_rect.x += 150
					self.transiction(False, 0)
				else:
					self.dialog([database.BATTLE[15]])

			self.aim.x = 100 + database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]

		#ENEMIES TURN
		else:
			self.tbt += round(self.btime/10)
			self.btime = 100
			self.mnu = 3
			for i in self.foe:
				if i['HP'] > 0:
					opt = int(random.randint(0,4))
					opt = 0
					if opt > 3:opt = 3
					act=i['HABILITIES'][opt]
					dd=i['NAME'] + database.BATTLE[17] + act[0]
					i['SPRITE']=pygame.image.load('Sprites/' + (i['NAME']).lower() + '_attack.png')
					pl=int(random.randint(0,len(database.PLAYER)-1))
					if act[3] == 2 and self.tatt ==2: act=i['HABILITIES'][0]
					if act[3] == 3 and self.tagi ==2: act=i['HABILITIES'][0]

					if act[3] == 1:
						if act[2] < 0:
							self.turn = pl
							self.ch_sfx.play(pygame.mixer.Sound('SFX/damage_1.wav'))
							database.PLAYER[pl]['HP'] += act[2] + self.pres[pl]
							self.shake(-act[2] * 10, None)
							print(self.pres[pl])
							if database.PLAYER[pl]['HP'] > 0:  minush = int(100/(database.PLAYER[pl]['MAXHP']/database.PLAYER[pl]['HP']))
							else: minush = 0
							#if database.PLAYER[pl]['BARHP'] > 0: minush = int(100/(database.PLAYER[pl]['MAXHP']/database.PLAYER[pl]['BARHP']))
							#else: minush = 0

							while self.barhp[pl] > minush:
								self.draw()
								self.update()
								self.ch_sfx.play(pygame.mixer.Sound('SFX/hp_loss.wav'))
								self.barhp[pl] -= 1
								pygame.time.wait(5)

							self.hpl += act[2]
						elif act[2] > 0:
							i['HP'] += act[2]
					elif act[3] == 2:
						if act[2] < 0:
							if self.tatt[pl] < 2:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/attribute_loss.wav'))
								self.patt[pl] += act[2]
								self.dialog([dd, database.PLAYER[pl]['NAME'] + database.BATTLE[19] + str(act[2]) + database.BATTLE[21]])
								self.tatt[pl] += 1
						elif act[2] > 0:
							act[2] += act[2]
							self.dialog([dd, i['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[21]])
					elif act[3] == 3:
						if act[2] < 0:
							if self.tagi[self.turn]<2:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/attribute_loss.wav'))
								self.pagi[self.turn]+=act[2]
								self.dialog([dd, database.PLAYER[pl]['NAME'] + database.BATTLE[19] + str(act[2]) + database.BATTLE[22]])
								self.tagi[self.turn]+=1
						elif act[2] > 0:
							i['AGILITY']+=act[2]
							self.dialog([dd, i['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[22]])
					elif act[3] == 4:	
						database.PLAYER[pl]['HEALTH']=act[2]
						if act[2] == 1:self.dialog([dd, database.PLAYER[pl]['NAME'] + database.BATTLE[23]])
						if act[2] == 2:self.dialog([dd, database.PLAYER[pl]['NAME'] + database.BATTLE[24]])

					#CHECK DEATH - GAME OVER
					if database.PLAYER[pl]['HP'] <= 0:
						self.ch_sfx.play(pygame.mixer.Sound('SFX/inconscious.wav'))
						self.dialog([database.PLAYER[pl]['NAME'] + database.BATTLE[26]])
					dth = 0
					for d in database.PLAYER:
						if d['HP'] <= 0: dth += 1
					if dth == len(database.PLAYER):
						self.transiction(True, 200)
						self.turn = -1
						self.dialog([database.BATTLE[27]])
						database.load_game(1)
						self.__init__()
						self.transiction(False, 0)
						break

					i['SPRITE']=pygame.image.load('Sprites/' + (i['NAME']).lower() + '_stand.png')

			if self.turn > -1:
				self.turn = 0
				self.mnu = 1
				for i in range(len(database.PLAYER)):
					if self.pres[i] > database.PLAYER[i]['RESISTANCE'][database.PLAYER[i]['LEVEL']]:
						self.pres[i] = database.PLAYER[i]['RESISTANCE'][database.PLAYER[i]['LEVEL']]

	def infohit(self, dmg, col):
		self.dmginfo = dmg
		self.dmgy = 200
		self.dmgcol = col
		hitac = 8

		while hitac > 0:
			self.draw()
			self.update()
			self.dmgy -= hitac
			pygame.time.wait(10)
			hitac -= 1

		while hitac < 8:
			self.draw()
			self.update()
			self.dmgy += hitac
			pygame.time.wait(10)
			hitac += 1

		pygame.time.wait(250)
		self.dmginfo = ''

	def shake(self, ex, tar):
		if tar == None:
			s = 0
			while s < 25:
				pygame.time.wait(10)
				self.displayx = round(random.randint(-ex, ex))
				self.displayy = round(random.randint(-ex, ex))
				self.screen.fill((255, 0, 0))
				self.draw()
				self.update()
				s += 1
			self.displayx = 0
			self.displayy = 0
			self.draw()
			self.update()

		else:
			s = 0
			sx = tar['MASK'].x
			sy = tar['MASK'].y
			while s < 15:
				tar['MASK'].x = sx
				tar['MASK'].y = sy
				pygame.time.wait(1)
				tar['MASK'].x += round(random.randint(-5,5))
				tar['MASK'].y += round(random.randint(-5,5))
				self.screen.fill((255, 0, 0))
				self.draw()
				self.update()
				s += 1
			tar['MASK'].x = sx
			tar['MASK'].y = sy
			self.draw()
			self.update()
     
	def rendermap(self):
		self.map = pytmx.load_pygame('Maps/' + database.MAP + '.tmx')
		self.tilmap = []
		self.en = []
		self.foe = []
		self.npcs = []
		self.vehicles = []
		self.shops = []
		self.portals = []
		self.chests = []

		for i in range(3):
			self.tilmap.append(pygame.Surface((self.map.width * self.map.tilewidth,self.map.height * self.map.tileheight)))
			for x in range(0, self.map.width):
				for y in range(0, self.map.height):
					try:
						tl = self.map.get_tile_image(x, y, i)
						if tl != 0: self.tilmap[0].blit(tl, (x * self.map.tilewidth - self.cam.x, y * self.map.tileheight - self.cam.y))
					except: pass

		for i in range(self.map.properties['NPC']):
			obj = self.map.get_object_by_name('npc_' + str(i))
			self.npcs.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), 60, 60), 'WHO': obj.properties['WHO']})

		for i in range(self.map.properties['SHOP']):
			obj = self.map.get_object_by_name('shop_' + str(i))
			if obj.type == '0': self.shops.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)), 'TYPE': int(obj.type)})
			if obj.type == '1': self.shops.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), 60, 60), 'TYPE': int(obj.type)})

		for i in range(self.map.properties['VEHICLE']):
			obj = self.map.get_object_by_name('vehicle_' + str(i))
			vh = database.VEHICLES[obj.properties['INDEX']].copy()
			vh['RECT'] = pygame.Rect(int(obj.x), int(obj.y), 60, 60)
			vh['INDEX'] = obj.properties['INDEX']
			self.vehicles.append(vh)

		for i in range(self.map.properties['CHEST']):
			obj = self.map.get_object_by_name('chest_' + str(i))
			self.chests.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), 60, 60), 'ITEM': obj.properties['ITEM']})

		for i in range(self.map.properties['PORTAL']):
			obj = self.map.get_object_by_name('portal_' + str(i))
			self.portals.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), 60, 60), 'PX': obj.properties['PX'], 'PY': obj.properties['PY'], 'MAP': obj.properties['MAP']})

		if database.MAP not in ('drugstore','bank','hotel'):
			for i in range(round(random.randint(3,10))):
				self.en.append(database.FREAKS[0].copy())
				self.en[i]['SPRITE'] = pygame.image.load('Sprites/' + (self.en[i]['NAME']).lower() + '_stand.png')
				self.en[i]['RECT'] = pygame.Rect(round(random.randint(0, self.map.width * self.map.tilewidth)),round(random.randint(0, self.map.height * self.map.tileheight)),10,16)
				self.en[i]['MASK'] = pygame.Rect(230,180,44,85)
				self.en[i]['FIGHTING'] = False
				if database.MAP.startswith(self.en[i]['HABITAT']):
					self.en[i]['AGILITY'] += 2
					self.en[i]['HP'] += 5

		if database.MAP.startswith('urban'):
			self.signal = 3

	def minimap(self, mp, x, y, w, h, sg):
		if self.battle == False:
			self.mimap = pygame.Surface((int(self.displayzw/6),int(self.displayzh/4)))
			mim = pygame.image.load('Maps/' + mp +'.png')
			pygame.transform.scale(mim, (50,50))
			self.mimap.blit(mim, (int(-x/8) + 50, int(-y/8) + 50))
			for i in self.en:
				if i['HP'] > 0:
					self.mimap.blit(pygame.image.load('Sprites/mp_anomaly.png'), (int(i['RECT'].x/8 + int(-x/8)) + 45, int(i['RECT'].y/8 + int(-y/8)) + 45))

			return self.mimap

	def radioplay(self, fm, msc):
		pygame.draw.rect(self.scr, (255, 0, 135), pygame.Rect(0,0,180,50))
		self.scr.blit(self.fnt.render('Tocando:', True, (0, 0, 0)), (0, 10))
		self.scr.blit(self.fnt.render(database.RADIO[str(round(fm/10))][msc][:-4], True, (0, 0, 0)), (0, 20))

	def notification(self, txt, col):
		self.nottxt = txt
		self.notcol = col
		self.notx = 0
		w = 0
		while self.notx < 180:
			self.draw()
			self.update()
			self.notx += 20
		while w < 50:
			self.draw()
			self.update()
			pygame.time.wait(1)
			w += 1
		self.notx = 0

	def draw(self):
		self.display.fill((0, 0, 0))
		self.display.blit(self.tilmap[0], (0 - self.cam.x, 0 - self.cam.y))

		#BATTLE
		if self.battle == True:
			self.display.blit(self.bbg, (0, 0))

			for i in self.foe:
				if self.mnu == 2:
					if self.direction == True: i['MASK'].x += i['AGILITY']
					if self.direction == False: i['MASK'].x -= i['AGILITY']

					if i['MASK'].x < 100: self.direction = True
					if i['MASK'].x > 500: self.direction = False

				if i['HP'] > 0: self.display.blit(i['SPRITE'], (i['MASK'].x, i['MASK'].y))

			#BLACK BARS
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

			#ENEMIES COUNT
			if self.winbar == 100:
				ce = 0
				for i in self.foe:
					if i['HP'] > 0: ce += 1
				self.display.blit(self.mininfo.render(str(ce) + '/' + str(len(self.foe)), True, (255,255,255)), (530, 20))

			#PLAYER BARS
				p = 0
				if self.turn >= 0: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(self.turn * 120,0,120,100))
				while p < len(database.PLAYER):
					if p == self.turn: plcol = (0,0,0)
					else: plcol = (255,255,255)
					self.display.blit(self.mininfo.render(database.PLAYER[p]['NAME'].lower(), True, plcol), (10 + p * 120, 10))
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10 + p * 120,40,100,20))
					'''while float(database.PLAYER[p]['BARHP']) > float(database.PLAYER[p]['HP']):
						database.PLAYER[p]['BARHP'] -= database.PLAYER[p]['RESISTANCE'][database.PLAYER[p]['LEVEL']]
						pygame.time.wait(10)
						pygame.draw.rect(self.display, (255, 255, 0), pygame.Rect(10,40,self.barhpl[p],20))'''
					if database.PLAYER[p]['HP'] > database.PLAYER[p]['MAXHP']/5: hpcol = (0, 255, 0)
					elif database.PLAYER[p]['HP'] > 0: hpcol = (255, 0, 0)
					if database.PLAYER[p]['HP'] > 0: pygame.draw.rect(self.display, hpcol, pygame.Rect(10 + p * 120,40,self.barhp[p],20))

					#pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10 + p * 120,70,100,20))
					if self.equip[p] < len(self.pp[p]) - 1:
						if database.EQUIPMENT[p][self.equip[p]] != '_':
							self.display.blit(self.monotype.render(str(self.pp[p][self.equip[p]]) + '/' + str(database.EQUIPMENT[p][self.equip[p]][1]['CAPACITY']), True, plcol), (10 + p * 120, 70))
						#pygame.draw.rect(self.display, (0, 100, 255), pygame.Rect(10 + p * 120,70,self.barpp[p][self.opt],20))
					p += 1

				if self.turn < len(database.PLAYER) and self.turn!=-1:
					#TIME BAR
					if self.mnu < 3:
						pygame.draw.rect(self.display, (255, 0, 255), pygame.Rect(0,302,int(600/(100/self.btime)),10))
						self.btime -= 0.5
						if self.btime == 0:
							self.turn = len(database.PLAYER)
							self.fight()

					#OPTIONS
					if self.mnu == 1:
						x=0
						for i in database.EQUIPMENT[self.turn]:
							if self.equip[self.turn] == x: pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(118+x*35,338,32,32))
							else:pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(118+x*35,338,32,32))
							pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(120+x*35,340,28,28))
							if i[0] != '_': self.display.blit(pygame.image.load('Sprites/it_' + i[0] + '.png'), (120+x*35, 340))
							x+=1

						if self.equip[self.turn] == 4: pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(304,338,32,32))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(304,338,32,32))
						pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(306,340,28,28))
						self.display.blit(pygame.image.load('Sprites/e_tactical.png'), (304, 340))

						if self.equip[self.turn] == 5: pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(339,338,32,32))
						pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(341,340,28,28))
						#else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(339,338,32,32))
						self.display.blit(pygame.image.load('Sprites/e_talk.png'), (339, 340))

						if self.equip[self.turn] == 6: pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(374,338,32,32))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(374,338,32,32))
						pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(376,340,28,28))
						self.display.blit(pygame.image.load('Sprites/e_guard.png'), (374, 340))

						if self.equip[self.turn] == 7: pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(409,338,32,32))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(409,338,32,32))
						pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(411,340,28,28))
						self.display.blit(pygame.image.load('Sprites/e_run.png'), (409, 340))

					#AIM BAR
					elif self.mnu == 2:
						if self.equip[self.turn] < 4:
							self.aim.x += 20 - database.PLAYER[self.turn]['AGILITY'][database.PLAYER[self.turn]['LEVEL']]
							if self.aim.x > 500 - database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]: self.aim.x = 100 + database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]
							self.display.blit(pygame.image.load('Sprites/aim.png'), (self.aim.x-15, self.aim.y))

			#INFOHIT
			if self.dmginfo != '':
				pygame.draw.rect(self.display, self.dmgcol, pygame.Rect(self.aim.x,self.dmgy,len(self.dmginfo) * 20,22))
				self.display.blit(self.mininfo.render(self.dmginfo, True, (0,0,0)), (self.aim.x, self.dmgy))

			if self.winbar == 210:
				for i in range(len(database.PLAYER)):
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,120 + i * 30,100,20))
					if database.PLAYER[i]['XP'] > 0: pygame.draw.rect(self.display, (0, 255, 100), pygame.Rect(10,120 + i * 30,self.barxp[i],20))
		
		#OBJECTS
		elif self.battle == False:
			self.display.blit(self.player_sprite[self.player_gif//len(self.player_sprite)], (self.player_rect.x - self.cam.x, self.player_rect.y - self.cam.y))

			for i in range(len(self.en)):
				if self.en[i]['HP'] > 0: self.enemy(i)
			for i in self.npcs:
				self.npc(i['RECT'].x,i['RECT'].y,i['WHO'])
			for i in self.shops:
				self.shop(i['RECT'].x,i['RECT'].y,i['RECT'].width,i['RECT'].height,i['TYPE'])
			for i in self.vehicles:
				self.vehicle(i['RECT'].x,i['RECT'].y,i['INDEX'])
			for i in self.chests:
				self.chest(i['RECT'].x,i['RECT'].y,i['ITEM'])
			for i in self.portals:
				self.portal(i['RECT'].x,i['RECT'].y,i['PX'],i['PY'],i['MAP'])

			#MINI MAP
			try:
				pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,self.displayzh - (106 * int(self.displayzh/400)),106 * int(self.displayzw/600),106 * int(self.displayzh/400)))
				self.display.blit(self.minimap(database.MAP, self.player_rect.x, self.player_rect.y, self.displayzw, self.displayzh, self.signal), (3 * int(self.displayzh/400),self.displayzh - (103 * int(self.displayzh/400))))
				self.display.blit(pygame.image.load('Sprites/mp_player.png'), (48 * int(self.displayzh/400),self.displayzh - (59 * int(self.displayzh/400))))
			except: pass

			#DRIVING BARS
			if self.driving > 0:
				pygame.draw.rect(self.display, (10,10,10), pygame.Rect(20,20,100,20))
				if database.GAS >= 1: pygame.draw.rect(self.display, (255,155,66), pygame.Rect(20,20,int(100/(self.vehicles[self.driving - 1]['CAPACITY']/round(database.GAS))),20))
				pygame.draw.rect(self.display, (10,10,10), pygame.Rect(20,42,100,20))
				if self.player_spd > 0: pygame.draw.rect(self.display, (0,255,0), pygame.Rect(20,42,int(100/(20/self.player_spd)),20))

		#INVENTORY
		if self.inventory == True:
			self.display.blit(self.inv.show(self.opt, self.lopt, self.mnu, self.invfade), (100,60))
			while self.invfade < 170:
				self.invfade += 1

		#SHOP
		if self.shp == True:
			if self.mnu == 0:
				shp = menu.Shop()
				self.display.blit(shp.products(self.opt, self.lopt, self.products), (100,60))
			if self.mnu == 1:
				shp = menu.Shop()
				self.display.blit(shp.buy(self.opt, self.lopt, self.basket), (100,60))
			if self.mnu == 2:
				shp = menu.Shop()
				self.display.blit(shp.bank(self.opt, self.lopt, self.mnu), (100,60))
			if self.mnu == 3:
				shp = menu.Shop()
				self.display.blit(shp.hotel(self.opt, self.lopt), (100,60))

		#PHONE
		if self.phone > 0:
			self.display.blit(pygame.image.load('Backgrounds/phone.png'), (200, 30))
		if self.phone == 1: self.display.blit(self.phn.apps(database.TIME, database.DATE, self.signal, database.BATTERY, self.opt, self.lopt), (210,60))
		elif self.phone == 2: self.display.blit(self.phn.map(database.MAP, self.opt, self.lopt, self.mnu, self.signal), (210,60))
		elif self.phone == 3: self.display.blit(self.phn.contacts(self.opt, self.lopt, self.mnu), (210,60))
		elif self.phone == 4: self.display.blit(self.phn.email(self.opt, self.lopt, self.mnu, self.signal), (210,60))
		elif self.phone == 5: self.display.blit(self.phn.news(self.lopt, self.mnu, self.signal), (210,60))
		elif self.phone == 6: self.display.blit(self.phn.radio(self.fm, self.msc), (210,60))
		elif self.phone == 7: self.display.blit(self.phn.camera(), (210,60))
		elif self.phone == 8: self.display.blit(self.phn.bestiary(self.opt, self.lopt, self.mnu, self.signal), (210,60))
		elif self.phone == 9: self.display.blit(self.phn.task(self.opt, self.lopt, self.mnu), (210,60))
		elif self.phone == 10: self.display.blit(self.phn.status(self.opt), (210,60))
		elif self.phone == 11: self.display.blit(self.phn.achievements(self.opt, self.signal), (210,60))
		elif self.phone == 12: self.display.blit(self.phn.ranking(self.opt, self.signal), (210,60))
		elif self.phone == 13: self.display.blit(self.phn.help(self.lopt, self.mnu), (210,60))
		elif self.phone == 14: self.display.blit(self.phn.settings(self.opt), (210,60))
		elif self.phone == 15: self.display.blit(self.phn.info(self.lopt), (210,60))
		elif self.phone == 16: self.display.blit(self.phn.save(self.lopt, self.signal), (210,60))

		#BLACK BARS
		if self.battle == False and self.winbar > 0:
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

		#DIALOG
		if self.dlgfa < 500:
			pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(50,30,500 - self.dlgfa,100))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(55,35,490 - self.dlgfa,90))
			if self.dlg != []:
				if self.lopt > 0:
					pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(70,30 + self.lopt * 20,460,20))
				y = 0
				for i in self.dlg:
					if (self.lopt - 1) * 20 == y: self.display.blit(self.monotype.render(i, True, (0, 0, 0)), (70, 50 + y))
					else: self.display.blit(self.monotype.render(i, True, (255, 255, 255)), (70, 50 + y))
					y += 20
		
		'''if self.dlg != []:
			y = 0
			for i in self.dlg:
				pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(20,200 - y,500,30))
				self.display.blit(self.monotype.render(i, True, (0, 0, 0)), (20, 200 - y))
				y += 35'''

		#NOTIFICATIONS
		if self.notx > 0:
			pygame.draw.rect(self.display, (0,0,0), pygame.Rect(-183 + self.notx,27,186,56))
			pygame.draw.rect(self.display, self.notcol, pygame.Rect(-180 + self.notx,30,180,50))
			self.display.blit(self.monotype.render(self.nottxt, True, (0, 0, 0)), (-170 + self.notx, 40))

		#CAMERA
		self.cam.x += int((self.player_rect.x  - self.cam.x - self.displayzw/2)/15)
		self.cam.y += int((self.player_rect.y  - self.cam.y - self.displayzh/2)/15)
		if self.cam.x < 0: self.cam.x = 0
		if self.cam.y < 0: self.cam.y = 0
		if self.cam.x > (self.map.width * self.map.tilewidth) - self.displayzw: self.cam.x = (self.map.width * self.map.tilewidth) - self.displayzw
		if self.cam.y > (self.map.height * self.map.tileheight) - self.displayzh: self.cam.y = (self.map.height * self.map.tileheight) - self.displayzh

		self.screen.blit(pygame.transform.scale(self.display, (1200, 800)), (self.displayx, self.displayy))

	def update(self):
		#ANIMATION
		if self.player_mov == True:
			self.player_gif +=1
			if self.player_gif == 60//len(self.player_sprite): self.player_gif = 0
		else: self.player_gif = 0

		#DATETIME
		database.TIME[2] +=1
		if database.TIME[2] == 60:
			database.TIME[1] += 1
			database.TIME[2] = 0

		if database.TIME[1] == 60:
			database.TIME[0] += 1
			database.TIME[1] = 0

		if database.TIME[0] == 24:
			database.DATE[0] += 1
			database.TIME[0] = 0

		if database.DATE[0] == 30:
			database.DATE[1] += 1
			database.DATE[0] = 1

		if database.DATE[1] == 12:
			database.DATE[2] += 1
			database.DATE[1] = 1

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