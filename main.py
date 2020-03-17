# -*- coding: utf-8 -*-
import pygame
import pytmx
import random
import sqlite3
import webbrowser
import numpy
import math
import sys
import menu

menu.recent_data(0)
if menu.FILES[3] != []:
	if menu.FILES[3][0] == 'PT': import database_PT as database
	if menu.FILES[3][0] == 'EN': import database_EN as database
else: import database_PT as database

pygame.init()
pygame.display.set_caption('Mutation Purge')
pygame.display.set_icon(pygame.image.load('icon.ico'))

class Title:
	def __init__(self):
		global ID
		self.screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
		self.display = pygame.Surface((600, 400))
		self.monotype = pygame.font.Font('Fonts/monotype.ttf', 15)
		self.sfx = pygame.mixer.Channel(0)
		self.ton = pygame.mixer.Channel(1)
		self.msc = pygame.mixer.Channel(2)
		self.n = menu.Naming()
		self.winbar = 210
		self.wait = 100
		self.noise = 0
		self.tv = 1
		self.opt = 0
		self.lopt = 0
		self.mnu = 0
		self.glock = pygame.time.Clock()
		self.FPS = 60
		self.scroll = 0
		self.skip = False
		self.classrun = True

		for i in menu.FILES[0]:
			if menu.FILES[1][i] == 0:
				del menu.FILES[0][i]
				del menu.FILES[1][i]
				del menu.FILES[2][i]
				del menu.FILES[3][i]

		for i in range(10):
			if self.mnu != 0: break
			self.run()
		self.mnu = 1
		for i in range(100):
			if self.mnu != 1: break
			self.run()
		self.mnu = 2
		for i in range(20):
			if self.mnu != 2: break
			self.run()
		while self.winbar > 50:
			self.winbar -= 5
			self.run()

	def random(self):
		self.ton.play(database.SOUND['NOISE'],-1)
		self.tv = 0
		for i in range(20): self.run()
		self.ton.stop()
		self.tv = round(random.randint(1,3))
		self.wait = round(random.randint(50,100))

	def run(self):
		#EVENTS
		if self.n.show == True: self.n.events()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if self.mnu == 4 and self.n.ind == 7: self.mnu = 2
			self.pressed = pygame.key.get_pressed()
			if self.pressed[database.ACT]:
				if self.mnu < 2: self.mnu += 1
				elif self.mnu == 5: self.skip = True
				elif self.winbar == 50:
					if self.lopt < len(menu.FILES[0]):
						if self.mnu < 3: self.mnu += 1
						elif self.mnu == 3: 
							if self.opt == 0:
								self.mnu = 5
								database.load_data()
								self.msc.play(database.SONGS['FATE_OCCURRENCES'],-1)
							else: del ID[self.lopt]
					else:
						self.n.show = True
						self.mnu = 4

			if self.pressed[database.RUN]:
				if self.mnu == 3: self.mnu = 2

			if self.pressed[database.UP] and self.mnu == 2: self.lopt -= 1; self.sfx.play(database.SOUND['MENU_HOR'])
			if self.pressed[database.DOWN] and self.mnu == 2: self.lopt += 1; self.sfx.play(database.SOUND['MENU_VER'])

			if self.pressed[database.LEFT] and self.mnu == 3: self.opt = 0; self.sfx.play(database.SOUND['MENU_HOR'])
			if self.pressed[database.RIGHT] and self.mnu == 3: self.opt = 1; self.sfx.play(database.SOUND['MENU_VER'])

			if self.lopt < 0: self.lopt = len(menu.FILES[0])
			if self.lopt > len(menu.FILES[0]): self.lopt = 0

		self.display.fill((255, 0, 0))

		#FILES MENU
		if self.mnu < 5:
			if self.tv == 0:
				self.noise += 1
				if self.noise == 3: self.noise = 0
				self.display.blit(pygame.image.load('Backgrounds/noise_' + str(self.noise) + '.png'), (0, 0))
			else: self.display.blit(pygame.image.load('Backgrounds/tv_' + str(self.tv) + '.png').convert(), (0, 0))

			for i in range(len(menu.FILES[1])):
				if self.lopt == i: col = (255,255,0)
				else: col = (255,255,255)
				pygame.draw.rect(self.display, col, pygame.Rect(400,100 + (i * 51),180,50))
				self.display.blit(self.monotype.render(database.CHAPTERS[menu.FILES[1][i]][0], True, (0,0,0)), (405, 105 + (i * 51)))

				if self.mnu > 2 and self.lopt == i:
					if self.opt == 0: pygame.draw.rect(self.display, (255,255,255), pygame.Rect(528,113 + (i * 51),24,24))
					if self.opt == 1: pygame.draw.rect(self.display, (255,255,255), pygame.Rect(550,113 + (i * 51),24,24))
					self.display.blit(pygame.image.load('Sprites/tc_7.png'), (530, 115 + (i * 51)))
					self.display.blit(pygame.image.load('Sprites/tc_8.png'), (552, 115 + (i * 51)))
				database.ID = self.lopt

			if self.lopt == len(menu.FILES[0]): col = (255,255,0)
			else: col = (255,255,255)
			pygame.draw.rect(self.display, col, pygame.Rect(400,100 + (len(menu.FILES[1]) * 51),180,50))
			self.display.blit(self.monotype.render(database.MENU[61], True, (0,0,0)), (405, 105 + (len(menu.FILES[1]) * 51)))

		#RECAP
		if self.mnu == 5:
			lt = 0
			for y in database.CHAPTERS[database.CHAPTER - 1][2:]:
				self.display.blit(self.monotype.render(y, True, (255,255,255)), (50, 360 - self.scroll + lt))
				lt += 20

			self.scroll += 0.3
			if self.scroll > 340 + lt or self.skip == True:
				if self.winbar == 50: self.msc.fadeout(5000)
				if self.winbar < 210:
					self.winbar += 5
			if self.winbar == 210:
				g.rendermap('urban_0')
				self.classrun = False

		#BLACK BARS
		pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
		pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

		#DISCLAIMER
		if self.mnu == 1:
			y = 0
			for i in database.DISCLAIMER:
				self.display.blit(self.monotype.render(i, True, (240,240,240)), (180, 100 + y))
				y += 20
			self.screen.blit(pygame.transform.scale(self.display, (1200, 800)), (0, 0))

		elif self.mnu > 1 and self.mnu < 5:
			self.display.blit(self.monotype.render(database.ABOUT[0], True, (240,240,240)), (5, 5))
			self.display.blit(self.monotype.render(database.ABOUT[1], True, (240,240,240)), (440, 370))
			if self.wait > 0: self.wait -= 1
			prb = round(random.randint(0,100))
			if prb > 50 and self.wait == 0 and self.tv > 0: self.random()

		if self.n.show == True: self.display.blit(self.n.run(), (200, 100))

		self.screen.blit(pygame.transform.scale(self.display, (1200, 800)), (0, 0))
		pygame.display.update()
		pygame.display.flip()
		self.glock.tick(self.FPS)

