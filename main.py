# -*- coding: utf-8 -*-
#if LANG == 'PT': import database_PT as database
#if LANG == 'EN': import database_EN as database
import database_PT as database

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
		self.sleepin = False

		#MIXER
		pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
		self.ch_sfx = pygame.mixer.Channel(0)
		self.ch_sfx.set_volume(database.SFX)
		self.ch_msc = pygame.mixer.Channel(1)
		self.ch_msc.set_volume(database.MSC)
		self.ch_ton = pygame.mixer.Channel(2)
		self.ch_ton.set_volume(database.SFX)
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
		print(database.PARTY)
		print(database.FORMATION)
		for i in database.PARTY[database.FORMATION]:
			self.equip.append(0)
			self.pp.append([])
			self.barpp.append([])
			self.barhp.append(int(100/(database.CHARACTERS[i]['VITALITY'][database.CHARACTERS[i]['LEVEL']]/database.CHARACTERS[i]['HP'])))
			self.barhpl.append(100)
			if database.CHARACTERS[i]['XP'] > 0: self.barxp.append(int(100/(database.CHARACTERS[i]['MAXXP']/database.CHARACTERS[i]['XP'])))
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
		self.products = []
		self.extract = [0,0,0,0,0,0]
		self.winbar = 210
		self.fm = 0
		self.msc = 0
		self.signal = 0
		self.nottxt = ''
		self.notcol = (0,0,0)
		self.notx = 0

		#PLAYER VARIABLES
		self.player_rect = pygame.Rect(database.PX,database.PY,20,32)
		self.player_spd = 3
		self.player_sprite = database.SPRITES['DOWN_Sid']
		self.player_gif = 1
		self.player_mov = False
		self.player_color = (100, 100, 100)

		#LOADING MAP
		self.en = []
		self.foe = []
		self.fig = []
		self.mrc = []
		self.npcs = []
		self.vehicles = []
		self.shops = []
		self.portals = []

		#self.start()
		self.rendermap('urban_')
		self.transiction(False, 0)

	def start(self):
		for i in range(50):
			pygame.time.wait(10)
			self.update()
		y = 0
		for i in database.DISCLAIMER:
			self.display.blit(self.monotype.render(i, True, (240,240,240)), (180, 100 + y))
			y += 20
		self.screen.blit(pygame.transform.scale(self.display, (1200, 800)), (self.displayx, self.displayy))
		for i in range(350):
			pygame.time.wait(10)
			self.update()

		self.display.fill((0, 0, 0))
		self.display.blit(self.monotype.render(database.ABOUT[1], True, (240,240,240)), (420, 350))
		self.screen.blit(pygame.transform.scale(self.display, (1200, 800)), (self.displayx, self.displayy))
		for i in range(100):
			pygame.time.wait(10)
			self.update()

	def enemy(self, en):
		if self.colide(self.en[en]['RECT'], self.cam) and self.battle == False:
			if self.en[en]['RECT'].x - self.cam.x < self.player_rect.x - self.cam.x: self.en[en]['RECT'].x += 3
			if self.en[en]['RECT'].x - self.cam.x > self.player_rect.x - self.cam.x: self.en[en]['RECT'].x -= 3
			if self.en[en]['RECT'].y - self.cam.y < self.player_rect.y - self.cam.y: self.en[en]['RECT'].y += 3
			if self.en[en]['RECT'].y - self.cam.y > self.player_rect.y - self.cam.y: self.en[en]['RECT'].y -= 3

		if self.colide(self.en[en]['RECT'], self.player_rect) == True and self.winbar == 0:
			if self.en[en]['FIGHTING'] == False:
				if self.en[en]['TYPE'] != 'mercenary': self.foe.append(self.en[en])
				else: self.mrc.append(self.en[en])
				self.en[en]['FIGHTING'] = True
				if len(self.foe) == 1: self.turn = -1; self.fight()

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/' + (self.en[0]['NAME']).lower() + '_mini.png'), (self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y))

	def npc(self, x, y, w, h, ndg):
		if w == 40 and h == 40: rect = pygame.Rect(x - 5,y - 5,w,h)
		elif w == 0 and h == 0: rect = pygame.Rect(x - 5,y - 5,40,40)
		else: rect = pygame.Rect(x - 5,y - 5,w,h)

		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[database.ACT]:
					print(self.dlgfa)
					if self.dlgfa > 0:
						if isinstance(ndg, int): self.dialog(database.DIALOGS['NPC_'+str(ndg)][database.PARTY[database.FORMATION][0]].copy())
						else: self.dialog(database.DIALOGS[ndg][database.PARTY[database.FORMATION][0]].copy())
			if self.battle == False: self.display.blit(pygame.image.load('Sprites/arw.png'), (rect.x - self.cam.x + int(rect.width/2) - 5, rect.y - self.cam.y - int(rect.height/2)))

		pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False:
			if w == 0 and h == 0: self.display.blit(pygame.image.load('Sprites/npc.png'), (rect.x - self.cam.x + 10, rect.y - self.cam.y + 5))

	def vehicle(self, x, y, vh):
		rect = pygame.Rect(x - 5,y - 5,60,40)
		if self.driving == int(vh[-1]) + 1:
			self.player_rect.x = rect.x
			self.player_rect.y = rect.y

		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[database.ACT] and self.driving == 0:
					trigger = True
					self.driving = int(vh[-1]) + 1
					self.displayzw = 1200
					self.displayzh = 800
					self.display = pygame.Surface((1200, 800))
			if self.battle == False: self.display.blit(pygame.image.load('Sprites/arw.png'), (rect.x - self.cam.x + int(rect.width/2) - 5, rect.y - self.cam.y - int(rect.height/2)))

		pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False: self.display.blit(pygame.image.load('Sprites/' + vh + '_walkL.png'), (rect.x - self.cam.x + 10, rect.y - self.cam.y + 10))

	def shop(self, x, y, w, h, t, ind):
		if t == 0: rect = pygame.Rect(x,y,w,h)
		elif t == 3: rect = pygame.Rect(x,y + 30,20,20)
		elif t == 4: rect = pygame.Rect(x,y + 30,35,20)
		elif t == 5: rect = pygame.Rect(x - 5,y - 5,35,60)
		else: rect = pygame.Rect(x - 5,y - 5,40,40)

		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[database.ACT]:
					if t == 1 and self.basket == []:
						if self.dlgfa > 0: self.dialog(database.DIALOGS['CASHIER ' + ind][0].copy())
					elif t == 5: self.sleepin = not self.sleepin
					else:
						print(self.basket)
						print(self.products)
						self.shp = True
						self.lopt = 0
						self.opt = 1
						self.mnu = t
						if t == 0 and self.products == []:
							for i in database.PRODUCTS[int(ind)]:
								self.products.append(database.ITEMS[i].copy())
						if t == 3: self.extract = [0,0,0,0,0,0]

			if t == 4 and self.player_spd == 0 and self.driving > 0:
				while database.GAS < self.vehicles[self.driving - 1]['CAPACITY']:
					database.GAS += 1
					self.draw()
					pygame.time.wait(10)

			if self.battle == False: self.display.blit(pygame.image.load('Sprites/arw.png'), (rect.x - self.cam.x + int(rect.width/2) - 5, rect.y - self.cam.y - int(rect.height/2)))

		pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False:
			if t == 1 or t == 2: self.display.blit(pygame.image.load('Sprites/npc.png'), (rect.x - self.cam.x + 10, rect.y - self.cam.y + 5))
			if t == 3: self.display.blit(pygame.image.load('Sprites/atm.png'), (rect.x - self.cam.x, rect.y - self.cam.y - 30))
			if t == 4: self.display.blit(pygame.image.load('Sprites/refuel.png'), (rect.x - self.cam.x, rect.y - self.cam.y - 30))
			if t == 5:
				self.display.blit(pygame.image.load('Sprites/bed.png'), (rect.x - self.cam.x + 5, rect.y - self.cam.y + 5))
				if self.sleepin == True: self.display.blit(pygame.image.load('Sprites/char_0_rest.png'), (rect.x - self.cam.x + 5, rect.y - self.cam.y + 5))

	def portal(self, x, y, px, py, mp, ot, ct):
		rect = pygame.Rect(x,y,20,40)
		if self.colide(self.player_rect, rect) == True and self.winbar == 0:
			if ot != None:
				if database.TIME[0] >= ot[0] and database.TIME[0] <= ct[0]: 
					if database.TIME[1] > ot[1] and database.TIME[1] < ct[1]: 
						self.player_mov = False
						self.ch_sfx.play(pygame.mixer.Sound('SFX/door_open.wav'))
						self.transiction(True, 210)
						self.player_rect.x = px
						self.player_rect.y = py
						self.rendermap(mp)
						self.ch_sfx.play(pygame.mixer.Sound('SFX/door_close.wav'))
						self.transiction(False, 0)
			else:
				self.player_mov = False
				self.ch_sfx.play(pygame.mixer.Sound('SFX/door_open.wav'))
				self.transiction(True, 210)
				self.player_rect.x = px
				self.player_rect.y = py
				self.rendermap(mp)
				self.ch_sfx.play(pygame.mixer.Sound('SFX/door_close.wav'))
				self.transiction(False, 0)

		pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
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
				if self.turn == len(database.PARTY[database.FORMATION]): self.fight()

				if self.mnu == 2:
					#DEBUG
					if self.pressed[database.UP]: database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['LEVEL'] += 1

					if self.pressed[database.ACT]:
						self.fight()
						self.turn += 1
						self.mnu = 1
						if self.turn == len(self.fig): self.fight()

				elif self.mnu == 1:
					if self.pressed[database.LEFT]: self.equip[self.turn] -=1
					if self.pressed[database.RIGHT]: self.equip[self.turn] +=1
				
					if self.equip[self.turn] < 0: self.equip[self.turn] = 7
					if self.equip[self.turn] > 7: self.equip[self.turn] = 0

					if self.pressed[database.ACT]:
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
							self.dialog([self.fig[self.turn]['NAME'] + ' está em guarda'])
							self.turn += 1
							if self.turn == len(self.fig): self.fight()
						elif self.equip[self.turn] == 7:
							self.fight()
							if self.turn != -1:
								self.turn = len(self.fig)
								self.fight()

			#SHOP OPTIONS
			if self.shp == True:
				if self.pressed[database.LEFT]: self.opt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
				if self.pressed[database.RIGHT]: self.opt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
				if self.pressed[database.UP]: self.lopt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
				if self.pressed[database.DOWN]: self.lopt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

				if self.mnu == 0:
					if self.pressed[database.ACT]:
						if self.lopt < len(self.products):
							for i in range(self.opt): self.basket.append(self.products[self.lopt].copy())
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))
						else:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 10
					if self.opt > 10: self.opt = 1
					if self.lopt < 0: self.lopt = len(self.products)
					if self.lopt > len(self.products): self.lopt = 0

				if self.mnu == 1:
					if self.pressed[database.ACT]:
						if self.lopt == 0:
							for i in self.basket:
								bb = False
								for j in database.INVENTORY[0]:
									for x in j:
										if x == '_':
											bb = True
								if bb == True:
									self.ch_sfx.play(pygame.mixer.Sound('SFX/buy.wav'))
									database.MONEY -= i[2]
									self.basket.remove(i)
									self.inv.add(i[0])
						else:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 1
					if self.lopt < 0: self.lopt = 1
					if self.lopt > 1: self.lopt = 0

				if self.mnu == 2:
					if self.pressed[database.ACT]:
						if self.lopt == len(self.products):
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))
							self.shp = False
							self.lopt = 0
						else:
							bb = False
							for j in database.INVENTORY[0]:
								for x in j:
									if x == '_':
										bb = True
							if bb == True:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/buy.wav'))
								database.MONEY -= self.products[self.lopt][2]
								self.inv.add(self.products[self.lopt][0])

					if self.opt < 1: self.opt = 1
					if self.lopt < 0: self.lopt = len(self.products)
					if self.lopt > len(self.products): self.lopt = 0

				if self.mnu == 11 or self.mnu == 12:
					if self.pressed[database.ACT]:
						self.ch_sfx.play(pygame.mixer.Sound('SFX/cash_get.wav'))
						self.shp = False
						self.opt = 0
						self.lopt = 0

					if self.opt < 0: self.opt = 5
					if self.opt > 5: self.opt = 0
					if self.lopt < 0: self.lopt = 9
					if self.lopt > 9: self.lopt = 0

					if self.pressed[database.LEFT]: self.lopt = self.extract[self.opt]
					if self.pressed[database.RIGHT]: self.lopt = self.extract[self.opt]
					
					self.extract[self.opt] = self.lopt

					if self.pressed[database.UP]:
						if self.mnu == 11:
							database.ATM -= 1
							database.MONEY += 1
						if self.mnu == 12:
							database.ATM += 1
							database.MONEY -= 1

					if self.pressed[database.DOWN]:
						if self.mnu == 11:
							database.ATM += 1
							database.MONEY -= 1
						if self.mnu == 12:
							database.ATM -= 1
							database.MONEY += 1
					'''if self.pressed[database.UP]:
						if self.mnu == 11:
							database.ATM -= int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))
							database.MONEY += int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))
						if self.mnu == 12:
							database.ATM += int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))
							database.MONEY -= int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))'''

				if self.mnu == 3:
					if self.pressed[database.ACT]:
						if self.lopt == 0:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))
							self.mnu = 11
							self.lopt = 0
							self.opt = 5
						if self.lopt == 1:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))
							self.mnu = 12
							self.lopt = 0
							self.opt = 5
						if self.lopt == 2:
							self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_back.wav'))
							self.shp = False
							self.lopt = 0

					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

			#INVENTORY OPTIONS
			if self.pressed[database.BAG] and self.phone == 0:
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
					if self.pressed[database.LEFT]: self.opt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[database.RIGHT]: self.opt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[database.UP]: self.lopt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
					if self.pressed[database.DOWN]: self.lopt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

					if self.pressed[database.ACT]:
						self.mnu += 1
						self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_go.wav'))

					if self.opt < 0: self.opt = 0
					if self.lopt < 1: self.lopt = 1

				elif self.mnu == 1:
					if self.pressed[database.UP]: self.mnu -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
					if self.pressed[database.DOWN]: self.mnu +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

					if self.pressed[database.ACT]:
						if self.mnu == 1:
							if database.INVENTORY[0][self.lopt][self.opt][3] == 9:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/heal.wav'))
								database.CHARACTERS[database.PARTY[database.FORMATION][0]]['HP'] += database.INVENTORY[0][self.lopt][self.opt][4]
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
					if self.pressed[database.LEFT]: self.opt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[database.RIGHT]: self.opt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_hor.wav'))
					if self.pressed[database.UP]: self.lopt -=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))
					if self.pressed[database.DOWN]: self.lopt +=1 ; self.ch_sfx.play(pygame.mixer.Sound('SFX/menu_ver.wav'))

					if self.pressed[database.ACT]:
						self.inv.move(ii,ij,inv,self.opt,self.lopt,1)
						self.mnu = 1

					if self.opt < 0: self.opt = 0
					if self.lopt < 1: self.opt = 1

			#PHONE OPTIONS
			if self.pressed[database.PHONE] and self.inventory == False:
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
					if self.pressed[database.UP]: self.lopt -=1
					if self.pressed[database.DOWN]: self.lopt +=1
					if self.pressed[database.LEFT]: self.opt -=1
					if self.pressed[database.RIGHT]: self.opt +=1

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = 4
					if self.lopt > 4: self.lopt = 0

					if self.pressed[database.ACT]:
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
						if self.pressed[database.UP]: self.lopt -=1
						if self.pressed[database.DOWN]: self.lopt +=1
						if self.pressed[database.LEFT]: self.opt -=1; self.lopt = 0
						if self.pressed[database.RIGHT]: self.opt +=1; self.lopt = 0

					if self.pressed[database.ACT]:
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
						if self.pressed[database.UP]: self.lopt -=1
						if self.pressed[database.DOWN]: self.lopt +=1
						if self.pressed[database.LEFT]: self.opt -=1; self.lopt = 0
						if self.pressed[database.RIGHT]: self.opt +=1; self.lopt = 0

					if self.pressed[database.ACT] and self.signal > 0:
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
						if self.pressed[database.UP]: self.lopt -=1
						if self.pressed[database.DOWN]: self.lopt +=1

					if self.pressed[database.ACT]:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.lopt < 0: self.lopt = 3
					if self.lopt > 3: self.lopt = 0

				elif self.phone == 6:
					if self.pressed[database.UP]: self.lopt -=1
					if self.pressed[database.DOWN]: self.lopt +=1

					if self.lopt < 0: self.lopt = len(database.RADIO[str(round(self.fm/10))]) - 1
					if self.lopt > len(database.RADIO[str(round(self.fm/10))]) - 1: self.lopt = 0

					if self.pressed[database.ACT]:
						pygame.mixer.music.load('Songs/FM_' + str(round(self.fm/10)) + '/' + database.RADIO[str(round(self.fm/10))][self.lopt])
						pygame.mixer.music.play(-1)

				elif self.phone == 8 and self.signal > 0:
					if self.pressed[database.UP]: self.lopt -=1
					if self.pressed[database.DOWN]: self.lopt +=1

					if self.pressed[database.ACT]:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.mnu == 0:
						if self.lopt < 0: self.lopt = len(database.BESTIARY) - 1
						if self.lopt > len(database.BESTIARY) - 1: self.lopt = 0

					if self.mnu > 0:
						if self.pressed[database.LEFT]: self.mnu = 1
						if self.pressed[database.RIGHT]: self.mnu = 2

						if self.lopt < 0: self.lopt = 3
						if self.lopt > 3: self.lopt = 0

				elif self.phone == 9:
					if self.pressed[database.UP]: self.lopt -=1
					if self.pressed[database.DOWN]: self.lopt +=1
					if self.pressed[database.LEFT]: self.opt -=1
					if self.pressed[database.RIGHT]: self.opt +=1

					if self.pressed[database.ACT]:
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
					if self.pressed[database.LEFT]: self.opt -=1
					if self.pressed[database.RIGHT]: self.opt +=1

					if self.opt < 0: self.opt = len(database.PARTY[database.FORMATION]) - 1
					if self.opt > len(database.PARTY[database.FORMATION]) - 1: self.opt = 0

				elif self.phone == 11:
					if self.pressed[database.UP]: self.lopt -=1
					if self.pressed[database.DOWN]: self.lopt +=1

					if self.lopt < 0: self.lopt = len(database.ACHIEVEMENTS) - 1
					if self.lopt > len(database.ACHIEVEMENTS) - 1: self.lopt = 0

				elif self.phone == 13:
					if self.mnu == 0:
						if self.pressed[database.UP]: self.lopt -=1
						if self.pressed[database.DOWN]: self.lopt +=1

					if self.pressed[database.ACT]:
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.lopt < 0: self.lopt = len(database.MANUAL) - 1
					if self.lopt > len(database.MANUAL) - 1: self.lopt = 0

				elif self.phone == 15:
					if self.pressed[database.UP]: self.lopt -=1
					if self.pressed[database.DOWN]: self.lopt +=1

					if self.lopt < 0: self.lopt = 0
					if self.lopt > 1: self.lopt = 1

					if self.pressed[database.ACT]:
						if self.lopt == 0:
							webbrowser.get('windows-default').open('twitter.com/kaixtr')
						if self.lopt == 1:
							webbrowser.get('windows-default').open('github.com/kaixtr')

				elif self.phone == 16 and self.signal > 0:
					if self.pressed[database.UP]: self.lopt -=1
					if self.pressed[database.DOWN]: self.lopt +=1

					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

					if self.pressed[database.ACT] and self.signal > 0:
						self.ch_sfx.play(pygame.mixer.Sound('SFX/save.wav'))
						database.PX = self.player_rect.x
						database.PY = self.player_rect.y
						database.ID = self.lopt
						database.save_data()

			'''if self.driving > 0:
				if self.pressed[database.LEFT]: self.dridir += 1
				if self.pressed[database.RIGHT]: self.dridir -= 1'''

		if self.phone == 2:
			if self.pressed[database.UP]: self.lopt -= 3
			if self.pressed[database.DOWN]: self.lopt += 3
			if self.pressed[database.LEFT]: self.opt -= 3
			if self.pressed[database.RIGHT]: self.opt += 3
			if self.pressed[database.ACT]: self.mnu +=5
			if self.pressed[database.BAG]: self.mnu -=5

			if self.opt < -self.map.width: self.opt = -self.map.width
			if self.opt > self.map.width: self.opt = self.map.width
			if self.lopt < -self.map.height: self.lopt = -self.map.height
			if self.lopt > self.map.height: self.lopt = self.map.height
			if self.mnu < 100: self.mnu = 100
			if self.mnu > 500: self.mnu = 500

		elif self.phone == 4:
			if self.mnu > 0:
				if self.pressed[database.UP]: self.mnu -=1
				if self.pressed[database.DOWN]: self.mnu +=1

				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 5:
			if self.mnu > 0:
				if self.pressed[database.UP]: self.mnu -=1
				if self.pressed[database.DOWN]: self.mnu +=1

				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 6:
			if self.pressed[database.LEFT]: self.fm -=1; self.lopt = 0
			if self.pressed[database.RIGHT]: self.fm +=1; self.lopt = 0

			if self.fm < 0: self.fm = 180
			if self.fm > 180: self.fm = 0

		elif self.phone == 13:
			if self.mnu > 0:
				if self.pressed[database.UP]: self.mnu -=1
				if self.pressed[database.DOWN]: self.mnu +=1
						
				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		#PLAYER MOVEMENT
		if self.battle == False and self.inventory == False and self.phone == 0 and self.shp == False and self.sleepin == False:
			self.player_mov = False
			self.pressed = pygame.key.get_pressed()
			if self.driving == 0:
				if self.pressed[database.UP]: self.player_mov = True; self.player_rect.y -= self.player_spd; self.player_sprite = database.SPRITES['UP_Sid']
				elif self.pressed[database.DOWN]: self.player_mov = True; self.player_rect.y += self.player_spd; self.player_sprite = database.SPRITES['DOWN_Sid']
				if self.pressed[database.LEFT]: self.player_mov = True; self.player_rect.x -= self.player_spd; self.player_sprite = database.SPRITES['LEFT_Sid']
				elif self.pressed[database.RIGHT]: self.player_mov = True; self.player_rect.x += self.player_spd; self.player_sprite = database.SPRITES['RIGHT_Sid']

				if self.pressed[database.ACT]: self.player_spd = 6
				else: self.player_spd = 3

			#DRIVING MOVEMENT
			if self.driving > 0:
				if database.GAS > 0:
					if self.pressed[database.UP]: self.player_mov = True; self.dridir = 0
					elif self.pressed[database.DOWN]: self.player_mov = True; self.dridir = 1
					elif self.pressed[database.LEFT]: self.player_mov = True; self.dridir = 2
					elif self.pressed[database.RIGHT]: self.player_mov = True; self.dridir = 3
					else: self.player_mov = False

				if self.dridir == 0: self.vehicles[self.driving - 1]['RECT'].y -= self.player_spd; self.player_sprite = database.SPRITES['UP_Sid']
				elif self.dridir == 1: self.vehicles[self.driving - 1]['RECT'].y += self.player_spd; self.player_sprite = database.SPRITES['DOWN_Sid']
				elif self.dridir == 2: self.vehicles[self.driving - 1]['RECT'].x -= self.player_spd; self.player_sprite = database.SPRITES['LEFT_Sid']
				elif self.dridir == 3: self.vehicles[self.driving - 1]['RECT'].x += self.player_spd; self.player_sprite = database.SPRITES['RIGHT_Sid']

				if self.pressed[database.ACT]:
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
		self.player_mov = False
		txt = tx
		tid = 0
		did = 0

		while tid < len(txt):
			self.dlg.append('')
			if isinstance(txt[tid], str):
				while self.dlgfa > 0:
					self.dlgfa -= 50
					self.draw()
					pygame.time.wait(2)

				else:
					for i in txt[tid]:
						self.ch_sfx.stop()
						self.ch_sfx.play(pygame.mixer.Sound('SFX/voice_mid.wav'))
						self.dlg[did] += i
						self.draw()
						pygame.time.wait(database.SPEED)
					self.wait()
					did += 1
			else:
				if txt[tid] == 0:
					self.dlg = []

				elif txt[tid][0] == 0 and self.notx == 0:
					self.inv.add(txt[tid][1])
					database.MONEY -= txt[tid][2]
					self.ch_sfx.play(pygame.mixer.Sound('SFX/item_get.wav'))
					self.notification('Adquiriu ' + txt[tid][1],(255, 255, 255))
					self.dlg = []

				elif txt[tid][0] == 1 and self.notx == 0:
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
							self.mnu = 1
							txt.insert(tid + 1, [2,'stop'])
							txt.insert(tid + 1, 0)
							for i in self.phn.call(str(database.CONTACTS[txt[tid][1]][1]),0,False,False)[-1:0:-1]:
								txt.insert(tid + 1, i)
							self.dlg = []
					else:
						self.phone = 0
						self.mnu = 0
						self.dlg = []

				elif txt[tid][0] == 3 and self.notx == 0:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/notification.wav'))
					database.INBOX.append(database.EMAILS[txt[tid][1]])
					self.notification('Novo email',(255, 221, 0))
					self.dlg = []

				elif txt[tid][0] == 4 and self.notx == 0:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/notification.wav'))
					database.TASKS.append([txt[tid][1], False])
					self.notification('Nova tarefa disponível',(255, 123, 0))
					self.dlg = []

				elif txt[tid][0] == 5 and self.notx == 0:
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

				elif txt[tid][0] == 6 and self.notx == 0:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/achievement.wav'))
					database.ACHIEVEMENTS[txt[tid][1]][2] = True
					self.notification(database.ACHIEVEMENTS[txt[tid][1]][0],(255, 191, 0))
					self.dlg = []

				elif txt[tid][0] == 7 and self.notx == 0:
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
			pygame.time.wait(2)

	def diopt(self, ln):
		self.lopt = 1
		trigger = True
		self.draw()
		while trigger:
			for event in pygame.event.get():
				pygame.time.Clock().tick(60)
				self.draw()
				self.pressed = pygame.key.get_pressed()
				if self.pressed[database.UP]:
					if self.lopt > 1: self.lopt -= 1
				if self.pressed[database.DOWN]:
					if self.lopt < ln: self.lopt += 1
				if self.pressed[database.ACT]:
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
				self.draw()
		else:
			while self.winbar < limit:
				self.winbar += 5
				self.draw()

	def fight(self):
		#BATTLE START
		if self.turn == -1:
			print('yes')
			self.ch_ton.play(pygame.mixer.Sound('SFX/battle_foe.wav'))
			for i in range(20):
				pygame.time.wait(10)
				self.draw()
			self.fig = []
			tr = 0
			for i in database.PARTY[database.FORMATION]:
				dt = database.CHARACTERS[i]
				dt['N'] = tr
				self.fig.append(dt)
				tr += 1

			self.bbg = pygame.image.load('Backgrounds/mountains.png')
			self.player_mov = False
			self.pstr = []
			self.patt = []
			self.pagi = []
			self.pres = []
			self.tatt = []
			self.tagi = []
			self.opt = 0
			self.mnu = 1
			p = 0
			for i in database.PARTY[database.FORMATION]:
				self.pstr.append(database.CHARACTERS[i]['STRENGHT'][database.CHARACTERS[i]['LEVEL']])
				self.patt.append(database.CHARACTERS[i]['ATTACK'][database.CHARACTERS[i]['LEVEL']])
				self.pagi.append(database.CHARACTERS[i]['AGILITY'][database.CHARACTERS[i]['LEVEL']])
				self.pres.append(database.CHARACTERS[i]['RESISTANCE'][database.CHARACTERS[i]['LEVEL']])
				self.tatt.append(0)
				self.tagi.append(0)
				p += 1
			enx = 0
			while enx < len(self.foe):
				self.foe[enx]['MASK'].x += enx * 80
				enx += 1
			self.battle = True
			self.transiction(True, 100)
			self.dialog([self.en[0]['NAME'] + database.BATTLE[0]])
			self.turn = 0

		#PLAYERS TURN
		elif self.turn < len(self.fig):
			self.mnu = 3
			if self.equip[self.turn] < 4:
				self.pp[self.turn][self.equip[self.turn]] -= 1
				gottem = False
				for i in self.foe:
					if self.colide(self.aim, i['MASK']):
						gottem = True
						dmg = int(random.randint(database.EQUIPMENT[self.turn][self.equip[self.turn]][1]['DAMAGE'] - 2, database.EQUIPMENT[self.turn][self.equip[self.turn]][1]['DAMAGE'] + 2)) - i['RESISTANCE']
						if database.EQUIPMENT[self.turn][self.equip[self.turn]][2][0] == database.ITEMS[93][0]:
							self.patt[self.turn] += database.EQUIPMENT[self.turn][self.equip[self.turn]][2][1]
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
							xp = int(((self.hits*self.tdmg)-self.hpl+self.tbt)/len(self.fig))
							self.dialog([database.BATTLE[6],database.BATTLE[7] + str(self.hits),database.BATTLE[8] + str(self.tdmg),database.BATTLE[9] + str(self.hpl),database.BATTLE[10]+str(self.tbt),database.BATTLE[11] + str(len(self.fig)),'= ' + str(xp)+database.BATTLE[12]])
							for i in range(len(self.fig)):
								self.fig[i]['XP'] += xp
								plux = int(100/(self.fig[i]['MAXXP']/xp))
							while self.barxp[0] < plux:
								self.draw()
								for i in range(len(database.PARTY[database.FORMATION])):
									self.barxp[i] += 1
									if self.barxp[i] >= 100:
										self.barxp[i] = 0
										self.fig[i]['LEVEL'] += 1
										self.fig[i]['XP'] = 0
										self.fig[i]['MAXXP'] *= 2
										plux = 0
										self.dialog([database.BATTLE[13] + str(self.fig[i]['LEVEL'])])
								database.SCENE = 1
								pygame.time.wait(10)
							self.wait()
							self.hits = 0
							self.tdmg = 0
							self.hpl = 0
							self.tbt = 0
							self.foe = []
							self.btime = 100
							self.battle = False
							self.turn = -1
							self.transiction(False, 0)
						self.mnu = 0
				if gottem == False:
					self.ch_sfx.play(pygame.mixer.Sound('SFX/miss.wav'))
					self.infohit(database.BATTLE[4], (200, 200, 200))
				#if self.pp[self.turn][self.equip] > 0: self.barpp[self.turn][self.opt] = int(100/(database.EQUIPMENT[self.turn][self.opt][1]['CAPACITY']/self.pp[self.turn][self.opt]))
				#else: self.barpp[self.turn][self.opt] = 0
			elif self.equip[self.turn] == 4:
				self.dialog(database.DIALOGS)

			elif self.equip[self.turn] == 5:
				if self.foe[0]['TYPE'] not in ('humanoid','psychic'):
					self.dialog(database.DIALOGS['IRRATIONAL'])
				self.turn += 1
				self.mnu = 1


			elif self.equip[self.turn] == 7:
				self.dialog([self.fig[self.turn]['NAME'] + database.BATTLE[14]])
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

			if self.turn < len(self.fig):
				self.aim.x = 100 + self.fig[self.turn]['ATTACK'][self.fig[self.turn]['LEVEL']]

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
					act = i['HABILITIES'][opt].copy()
					dd = i['NAME'] + database.BATTLE[17] + act[0]
					i['SPRITE'] = pygame.image.load('Sprites/' + (i['NAME']).lower() + '_attack.png')
					pl = int(random.randint(0,len(self.fig) - 1 + len(self.mrc)))
					if act[3] == 2 and self.tatt ==2: act = i['HABILITIES'][0]
					if act[3] == 3 and self.tagi ==2: act = i['HABILITIES'][0]

					if act[3] == 1:
						if act[2] < 0:
							if pl < len(self.fig):
								self.turn = self.fig[pl]['N']
								self.ch_sfx.play(pygame.mixer.Sound('SFX/damage_1.wav'))

								if database.ARMOR[pl] != []:
									act[2] += database.ARMOR[pl][1]
									database.ARMOR[pl][2] -=1
									if database.ARMOR[pl][2] == 0:
										self.dialog([database.ARMOR[pl][0] + 'foi quebrado...'])
										database.ARMOR[pl] = []
								self.fig[pl]['HP'] += act[2] + self.pres[pl]

								if -act[2] > 0: self.shake(-act[2] * 10, None)
								if self.fig[pl]['HP'] > 0:
									minush = int(100/(self.fig[pl]['VITALITY'][self.fig[pl]['LEVEL']]/self.fig[pl]['HP']))
								else: minush = 0

								while self.barhp[pl] > minush:
									self.draw()
									self.ch_sfx.play(pygame.mixer.Sound('SFX/hp_loss.wav'))
									self.barhp[pl] -= 1
									pygame.time.wait(5)

								self.hpl += act[2]

							else:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/hit.wav'))
								self.shake(10, self.mrc[pl])
								self.infohit(str(act[2]), (200, 0, 0))
								self.mrc[pl]['SPRITE'] = pygame.image.load('Sprites/' + (self.mrc[pl]['NAME']).lower() + '_stand.png')
								self.mrc[pl]['HP'] += act[2]

						elif act[2] > 0:
							i['HP'] += act[2]

					elif act[3] == 2:
						if act[2] < 0:
							if self.tatt[pl] < 2:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/attribute_loss.wav'))
								self.patt[pl] += act[2]
								self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[19] + str(act[2]) + database.BATTLE[21]])
								self.tatt[pl] += 1
						elif act[2] > 0:
							act[2] += act[2]
							self.dialog([dd, i['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[21]])
					elif act[3] == 3:
						if act[2] < 0:
							if self.tagi[self.turn]<2:
								self.ch_sfx.play(pygame.mixer.Sound('SFX/attribute_loss.wav'))
								self.pagi[self.turn]+=act[2]
								self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[19] + str(act[2]) + database.BATTLE[22]])
								self.tagi[self.turn]+=1
						elif act[2] > 0:
							i['AGILITY']+=act[2]
							self.dialog([dd, i['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[22]])
					elif act[3] == 4:	
						self.fig[pl]['HEALTH'] = act[2]
						if act[2] == 1:self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[23]])
						if act[2] == 2:self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[24]])

					#CHECK DEATH - GAME OVER
					if self.fig[pl]['HP'] <= 0:
						self.ch_ton.play(pygame.mixer.Sound('SFX/inconscious.wav'))
						self.dialog([self.fig[pl]['NAME'] + database.BATTLE[26]])
						del self.fig[pl]
					dth = 0
					for d in self.fig:
						if d['HP'] <= 0: dth += 1
					if dth == len(self.fig):
						self.transiction(True, 200)
						self.turn = -1
						self.dialog([database.BATTLE[27]])
						database.new_data()
						database.PX = 315
						database.PY = 200
						database.MONEY -= 100 * len(database.PARTY[database.FORMATION])
						for i in database.PARTY[database.FORMATION]:
							database.CHARACTERS[i]['HP'] = database.CHARACTERS[i]['VITALITY'][database.CHARACTERS[i]['LEVEL']]
						self.__init__()
						self.rendermap('hospital_')
						self.transiction(False, 0)
						break

					i['SPRITE'] = pygame.image.load('Sprites/' + (i['NAME']).lower() + '_stand.png')

			if self.turn > -1:
				self.turn =  0
				self.mnu = 1
				for i in range(len(self.fig)):
					if self.pres[i] > self.fig[i]['RESISTANCE'][self.fig[i]['LEVEL']]:
						self.pres[i] = self.fig[i]['RESISTANCE'][self.fig[i]['LEVEL']]

		if self.turn == len(self.fig): self.fight()

	def infohit(self, dmg, col):
		self.dmginfo = dmg
		self.dmgy = 200
		self.dmgcol = col
		hitac = 8

		while hitac > 0:
			self.draw()
			self.dmgy -= hitac
			pygame.time.wait(10)
			hitac -= 1

		while hitac < 8:
			self.draw()
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
				s += 1
			self.displayx = 0
			self.displayy = 0
			self.draw()

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
				s += 1
			tar['MASK'].x = sx
			tar['MASK'].y = sy
			self.draw()
     
	def rendermap(self, mp):
		self.map = pytmx.load_pygame('Maps/' + mp + str(database.MAP) + '.tmx')
		self.cam.x = 0
		self.cam.y = 0
		self.tilmap = []
		self.en = []
		self.foe = []
		self.npcs = []
		self.vehicles = []
		self.shops = []
		self.portals = []

		for i in range(3):
			self.tilmap.append(pygame.Surface((self.map.width * self.map.tilewidth,self.map.height * self.map.tileheight), pygame.SRCALPHA, 32))
			for x in range(0, self.map.width):
				for y in range(0, self.map.height):
					try:
						tl = self.map.get_tile_image(x, y, i)
						tl.convert_alpha()
						if tl != 0: self.tilmap[i].blit(tl, (x * self.map.tilewidth - self.cam.x, y * self.map.tileheight - self.cam.y))
					except: pass
			self.tilmap[i].convert_alpha()

		for i in range(self.map.properties['NPC']):
			obj = self.map.get_object_by_name('npc_' + str(i))
			self.npcs.append({'RECT': pygame.Rect(int(obj.x) - 10, int(obj.y) - 16, int(obj.width), int(obj.height)), 'WHO': obj.properties['WHO']})

		for i in range(self.map.properties['SHOP']):
			obj = self.map.get_object_by_name('shop_' + str(i))
			self.shops.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)), 'TYPE': int(obj.type), 'INDEX': obj.properties['INDEX']})

		for i in range(self.map.properties['VEHICLE']):
			obj = self.map.get_object_by_name('vehicle_' + str(i))
			vh = database.VEHICLES[obj.properties['INDEX']].copy()
			vh['RECT'] = pygame.Rect(float(obj.x), float(obj.y), 60, 60)
			vh['INDEX'] = obj.properties['INDEX']
			self.vehicles.append(vh)

		for i in range(self.map.properties['PORTAL']):
			obj = self.map.get_object_by_name('portal_' + str(i))
			if obj.properties['TIME'] != 'none':
				self.portals.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), 60, 60), 'PX': obj.properties['PX'], 'PY': obj.properties['PY'], 'MAP': obj.properties['MAP'], \
				'OPENING': [int(obj.properties['TIME'][0:2]),int(obj.properties['TIME'][2:4])], 'CLOSURE': [int(obj.properties['TIME'][4:6]),int(obj.properties['TIME'][6:8])]})
				print([int(obj.properties['TIME'][0:2]),int(obj.properties['TIME'][2:4])])
				print([int(obj.properties['TIME'][4:6]),int(obj.properties['TIME'][6:8])])
			else:
				self.portals.append({'RECT': pygame.Rect(int(obj.x), int(obj.y), 60, 60), 'PX': obj.properties['PX'], 'PY': obj.properties['PY'], 'MAP': obj.properties['MAP'], \
				'OPENING': None, 'CLOSURE': None})

		if mp not in ('drugstore_','bank_','hotel_','hospital_'):
			foe = self.map.properties['ENEMIES']
			lst = []
			trg = 0
			for i in range(len(foe)):
				if trg == 0: lst.append(int(foe[i:i + 2]))
				trg += 1
				if trg == 2: trg = 0
			print(lst)
			for i in range(round(random.randint(3,10))):
				self.en.append(database.FREAKS[lst[round(random.randint(0,len(lst) - 1))]].copy())
				self.en[i]['SPRITE'] = pygame.image.load('Sprites/' + (self.en[i]['NAME']).lower() + '_stand.png')
				self.en[i]['RECT'] = pygame.Rect(round(random.randint(0, self.map.width * self.map.tilewidth)),round(random.randint(0, self.map.height * self.map.tileheight)),10,16)
				self.en[i]['MASK'] = pygame.Rect(230,180,44,85)
				self.en[i]['FIGHTING'] = False
				if mp == self.en[i]['HABITAT']:
					self.en[i]['AGILITY'] += 2
					self.en[i]['HP'] += 5

		if mp in ('urban','drugstore','bank','market','hotel'): self.signal = 3
		else: self.signal = 0

	def minimap(self, mp, x, y, w, h, sg):
		if self.battle == False:
			self.mimap = pygame.Surface((int(self.displayzw/6),int(self.displayzh/4)))
			mim = pygame.image.load('Maps/urban_' + str(mp) +'.png')
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
			self.notx += 20
		while w < 50:
			self.draw()
			pygame.time.wait(1)
			w += 1
		self.notx = 0

	def draw(self):
		self.display.fill((0, 0, 0))
		self.display.blit(self.tilmap[0], (0 - self.cam.x, 0 - self.cam.y))
		self.display.blit(self.tilmap[1], (0 - self.cam.x, 0 - self.cam.y))

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
				while p < len(database.PARTY[database.FORMATION]):
					if p == self.turn: plcol = (0,0,0)
					else: plcol = (255,255,255)
					self.display.blit(self.mininfo.render(database.CHARACTERS[database.PARTY[database.FORMATION][p]]['NAME'].lower(), True, plcol), (10 + p * 120, 10))
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10 + p * 120,40,100,20))
					'''while float(database.PARTY[p]['BARHP']) > float(database.PARTY[p]['HP']):
						database.PARTY[p]['BARHP'] -= database.PARTY[p]['RESISTANCE'][database.PARTY[p]['LEVEL']]
						pygame.time.wait(10)ss
						pygame.draw.rect(self.display, (255, 255, 0), pygame.Rect(10,40,self.barhpl[p],20))'''
					if database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP'] > database.CHARACTERS[database.PARTY[database.FORMATION][p]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][p]]['LEVEL']]/5: hpcol = (0, 255, 0)
					elif database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP'] > 0: hpcol = (255, 0, 0)
					else: hpcol = (255, 0, 0)
					if self.barhp[p] > 0: pygame.draw.rect(self.display, hpcol, pygame.Rect(10 + p * 120,40,self.barhp[p],20))

					#pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10 + p * 120,70,100,20))
					if self.equip[p] < len(self.pp[p]) - 1:
						if database.EQUIPMENT[p][self.equip[p]] != '_':
							self.display.blit(self.monotype.render(str(self.pp[p][self.equip[p]]) + '/' + str(database.EQUIPMENT[p][self.equip[p]][1]['CAPACITY']), True, plcol), (10 + p * 120, 70))
						#pygame.draw.rect(self.display, (0, 100, 255), pygame.Rect(10 + p * 120,70,self.barpp[p][self.opt],20))
					p += 1

				if self.turn < len(database.PARTY[database.FORMATION]) and self.turn!=-1:
					#TIME BAR
					if self.mnu < 3:
						pygame.draw.rect(self.display, (255, 0, 255), pygame.Rect(0,302,int(600/(100/self.btime)),10))
						self.btime -= 0.5
						if self.btime == 0:
							self.turn = len(database.PARTY[database.FORMATION])
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
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(339,338,32,32))
						pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(341,340,28,28))
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
							self.aim.x += 20 - database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['AGILITY'][database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['LEVEL']]
							if self.aim.x > 500 - database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['ATTACK'][database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['LEVEL']]:
								self.aim.x = 100 + database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['ATTACK'][database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['LEVEL']]
							self.display.blit(pygame.image.load('Sprites/aim.png'), (self.aim.x-15, self.aim.y))

			#INFOHIT
			if self.dmginfo != '':
				pygame.draw.rect(self.display, self.dmgcol, pygame.Rect(self.aim.x,self.dmgy,len(self.dmginfo) * 20,22))
				self.display.blit(self.mininfo.render(self.dmginfo, True, (0,0,0)), (self.aim.x, self.dmgy))

			if self.winbar == 210:
				for i in range(len(database.PARTY[database.FORMATION])):
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,120 + i * 30,100,20))
					if database.CHARACTERS[database.PARTY[database.FORMATION][i]]['XP'] > 0: pygame.draw.rect(self.display, (0, 255, 100), pygame.Rect(10,120 + i * 30,self.barxp[i],20))
		
		#OBJECTS
		elif self.battle == False:
			pygame.draw.rect(self.display, (0,0,255), pygame.Rect(self.player_rect.x - self.cam.x, self.player_rect.y - self.cam.y, self.player_rect.width, self.player_rect.height))
			if self.sleepin == False: self.display.blit(self.player_sprite[self.player_gif//len(self.player_sprite)], (self.player_rect.x - self.cam.x, self.player_rect.y - self.cam.y))

			for i in range(len(self.en)):
				if self.en[i]['HP'] > 0: self.enemy(i)
			for i in self.npcs:
				self.npc(i['RECT'].x,i['RECT'].y,i['RECT'].width,i['RECT'].height,i['WHO'])
			for i in self.shops:
				self.shop(i['RECT'].x,i['RECT'].y,i['RECT'].width,i['RECT'].height,i['TYPE'],i['INDEX'])
			for i in self.vehicles:
				self.vehicle(i['RECT'].x,i['RECT'].y,i['INDEX'])
			for i in self.portals:
				self.portal(i['RECT'].x,i['RECT'].y,i['PX'],i['PY'],i['MAP'],i['OPENING'],i['CLOSURE'])

			self.display.blit(self.tilmap[2], (0 - self.cam.x, 0 - self.cam.y))


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
				self.display.blit(shp.mercator(self.opt, self.lopt, self.products), (100,60))
			if self.mnu == 3 or self.mnu == 11 or self.mnu == 12:
				shp = menu.Shop()
				self.display.blit(shp.bank(self.opt, self.lopt, self.mnu, self.extract), (100,60))

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
		elif self.phone == 11: self.display.blit(self.phn.achievements(self.lopt, self.signal), (210,60))
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
		self.update()

	def update(self):
		#ANIMATION
		if self.player_mov == True:
			self.player_gif += int(self.player_spd/3)
			self.ch_sfx.stop()
			self.ch_sfx.play(pygame.mixer.Sound('SFX/step_grass.wav'))
			if self.player_gif >= 60//len(self.player_sprite): self.player_gif = 0
		else: self.player_gif = 0

		#DATETIME
		if self.sleepin == False: database.TIME[2] += 1
		else: database.TIME[1] += 5

		if database.TIME[2] >= 60:
			database.TIME[1] += 1
			database.TIME[2] = 0

		if database.TIME[1] >= 60:
			database.TIME[0] += 1
			database.TIME[1] = 0

		if database.TIME[0] >= 24:
			database.DATE[0] += 1
			database.TIME[0] = 0

		if database.DATE[0] >= 30:
			database.DATE[1] += 1
			database.DATE[0] = 1

		if database.DATE[1] >= 12:
			database.DATE[2] += 1
			database.DATE[1] = 1

		pygame.display.update()
		pygame.display.flip()

	def run(self):
		pygame.time.Clock().tick(self.FPS)
		self.events()
		self.draw()

database.new_data()
database.party_make(0)
g = Game()
while True:
	g.run()