class Game:
	def __init__(self):
		#GAME SETTINGS
		self.screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE | pygame.DOUBLEBUF)
		self.display = pygame.Surface((600, 400))
		self.displayzw = 600
		self.displayzh = 400
		self.displayx = 0
		self.displayy = 0
		self.windoww = 1200
		self.windowh = 800
		self.glock = pygame.time.Clock()
		self.FPS = 60
		self.mininfo = pygame.font.Font('Fonts/pixel-font.ttf', 25)
		self.monotype = pygame.font.Font('Fonts/monotype.ttf', 15)
		self.cam = pygame.Rect(0,0,self.displayzw,self.displayzh)
		self.driving = 0
		self.sleepin = False
		self.tilemation = 0
		self.room = ''

		hm = database.TIME[0] + 10
		if hm > 24: hm -= 24
		self.waitime = [['advice',hm,0],['rain',database.TIME[0],database.TIME[1] + 5]]#,['cal923778988',database.TIME[0],database.TIME[1] + 6]]

		#MIXER
		pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
		self.ch_sfx = pygame.mixer.Channel(0)
		self.ch_sfx.set_volume(database.SFX)
		self.ch_msc = pygame.mixer.Channel(1)
		self.ch_msc.set_volume(database.MSC)
		self.ch_ton = pygame.mixer.Channel(2)
		self.ch_ton.set_volume(database.SFX)
		self.ch_rad = pygame.mixer.Channel(3)
		self.ch_rad.set_volume(0.1)
		self.ch_stp = pygame.mixer.Channel(4)
		self.ch_stp.set_volume(database.SFX)
		self.ch_rng = pygame.mixer.Channel(5)
		self.ch_rng.set_volume(database.MSC)

		#BATTLE VARIABLES
		self.dlg = []
		self.dlgfa = 500
		self.dlgy = 0
		self.dmginfo = ''
		self.dmgy = 200
		self.dlgspd = database.SPEED
		self.speakin = 0
		self.equip = []
		self.battle = False
		self.effttack = None
		self.effgif = 0
		self.btime = 100
		self.bbg = ''
		self.bbm = 0
		self.obstacles = False
		self.hits = 0
		self.tdmg = 0
		self.hpl = 0
		self.tbt = 0
		self.xp = 0
		self.turn = -1
		self.aim = pygame.Rect(300,200,30,30)
		self.barhp = []
		self.barhpl = []
		self.barpp = []
		self.barxp = []
		self.greenblood = 0
		x = 0
		for i in database.PARTY[database.FORMATION]:
			database.CHARACTERS[i]['HP'] = database.CHARACTERS[i]['VITALITY'][database.CHARACTERS[i]['LEVEL']]
			self.equip.append(0)
			self.barpp.append([])
			self.barhp.append(int(100/(database.CHARACTERS[i]['VITALITY'][database.CHARACTERS[i]['LEVEL']]/database.CHARACTERS[i]['HP'])))
			self.barhpl.append(100)
			if database.CHARACTERS[i]['XP'] > 0: self.barxp.append(int(100/(database.CHARACTERS[i]['NEXTLEVEL'][database.CHARACTERS[i]['LEVEL']]/database.CHARACTERS[i]['XP'])))
			else: self.barxp.append(0)
			for j in database.INVENTORY[database.PARTY[database.FORMATION][x]][4][1:]:
				if j[0] != '_':
					if int(j[1]) > 0: b = int(100/(database.ITEMS[j[0]][5]['CAPACITY']/int(j[1])))
					else: b = 0
					self.barpp[x].append(b)
				else:
					self.barpp[x].append(0)
			x += 1

		#MENU VARIABLES
		self.phn = menu.Phone()
		self.inv = menu.Inventory()
		self.shpmnu = menu.Shop()
		self.nmenu = menu.Naming()
		self.opt = 1
		self.lopt = 0
		self.mnu = 1
		self.exvar = 0
		self.inventory = 0
		self.invfade = 1050
		self.phone = 0
		self.phofa = 0
		self.nb = ''
		self.shp = False
		self.basket = []
		self.products = []
		self.extract = [0,0,0,0,0,0]
		self.promo = 0
		self.winbar = 210
		self.radonoff = False
		self.fm = 0
		self.vm = 0.5
		self.msc = 0
		self.signal = 0
		self.nottxt = ''
		self.notcol = (0,0,0)
		self.notx = 0

		#MAP VARIABLES
		self.player = {'RECT': pygame.Rect(database.PX,database.PY,20,20),'SPD': 0,'JUMP': 0,'GRAVITY': -5,'HEAD': 'BLANKD_011', 'SPRITE': 'STANDD_000','GIF': 0.0,
		'BLINK': 100,'DIRECTION': 0, 'PAUSE': 0,'FOLLOW': None,'FOLLEND': 0}
		self.objects = []
		self.tilrect = []
		self.en = []
		self.foe = []
		self.fig = []
		self.mrc = []
		self.npcs = []
		self.vehicles = []
		self.portals = []
		self.signs = []
		self.particles = []

		#STARTING GAME
		if database.GAMETIME == 0:
			self.player['PAUSE'] = 1
			self.rendermap('hauntedhouse_0')
			self.phone = 15
			self.mnu = 1

	def enemy(self, en):
		#DRAW
		if self.battle == False and self.colide(self.en[en]['RECT'], self.cam):
			pygame.draw.rect(self.display, (255,0,0), pygame.Rect(self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y, self.en[en]['RECT'].width, self.en[en]['RECT'].height))
			self.display.blit(pygame.image.load('Sprites/frk_' + (self.en[en]['FILE']) + '_mini.png'), (self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y))
			if self.en[en]['PATH'] == 'notice': self.display.blit(pygame.image.load('Sprites/notice.png'), (self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y - 30))

		#MOVEMENT
		if self.colide(self.en[en]['RECT'], self.cam) and self.winbar == 0 and self.battle == False and self.en[en]['FIGHTING'] == False:
			if self.en[en]['PATH'] == 'stealth':
				if self.facing(self.en[en],self.player) == 2:
					self.ch_sfx.play(database.SOUND['NOTICED'])
					self.en[en]['PATH'] = 'notice'
					for i in range(10):
						self.run()
					self.en[en]['PATH'] = 'follow'
				else:
					if self.en[en]['DIRECTION'] == 0:
						self.en[en]['DIRECTION'] = 1

					if self.en[en]['TIME'] == 0:
						if self.en[en]['DIRECTION'] == 1: self.en[en]['DIRECTION'] = 5
						elif self.en[en]['DIRECTION'] == 5: self.en[en]['DIRECTION'] = 1
						self.en[en]['TIME'] = 20

			elif self.en[en]['PATH'] == 'follow':
				if self.en[en]['RECT'].y - self.cam.y > self.player['RECT'].y - 5 - self.cam.y:
					if self.en[en]['RECT'].x - self.cam.x < self.player['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 8
					elif self.en[en]['RECT'].x - self.cam.x > self.player['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 6
					else: self.en[en]['DIRECTION'] = 7

				elif self.en[en]['RECT'].y - self.cam.y < self.player['RECT'].y - 5 - self.cam.y: 
					if self.en[en]['RECT'].x - self.cam.x < self.player['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 2
					elif self.en[en]['RECT'].x - self.cam.x > self.player['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 4
					else: self.en[en]['DIRECTION'] = 3

				elif self.en[en]['RECT'].x - self.cam.x < self.player['RECT'].x + 10 - self.cam.x:
					if self.en[en]['RECT'].y - self.cam.y > self.player['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 8
					elif self.en[en]['RECT'].y - self.cam.y < self.player['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 2
					else: self.en[en]['DIRECTION'] = 1

				elif self.en[en]['RECT'].x - self.cam.x > self.player['RECT'].x + 10 - self.cam.x:
					if self.en[en]['RECT'].y - self.cam.y > self.player['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 6
					elif self.en[en]['RECT'].y - self.cam.y < self.player['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 4
					else: self.en[en]['DIRECTION'] = 5

			elif self.en[en]['PATH'] == 'horizontal':
				if self.en[en]['DIRECTION'] == 0:
					self.en[en]['DIRECTION'] = 1

				if self.en[en]['TIME'] == 0:
					if self.en[en]['DIRECTION'] == 1: self.en[en]['DIRECTION'] = 5
					elif self.en[en]['DIRECTION'] == 5: self.en[en]['DIRECTION'] = 1
					self.en[en]['TIME'] = 20

			if self.player['PAUSE'] < 3:
				if self.en[en]['DIRECTION'] == 1: self.en[en]['RECT'].x += self.en[en]['AGILITY'] - 1
				if self.en[en]['DIRECTION'] == 2: self.en[en]['RECT'].x += self.en[en]['AGILITY'] - 1; self.en[en]['RECT'].y += self.en[en]['AGILITY'] - 1
				if self.en[en]['DIRECTION'] == 3: self.en[en]['RECT'].y += self.en[en]['AGILITY'] - 1
				if self.en[en]['DIRECTION'] == 4: self.en[en]['RECT'].x -= self.en[en]['AGILITY'] - 1; self.en[en]['RECT'].y += self.en[en]['AGILITY'] - 1
				if self.en[en]['DIRECTION'] == 5: self.en[en]['RECT'].x -= self.en[en]['AGILITY'] - 1
				if self.en[en]['DIRECTION'] == 6: self.en[en]['RECT'].x -= self.en[en]['AGILITY'] - 1; self.en[en]['RECT'].y -= self.en[en]['AGILITY'] - 1
				if self.en[en]['DIRECTION'] == 7: self.en[en]['RECT'].y -= self.en[en]['AGILITY'] - 1
				if self.en[en]['DIRECTION'] == 8: self.en[en]['RECT'].x += self.en[en]['AGILITY'] - 1; self.en[en]['RECT'].y -= self.en[en]['AGILITY'] - 1
				self.en[en]['TIME'] -= 1

		#BATTLE ENTER
		if self.colide(self.en[en]['RECT'], self.player['RECT']) == True and self.en[en]['DIRECTION'] > 0 and self.battle == False and self.dlgfa == 500:
			if self.en[en]['FIGHTING'] == False:
				if self.en[en]['TYPE'] != 'mercenary': self.foe.append(self.en[en])
				else: self.mrc.append(self.en[en])
				self.en[en]['FIGHTING'] = True
				if len(self.foe) == 1:
					self.turn = -self.facing(self.en[en],self.player)
					print(self.turn)
					self.fight()

	def npc(self, i):
		if i['RECT'].width > 0: rect = pygame.Rect(i['RECT'].x,i['RECT'].y,i['RECT'].width,i['RECT'].height)
		else: rect = pygame.Rect(i['RECT'].x,i['RECT'].y,20,20)

		#DRAW
		pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False and self.colide(rect, self.cam):
			if i['TYPE'] == 0 or i['TYPE'] == 2 and i['RECT'].width == 0:
				if self.speakin == rect and self.dlgfa == 0: img = pygame.image.load('Sprites/npc_' + i['INDEX'] + '_talk_' + str(math.floor(i['IMAGE'])) +'.png')
				else: img = pygame.image.load('Sprites/npc_' + i['INDEX'] + '_stand_0.png')
				self.display.blit(img, (rect.x - self.cam.x - int(img.get_rect().width/2) + 10, rect.y - self.cam.y - int(img.get_rect().height/2) - 3))
			elif i['TYPE'] == 3:
				img = pygame.image.load('Sprites/mercator.png')
				self.display.blit(img, (rect.x - self.cam.x - int(img.get_rect().width/2) + 10, rect.y - self.cam.y - int(img.get_rect().height/2) - 3))
			elif i['TYPE'] == 5:
				self.display.blit(pygame.image.load('Sprites/obj_' + str(i['INDEX']) + str(i['WHO']) + '.png'), (rect.x - self.cam.x, rect.y - self.cam.y - 10))
				if self.sleepin == True and i['INDEX'] == 1: self.display.blit(pygame.image.load('Sprites/char_0_rest.png'), (rect.x - self.cam.x + 5, rect.y - self.cam.y + 5))

		#MOVEMENT
		if i['FOLLOW'] != None and i['FOLLOW'] != (None,None):
			i['SPD'] = 3
			if i['RECT'].y - self.cam.y > i['FOLLOW'].y - self.cam.y:
				if i['RECT'].x - self.cam.x < i['FOLLOW'].x - self.cam.x: i['DIRECTION'] = 8
				elif i['RECT'].x - self.cam.x > i['FOLLOW'].x - self.cam.x: i['DIRECTION'] = 6
				else: i['DIRECTION'] = 7

			elif i['RECT'].y - self.cam.y < i['FOLLOW'].y - self.cam.y: 
				if i['RECT'].x - self.cam.x < i['FOLLOW'].x - self.cam.x: i['DIRECTION'] = 2
				elif i['RECT'].x - self.cam.x > i['FOLLOW'].x - self.cam.x: i['DIRECTION'] = 4
				else: i['DIRECTION'] = 3

			elif i['RECT'].x - self.cam.x < i['FOLLOW'].x - self.cam.x:
				if i['RECT'].y - self.cam.y > i['FOLLOW'].y - self.cam.y: i['DIRECTION'] = 8
				elif i['RECT'].y - self.cam.y < i['FOLLOW'].y - self.cam.y: i['DIRECTION'] = 2
				else: i['DIRECTION'] = 1

			elif i['RECT'].x - self.cam.x > i['FOLLOW'].x - self.cam.x:
				if i['RECT'].y - self.cam.y > i['FOLLOW'].y - self.cam.y: i['DIRECTION'] = 6
				elif i['RECT'].y - self.cam.y < i['FOLLOW'].y - self.cam.y: i['DIRECTION'] = 4
				else: i['DIRECTION'] = 5

		if self.colide(i['RECT'], self.cam) and self.winbar == 0 and self.battle == False and self.dlgfa == 500 and i['TYPE'] == 0 and i['RECT'].width == 0:
			if i['MOVE'] == 'horizontal':
				i['SPD'] = 1
				if i['DIRECTION'] not in [1,5]:
					i['DIRECTION'] = 1

				if i['TIME'] == 0:
					if i['DIRECTION'] == 1: i['DIRECTION'] = 5
					elif i['DIRECTION'] == 5: i['DIRECTION'] = 1
					i['TIME'] = 30
				i['TIME'] -= 1

		if self.player['PAUSE'] < 3:
			if i['DIRECTION'] == 1: i['RECT'].x += i['SPD']
			if i['DIRECTION'] == 2: i['RECT'].x += i['SPD']; i['RECT'].y += i['SPD']
			if i['DIRECTION'] == 3: i['RECT'].y += i['SPD']
			if i['DIRECTION'] == 4: i['RECT'].x -= i['SPD']; i['RECT'].y += i['SPD']
			if i['DIRECTION'] == 5: i['RECT'].x -= i['SPD']
			if i['DIRECTION'] == 6: i['RECT'].x -= i['SPD']; i['RECT'].y -= i['SPD']
			if i['DIRECTION'] == 7: i['RECT'].y -= i['SPD']
			if i['DIRECTION'] == 8: i['RECT'].x += i['SPD']; i['RECT'].y -= i['SPD']

			if i['FOLLOW'] != None:
				if i['FOLLOW'] != (None,None):
					if self.colide(rect,i['FOLLOW']):
						i['DIRECTION'] = i['FOLLEND']
						i['FOLLOW'] = None
						i['FOLLEND'] = 0
						i['SPD'] = 0
				else:
					i['DIRECTION'] = i['FOLLEND']
					i['FOLLOW'] = None
					i['FOLLEND'] = 0
					i['SPD'] = 0

		#ACTIONS
		if self.colide(self.player['RECT'], rect) == True:
			if self.battle == False and self.speakin != rect: self.display.blit(pygame.image.load('Sprites/arw.png'), (rect.x - self.cam.x + int(rect.width/2) - 5, rect.y - self.cam.y - rect.height * 2))
			for event in pygame.event.get():
				self.pressed = pygame.key.get_pressed()
				if self.pressed[database.ACT]:
					self.player['PAUSE'] = 1

					#NPC DIALOG
					if i['TYPE'] == 0:
						if self.dlgfa > 0:
							i['DIRECTION'] = 0
							if i['WHO'] != 'REWARD':
								if isinstance(i['WHO'], int): self.dialog(database.DIALOGS['NPC_'+str(i['WHO'])][database.DLGSAV[str(database.MAP) + self.room][i['N']]].copy(),rect)
								else: self.dialog(database.DIALOGS[i['WHO']][database.DLGSAV[str(database.MAP) + self.room][i['N']]].copy(),rect)
							else:
								if self.greenblood > 700: self.dialog(database.DIALOGS['REWARD'][3].copy(),rect)
								elif self.greenblood > 300: self.dialog(database.DIALOGS['REWARD'][2].copy(),rect)
								elif self.greenblood > 0: self.dialog(database.DIALOGS['REWARD'][1].copy(),rect)
								else: self.dialog(database.DIALOGS['REWARD'][0].copy(),rect)

								if self.notx == 0 and self.greenblood > 0:
									database.MONEY += self.greenblood
									self.ch_sfx.play(database.SOUND['CASH_GET'])
									self.notification('Adquiriu $' + str(self.greenblood),(255, 255, 255))
									self.dlg = []
									self.greenblood = 0

					#MARKET CASHIER
					elif i['TYPE'] == 2:
						if i['WHO'].startswith('DRITHR'):
							if self.driving == 0:
								if self.dlgfa > 0: self.dialog(database.DIALOGS[i['WHO']][0].copy(),rect)
							else:
								self.products = []
								for p in database.PRODUCTS[int(i['INDEX'])][0]:
									self.products.append(p)
								self.shp = True
								self.lopt = 0
								self.opt = 0
								self.mnu = 2
						elif self.basket == []:
							if self.dlgfa > 0: self.dialog(database.DIALOGS[i['WHO']][0].copy(),rect)
						else:
							self.products = []
							for p in database.PRODUCTS[int(i['INDEX'])][0]:
								self.products.append(p)
							self.shp = True
							self.lopt = 0
							self.opt = 0
							self.mnu = 2

					#DEPOSIT ITEMS
					elif i['TYPE'] == 4:
						self.inventory = 2
						self.ch_sfx.play(database.SOUND['INVENTORY_OPEN'])
						self.invfade = 0
						self.opt = 0
						self.lopt = 1
						self.mnu = 0
						self.exvar = 0

					elif i['TYPE'] == 5:
						#ATM MACHINE
						if i['INDEX'] == 0:
							self.extract = [0,0,0,0,0,0]
							self.opt = 0
							self.lopt = 1
							self.mnu = 0
							self.exvar = 0
						#BED
						elif i['INDEX'] == 1:
							self.sleepin = not self.sleepin
							if self.sleepin == False: self.player['PAUSE'] = 1
							else: self.player['PAUSE'] = 0
						#TRASH CAN
						elif i['INDEX'] == 2:
							self.inventory = 3
							self.ch_sfx.play(database.SOUND['INVENTORY_OPEN'])
							self.invfade = 0
							self.opt = 0
							self.lopt = 1
							self.mnu = 0
						#PHONE
						elif i['INDEX'] == 3:
							if database.MONEY > 0:
								database.MONEY -= 1
								database.CALLHIST.insert(0,[database.CONTACTS[self.lopt][1],False])
								self.dialog(database.DIALOGS[database.CONTACTS[self.lopt][1]][0],rect)
							else:
								self.dialog([database.MENU[18]],rect)
						#BATTERY PLUG
						elif i['INDEX'] == 4:
							print('here')
							if self.inv.find(0,'charger') != None: self.ch_sfx.play(database.SOUND['MENU_GO']); database.BATTERY = 360
							else: self.ch_sfx.play(database.SOUND['MENU_GO']); self.dialog(database.DIALOGS['PLUG'])
						#REFUEL
						elif i['INDEX'] == 5 and self.driving > 0:
							while database.GAS < self.vehicles[self.driving - 1]['CAPACITY']:
								database.GAS += 1
								self.run()

					#PRODUCTS AND MERCATOR
					else:
						if i['TYPE'] == 3:
							self.dialog(database.DIALOGS['MERCATOR'][0],rect)
							self.basket = []
							j = 0
							x = 0
							for p in range(len(database.INVENTORY)):
								if p in database.PARTY[database.FORMATION]:
									for t in database.INVENTORY[p]:
										for k in t:
											if k[0] != '_' and database.ITEMS[database.INVENTORY[p][j][x][0]][2] != 0:
												self.basket.append([p,j,x])
											x += 1
										x = 0
										j += 1
								x = 0
								j = 0
						if database.DATE[3] == database.PRODUCTS[int(i['INDEX'])][1]:
							self.promo = database.PRODUCTS[int(i['INDEX'])][2]
						self.products = []
						for p in database.PRODUCTS[int(i['INDEX'])][0]:
							self.products.append(p)
						self.shp = True
						self.lopt = 0
						self.opt = 0
						self.mnu = i['WHO']

	def vehicle(self, i):
		rect = pygame.Rect(i['RECT'].x - 5,i['RECT'].y - 5,60,30)
		if self.driving == i['INDEX'] + 1:
			i['RECT'].x = self.player['RECT'].x
			i['RECT'].y = self.player['RECT'].y

		pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False and self.colide(rect, self.cam):
			self.display.blit(pygame.image.load('Sprites/moto_' + str(i['INDEX']) + '_walkL.png'), (rect.x - self.cam.x + 10, rect.y + rect.height - self.cam.y - 30))

		if self.colide(self.player['RECT'], rect) == True:
			for event in pygame.event.get():
				if self.pressed[database.ACT] and self.driving == 0:
					trigger = True
					self.driving = i['INDEX'] + 1
					'''self.displayzw = 1200
					self.displayzh = 800
					self.display = pygame.Surface((1200, 800))
					self.cam = pygame.Rect(0,0,self.displayzw,self.displayzh)'''
			if self.battle == False: self.display.blit(pygame.image.load('Sprites/arw.png'), (rect.x - self.cam.x + int(rect.width/2) - 5, rect.y - self.cam.y - int(rect.height/2)))

	def portal(self, i):
		rect = pygame.Rect(i['RECT'].x,i['RECT'].y,i['RECT'].width,i['RECT'].height)
		goto = False

		pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False and self.colide(rect, self.cam):
			if self.colide(self.player['RECT'], rect) == True and self.winbar > 0: spr = '1'
			else: spr = '0'
			if database.MAP > 0:
				if i['RECT'].width == 24: self.display.blit(pygame.image.load('Sprites/door_0' + spr + '.png'), (rect.x - self.cam.x, rect.y - self.cam.y))
				if i['RECT'].width == 48: self.display.blit(pygame.image.load('Sprites/door_1' + spr + '.png'), (rect.x - self.cam.x, rect.y - self.cam.y))
			else: self.display.blit(pygame.image.load('Sprites/mp_player.png'), (rect.x - self.cam.x, rect.y - self.cam.y))

		if self.colide(self.player['RECT'], rect) == True and self.winbar == 0:
			if i['OPENING'] == 'key':
				fnd = self.inv.find(0,'key_bedroom')
				if fnd != None and fnd[1] == i['CLOSURE']: goto = True
				else: goto = False

			elif i['OPENING'] != None:
				if database.TIME[0] > i['OPENING'][0] and database.TIME[0] < i['CLOSURE'][0]: goto = True
				elif database.TIME[0] == i['OPENING'][0]:
					if database.TIME[1] > i['OPENING'][1]: goto = True
				elif database.TIME[0] == i['CLOSURE'][0]:
					if database.TIME[1] < i['CLOSURE'][1]: goto = True
			else: goto = True

		if goto == True:
			self.player['PAUSE'] = 1
			self.player['SPD'] = 0
			if i['TYPE'] > 0: self.ch_sfx.play(database.SOUND['DOOR_OPEN'])
			self.transiction(True, 210)
			self.rendermap(i['MAP'])
			self.player['RECT'].x = i['PX']
			self.player['RECT'].y = i['PY']
			if i['TYPE'] > 0: self.ch_sfx.play(database.SOUND['DOOR_CLOSE'])
			self.transiction(False, 0)
			self.player['PAUSE'] = 0

	def colide(self, i1, i2):
		cld = False
		'''if i1.x - self.cam.x > i2.x - self.cam.x and i1.x - self.cam.x < i2.x - self.cam.x + i2.width or i1.x - self.cam.x + i1.width > i2.x - self.cam.x and i1.x - self.cam.x + i1.width < i2.x - self.cam.x + i2.width:
			if i1.y - self.cam.y > i2.y - self.cam.y and i1.y - self.cam.y < i2.y - self.cam.y + i2.height or i1.y - self.cam.y + i1.height > i2.y - self.cam.y and i1.y - self.cam.y + i1.height < i2.y - self.cam.y + i2.height:
				return True
			else: return False
		else: return False'''
		if isinstance(i2, list):
			for t in range(2):
				for i in i2[t]:
					if i[0] == 'WALL' and self.facing(i1,i[1]) == 2:
						cld = pygame.Rect.colliderect(i1['RECT'],i[1])
						if cld == True and i1['JUMP'] == 0:  break
		else:
			cld = pygame.Rect.colliderect(i1,i2)

		return cld

	def facing(self, i1, i2):
		if isinstance(i2, dict) == False: i2 = {'RECT': i2, 'DIRECTION': self.player['DIRECTION']}
		if i1['DIRECTION'] == i2['DIRECTION'] or i1['DIRECTION'] == i2['DIRECTION'] + 1 or i1['DIRECTION'] == i2['DIRECTION'] - 1:
			if i1['DIRECTION'] == 1:
				if i1['RECT'].x < i2['RECT'].x: return 2
				elif i1['RECT'].x > i2['RECT'].x: return 3
				else: return 1
			elif i1['DIRECTION'] == 2:
				if i1['RECT'].x < i2['RECT'].y: return 2
				elif i1['RECT'].x > i2['RECT'].y: return 3
				else: return 1
			elif i1['DIRECTION'] == 3:
				if i1['RECT'].y < i2['RECT'].y: return 2
				elif i1['RECT'].y > i2['RECT'].y: return 3
				else: return 1
			elif i1['DIRECTION'] == 4:
				if i1['RECT'].y < i2['RECT'].y: return 2
				elif i1['RECT'].y > i2['RECT'].y: return 3
				else: return 1
			elif i1['DIRECTION'] == 5:
				if i1['RECT'].x > i2['RECT'].x: return 2
				elif i1['RECT'].x < i2['RECT'].x: return 3
				else: return 1
			elif i1['DIRECTION'] == 6:
				if i1['RECT'].x > i2['RECT'].y: return 2
				elif i1['RECT'].x < i2['RECT'].y: return 3
				else: return 1
			elif i1['DIRECTION'] == 7:
				if i1['RECT'].y > i2['RECT'].y: return 2
				elif i1['RECT'].y < i2['RECT'].y: return 3
				else: return 1
			elif i1['DIRECTION'] == 8:
				if i1['RECT'].y > i2['RECT'].y: return 2
				elif i1['RECT'].y < i2['RECT'].y: return 3
				else: return 1
		else: return 1

	def events(self):
		#EXIT GAME
		for event in pygame.event.get():
			if event.type == pygame.VIDEORESIZE:
				self.windowh = event.h
				sh = int(event.h/4)
				self.windoww = 6 * sh
				self.screen = pygame.display.set_mode((self.windoww, self.windowh), pygame.RESIZABLE)
				self.FPS = int(event.w/20)
			if event.type == pygame.QUIT:
				menu.recent_data(1)
				pygame.quit()
				sys.exit()

			self.pressed = pygame.key.get_pressed()
			if self.pressed[pygame.K_DELETE]:
				self.__init__()
				self.rendermap('urban_0')
				self.transiction(False,0)
			if self.pressed[pygame.K_9]:
				database.CHARACTERS[database.PARTY[database.FORMATION][0]]['HEALTH'] -= 1
			if self.pressed[pygame.K_0]:
				database.CHARACTERS[database.PARTY[database.FORMATION][0]]['HEALTH'] += 1

			#BATTLE OPTIONS
			if self.battle == True and self.phone == 0:
				self.pressed = pygame.key.get_pressed()
				if self.turn == len(database.PARTY[database.FORMATION]): self.fight()

				if self.mnu == 2:
					if self.equip[self.turn] == 4:
						if self.pressed[database.LEFT]: self.opt -= 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.pressed[database.RIGHT]: self.opt += 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])


					if self.pressed[database.ACT]:
						if self.equip[self.turn] < 4:
							self.fight()
							self.turn += 1
							self.mnu = 1
							if self.turn == len(database.PARTY[database.FORMATION]): self.fight()
						elif self.equip[self.turn] == 4:
							ttl = self.opt
							for i in self.fig:
								self.equip[self.turn] = database.TACTICAL[ttl][self.turn]
								if self.equip[self.turn] != 0:
									if self.equip[self.turn] + 1 < 5:
										self.equip[self.turn] -= 1
										self.ch_sfx.play(database.SOUND['GUN_TRIGGER'])
										self.mnu = 2
										self.wait()
									if self.equip[self.turn] != 6: self.fight()
									else:
										self.pres[self.turn] += 3
										self.ch_sfx.play(database.SOUND['GUARD'])
										self.dialog([self.fig[self.turn]['NAME'] + ' está em guarda'])
								self.turn += 1
							for i in self.equip: i = 4

					if self.opt < 0: self.opt = len(database.TACTICAL) - 1
					if self.opt > len(database.TACTICAL) - 1: self.opt = 0

				elif self.mnu == 1:
					if self.pressed[database.LEFT]: self.equip[self.turn] -=1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: self.equip[self.turn] +=1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
				
					if self.equip[self.turn] < 0: self.equip[self.turn] = 7
					if self.equip[self.turn] > 7: self.equip[self.turn] = 0

					if self.pressed[database.ACT]:
						if self.equip[self.turn] < 4:
							if int(database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1]) > 0:
								self.ch_sfx.play(database.SOUND['GUN_TRIGGER'])
								self.mnu = 2
							else:
								self.ch_sfx.play(database.SOUND['ERROR'])
						elif self.equip[self.turn] == 4:
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.mnu = 2
						elif self.equip[self.turn] == 5:
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.fight()
							self.turn += 1
						elif self.equip[self.turn] == 6:
							self.ch_ton.play(database.SOUND['GUARD'])
							self.pres[self.turn] += 3
							self.dialog([self.fig[self.turn]['NAME'] + ' está em guarda'])
							self.turn += 1
							if self.turn == len(self.fig): self.fight()
						elif self.equip[self.turn] == 7:
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.fight()
							if self.battle == True:
								self.turn = len(database.PARTY[database.FORMATION])
								self.fight()

			#SHOP OPTIONS
			if self.shp == True:
				if self.pressed[database.LEFT]: self.opt -= 1 ; self.ch_sfx.play(database.SOUND['MENU_HOR'])
				if self.pressed[database.RIGHT]: self.opt += 1 ; self.ch_sfx.play(database.SOUND['MENU_HOR'])
				if self.pressed[database.UP]: self.lopt -= 1 ; self.ch_sfx.play(database.SOUND['MENU_VER'])
				if self.pressed[database.DOWN]: self.lopt += 1 ; self.ch_sfx.play(database.SOUND['MENU_VER'])

				if self.mnu == 0:
					if self.pressed[database.ACT]:
						if self.lopt < len(self.products):
							for i in range(self.opt): self.basket.append(self.products[self.lopt])
							self.ch_sfx.play(database.SOUND['MENU_GO'])
						else:
							self.ch_sfx.play(database.SOUND['MENU_BACK'])
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
								if database.MONEY >= database.ITEMS[i][2]:
									if self.inv.space(0) == False:
										self.dialog(database.DIALOGS['MERCATOR'][2])
									elif self.confirmation() == 1:
										self.inv.add(0,i)
										self.ch_sfx.play(database.SOUND['BUY'])
										database.MONEY -= database.ITEMS[i][2] - int(database.ITEMS[i][2]/self.promo)
								else:
									self.ch_sfx.play(database.SOUND['ERROR'])
									self.dialog(database.DIALOGS['MERCATOR'][1])
						else:
							self.ch_sfx.play(database.SOUND['MENU_BACK'])
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 1
					if self.lopt < 0: self.lopt = 1
					if self.lopt > 1: self.lopt = 0

				if self.mnu == 2:
					if self.pressed[database.ACT]:
						if self.opt == 0:
							if self.lopt == len(self.products):
								self.ch_sfx.play(database.SOUND['MENU_BACK'])
								self.shp = False
								self.lopt = 0
							else:
								if database.MONEY >= database.ITEMS[self.products[self.lopt]][2]:
									if self.inv.space(0) == False:
										self.dialog(database.DIALOGS['MERCATOR'][2])
									elif self.confirmation() == 1:
										self.inv.add(0,self.products[self.lopt])
										self.ch_sfx.play(database.SOUND['BUY'])
										database.MONEY -= database.ITEMS[self.products[self.lopt]][2] - int(database.ITEMS[self.products[self.lopt]][2]/self.promo)
								else:
									self.ch_sfx.play(database.SOUND['ERROR'])
									self.dialog(database.DIALOGS['MERCATOR'][1])
						else:
							if self.lopt == len(self.basket):
								self.ch_sfx.play(database.SOUND['MENU_BACK'])
								self.shp = False
								self.lopt = 0
							elif self.confirmation() == 1:
								database.MONEY += int(database.ITEMS[database.INVENTORY[self.basket[self.lopt][0]][self.basket[self.lopt][1]][self.basket[self.lopt][2]][0]][2]/2)
								database.INVENTORY[self.basket[self.lopt][0]][self.basket[self.lopt][1]][self.basket[self.lopt][2]] = ['_','0000','_','_']
								del self.basket[self.lopt]
								self.ch_sfx.play(database.SOUND['SELL'])


					if self.opt < 0: self.opt = len(database.PARTY[database.FORMATION])
					if self.opt > len(database.PARTY[database.FORMATION]): self.opt = 0
					if self.opt == 0:
						if self.lopt < 0: self.lopt = len(self.products)
						if self.lopt > len(self.products): self.lopt = 0
					else:
						ln = 1
						for i in self.basket:
							if i[0] == self.opt - 1: ln += 1
						if self.lopt < 0: self.lopt = ln
						if self.lopt > ln: self.lopt = 0

				if self.mnu == 11 or self.mnu == 12:
					if self.pressed[database.ACT]:
						self.ch_sfx.play(database.SOUND['CASH_GET'])
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
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.mnu = 11
							self.lopt = 0
							self.opt = 5
						if self.lopt == 1:
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.mnu = 12
							self.lopt = 0
							self.opt = 5
						if self.lopt == 2:
							self.ch_sfx.play(database.SOUND['MENU_BACK'])
							self.shp = False
							self.lopt = 0

					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

			#INVENTORY OPTIONS
			if self.pressed[database.BAG] and self.phone == 0 and self.shp == False and self.inv.itmov == '':
				if self.inventory > 0:
					self.inventory = 0
					self.ch_sfx.play(database.SOUND['INVENTORY_CLOSE'])
					self.player['PAUSE'] = 0
					if self.battle == True: self.mnu = 1
				elif self.inventory == 0:
					self.inventory = 1
					self.ch_sfx.play(database.SOUND['INVENTORY_OPEN'])
					self.player['PAUSE'] = 1
					self.invfade = 0
					self.opt = 0
					self.lopt = 1
					self.mnu = 0

			if self.inventory > 0:
				if self.inv.itmov != '':
					if self.inv.itmov[0] == 0:
						if self.pressed[database.LEFT]:
							if self.exvar > 1: self.exvar -= 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.pressed[database.RIGHT]:
							if self.exvar < 3: self.exvar += 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					else:
						if self.pressed[database.LEFT]: self.opt -= 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.pressed[database.RIGHT]: self.opt += 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
				else:
					if self.pressed[database.LEFT]: self.opt -= 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: self.opt += 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

				if self.pressed[database.ACT]:
					if self.inv.itmov == '':
						if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('food') and database.CHARACTERS[database.PARTY[database.FORMATION][0]]['HEALTH'] != 10:
							self.ch_ton.play(database.SOUND['HEAL'])
							hl = database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0]][5]
							if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][2] != '_': hl += database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][2]][5]
							if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][3] != '_': hl += database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][3]][5]
							if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] in database.CHARACTERS[self.mnu]['FAVFOOD']:
								hl += int(hl/2)
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['HP'] += hl
							if database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['HP'] > database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL']]:
								database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['HP'] = database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL']]
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('repellent'):
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['HEALTH'] = 2
							wtm = database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0]][5]
							wtm += database.TIME[1]
							self.waitime.append(['repellent' + str(database.PARTY[database.FORMATION][self.mnu]),wtm])
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_strenght':
							self.ch_ton.play(database.SOUND['ATTRIBUTE_GAIN'])
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_attack':
							self.ch_ton.play(database.SOUND['ATTRIBUTE_GAIN'])
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_agility':
							self.ch_ton.play(database.SOUND['ATTRIBUTE_GAIN'])
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_resistance':
							self.ch_ton.play(database.SOUND['ATTRIBUTE_GAIN'])
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_vitality':
							self.ch_ton.play(database.SOUND['ATTRIBUTE_GAIN'])
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_mistery':
							self.ch_ton.play(database.SOUND['ATTRIBUTE_GAIN'])
							database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('locksmith'):
							self.ch_ton.play(database.SOUND['MENU_GO'])
							self.inv.itmov = [0,database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][2],database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][3]]
							self.exvar = 1

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'wallet':
							self.ch_ton.play(database.SOUND['MENU_GO'])
							self.inv.itmov = [0,database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][2],database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][3]]
							self.exvar = 1

						else: self.ch_ton.play(database.SOUND['ERROR'])

						if self.battle == True:
							self.turn += 1
							self.mnu = 1
							self.inventory = 0

					elif self.inv.itmov[0] == 0:
						if self.exvar == 3:
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.inv.itmov = ''
						else: self.ch_ton.play(database.SOUND['ERROR'])

					elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_':
						craft = False
						if self.inv.itmov[0].startswith('key') and database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('locksmith'): craft = True
						if self.inv.itmov[0].startswith('id_card') and database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('wallet'): craft = True
						if self.inv.itmov[0].startswith('credit_card') and database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('wallet'): craft = True
						elif self.inv.itmov[0].startswith('condiment') and database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('food'): craft = True
						elif self.inv.itmov[0].startswith('acc') and database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('gun'): craft = True

						if craft == True:
							if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][2] == '_':
								self.ch_ton.play(database.SOUND['CRAFT'])
								database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][2] = self.inv.itmov[0]
								database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1] = self.inv.itmov[1] + database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1]
								self.inv.itmov = ''
							elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][3] == '_':
								self.ch_ton.play(database.SOUND['CRAFT'])
								database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][3] = self.inv.itmov[0]
								database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1] += self.inv.itmov[1]
								self.inv.itmov = ''
							else: self.ch_ton.play(database.SOUND['ERROR']); self.shake = 5

						elif self.inv.itmov[0].startswith('ammo') and database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('gun'):
							self.ch_ton.play(database.SOUND['GUN_RECHARGE'])
							if int(database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][4][self.equip[self.mnu] + 1][1]) > 0:
								plus = int(100/(database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][4][self.equip[self.mnu] + 1][0]][5]['CAPACITY']/int(database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][4][self.equip[self.mnu] + 1][1])))
							else: plus = 0
							while self.barpp[self.mnu][self.equip[self.mnu]] < plus:
								self.barpp[self.mnu][self.equip[self.mnu]] += 1
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1] = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1]
							self.inv.itmov = ''

						else: self.ch_ton.play(database.SOUND['ERROR']); self.inv.shake = 5

						if self.battle == True:
							self.turn += 1
							self.mnu = 1
							self.inventory = 0

				if self.pressed[database.RUN]:
					if self.inventory == 1:
						if self.inv.itmov != '':
							if self.inv.itmov[0] == 0:
								if self.inv.itmov[self.exvar] != '_':
									self.ch_sfx.play(database.SOUND['MENU_GO'])
									itm = self.inv.itmov[self.exvar]
									database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][self.exvar + 1] = '_'
									if self.exvar == 1:
										prp = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1][0:4]
										database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1] = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1][4:8]
									if self.exvar == 2:
										if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][2] == '_':
											prp = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1][0:4]
											database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1] = ''
										else:
											prp = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1][4:8]
											database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1] = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][1][0:4]
									self.inv.itmov = [itm,prp,'_','_']
								else: self.ch_sfx.play(database.SOUND['ERROR']); self.inv.shake = 5

							elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == '_' and self.inv.space(database.PARTY[database.FORMATION][self.mnu],self.exvar,self.opt,self.lopt) == True:
								self.ch_sfx.play(database.SOUND['EQUIP'])
								database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
								if self.inv.itmov[0].startswith('clth'):
									database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['COSTUME'] = database.ITEMS[self.inv.itmov[0]][5] + database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['SKIN']
								self.inv.itmov = ''

								if self.battle == True:
									self.turn += 1
									self.mnu = 1
									self.inventory = 0

							elif self.inv.space(self.mnu,self.exvar,self.opt,self.lopt) == True:
								self.ch_sfx.play(database.SOUND['EQUIP'])
								trd = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt]
								database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
								if self.inv.itmov[0].startswith('clth'):
									database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['COSTUME'] = database.ITEMS[self.inv.itmov[0]][5] + database.CHARACTERS[database.PARTY[database.FORMATION][self.mnu]]['SKIN']
								self.inv.itmov = trd

							else: self.ch_sfx.play(database.SOUND['ERROR']); self.inv.shake = 5

						elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_':
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.inv.itmov = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt]
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

					if self.inventory == 2:
						if self.exvar == 0:
							if self.inv.itmov != '':
								if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] == '_': 
									self.ch_sfx.play(database.SOUND['EQUIP'])
									database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
									self.inv.itmov = ''
								else:
									self.ch_sfx.play(database.SOUND['EQUIP'])
									trd = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt]
									database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
									self.inv.itmov = trd
							elif database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_':
								self.ch_sfx.play(database.SOUND['MENU_GO'])
								self.inv.itmov = database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt]
								database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']
						if self.exvar == 1:
							if self.inv.itmov != '':
								if database.STORAGE[self.opt][0] == '_':
									self.ch_sfx.play(database.SOUND['EQUIP'])
									database.STORAGE[self.opt] = self.inv.itmov
									self.inv.itmov = ''
								else:
									self.ch_sfx.play(database.SOUND['EQUIP'])
									trd = database.STORAGE[self.opt]
									database.STORAGE[self.opt] = self.inv.itmov
									self.inv.itmov = trd
							elif database.STORAGE[self.opt][0] != '_':
								self.ch_sfx.play(database.SOUND['MENU_GO'])
								self.inv.itmov = database.STORAGE[self.opt]
								database.STORAGE[self.opt] = ['_','0000','_','_']
					elif self.inventory == 3:
						if database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_' and self.confirmation() == 1:
							database.INVENTORY[database.PARTY[database.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

				if self.inventory == 1:
					if self.opt < 0: self.opt = 4; self.mnu -= 1
					if self.opt > 4: self.opt = 0; self.mnu += 1
					if self.lopt < 0: self.lopt = 4
					if self.lopt > 4: self.lopt = 0
				if self.inventory == 2:
					if self.lopt < 0: self.lopt = 4; self.mnu -= 1
					if self.lopt > 4: self.lopt = 0; self.mnu += 1
					if self.opt < 0: self.opt = 4; self.exvar -= 1
					if self.opt > 4: self.opt = 0; self.exvar += 1
					if self.exvar < 0: self.exvar = 1
					if self.exvar > 1: self.exvar = 0

				if self.mnu < 0: self.mnu = len(database.PARTY[database.FORMATION]) - 1
				if self.mnu > len(database.PARTY[database.FORMATION]) - 1: self.mnu = 0

			#PHONE OPTIONS
			if self.pressed[database.PHONE] and self.inv.find(0,'phone') != None and self.inventory == 0 and self.shp == False and self.nmenu.show == False:
				if self.phone == 0 or self.phone > 1:
					if self.phone == 0:
						self.player['HEAD'] = 'BLANKDD_0' + str(database.PARTY[database.FORMATION][0]) + '0'
						self.player['SPRITE'] = 'PHONE_' + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['COSTUME'] + str(database.PARTY[database.FORMATION][0])
						self.opt = 0; self.lopt = 0; self.player['PAUSE'] = 1
					if self.phone == 2: self.opt = 0; self.lopt = 0; self.phn.scroll = 0
					if self.phone == 3: self.opt = 1; self.lopt = 0; self.phn.scroll = 0
					if self.phone == 4: self.opt = 2; self.lopt = 0; self.phn.scroll = 0
					if self.phone == 5: self.opt = 0; self.lopt = 1; self.phn.scroll = 0
					if self.phone == 6: self.opt = 1; self.lopt = 1; self.phn.scroll = 0; self.ch_ton.stop(); self.ch_ton.set_volume(database.SFX)
					if self.phone == 7: self.opt = 2; self.lopt = 1; self.phn.scroll = 0
					if self.phone == 8: self.opt = 0; self.lopt = 2; self.phn.scroll = 0
					if self.phone == 9: self.opt = 1; self.lopt = 2; self.phn.scroll = 0
					if self.phone == 10: self.opt = 2; self.lopt = 2; self.phn.scroll = 0
					if self.phone == 11: self.opt = 0; self.lopt = 3; self.phn.scroll = 60
					if self.phone == 12: self.opt = 1; self.lopt = 3; self.phn.scroll = 60
					if self.phone == 13: self.opt = 2; self.lopt = 3; self.phn.scroll = 60
					if self.phone == 14: self.opt = 0; self.lopt = 4; self.phn.scroll = 120
					if self.phone == 15: self.opt = 1; self.lopt = 4; self.phn.scroll = 120
					if self.phone == 16: self.opt = 2; self.lopt = 4; self.phn.scroll = 120
					if self.phone == 17: self.opt = 0; self.lopt = 5

					if self.phone == 0 and self.battle == True:
						self.phone = 18
						self.mnu = 2
					elif self.nb != '':
						if self.phone == 0: self.phone = 17; self.opt = 0
						elif self.phone == 17: self.phone = 0
					else:
						if self.phone > 1: self.ch_sfx.play(database.SOUND['MENU_BACK'])
						self.phone = 1
						self.mnu = 0

				else:
					self.phone = 0
					if self.battle == False:
						self.opt = 0
						self.lopt = 0
						self.player['PAUSE'] = 0
					else:
						self.mnu = 1

			if self.phone > 0 and database.BATTERY > 1.0:
				if self.phone == 1:
					if self.pressed[database.UP]: self.lopt -=1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN]: self.lopt +=1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.LEFT]: self.opt -=1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: self.opt +=1; self.ch_sfx.play(database.SOUND['MENU_HOR'])

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = 4
					if self.lopt > 4: self.lopt = 0

					if self.pressed[database.ACT]:
						if self.lopt == 0:
							if self.opt == 0: self.phone = 2; self.opt = round(self.player['RECT'].x/30); self.lopt = round(self.player['RECT'].x/30); self.mnu = 375
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

						if self.phone == 7: menu.recent_data(0)

						self.ch_sfx.play(database.SOUND['MENU_GO'])
						self.phn.scroll = 0
						self.opt = 0
						self.lopt = 0
						self.mnu = 0

				elif self.phone == 3:
					if self.pressed[database.LEFT]:
						self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.mnu == 0: self.opt -=1; self.lopt = 0
						elif self.mnu < 3: self.mnu = 1
						else:
							self.mnu -=1
							if self.mnu < 3: self.mnu = 5

					if self.pressed[database.RIGHT]:
						self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.mnu == 0: self.opt +=1; self.lopt = 0
						elif self.mnu < 3: self.mnu = 2
						else:
							self.mnu +=1
							if self.mnu > 5: self.mnu = 3

					if self.pressed[database.UP]:
						self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.mnu < 3: self.lopt -= 1
						else:
							self.exvar -= 1
							if self.exvar < 0: self.exvar = 5
							database.PARTY[self.lopt][self.mnu - 3] = self.exvar

					if self.pressed[database.DOWN]:
						self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.mnu < 3: self.lopt += 1
						else:
							self.exvar += 1
							if self.exvar > 5: self.exvar = 0
							database.PARTY[self.lopt][self.mnu - 3] = self.exvar

					if self.opt == 0:
						if self.lopt < 0: self.lopt = len(database.PARTY)
						if self.lopt > len(database.PARTY): self.lopt = 0

						if self.pressed[database.ACT]:
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							if self.lopt < len(database.PARTY):
								if self.mnu == 0:
									self.mnu = 1
								elif self.mnu == 1:
									database.FORMATION = self.lopt
									for i in database.PARTY[database.FORMATION]:
										database.CHARACTERS[i]['HP'] = database.CHARACTERS[i]['VITALITY'][database.CHARACTERS[i]['LEVEL']]
									self.ch_ton.play(database.SOUND['PARTY_CHANGE'])
									self.phn.pbg = database.PARTY[database.FORMATION][0]
									self.mnu = 0
									self.opt = 0
									self.lopt = 0
								elif self.mnu > 2:
									database.party_make(self.lopt)
									self.mnu = 0
								elif len(database.PARTY) > 1:
									del database.PARTY[self.lopt]
									self.mnu = 0 
							else:
								database.PARTY.append([0,0,0])
								self.exvar = 0
								self.mnu = 3

					if self.opt == 1:
						if self.lopt < 0: self.lopt = len(database.CONTACTS) - 1
						if self.lopt > len(database.CONTACTS) - 1: self.lopt = 0

						if self.pressed[database.ACT]:
							if self.mnu == 0:
								pygame.time.wait(round(random.randint(10,200)))

								if database.CREDIT > 0:
									database.CREDIT -= 1
									database.CALLHIST.insert(0,[database.CONTACTS[self.lopt][1],False])
									self.player['SPRITE'] = 'CALL_' + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['COSTUME'] + str(database.PARTY[database.FORMATION][0])
									self.phone = 0
									self.dialog(database.DIALOGS[database.CONTACTS[self.lopt][1]][0])
									self.player['PAUSE'] = 1
									self.player['SPRITE'] = 'PHONE_' + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['COSTUME'] + str(database.PARTY[database.FORMATION][0])
									self.phone = 3
								else:
									self.dialog([database.MENU[17]])

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0

				elif self.phone == 4 and self.signal > 0:
					if self.mnu == 0:
						if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.LEFT]: self.opt -= 1; self.lopt = 0; self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.pressed[database.RIGHT]: self.opt += 1; self.lopt = 0; self.ch_sfx.play(database.SOUND['MENU_HOR'])

					if self.pressed[database.ACT] and self.signal > 0:
						if self.mnu == 0: self.mnu = 1; self.ch_sfx.play(database.SOUND['MENU_GO'])
						elif self.mnu > 0:
							self.ch_sfx.play(database.SOUND['MENU_BACK'])
							if self.opt == 0: self.phn.e_unread[self.lopt][3] = 1
							if self.opt == 2: database.EMAILS[self.lopt][3] = 1
							self.mnu = 0

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = len(database.EMAILS) - 1
					if self.lopt > len(database.EMAILS) - 1: self.lopt = 0

				elif self.phone == 5 and self.signal > 0:
					if self.mnu == 0:
						if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

					if self.pressed[database.ACT]:
						self.ch_sfx.play(database.SOUND['MENU_GO'])
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.lopt < 0: self.lopt = 3
					if self.lopt > 3: self.lopt = 0

				elif self.phone == 6 and self.signal > 0:
					if self.pressed[database.ACT]:
						self.radonoff = not self.radonoff
					if self.radonoff == False and pygame.mixer.music.get_busy() == True:
						self.ch_sfx.play(database.SOUND['MENU_BACK'])
						self.ch_ton.stop()
						pygame.mixer.music.stop()
					else:
						self.ch_sfx.play(database.SOUND['MENU_GO'])
						self.ch_ton.play(database.SOUND['NOISE'],-1)

				elif self.phone == 7 and self.signal > 0:
					if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

					if self.pressed[database.ACT] and self.signal > 0:
						self.ch_sfx.play(database.SOUND['FILE_SAVE'])
						database.PX = self.player['RECT'].x
						database.PY = self.player['RECT'].y
						database.ID = self.lopt
						if self.lopt < len(menu.FILES[0]): database.save_data(); menu.recent_data(1,self.lopt); menu.recent_data(0)
						else: database.new_data(); database.save_data(); menu.recent_data(2,self.lopt); menu.recent_data(0)

				elif self.phone == 8 and self.signal > 0:
					if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

					if self.pressed[database.ACT]:
						if self.mnu == 0: self.mnu = 1; self.ch_sfx.play(database.SOUND['MENU_GO'])
						elif self.mnu > 0: self.mnu = 0; self.ch_sfx.play(database.SOUND['MENU_BACK'])

					if self.mnu == 0:
						if self.lopt < 0: self.lopt = len(database.BESTIARY) - 1
						if self.lopt > len(database.BESTIARY) - 1: self.lopt = 0

					if self.mnu > 0:
						if self.pressed[database.LEFT]: self.mnu = 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.pressed[database.RIGHT]: self.mnu = 2; self.ch_sfx.play(database.SOUND['MENU_HOR'])

						if self.lopt < 0: self.lopt = 3
						if self.lopt > 3: self.lopt = 0

				elif self.phone == 9:
					if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.LEFT]: self.opt -= 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: self.opt += 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = len(database.TASKS) - 1
					if self.lopt > len(database.TASKS) - 1: self.lopt = 0

				elif self.phone == 10:
					if self.pressed[database.LEFT]: self.opt -= 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: self.opt += 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])

					if self.opt < 0: self.opt = len(database.PARTY[database.FORMATION]) - 1
					if self.opt > len(database.PARTY[database.FORMATION]) - 1: self.opt = 0

				elif self.phone == 11:
					if self.mnu == 0:
						if self.pressed[database.ACT]:
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							if self.lopt == len(database.TACTICAL):
								database.TACTICAL.append([0,0,0,0])
							self.mnu = 1
							self.opt = database.TACTICAL[self.lopt][self.mnu - 1]

						if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

						if self.lopt < 0: self.lopt = len(database.TACTICAL)
						if self.lopt > len(database.TACTICAL): self.lopt = 0

					elif self.mnu > 0:
						if self.pressed[database.ACT]:
							self.ch_sfx.play(database.SOUND['MENU_BACK'])
							if self.mnu < 5:
								database.tact_save(self.lopt)
								self.mnu = 0
							else:
								del database.TACTICAL[self.lopt]
								self.mnu = 0

						if self.pressed[database.UP]: self.opt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.DOWN]: self.opt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.LEFT]: self.mnu -= 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
						if self.pressed[database.RIGHT]: self.mnu += 1; self.ch_sfx.play(database.SOUND['MENU_HOR'])

						if self.mnu > 0:
							if self.mnu < 1: self.mnu = 5
							if self.mnu > 5: self.mnu = 1
							if self.opt < 0: self.opt = 7
							if self.opt > 7: self.opt = 0

							if self.pressed[database.LEFT] or self.pressed[database.RIGHT]:
								if self.mnu < 5 and len(database.TACTICAL) > 0: self.opt = database.TACTICAL[self.lopt][self.mnu - 1]
							else:
								if self.mnu < 5 and len(database.TACTICAL) > 0: database.TACTICAL[self.lopt][self.mnu - 1] = self.opt

				elif self.phone == 12:
					if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

					if self.lopt < 0: self.lopt = len(database.ACHIEVEMENTS) - 1
					if self.lopt > len(database.ACHIEVEMENTS) - 1: self.lopt = 0

				elif self.phone == 14:
					if self.mnu == 0:
						if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
						if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

					if self.pressed[database.ACT]:
						if self.mnu == 0: self.mnu = 1; self.ch_sfx.play(database.SOUND['MENU_GO'])
						elif self.mnu > 0: self.mnu = 0; self.ch_sfx.play(database.SOUND['MENU_BACK'])

					if self.lopt < 0: self.lopt = len(database.MANUAL) - 1
					if self.lopt > len(database.MANUAL) - 1: self.lopt = 0

				elif self.phone == 15:
					if self.pressed[database.UP]: self.lopt -= 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN]: self.lopt += 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

					if self.mnu == 0:
						if self.lopt < 0: self.lopt = 3
						if self.lopt > 3: self.lopt = 0
					if self.mnu == 1:
						if self.lopt < 0: self.lopt = 5
						if self.lopt > 5: self.lopt = 0
					if self.mnu == 2:
						if self.lopt < 0: self.lopt = 1
						if self.lopt > 1: self.lopt = 0
					if self.mnu == 3:
						if self.lopt < 0: self.lopt = 7
						if self.lopt > 7: self.lopt = 0

					if self.mnu == 0:
						if self.pressed[database.ACT]:
							if self.lopt == 3:
								self.phn = menu.Phone()
								self.inv = menu.Inventory()
								self.shpmnu = menu.Shop()
								database.save_sett()
								self.ch_sfx.play(database.SOUND['MENU_GO'])
								self.opt = 1
								self.lopt = 4
								self.phone = 1
								if database.CHAPTER == 0:
									self.ch_ton.play(database.SOUND['CALLING'],-1)
									self.ch_rng.play(database.SOUND['RINGTONE_' + str(self.phn.pbg)],-1)
									self.phone = 17
									self.nb = '977904623'
							else:
								self.mnu = self.lopt + 1
								self.opt = 0
								self.lopt = 0

					elif self.mnu == 1:

						if self.lopt == 0:
							if self.pressed[database.LEFT]:
								database.LANG = 'EN'; self.ch_sfx.set_volume(database.SFX); self.ch_sfx.play(database.SOUND['MENU_HOR'])
							if self.pressed[database.RIGHT]:
								database.LANG = 'PT'; self.ch_sfx.set_volume(database.SFX); self.ch_sfx.play(database.SOUND['MENU_HOR'])
					
						if self.lopt == 1:
							if self.pressed[database.LEFT]: database.SPEED += 1; self.ch_sfx.set_volume(database.SFX); self.ch_sfx.play(database.SOUND['MENU_HOR'])
							if self.pressed[database.RIGHT]: database.SPEED -= 1; self.ch_sfx.set_volume(database.SFX); self.ch_sfx.play(database.SOUND['MENU_HOR'])

							if database.SPEED < 1: database.SPEED = 5
							if database.SPEED > 5: database.SPEED = 1

						if self.lopt == 5:
							if self.pressed[database.LEFT]: database.BORDER -= 1; self.ch_sfx.set_volume(database.SFX); self.ch_sfx.play(database.SOUND['MENU_HOR'])
							if self.pressed[database.RIGHT]: database.BORDER += 1; self.ch_sfx.set_volume(database.SFX); self.ch_sfx.play(database.SOUND['MENU_HOR'])

							if database.BORDER < 0: database.BORDER = 5
							if database.BORDER > 5: database.BORDER = 0

					elif self.mnu == 3:
						if self.lopt == 0:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.DOWN,database.LEFT,database.RIGHT,database.ACT,database.PHONE,database.BAG,database.RUN):
										database.UP = event.key; self.opt = 0

						if self.lopt == 1:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.UP,database.LEFT,database.RIGHT,database.ACT,database.PHONE,database.BAG,database.RUN):
										database.DOWN = event.key; self.opt = 0

						if self.lopt == 2:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.DOWN,database.UP,database.RIGHT,database.ACT,database.PHONE,database.BAG,database.RUN):
										database.LEFT = event.key; self.opt = 0

						if self.lopt == 3:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.DOWN,database.LEFT,database.UP,database.ACT,database.PHONE,database.BAG,database.RUN):
										database.RIGHT = event.key; self.opt = 0

						if self.lopt == 4:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.DOWN,database.LEFT,database.RIGHT,database.UP,database.PHONE,database.BAG,database.RUN):
										database.ACT = event.key; self.opt = 0

						if self.lopt == 5:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.DOWN,database.LEFT,database.RIGHT,database.UP,database.PHONE,database.BAG,database.ACT):
										database.RUN = event.key; self.opt = 0

						if self.lopt == 6:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.DOWN,database.LEFT,database.RIGHT,database.ACT,database.UP,database.BAG,database.RUN):
										database.PHONE = event.key; self.opt = 0

						if self.lopt == 7:
							if self.pressed[database.ACT]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (database.DOWN,database.LEFT,database.RIGHT,database.ACT,database.PHONE,database.UP,database.RUN):
										database.BAG = event.key; self.opt = 0


					if self.pressed[database.RUN]:
						if self.mnu > 0:
							self.ch_sfx.play(database.SOUND['MENU_BACK'])
							self.mnu = 0

				elif self.phone == 16:
					if self.pressed[database.UP] and self.lopt == 1: self.lopt = 0; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.DOWN] and self.lopt == 0: self.lopt = 1; self.ch_sfx.play(database.SOUND['MENU_VER'])

					if self.pressed[database.ACT]:
						self.ch_sfx.play(database.SOUND['MENU_GO'])
						if self.lopt == 0:
							webbrowser.get('windows-default').open('twitter.com/kaixtr')
						if self.lopt == 1:
							webbrowser.get('windows-default').open('github.com/kaixtr')

				elif self.phone == 17:
					if self.pressed[database.LEFT] and self.opt == 1: self.opt = 0; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.RIGHT] and self.opt == 0: self.opt = 1; self.ch_sfx.play(database.SOUND['MENU_VER'])
					if self.pressed[database.ACT]:
						self.ch_ton.stop()
						self.ch_rng.stop()
						if self.opt == 0:
							self.phone = 0
							self.ch_sfx.play(database.SOUND['MENU_GO'])
							self.player['DIRECTION'] = 0
							self.player['SPD'] = 0
							self.player['SPRITE'] = 'CALL_' + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['COSTUME'] + str(database.PARTY[database.FORMATION][0])
							if self.dlgfa > 0:
								self.dialog(database.DIALOGS[self.nb][0])
								database.CALLHIST.append([self.nb,True])
								self.player['SPRITE'] = 'STANDD_' + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['COSTUME'] + str(database.PARTY[database.FORMATION][0])
						elif self.opt == 1:
							self.ch_sfx.play(database.SOUND['MENU_BACK'])
							self.phone = 1
						self.nb = ''
						if self.radonoff == True: pygame.mixer.music.unpause()
						if database.CHAPTER == 0:
							self.phone = 0
							self.transiction(False, 50)
							self.dialog(database.DIALOGS['DALIBOR'][0])

				elif self.phone == 18:
					if self.pressed[database.ACT]:
						trg = self.foe[0]
						f = {'N': trg['FILE']}
						f['DATE'] = str(database.DATE[0]) + '/' + str(database.DATE[1])
						i = len(database.BESTIARY) + 1
						if i < 10: i = '00' + str(i)
						elif i < 40: i = '0' + str(i)
						f['ID'] = i
						database.BESTIARY.append(f)
						self.ch_sfx.play(database.SOUND['CAMERA'])
						self.phone = 0
						self.mnu = 1
						self.notification(trg['NAME'] + ' registrada',(134, 0, 211))
						database.best_regs(f)
			
			if self.battle == False and self.inventory == 0 and self.phone == 0 and self.shp == False and self.sleepin == False:
				if self.driving > 0:
					if database.GAS > 0:
						if self.pressed[database.LEFT]:
							self.player['DIRECTION'] -= 1
							if self.player['DIRECTION'] == 0: self.player['DIRECTION'] = 8

						elif self.pressed[database.RIGHT]:
							self.player['DIRECTION'] += 1
							if self.player['DIRECTION'] == 9: self.player['DIRECTION'] = 1

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
			if self.pressed[database.LEFT]: self.fm -=1; self.vm -= 0.05
			if self.pressed[database.RIGHT]: self.fm +=1; self.vm += 0.05

			if self.fm < 0: self.fm = 180
			if self.fm > 180: self.fm = 0
			if self.vm < 0.0: self.vm = 1.0
			if self.vm > 1.0: self.vm = 0.0

			pygame.mixer.music.set_volume(self.vm)
			self.ch_ton.set_volume(1 - self.vm)
			if self.vm == 0.0 and self.radonoff == True:
				if database.RADIO[str(math.floor(self.fm/20))] != []:
					pygame.mixer.music.load('Songs/FM_' + str(math.floor(self.fm/20)) + '/' + database.RADIO[str(math.floor(self.fm/20))][self.msc])
					pygame.mixer.music.play()
				else: pygame.mixer.music.stop()

		elif self.phone == 13:
			if self.mnu > 0:
				if self.pressed[database.UP]: self.mnu -=1
				if self.pressed[database.DOWN]: self.mnu +=1
						
				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 15:
			if self.mnu == 1:
				if self.lopt == 2:
					if self.pressed[database.LEFT]: database.COLOR[0] -= 2; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: database.COLOR[0] += 2; self.ch_sfx.play(database.SOUND['MENU_HOR'])

					if database.COLOR[0] < 30: database.COLOR[0] = 242
					if database.COLOR[0] > 242: database.COLOR[0] = 30
				if self.lopt == 3:
					if self.pressed[database.LEFT]: database.COLOR[1] -= 2; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: database.COLOR[1] += 2; self.ch_sfx.play(database.SOUND['MENU_HOR'])

					if database.COLOR[1] < 30: database.COLOR[1] = 242
					if database.COLOR[1] > 242: database.COLOR[1] = 30
				if self.lopt == 4:
					if self.pressed[database.LEFT]: database.COLOR[2] -= 2; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: database.COLOR[2] += 2; self.ch_sfx.play(database.SOUND['MENU_HOR'])

					if database.COLOR[2] < 30: database.COLOR[2] = 242
					if database.COLOR[2] > 242: database.COLOR[2] = 30

			if self.mnu == 2:
				if self.lopt == 0:
					if self.pressed[database.LEFT]: database.SFX -= 0.1; self.ch_sfx.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: database.SFX += 0.1;  self.ch_sfx.play(database.SOUND['MENU_HOR'])

					self.ch_sfx.set_volume(database.SFX)
					self.ch_ton.set_volume(database.SFX)
					self.ch_stp.set_volume(database.SFX)

					if database.SFX < 0.0: database.SFX = 0.0
					if database.SFX > 1.0: database.SFX = 1.0
				if self.lopt == 1:
					if self.pressed[database.LEFT]: database.MSC -= 0.1; self.ch_msc.play(database.SOUND['MENU_HOR'])
					if self.pressed[database.RIGHT]: database.MSC += 0.1; self.ch_msc.play(database.SOUND['MENU_HOR'])

					self.ch_msc.set_volume(database.MSC)
					self.ch_rad.set_volume(database.MSC)
					self.ch_rng.set_volume(database.MSC)

					if database.MSC < 0.0: database.MSC = 0.0
					if database.MSC > 1.0: database.MSC = 1.0

		#PLAYER MOVEMENT
		if self.player['PAUSE'] == 0:
			self.pressed = pygame.key.get_pressed()
			if self.driving == 0:
				if self.player['JUMP'] == 0:
					if self.pressed[database.RUN]:
						self.player['SPD'] = 6
					else: self.player['SPD'] = 3

					if self.pressed[database.UP]:
						if self.pressed[database.LEFT]: self.player['DIRECTION'] = 6
						elif self.pressed[database.RIGHT]: self.player['DIRECTION'] = 8
						else: self.player['DIRECTION'] = 7

					elif self.pressed[database.DOWN]:
						if self.pressed[database.LEFT]: self.player['DIRECTION'] = 4
						elif self.pressed[database.RIGHT]: self.player['DIRECTION'] = 2
						else: self.player['DIRECTION'] = 3

					elif self.pressed[database.LEFT]:
						if self.pressed[database.UP]: self.player['DIRECTION'] = 6
						elif self.pressed[database.DOWN]: self.player['DIRECTION'] = 4
						else: self.player['DIRECTION'] = 5

					elif self.pressed[database.RIGHT]:
						if self.pressed[database.UP]: self.player['DIRECTION'] = 8
						if self.pressed[database.DOWN]: self.player['DIRECTION'] = 2
						else: self.player['DIRECTION'] = 1

					else: self.player['SPD'] = 0

			elif self.driving > 0:
				if database.GAS > 0:
					if self.pressed[database.UP]:
						self.driving = 0
						self.displayzw = 600
						self.displayzh = 400
						self.display = pygame.Surface((600, 400))
						self.cam.width = self.displayzw
						self.cam.height = self.displayzh
						self.player['DIRECTION'] = 3

					if self.pressed[database.DOWN]:
						if self.player['SPD'] > 0.0: self.player['SPD'] -= self.vehicles[self.driving - 1]['ACCELERATION']

					elif self.pressed[database.RUN]:
						if self.player['SPD'] < self.vehicles[self.driving - 1]['SPEED'] and database.GAS > 0.0:
							self.player['SPD'] += self.vehicles[self.driving - 1]['ACCELERATION']
						database.GAS -= self.vehicles[self.driving - 1]['GAS']
					else: self.player['SPD'] -= self.vehicles[self.driving - 1]['ACCELERATION']

		if self.player['FOLLOW'] != None:
			if self.player['FOLLOW'] != (None,None):
				self.player['SPD'] = 3
				if self.player['RECT'].y - self.cam.y > self.player['FOLLOW'].y - self.cam.y:
					if self.player['RECT'].x - self.cam.x < self.player['FOLLOW'].x - self.cam.x: self.player['DIRECTION'] = 8
					elif self.player['RECT'].x - self.cam.x > self.player['FOLLOW'].x - self.cam.x: self.player['DIRECTION'] = 6
					else: self.player['DIRECTION'] = 7

				elif self.player['RECT'].y - self.cam.y < self.player['FOLLOW'].y - self.cam.y: 
					if self.player['RECT'].x - self.cam.x < self.player['FOLLOW'].x - self.cam.x: self.player['DIRECTION'] = 2
					elif self.player['RECT'].x - self.cam.x > self.player['FOLLOW'].x - self.cam.x: self.player['DIRECTION'] = 4
					else: self.player['DIRECTION'] = 3

				elif self.player['RECT'].x - self.cam.x < self.player['FOLLOW'].x - self.cam.x:
					if self.player['RECT'].y - self.cam.y > self.player['FOLLOW'].y - self.cam.y: self.player['DIRECTION'] = 8
					elif self.player['RECT'].y - self.cam.y < self.player['FOLLOW'].y - self.cam.y: self.player['DIRECTION'] = 2
					else: self.player['DIRECTION'] = 1

				elif self.player['RECT'].x - self.cam.x > self.player['FOLLOW'].x - self.cam.x:
					if self.player['RECT'].y - self.cam.y > self.player['FOLLOW'].y - self.cam.y: self.player['DIRECTION'] = 6
					elif self.player['RECT'].y - self.cam.y < self.player['FOLLOW'].y - self.cam.y: self.player['DIRECTION'] = 4
					else: self.player['DIRECTION'] = 5

				if self.colide(self.player['RECT'],self.player['FOLLOW']):
					self.player['DIRECTION'] = self.player['FOLLEND']
					self.player['FOLLOW'] = None
					self.player['FOLLEND'] = 0
					self.player['SPD'] = 0
			else:
				self.player['DIRECTION'] = self.player['FOLLEND']
				self.player['FOLLOW'] = None
				self.player['FOLLEND'] = 0
				self.player['SPD'] = 0

		if self.colide(self.player, self.tilrect) == False:
			wh = '0' + str(database.PARTY[database.FORMATION][0]) + '1'
			cl = database.CHARACTERS[database.PARTY[database.FORMATION][0]]['COSTUME']
			gl = 1
			if self.player['JUMP'] > 0:
				if self.player['DIRECTION'] == 3: self.player['SPRITE'] = 'JUMPD_' + cl; self.player['RECT'].y += self.player['SPD']
				elif self.player['DIRECTION'] == 7: self.player['SPRITE'] = 'JUMPU_' + cl; self.player['RECT'].y -= self.player['SPD']
			elif self.player['SPD'] > 3:
				if self.player['DIRECTION'] == 1: self.player['HEAD'] = 'BLANKR_' + wh; self.player['SPRITE'] = 'RUNR_' + cl; self.player['RECT'].x += self.player['SPD']
				elif self.player['DIRECTION'] == 2: self.player['HEAD'] = 'BLANKRD_' + wh; self.player['SPRITE'] = 'RUNRD_' + cl; self.player['RECT'].x += self.player['SPD']; self.player['RECT'].y += self.player['SPD']
				elif self.player['DIRECTION'] == 3: self.player['HEAD'] = 'BLANKD_' + wh; self.player['SPRITE'] = 'RUND_' + cl; self.player['RECT'].y += self.player['SPD']
				elif self.player['DIRECTION'] == 4: self.player['HEAD'] = 'BLANKLD_' + wh; self.player['SPRITE'] = 'RUNLD_' + cl; self.player['RECT'].x -= self.player['SPD']; self.player['RECT'].y += self.player['SPD']
				elif self.player['DIRECTION'] == 5: self.player['HEAD'] = 'BLANKL_' + wh; self.player['SPRITE'] = 'RUNL_' + cl; self.player['RECT'].x -= self.player['SPD']
				elif self.player['DIRECTION'] == 6: self.player['HEAD'] = 'BLANKLU_' + wh; self.player['SPRITE'] = 'RUNLU_' + cl; self.player['RECT'].x -= self.player['SPD']; self.player['RECT'].y -= self.player['SPD']
				elif self.player['DIRECTION'] == 7: self.player['HEAD'] = 'BLANKU_' + wh; self.player['SPRITE'] = 'RUNU_' + cl; self.player['RECT'].y -= self.player['SPD']
				elif self.player['DIRECTION'] == 8: self.player['HEAD'] = 'BLANKRU_' + wh; self.player['SPRITE'] = 'RUNRU_' + cl; self.player['RECT'].x += self.player['SPD']; self.player['RECT'].y -= self.player['SPD']
			elif self.player['SPD'] > 0:
				if self.player['DIRECTION'] == 1: self.player['HEAD'] = 'BLANKR_' + wh; self.player['SPRITE'] = 'WALKR_' + cl; self.player['RECT'].x += self.player['SPD']
				elif self.player['DIRECTION'] == 2: self.player['HEAD'] = 'BLANKRD_' + wh; self.player['SPRITE'] = 'WALKRD_' + cl; self.player['RECT'].x += self.player['SPD']; self.player['RECT'].y += self.player['SPD']
				elif self.player['DIRECTION'] == 3: self.player['HEAD'] = 'BLANKD_' + wh; self.player['SPRITE'] = 'WALKD_' + cl; self.player['RECT'].y += self.player['SPD']
				elif self.player['DIRECTION'] == 4: self.player['HEAD'] = 'BLANKLD_' + wh; self.player['SPRITE'] = 'WALKLD_' + cl; self.player['RECT'].x -= self.player['SPD']; self.player['RECT'].y += self.player['SPD']
				elif self.player['DIRECTION'] == 5: self.player['HEAD'] = 'BLANKL_' + wh; self.player['SPRITE'] = 'WALKL_' + cl; self.player['RECT'].x -= self.player['SPD']
				elif self.player['DIRECTION'] == 6: self.player['HEAD'] = 'BLANKLU_' + wh; self.player['SPRITE'] = 'WALKLU_' + cl; self.player['RECT'].x -= self.player['SPD']; self.player['RECT'].y -= self.player['SPD']
				elif self.player['DIRECTION'] == 7: self.player['HEAD'] = 'BLANKU_' + wh; self.player['SPRITE'] = 'WALKU_' + cl; self.player['RECT'].y -= self.player['SPD']
				elif self.player['DIRECTION'] == 8: self.player['HEAD'] = 'BLANKRU_' + wh; self.player['SPRITE'] = 'WALKRU_' + cl; self.player['RECT'].x += self.player['SPD']; self.player['RECT'].y -= self.player['SPD']
			elif self.player['SPD'] == 0:
				if self.player['DIRECTION'] == 1: self.player['SPRITE'] = 'STANDR_' + cl
				elif self.player['DIRECTION'] == 2: self.player['SPRITE'] = 'STANDRD_' + cl
				elif self.player['DIRECTION'] == 3: self.player['SPRITE'] = 'STANDD_' + cl
				elif self.player['DIRECTION'] == 4: self.player['SPRITE'] = 'STANDLD_' + cl
				elif self.player['DIRECTION'] == 5: self.player['SPRITE'] = 'STANDL_' + cl
				elif self.player['DIRECTION'] == 6: self.player['SPRITE'] = 'STANDLU_' + cl
				elif self.player['DIRECTION'] == 7: self.player['SPRITE'] = 'STANDU_' + cl
				elif self.player['DIRECTION'] == 8: self.player['SPRITE'] = 'STANDRU_' + cl
			else: self.player['SPD'] = 0

		if database.GAS < 1.0: self.player['DIRECTION'] = 0
		if self.player['SPD'] < 0: self.player['SPD'] = 0

		if self.dlgfa == 0:
			self.pressed = pygame.key.get_pressed()
			if self.pressed[database.ACT]: self.dlgspd = 1
			else: self.dlgspd = database.SPEED

	def dialog(self, tx, wh=0):
		self.dlg = []
		self.dlgy = 0
		self.lopt = 0
		self.speakin = wh
		self.player['PAUSE'] = 1
		self.player['SPD'] = 0
		txt = tx
		tid = 0
		did = 0
		spd = 10

		while tid < len(txt):
			#DELET TEXT
			'''c = 0
			lst = self.dlg[::-1]
			for i in range(len(lst)):
				if isinstance(i,str):
					if c < 6: c += 1
					else: del lst[i]'''
			#TEXT
			if isinstance(txt[tid], str):
				while self.dlgfa > 0:
					if self.winbar < 50 and self.battle == False: self.winbar += 5
					self.dlgfa -= 50
					self.run()
				else:
					self.dlg.append('')
					for i in txt[tid]:
						while True:
							if spd > 0: spd -= 10/self.dlgspd
							else:
								self.ch_sfx.play(database.SOUND['VOICE_MID'])
								self.dlg[did] += i
								spd = 10
								break
							self.run()
					did += 1

			#DIALOG PROTOCOLS
			else:
				if txt[tid] == 0:
					self.dlg.append(0)
					did += 1

				elif txt[tid] == 1:
					self.dlg.append(1)
					self.wait()
					self.ch_ton.play(database.SOUND['MENU_GO'])
					did += 1

				elif txt[tid] == 2:
					database.SCENE = -1
					self.ch_ton.play(database.SOUND['BAUM'])
					#self.display.set_palette(database.PALETTES[0])
					self.player['PAUSE'] = 3
					for i in range(100): self.run()
					#self.display.set_palette()
					database.SCENE = 0
					self.player['PAUSE'] = 1

				elif txt[tid][0] == 0 and self.notx == 0:
					database.MONEY += txt[tid][1]
					self.ch_sfx.play(database.SOUND['CASH_GET'])
					self.notification('Adquiriu $' + str(txt[tid][1]),(255, 255, 255))

				elif txt[tid][0] == 1 and self.notx == 0:
					if txt[tid][3] > 0 and database.CHESTS[str(database.MAP) + self.room][txt[tid][3] - 1] == False:
						self.inv.add(0,txt[tid][1])
						database.MONEY -= txt[tid][2]
						self.ch_sfx.play(database.SOUND['ITEM_GET'])
						self.notification('Adquiriu ' + database.ITEMS[txt[tid][1]][0],(255, 255, 255))
						database.CHESTS[str(database.MAP) + self.room][txt[tid][3] - 1] = True
					else:
						for j in database.DIALOGS['EMPTY CHEST'][::-1]:
							txt.insert(tid + 1, j)

				elif txt[tid][0] == 2 and self.notx == 0:
					database.MORALITY += txt[tid][1]
					self.ch_sfx.play(database.SOUND['NOTIFICATION'])
					self.notification(txt[tid][1],(0, 0, 0))

				elif txt[tid][0] == 3 and self.notx == 0:
					self.ch_sfx.play(database.SOUND['NOTIFICATION'])
					self.notification('Marcador adicionado',(140, 255, 253))

				elif txt[tid][0] == 4:
					if txt[tid][1] != 'stop':
						self.ch_ton.play(database.SOUND['CALLING'],-1)
						self.ch_rng.play(database.SOUND['RINGTONE_' + str(self.phn.pbg)])
						if self.radonoff == True: pygame.mixer.music.pause()
						tw = 0
						cl = False
						while tw < 2000 and cl == False:
							pygame.time.wait(10)
							for event in pygame.event.get():
								if event.type == pygame.KEYUP:
									cl = True
							tw += 1
						self.ch_ton.stop()
						self.ch_rng.stop()
						self.ch_sfx.play(database.SOUND['EQUIP'])
						if cl == True:
							self.phone = 3
							self.mnu = 1
							txt.insert(tid + 1, [2,'stop'])
							txt.insert(tid + 1, 0)
							for i in self.phn.call(str(database.CONTACTS[txt[tid][1]][1]),0,False,False)[-1:0:-1]:
								txt.insert(tid + 1, i)
					else:
						self.phone = 0
						self.mnu = 0

				elif txt[tid][0] == 5 and self.notx == 0:
					self.ch_sfx.play(database.SOUND['NOTIFICATION'])
					mail = database.EMAILS[txt[tid][1]].copy()
					mail.append(0)
					database.INBOX.append(mail)
					database.inbx_save(len(database.INBOX)-1,0)
					self.notification('Novo email',(255, 221, 0))

				elif txt[tid][0] == 6 and self.notx == 0:
					self.ch_sfx.play(database.SOUND['NOTIFICATION'])
					database.TASKS.append([txt[tid][1], 0])
					database.task_save(txt[tid][1],0)
					self.notification('Nova tarefa disponível',(255, 123, 0))

				elif txt[tid][0] == 7 and self.notx == 0:
					self.ch_sfx.play(database.SOUND['NOTIFICATION'])
					database.CONTACTS.append(database.NUMBERS[txt[tid][1]].copy())
					database.call_save(len(database.CONTACTS)-1)
					self.notification('Contato adicionado',(165, 255, 0))

				elif txt[tid][0] == 8 and self.notx == 0:
					self.ch_sfx.play(database.SOUND['ACHIEVEMENT'])
					database.ACHIEVEMENTS[txt[tid][1]][2] = True
					self.notification(database.ACHIEVEMENTS[txt[tid][1]][0],(255, 191, 0))

				elif txt[tid][0] == 9 and self.notx == 0:
					self.ch_sfx.play(database.SOUND['NOTIFICATION'])
					self.notification('Subiu de posição!',(56, 255, 0))

				elif txt[tid][0] == 10:
					self.speakin = 0
					self.dlg.append(0)
					for j in txt[tid][-1:0:-1]:
						self.dlg.append(j[0])
					self.dlg.append(0)
					self.diopt(len(txt[tid][1:]))
					self.speakin = wh
					for j in txt[tid][self.lopt][-1:0:-1]:
						txt.insert(tid + 1, j)
					self.lopt = 0
					did = len(self.dlg)

				elif txt[tid][0] == 11:
					tid += txt[tid][1]

				elif txt[tid][0] == 12:
					tid -= txt[tid][1]

				elif txt[tid][0] == 13:
					pygame.mixer.music.stop()
					for i in txt[tid][1:]:
						fo = database.FREAKS[i].copy()
						fo['FILE'] = i
						fo['SPRITE'] = pygame.image.load('Sprites/frk_' + (fo['FILE']) + '_stand.png')
						siz = fo['SPRITE'].get_rect()
						fo['MASK'] = pygame.Rect(230,280 - siz.height,44,85)
						fo['DIRECTION'] = False
						fo['FIGHTING'] = False
						fo['HEALTH'] = 0
						fo['FADE'] = 10
						if fo['TYPE'] == 'mercenary': self.mrc.append(fo)
						else: self.foe.append(fo)
					txt = []
					tid = 0
					self.mnu = 0
					self.turn = -5
					self.fight()

				elif txt[tid][0] == 14:
					pygame.mixer.music.stop()
					for k in database.ARMY[txt[tid][1]].copy():
						i = database.FREAKS[k].copy()
						i['FILE'] = k
						i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE']) + '_stand.png')
						siz = i['SPRITE'].get_rect()
						i['MASK'] = pygame.Rect(230,280 - siz.height,44,85)
						i['DIRECTION'] = False
						i['FIGHTING'] = False
						i['HEALTH'] = 0
						i['FADE'] = 10
						if i['TYPE'] == 'mercenary': self.mrc.append(i)
						else: self.foe.append(i)
					txt = []
					tid = 0
					self.mnu = 0
					self.turn = -4
					self.fight()

				elif txt[tid][0] == 15:
					pygame.mixer.music.load('Music/' + txt[tid][1] + '.mp3')
					pygame.mixer.music.play(-1)

				elif txt[tid][0] == 16:
					self.ch_sfx.play('SFX/' + database.SOUND[txt[tid][1]] + '.mp3')

				elif txt[tid][0] == 17:
					self.waitime.append([txt[tid][1],txt[tid][2],txt[tid][3]])

				elif txt[tid][0] == 18:
					database.PARTY[database.FORMATION] = txt[tid][1:]

				elif txt[tid][0] == 19:
					for i in self.foe:
						prb = round(random.randint(0,10))
						if prb > 4:
							if txt[tid][1] == 0: i['STRENGHT'] -= txt[tid][2]
							if txt[tid][1] == 1: i['AGILITY'] -= txt[tid][2]
							if txt[tid][1] == 2: i['RESISTANCE'] -= txt[tid][2]
							self.attackimation(0)

				elif txt[tid][0] == 20:
					for i in self.fig:
						prb = round(random.randint(0,10))
						if prb > 4:
							if txt[tid][1] == 0: i['STRENGHT'] += txt[tid][2]
							if txt[tid][1] == 1: i['AGILITY'] += txt[tid][2]
							if txt[tid][1] == 2: i['RESISTANCE'] += txt[tid][2]
							self.attackimation(0)

				elif txt[tid][0] == 21:
					database.DLGSAV[str(database.MAP) + self.room][txt[tid][1]] = txt[tid][2]

				elif txt[tid][0] == 22:
					self.nmenu = menu.Naming()
					self.nmenu.ninput = txt[tid][1]
					self.nmenu.show = True
					while self.nmenu.show == True:
						self.nmenu.events()
						self.nmenu.run()
						self.run()

				elif txt[tid][0] == 23:
					for j in database.DIALOGS[txt[tid][1]][txt[tid][2]].copy()[::-1]:
						txt.insert(tid + 1, j)
					did = len(self.dlg)

				elif txt[tid][0] == 24:
					if txt[tid][1] == None:
						if txt[tid][2] != (None,None):
							self.player['FOLLOW'] = pygame.Rect(txt[tid][2][0],txt[tid][2][1],10,10)
						else: self.player['FOLLOW'] = (None,None)
						self.player['FOLLEND'] = txt[tid][3]
					else:
						for i in self.npcs:
							if i['N'] == txt[tid][1]:
								if txt[tid][2] != (None,None):
									i['FOLLOW'] = pygame.Rect(txt[tid][2][0],txt[tid][2][1],10,10)
								else: i['FOLLOW'] = (None,None)
								i['FOLLEND'] = txt[tid][3]

				elif txt[tid][0] == 25:
					if txt[tid][1] == None:
						self.player['HEAD'] = txt[tid][2] + '_0' + str(database.PARTY[database.FORMATION][0]) + '1'
					else:
						for i in self.npcs:
							if i['N'] == txt[tid][1]:
								'''i['FOLLOW'] = txt[tid][2]
								i['FOLLEND'] = txt[tid][3]'''

				elif txt[tid][0] == 26:
					if isinstance(txt[tid][1],int):
						for i in self.npcs:
							if i['N'] == txt[tid][1]:
								self.speakin = i['RECT']
					else: self.speakin = pygame.Rect(txt[tid][1][0],txt[tid][1][1],1,1)

				elif txt[tid][0] == 27:
					ds = self.dlg.copy()
					self.dlg = []
					for i in range(txt[tid][1]): self.run()
					self.dlg = ds
			tid += 1

		self.dlg = []
		self.speakin = 0
		self.player['PAUSE'] = 0

		while self.dlgfa < 500:
			self.dlgfa += 50
			if self.winbar > 0 and self.battle == False: self.winbar -= 5
			self.run()

	def diopt(self, ln):
		self.lopt = 1
		trigger = True
		while trigger:
			self.run()
			for event in pygame.event.get():
				self.pressed = pygame.key.get_pressed()
				if self.pressed[database.UP]:
					if self.lopt < ln: self.ch_sfx.play(database.SOUND['MENU_HOR']); self.lopt += 1
				if self.pressed[database.DOWN]:
					if self.lopt > 1: self.ch_sfx.play(database.SOUND['MENU_VER']); self.lopt -= 1
				if self.pressed[database.ACT]:
					self.ch_ton.play(database.SOUND['MENU_GO'])
					i = 1
					crg = -1
					while i <= ln + 1:
						if i != self.lopt: del self.dlg[crg - i]; crg += 1; ln -= 1; print(self.dlg)
						i += 1
					trigger = False
					break
				if event.type == pygame.QUIT:
					waiting = False
					pygame.quit()
					sys.exit()

	def wait(self):
		waiting = True
		while waiting == True:
			self.events()
			self.draw()
			pygame.time.Clock().tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					waiting = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					waiting = False

	def confirmation(self):
		yesno = 0
		opt = 1
		brd = pygame.Surface((200,100))
		brd.fill((database.COLOR[0],database.COLOR[1],database.COLOR[2]))
		for x in range(20):
			for y in range(10):
				brd.blit(pygame.image.load('Sprites/border.png'), (x * 10, y * 10))
		wdw = pygame.Surface((190,90))

		while yesno == 0:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				self.pressed = pygame.key.get_pressed()
				if self.pressed[database.LEFT]: self.ch_sfx.play(database.SOUND['MENU_HOR']); opt = 1
				if self.pressed[database.RIGHT]: self.ch_sfx.play(database.SOUND['MENU_VER']); opt = 2
				if self.pressed[database.ACT]:
					yesno = opt
					if yesno == 1: self.ch_sfx.play(database.SOUND['MENU_GO'])
					if yesno == 2: self.ch_sfx.play(database.SOUND['MENU_BACK'])
					opt = 0

			wdw.fill((0,0,0))
			wdw.blit(self.monotype.render(database.MENU[85], True, (255, 255, 255)), (45, 10))
			if opt == 1: wdw.blit(self.monotype.render(database.MENU[83], True, (database.COLOR[0],database.COLOR[1],database.COLOR[2])), (40, 50))
			else: wdw.blit(self.monotype.render(database.MENU[83], True, (255, 255, 255)), (40, 50))
			if opt == 2: wdw.blit(self.monotype.render(database.MENU[84], True, (database.COLOR[0],database.COLOR[1],database.COLOR[2])), (110, 50))
			else: wdw.blit(self.monotype.render(database.MENU[84], True, (255, 255, 255)), (110, 50))

			self.display.blit(brd,(195,145))
			self.display.blit(wdw,(200,150))
			self.screen.blit(pygame.transform.scale(self.display, (self.windoww, self.windowh)), (self.displayx, self.displayy))
			pygame.display.update()
			pygame.display.flip()
			pygame.time.Clock().tick(self.FPS)

		return yesno

	def transiction(self, fade, limit):
		if fade == False:
			while self.winbar > limit:
				self.winbar -= 5
				self.run()
		else:
			while self.winbar < limit:
				self.winbar += 5
				self.run()

	def fight(self):
		#BATTLE START
		if self.turn < 0:
			self.inventory = 0
			self.phone = 0
			self.shp = False
			self.player['PAUSE'] = 2
			if self.radonoff == True: pygame.mixer.music.pause()
			if self.turn == -1: self.ch_ton.play(database.SOUND['BATTLE_FOE'])
			if self.turn == -2: self.ch_ton.play(database.SOUND['BATTLE_ENEMY'])
			if self.turn == -3: self.ch_ton.play(database.SOUND['BATTLE_AMBUSH'])
			else: self.ch_ton.play(database.SOUND['BATTLE_BOSS'])
			if self.driving > 0: self.obstacles = True

			acc = 0
			while True:
				self.displayzw -= acc * 6
				self.displayzh -= acc * 4
				self.cam.x += acc * 3
				self.cam.y += acc * 2
				self.cam.width = self.displayzw
				self.cam.height = self.displayzh
				if self.displayzw > 6: self.display = pygame.Surface((self.displayzw, self.displayzh))
				else:
					self.displayzw = 6; self.displayzh = 4;
					self.cam.width = 6; self.cam.height = 4;
					self.display = pygame.Surface((self.displayzw, self.displayzh))
					break
				self.draw()
				acc += 1

			self.fig = []
			tr = 0
			for i in database.PARTY[database.FORMATION]:
				dt = database.CHARACTERS[i]
				if dt['HP'] > 0:
					dt['N'] = tr
					self.fig.append(dt)
				tr += 1

			self.bbg = pygame.image.load('Backgrounds/mountains.png')
			self.player['SPD'] = 0
			self.pstr = []
			self.patt = []
			self.pagi = []
			self.pres = []
			self.tatt = []
			self.tagi = []
			self.tstr = []
			self.tres = []
			self.opt = 0
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
				self.foe[enx]['DIRECTION'] = 5
				self.foe[enx]['VITALITY'] = self.foe[enx]['HP']
				enx += 1
			if self.turn == -3: self.foe[0]['SPRITE'] = pygame.image.load('Sprites/frk_' + (self.foe[0]['FILE']) + '_backwards.png'); self.foe[0]['HEALTH'] = 1

			self.battle = True

			acc = 0
			while True:
				self.displayzw += acc * 6
				self.displayzh += acc * 4
				self.cam.x -= acc * 3
				self.cam.y -= acc * 2
				self.cam.width = self.displayzw
				self.cam.height = self.displayzh
				if self.displayzw < 600: self.display = pygame.Surface((self.displayzw, self.displayzh))
				else:
					self.displayzw = 600; self.displayzh = 400;
					self.cam.x = 0; self.cam.y = 0;
					self.cam.width = 600; self.cam.height = 400;
					self.display = pygame.Surface((self.displayzw, self.displayzh))
					break
				self.draw()
				acc += 1

			self.ch_msc.play(database.SONGS[self.foe[0]['SONG']],-1)
			self.player['GIF'] = 0.0
			self.tilemation = 0.0
			self.transiction(True, 100)
			chk = False
			for i in database.BESTIARY:
				if self.foe[0]['NAME'] == database.FREAKS[i['N']]['NAME']: chk = True
				
			if self.turn == -1:
				if chk == False: self.dialog([self.foe[0]['NAME'] + database.BATTLE[0],1])
				self.turn = 0
			if self.turn == -2:
				if chk == False: self.dialog([self.foe[0]['NAME'] + database.BATTLE[1],1])
				self.turn = len(self.fig)
			if self.turn == -3:
				if chk == False: self.dialog([self.foe[0]['NAME'] + database.BATTLE[2],1])
				self.turn = 0
			if self.turn == -4:
				self.dialog([database.BATTLE[44],1])
				self.turn = 0
			if self.turn == -5:
				if chk == False: self.dialog([self.foe[0]['NAME'] + database.BATTLE[0],1])
				self.turn = 0
			self.mnu = 1
			print(self.foe)
			print(self.mrc)

		#PLAYERS TURN
		elif self.turn < len(database.PARTY[database.FORMATION]):
			again = False
			self.mnu = 3
			if self.equip[self.turn] < 4:
				pp = int(database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1])
				pp -= 1
				database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1] = str(pp)
				gottem = False
				for i in self.foe:
					if self.colide(self.aim, i['MASK']) and i['FIGHTING'] == True:
						gottem = True
						dmg = int(random.randint(database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0]][5]['DAMAGE'] - 2,\
						database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0]][5]['DAMAGE'] + 2)) - i['RESISTANCE']
						if database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['HEALTH'] == 11: dmg = int(dmg/2)
						if i['HEALTH'] != 1: i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE']) + '_damage.png')

						if dmg > 0:
							for p in range(dmg * 2):
								self.particles.append({'X': self.aim.x, 'Y': self.aim.y, 'RADIUS': round(random.randint(3,5)), 'DIRECTION': round(random.randint(0,360)), 'SPEED': round(random.randint(2,6))})
							if dmg == database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0]][5]['DAMAGE'] + 2 - i['RESISTANCE']:
								self.ch_sfx.play(database.SOUND['CRITICAL'])
								self.hitisplay(10, i['MASK'], database.BATTLE[3], (200, 0, 0))
							else:
								self.ch_sfx.play(database.SOUND['HIT'])
								self.hitisplay(10, i['MASK'], str(dmg), (200, 0, 0))
							if i['HEALTH'] != 1: i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE'])+ '_stand.png')
							i['HP'] -= dmg
							self.hits += 1
							self.tdmg += dmg
						else: self.hitisplay(0, None, database.BATTLE[5], (255, 255, 255))

						#CHECK WIN
						if i['HP'] <= 0:
							if dmg >= i['VITALITY']: again = True
							self.ch_ton.play(database.SOUND['SCREAM_' + i['FILE'].upper()])
							while i['FADE'] > 0:
								i['FADE'] -= 1
								self.run()
							if i['ITEM'] != None:
								prb = round(random.randint(0,100))
								if prb > i['ITEM'][1]:
									self.inv.add(0,i['ITEM'][0])
									self.ch_sfx.play(database.SOUND['ITEM_GET'])
									self.notification('Adquiriu ' + database.ITEMS[i['ITEM'][0]][0],(255, 255, 255))
							i['FIGHTING'] = False

						self.mnu = 0
				if gottem == False:
					self.ch_sfx.play(database.SOUND['MISS'])
					self.hitisplay(5, self.aim, database.BATTLE[4], (200, 200, 200))

			elif self.equip[self.turn] == 5:
				if self.foe[0]['TYPE'] not in ('humanoid','psychic'):
					self.dialog(database.DIALOGS['IRRATIONAL'])
				else: self.dialog(database.DIALOGS[self.foe[0]['NAME'].upper()])
				self.mnu = 1

			elif self.equip[self.turn] == 7:
				self.dialog([self.fig[self.turn]['NAME'] + database.BATTLE[15]])
				run = round(random.randint(0,100))
				if run > 49:
					self.ch_msc.fadeout(500)
					self.dialog([database.BATTLE[17]])
					self.transiction(True, 210)
					for i in self.foe:
						i['FIGHTING'] = False
					self.turn = 0
					self.mnu = 0
					self.hits = 0
					self.tdmg = 0
					self.hpl = 0
					self.tbt = 0
					self.battle = False
					self.opt = 1
					self.player['RECT'].x += 150
					self.transiction(False, 0)
				else:
					self.dialog([database.BATTLE[16]])

			if again == True and self.battle == True:
				self.ch_ton.play(database.SOUND['ONE_MORE'])
				self.hitisplay(0, self.aim, database.BATTLE[5], (10, 50, 255))
				self.turn -= 1
			if self.turn < len(self.fig):
				self.aim.x = 100 + self.fig[self.turn]['ATTACK'][self.fig[self.turn]['LEVEL']]

		else:
			self.inventory = 0
			self.phone = 0
			self.tbt += round(self.btime/10)
			self.btime = 100
			self.mnu = 3
			count = 0

			#MERCENARIES TURN
			for i in self.mrc:
				print('im here')

			#ENEMIES TURN
			for i in self.foe:
				if i['HP'] > 0 and i['FIGHTING'] == True and i['HEALTH'] != 1 and len(self.fig) > 0:
					count += 1
					if count == 6: break

					if i['HEALTH'] > 9:
						i['HP'] -= 5
						self.hitisplay(5, i['MASK'], str(5), (200, 0, 0))

					prb = []
					for h in i['HABILITIES']:
						prb.append(h[4])
					opt = int(random.randint(0,100))
					rng = 100
					for p in range(len(prb)):
						rng -= prb[p]
						if opt >= rng:
							act = i['HABILITIES'][p].copy()
							break
					dd = i['NAME'] + database.BATTLE[18] + act[0]
					i['SPRITE'] = pygame.image.load('Sprites/frk_' + i['FILE'] + '_attack.png')
					if i['HEALTH'] == 7: pl = int(random.randint(-20,len(self.fig) - 1 + len(self.mrc)))
					else: pl = int(random.randint(-1,len(self.fig) - 1 + len(self.mrc)))

					if act[3] == 2 and self.tatt == 2: act = i['HABILITIES'][0]
					if act[3] == 3 and self.tagi == 2: act = i['HABILITIES'][0]

					if pl >= 0:
						if act[3] == 1:
							if act[2] < 0:
								if pl < len(self.fig):
									for a in database.INVENTORY[pl][:-1]:
										if a[0][0] != '_':
											act[2] += int(database.ITEMS[a[0][0]][5])
											a[0][1] = int(a[0][1])
											a[0][1] -=1
											if a[0][1] == 0:
												self.dialog([a[0][0] + database.BATTLE[36],1])
												a[0] = ['_','0000','_','_']
											a[0][1] = str(a[0][1])

									self.turn = self.fig[pl]['N']
									self.ch_ton.play(database.SOUND['SCREAM_' + i['FILE'].upper()])
									self.ch_sfx.play(database.SOUND['DAMAGE_1'])
									if self.attackimation(act[5]) == True:
										act[2] -= int(act[2]/5)
										self.hitisplay(5, i['MASK'], 'dodge', (0, 200, 0))
									if -act[2] > 0:
										self.fig[pl]['HP'] += act[2] + self.pres[pl]
										self.hitisplay(-act[2] * 2, None, '', (0,0,0))
									else:
										self.fig[pl]['HP'] += -1
										self.hitisplay(2, None, '', (0,0,0))
									self.hpl += act[2]

								else:
									self.ch_sfx.play(database.SOUND['HIT'])
									self.hitisplay(10, self.mrc[pl], str(act[2]), (0, 200, 0))
									self.mrc[pl]['SPRITE'] = pygame.image.load('Sprites/frk_' + (self.mrc[pl]['FILE']) + '_stand.png')
									self.mrc[pl]['HP'] += act[2]

							elif act[2] > 0:
								self.ch_ton.play(database.SOUND['HEAL'])
								i['HP'] += act[2]

						elif act[3] == 2:
							if act[2] < 0:
								if self.tatt[pl] < 2:
									self.ch_ton.play(database.SOUND['ATTRIBUTE_LOSS'])
									self.patt[pl] += act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[22],1])
									self.tatt[pl] += 1
							elif act[2] > 0:
								act[2] += act[2]
								self.ton_sfx.play(database.SOUND['ATTRIBUTE_GAIN'])
								self.dialog([dd, i['NAME'] + database.BATTLE[21] + str(act[2]) + database.BATTLE[22],1])

						elif act[3] == 3:
							if act[2] < 0:
								self.turn = self.fig[pl]['N']
								if self.tagi[self.turn] < 2:
									self.ch_ton.play(database.SOUND['ATTRIBUTE_LOSS'])
									self.pagi[self.turn]+=act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[23],1])
									self.tagi[self.turn]+=1
							elif act[2] > 0:
								i['AGILITY']+=act[2]
								self.ton_sfx.play(database.SOUND['ATTRIBUTE_GAIN'])
								self.dialog([dd, i['NAME'] + database.BATTLE[21] + str(act[2]) + database.BATTLE[23],1])

						elif act[3] == 4:
							if act[2] < 0:
								self.turn = self.fig[pl]['N']
								if self.tstr[self.turn]<2:
									self.ch_ton.play(database.SOUND['ATTRIBUTE_LOSS'])
									self.pstr[self.turn] += act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[24],1])
									self.tstr[self.turn] += 1
							elif act[2] > 0:
								i['STRENGHT'] += act[2]
								self.ton_sfx.play(database.SOUND['ATTRIBUTE_GAIN'])
								self.dialog([dd, i['NAME'] + database.BATTLE[21] + str(act[2]) + database.BATTLE[24],1])

						elif act[3] == 5:
							if act[2] < 0:
								self.turn = self.fig[pl]['N']
								if self.tagi[self.turn] < 2:
									self.ch_ton.play(database.SOUND['ATTRIBUTE_LOSS'])
									self.pres[self.turn] += act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[25],1])
									self.tres[self.turn] += 1
							elif act[2] > 0:
								i['RESISTANCE'] += act[2]
								self.ton_sfx.play(database.SOUND['ATTRIBUTE_GAIN'])
								self.dialog([dd, i['NAME'] + database.BATTLE[21] + str(act[2]) + database.BATTLE[25],1])

						elif act[3] == 6:	
							self.fig[pl]['HEALTH'] = act[2]
							if self.dlgfa > 0:
								if act[2] == 2: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[26],1])
								if act[2] == 3: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[27],1])
								if act[2] == 4: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[28],1])
								if act[2] == 5: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[29],1])
								if act[2] == 6: self.dialog([dd, self.fig[pl]['NAME'] +  database.BATTLE[30],1])
								if act[2] == 7: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[31],1])
								if act[2] == 8: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[32],1])
								if act[2] == 9: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[33],1])
								if act[2] == 10 or act[2] == 11 or act[2] == 12: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[34],1])
								if act[2] == 13: self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[35],1])
								self.fig[pl]['HEALTH'] = act[2]
								if self.fig[pl]['HEALTH'] == 5: self.pagi[pl] -= 20
								act[2] == 0

						elif act[3] == 7:
							prb = round(random.randint(0,100))
							if prb > 49:
								wh = round(random.randint(0,len(act[2]) - 1))
								nw = database.FREAKS[act[2][wh]].copy()
								nw['FILE'] = act[2][wh]
								nw['SPRITE'] = pygame.image.load('Sprites/frk_' + (nw['FILE']) + '_stand.png')
								nw['MASK'] = pygame.Rect(230,180,44,85)
								nw['FIGHTING'] = True
								nw['HEALTH'] = 0
								nw['DIRECTION'] = False
								nw['FADE'] = 10
								if database.MAP == nw['HABITAT']:
									nw['AGILITY'] += 2
									nw['HP'] += 5
								self.foe.append(nw)
								if self.dlgfa > 0:
									self.dialog([i['NAME'] + ' usou ' + act[0],1,nw['NAME'] + database.BATTLE[37],1])
							else:
								if self.dlgfa > 0:
									self.dialog([i['NAME'] + ' usou ' + act[0],1,database.BATTLE[38],1])

						elif act[3] == 9:
							if self.dlgfa > 0: self.dialog([i['NAME'] + ' arregou!',1])
							i['HP'] = 0

						elif act[3] == 10:
							self.ch_ton.play(database.SOUND['CHARGE'])
							self.attackimation(act[5])
							self.turn = self.fig[pl]['N']
							self.ch_ton.play(database.SOUND['SCREAM_' + i['FILE'].upper()])
							self.ch_sfx.play(database.SOUND['DAMAGE_1'])
							if self.attackimation(act[5]) == False:
								act[2] -= int(act[2]/5)
								self.fig[pl]['HP'] += act[2] + self.pres[pl]
								self.hitisplay(-act[2] * 2, None, '', (0,0,0))
								self.hpl += act[2]
							else:
								self.ch_sfx.play(database.SOUND['HIT'])
								for p in range(dmg * 3):
									self.particles.append({'X': self.aim.x, 'Y': self.aim.y, 'RADIUS': round(random.randint(3,5)), 'DIRECTION': round(random.randint(0,360)), 'SPEED': round(random.randint(2,6))})
								self.hitisplay(10, i['MASK'], str(act[2]), (200, 0, 0))
								if i['HEALTH'] != 1: i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE'])+ '_stand.png')
								i['HP'] -= act[2]
								self.hits += 1
								self.tdmg += act[2]

							#CHECK WIN
							if i['HP'] <= 0:
								self.ch_ton.play(database.SOUND['SCREAM_' + i['FILE'].upper()])
								while i['FADE'] > 0:
									i['FADE'] -= 1
									print(i['FADE'])
									self.run()
								if i['ITEM'] != None:
									prb = round(random.randint(0,100))
									if prb > i['ITEM'][1]:
										self.inv.add(0,i['ITEM'][0])
										self.ch_sfx.play(database.SOUND['ITEM_GET'])
										self.notification('Adquiriu ' + database.ITEMS[i['ITEM'][0]][0],(255, 255, 255))
								i['FIGHTING'] = False

						#CHECK DEATH
						if self.fig[pl]['HP'] <= 0:
							self.mnu = 1
							self.fig[pl]['HEALTH'] = 9
							self.ch_ton.play(database.SOUND['INCONSCIOUS'])
							self.dialog([self.fig[pl]['NAME'] + database.BATTLE[31]])
							del self.fig[pl]

						i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE']).lower() + '_stand.png')

					else: 
						self.ch_sfx.play(database.SOUND['MISS'])
						#self.hitisplay(5, self.aim, database.BATTLE[4], (200, 200, 200))

				elif i['HEALTH'] == 1 and self.dlgfa > 0:
					self.dialog([i['NAME'] + ' virou de costas',1])
					i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE']) + '_stand.png')
					i['HEALTH'] = 7

			if self.turn > -1:
				self.turn =  0
				self.mnu = 1
				for i in range(len(self.fig)):
					if self.pres[i] > self.fig[i]['RESISTANCE'][self.fig[i]['LEVEL']]:
						self.pres[i] = self.fig[i]['RESISTANCE'][self.fig[i]['LEVEL']]

		#OBSTACLES
		if self.obstacles == True:
			dmg = []
			self.mnu = 3
			for p in range(len(self.fig)):
				dmg.append(5)
				for a in database.INVENTORY[self.fig[p]['N']][:-1]:
					if a[0][0] != '_':
						dmg[p] += int(database.ITEMS[a[0][0]][5])
						a[0][1] = int(a[0][1])
						a[0][1] -= 1
						if a[0][1] == 0:
							self.dialog([a[0][0] + database.BATTLE[36],1])
							a[0] = ['_','0000','_','_']
						a[0][1] = str(a[0][1])

			if self.attackimation(1) == True:
				for p in range(len(self.fig)): dmg -= int(dmg/5)
				self.hitisplay(5, i['MASK'], 'dodge', (0, 200, 0))
			else:
				for p in range(len(self.fig)): self.fig[p]['HP'] += dmg[p] + self.pres[p]
				self.hitisplay(-dmg[p] * 2, None, '', (0,0,0))
				self.ch_sfx.play(database.SOUND['DAMAGE_1'])
				self.hpl += dmg[p]
			self.mnu = 1

		if self.turn == len(self.fig): self.fight()

		#VICTORY
		dth = 0
		for d in self.foe:
			if d['HP'] <= 0: dth += 1
		if dth == len(self.foe):
			self.ch_msc.fadeout(500)
			if len(self.foe) >= 10 or self.foe[0]['TYPE'] == 'boss': self.ch_ton.play(database.SOUND['BATTLE_BOSS_WON'])
			elif self.hpl == 0: self.ch_ton.play(database.SOUND['BATTLE_PERFECT'])
			else: self.ch_ton.play(database.SOUND['BATTLE_WON'])
			self.tbt += round(self.btime/10)
			self.xp = int(((self.hits*self.tdmg)-self.hpl+self.tbt)/len(self.fig))
			self.mnu = 600
			self.turn = -4
			self.transiction(True, 210)
			self.obstacles = False
			self.bbm = 0
			acc = 60
			while self.mnu > 0:
				self.mnu -= acc
				self.run()
			self.wait()
			for i in range(len(database.PARTY[database.FORMATION])):
				database.CHARACTERS[i]['XP'] += self.xp
				plux = int(100/(database.CHARACTERS[i]['NEXTLEVEL'][database.CHARACTERS[i]['LEVEL']]/database.CHARACTERS[i]['XP']))
			gb = self.greenblood
			for i in self.foe:
				gb += i['BLOOD']
			while self.greenblood < gb:
				if gb > 100: self.greenblood += 5
				else: self.greenblood += 1
				self.run()
			pl = False
			while self.barxp[0] < plux:
				self.run()
				for i in range(len(self.fig)):
					self.barxp[i] += 1
					if self.barxp[i] >= 100:
						if pl == False:
							self.ch_ton.play(database.SOUND['LEVEL_UP'],-1)
							acc = 35
							while self.mnu > -350:
								self.mnu -= acc
								self.run()
							pl = True
						self.barxp[i] = 0
						database.CHARACTERS[database.PARTY[database.FORMATION][i]]['LEVEL'] += 1
						database.CHARACTERS[database.PARTY[database.FORMATION][i]]['HP'] += database.CHARACTERS[database.PARTY[database.FORMATION][i]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][i]]['LEVEL'] - 1] - database.CHARACTERS[database.PARTY[database.FORMATION][i]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][i]]['LEVEL']]
						database.CHARACTERS[database.PARTY[database.FORMATION][i]]['XP'] = 0
						plux -= 100
				database.SCENE = 1
			self.wait()
			if pl == True: self.ch_ton.fadeout(2500)
			self.hits = 0
			self.tdmg = 0
			self.hpl = 0
			self.tbt = 0
			self.xp = 0
			self.foe = []
			self.btime = 100
			self.turn = -1
			self.battle = False
			if self.radonoff == True: pygame.mixer.music.unpause()
			self.player['PAUSE'] = 0
			self.transiction(False, 0)

		#GAME OVER
		dth = 0
		for d in self.fig:
			if d['HP'] <= 0: dth += 1
		if dth == len(self.fig):
			self.ch_msc.fadeout(500)
			self.ch_ton.play(database.SOUND['BATTLE_LOST'])
			self.transiction(True, 210)
			self.obstacles = False
			self.bbm = 0
			self.turn = -5
			self.mnu = 600
			acc = 60
			while self.mnu > 0:
				self.mnu -= acc
				acc -= 2
				self.run()
			self.turn = -5
			self.wait()
			database.load_data()
			database.PX = 315
			database.PY = 200
			database.MONEY -= 100 * len(database.PARTY[database.FORMATION])
			for i in database.PARTY[database.FORMATION]:
				database.CHARACTERS[i]['HP'] = database.CHARACTERS[i]['VITALITY'][database.CHARACTERS[i]['LEVEL']]
				database.CHARACTERS[i]['HEALTH'] = 0
			self.__init__()
			self.rendermap('hospital_0')
			self.transiction(False, 0)

	def hitisplay(self, ex, tar, dmg, col):
		self.dmgy = 200
		hitac = 8
		lgy = 1
		inf = 0
		wt = 0

		if tar == None:
			while ex != 0:
				self.screen.fill((255, 0, 0))
				if ex > 0:
					self.displayx = ex
					self.displayy = ex
					ex = -ex
				elif ex < 0:
					self.displayx = ex
					self.displayy = ex
					ex = -ex
					ex -= 1
				self.run()
			self.displayx = 0
			self.displayy = 0
			self.run()

		else:
			self.dmginfo = pygame.Surface((9 + (len(dmg) * 17),40), pygame.SRCALPHA, 32)
			self.dmginfo.convert_alpha()

			sx = tar.x
			sy = tar.y
			while wt < 10:
				tar.x = sx
				tar.y = sy
				if ex > 0:
					tar.x += ex
					tar.y += ex
					ex = -ex
				elif ex < 0:
					tar.x += ex
					tar.y += ex
					ex = -ex
					ex -= 1
				if inf == 0:
					self.dmgy -= hitac
					hitac -= 1
					lgy += 1
					if hitac == 0: inf = 1
				elif inf == 1:
					self.dmgy += hitac
					hitac += 1
					if hitac == 8: inf = 2
				elif ex == 0:
					wt += 1

				self.dmginfo.blit(self.mininfo.render(dmg, True, (0,0,0)), (11 - lgy, 11 - lgy))
				self.dmginfo.blit(self.mininfo.render(dmg, True, col), (10 - lgy, 10 - lgy))
				self.run()
			tar.x = sx
			tar.y = sy
		self.run()
		self.dmginfo = ''

	def attackimation(self, wh):
		self.effttack = wh
		self.effgif = 0
		ddg = False
		counter = False
		if wh != 10:
			while self.effgif < len(database.SPRITES['ATTACKIMATION_' + str(wh)]):
				for event in pygame.event.get():
					self.pressed = pygame.key.get_pressed()
					if self.pressed[database.ACT] and self.effgif == len(database.SPRITES['ATTACKIMATION_' + str(wh)]):
						ddg = True
				self.run()
				self.effgif += 0.5
		else:
			while True:
				for event in pygame.event.get():
					self.pressed = pygame.key.get_pressed()
					if self.pressed[database.ACT] and self.effgif > 4.0:
						counter = True
				if counter == False: self.effgif += 0.25
				if counter == True: self.effgif -= 0.25
				print(self.effgif)

				if self.effgif == len(database.SPRITES['ATTACKIMATION_' + str(wh)]): ddg = False; break
				elif self.effgif == 0.0: ddg = True; break
				self.run()

		self.effttack = None
		self.effgif = 0

		return ddg

	def rendermap(self, mp):
		if isinstance(mp,int):
			self.map = pytmx.load_pygame('Maps/urban_' + str(mp) + '.tmx'); database.MAP = mp; mp = 'urban_' + str(mp)
		elif mp != 'rodoviary':
			self.map = pytmx.load_pygame('Maps/' + mp + '.tmx')
		elif mp == 'rodoviary':
			self.map = pytmx.load_pygame('Maps/rodoviary.tmx'); database.MAP = 0
		else:
			self.map = pytmx.load_pygame('Maps/' + mp + '.tmx')
		self.room = mp
		self.cam.x = 0
		self.cam.y = 0
		self.tilmap = []
		self.objects = [[0,0,self.player['RECT'].y]]
		self.tilrect = []
		self.en = []
		self.foe = []
		self.npcs = []
		self.vehicles = []
		self.portals = []
		self.signs = []
		self.signal = self.map.properties['SIGNAL']

		#DRAW MAP
		for i in range(3):
			self.tilmap.append([])
			self.tilrect.append([])
			for a in range(2):
				self.tilmap[i].append(pygame.Surface((self.map.width * self.map.tilewidth,self.map.height * self.map.tileheight), pygame.SRCALPHA, 32))
				for x in range(0, self.map.width):
					for y in range(0, self.map.height):
						try: gid = self.map.get_tile_gid(x, y, i)
						except: gid = None
						if gid != None:
							tl = self.map.get_tile_properties_by_gid(gid)
							if tl != None:
								if tl['frames'] != []: image = self.map.get_tile_image_by_gid(tl['frames'][a].gid)
								else: image = self.map.get_tile_image_by_gid(gid)
								image.convert()
								self.tilmap[i][a].blit(image, (x * self.map.tilewidth - self.cam.x, y * self.map.tileheight - self.cam.y))

								if self.room != 'rodoviary' and i < 2:
									self.tilrect[i].append([self.map.get_tile_properties(x, y, i)['TYPE'].upper(),pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight,self.map.tilewidth,self.map.tileheight)])
						elif i == 0: self.tilrect[i].append(['WALL',pygame.Rect(x * 30, y * 30,30,30)])
		#NPCS
		ind = 0
		for i in range(len(self.map.layers[6])):
			obj = self.map.get_object_by_name('npc_' + str(i))
			self.npcs.append({'N': ind, 'RECT': pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)), 'TYPE': int(obj.type), 'INDEX': obj.properties['INDEX'], 'WHO': obj.properties['WHO'],
			'IMAGE': 0.0,'MOVE': 'horizontal','DIRECTION': 0,'SPD': 1, 'TIME': 20,'FOLLOW': None,'FOLLEND': 0})
			self.objects.append([2,ind,int(obj.y)])
			ind += 1

		#VEICHLES
		ind = 0
		for i in range(len(self.map.layers[5])):
			obj = self.map.get_object_by_name('vehicle_' + str(i))
			vh = database.VEHICLES['moto_' + str(obj.type)].copy()
			vh['RECT'] = pygame.Rect(float(obj.x), float(obj.y), 60, 10)
			vh['INDEX'] = int(obj.type)
			vh['N'] = ind
			self.vehicles.append(vh)
			self.objects.append([3,ind,int(obj.y)])
			ind += 1

		#PORTALS
		ind = 0
		for i in range(len(self.map.layers[4])):
			obj = self.map.get_object_by_name('portal_' + str(i))
			dt = {'N': ind, 'RECT': pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)), 'TYPE': int(obj.type), 'PX': obj.properties['PX'], 'PY': obj.properties['PY'], 'MAP': obj.properties['MAP']}
			if obj.properties['TIME'].startswith('key'):
				dt['OPENING'] = obj.properties['TIME'][0:3]; dt['CLOSURE'] = obj.properties['TIME'][3:7]
			elif obj.properties['TIME'] != 'none':
				dt['OPENING'] = [int(obj.properties['TIME'][0:2]),int(obj.properties['TIME'][2:4])]; dt['CLOSURE'] = [int(obj.properties['TIME'][4:6]),int(obj.properties['TIME'][6:8])]
			else:
				dt['OPENING'] = None; dt['CLOSURE'] = None
			self.portals.append(dt)
			self.objects.append([4,ind,int(obj.y)])
			ind += 1

		#SIGNS
		ind = 0
		for i in range(len(self.map.layers[3])):
			obj = self.map.get_object_by_name('text_' + str(i))
			self.signs.append({'N': ind, 'RECT': pygame.Rect(int(obj.x), int(obj.y), len(obj.properties['TEXT']) * 10, int(obj.height)), 'TYPE': int(obj.type), 'TEXT': obj.properties['TEXT']})
			self.objects.append([5,ind,int(obj.y)])
			ind += 1

		#ENEMIES
		if mp.startswith('urban') or mp.startswith('jungle') or mp.startswith('farm') or mp.startswith('sierra'):
			st = 0
			en = 0
			lst = []
			for i in self.map.properties['ENEMIES']:
				if i == '-': lst.append(self.map.properties['ENEMIES'][st:en]); st += en + 1
				en += 1
			for i in range(round(random.randint(3,10))):
				wh = lst[round(random.randint(0,len(lst) - 1))]
				self.en.append(database.FREAKS[wh].copy())
				self.en[i]['FILE'] = wh
				self.en[i]['SPRITE'] = pygame.image.load('Sprites/frk_' + (self.en[i]['FILE']) + '_stand.png')
				siz = pygame.image.load('Sprites/frk_' + self.en[i]['FILE'] + '_mini.png').get_rect()
				self.en[i]['RECT'] = pygame.Rect(round(random.randint(0, self.map.width * self.map.tilewidth)),round(random.randint(0, self.map.height * self.map.tileheight)),siz.width,siz.height)
				self.en[i]['MASK'] = pygame.Rect(230,180,44,85)
				self.en[i]['DIRECTION'] = 0
				self.en[i]['FIGHTING'] = False
				self.en[i]['HEALTH'] = 0
				self.en[i]['TIME'] = 20
				self.en[i]['FADE'] = 10
				self.en[i]['EFFECT'] = 0.0
				self.en[i]['JUMP'] = 0
				if mp == self.en[i]['HABITAT']:
					self.en[i]['AGILITY'] += 2
					self.en[i]['HP'] += 5
				self.objects.append([1,i,self.en[i]['RECT'].y])

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

	def notification(self, txt, col):
		self.nottxt = txt
		self.notcol = col
		self.notx = 0
		w = 0
		while self.notx < 180:
			self.run()
			self.notx += 20
		while w < 50:
			self.run()
			pygame.time.wait(1)
			w += 1
		self.notx = 0

	def draw(self):
		self.display.fill((0, 0, 0))

		#BATTLE
		if self.battle == True:
			#BACKGROUND
			if self.bbg != '':
				self.display.blit(self.bbg, (self.bbm, 0))
				if self.obstacles == True:
					self.display.blit(self.bbg, (self.bbm - 600, 0))
					self.bbm += 5
					if self.bbm > 600: self.bbm = 0

			count = 0
			for i in self.foe:
				if count == 5: break

				#FOES
				if i['FADE'] > 0 and i['HEALTH'] != 9:
					i['FIGHTING'] = True
					if i['MASK'].x < 600:
						if self.mnu == 2 and self.equip[self.turn] < 4 and i['HEALTH'] != 1:
							if i['DIRECTION'] == 1: i['MASK'].x += i['AGILITY']
							if i['DIRECTION'] == 5: i['MASK'].x -= i['AGILITY']

							if i['MASK'].x < 100: i['DIRECTION'] = 1
							if i['MASK'].x > 500: i['DIRECTION'] = 5

						img = i['SPRITE']
						if i['FADE'] < 10: img.blit(pygame.image.load('Sprites/eff_death_' + str(i['FADE']) + '.png'), (0,0), special_flags=pygame.BLEND_SUB)
						self.display.blit(img, (i['MASK'].x, i['MASK'].y))

						if i['HEALTH'] > 2:
							self.display.blit(database.SPRITES['EFFECT_' + str(i['HEALTH'])][math.floor(i['EFFECT'])], (i['MASK'].x + 5, i['MASK'].y - 10))
							i['EFFECT'] += 0.5
							if i['EFFECT'] >= len(database.SPRITES['EFFECT_' + str(i['HEALTH'])]): i['EFFECT'] = 0.0
						count += 1
					else: i['MASK'].x -= i['AGILITY']

			#SKIP PLAYER
			if self.mnu < 3:
				if self.turn >= len(self.fig): self.fight()
				if self.turn >= 0:
					if self.fig[self.turn]['HP'] <= 0 or self.fig[self.turn]['HEALTH'] in [8,12,13,14,15]: self.turn += 1

			#BLACK BARS
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

			#ENEMIES COUNT
			if self.winbar == 100:
				ce = 0
				for i in self.foe:
					if i['HP'] > 0: ce += 1
				self.display.blit(self.mininfo.render(str(ce) + '/' + str(len(self.foe)), True, (255,255,255)), (500, 20))

			#PLAYER BARS
				p = 0
				low = False

				while p < len(database.PARTY[database.FORMATION]):
					if p == self.turn:
						pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(p * 120,0,120,100))
						self.display.blit(self.mininfo.render(database.CHARACTERS[database.PARTY[database.FORMATION][p]]['NAME'].lower(), True, (0,0,0)), (10 + p * 120, 10))
					else: 
						self.display.blit(self.mininfo.render(database.CHARACTERS[database.PARTY[database.FORMATION][p]]['NAME'].lower(), True, (database.COLOR[0],database.COLOR[1],database.COLOR[2])), (10 + p * 120, 10))

					#LIFE BAR
					if database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP'] > 0:
						minush = int(100/(database.CHARACTERS[database.PARTY[database.FORMATION][p]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][p]]['LEVEL']]/database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP']))
					else: minush = 0
					if self.barhp[p] > minush:
						self.ch_sfx.play(database.SOUND['HP_LOSS'])
						self.barhp[p] -= 1
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10 + p * 120,40,100,20))
					if database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP'] > database.CHARACTERS[database.PARTY[database.FORMATION][p]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][p]]['LEVEL']]/5: hpcol = (0, 255, 0)
					elif database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP'] > 0:
						hpcol = (255, 0, 0)
						low = True
					else: hpcol = (255, 0, 0)
					if low == True:
						if self.ch_ton.get_busy() == False: self.ch_ton.play(database.SOUND['HP_LOW'])
					if self.barhp[p] > 0: pygame.draw.rect(self.display, (255,255,0), pygame.Rect(10 + p * 120,40,self.barhp[p],20))
					if database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP'] > 0:
						pygame.draw.rect(self.display, hpcol, pygame.Rect(10 + p * 120,40,int(100/(database.CHARACTERS[database.PARTY[database.FORMATION][p]]['VITALITY'][database.CHARACTERS[database.PARTY[database.FORMATION][p]]['LEVEL']]/database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HP'])),20))
					if database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HEALTH'] > 1:
						self.display.blit(pygame.image.load('Sprites/hl_' + str(database.CHARACTERS[database.PARTY[database.FORMATION][p]]['HEALTH']) + '.png'), (14 + p * 120, 44))

					#AMMO BAR
					if self.equip[p] < 4:
						if int(database.INVENTORY[database.PARTY[database.FORMATION][p]][4][self.equip[p] + 1][1]) > 0:
							minush = int(100/(database.ITEMS[database.INVENTORY[database.PARTY[database.FORMATION][p]][4][self.equip[p] + 1][0]][5]['CAPACITY']/int(database.INVENTORY[database.PARTY[database.FORMATION][p]][4][self.equip[p] + 1][1])))
						else: minush = 0
						if self.barpp[p][self.equip[p]] > minush:
							self.barpp[p][self.equip[p]] -= 1
						pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10 + p * 120,70,100,20))
						pygame.draw.rect(self.display, (0, 100, 255), pygame.Rect(10 + p * 120,70,self.barpp[p][self.equip[p]],20))
					p += 1

				if self.turn < len(database.PARTY[database.FORMATION]) and self.turn >= 0:
					#TIME BAR:
					pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(0,302,int(600/(100/self.btime)),10))
					if ce > 0 and self.mnu < 3 and self.turn < len(self.fig): self.btime -= 0.5
					if self.btime == 0:
						self.turn = len(self.fig)
						self.fight()

					#OPTIONS
					if self.mnu == 1:
						x = 0
						for i in database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][1:]:
							if self.equip[self.turn] == x: pygame.draw.rect(self.display, (database.COLOR[0], database.COLOR[1], database.COLOR[2]), pygame.Rect(118 + x * 35,338,32,32))
							else: pygame.draw.rect(self.display, (255,255,255), pygame.Rect(118 + x * 35,338,32,32))
							pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(120 + x * 35,340,28,28))
							if database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][x + 1][0] != '_':
								self.display.blit(pygame.image.load('Sprites/it_' + database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][x + 1][0] + '.png'), (120 + x * 35, 340))
							x += 1

						if self.equip[self.turn] == 4: pygame.draw.rect(self.display, (database.COLOR[0], database.COLOR[1], database.COLOR[2]), pygame.Rect(304,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(304,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_tactical.png'), (304, 338))

						if self.equip[self.turn] == 5: pygame.draw.rect(self.display, (database.COLOR[0], database.COLOR[1], database.COLOR[2]), pygame.Rect(339,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(339,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_talk.png'), (339, 338))

						if self.equip[self.turn] == 6: pygame.draw.rect(self.display, (database.COLOR[0], database.COLOR[1], database.COLOR[2]), pygame.Rect(374,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(374,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_guard.png'), (374, 338))

						if self.equip[self.turn] == 7: pygame.draw.rect(self.display, (database.COLOR[0], database.COLOR[1], database.COLOR[2]), pygame.Rect(409,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(409,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_run.png'), (409, 338))

						self.display.blit(pygame.image.load('Sprites/e_invphn.png'), (442, 338))

					#AIM BAR
					elif self.mnu == 2:
						if self.equip[self.turn] < 4:
							if database.CHARACTERS[database.PARTY[database.FORMATION][self.turn]]['HEALTH'] == 9:
								prb = random.randint(0,10)
								if prb > 5: self.aim.x += round(random.randint(30,60))
								if prb < 5: self.aim.x -= round(random.randint(30,60))
							else: self.aim.x += 20 - self.pagi[self.turn]
							if self.aim.x > 500 - self.patt[self.turn]:
								self.aim.x = 100 + self.patt[self.turn]
							chk = False
							for i in database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1:]:
								if i.startswith('aim') == True: chk = True; break
							if chk == True:
								self.display.blit(pygame.image.load('Sprites/aim_' + str(database.ITEMS[i][5]) + '.png'), (self.aim.x - 15, self.aim.y))
							else:
								self.display.blit(pygame.image.load('Sprites/aim_0.png'), (self.aim.x-15, self.aim.y))
							self.display.blit(pygame.image.load('Sprites/' + database.INVENTORY[database.PARTY[database.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0] + '.png'), (150 + int(self.aim.x/2), 255))

					#TACTICS
						elif self.equip[self.turn] == 4:
							x = 0
							for i in database.TACTICAL:
								if self.opt == x: pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(118 + x * 35,338,32,32))
								else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(118 + x * 35,338,32,32))
								pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(120 + x * 35,340,28,28))
								x += 1
			#PARTICLES
			if len(self.particles) > 0:
				for p in range(len(self.particles)):
					self.particles[p]['RADIUS'] -= 0.25
					if self.particles[p]['RADIUS'] <= 0.0:
						del self.particles[p]; break
					self.particles[p]['X'] += int(math.cos(self.particles[p]['DIRECTION']) * self.particles[p]['SPEED'])
					self.particles[p]['Y'] += int(math.sin(self.particles[p]['DIRECTION']) * self.particles[p]['SPEED'])
					pygame.draw.circle(self.display, (10, 255, 50), (self.particles[p]['X'],self.particles[p]['Y']), math.ceil(self.particles[p]['RADIUS']))

			#INFOHIT
			if self.dmginfo != '':
				self.display.blit(self.dmginfo, (self.aim.x, self.dmgy))

			#ATTACKIMATION
			if self.effttack != None:
				srf = pygame.Surface((self.displayzw,self.displayzh))
				srf.set_alpha(100)
				srf.fill((0, 0, 0))
				self.display.blit(srf, (0,0))
				self.display.blit(database.SPRITES['ATTACKIMATION_' + str(self.effttack)][math.floor(self.effgif)], (200,200))

			#WIN/LOST SCREEN
			if self.winbar > 200:
				if self.turn == -4:
					if self.hpl < 0: self.display.blit(self.mininfo.render(database.BATTLE[6], True, (255,255,255)), (130 + self.mnu, 70))
					else: self.display.blit(self.mininfo.render(database.BATTLE[7], True, (255,255,255)), (130 + self.mnu, 70))
					'''self.display.blit(self.monotype.render(database.BATTLE[9] + str(self.hits), True, (255,255,255)), (180 + self.mnu, 120))
					self.display.blit(self.monotype.render(database.BATTLE[10] + str(self.tdmg), True, (255,255,255)), (180 + self.mnu, 140))
					self.display.blit(self.monotype.render(database.BATTLE[11] + str(self.hpl), True, (255,255,255)), (180 + self.mnu, 160))
					self.display.blit(self.monotype.render(database.BATTLE[12]+str(self.tbt), True, (255,255,255)), (180 + self.mnu, 180))
					#self.display.blit(self.monotype.render(database.BATTLE[12] + str(len(self.fig)), True, (255,255,255)), (180 + self.mnu, 200))
					self.display.blit(self.monotype.render('= ' + str(self.xp) + database.BATTLE[13], True, (255,255,255)), (180 + self.mnu, 200))'''

					if self.greenblood > 0 and int(200/(1000/self.greenblood)) >= 1:
						pygame.draw.rect(self.display, (0, 255, 100), pygame.Rect(460 + self.mnu,300 - int(200/(1000/self.greenblood)),30,int(200/(1000/self.greenblood))))
						pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(500 + self.mnu,280 - int(200/(1000/self.greenblood)),50,20))
						self.display.blit(self.monotype.render(str(self.greenblood) + 'ml', True, (0,0,0)), (505 + self.mnu, 278 - int(200/(1000/self.greenblood))))
					self.display.blit(pygame.image.load('Sprites/gbbar.png'), (460 + self.mnu, 100))

					for i in range(len(database.PARTY[database.FORMATION])):
						self.display.blit(pygame.image.load('Sprites/who_' + str(database.PARTY[database.FORMATION][i]) + '.png'), (100 + self.mnu, 120 + i * 30))
						pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(130 + self.mnu,120 + i * 30,100,20))
						if self.barxp[i] > 0: pygame.draw.rect(self.display, (0, 255, 100), pygame.Rect(130 + self.mnu,120 + i * 30,self.barxp[i],20))

					self.display.blit(self.mininfo.render(database.CHARACTERS[0]['NAME'].lower(), True, (255,255,255)), (800 + self.mnu * 2, 70))
					self.display.blit(self.monotype.render(database.BATTLE[14] + str(database.CHARACTERS[0]['LEVEL']) + ' !', True, (255,255,255)), (800 + self.mnu * 2, 100))
					self.display.blit(self.mininfo.render(database.BATTLE[39] + ' +' + str(database.CHARACTERS[0]['STRENGHT'][database.CHARACTERS[0]['LEVEL']] - database.CHARACTERS[0]['STRENGHT'][database.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 200))
					self.display.blit(self.mininfo.render(database.BATTLE[40] + ' +' + str(database.CHARACTERS[0]['ATTACK'][database.CHARACTERS[0]['LEVEL']] - database.CHARACTERS[0]['ATTACK'][database.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 230))
					self.display.blit(self.mininfo.render(database.BATTLE[41] + ' +' + str(database.CHARACTERS[0]['AGILITY'][database.CHARACTERS[0]['LEVEL']] - database.CHARACTERS[0]['AGILITY'][database.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 260))
					self.display.blit(self.mininfo.render(database.BATTLE[42] + ' +' + str(database.CHARACTERS[0]['RESISTANCE'][database.CHARACTERS[0]['LEVEL']] - database.CHARACTERS[0]['RESISTANCE'][database.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 290))
					self.display.blit(self.mininfo.render(database.BATTLE[43] + ' +' + str(database.CHARACTERS[0]['VITALITY'][database.CHARACTERS[0]['LEVEL']] - database.CHARACTERS[0]['VITALITY'][database.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 320))

				elif self.turn == -5:
					self.display.blit(self.mininfo.render(database.BATTLE[8], True, (255,255,255)), (200 + self.mnu, 70))
					self.display.blit(self.monotype.render('-$' + str(database.MONEY), True, (255,255,255)), (200 + self.mnu, 120))

		elif self.battle == False and database.MAP > 0:
			#TILED MAP
			self.display.blit(self.tilmap[0][math.floor(self.tilemation)], (0 - self.cam.x, 0 - self.cam.y))
			self.display.blit(self.tilmap[1][math.floor(self.tilemation)], (0 - self.cam.x, 0 - self.cam.y))
			'''self.display.blit(self.tilmap[0 + math.floor(self.tilemation)], (0 - self.cam.x, 0 - self.cam.y))
			self.display.blit(self.tilmap[2 + math.floor(self.tilemation)], (0 - self.cam.x, 0 - self.cam.y))'''

			'''for t in self.tilrect[0 + math.floor(self.tilemation)]:
				if self.colide(t[1],self.cam): self.display.blit(t[2], (t[1].x - self.cam.x, t[1].y - self.cam.y))
			for t in self.tilrect[2 + math.floor(self.tilemation)]:
				if self.colide(t[1],self.cam): self.display.blit(t[2], (t[1].x - self.cam.x, t[1].y - self.cam.y))'''

			#ANIMATION
			if self.player['PAUSE'] < 2: self.player['GIF'] += 0.5
			if self.player['GIF'] >= len(database.SPRITES[self.player['SPRITE']]): self.player['GIF'] = 0
			if self.player['PAUSE'] < 2: self.player['BLINK'] -= 1
			if self.player['BLINK'] < 0: self.player['BLINK'] = round(random.randint(30,90))
			if self.player['PAUSE'] < 2: self.tilemation += 0.1
			if self.tilemation >= 2.0: self.tilemation = 0.0

			#DEPTH
			dpth = 0
			for i in range(len(self.objects)):
				if i!= len(self.objects) - 1:
					if self.objects[i][2] > self.objects[i + 1][2]:
						self.objects.insert(i, self.objects[i + 1])
						del self.objects[i + 2]
			#JUMP
			if self.player['GRAVITY'] > -5:
				self.player['JUMP'] += self.player['GRAVITY']
				self.player['GRAVITY'] -= 0.5

			for y in self.objects:
				if y[0] == 0:
					#pygame.draw.rect(self.display, (0,0,255), pygame.Rect(self.player['RECT'].x - self.cam.x, self.player['RECT'].y - self.cam.y, self.player['RECT'].width, self.player['RECT'].height))
					#PLAYER
					if self.sleepin == False:
						self.display.blit(database.SPRITES[self.player['SPRITE']][math.floor(self.player['GIF'])], (self.player['RECT'].x - self.cam.x,self.player['RECT'].y - self.cam.y - 10 - self.player['JUMP']))
						self.display.blit(pygame.image.load('Sprites/it_shade.png'), (self.player['RECT'].x - self.cam.x - 1,self.player['RECT'].y - self.cam.y + 7))
						xsp = 0
						if self.player['SPD'] == 0 and self.player['GIF'] >= 1.0 and self.player['GIF'] < 3.0: xsp = 1
						if self.player['SPD'] > 0:
							if self.player['GIF'] >= 0.0 and self.player['GIF'] < 1.0: xsp = 0
							elif self.player['GIF'] >= 4.0 and self.player['GIF'] < 5.0: xsp = 0
							else: xsp = 1
						if self.player['JUMP'] > 0: xsp = 0
						if self.player['BLINK'] < 2 and self.player['DIRECTION'] < 6 and self.player['GRAVITY'] == -5 and self.player['JUMP'] == 0:
							self.display.blit(database.SPRITES[self.player['HEAD']][1], (self.player['RECT'].x - self.cam.x,self.player['RECT'].y - self.cam.y - 21 + xsp - self.player['JUMP']))
						else: self.display.blit(database.SPRITES[self.player['HEAD']][0], (self.player['RECT'].x - self.cam.x,self.player['RECT'].y - self.cam.y - 21 + xsp - self.player['JUMP']))

					#CONDITIONS
					if database.CHARACTERS[database.PARTY[database.FORMATION][0]]['HEALTH'] > 1:
						if database.CHARACTERS[database.PARTY[database.FORMATION][0]]['SHK'] == 0:
							pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(self.player['RECT'].x - self.cam.x + 10 + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['SHK'],self.player['RECT'].y - self.cam.y - 40,16,13))
						else: pygame.draw.rect(self.display, (255,10,10), pygame.Rect(self.player['RECT'].x - self.cam.x + 10 + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['SHK'],self.player['RECT'].y - self.cam.y - 40,16,13))
						self.display.blit(pygame.image.load('Sprites/hl_' + str(database.CHARACTERS[database.PARTY[database.FORMATION][0]]['HEALTH']) + '.png'), (self.player['RECT'].x - self.cam.x + 10 + database.CHARACTERS[database.PARTY[database.FORMATION][0]]['SHK'],self.player['RECT'].y - self.cam.y - 40))

					y[2] = self.player['RECT'].y

					#TILE COLISION
					for t in range(2):
						for i in self.tilrect[t]:
							if self.colide(self.player['RECT'],i[1]) and self.player['SPD'] > 0 and self.dlgfa > 0 and self.player['PAUSE'] == 0:
								if self.driving == 0:
									if i[0].startswith('JUMP') and self.player['DIRECTION'] == int(i[0][4]) and self.player['GRAVITY'] == -5:
										self.player['GRAVITY'] = 4.5
										self.ch_sfx.play(database.SOUND['FALL'])
									elif i[0] != 'WALL' and i[0].startswith('JUMP') == False and self.player['JUMP'] == 0:
										self.ch_stp.stop()
										self.ch_stp.play(database.SOUND['STEP_' + i[0]])
								elif i[0] != 'WALL' and i[0].startswith('JUMP') == False and self.player['JUMP'] == 0:
									self.ch_stp.stop()
									self.ch_stp.play(database.SOUND['STEP_VEHICLE'])

				#OBJECTS
				if y[0] == 1:
					for i in range(len(self.en)):
						if self.en[i]['HP'] > 0 and i == y[1]: self.enemy(i)
				elif y[0] == 2:
					for i in self.npcs:
						i['IMAGE'] += 0.5
						if i['IMAGE'] == 2.0: i['IMAGE'] = 0.0
						if i['N'] == y[1]: self.npc(i); y[2] = i['RECT'].y
				elif y[0] == 3:
					for i in self.vehicles:
						if i['N'] == y[1]: self.vehicle(i); y[2] = i['RECT'].y
				elif y[0] == 4:
					for i in self.portals:
						if i['N'] == y[1]: self.portal(i); y[2] = i['RECT'].y
				elif y[0] == 5:
					for i in self.signs:
						if i['N'] == y[1]:
							if self.colide(i['RECT'], self.cam):
								pygame.draw.rect(self.display, (250, 250, 250), pygame.Rect(i['RECT'].x - self.cam.x, i['RECT'].y - self.cam.y, i['RECT'].width, i['RECT'].height))
								self.display.blit(self.monotype.render(database.SIGNS[i['TEXT']], True, (0,0,0)), (i['RECT'].x - self.cam.x,i['RECT'].y - self.cam.y))
							y[2] = i['RECT'].y

			self.display.blit(self.tilmap[2][math.floor(self.tilemation)], (0 - self.cam.x, 0 - self.cam.y))
			'''for t in self.tilrect[4 + math.floor(self.tilemation)]:
				if self.colide(t[1],self.cam): self.display.blit(t[2], (t[1].x - self.cam.x, t[1].y - self.cam.y))'''

			#DAYTIME & WEATHER
			if database.TIME[0] > 18: tim = 100
			elif database.TIME[0] > 6: tim = 0
			else: tim = 100
			srf = pygame.Surface((self.displayzw,self.displayzh))
			srf.set_alpha(tim)
			srf.fill((0, 58, 160))
			self.display.blit(srf, (0,0))

			if len(self.particles) > 0:
				for p in range(len(self.particles)):
					if self.particles[p]['RADIUS'] <= 0.0:
						del self.particles[p]; break
					self.particles[p]['Y'] += int(math.sin(self.particles[p]['DIRECTION']) * self.particles[p]['SPEED'])
					pygame.draw.circle(self.display, (10, 50, 255), (self.particles[p]['X'],self.particles[p]['Y']), math.ceil(self.particles[p]['RADIUS']))

			#MINI MAP
			try:
				pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,self.displayzh - (106 * int(self.displayzh/400)),106 * int(self.displayzw/600),106 * int(self.displayzh/400)))
				self.display.blit(self.minimap(database.MAP, self.player['RECT'].x, self.player['RECT'].y, self.displayzw, self.displayzh, self.signal), (3 * int(self.displayzh/400),self.displayzh - (103 * int(self.displayzh/400))))
				self.display.blit(pygame.image.load('Sprites/mp_player.png'), (48 * int(self.displayzh/400),self.displayzh - (59 * int(self.displayzh/400))))
			except: pass

			#DRIVING BARS
			if self.driving > 0:
				pygame.draw.rect(self.display, (10,10,10), pygame.Rect(20,20,100,20))
				if database.GAS >= 1: pygame.draw.rect(self.display, (255,155,66), pygame.Rect(20,20,int(100/(self.vehicles[self.driving - 1]['CAPACITY']/round(database.GAS))),20))
				pygame.draw.rect(self.display, (10,10,10), pygame.Rect(20,42,100,20))
				if self.player['SPD'] > 0: pygame.draw.rect(self.display, (0,255,0), pygame.Rect(20,42,int(100/(20/self.player['SPD'])),20))

		#HEALTH DAMAGE
		for i in database.PARTY[database.FORMATION]:
			if database.CHARACTERS[i]['HEALTH'] in [4,5,6,7,16,17,18,19,20,21] and self.dlgfa > 0:
				database.CHARACTERS[i]['DMGTIM'] -= 1
				if database.CHARACTERS[i]['DMGTIM'] == 0:
					database.CHARACTERS[i]['DMGTIM'] = 100
					database.CHARACTERS[i]['SHK'] = 3
					database.CHARACTERS[i]['HP'] -= 1

					'''dth = 0
					for d in self.fig:
						if d['HP'] <= 0: dth += 1
					if dth == len(self.fig):'''
					if database.CHARACTERS[i]['HP'] <= 0:
						database.CHARACTERS[i]['HEALTH'] = 0
						self.ch_msc.fadeout(500)
						self.ch_ton.play(database.SOUND['BATTLE_LOST'])
						self.transiction(True, 210)
						self.battle = True
						self.turn = -5
						self.mnu = 600
						acc = 60
						while self.mnu > 0:
							self.mnu -= acc
							acc -= 2
							self.run()
						self.turn = -5
						self.wait()
						#database.load_data()
						database.PX = 315
						database.PY = 200
						database.MONEY -= 100 * len(database.PARTY[database.FORMATION])
						for w in database.PARTY[database.FORMATION]:
							database.CHARACTERS[w]['HP'] = database.CHARACTERS[w]['VITALITY'][database.CHARACTERS[w]['LEVEL']]
							database.CHARACTERS[w]['HEALTH'] = 0
						self.__init__()
						self.rendermap('hospital_0')
						self.transiction(False, 0)

					self.ch_ton.play(database.SOUND['DAMAGE_1'])
				if database.CHARACTERS[i]['SHK'] > 0: database.CHARACTERS[i]['SHK'] = -database.CHARACTERS[i]['SHK']
				elif database.CHARACTERS[i]['SHK'] < 0: database.CHARACTERS[i]['SHK'] = -database.CHARACTERS[i]['SHK'] - 1

		#RODOVIARY
		if database.MAP == 0:
			self.display.blit(pygame.image.load('Backgrounds/rodoviary.png'), (0 - self.cam.x, 0 - self.cam.y))
			pygame.draw.rect(self.display, (0,0,255), pygame.Rect(self.player['RECT'].x - self.cam.x, self.player['RECT'].y - self.cam.y, self.player['RECT'].width, self.player['RECT'].height))
			self.display.blit(pygame.image.load('Sprites/mp_player.png'), (self.player['RECT'].x - self.cam.x, self.player['RECT'].y - self.cam.y))
			for i in self.portals:
				self.portal(i)

		#BLACK BARS
		if self.battle == False and self.winbar > 0:
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

		#INVENTORY
		if self.invfade < 1050:
			if self.inventory != 2: self.display.blit(self.inv.show(self.opt, self.lopt, self.mnu, self.exvar), (610 - self.invfade,60))
			else: self.display.blit(self.inv.deposit(self.opt, self.lopt, self.mnu, self.exvar), (610 - self.invfade,60))
		if self.inventory > 0:
			if self.invfade < 500: self.invfade += 50
		else:
			if self.invfade < 1050: self.invfade += 50

		#SHOP
		if self.shp == True:
			if self.mnu == 0:
				self.display.blit(self.shpmnu.products(self.opt, self.lopt, self.products), (100,60))
			if self.mnu == 1:
				self.display.blit(self.shpmnu.buy(self.opt, self.lopt, self.basket), (100,60))
			if self.mnu == 2:
				lst = []
				if self.opt == 0: lst = self.products
				else: lst = self.basket
				self.display.blit(self.shpmnu.mercator(self.opt, self.lopt, lst, self.promo), (100,60))
			if self.mnu == 3 or self.mnu == 11 or self.mnu == 12:
				self.display.blit(self.shpmnu.bank(self.opt, self.lopt, self.mnu, self.extract), (100,60))

		#PHONE
		if self.phofa > 0:
			self.display.blit(pygame.image.load('Backgrounds/phone.png'), (200, 400 - self.phofa))
			if self.battle == False: pygame.draw.rect(self.display, (10,10,10), pygame.Rect(210,430 - self.phofa,180,250))
		if self.phone > 0:
			if self.phofa == 320: self.ch_sfx.play(database.SOUND['PHONE_UNLOCK'])
			if self.phofa < 360: self.phofa += 40
		else:
			if self.phofa == 360: self.ch_sfx.play(database.SOUND['PHONE_LOCK'])
			if self.phofa > 0: self.phofa -= 40
		if self.phofa == 360 and database.BATTERY > 1.0:
			self.display.blit(self.phn.bar(self.signal), (210,70))
			if self.battle == False:
				if self.phone == 1: self.display.blit(self.phn.apps(self.opt, self.lopt), (210,88))
				elif self.phone == 2: self.display.blit(self.phn.map('urban_', self.opt, self.lopt, self.mnu, self.signal), (210,88))
				elif self.phone == 3: self.display.blit(self.phn.contacts(self.opt, self.lopt, self.mnu), (210,88))
				elif self.phone == 4: self.display.blit(self.phn.email(self.opt, self.lopt, self.mnu, self.signal), (210,88))
				elif self.phone == 5: self.display.blit(self.phn.news(self.lopt, self.mnu, self.signal), (210,88))
				elif self.phone == 6: self.display.blit(self.phn.radio(self.fm, self.msc), (210,88))
				elif self.phone == 7: self.display.blit(self.phn.camera(self.lopt, self.signal), (210,88))
				elif self.phone == 8: self.display.blit(self.phn.bestiary(self.opt, self.lopt, self.mnu, self.signal), (210,88))
				elif self.phone == 9: self.display.blit(self.phn.task(self.opt, self.lopt, self.mnu), (210,88))
				elif self.phone == 10: self.display.blit(self.phn.status(self.opt), (210,88))
				elif self.phone == 11: self.display.blit(self.phn.tactics(self.opt, self.lopt, self.mnu, self.signal), (210,88))
				elif self.phone == 12: self.display.blit(self.phn.achievements(self.lopt, self.signal), (210,88))
				elif self.phone == 13: self.display.blit(self.phn.ranking(self.opt, self.signal), (210,88))
				elif self.phone == 14: self.display.blit(self.phn.help(self.lopt, self.mnu), (210,88))
				elif self.phone == 15: self.display.blit(self.phn.settings(self.lopt, self.mnu, self.opt), (210,88))
				elif self.phone == 16: self.display.blit(self.phn.info(self.lopt), (210,88))
				elif self.phone == 17 and self.nb != '': self.display.blit(self.phn.call(self.opt, self.nb), (210,88))
		elif self.phofa == 360:
			self.display.blit(pygame.image.load('Backgrounds/battery_low.png'), (270, 510 - self.phofa))
			if self.battle == True: pygame.draw.rect(self.display, (10,10,10), pygame.Rect(210,430 - self.phofa,180,250))

		#NAMING
		if self.nmenu.show == True:
			self.display.blit(self.nmenu.run(), (200, 100))

		#RADIOPLAY
		if self.radonoff == True:
			pygame.draw.rect(self.display, (255, 0, 135), pygame.Rect(0,0,180,50))
			self.display.blit(self.monotype.render('Tocando:', True, (0, 0, 0)), (10, 5))
			self.display.blit(self.monotype.render(database.RADIO[str(math.floor(self.fm/20))][self.msc][:-4], True, (0, 0, 0)), (10, 25))
		if pygame.mixer.music.get_busy() == False and self.radonoff == True:
			self.msc += 1
			if self.msc > len(database.RADIO[str(round(self.fm/20))]) - 1: self.msc = 0
			if database.RADIO[str(round(self.fm/20))] != []:
				pygame.mixer.music.load('Songs/FM_' + str(round(self.fm/20)) + '/' + database.RADIO[str(round(self.fm/20))][self.msc])
				pygame.mixer.music.play()

		#DIALOG
		'''if self.dlgfa < 500:
			pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(50,30,500 - self.dlgfa,100))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(55,35,490 - self.dlgfa,90))
			if self.dlg != []:
				if self.lopt > 0:
					pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(70,30 + self.lopt * 20,460,20))
				y = 0
				for i in self.dlg:
					if (self.lopt - 1) * 20 == y: self.display.blit(self.monotype.render(i, True, (0, 0, 0)), (70, 50 + y))
					else: self.display.blit(self.monotype.render(i, True, (255, 255, 255)), (70, 50 + y))
					y += 20'''

		if self.dlgfa < 500 and database.SCENE != -1 and self.nmenu.show == False:
			if self.dlg != []:
				self.dlgy = 0
				sd = False
				opt = 1
				ind = 0
				for i in self.dlg:
					if i == 0: sd = not sd
				for i in self.dlg[::-1]:
					lng = 0
					if isinstance(i,str):
						for l in i:
							if l in ['m','w','M','Q','T','U','V','W','Y','?']: lng += 8
							elif l in ['f','r']: lng += 6
							elif l in ['J']: lng += 5
							elif l in ['l']: lng += 4
							elif l in ['i','I','!','.',',']: lng += 2
							else: lng += 7
						lng += 20
					if i != 1 and i != 0 and len(i) != 0:
						if sd == False:
							pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(20,200 - self.dlgy,5 + lng,25))
							pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(20,225 - self.dlgy,5 + lng,5))
							pygame.draw.polygon(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), ((25,225 - self.dlgy),(45,225 - self.dlgy),(25,235 - self.dlgy)))
							pygame.draw.polygon(self.display, (0, 0, 0), ((25,221 - self.dlgy),(45,221 - self.dlgy),(25,231 - self.dlgy)))
						else:
							if self.lopt == opt:
								pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(568 - lng,200 - self.dlgy,15 + lng,25))
								pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(568 - lng,225 - self.dlgy,15 + lng,5))
								pygame.draw.polygon(self.display, (0, 0, 0), ((548,225 - self.dlgy),(568,225 - self.dlgy),(568,235 - self.dlgy)))
								pygame.draw.polygon(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), ((548,221 - self.dlgy),(568,221 - self.dlgy),(568,231 - self.dlgy)))
							else:
								pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(578 - lng,200 - self.dlgy,5 + lng,25))
								pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(578 - lng,225 - self.dlgy,5 + lng,5))
								pygame.draw.polygon(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), ((558,225 - self.dlgy),(578,225 - self.dlgy),(578,235 - self.dlgy)))
								pygame.draw.polygon(self.display, (0, 0, 0), ((558,221 - self.dlgy),(578,221 - self.dlgy),(578,231 - self.dlgy)))
							opt += 1
					if i == 0:
						if sd == False: sd = True
						elif sd == True: sd = False
					elif isinstance(i, str):
						if sd == False:
							self.display.blit(self.monotype.render(i, True, (255, 255, 255)), (30, 202 - self.dlgy))
						else:
							self.display.blit(self.monotype.render(i, True, (255, 255, 255)), (588 - lng, 202 - self.dlgy))
						self.dlgy += 40
					ind += 1

		#NOTIFICATIONS
		if self.notx > 0:
			if self.notcol != (0,0,0): pygame.draw.rect(self.display, (0,0,0), pygame.Rect(-183 + self.notx,27,186,56))
			else: pygame.draw.rect(self.display, (255,255,255), pygame.Rect(-183 + self.notx,27,186,56))
			pygame.draw.rect(self.display, self.notcol, pygame.Rect(-180 + self.notx,30,180,50))
			if isinstance(self.nottxt,str):
				self.display.blit(self.monotype.render(self.nottxt, True, (0, 0, 0)), (-170 + self.notx, 40))
			else:
				pygame.draw.rect(self.display, (255,255,255), pygame.Rect(-170 + self.notx,40,160,30))
				pygame.draw.rect(self.display, (0,0,0), pygame.Rect(-168 + self.notx,42,156,26))
				if database.MORALITY > 0:
					pygame.draw.rect(self.display, (255,255,0), pygame.Rect(-90 + self.notx,45,int(70/(10/database.MORALITY)),20))
				if database.MORALITY < 0:
					pygame.draw.rect(self.display, (175,0,0), pygame.Rect(-int(70/(10/database.MORALITY)) - 160 + self.notx,45,int(70/(10/database.MORALITY)),20))
				pygame.draw.line(self.display, (255,255,255), (-90 + self.notx,42),(-90 + self.notx,68),2)

		#CHAPTER NAME
		if database.SCENE == -1:
			'''arr = pygame.surfarray.pixels3d(self.display)
			arr[:,:,0] = 255
			arr[:,:,1] -= 50
			arr[:,:,2] -= 50'''
			srf = pygame.Surface((self.displayzw,self.displayzh))
			srf.set_alpha(200)
			srf.fill((221, 0, 0))
			self.display.blit(srf, (0,0))
			pygame.draw.rect(self.display, (250,250,250), pygame.Rect(0,160,600,80))
			self.display.blit(self.mininfo.render(database.CHAPTERS[database.CHAPTER][0].lower(), True, (10, 10, 10)), (10, 200))
			pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(0,167,600,3))
			pygame.draw.rect(self.display, (10,10,10), pygame.Rect(0,170,600,22))
			pygame.draw.rect(self.display, (database.COLOR[0],database.COLOR[1],database.COLOR[2]), pygame.Rect(0,192,600,3))
			self.display.blit(self.monotype.render(database.CHAPTERS[database.CHAPTER][1], True, (250, 250, 250)), (10, 170))

		#CAMERA
		if self.speakin == 0:
			self.cam.x += int((self.player['RECT'].x  - self.cam.x - self.displayzw/2)/15)
			self.cam.y += int((self.player['RECT'].y  - self.cam.y - self.displayzh/2)/15)
		else:
			self.cam.x += int((self.speakin.x  - self.cam.x - self.displayzw/2)/15)
			self.cam.y += int((self.speakin.y  - self.cam.y - self.displayzh/2)/15)

		if self.cam.x < 0: self.cam.x = 0
		if self.cam.y < 0: self.cam.y = 0
		if self.cam.x > (self.map.width * self.map.tilewidth) - self.displayzw: self.cam.x = (self.map.width * self.map.tilewidth) - self.displayzw
		if self.cam.y > (self.map.height * self.map.tileheight) - self.displayzh: self.cam.y = (self.map.height * self.map.tileheight) - self.displayzh

		self.screen.blit(pygame.transform.scale(self.display, (self.windoww, self.windowh)), (self.displayx, self.displayy))

		pygame.display.update()
		pygame.display.flip()

	def run(self):
		self.glock.tick(self.FPS)
		if self.nmenu.show == False:
			self.events()
		self.draw()

		#DATETIME
		if self.sleepin == False:
			database.TIME[2] += 1
			for i in database.PARTY[database.FORMATION]:
				ph = self.inv.find(i,'phone')
				if ph != None:
					bt = float(ph[1][0:3])
					bt -= 0.05
			if self.phone > 0: database.BATTERY -= 0.05
		else:
			database.TIME[1] += 5
			database.BATTERY -= 2.5

		if database.BATTERY < 1.0:
			if self.radonoff == True:
				self.radonoff = False
				self.ch_ton.stop()
				pygame.mixer.music.stop()
			database.BATTERY = 1.0
		if database.TIME[2] >= 60:
			database.TIME[1] += 1
			database.TIME[2] = 0

		if database.TIME[1] >= 60:
			database.TIME[0] += 1
			database.TIME[1] = 0

			for p in database.PARTY[database.FORMATION]:
				if database.CHARACTERS[p]['HUNGER'] == 0: database.CHARACTERS[p]['HEALTH'] = 6
				else: database.CHARACTERS[p]['HUNGER'] -= 1
				if database.CHARACTERS[p]['THIRST'] == 0: database.CHARACTERS[p]['HEALTH'] = 7
				else: database.CHARACTERS[p]['THIRST'] -= 1
				if database.CHARACTERS[p]['SLEEP'] == 0: database.CHARACTERS[p]['HEALTH'] = 8
				else: database.CHARACTERS[p]['SLEEP'] -= 1
			print(database.CHARACTERS[1]['HUNGER'])
			print(database.CHARACTERS[1]['THIRST'])
			print(database.CHARACTERS[1]['SLEEP'])


		if database.TIME[0] >= 24:
			database.DATE[0] += 1
			database.DATE[3] += 1
			database.TIME[0] = 0

		if database.DATE[0] >= 30:
			database.DATE[1] += 1
			database.DATE[0] = 1

		if database.DATE[1] >= 12:
			database.DATE[2] += 1
			database.DATE[1] = 1

		if database.DATE[3] > 7:
			database.DATE[3] = 1

		#WAITIME
		for i in range(len(self.waitime)):
			if self.waitime[i][1] <= database.TIME[0] and self.waitime[i][2] <= database.TIME[1] and self.dlgfa > 0 and self.battle == False:
				if self.waitime[i][0] == 'sun':
					database.WEATHER = 0
					tm = database.TIME[1] + 5
					hm = database.TIME[0]
					if tm > 60: tm -= 60; hm += 1
					self.waitime.append(['rain',hm,tm])
				elif self.waitime[i][0] == 'rain':
					database.WEATHER = 1
					tm = database.TIME[1] + 5
					hm = database.TIME[0]
					if tm > 60: tm -= 60; hm += 1
					self.waitime.append(['sun',hm,tm])
				elif self.waitime[i][0].startswith('repellent'):
					database.CHARACTERS[int(self.waitime[i][0][9])]['HEALTH'] = 0
				elif self.waitime[i][0].startswith('cal'):
					self.ch_ton.play(database.SOUND['CALLING'],-1)
					self.ch_rng.play(database.SOUND['RINGTONE_' + str(self.phn.pbg)],-1)
					if self.radonoff == True: pygame.mixer.music.pause()
					if self.phone > 0: self.phone = 17
					self.nb = self.waitime[i][0][3:]
					tm = database.TIME[1] + 5
					hm = database.TIME[0]
					if tm > 60: tm -= 60; hm += 1
					self.waitime.append(['cutcal',hm,tm])
				elif self.waitime[i][0].startswith('cutcal'):
					if self.nb != '':
						self.ch_ton.stop()
						self.ch_rng.stop()
						self.nb = ''
						if self.phone == 17: self.phone = 1
				elif self.waitime[i][0].startswith('maicon'):
					self.npcs.append({'N': len(self.npcs), 'RECT': pygame.Rect(self.player['RECT'].x - 20, self.player['RECT'].y, 0, 0), 'TYPE': 4, 'INDEX': 0, 'WHO': 'MAICON', 'IMAGE': 0.0,'MOVE': 'fixed','DIRECTION': 3})
					self.objects.append([3,len(self.npcs),self.player['RECT'].y])
				elif self.waitime[i][0].startswith('mercador'):
					self.npcs.append({'N': len(self.npcs), 'RECT': pygame.Rect(self.player['RECT'].x - 20, self.player['RECT'].y, 0, 0), 'TYPE': 3, 'INDEX': 0, 'WHO': 'MERCATOR', 'IMAGE': 0.0,'MOVE': 'fixed','DIRECTION': 3})
					self.objects.append([3,len(self.npcs),self.player['RECT'].y])
				elif self.waitime[i][0].startswith('pizza'):
					self.npcs.append({'N': len(self.npcs), 'RECT': pygame.Rect(self.player['RECT'].x - 20, self.player['RECT'].y, 0, 0), 'TYPE': 0, 'WHO': self.waitime[i][0][9:].upper(), 'INDEX': 0,'IMAGE': 0.0,'MOVE': 'fixed','DIRECTION': 3})
					self.objects.append([3,len(self.npcs),self.player['RECT'].y])
				elif self.waitime[i][0].startswith('advice'):
					if self.dlgfa > 0:
						self.dialog(database.DIALOGS['ADVICE'])
				del self.waitime[i]
				break

		#FOOD WASTE
		for b in database.INVENTORY:
			for j in b:
				for i in j:
					if i[0].startswith('food') == True and i[0].endswith('wasted') == False:
						if int(i[1][2:4]) <= database.DATE[1]:
							if int(i[1][0:2]) <= database.DATE[0]:
								i[0] += '_wasted' 

		database.GAMETIME += 0.05


print(menu.FILES)
if menu.FILES[2] == 0:
	t = Title()
	while t.classrun == True: t.run()
else: database.new_data()

g = Game()
if database.GAMETIME > 0: g.transiction(False, 0)
while True: g.run()