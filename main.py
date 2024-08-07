# -*- coding: utf-8 -*-
import pygame
import pytmx
import random
import sqlite3
import webbrowser
from mutagen.mp3 import MP3
import numpy
import math
import sys
import resources
import os
import menu

pygame.init()
pygame.display.set_caption('Mutation Purge')
pygame.display.set_icon(pygame.image.load('icon.ico'))
pygame.mouse.set_visible(False)
if resources.FILES[3] != []:
	if resources.FILES[3][0] == 'PT': import database_PT as database
	if resources.FILES[3][0] == 'EN': import database_EN as database
else: import database_PT as database

class Loading():
	def __init__(self):
		self.screen = pygame.display.set_mode(resources.SCREEN_SIZE, pygame.RESIZABLE)
		self.display = pygame.Surface(resources.SURFACE_SIZE)
		self.monotype = pygame.font.Font('Fonts/monotype.ttf', 15)
		self.load = 0
		self.classrun = True
		self.dot = ''
		self.txt = 0
		self.msg = 0
		self.tim = 1.0
		self.gif = 0

	def callresources(self):
		self.load = 2
		self.txt = 1
		'''for w in range(resources.RANGE_SKIN):
			for p in range(resources.RANGE_FACE):
				for h in range(resources.RANGE_HAIR):
					resources.heads(p,w,h)
					self.run()
		self.txt = 2
		for w in range(resources.RANGE_SKIN):
			for t in range(resources.RANGE_COSTUME):
				resources.bodies(w,t)
				self.run()'''
		self.txt = 3
		resources.battlesprites()
		self.txt = 4
		for j in os.listdir('SFX'): 
			resources.sfx(j)
			self.run()
		self.txt = 5
		for i in range(resources.RANGE_RADIO): 
			resources.radio(i)
			self.run()
		self.txt = 6
		resources.music()
		self.run()
		self.classrun = False

	def run(self):
		if self.load == 1:
			self.callresources()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		'''self.dot += '.'
		if self.dot == '....': self.dot = ''
		self.display.blit(self.monotype.render(database.LOADING[self.txt] + self.dot, True, (240,240,240)), (10, 10))'''
		flp = False
		self.tim += 0.01
		if self.tim >= 1.0: self.tim = 0.0; self.msg += 1; flp = True
		if self.msg >= len(database.MESSAGES): self.msg = 0
		if flp == True: self.display.fill((0,0,0))
		else: self.display.fill((0,0,0),pygame.Rect(1120,720,30,30))
		for i in range(len(database.MESSAGES[self.msg])):
			self.display.blit(self.monotype.render(database.MESSAGES[self.msg][i], True, (240,240,240)), (200, 140 + (i * 20)))
		self.screen.blit(pygame.transform.scale(self.display, (1200, 800)), (0, 0))
		self.gif += 1
		if self.gif >= 8: self.gif = 0
		self.screen.blit(pygame.image.load('Sprites/loading_' + str(self.gif) + '.png'), (1120, 720))
		if flp == True: pygame.display.flip()
		else: pygame.display.update(pygame.Rect(1120,720,30,30))
		if self.load == 0: self.load = 1

class Title:
	def __init__(self):
		self.screen = pygame.display.set_mode(resources.SCREEN_SIZE, pygame.RESIZABLE)
		self.display = pygame.Surface(resources.SURFACE_SIZE)
		self.monotype = pygame.font.Font('Fonts/monotype.ttf', 15)
		self.sfx = pygame.mixer.Channel(0)
		self.ton = pygame.mixer.Channel(1)
		self.msc = pygame.mixer.Channel(2)
		self.msc.play(pygame.mixer.Sound('Music/here_comes_the_death.wav'))
		self.winbar = 210
		self.wait = 100
		self.noise = 0
		self.tv = round(random.randint(1,10))
		self.transtype = 0
		self.transform = 0
		self.transpeed = 0
		self.rectrot = 0
		self.opt = 0
		self.lopt = 0
		self.mnu = 2
		self.glock = pygame.time.Clock()
		self.FPS = 60
		self.scroll = 0
		self.skip = False
		self.classrun = True
		self.loadingif = None

		for i in resources.FILES[0]:
			if resources.FILES[1][i] == 0:
				del resources.FILES[0][i]
				del resources.FILES[1][i]
				del resources.FILES[2][i]
				del resources.FILES[3][i]

		for i in range(40):
			if self.mnu >= 2: break
			self.run()
		while self.winbar > 50:
			self.winbar -= 5
			self.run()

	def random(self):
		self.msc.stop()
		pygame.mixer.music.stop()
		self.ton.play(resources.SOUND['NOISE'],-1)
		self.tv = 0
		self.transform = 0
		self.rectrot = 0
		for i in range(round(random.randint(5,30))): self.run()
		if self.mnu < 6:
			self.ton.stop()
			self.tv = round(random.randint(1,17))
			self.transtype = round(random.randint(0,4))
			spd = round(random.randint(0,3))
			if spd == 0: self.transpeed = -2
			elif spd == 1: self.transpeed = 2
			elif spd == 2: self.transpeed = -1
			else: self.transpeed = 1
			self.wait = round(random.randint(50,100))
			rd = round(random.randint(0,9))
			if len(resources.RADIO[str(rd)]) > 0:
				sng = round(random.randint(0,len(resources.RADIO[str(rd)]) - 1))
				msc = 'Songs/FM_' + str(rd) + '/' + resources.RADIO[str(rd)][sng]
				if msc.endswith('.mp3'):
					audio = MP3(msc)
					pygame.mixer.music.load(msc)
					pygame.mixer.music.play(1,round(random.randint(20,int(audio.info.length) - 20)))
				elif msc.endswith('.wav'):
					audio = pygame.mixer.Sound(msc)
					self.msc.play(audio)
				elif msc.endswith('.ogg'):
					audio = pygame.mixer.Sound(msc)
					self.msc.play(audio)
			if self.transtype in [0,4] and self.transpeed < 0: self.transform = round(random.randint(200,300))
			if self.transtype in [1,4]:
				img = pygame.image.load('Backgrounds/chp_' + str(self.tv) + '.png').convert()
				self.rectrot = img.get_rect(center=pygame.Rect(0,0,600,400).center)

	def run(self):
		#EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if self.mnu == 4 and self.n.ind == 7: self.mnu = 2
			self.pressed = pygame.key.get_pressed()
			if self.pressed[resources.ACT[0]]:
				if self.mnu < 2: self.mnu += 1
				elif self.mnu == 5: self.skip = True
				elif self.winbar == 50:
					if self.lopt < len(resources.FILES[0]):
						if self.mnu < 3: self.mnu += 1
						elif self.mnu == 3: 
							if self.opt == 0:
								self.mnu = 5
								database.load_data()
								self.msc.play(resources.SONGS['FATE_OCCURRENCES'],-1)
							else: del ID[self.lopt]
					else:
						if self.winbar == 50:
							self.sfx.play(resources.SOUND['FILE_NEW'])
							resources.new_data()
							resources.save_data()
							resources.save_sett()
							resources.recent_data(2)
							pygame.mixer.music.fadeout(3000)
							self.msc.fadeout(3000)
							self.ton.fadeout(3000)
							self.mnu = 6

			if self.pressed[resources.RUN[0]]:
				if self.mnu == 3: self.mnu = 2

			if self.pressed[resources.UP[0]] and self.mnu == 2: self.lopt -= 1; self.sfx.play(resources.SOUND['MENU_HOR'])
			if self.pressed[resources.DOWN[0]] and self.mnu == 2: self.lopt += 1; self.sfx.play(resources.SOUND['MENU_VER'])

			if self.pressed[resources.LEFT[0]] and self.mnu == 3: self.opt = 0; self.sfx.play(resources.SOUND['MENU_HOR'])
			if self.pressed[resources.RIGHT[0]] and self.mnu == 3: self.opt = 1; self.sfx.play(resources.SOUND['MENU_VER'])

			if self.lopt < 0: self.lopt = len(resources.FILES[0])
			if self.lopt > len(resources.FILES[0]): self.lopt = 0

		self.display.fill((255, 0, 0))

		#FILES MENU
		if self.mnu != 5:
			if self.tv == 0:
				self.noise += 1
				if self.noise == 3: self.noise = 0
				self.display.blit(pygame.image.load('Backgrounds/noise_' + str(self.noise) + '.png'), (0, 0))
			else:
				self.transform += self.transpeed
				img = pygame.image.load('Backgrounds/chp_' + str(self.tv) + '.png').convert()
				if self.transtype == 0:
					img = pygame.transform.scale(img,(img.get_rect().width + round(self.transform * 2),img.get_rect().height + round(self.transform * 2)))
					self.display.blit(img, (600 - img.get_rect().width, 600 - img.get_rect().height))
				elif self.transtype == 1:
					img = pygame.transform.scale(img,(800,800))
					trs = pygame.transform.rotate(img,self.transform)
					self.rectrot = trs.get_rect(center = self.rectrot.center)
					self.display.blit(trs, self.rectrot)
				elif self.transtype == 2:
					self.display.blit(img, (self.transform, 0))
					if self.transform < 0: self.display.blit(img, (600 + self.transform, 0))
					if self.transform > 0: self.display.blit(img, (-600 + self.transform, 0))
				elif self.transtype == 3:
					self.display.blit(img, (0, self.transform))
					if self.transform < 0: self.display.blit(img, (0, 600 + self.transform))
					if self.transform > 0: self.display.blit(img, (0, -600 + self.transform))
				if self.transtype == 4:
					img = pygame.transform.scale(img,(img.get_rect().width + round(self.transform/6),img.get_rect().height + round(self.transform/4)))
					trs = pygame.transform.rotate(img,self.transform)
					self.rectrot = trs.get_rect(center = self.rectrot.center)
					self.display.blit(trs, self.rectrot)

		if self.mnu < 5:
			for i in range(len(resources.FILES[1])):
				if self.lopt == i: col = (255,255,0)
				else: col = (255,255,255)
				pygame.draw.rect(self.display, col, pygame.Rect(400,100 + (i * 51),180,50))
				self.display.blit(self.monotype.render(database.CHAPTERS[resources.FILES[1][i]][0], True, (0,0,0)), (405, 105 + (i * 51)))

				if self.mnu > 2 and self.lopt == i:
					if self.opt == 0: pygame.draw.rect(self.display, (255,255,255), pygame.Rect(528,113 + (i * 51),24,24))
					if self.opt == 1: pygame.draw.rect(self.display, (255,255,255), pygame.Rect(550,113 + (i * 51),24,24))
					self.display.blit(pygame.image.load('Sprites/tc_7.png'), (530, 115 + (i * 51)))
					self.display.blit(pygame.image.load('Sprites/tc_8.png'), (552, 115 + (i * 51)))
				resources.ID = self.lopt

			if self.lopt == len(resources.FILES[0]): col = (255,255,0)
			else: col = (255,255,255)
			pygame.draw.rect(self.display, col, pygame.Rect(400,100 + (len(resources.FILES[1]) * 51),180,50))
			self.display.blit(self.monotype.render(database.MENU[61], True, (0,0,0)), (405, 105 + (len(resources.FILES[1]) * 51)))

		#RECAP
		if self.mnu == 5:
			lt = 0
			for y in database.CHAPTERS[resources.CHAPTER - 1][2:]:
				self.display.blit(self.monotype.render(y, True, (255,255,255)), (50, 360 - self.scroll + lt))
				lt += 20

			self.scroll += 0.3
			if self.scroll > 340 + lt or self.skip == True:
				if self.winbar == 50: g.rendermap('urban_0'); self.msc.fadeout(5000)
		if self.mnu == 6:
			if self.winbar < 210:
				self.winbar += 5
			if self.winbar == 210:
				self.classrun = False

		#BLACK BARS
		pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
		pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

		#INFO
		if self.mnu > 1 and self.mnu < 5:
			self.display.blit(self.monotype.render(database.ABOUT[0] + ' ' + resources.VERSION, True, (240,240,240)), (-45 + self.winbar, -45 + self.winbar))
			self.display.blit(self.monotype.render(database.ABOUT[1], True, (240,240,240)), (530 - self.winbar, 420 - self.winbar))

		#WAIT
		if self.mnu < 6:
			if self.wait > 0: self.wait -= 1
			prb = round(random.randint(0,100))
			if prb > 50 and self.wait == 0 and self.tv > 0: self.random()

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
		self.controlkeys = pygame.font.Font('Fonts/controlkeys.ttf', 15)
		self.cam = pygame.Rect(0,0,self.displayzw,self.displayzh)
		self.driving = 0
		self.sleepin = False
		self.tilemation = 0
		self.room = ''
		self.rectdebug = False
		self.classrun = True

		hm = resources.TIME[0] + 10
		if hm > 24: hm -= 24
		self.waitime = [['advice',hm,0],['rain',resources.TIME[0],resources.TIME[1] + 5]]#,['cal923778988',resources.TIME[0],resources.TIME[1] + 6]]

		#MIXER CHANNELS
		pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12)
		self.ch_sfx = pygame.mixer.Channel(0) #for quick sounds
		self.ch_sfx.set_volume(resources.SFX)
		self.ch_msc = pygame.mixer.Channel(1) #for background ambience loops
		self.ch_msc.set_volume(resources.MSC)
		self.ch_ton = pygame.mixer.Channel(2) #for long sounds or jingles
		self.ch_ton.set_volume(resources.SFX)
		self.ch_rad = pygame.mixer.Channel(3) #for radio songs
		self.ch_rad.set_volume(0.1)
		self.ch_stp = pygame.mixer.Channel(4) #for steps sounds
		self.ch_stp.set_volume(resources.SFX)
		self.ch_rng = pygame.mixer.Channel(5) #for phone ringtone
		self.ch_rng.set_volume(resources.MSC)
		self.ch_dlg = pygame.mixer.Channel(6) #for dialog text sound
		self.ch_dlg.set_volume(resources.SFX)

		#BATTLE VARIABLES
		self.dlg = []
		self.dlgfa = 500
		self.dlgy = 0
		self.dmginfo = ''
		self.dmgy = 200
		self.dlgspd = resources.SPEED
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
		for i in resources.PARTY[resources.FORMATION]:
			resources.CHARACTERS[i]['HP'] = resources.CHARACTERS[i]['VITALITY'][resources.CHARACTERS[i]['LEVEL']]
			resources.CHARACTERS[i]['BARHP'] = resources.CHARACTERS[i]['VITALITY'][resources.CHARACTERS[i]['LEVEL']]
			self.equip.append(0)
			self.barpp.append([])
			self.barhp.append(int(100/(resources.CHARACTERS[i]['VITALITY'][resources.CHARACTERS[i]['LEVEL']]/resources.CHARACTERS[i]['HP'])))
			self.barhpl.append(100)
			if resources.CHARACTERS[i]['XP'] > 0: self.barxp.append(int(100/(resources.CHARACTERS[i]['NEXTLEVEL'][resources.CHARACTERS[i]['LEVEL']]/resources.CHARACTERS[i]['XP'])))
			else: self.barxp.append(0)
			for j in database.INVENTORY[resources.PARTY[resources.FORMATION][x]][4][1:]:
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
		self.dmenu = None
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
		self.tutorial = {'TEXT': [], 'OUTPUT': [], 'FADE': 0, 'TIME': 0, 'WAIT': 0, 'NEXT': '','GO': 0}
		self.cityname = ''

		#MAP VARIABLES
		self.player = []
		for i in range(1): self.player.append({'RECT': pygame.Rect(resources.PX,resources.PY,20,20),'SPD': 0,'JUMP': 0,'GRAVITY': -5,'STEP': 10,'SWIM': None,'HEAD': 'BLANKD_0114',
		'SPRITE': 'STANDD_' + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['COSTUME'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN'],'GIF': 0.0,
		'BLINK': 100,'DIRECTION': 3, 'PAUSE': 0,'FOLLOW': None,'FOLLEND': 0,'FOLLMOV': '','GRID': [0,0],'PLAYING': False,'NODES': [],'HOLD': None})
		self.player[0]['PLAYING'] = True
		self.objects = []
		self.tilrect = []
		self.tilhide = False
		self.tilalpha = 0
		self.en = []
		self.foe = []
		self.fig = []
		self.mrc = []
		self.npcs = []
		self.vehicles = []
		self.portals = []
		self.signs = []
		self.lights = []
		self.particles = []
		self.portalgo = {}

		#STARTING GAME
		if resources.CHAPTER == 0 and resources.SCENE == 0:
			self.tutorial = {'TEXT': database.TUTORIALS['BEGIN'], 'OUTPUT': [], 'FADE': 0, 'TIME': 0, 'WAIT': 300, 'NEXT': '','GO': 0}
			for j in self.tutorial['TEXT']:
				if isinstance(j,list):
					if j[0] == 'phone':
						self.tutorial['GO'] = j[1]
					if j[0] == 'wait':
						self.tutorial['WAIT'] = j[1]
						if len(j) > 2: self.tutorial['NEXT'] = j[2]
				else: self.tutorial['OUTPUT'].append(j)
			self.player[0]['PAUSE'] = 1
			self.rendermap('hauntedhouse_0')
			self.phone = 15
			self.mnu = 1

	def people(self, i, t):
		#ANIMATION
		if i['PAUSE'] < 2: i['GIF'] += 0.5
		if i['GIF'] >= len(resources.SPRITES[i['SPRITE']]): i['GIF'] = 0
		if i['PAUSE'] < 2: i['BLINK'] -= 1
		if i['BLINK'] < 0: i['BLINK'] = round(random.randint(30,90))

		#JUMP
		if i['GRAVITY'] > -5:
			i['JUMP'] += i['GRAVITY']
			i['GRAVITY'] -= 0.5
		if self.sleepin == False and self.portalgo == {}:
			#MAP ICON
			if resources.MAP == 0:
				self.display.blit(pygame.image.load('Sprites/mp_player.png'), (i['RECT'].x - self.cam.x, i['RECT'].y - self.cam.y))
			else:
				xsp = 0
				#BODY AND SHADE
				if i['SWIM'] == None:
					if i['SPRITE'].startswith('SEAT') == False or i['SPRITE'].startswith('DRIVE') == False:
						self.display.blit(pygame.image.load('Sprites/Items/it_shade.png'), (i['RECT'].x - self.cam.x - 1,i['RECT'].y - self.cam.y + 7))
					img = resources.SPRITES[i['SPRITE']][math.floor(i['GIF'])]
					self.display.blit(img, (i['RECT'].x - self.cam.x + math.floor((20 - img.get_rect().width)/2),i['RECT'].y - self.cam.y - 10 - i['JUMP']))
				#SWIMMING
				else:
					xsp += 21
					i['SWIM'] += 0.1
					if i['SWIM'] > 1.5: i['SWIM'] = 0.0
					self.display.blit(pygame.image.load('Sprites/water_' + str(math.floor(i['SWIM'])) + '.png'), (i['RECT'].x - self.cam.x + 4,i['RECT'].y - self.cam.y + 9))
				#HOLDING ITEM
				if i['HOLD'] != None:
					xx = -5; yy = -20
					if i['DIRECTION'] in [1,2,8]: xx = 10
					if i['DIRECTION'] in [4,5,6]: xx = -20
					if i['DIRECTION'] in [2,3,4]: yy = 5
					if i['DIRECTION'] in [6,7,8]: yy = -30
					self.tilrect[2][i['HOLD']][1].x = i['RECT'].x + xx
					self.tilrect[2][i['HOLD']][1].y = i['RECT'].y + yy
				#EXTRA SPACEMENT
				if i['SPD'] == 0 and i['GIF'] >= 1.0 and i['GIF'] < 3.0: xsp += 1
				if i['SPD'] > 0:
					if i['GIF'] >= 0.0 and i['GIF'] < 1.0: pass
					elif i['GIF'] >= 4.0 and i['GIF'] < 5.0: pass
					else: xsp += 1
				if i['JUMP'] > 0: xsp = 1
				if i['HEAD'].startswith('BLANKDD'): xsp += 1

				#HEAD
				if i['BLINK'] < 2 and i['DIRECTION'] < 6 and i['GRAVITY'] == -5 and i['JUMP'] == 0:
					try: img = resources.SPRITES[i['HEAD']][1]
					except: img = resources.SPRITES[i['HEAD']][0]
				else: img = resources.SPRITES[i['HEAD']][0]
				self.display.blit(img, (i['RECT'].x - self.cam.x + math.floor((20 - img.get_rect().width)/2),i['RECT'].y - self.cam.y - 21 + xsp - i['JUMP']))

				#ACCESORIES
				if t == True and resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['ACCESORIES'] != None and int(i['DIRECTION']) < 6:
					if i['DIRECTION'] == 1: ex = 8
					elif i['DIRECTION'] == 2: ex = 3
					elif i['DIRECTION'] == 3: ex = 2
					elif i['DIRECTION'] == 4: ex = 1
					elif i['DIRECTION'] == 5: ex = 1
					else: ex = 0

					if i['DIRECTION'] == 1: acc = pygame.transform.flip(pygame.image.load('Sprites/Characters/' + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['ACCESORIES'] + '_1.png'),True,False)
					elif i['DIRECTION'] == 5: acc = pygame.image.load('Sprites/Characters/' + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['ACCESORIES'] + '_1.png')
					else: acc = pygame.image.load('Sprites/Characters/' + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['ACCESORIES'] + '_0.png')
					self.display.blit(acc, (i['RECT'].x - self.cam.x + math.floor((20 - img.get_rect().width)/2) + ex,i['RECT'].y - self.cam.y - 21 + xsp - i['JUMP'] + 7))

	def enemy(self, en):
		#DRAW
		if self.battle == False and self.colide(self.en[en]['RECT'], self.cam):
			if self.rectdebug == True: pygame.draw.rect(self.display, (255,0,0), pygame.Rect(self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y, self.en[en]['RECT'].width, self.en[en]['RECT'].height))
			self.display.blit(pygame.image.load('Sprites/frk_' + (self.en[en]['FILE']) + '_mini.png'), (self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y))
			if self.en[en]['PATH'] == 'notice': self.display.blit(pygame.image.load('Sprites/notice.png'), (self.en[en]['RECT'].x - self.cam.x, self.en[en]['RECT'].y - self.cam.y - 30))

		#MOVEMENT
		if self.colide(self.en[en]['RECT'], self.cam) and self.winbar == 0 and self.battle == False and self.en[en]['FIGHTING'] == False:
			if self.en[en]['PATH'] == 'stealth':
				if self.facing(self.en[en],self.player[0]) == 2:
					self.ch_sfx.play(resources.SOUND['NOTICED'])
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
				if self.en[en]['RECT'].y - self.cam.y > self.player[0]['RECT'].y - 5 - self.cam.y:
					if self.en[en]['RECT'].x - self.cam.x < self.player[0]['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 8
					elif self.en[en]['RECT'].x - self.cam.x > self.player[0]['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 6
					else: self.en[en]['DIRECTION'] = 7

				elif self.en[en]['RECT'].y - self.cam.y < self.player[0]['RECT'].y - 5 - self.cam.y: 
					if self.en[en]['RECT'].x - self.cam.x < self.player[0]['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 2
					elif self.en[en]['RECT'].x - self.cam.x > self.player[0]['RECT'].x + 10 - self.cam.x: self.en[en]['DIRECTION'] = 4
					else: self.en[en]['DIRECTION'] = 3

				elif self.en[en]['RECT'].x - self.cam.x < self.player[0]['RECT'].x + 10 - self.cam.x:
					if self.en[en]['RECT'].y - self.cam.y > self.player[0]['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 8
					elif self.en[en]['RECT'].y - self.cam.y < self.player[0]['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 2
					else: self.en[en]['DIRECTION'] = 1

				elif self.en[en]['RECT'].x - self.cam.x > self.player[0]['RECT'].x + 10 - self.cam.x:
					if self.en[en]['RECT'].y - self.cam.y > self.player[0]['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 6
					elif self.en[en]['RECT'].y - self.cam.y < self.player[0]['RECT'].y - 5 - self.cam.y: self.en[en]['DIRECTION'] = 4
					else: self.en[en]['DIRECTION'] = 5

			elif self.en[en]['PATH'] == 'horizontal':
				if self.en[en]['DIRECTION'] == 0:
					self.en[en]['DIRECTION'] = 1

				if self.en[en]['TIME'] == 0:
					if self.en[en]['DIRECTION'] == 1: self.en[en]['DIRECTION'] = 5
					elif self.en[en]['DIRECTION'] == 5: self.en[en]['DIRECTION'] = 1
					self.en[en]['TIME'] = 20

			if self.player[0]['PAUSE'] < 3:
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
		if self.colide(self.en[en]['RECT'], self.player[0]['RECT']) == True and self.en[en]['DIRECTION'] > 0 and self.battle == False and self.dlgfa == 500:
			if self.en[en]['FIGHTING'] == False:
				if self.en[en]['TYPE'] != 'mercenary': self.foe.append(self.en[en])
				else: self.mrc.append(self.en[en])
				self.en[en]['FIGHTING'] = True
				if len(self.foe) == 1:
					self.turn = -self.facing(self.en[en],self.player[0])
					print(self.turn)
					self.fight()

	def npc(self, i):
		if i['RECT'].width > 0: rect = pygame.Rect(i['RECT'].x,i['RECT'].y,i['RECT'].width,i['RECT'].height)
		else: rect = pygame.Rect(i['RECT'].x,i['RECT'].y,20,20)

		#DRAW
		if self.rectdebug == True: pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False and self.colide(rect, self.cam):
			if i['TYPE'] in [0,2] and i['RECT'].width == 0: self.people(i,False)
			elif i['TYPE'] == 3:
				img = pygame.image.load('Sprites/mercator.png')
				self.display.blit(img, (rect.x - self.cam.x - math.floor(img.get_rect().width/2) + 10, rect.y - self.cam.y - int(img.get_rect().height/2) - 3))
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

		if self.colide(i['RECT'], self.cam) and self.battle == False and i['TYPE'] == 0 and i['RECT'].width == 0 and i['FOLLOW'] == None:
			if i['MOVE'] == 'horizontal':
				i['SPD'] = 1
				if i['DIRECTION'] not in [1,5]:
					i['DIRECTION'] = 1

				if i['TIME'] == 0:
					if i['DIRECTION'] == 1: i['DIRECTION'] = 5
					elif i['DIRECTION'] == 5: i['DIRECTION'] = 1
					i['TIME'] = 30
				i['TIME'] -= 1
			elif i['MOVE'] == 'fixed': i['SPD'] = 0

		if self.player[0]['PAUSE'] < 3:
			if i['SPD'] > 0:
				if i['DIRECTION'] == 1: i['HEAD'] = 'BLANKR_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKR_' + i['INDEX'][3:6]; i['RECT'].x += i['SPD']
				if i['DIRECTION'] == 2: i['HEAD'] = 'BLANKRD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKRD_' + i['INDEX'][3:6]; i['RECT'].x += i['SPD']; i['RECT'].y += i['SPD']
				if i['DIRECTION'] == 3: i['HEAD'] = 'BLANKD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKD_' + i['INDEX'][3:6]; i['RECT'].y += i['SPD']
				if i['DIRECTION'] == 4: i['HEAD'] = 'BLANKLD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKLD_' + i['INDEX'][3:6]; i['RECT'].x -= i['SPD']; i['RECT'].y += i['SPD']
				if i['DIRECTION'] == 5: i['HEAD'] = 'BLANKL_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKL_' + i['INDEX'][3:6]; i['RECT'].x -= i['SPD']
				if i['DIRECTION'] == 6: i['HEAD'] = 'BLANKLU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKLU_' + i['INDEX'][3:6]; i['RECT'].x -= i['SPD']; i['RECT'].y -= i['SPD']
				if i['DIRECTION'] == 7: i['HEAD'] = 'BLANKU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKU_' + i['INDEX'][3:6]; i['RECT'].y -= i['SPD']
				if i['DIRECTION'] == 8: i['HEAD'] = 'BLANKRU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'WALKRU_' + i['INDEX'][3:6]; i['RECT'].x += i['SPD']; i['RECT'].y -= i['SPD']
			elif i['MOVE'] == 'stand':
				if i['DIRECTION'] == 1: i['HEAD'] = 'BLANKR_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDR_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 2: i['HEAD'] = 'BLANKRD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDRD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 3: i['HEAD'] = 'BLANKD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 4: i['HEAD'] = 'BLANKLD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDLD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 5: i['HEAD'] = 'BLANKL_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDL_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 6: i['HEAD'] = 'BLANKLU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDLU_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 7: i['HEAD'] = 'BLANKU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDU_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 8: i['HEAD'] = 'BLANKRU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'STANDRU_' + i['INDEX'][3:6]
				i['MOVE'] = 'fixed'
			elif i['MOVE'] == 'seat':
				if i['DIRECTION'] == 1: i['HEAD'] = 'BLANKR_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATR_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 2: i['HEAD'] = 'BLANKRD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATRD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 3: i['HEAD'] = 'BLANKD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 4: i['HEAD'] = 'BLANKLD_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATLD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 5: i['HEAD'] = 'BLANKL_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATL_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 6: i['HEAD'] = 'BLANKLU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATLU_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 7: i['HEAD'] = 'BLANKU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATU_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 8: i['HEAD'] = 'BLANKRU_' + i['INDEX'][0:3] + i['INDEX'][5]; i['SPRITE'] = 'SEATRU_' + i['INDEX'][3:6]
			else:
				if i['DIRECTION'] == 1: i['SPRITE'] = 'STANDR_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 2: i['SPRITE'] = 'STANDRD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 3: i['SPRITE'] = 'STANDD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 4: i['SPRITE'] = 'STANDLD_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 5: i['SPRITE'] = 'STANDL_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 6: i['SPRITE'] = 'STANDLU_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 7: i['SPRITE'] = 'STANDU_' + i['INDEX'][3:6]
				if i['DIRECTION'] == 8: i['SPRITE'] = 'STANDRU_' + i['INDEX'][3:6]

			if i['FOLLOW'] != None:
				if i['FOLLOW'] != (None,None):
					if self.colide(rect,i['FOLLOW']):
						if i['FOLLMOV'] != '': i['MOVE'] = i['FOLLMOV']
						i['DIRECTION'] = i['FOLLEND']
						i['FOLLOW'] = None
						i['FOLLEND'] = 0
						i['FOLLMOV'] = ''
						i['SPD'] = 0
				else:
					if i['FOLLMOV'] != '': i['MOVE'] = i['FOLLMOV']
					i['DIRECTION'] = i['FOLLEND']
					i['FOLLOW'] = None
					i['FOLLEND'] = 0
					i['FOLLMOV'] = ''
					i['SPD'] = 0

		#ACTIONS
		if self.colide(self.player[0]['RECT'], rect) == True:
			if i['TALKING'] == False:
				if self.battle == False and self.speakin != rect and self.dlgfa > 0 and isinstance(i['TYPE'],str) == False:
					self.display.blit(pygame.image.load('Sprites/arw.png'), (rect.x - self.cam.x + int(rect.width/2) - 5, rect.y - self.cam.y - rect.height * 2))
				if isinstance(i['TYPE'],str) and i['TYPE'].startswith('scene'):
					if resources.SCENE == int(i['TYPE'][5]) - 1:
						resources.SCENE = int(i['TYPE'][5])
						act = True
					else: act = False
				else:
					act = False
					self.pressed = pygame.key.get_pressed()
					if self.pressed[resources.ACT[0]]:
						self.player[0]['PAUSE'] = 1
						act = True
				if act == True:
					i['TALKING'] = True
					#NPC DIALOG
					if i['TYPE'] in [0,None] or i['TYPE'].startswith('scene'):
						if self.dlgfa > 0:
							i['SPD'] = 0
							if i['DIRECTION'] == 1: i['HEAD'] = 'TALKR_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['DIRECTION'] == 2: i['HEAD'] = 'TALKRD_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['DIRECTION'] == 3: i['HEAD'] = 'TALKD_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['DIRECTION'] == 4: i['HEAD'] = 'TALKLD_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['DIRECTION'] == 5: i['HEAD'] = 'TALKL_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['DIRECTION'] == 6: i['HEAD'] = 'TALKLU_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['DIRECTION'] == 7: i['HEAD'] = 'TALKU_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['DIRECTION'] == 8: i['HEAD'] = 'TALKRU_' + i['INDEX'][0:3] + i['INDEX'][5]
							if i['WHO'] != 'REWARD':
								if isinstance(i['WHO'], int): self.dialog(database.DIALOGS['NPC_'+str(i['WHO'])][resources.DLGSAV[i['WHO']]].copy(),rect)
								else: self.dialog(database.DIALOGS[i['WHO']][resources.DLGSAV[i['WHO']]].copy(),rect)
							else:
								if self.greenblood > 700: self.dialog(database.DIALOGS['REWARD'][3].copy(),rect)
								elif self.greenblood > 300: self.dialog(database.DIALOGS['REWARD'][2].copy(),rect)
								elif self.greenblood > 0: self.dialog(database.DIALOGS['REWARD'][1].copy(),rect)
								else: self.dialog(database.DIALOGS['REWARD'][0].copy(),rect)

								if self.notx == 0 and self.greenblood > 0:
									resources.MONEY += self.greenblood
									self.ch_sfx.play(resources.SOUND['CASH_GET'])
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
						self.ch_sfx.play(resources.SOUND['INVENTORY_OPEN'])
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
							if self.sleepin == False: self.player[0]['PAUSE'] = 1
							else: self.player[0]['PAUSE'] = 0
						#TRASH CAN
						elif i['INDEX'] == 2:
							self.inventory = 3
							self.ch_sfx.play(resources.SOUND['INVENTORY_OPEN'])
							self.invfade = 0
							self.opt = 0
							self.lopt = 1
							self.mnu = 0
						#PHONE
						elif i['INDEX'] == 3:
							if resources.MONEY > 0:
								resources.MONEY -= 1
								database.CALLHIST.insert(0,[database.CONTACTS[self.lopt][1],False])
								self.dialog(database.DIALOGS[database.CONTACTS[self.lopt][1]][0],rect)
							else:
								self.dialog([database.MENU[18]],rect)
						#BATTERY PLUG
						elif i['INDEX'] == 4:
							print('here')
							if self.inv.find(0,'charger') != None: self.ch_sfx.play(resources.SOUND['MENU_GO']); resources.BATTERY = 360
							else: self.ch_sfx.play(resources.SOUND['MENU_GO']); self.dialog(database.DIALOGS['PLUG'])
						#REFUEL
						elif i['INDEX'] == 5 and self.driving > 0:
							while resources.GAS < self.vehicles[self.driving - 1]['CAPACITY']:
								resources.GAS += 1
								self.run()

					#PRODUCTS AND MERCATOR
					else:
						if i['TYPE'] == 3:
							self.dialog(database.DIALOGS['MERCATOR'][0],rect)
							self.basket = []
							j = 0
							x = 0
							for p in range(len(database.INVENTORY)):
								if p in resources.PARTY[resources.FORMATION]:
									for t in database.INVENTORY[p]:
										for k in t:
											if k[0] != '_' and database.ITEMS[database.INVENTORY[p][j][x][0]][2] != 0:
												self.basket.append([p,j,x])
											x += 1
										x = 0
										j += 1
								x = 0
								j = 0
						if resources.DATE[3] == database.PRODUCTS[int(i['INDEX'])][1]:
							self.promo = database.PRODUCTS[int(i['INDEX'])][2]
						self.products = []
						for p in database.PRODUCTS[int(i['INDEX'])][0]:
							self.products.append(p)
						self.shp = True
						self.lopt = 0
						self.opt = 0
						self.mnu = i['WHO']
		else: i['TALKING'] = False

	def vehicle(self, i):
		rect = pygame.Rect(i['RECT'].x - 5,i['RECT'].y - 5,60,30)
		if self.driving == i['INDEX'] + 1:
			i['RECT'].x = self.player[0]['RECT'].x
			i['RECT'].y = self.player[0]['RECT'].y

		if self.rectdebug == True: pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False and self.colide(rect, self.cam):
			self.display.blit(pygame.image.load('Sprites/moto_' + str(i['INDEX']) + '_walkL.png'), (rect.x - self.cam.x + 10, rect.y + rect.height - self.cam.y - 30))

		if self.colide(self.player[0]['RECT'], rect) == True:
			for event in pygame.event.get():
				if self.pressed[resources.ACT[0]] and self.driving == 0:
					trigger = True
					self.driving = i['INDEX'] + 1
					'''self.displayzw = 1200
					self.displayzh = 800
					self.display = pygame.Surface((1200, 800))
					self.cam = pygame.Rect(0,0,self.displayzw,self.displayzh)'''
			if self.battle == False: self.display.blit(pygame.image.load('Sprites/arw.png'), (rect.x - self.cam.x + int(rect.width/2) - 5, rect.y - self.cam.y - int(rect.height/2)))

	def portal(self, i):
		if i['RECT'].width > 0: rect = pygame.Rect(i['RECT'].x,i['RECT'].y,i['RECT'].width,i['RECT'].height)
		else: rect = pygame.Rect(i['RECT'].x,i['RECT'].y,30,30)
		goto = False

		if self.rectdebug == True: pygame.draw.rect(self.display, (255,0,0), pygame.Rect(rect.x - self.cam.x, rect.y - self.cam.y, rect.width, rect.height))
		if self.battle == False and self.colide(rect, self.cam):
			if self.colide(self.player[0]['RECT'], rect) == True and self.winbar > 0: spr = '1'
			else: spr = '0'
			if resources.MAP > 0:
				if i['RECT'].width == 24: self.display.blit(pygame.image.load('Sprites/door_0' + spr + '.png'), (rect.x - self.cam.x, rect.y - self.cam.y))
				if i['RECT'].width == 48: self.display.blit(pygame.image.load('Sprites/door_1' + spr + '.png'), (rect.x - self.cam.x, rect.y - self.cam.y))
			else: self.display.blit(pygame.image.load('Sprites/mp_player.png'), (rect.x - self.cam.x, rect.y - self.cam.y))

		if self.colide(self.player[0]['RECT'], rect) == True and self.winbar == 0:
			if i['OPENING'] == 'key':
				fnd = self.inv.find(0,'key_bedroom')
				if fnd != None and fnd[1] == i['CLOSURE']: goto = True
				else: goto = False

			elif i['OPENING'] != None:
				if resources.TIME[0] > i['OPENING'][0] and resources.TIME[0] < i['CLOSURE'][0]: goto = True
				elif resources.TIME[0] == i['OPENING'][0]:
					if resources.TIME[1] > i['OPENING'][1]: goto = True
				elif resources.TIME[0] == i['CLOSURE'][0]:
					if resources.TIME[1] < i['CLOSURE'][1]: goto = True
			else: goto = True

		if goto == True:
			for p in self.player:
				p['PAUSE'] = 1
				p['SPD'] = 0
			if i['TYPE'] > 0:
				self.ch_ton.play(resources.SOUND['DOOR_OPEN'])
				#self.portalgo = [{'POS' : [self.player[0]['RECT'].x - self.cam.x,self.player[0]['RECT'].y - self.cam.y], 'SPRITE': self.player[0]['SPRITE']
				#'HEAD': self.player[0]['HEAD'], 'FOL': [self.player[0]['RECT'].x - self.cam.x,self.player[0]['RECT'].y - self.cam.y]}]
				self.portalgo = [{'RECT' : i['RECT']}]
			if i['MUSIC'] not in ['inside','outside',None]:
				self.ch_msc.fadeout(1000)
				spd = 5
			else: spd = 10
			self.transiction(True, 210, spd)
			self.rendermap(i['MAP'])
			for p in self.player:
				p['RECT'].x = i['PX']
				p['RECT'].y = i['PY']
			if i['TYPE'] > 0:
				self.ch_ton.play(resources.SOUND['DOOR_CLOSE'])
			if i['MUSIC'] == 'outside': self.ch_msc.set_volume(1.0)
			elif i['MUSIC'] == 'inside': self.ch_msc.set_volume(0.2)
			elif i['MUSIC'] != None: self.ch_msc.play(resources.SOUND[i['MUSIC'].upper()],-1)
			if self.cityname == '':
				self.transiction(False, 0, spd)
			else:
				self.transiction(False, 50, 5)
				for i in range(100): self.run()
				self.transiction(False, 0, 5)
				self.cityname = ''
			self.portalgo = {}
			for p in self.player: p['PAUSE'] = 0

	def colide(self, i1, i2):
		cld = False
		if isinstance(i2, list):
			ind = 0
			for i in i2[2]:
				if self.facing(i1,i[1]) == 2:
					cld = pygame.Rect.colliderect(i1['RECT'],i[1])
					if cld == True and i1['JUMP'] == 0:
						if i[0] == 'HOLD':
							self.display.blit(pygame.image.load('Sprites/arw.png'), (i[1].x - self.cam.x + int(i[1].width/2) - 5, i[1].y - self.cam.y - i[1].height))
							self.pressed = pygame.key.get_pressed()
							if self.pressed[resources.ACT[0]] and self.player[0]['HOLD'] == None:
								self.player[0]['HOLD'] = ind
							cld = False
						elif i[0] == 'CARRY':
							if i1['DIRECTION'] in [1,2]: i[1].x += i1['SPD']
							if i1['DIRECTION'] in [3,4]: i[1].y += i1['SPD']
							if i1['DIRECTION'] in [5,6]: i[1].x -= i1['SPD']
							if i1['DIRECTION'] in [7,8]: i[1].y -= i1['SPD']
						break
				ind += 1
			if cld == False:
				for i in i2[3]:
					if self.facing(i1,i[1]) == 2:
						cld = pygame.Rect.colliderect(i1['RECT'],i[1])
						if cld == True and i1['JUMP'] == 0: break
			if cld == False:
				for i in i2[4]:
					if self.facing(i1,i[1]) == 2:
						if pygame.Rect.colliderect(i1['RECT'],i[1]) and i1['JUMP'] == 0:
							if i[0].endswith('ON') and self.tilhide == False: self.tilhide = True
							if i[0].endswith('OFF') and self.tilhide == True: self.tilhide = False
							break
		else:
			cld = pygame.Rect.colliderect(i1,i2)

		return cld

	def facing(self, i1, i2):
		if isinstance(i2, dict) == False: i2 = {'RECT': i2, 'DIRECTION': self.player[0]['DIRECTION']}
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
		for event in pygame.event.get():
			self.pressed = pygame.key.get_pressed()
			#EXIT GAME
			if event.type == pygame.QUIT:
				resources.recent_data(1,resources.ID)
				pygame.quit()
				sys.exit()
			#RESIZE
			if event.type == pygame.VIDEORESIZE:
				self.windowh = event.h
				sh = int(event.h/4)
				self.windoww = 6 * sh
				self.screen = pygame.display.set_mode((self.windoww, self.windowh), pygame.RESIZABLE)
				self.FPS = int(event.w/20)

			#DEBUG
			if self.pressed[pygame.K_INSERT]:
				self.dmenu = menu.Debug()
				while self.dmenu.classrun:
					self.dmenu.run()
					self.screen.fill((0,0,0),pygame.Rect(1120,720,30,30))
					self.screen.blit(self.dmenu.draw(), (0, 0))
					pygame.display.update(pygame.Rect(0,0,1200,50))
				self.dmenu.command()
				if self.dmenu.dlg != []:
					self.dialog(self.dmenu.dlg)
					self.dmenu.dlg = []
				if self.dmenu.goto != '':
					self.__init__()
					self.rendermap(self.dmenu.goto)
					self.transiction(False,0)
				self.dmenu = None

			#BATTLE OPTIONS
			if self.battle == True and self.phone == 0:
				self.pressed = pygame.key.get_pressed()
				if self.turn == len(resources.PARTY[resources.FORMATION]): self.fight()

				if self.mnu == 2:
					if self.equip[self.turn] == 4:
						if self.pressed[resources.LEFT[0]]: self.opt -= 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.pressed[resources.RIGHT[0]]: self.opt += 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])


					if self.pressed[resources.ACT[0]]:
						if self.equip[self.turn] < 4:
							self.fight()
							self.turn += 1
							self.mnu = 1
							if self.turn == len(resources.PARTY[resources.FORMATION]): self.fight()
						elif self.equip[self.turn] == 4:
							ttl = self.opt
							for i in self.fig:
								self.equip[self.turn] = resources.TACTICAL[ttl][self.turn]
								if self.equip[self.turn] != 0:
									if self.equip[self.turn] + 1 < 5:
										self.equip[self.turn] -= 1
										self.ch_sfx.play(resources.SOUND['GUN_TRIGGER'])
										self.mnu = 2
										self.wait()
									if self.equip[self.turn] != 6: self.fight()
									else:
										self.pres[self.turn] += 3
										self.ch_sfx.play(resources.SOUND['GUARD'])
										self.dialog([self.fig[self.turn]['NAME'] + ' está em guarda'])
								self.turn += 1
							for i in self.equip: i = 4

					if self.opt < 0: self.opt = len(resources.TACTICAL) - 1
					if self.opt > len(resources.TACTICAL) - 1: self.opt = 0

				elif self.mnu == 1:
					if self.pressed[resources.LEFT[0]]: self.equip[self.turn] -=1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: self.equip[self.turn] +=1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
				
					if self.equip[self.turn] < 0: self.equip[self.turn] = 7
					if self.equip[self.turn] > 7: self.equip[self.turn] = 0

					if self.pressed[resources.ACT[0]]:
						if self.equip[self.turn] < 4:
							if int(database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1]) > 0:
								self.ch_sfx.play(resources.SOUND['GUN_TRIGGER'])
								self.mnu = 2
							else:
								self.ch_sfx.play(resources.SOUND['ERROR'])
						elif self.equip[self.turn] == 4:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.mnu = 2
						elif self.equip[self.turn] == 5:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.fight()
							self.turn += 1
						elif self.equip[self.turn] == 6:
							self.ch_ton.play(resources.SOUND['GUARD'])
							self.pres[self.turn] += 3
							self.dialog([self.fig[self.turn]['NAME'] + ' está em guarda'])
							self.turn += 1
							if self.turn == len(self.fig): self.fight()
						elif self.equip[self.turn] == 7:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.fight()
							if self.battle == True:
								self.turn = len(resources.PARTY[resources.FORMATION])
								self.fight()

			#SHOP OPTIONS
			if self.shp == True:
				if self.pressed[resources.LEFT[0]]: self.opt -= 1 ; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
				if self.pressed[resources.RIGHT[0]]: self.opt += 1 ; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
				if self.pressed[resources.UP[0]]: self.lopt -= 1 ; self.ch_sfx.play(resources.SOUND['MENU_VER'])
				if self.pressed[resources.DOWN[0]]: self.lopt += 1 ; self.ch_sfx.play(resources.SOUND['MENU_VER'])

				if self.mnu == 0:
					if self.pressed[resources.ACT[0]]:
						if self.lopt < len(self.products):
							for i in range(self.opt): self.basket.append(self.products[self.lopt])
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
						else:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 10
					if self.opt > 10: self.opt = 1
					if self.lopt < 0: self.lopt = len(self.products)
					if self.lopt > len(self.products): self.lopt = 0

				if self.mnu == 1:
					if self.pressed[resources.ACT[0]]:
						if self.lopt == 0:
							for i in self.basket:
								if resources.MONEY >= database.ITEMS[i][2]:
									if self.inv.space(0) == False:
										self.dialog(database.DIALOGS['MERCATOR'][2])
									elif self.confirmation() == 1:
										self.inv.add(0,i)
										self.ch_sfx.play(resources.SOUND['BUY'])
										resources.MONEY -= database.ITEMS[i][2] - int(database.ITEMS[i][2]/self.promo)
								else:
									self.ch_sfx.play(resources.SOUND['ERROR'])
									self.dialog(database.DIALOGS['MERCATOR'][1])
						else:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							self.shp = False
							self.lopt = 0

					if self.opt < 1: self.opt = 1
					if self.lopt < 0: self.lopt = 1
					if self.lopt > 1: self.lopt = 0

				if self.mnu == 2:
					if self.pressed[resources.ACT[0]]:
						if self.opt == 0:
							if self.lopt == len(self.products):
								self.ch_sfx.play(resources.SOUND['MENU_BACK'])
								self.shp = False
								self.lopt = 0
							else:
								if resources.MONEY >= database.ITEMS[self.products[self.lopt]][2]:
									if self.inv.space(0) == False:
										self.dialog(database.DIALOGS['MERCATOR'][2])
									elif self.confirmation() == 1:
										self.inv.add(0,self.products[self.lopt])
										self.ch_sfx.play(resources.SOUND['BUY'])
										resources.MONEY -= database.ITEMS[self.products[self.lopt]][2] - int(database.ITEMS[self.products[self.lopt]][2]/self.promo)
								else:
									self.ch_sfx.play(resources.SOUND['ERROR'])
									self.dialog(database.DIALOGS['MERCATOR'][1])
						else:
							if self.lopt == len(self.basket):
								self.ch_sfx.play(resources.SOUND['MENU_BACK'])
								self.shp = False
								self.lopt = 0
							elif self.confirmation() == 1:
								resources.MONEY += int(database.ITEMS[database.INVENTORY[self.basket[self.lopt][0]][self.basket[self.lopt][1]][self.basket[self.lopt][2]][0]][2]/2)
								database.INVENTORY[self.basket[self.lopt][0]][self.basket[self.lopt][1]][self.basket[self.lopt][2]] = ['_','0000','_','_']
								del self.basket[self.lopt]
								self.ch_sfx.play(resources.SOUND['SELL'])


					if self.opt < 0: self.opt = len(resources.PARTY[resources.FORMATION])
					if self.opt > len(resources.PARTY[resources.FORMATION]): self.opt = 0
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
					if self.pressed[resources.ACT[0]]:
						self.ch_sfx.play(resources.SOUND['CASH_GET'])
						self.shp = False
						self.opt = 0
						self.lopt = 0

					if self.opt < 0: self.opt = 5
					if self.opt > 5: self.opt = 0
					if self.lopt < 0: self.lopt = 9
					if self.lopt > 9: self.lopt = 0

					if self.pressed[resources.LEFT[0]]: self.lopt = self.extract[self.opt]
					if self.pressed[resources.RIGHT[0]]: self.lopt = self.extract[self.opt]
					
					self.extract[self.opt] = self.lopt

					if self.pressed[resources.UP[0]]:
						if self.mnu == 11:
							resources.ATM -= 1
							resources.MONEY += 1
						if self.mnu == 12:
							resources.ATM += 1
							resources.MONEY -= 1

					if self.pressed[resources.DOWN[0]]:
						if self.mnu == 11:
							resources.ATM += 1
							resources.MONEY -= 1
						if self.mnu == 12:
							resources.ATM -= 1
							resources.MONEY += 1
					'''if self.pressed[resources.UP[0]]:
						if self.mnu == 11:
							resources.ATM -= int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))
							resources.MONEY += int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))
						if self.mnu == 12:
							resources.ATM += int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))
							resources.MONEY -= int(str(self.extract[0]) + str(self.extract[1]) + str(self.extract[2]) + str(self.extract[3]) + str(self.extract[4]) + str(self.extract[5]))'''

				if self.mnu == 3:
					if self.pressed[resources.ACT[0]]:
						if self.lopt == 0:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.mnu = 11
							self.lopt = 0
							self.opt = 5
						if self.lopt == 1:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.mnu = 12
							self.lopt = 0
							self.opt = 5
						if self.lopt == 2:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							self.shp = False
							self.lopt = 0

					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

			#INVENTORY OPTIONS
			if self.pressed[resources.BAG[0]] and self.phone == 0 and self.shp == False and self.inv.itmov == '':
				if self.inventory > 0:
					self.inventory = 0
					self.ch_sfx.play(resources.SOUND['INVENTORY_CLOSE'])
					self.player[0]['PAUSE'] = 0
					if self.battle == True: self.mnu = 1
				elif self.inventory == 0:
					self.inventory = 1
					self.ch_sfx.play(resources.SOUND['INVENTORY_OPEN'])
					self.player[0]['PAUSE'] = 1
					self.invfade = 0
					self.opt = 0
					self.lopt = 1
					self.mnu = 0

			if self.inventory > 0:
				if self.inv.itmov != '':
					if self.inv.itmov[0] == 0:
						if self.pressed[resources.LEFT[0]]:
							if self.exvar > 1: self.exvar -= 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.pressed[resources.RIGHT[0]]:
							if self.exvar < 3: self.exvar += 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					else:
						if self.pressed[resources.LEFT[0]]: self.opt -= 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.pressed[resources.RIGHT[0]]: self.opt += 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
				else:
					if self.pressed[resources.LEFT[0]]: self.opt -= 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: self.opt += 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

				if self.pressed[resources.ACT[0]]:
					if self.inv.itmov == '':
						if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('food') and resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HEALTH'] != 10:
							self.ch_ton.play(resources.SOUND['HEAL'])
							hl = database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0]][5]
							if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][2] != '_': hl += database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][2]][5]
							if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][3] != '_': hl += database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][3]][5]
							if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] in resources.CHARACTERS[self.mnu]['FAVFOOD']:
								hl += int(hl/2)
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['HP'] += hl
							if resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['HP'] > resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL']]:
								resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['HP'] = resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL']]
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('repellent'):
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['HEALTH'] = 2
							wtm = database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0]][5]
							wtm += resources.TIME[1]
							self.waitime.append(['repellent' + str(resources.PARTY[resources.FORMATION][self.mnu]),wtm])
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_strenght':
							self.ch_ton.play(resources.SOUND['ATTRIBUTE_GAIN'])
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_attack':
							self.ch_ton.play(resources.SOUND['ATTRIBUTE_GAIN'])
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_agility':
							self.ch_ton.play(resources.SOUND['ATTRIBUTE_GAIN'])
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_resistance':
							self.ch_ton.play(resources.SOUND['ATTRIBUTE_GAIN'])
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_vitality':
							self.ch_ton.play(resources.SOUND['ATTRIBUTE_GAIN'])
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'pill_mistery':
							self.ch_ton.play(resources.SOUND['ATTRIBUTE_GAIN'])
							resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['LEVEL'] += 1
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('locksmith'):
							self.ch_ton.play(resources.SOUND['MENU_GO'])
							self.inv.itmov = [0,database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][2],database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][3]]
							self.exvar = 1

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == 'wallet':
							self.ch_ton.play(resources.SOUND['MENU_GO'])
							self.inv.itmov = [0,database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][2],database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][3]]
							self.inv.money = True
							self.exvar = 1

						else: self.ch_ton.play(resources.SOUND['ERROR'])

						if self.battle == True:
							self.turn += 1
							self.mnu = 1
							self.inventory = 0

					elif self.inv.itmov[0] == 0:
						if self.exvar == 3:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.inv.itmov = ''
							self.inv.money = False
						else: self.ch_ton.play(resources.SOUND['ERROR'])

					elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_':
						craft = False
						if self.inv.itmov[0].startswith('key') and database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('locksmith'): craft = True
						if self.inv.itmov[0].startswith('id_card') and database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('wallet'): craft = True
						if self.inv.itmov[0].startswith('credit_card') and database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('wallet'): craft = True
						elif self.inv.itmov[0].startswith('condiment') and database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('food'): craft = True
						elif self.inv.itmov[0].startswith('acc') and database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('gun'): craft = True

						if craft == True:
							if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][2] == '_':
								self.ch_ton.play(resources.SOUND['CRAFT'])
								database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][2] = self.inv.itmov[0]
								database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1] = self.inv.itmov[1] + database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1]
								self.inv.itmov = ''
							elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][3] == '_':
								self.ch_ton.play(resources.SOUND['CRAFT'])
								database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][3] = self.inv.itmov[0]
								database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1] += self.inv.itmov[1]
								self.inv.itmov = ''
							else: self.ch_ton.play(resources.SOUND['ERROR']); self.shake = 5

						elif self.inv.itmov[0].startswith('ammo') and database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0].startswith('gun'):
							self.ch_ton.play(resources.SOUND['GUN_RECHARGE'])
							if int(database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][4][self.equip[self.mnu] + 1][1]) > 0:
								plus = int(100/(database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][4][self.equip[self.mnu] + 1][0]][5]['CAPACITY']/int(database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][4][self.equip[self.mnu] + 1][1])))
							else: plus = 0
							while self.barpp[self.mnu][self.equip[self.mnu]] < plus:
								self.barpp[self.mnu][self.equip[self.mnu]] += 1
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1] = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1]
							self.inv.itmov = ''

						else: self.ch_ton.play(resources.SOUND['ERROR']); self.inv.shake = 5

						if self.battle == True:
							self.turn += 1
							self.mnu = 1
							self.inventory = 0

				if self.pressed[resources.RUN[0]]:
					if self.inventory == 1:
						if self.inv.itmov != '':
							if self.inv.itmov[0] == 0:
								if self.exvar < 3 and self.inv.itmov[self.exvar] != '_':
									self.ch_sfx.play(resources.SOUND['MENU_GO'])
									itm = self.inv.itmov[self.exvar]
									database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][self.exvar + 1] = '_'
									if self.exvar == 1:
										prp = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1][0:4]
										database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1] = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1][4:8]
									if self.exvar == 2:
										if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][2] == '_':
											prp = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1][0:4]
											database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1] = ''
										else:
											prp = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1][4:8]
											database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1] = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][1][0:4]
									self.inv.itmov = [itm,prp,'_','_']
									self.inv.money = False
								else: self.ch_sfx.play(resources.SOUND['ERROR']); self.inv.shake = 5

							elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == '_' and self.inv.space(resources.PARTY[resources.FORMATION][self.mnu],self.exvar,self.opt,self.lopt) == True:
								self.ch_sfx.play(resources.SOUND['EQUIP'])
								database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
								if self.inv.itmov[0].startswith('clth'):
									resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['COSTUME'] = database.ITEMS[self.inv.itmov[0]][5]
								if self.inv.itmov[0].startswith('head'):
									resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['ACCESORIES'] = self.inv.itmov[0]
								self.inv.itmov = ''

								if self.battle == True:
									self.turn += 1
									self.mnu = 1
									self.inventory = 0

							elif self.inv.space(self.mnu,self.exvar,self.opt,self.lopt) == True:
								self.ch_sfx.play(resources.SOUND['EQUIP'])
								trd = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt]
								database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
								if self.inv.itmov[0].startswith('clth'):
									resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['COSTUME'] = database.ITEMS[self.inv.itmov[0]][5] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.mnu]]['SKIN']
								self.inv.itmov = trd

							else: self.ch_sfx.play(resources.SOUND['ERROR']); self.inv.shake = 5

						elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_':
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.inv.itmov = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt]
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

					if self.inventory == 2:
						if self.exvar == 0:
							if self.inv.itmov != '':
								if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] == '_': 
									self.ch_sfx.play(resources.SOUND['EQUIP'])
									database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
									self.inv.itmov = ''
								else:
									self.ch_sfx.play(resources.SOUND['EQUIP'])
									trd = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt]
									database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = self.inv.itmov
									self.inv.itmov = trd
							elif database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_':
								self.ch_sfx.play(resources.SOUND['MENU_GO'])
								self.inv.itmov = database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt]
								database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']
						if self.exvar == 1:
							if self.inv.itmov != '':
								if database.STORAGE[self.opt][0] == '_':
									self.ch_sfx.play(resources.SOUND['EQUIP'])
									database.STORAGE[self.opt] = self.inv.itmov
									self.inv.itmov = ''
								else:
									self.ch_sfx.play(resources.SOUND['EQUIP'])
									trd = database.STORAGE[self.opt]
									database.STORAGE[self.opt] = self.inv.itmov
									self.inv.itmov = trd
							elif database.STORAGE[self.opt][0] != '_':
								self.ch_sfx.play(resources.SOUND['MENU_GO'])
								self.inv.itmov = database.STORAGE[self.opt]
								database.STORAGE[self.opt] = ['_','0000','_','_']
					elif self.inventory == 3:
						if database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt][0] != '_' and self.confirmation() == 1:
							database.INVENTORY[resources.PARTY[resources.FORMATION][self.mnu]][self.lopt][self.opt] = ['_','0000','_','_']

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

				if self.mnu < 0: self.mnu = len(resources.PARTY[resources.FORMATION]) - 1
				if self.mnu > len(resources.PARTY[resources.FORMATION]) - 1: self.mnu = 0

			#PHONE OPTIONS
			if self.pressed[resources.PHONE[0]] and self.inv.find(0,'phone') != None and self.inventory == 0 and self.shp == False and self.nmenu.show == False:
				if self.phone == 0 or self.phone > 1:
					if self.phone == 0:
						wh = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HAIR'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
						cl = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['COSTUME'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
						self.player[0]['HEAD'] = 'BLANKDD_' + wh
						self.player[0]['SPRITE'] = 'PHONE_' + cl
						self.opt = 0; self.lopt = 0; self.player[0]['PAUSE'] = 1
					if self.phone == 2: self.opt = 0; self.lopt = 0; self.phn.scroll = 0
					if self.phone == 3: self.opt = 1; self.lopt = 0; self.phn.scroll = 0
					if self.phone == 4: self.opt = 2; self.lopt = 0; self.phn.scroll = 0
					if self.phone == 5: self.opt = 0; self.lopt = 1; self.phn.scroll = 0
					if self.phone == 6: self.opt = 1; self.lopt = 1; self.phn.scroll = 0; self.ch_ton.stop(); self.ch_ton.set_volume(resources.SFX)
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
						if self.phone > 1: self.ch_sfx.play(resources.SOUND['MENU_BACK'])
						self.phone = 1
						self.mnu = 0
				else:
					self.phone = 0
					if self.battle == False:
						self.opt = 0
						self.lopt = 0
						self.player[0]['PAUSE'] = 0
					else:
						self.mnu = 1

			if self.phone > 0 and resources.BATTERY > 1.0:
				if self.phone > 1 and self.mnu == 0 and self.pressed[resources.RUN[0]]:
					self.ch_sfx.play(resources.SOUND['MENU_BACK'])
					self.phone = 1

				if self.phone == 1:
					if self.pressed[resources.UP[0]]: self.lopt -=1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]]: self.lopt +=1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.LEFT[0]]: self.opt -=1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: self.opt +=1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = 4
					if self.lopt > 4: self.lopt = 0

					if self.pressed[resources.ACT[0]]:
						if self.lopt == 0:
							if self.opt == 0: self.phone = 2; self.opt = round(self.player[0]['RECT'].x/30); self.lopt = round(self.player[0]['RECT'].x/30); self.mnu = 375
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

						if self.phone == 7: resources.recent_data(0)

						self.ch_sfx.play(resources.SOUND['MENU_GO'])
						self.phn.scroll = 0
						self.opt = 0
						self.lopt = 0
						self.mnu = 0

				elif self.phone == 3:
					if self.pressed[resources.LEFT[0]]:
						self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.mnu == 0: self.opt -=1; self.lopt = 0
						elif self.mnu < 3: self.mnu = 1
						else:
							self.mnu -=1
							if self.mnu < 3: self.mnu = 5

					if self.pressed[resources.RIGHT[0]]:
						self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.mnu == 0: self.opt +=1; self.lopt = 0
						elif self.mnu < 3: self.mnu = 2
						else:
							self.mnu +=1
							if self.mnu > 5: self.mnu = 3

					if self.pressed[resources.UP[0]]:
						self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.mnu < 3: self.lopt -= 1
						else:
							self.exvar -= 1
							if self.exvar < 0: self.exvar = 5
							resources.PARTY[self.lopt][self.mnu - 3] = self.exvar

					if self.pressed[resources.DOWN[0]]:
						self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.mnu < 3: self.lopt += 1
						else:
							self.exvar += 1
							if self.exvar > 5: self.exvar = 0
							resources.PARTY[self.lopt][self.mnu - 3] = self.exvar

					if self.opt == 0:
						if self.lopt < 0: self.lopt = len(resources.PARTY)
						if self.lopt > len(resources.PARTY): self.lopt = 0

						if self.pressed[resources.ACT[0]]:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							if self.lopt < len(resources.PARTY):
								if self.mnu == 0:
									self.mnu = 1
								elif self.mnu == 1:
									resources.FORMATION = self.lopt
									for i in resources.PARTY[resources.FORMATION]:
										resources.CHARACTERS[i]['HP'] = resources.CHARACTERS[i]['VITALITY'][resources.CHARACTERS[i]['LEVEL']]
									self.ch_ton.play(resources.SOUND['PARTY_CHANGE'])
									self.phn.pbg = resources.PARTY[resources.FORMATION][0]
									self.mnu = 0
									self.opt = 0
									self.lopt = 0
								elif self.mnu > 2:
									resources.PARTY_make(self.lopt)
									self.mnu = 0
								elif len(resources.PARTY) > 1:
									del resources.PARTY[self.lopt]
									self.mnu = 0 
							else:
								resources.PARTY.append([0,0,0])
								self.exvar = 0
								self.mnu = 3

					if self.opt == 1:
						if self.lopt < 0: self.lopt = len(resources.CONTACTS) - 1
						if self.lopt > len(resources.CONTACTS) - 1: self.lopt = 0

						if self.pressed[resources.ACT[0]]:
							if self.mnu == 0:
								pygame.time.wait(round(random.randint(10,200)))

								if resources.CREDIT > 0:
									wh = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HAIR'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
									cl = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['COSTUME'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
									resources.CREDIT -= 1
									resources.CALLHIST.insert(0,[resources.CONTACTS[self.lopt][1],False])
									self.player[0]['SPRITE'] = 'CALL_' + cl
									self.phone = 0
									self.dialog(database.DIALOGS[resources.CONTACTS[self.lopt][1]][0])
									self.player[0]['PAUSE'] = 1
									self.player[0]['SPRITE'] = 'PHONE_' + cl
									self.phone = 3
								else:
									self.dialog([database.MENU[17]])

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0

				elif self.phone == 4 and self.signal > 0:
					if self.mnu == 0:
						if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.LEFT[0]]: self.opt -= 1; self.lopt = 0; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.pressed[resources.RIGHT[0]]: self.opt += 1; self.lopt = 0; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					if self.pressed[resources.ACT[0]] and self.signal > 0:
						if self.mnu == 0: self.mnu = 1; self.ch_sfx.play(resources.SOUND['MENU_GO'])
						elif self.mnu > 0:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							if self.opt == 0: self.phn.e_unread[self.lopt][3] = 1
							if self.opt == 2: resources.EMAILS[self.lopt][3] = 1
							self.mnu = 0

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = len(resources.EMAILS) - 1
					if self.lopt > len(resources.EMAILS) - 1: self.lopt = 0

				elif self.phone == 5 and self.signal > 0:
					if self.mnu == 0:
						if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

					if self.pressed[resources.ACT]:
						self.ch_sfx.play(resources.SOUND['MENU_GO'])
						if self.mnu == 0: self.mnu = 1
						elif self.mnu > 0: self.mnu = 0

					if self.lopt < 0: self.lopt = 3
					if self.lopt > 3: self.lopt = 0

				elif self.phone == 6 and self.signal > 0:
					if self.pressed[resources.ACT[0]]:
						self.radonoff = not self.radonoff
					if self.radonoff == False and pygame.mixer.music.get_busy() == True:
						self.ch_sfx.play(resources.SOUND['MENU_BACK'])
						self.ch_ton.stop()
						pygame.mixer.music.stop()
					else:
						self.ch_sfx.play(resources.SOUND['MENU_GO'])
						self.ch_ton.play(resources.SOUND['NOISE'],-1)

				elif self.phone == 7 and self.signal > 0:
					if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

					if self.lopt < 0: self.lopt = 2
					if self.lopt > 2: self.lopt = 0

					if self.pressed[resources.ACT[0]] and self.signal > 0:
						self.ch_sfx.play(resources.SOUND['FILE_SAVE'])
						resources.PX = self.player[0]['RECT'].x
						resources.PY = self.player[0]['RECT'].y
						database.ID = self.lopt
						self.loadingif = 0.0
						if self.lopt < len(resources.FILES[0]):
							self.loading()
							resources.save_data()
							self.loading()
							resources.recent_data(1,self.lopt)
							self.loading()
							resources.recent_data(0)
						else: resources.new_data(); resources.save_data(); resources.recent_data(2,self.lopt); resources.recent_data(0)
						self.loadingif = None

				elif self.phone == 8 and self.signal > 0:
					if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

					if self.pressed[resources.ACT[0]]:
						if self.mnu == 0: self.mnu = 1; self.ch_sfx.play(resources.SOUND['MENU_GO'])
						elif self.mnu > 0: self.mnu = 0; self.ch_sfx.play(resources.SOUND['MENU_BACK'])

					if self.mnu == 0:
						if self.lopt < 0: self.lopt = len(database.BESTIARY) - 1
						if self.lopt > len(database.BESTIARY) - 1: self.lopt = 0

					if self.mnu > 0:
						if self.pressed[resources.LEFT[0]]: self.mnu = 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.pressed[resources.RIGHT[0]]: self.mnu = 2; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

						if self.lopt < 0: self.lopt = 3
						if self.lopt > 3: self.lopt = 0

				elif self.phone == 9:
					if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.LEFT[0]]: self.opt -= 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: self.opt += 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					if self.opt < 0: self.opt = 2
					if self.opt > 2: self.opt = 0
					if self.lopt < 0: self.lopt = len(resources.TASKS) - 1
					if self.lopt > len(resources.TASKS) - 1: self.lopt = 0

				elif self.phone == 10:
					if self.pressed[resources.LEFT[0]]: self.opt -= 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: self.opt += 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					if self.opt < 0: self.opt = len(resources.PARTY[resources.FORMATION]) - 1
					if self.opt > len(resources.PARTY[resources.FORMATION]) - 1: self.opt = 0

				elif self.phone == 11:
					if self.mnu == 0:
						if self.pressed[resources.ACT[0]]:
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							if self.lopt == len(resources.TACTICAL):
								resources.TACTICAL.append([0,0,0,0])
							self.mnu = 1
							self.opt = resources.TACTICAL[self.lopt][self.mnu - 1]

						if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

						if self.lopt < 0: self.lopt = len(resources.TACTICAL)
						if self.lopt > len(resources.TACTICAL): self.lopt = 0

					elif self.mnu > 0:
						if self.pressed[resources.ACT[0]]:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							if self.mnu < 5:
								database.tact_save(self.lopt)
								self.mnu = 0
							else:
								del resources.TACTICAL[self.lopt]
								self.mnu = 0

						if self.pressed[resources.UP[0]]: self.opt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.DOWN[0]]: self.opt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.LEFT[0]]: self.mnu -= 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
						if self.pressed[resources.RIGHT[0]]: self.mnu += 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

						if self.mnu > 0:
							if self.mnu < 1: self.mnu = 5
							if self.mnu > 5: self.mnu = 1
							if self.opt < 0: self.opt = 7
							if self.opt > 7: self.opt = 0

							if self.pressed[resources.LEFT[0]] or self.pressed[resources.RIGHT[0]]:
								if self.mnu < 5 and len(resources.TACTICAL) > 0: self.opt = resources.TACTICAL[self.lopt][self.mnu - 1]
							else:
								if self.mnu < 5 and len(resources.TACTICAL) > 0: resources.TACTICAL[self.lopt][self.mnu - 1] = self.opt

				elif self.phone == 12:
					if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

					if self.lopt < 0: self.lopt = len(database.ACHIEVEMENTS) - 1
					if self.lopt > len(database.ACHIEVEMENTS) - 1: self.lopt = 0

				elif self.phone == 14:
					if self.mnu == 0:
						if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
						if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

					if self.pressed[resources.ACT[0]]:
						if self.mnu == 0: self.mnu = 1; self.ch_sfx.play(resources.SOUND['MENU_GO'])
						elif self.mnu > 0: self.mnu = 0; self.ch_sfx.play(resources.SOUND['MENU_BACK'])

					if self.lopt < 0: self.lopt = len(database.MANUAL) - 1
					if self.lopt > len(database.MANUAL) - 1: self.lopt = 0

				elif self.phone == 15:
					if self.pressed[resources.UP[0]]: self.lopt -= 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]]: self.lopt += 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

					if self.mnu == 0:
						if self.lopt < 0: self.lopt = 3
						if self.lopt > 3: self.lopt = 0
					if self.mnu == 1:
						if self.lopt < 0: self.lopt = 7
						if self.lopt > 7: self.lopt = 0
					if self.mnu == 2:
						if self.lopt < 0: self.lopt = 1
						if self.lopt > 1: self.lopt = 0
					if self.mnu == 3:
						if self.lopt < 0: self.lopt = 7
						if self.lopt > 7: self.lopt = 0

					if self.mnu == 0:
						if self.pressed[resources.ACT[0]]:
							if self.lopt == 3:
								self.phn = menu.Phone()
								self.inv = menu.Inventory()
								self.shpmnu = menu.Shop()
								resources.save_sett()
								self.ch_sfx.play(resources.SOUND['MENU_GO'])
								self.opt = 1
								self.lopt = 4
								self.phone = 1
								if resources.CHAPTER == 0 and resources.SCENE == 0:
									self.ch_ton.play(resources.SOUND['CALLING'],-1)
									self.ch_rng.play(resources.SOUND['RINGTONE_' + str(self.phn.pbg)],-1)
									self.phone = 17
									self.nb = '977904623'
							else:
								self.mnu = self.lopt + 1
								self.opt = 0
								self.lopt = 0

					elif self.mnu == 1:

						if self.lopt == 0:
							if self.pressed[resources.LEFT[0]]:
								resources.LANG = 'EN'; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])
							if self.pressed[resources.RIGHT[0]]:
								resources.LANG = 'PT'; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					
						if self.lopt == 1:
							if self.pressed[resources.LEFT[0]]: resources.SPEED += 1; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])
							if self.pressed[resources.RIGHT[0]]: resources.SPEED -= 1; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])

							if resources.SPEED < 1: resources.SPEED = 5
							if resources.SPEED > 5: resources.SPEED = 1

						if self.lopt == 5:
							if self.pressed[resources.LEFT[0]]: resources.BORDER -= 1; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])
							if self.pressed[resources.RIGHT[0]]: resources.BORDER += 1; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])

							if resources.BORDER < 0: resources.BORDER = resources.RANGE_BORDER
							if resources.BORDER > resources.RANGE_BORDER: resources.BORDER = 0

						if self.lopt == 6:
							if self.pressed[resources.LEFT[0]]: resources.CENSORSHIP = False; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])
							if self.pressed[resources.RIGHT[0]]: resources.CENSORSHIP = True; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])

						if self.lopt == 7:
							if self.pressed[resources.LEFT[0]]: resources.HINT = False; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])
							if self.pressed[resources.RIGHT[0]]: resources.HINT = True; self.ch_sfx.set_volume(resources.SFX); self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					elif self.mnu == 3:
						if self.lopt == 0:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.DOWN[0],resources.LEFT[0],resources.RIGHT[0],resources.ACT[0],resources.PHONE[0],resources.BAG[0],resources.RUN[0]):
										database.UP = event.key; self.opt = 0

						if self.lopt == 1:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.UP[0],resources.LEFT[0],resources.RIGHT[0],resources.ACT[0],resources.PHONE[0],resources.BAG[0],resources.RUN[0]):
										database.DOWN = event.key; self.opt = 0

						if self.lopt == 2:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.DOWN[0],resources.UP[0],resources.RIGHT[0],resources.ACT[0],resources.PHONE[0],resources.BAG[0],resources.RUN[0]):
										database.LEFT = event.key; self.opt = 0

						if self.lopt == 3:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.DOWN[0],resources.LEFT[0],resources.UP[0],resources.ACT[0],resources.PHONE[0],resources.BAG[0],resources.RUN[0]):
										database.RIGHT = event.key; self.opt = 0

						if self.lopt == 4:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.DOWN[0],resources.LEFT[0],resources.RIGHT[0],resources.UP[0],resources.PHONE[0],resources.BAG[0],resources.RUN[0]):
										database.ACT = event.key; self.opt = 0

						if self.lopt == 5:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.DOWN[0],resources.LEFT[0],resources.RIGHT[0],resources.UP[0],resources.PHONE[0],resources.BAG[0],resources.ACT[0]):
										database.RUN = event.key; self.opt = 0

						if self.lopt == 6:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.DOWN[0],resources.LEFT[0],resources.RIGHT[0],resources.ACT[0],resources.UP[0],resources.BAG[0],resources.RUN[0]):
										database.PHONE = event.key; self.opt = 0

						if self.lopt == 7:
							if self.pressed[resources.ACT[0]]:
								if self.opt == 0: self.opt = 1
							else:
								if self.opt == 1:
									if event.key not in (resources.DOWN[0],resources.LEFT[0],resources.RIGHT[0],resources.ACT[0],resources.PHONE[0],resources.UP[0],resources.RUN[0]):
										database.BAG = event.key; self.opt = 0


					if self.pressed[resources.RUN[0]]:
						if self.mnu > 0:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							self.mnu = 0

				elif self.phone == 16:
					if self.pressed[resources.UP[0]] and self.lopt == 1: self.lopt = 0; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.DOWN[0]] and self.lopt == 0: self.lopt = 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])

					if self.pressed[resources.ACT[0]]:
						self.ch_sfx.play(resources.SOUND['MENU_GO'])
						if self.lopt == 0:
							webbrowser.get('windows-default').open('twitter.com/kaixtr')
						if self.lopt == 1:
							webbrowser.get('windows-default').open('github.com/kaixtr')

				elif self.phone == 17:
					if self.pressed[resources.LEFT[0]] and self.opt == 1: self.opt = 0; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.RIGHT[0]] and self.opt == 0: self.opt = 1; self.ch_sfx.play(resources.SOUND['MENU_VER'])
					if self.pressed[resources.ACT[0]]:
						self.ch_ton.stop()
						self.ch_rng.stop()
						if self.opt == 0:
							wh = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HAIR'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
							cl = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['COSTUME'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
							self.phone = 0
							self.ch_sfx.play(resources.SOUND['MENU_GO'])
							self.player[0]['DIRECTION'] = 0
							self.player[0]['SPD'] = 0
							self.player[0]['SPRITE'] = 'CALL_' + cl
							if self.dlgfa > 0:
								self.dialog(database.DIALOGS[self.nb][0])
								resources.CALLHIST.append([self.nb,True])
								self.player[0]['SPRITE'] = 'STANDD_' + cl
						elif self.opt == 1:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							self.phone = 1
						self.nb = ''
						if self.radonoff == True: pygame.mixer.music.unpause()
						if resources.CHAPTER == 0 and resources.SCENE == 0:
							self.phone = 0
							self.ch_msc.play(resources.SOUND['AMBIENCE_SIREN'],-1)
							self.transiction(False, 50)
							#self.dialog(database.DIALOGS['DALIBOR'][0])
							self.player[0]['PAUSE'] = 0
							self.transiction(False,0)

				elif self.phone == 18:
					if self.pressed[resources.ACT[0]]:
						trg = self.foe[0]
						f = {'N': trg['FILE']}
						f['DATE'] = str(resources.DATE[0]) + '/' + str(resources.DATE[1])
						i = len(database.BESTIARY) + 1
						if i < 10: i = '00' + str(i)
						elif i < 40: i = '0' + str(i)
						f['ID'] = i
						database.BESTIARY.append(f)
						self.ch_sfx.play(resources.SOUND['CAMERA'])
						self.phone = 0
						self.mnu = 1
						self.notification(trg['NAME'] + ' registrada',(134, 0, 211))
						database.best_regs(f)
			
			if self.battle == False and self.inventory == 0 and self.phone == 0 and self.shp == False and self.sleepin == False:
				p = 0
				for i in self.player:
					if i['PAUSE'] == 0 and i['PLAYING'] == True:
						if self.driving == 0:
							if i['JUMP'] == 0 and resources.MAP > 0:
								if self.pressed[resources.ACT[p]]:
									if i['HOLD'] != None:
										i['HOLD'] = None
						elif self.driving > 0:
							if resources.GAS > 0:
								if self.pressed[resources.LEFT[p]]:
									i['DIRECTION'] -= 1
									if i['DIRECTION'] == 0: i['DIRECTION'] = 8

								elif self.pressed[resources.RIGHT[p]]:
									i['DIRECTION'] += 1
									if i['DIRECTION'] == 9: i['DIRECTION'] = 1
					p += 1

		if self.phone == 2:
			if self.pressed[resources.UP[0]]: self.lopt -= 3
			if self.pressed[resources.DOWN[0]]: self.lopt += 3
			if self.pressed[resources.LEFT[0]]: self.opt -= 3
			if self.pressed[resources.RIGHT[0]]: self.opt += 3
			if self.pressed[resources.ACT[0]]: self.mnu +=5
			if self.pressed[resources.BAG[0]]: self.mnu -=5

			if self.opt < -self.map.width: self.opt = -self.map.width
			if self.opt > self.map.width: self.opt = self.map.width
			if self.lopt < -self.map.height: self.lopt = -self.map.height
			if self.lopt > self.map.height: self.lopt = self.map.height
			if self.mnu < 100: self.mnu = 100
			if self.mnu > 500: self.mnu = 500

		elif self.phone == 4:
			if self.mnu > 0:
				if self.pressed[resources.UP[0]]: self.mnu -=1
				if self.pressed[resources.DOWN[0]]: self.mnu +=1

				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 5:
			if self.mnu > 0:
				if self.pressed[resources.UP[0]]: self.mnu -=1
				if self.pressed[resources.DOWN[0]]: self.mnu +=1

				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 6:
			if self.pressed[resources.LEFT[0]]: self.fm -=1; self.vm -= 0.05
			if self.pressed[resources.RIGHT[0]]: self.fm +=1; self.vm += 0.05

			if self.fm < 0: self.fm = 180
			if self.fm > 180: self.fm = 0
			if self.vm < 0.0: self.vm = 1.0
			if self.vm > 1.0: self.vm = 0.0

			pygame.mixer.music.set_volume(self.vm)
			self.ch_ton.set_volume(1 - self.vm)
			if self.vm == 0.0 and self.radonoff == True:
				if resources.RADIO[str(math.floor(self.fm/20))] != []:
					pygame.mixer.music.load('Songs/FM_' + str(math.floor(self.fm/20)) + '/' + resources.RADIO[str(math.floor(self.fm/20))][self.msc])
					pygame.mixer.music.play()
				else: pygame.mixer.music.stop()

		elif self.phone == 13:
			if self.mnu > 0:
				if self.pressed[resources.UP[0]]: self.mnu -=1
				if self.pressed[resources.DOWN[0]]: self.mnu +=1
						
				if self.mnu < 1: self.mnu = 1
				if self.mnu > 1000: self.mnu = 1000

		elif self.phone == 15:
			if self.mnu == 1:
				if self.lopt == 2:
					if self.pressed[resources.LEFT[0]]: resources.COLOR[0] -= 2; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: resources.COLOR[0] += 2; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					if resources.COLOR[0] < 30: resources.COLOR[0] = 242
					if resources.COLOR[0] > 242: resources.COLOR[0] = 30
				if self.lopt == 3:
					if self.pressed[resources.LEFT[0]]: resources.COLOR[1] -= 2; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: resources.COLOR[1] += 2; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					if resources.COLOR[1] < 30: resources.COLOR[1] = 242
					if resources.COLOR[1] > 242: resources.COLOR[1] = 30
				if self.lopt == 4:
					if self.pressed[resources.LEFT[0]]: resources.COLOR[2] -= 2; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: resources.COLOR[2] += 2; self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					if resources.COLOR[2] < 30: resources.COLOR[2] = 242
					if resources.COLOR[2] > 242: resources.COLOR[2] = 30

			if self.mnu == 2:
				if self.lopt == 0:
					if self.pressed[resources.LEFT[0]]: resources.SFX -= 0.1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: resources.SFX += 0.1;  self.ch_sfx.play(resources.SOUND['MENU_HOR'])

					self.ch_sfx.set_volume(resources.SFX)
					self.ch_ton.set_volume(resources.SFX)
					self.ch_stp.set_volume(resources.SFX)
					self.ch_dlg.set_volume(resources.SFX)

					if resources.SFX < 0.0: resources.SFX = 0.0
					if resources.SFX > 1.0: resources.SFX = 1.0
				if self.lopt == 1:
					if self.pressed[resources.LEFT[0]]: resources.MSC -= 0.1; self.ch_msc.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT[0]]: resources.MSC += 0.1; self.ch_msc.play(resources.SOUND['MENU_HOR'])

					self.ch_msc.set_volume(resources.MSC)
					self.ch_rad.set_volume(resources.MSC)
					self.ch_rng.set_volume(resources.MSC)

					if resources.MSC < 0.0: resources.MSC = 0.0
					if resources.MSC > 1.0: resources.MSC = 1.0

		#PLAYER MOVEMENT
		p = 0
		for i in self.player:
			if i['PAUSE'] == 0 and i['PLAYING'] == True:
				self.pressed = pygame.key.get_pressed()
				if self.driving == 0:
					if i['JUMP'] == 0:
						if resources.MAP > 0:
							if self.pressed[resources.RUN[p]]:
								if len(self.player) > 1 and self.player[0]['SPD'] < 6:
									self.player[0]['NODES'].append({'RECT': self.player[0]['RECT'],'DIRECTION': self.player[0]['DIRECTION'],'SPD': self.player[0]['SPD']})
								i['SPD'] = 6
							else:
								if len(self.player) > 1 and self.player[0]['SPD'] > 3:
									self.player[0]['NODES'].append({'RECT': self.player[0]['RECT'],'DIRECTION': self.player[0]['DIRECTION'],'SPD': self.player[0]['SPD']})
								i['SPD'] = 3
						else: i['SPD'] = 1

						if self.pressed[resources.UP[p]]:
							if self.pressed[resources.LEFT[p]]: i['DIRECTION'] = 6
							elif self.pressed[resources.RIGHT[p]]: i['DIRECTION'] = 8
							else: i['DIRECTION'] = 7
							if len(self.player) > 1:
								self.player[0]['NODES'].append({'RECT': self.player[0]['RECT'],'DIRECTION': self.player[0]['DIRECTION'],'SPD': self.player[0]['SPD']})

						elif self.pressed[resources.DOWN[p]]:
							if self.pressed[resources.LEFT[p]]: i['DIRECTION'] = 4
							elif self.pressed[resources.RIGHT[p]]: i['DIRECTION'] = 2
							else: i['DIRECTION'] = 3
							if len(self.player) > 1:
								self.player[0]['NODES'].append({'RECT': self.player[0]['RECT'],'DIRECTION': self.player[0]['DIRECTION'],'SPD': self.player[0]['SPD']})

						elif self.pressed[resources.LEFT[p]]:
							if self.pressed[resources.UP[p]]: i['DIRECTION'] = 6
							elif self.pressed[resources.DOWN[p]]: i['DIRECTION'] = 4
							else: i['DIRECTION'] = 5
							if len(self.player) > 1:
								self.player[0]['NODES'].append({'RECT': self.player[0]['RECT'],'DIRECTION': self.player[0]['DIRECTION'],'SPD': self.player[0]['SPD']})

						elif self.pressed[resources.RIGHT[p]]:
							if self.pressed[resources.UP[p]]: i['DIRECTION'] = 8
							if self.pressed[resources.DOWN[p]]: i['DIRECTION'] = 2
							else: i['DIRECTION'] = 1
							if len(self.player) > 1:
								self.player[0]['NODES'].append({'RECT': self.player[0]['RECT'],'DIRECTION': self.player[0]['DIRECTION'],'SPD': self.player[0]['SPD']})

						else: i['SPD'] = 0

				elif self.driving > 0:
					if resources.GAS > 0:
						if self.pressed[resources.UP[p]]:
							self.driving = 0
							self.displayzw = 600
							self.displayzh = 400
							self.display = pygame.Surface((600, 400))
							self.cam.width = self.displayzw
							self.cam.height = self.displayzh
							i['DIRECTION'] = 3

						if self.pressed[databasresourcese.DOWN[p]]:
							if i['SPD'] > 0.0: i['SPD'] -= self.vehicles[self.driving - 1]['ACCELERATION']

						elif self.pressed[resources.RUN[p]]:
							if i['SPD'] < self.vehicles[self.driving - 1]['SPEED'] and resources.GAS > 0.0:
								i['SPD'] += self.vehicles[self.driving - 1]['ACCELERATION']
							resources.GAS -= self.vehicles[self.driving - 1]['GAS']
						else: i['SPD'] -= self.vehicles[self.driving - 1]['ACCELERATION']

			elif i['PLAYING'] == False:
				if len(self.player[0]['NODES']) > 0:
					if self.colide(i['RECT'], self.player[0]['NODES'][0]['RECT']):
						i['SPD'] = self.player[0]['NODES'][0]['SPD']
						i['DIRECTION'] = self.player[0]['NODES'][0]['DIRECTION']
						del self.player[0]['NODES'][0]
						break
				else: i['SPD'] = 0

			if i['FOLLOW'] != None:
				if i['FOLLOW'] != (None,None):
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

					if self.colide(i['RECT'],i['FOLLOW']):
						i['DIRECTION'] = i['FOLLEND']
						i['FOLLOW'] = None
						i['FOLLEND'] = 'head'
						i['SPD'] = 0
				else:
					i['DIRECTION'] = i['FOLLEND']
					i['FOLLOW'] = None
					i['FOLLEND'] = 'head'
					i['SPD'] = 0

			if self.colide(i, self.tilrect) == False:
				wh = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HAIR'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
				cl = resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['COSTUME'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
				gl = 1
				if i['JUMP'] > 0:
					if i['DIRECTION'] == 3: i['SPRITE'] = 'JUMPD_' + cl; i['RECT'].y += i['SPD']
					elif i['DIRECTION'] == 7: i['SPRITE'] = 'JUMPU_' + cl; i['RECT'].y -= i['SPD']
					'''elif i['SPD'] > 3:
						if i['DIRECTION'] == 1: i['HEAD'] = 'BLANKR_' + wh; i['SPRITE'] = 'RUNR_' + cl; i['RECT'].x += i['SPD']
						elif i['DIRECTION'] == 2: i['HEAD'] = 'BLANKRD_' + wh; i['SPRITE'] = 'RUNRD_' + cl; i['RECT'].x += i['SPD']; i['RECT'].y += i['SPD']
						elif i['DIRECTION'] == 3: i['HEAD'] = 'BLANKD_' + wh; i['SPRITE'] = 'RUND_' + cl; i['RECT'].y += i['SPD']
						elif i['DIRECTION'] == 4: i['HEAD'] = 'BLANKLD_' + wh; i['SPRITE'] = 'RUNLD_' + cl; i['RECT'].x -= i['SPD']; i['RECT'].y += i['SPD']
						elif i['DIRECTION'] == 5: i['HEAD'] = 'BLANKL_' + wh; i['SPRITE'] = 'RUNL_' + cl; i['RECT'].x -= i['SPD']
						elif i['DIRECTION'] == 6: i['HEAD'] = 'BLANKLU_' + wh; i['SPRITE'] = 'RUNLU_' + cl; i['RECT'].x -= i['SPD']; i['RECT'].y -= i['SPD']
						elif i['DIRECTION'] == 7: i['HEAD'] = 'BLANKU_' + wh; i['SPRITE'] = 'RUNU_' + cl; i['RECT'].y -= i['SPD']
						elif i['DIRECTION'] == 8: i['HEAD'] = 'BLANKRU_' + wh; i['SPRITE'] = 'RUNRU_' + cl; i['RECT'].x += i['SPD']; i['RECT'].y -= i['SPD']'''
				elif i['SPD'] > 0:
					if i['DIRECTION'] == 1: i['HEAD'] = 'BLANKR_' + wh; i['SPRITE'] = 'WALKR_' + cl; i['RECT'].x += i['SPD']
					elif i['DIRECTION'] == 2: i['HEAD'] = 'BLANKRD_' + wh; i['SPRITE'] = 'WALKRD_' + cl; i['RECT'].x += i['SPD']; i['RECT'].y += i['SPD']
					elif i['DIRECTION'] == 3: i['HEAD'] = 'BLANKD_' + wh; i['SPRITE'] = 'WALKD_' + cl; i['RECT'].y += i['SPD']
					elif i['DIRECTION'] == 4: i['HEAD'] = 'BLANKLD_' + wh; i['SPRITE'] = 'WALKLD_' + cl; i['RECT'].x -= i['SPD']; i['RECT'].y += i['SPD']
					elif i['DIRECTION'] == 5: i['HEAD'] = 'BLANKL_' + wh; i['SPRITE'] = 'WALKL_' + cl; i['RECT'].x -= i['SPD']
					elif i['DIRECTION'] == 6: i['HEAD'] = 'BLANKLU_' + wh; i['SPRITE'] = 'WALKLU_' + cl; i['RECT'].x -= i['SPD']; i['RECT'].y -= i['SPD']
					elif i['DIRECTION'] == 7: i['HEAD'] = 'BLANKU_' + wh; i['SPRITE'] = 'WALKU_' + cl; i['RECT'].y -= i['SPD']
					elif i['DIRECTION'] == 8: i['HEAD'] = 'BLANKRU_' + wh; i['SPRITE'] = 'WALKRU_' + cl; i['RECT'].x += i['SPD']; i['RECT'].y -= i['SPD']
				elif i['SPD'] == 0:
					if i['FOLLEND'] == 'head':
						print(wh)
						print(cl)
						if i['DIRECTION'] == 1: i['HEAD'] = 'BLANKR_' + wh; i['SPRITE'] = 'STANDR_' + cl
						elif i['DIRECTION'] == 2: i['HEAD'] = 'BLANKRD_' + wh; i['SPRITE'] = 'STANDRD_' + cl
						elif i['DIRECTION'] == 3: i['HEAD'] = 'BLANKD_' + wh; i['SPRITE'] = 'STANDD_' + cl
						elif i['DIRECTION'] == 4: i['HEAD'] = 'BLANKLD_' + wh; i['SPRITE'] = 'STANDLD_' + cl
						elif i['DIRECTION'] == 5: i['HEAD'] = 'BLANKL_' + wh; i['SPRITE'] = 'STANDL_' + cl
						elif i['DIRECTION'] == 6: i['HEAD'] = 'BLANKLU_' + wh; i['SPRITE'] = 'STANDLU_' + cl
						elif i['DIRECTION'] == 7: i['HEAD'] = 'BLANKU_' + wh; i['SPRITE'] = 'STANDU_' + cl
						elif i['DIRECTION'] == 8: i['HEAD'] = 'BLANKRU_' + wh; i['SPRITE'] = 'STANDRU_' + cl
						i['FOLLEND'] = 0
					else:
						if i['DIRECTION'] == 1: i['SPRITE'] = 'STANDR_' + cl
						elif i['DIRECTION'] == 2: i['SPRITE'] = 'STANDRD_' + cl
						elif i['DIRECTION'] == 3: i['SPRITE'] = 'STANDD_' + cl
						elif i['DIRECTION'] == 4: i['SPRITE'] = 'STANDLD_' + cl
						elif i['DIRECTION'] == 5: i['SPRITE'] = 'STANDL_' + cl
						elif i['DIRECTION'] == 6: i['SPRITE'] = 'STANDLU_' + cl
						elif i['DIRECTION'] == 7: i['SPRITE'] = 'STANDU_' + cl
						elif i['DIRECTION'] == 8: i['SPRITE'] = 'STANDRU_' + cl
				else: i['SPD'] = 0

			if resources.GAS < 1.0: i['DIRECTION'] = 0
			if i['SPD'] < 0: i['SPD'] = 0

		if self.dlgfa == 0:
			self.pressed = pygame.key.get_pressed()
			self.dlgspd = resources.SPEED
			for i in resources.ACT:
				if self.pressed[i]: self.dlgspd = 1
		p += 1

	def dialog(self, tx, wh=0):
		self.dlg = []
		self.dlgy = 0
		self.lopt = 0
		self.speakin = wh
		self.player[0]['PAUSE'] = 1
		self.player[0]['SPD'] = 0
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
								if self.ch_dlg.get_busy(): self.ch_sfx.play(resources.SOUND['TEXT_INPUT'])
								else: self.ch_dlg.play(resources.SOUND['TEXT_INPUT'])
								self.dlg[did] += i
								spd = 10
								break
							self.run()
					did += 1

			#DIALOG PROTOCOLS
			else:
				#SIDE MESSAGE
				if txt[tid] == 0:
					self.dlg.append(0)
					did += 1

				#WAIT FOR PRESS
				elif txt[tid] == 1:
					self.dlg.append(1)
					self.wait()
					self.ch_ton.play(resources.SOUND['MENU_GO'])
					did += 1

				#CHAPTER INTRO
				elif txt[tid] == 2:
					resources.SCENE = -1
					self.ch_msc.pause()
					self.ch_ton.play(resources.SOUND['BAUM'])
					self.player[0]['PAUSE'] = 3
					for i in range(100): self.run()
					resources.SCENE = 0
					self.player[0]['PAUSE'] = 1
					self.ch_msc.unpause()

				#CHAPTER END
				elif txt[tid] == 2:
					self.classrun = False

				#MONEY GET
				elif txt[tid][0] == 0 and self.notx == 0:
					resources.MONEY += txt[tid][1]
					self.ch_sfx.play(resources.SOUND['CASH_GET'])
					self.notification('Adquiriu $' + str(txt[tid][1]),(255, 255, 255))

				#ITEM GET
				elif txt[tid][0] == 1 and self.notx == 0:
					if txt[tid][3] > 0 and database.CHESTS[self.room][txt[tid][3] - 1] == False:
						if len(txt[tid]) > 4: prp = txt[tid][4]
						else: prp = '0000'
						self.inv.add(resources.PARTY[resources.FORMATION][0],txt[tid][1],prp)
						resources.MONEY -= txt[tid][2]
						self.ch_sfx.play(resources.SOUND['ITEM_GET'])
						self.notification('Adquiriu ' + database.ITEMS[txt[tid][1]][0],(255, 255, 255))
						database.CHESTS[self.room][txt[tid][3] - 1] = True
					else:
						for j in database.DIALOGS['EMPTY CHEST'][::-1]:
							txt.insert(tid + 1, j)

				#MORALITY
				elif txt[tid][0] == 2 and self.notx == 0:
					resources.MORALITY += txt[tid][1]
					self.ch_sfx.play(resources.SOUND['NOTIFICATION'])
					self.notification(txt[tid][1],(0, 0, 0))

				#MAP MARKER
				elif txt[tid][0] == 3 and self.notx == 0:
					self.ch_sfx.play(resources.SOUND['NOTIFICATION'])
					self.notification('Marcador adicionado',(140, 255, 253))

				#CALLING
				elif txt[tid][0] == 4:
					if txt[tid][1] != 'stop':
						self.ch_ton.play(resources.SOUND['CALLING'],-1)
						self.ch_rng.play(resources.SOUND['RINGTONE_' + str(self.phn.pbg)])
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
						self.ch_sfx.play(resources.SOUND['EQUIP'])
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

				#NEW EMAIL
				elif txt[tid][0] == 5 and self.notx == 0:
					self.ch_sfx.play(resources.SOUND['NOTIFICATION'])
					mail = database.EMAILS[txt[tid][1]].copy()
					mail.append(0)
					resources.INBOX.append(mail)
					resources.inbx_save(len(resources.INBOX)-1,0)
					self.notification('Novo email',(255, 221, 0))

				#NEW TASK
				elif txt[tid][0] == 6 and self.notx == 0:
					self.ch_sfx.play(resources.SOUND['NOTIFICATION'])
					resources.TASKS.append([txt[tid][1], 0])
					resources.task_save(txt[tid][1],0)
					self.notification('Nova tarefa disponível',(255, 123, 0))

				#NEW CONTACT
				elif txt[tid][0] == 7 and self.notx == 0:
					self.ch_sfx.play(resources.SOUND['NOTIFICATION'])
					database.CONTACTS.append(database.NUMBERS[txt[tid][1]].copy())
					database.call_save(len(database.CONTACTS)-1)
					self.notification('Contato adicionado',(165, 255, 0))

				#ACHIEVEMENT
				elif txt[tid][0] == 8 and self.notx == 0:
					self.ch_sfx.play(resources.SOUND['ACHIEVEMENT'])
					database.ACHIEVEMENTS[txt[tid][1]][2] = True
					self.notification(database.ACHIEVEMENTS[txt[tid][1]][0],(255, 191, 0))

				#RANKING
				elif txt[tid][0] == 9 and self.notx == 0:
					self.ch_sfx.play(resources.SOUND['NOTIFICATION'])
					self.notification('Subiu de posição!',(56, 255, 0))

				#DIALOG CHOICES
				elif txt[tid][0] == 10:
					while self.dlgfa > 0:
						if self.winbar < 50 and self.battle == False: self.winbar += 5
						self.dlgfa -= 50
						self.run()
					else:
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

				#SKIP DIALOGS
				elif txt[tid][0] == 11:
					tid += txt[tid][1]

				#RETURN DIALOGS
				elif txt[tid][0] == 12:
					tid -= txt[tid][1]

				#BATTLE
				elif txt[tid][0] == 13:
					self.dlg = []
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

				#ARMY BATTLE
				elif txt[tid][0] == 14:
					self.dlg = []
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

				#PLAY MUSIC
				elif txt[tid][0] == 15:
					pygame.mixer.music.load('Music/' + txt[tid][1] + '.mp3')
					pygame.mixer.music.play(-1)

				#PLAY SFX
				elif txt[tid][0] == 16:
					if len(txt[tid]) > 2: lp = txt[tid][2]
					else: lp = 0
					self.ch_sfx.play(resources.SOUND[txt[tid][1]],lp)

				#DELIVERY
				elif txt[tid][0] == 17:
					self.waitime.append([txt[tid][1],txt[tid][2],txt[tid][3]])

				#CHANGE PARTY
				elif txt[tid][0] == 18:
					ap = []
					p = 0
					for i in txt[tid][1:]:
						if i[1] != None:
							for n in range(len(self.npcs)):
								if i[1] == self.npcs[n]['N']:
									player = self.player[p].copy()
									xx = player['RECT'].x
									yy = player['RECT'].y
									dd = player['DIRECTION']
									cc = resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]].copy()
									ii = cc['HAIR'] + cc['COSTUME'] + cc['SKIN']
									npc = self.npcs[n].copy()
									self.player[p]['RECT'].x = npc['RECT'].x
									self.player[p]['RECT'].y = npc['RECT'].y
									self.player[p]['DIRECTION'] = npc['DIRECTION']
									self.player[p]['FOLLEND'] = 'head'
									self.player[p]['SPD'] = 0
									self.npcs[n]['RECT'].x = xx
									self.npcs[n]['RECT'].y = yy
									self.npcs[n]['INDEX'] = ii
									self.npcs[n]['DIRECTION'] = dd
									self.npcs[n]['MOVE'] = 'stand'
									if len(i) > 2: self.npcs[n]['WHO'] = i[2]
						ap.append(i[0])
						p += 1
					resources.PARTY[resources.FORMATION] = ap

				#DECREASE STATUS
				elif txt[tid][0] == 19:
					for i in self.foe:
						prb = round(random.randint(0,10))
						if prb > 4:
							if txt[tid][1] == 0: i['STRENGHT'] -= txt[tid][2]
							if txt[tid][1] == 1: i['AGILITY'] -= txt[tid][2]
							if txt[tid][1] == 2: i['RESISTANCE'] -= txt[tid][2]
							self.attackimation(0)

				#INCREASE STATUS
				elif txt[tid][0] == 20:
					for i in self.fig:
						prb = round(random.randint(0,10))
						if prb > 4:
							if txt[tid][1] == 0: i['STRENGHT'] += txt[tid][2]
							if txt[tid][1] == 1: i['AGILITY'] += txt[tid][2]
							if txt[tid][1] == 2: i['RESISTANCE'] += txt[tid][2]
							self.attackimation(0)

				#NEXT SCENE
				elif txt[tid][0] == 21:
					if isinstance(txt[tid][1],str): resources.DLGSAV[txt[tid][1]] = txt[tid][2]
					else: resources.SCENE = txt[tid][1]

				#NAME INPUT
				elif txt[tid][0] == 22:
					snd = self.ch_msc.get_sound()
					self.ch_msc.stop()
					self.nmenu = menu.Naming()
					self.nmenu.ninput = txt[tid][1]
					self.nmenu.show = True
					self.FPS = 0
					while self.nmenu.show == True:
						self.nmenu.events()
						self.nmenu.run()
						self.run()
					self.FPS = 60
					database.load_dialogs()
					self.ch_msc.play(snd,-1)

				#GET OTHER DIALOG
				elif txt[tid][0] == 23:
					if self.battle == True:
						if database.FREAKS[txt[tid][1]]['TYPE'] not in ('humanoid','psychic'):
							txt[tid][1] = database.DIALOGS['IRRATIONAL']; txt[tid][2] = 0
						else: txt[tid][1] = database.DIALOGS[self.foe[0]['NAME'].upper()]; txt[tid][2] = 0
					for j in database.DIALOGS[txt[tid][1]][txt[tid][2]].copy()[::-1]:
						txt.insert(tid + 1, j)
					did = len(self.dlg)

				#MOVE CHARACTER
				elif txt[tid][0] == 24:
					if txt[tid][1] == None:
						if txt[tid][2] != (None,None):
							self.player[0]['FOLLOW'] = pygame.Rect(txt[tid][2][0],txt[tid][2][1],10,10)
						else: self.player[0]['FOLLOW'] = (None,None)
						self.player[0]['FOLLEND'] = txt[tid][3]
						if len(txt[tid]) > 4: self.player[0]['FOLLMOV'] = txt[tid][4]
					else:
						for i in self.npcs:
							if i['N'] == txt[tid][1]:
								if txt[tid][2] != (None,None):
									i['FOLLOW'] = pygame.Rect(txt[tid][2][0],txt[tid][2][1],10,10)
								else: i['FOLLOW'] = (None,None)
								i['FOLLEND'] = txt[tid][3]
								if len(txt[tid]) > 4: i['FOLLMOV'] = txt[tid][4]

				#CHARACTER EMOTION
				elif txt[tid][0] == 25:
					if txt[tid][1] == None:
						self.player[0]['HEAD'] = txt[tid][2] + '_' + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HAIR'] + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SKIN']
					else:
						for i in self.npcs:
							if i['N'] == txt[tid][1]:
								i['HEAD'] = txt[tid][2] + '_' + i['INDEX'][0:3] + i['INDEX'][5]

				#CAMERA
				elif txt[tid][0] == 26:
					if isinstance(txt[tid][1],int):
						for i in self.npcs:
							if i['N'] == txt[tid][1]:
								self.speakin = i['RECT']
					else: self.speakin = pygame.Rect(txt[tid][1][0],txt[tid][1][1],1,1)

				#WAIT
				elif txt[tid][0] == 27:
					ds = self.dlg.copy()
					self.dlg = []
					for i in range(txt[tid][1]): self.run()
					self.dlg = ds

				#TUTORIAL
				elif txt[tid][0] == 28:
					if resources.HINT == True:
						self.ch_ton.play(resources.SOUND['NOTIFICATION'])
						self.tutorial = {'TEXT': database.TUTORIALS[txt[tid][1]].copy(), 'OUTPUT': [], 'FADE': 0, 'TIME': 0, 'WAIT': 300, 'NEXT': '','GO': 0}
						for j in self.tutorial['TEXT']:
							if isinstance(j,list):
								if j[0] == 'phone':
									self.tutorial['GO'] = j[1]
									if len(j) > 2: self.tutorial['NEXT'] = j[2]
								if j[0] == 'wait':
									self.tutorial['WAIT'] = j[1]
									if len(j) > 2: self.tutorial['NEXT'] = j[2]
								if j[0] == 'image':
									self.tutorial['OUTPUT'].append(j)
							else: self.tutorial['OUTPUT'].append(j)

				#ANOTHER PLACE
				elif txt[tid][0] == 29:
					ds = self.dlg.copy()
					self.dlg = []
					self.transiction(True, 210, 10)
					self.rendermap(txt[tid][1])
					self.player[0]['RECT'].x = txt[tid][2]
					self.player[0]['RECT'].y = txt[tid][3]
					self.transiction(False, 50, 10)
					self.dlg = ds

				#PUT CHARACTER
				elif txt[tid][0] == 30:
					ind = 0
					for n in self.npcs:
						if n['N'] > ind: ind = n['N']
					ind += 1
					print(txt[tid])
					self.npcs.append({'N': ind, 'RECT': pygame.Rect(txt[tid][1][0], txt[tid][1][1], 0, 0), 'TYPE': 0, 'INDEX': txt[tid][2], 'WHO': txt[tid][3],
					'GIF': 0.0,'BLINK': 100,'HEAD': 'BLANKD_' + txt[tid][2][0:3] + txt[tid][2][5],'SPRITE': 'STANDD_' + txt[tid][2][3:6],'MOVE': 'fixed','DIRECTION': 3,'SPD': 0,
					'JUMP': 0,'GRAVITY': -5,'TIME': 20,'FOLLOW': None,'FOLLEND': 0,'FOLLMOV': '','TALKING': False,'SWIM': None,'HOLD': None})
					self.objects.append([2,ind,txt[tid][1][1]])

				#CENSORSHIP
				elif txt[tid][0] == 31:
					if resources.CENSORSHIP == False: txt.insert(tid + 1, txt[tid][2])
					elif resources.CENSORSHIP == True: txt.insert(tid + 1, txt[tid][1])
			tid += 1

		self.dlg = []
		self.speakin = 0
		self.player[0]['PAUSE'] = 0

		while self.dlgfa < 500:
			self.dlgfa += 50
			if self.winbar > 0 and self.battle == False:
				self.winbar -= 5
				self.run()

	def diopt(self, ln):
		self.lopt = 1
		trigger = True
		while trigger:
			self.run()
			for event in pygame.event.get():
				self.pressed = pygame.key.get_pressed()
				if self.pressed[resources.UP[0]]:
					if self.lopt < ln: self.ch_sfx.play(resources.SOUND['MENU_HOR']); self.lopt += 1
				if self.pressed[resources.DOWN[0]]:
					if self.lopt > 1: self.ch_sfx.play(resources.SOUND['MENU_VER']); self.lopt -= 1
				if self.pressed[resources.ACT[0]]:
					self.ch_ton.play(resources.SOUND['MENU_GO'])
					i = 1
					crg = -1
					while i <= ln + 1:
						if i != self.lopt: del self.dlg[crg - i]; crg += 1; ln -= 1
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
		brd.fill((resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]))
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
				if self.pressed[resources.LEFT[0]]: self.ch_sfx.play(resources.SOUND['MENU_HOR']); opt = 1
				if self.pressed[resources.RIGHT[0]]: self.ch_sfx.play(resources.SOUND['MENU_VER']); opt = 2
				if self.pressed[resources.ACT[0]]:
					yesno = opt
					if yesno == 1: self.ch_sfx.play(resources.SOUND['MENU_GO'])
					if yesno == 2: self.ch_sfx.play(resources.SOUND['MENU_BACK'])
					opt = 0

			wdw.fill((0,0,0))
			wdw.blit(self.monotype.render(database.MENU[85], True, (255, 255, 255)), (45, 10))
			if opt == 1: wdw.blit(self.monotype.render(database.MENU[83], True, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2])), (40, 50))
			else: wdw.blit(self.monotype.render(database.MENU[83], True, (255, 255, 255)), (40, 50))
			if opt == 2: wdw.blit(self.monotype.render(database.MENU[84], True, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2])), (110, 50))
			else: wdw.blit(self.monotype.render(database.MENU[84], True, (255, 255, 255)), (110, 50))

			self.display.blit(brd,(195,145))
			self.display.blit(wdw,(200,150))
			self.screen.blit(pygame.transform.scale(self.display, (self.windoww, self.windowh)), (self.displayx, self.displayy))
			pygame.display.update()
			pygame.display.flip()
			pygame.time.Clock().tick(self.FPS)

		return yesno

	def transiction(self, fade, limit, spd=5):
		if fade == False:
			while self.winbar > limit:
				self.winbar -= spd
				if self.winbar > limit: self.run()
		else:
			while self.winbar < limit:
				self.winbar += spd
				if self.winbar < limit: self.run()

	def fight(self):
		#BATTLE START
		if self.turn < 0:
			self.inventory = 0
			self.phone = 0
			self.shp = False
			self.player[0]['PAUSE'] = 2
			if self.radonoff == True: pygame.mixer.music.pause()
			if self.turn == -1: self.ch_ton.play(resources.SOUND['BATTLE_FOE'])
			if self.turn == -2: self.ch_ton.play(resources.SOUND['BATTLE_ENEMY'])
			if self.turn == -3: self.ch_ton.play(resources.SOUND['BATTLE_AMBUSH'])
			else: self.ch_ton.play(resources.SOUND['BATTLE_BOSS'])
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
			for i in resources.PARTY[resources.FORMATION]:
				dt = resources.CHARACTERS[i]
				if dt['HP'] > 0:
					dt['N'] = tr
					self.fig.append(dt)
				tr += 1

			self.bbg = pygame.image.load('Backgrounds/mountains.png')
			self.player[0]['SPD'] = 0
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
			for i in resources.PARTY[resources.FORMATION]:
				self.pstr.append(resources.CHARACTERS[i]['STRENGHT'][resources.CHARACTERS[i]['LEVEL']])
				self.patt.append(resources.CHARACTERS[i]['ATTACK'][resources.CHARACTERS[i]['LEVEL']])
				self.pagi.append(resources.CHARACTERS[i]['AGILITY'][resources.CHARACTERS[i]['LEVEL']])
				self.pres.append(resources.CHARACTERS[i]['RESISTANCE'][resources.CHARACTERS[i]['LEVEL']])
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

			self.ch_msc.play(resources.SONGS[self.foe[0]['SONG']],-1)
			self.player[0]['GIF'] = 0.0
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
		elif self.turn < len(resources.PARTY[resources.FORMATION]):
			again = False
			self.mnu = 3
			if self.equip[self.turn] < 4:
				pp = int(database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1])
				pp -= 1
				database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1] = str(pp)
				gottem = False
				for i in self.foe:
					if self.colide(self.aim, i['MASK']) and i['FIGHTING'] == True:
						gottem = True
						dmg = int(random.randint(database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0]][5]['DAMAGE'] - 2,\
						database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0]][5]['DAMAGE'] + 2)) - i['RESISTANCE']
						if resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.turn]]['HEALTH'] == 11: dmg = int(dmg/2)
						if i['HEALTH'] != 1: i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE']) + '_damage.png')

						if dmg > 0:
							for p in range(dmg * 2):
								self.particles.append({'X': self.aim.x, 'Y': self.aim.y, 'RADIUS': round(random.randint(3,5)), 'DIRECTION': round(random.randint(0,360)), 'SPEED': round(random.randint(2,6))})
							if dmg == database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0]][5]['DAMAGE'] + 2 - i['RESISTANCE']:
								self.ch_sfx.play(resources.SOUND['CRITICAL'])
								self.hitisplay(10, i['MASK'], database.BATTLE[3], (200, 0, 0))
							else:
								self.ch_sfx.play(resources.SOUND['HIT'])
								self.hitisplay(10, i['MASK'], str(dmg), (200, 0, 0))
							if i['HEALTH'] != 1: i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE'])+ '_stand.png')
							i['HP'] -= dmg
							self.hits += 1
							self.tdmg += dmg
						else: self.hitisplay(0, None, database.BATTLE[5], (255, 255, 255))

						#CHECK WIN
						if i['HP'] <= 0:
							if dmg >= i['VITALITY']: again = True
							self.ch_ton.play(resources.SOUND['SCREAM_' + i['FILE'].upper()])
							while i['FADE'] > 0:
								i['FADE'] -= 1
								self.run()
							if i['ITEM'] != None:
								prb = round(random.randint(0,100))
								if prb > i['ITEM'][1]:
									self.inv.add(0,i['ITEM'][0])
									self.ch_sfx.play(resources.SOUND['ITEM_GET'])
									self.notification('Adquiriu ' + database.ITEMS[i['ITEM'][0]][0],(255, 255, 255))
							i['FIGHTING'] = False

						self.mnu = 0
				if gottem == False:
					self.ch_sfx.play(resources.SOUND['MISS'])
					self.hitisplay(5, self.aim, database.BATTLE[4], (200, 200, 200))

			elif self.equip[self.turn] == 5:
				self.dialog(database.DIALOGS['BATTLEDIALOG'][resources.PARTY[resources.FORMATION][self.turn]])
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
					self.player[0]['RECT'].x += 150
					self.transiction(False, 0)
				else:
					self.dialog([database.BATTLE[16]])

			if again == True and self.battle == True:
				self.ch_ton.play(resources.SOUND['ONE_MORE'])
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
									self.ch_ton.play(resources.SOUND['SCREAM_' + i['FILE'].upper()])
									self.ch_sfx.play(resources.SOUND['DAMAGE_1'])
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
									self.ch_sfx.play(resources.SOUND['HIT'])
									self.hitisplay(10, self.mrc[pl], str(act[2]), (0, 200, 0))
									self.mrc[pl]['SPRITE'] = pygame.image.load('Sprites/frk_' + (self.mrc[pl]['FILE']) + '_stand.png')
									self.mrc[pl]['HP'] += act[2]

							elif act[2] > 0:
								self.ch_ton.play(resources.SOUND['HEAL'])
								i['HP'] += act[2]

						elif act[3] == 2:
							if act[2] < 0:
								if self.tatt[pl] < 2:
									self.ch_ton.play(resources.SOUND['ATTRIBUTE_LOSS'])
									self.patt[pl] += act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[22],1])
									self.tatt[pl] += 1
							elif act[2] > 0:
								act[2] += act[2]
								self.ton_sfx.play(resources.SOUND['ATTRIBUTE_GAIN'])
								self.dialog([dd, i['NAME'] + database.BATTLE[21] + str(act[2]) + database.BATTLE[22],1])

						elif act[3] == 3:
							if act[2] < 0:
								self.turn = self.fig[pl]['N']
								if self.tagi[self.turn] < 2:
									self.ch_ton.play(resources.SOUND['ATTRIBUTE_LOSS'])
									self.pagi[self.turn]+=act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[23],1])
									self.tagi[self.turn]+=1
							elif act[2] > 0:
								i['AGILITY']+=act[2]
								self.ton_sfx.play(resources.SOUND['ATTRIBUTE_GAIN'])
								self.dialog([dd, i['NAME'] + database.BATTLE[21] + str(act[2]) + database.BATTLE[23],1])

						elif act[3] == 4:
							if act[2] < 0:
								self.turn = self.fig[pl]['N']
								if self.tstr[self.turn]<2:
									self.ch_ton.play(resources.SOUND['ATTRIBUTE_LOSS'])
									self.pstr[self.turn] += act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[24],1])
									self.tstr[self.turn] += 1
							elif act[2] > 0:
								i['STRENGHT'] += act[2]
								self.ton_sfx.play(resources.SOUND['ATTRIBUTE_GAIN'])
								self.dialog([dd, i['NAME'] + database.BATTLE[21] + str(act[2]) + database.BATTLE[24],1])

						elif act[3] == 5:
							if act[2] < 0:
								self.turn = self.fig[pl]['N']
								if self.tagi[self.turn] < 2:
									self.ch_ton.play(resources.SOUND['ATTRIBUTE_LOSS'])
									self.pres[self.turn] += act[2]
									self.dialog([dd, self.fig[pl]['NAME'] + database.BATTLE[20] + str(act[2]) + database.BATTLE[25],1])
									self.tres[self.turn] += 1
							elif act[2] > 0:
								i['RESISTANCE'] += act[2]
								self.ton_sfx.play(resources.SOUND['ATTRIBUTE_GAIN'])
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
								if resources.MAP == nw['HABITAT']:
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
							self.ch_ton.play(resources.SOUND['CHARGE'])
							self.attackimation(act[5])
							self.turn = self.fig[pl]['N']
							self.ch_ton.play(resources.SOUND['SCREAM_' + i['FILE'].upper()])
							self.ch_sfx.play(resources.SOUND['DAMAGE_1'])
							if self.attackimation(act[5]) == False:
								act[2] -= int(act[2]/5)
								self.fig[pl]['HP'] += act[2] + self.pres[pl]
								self.hitisplay(-act[2] * 2, None, '', (0,0,0))
								self.hpl += act[2]
							else:
								self.ch_sfx.play(resources.SOUND['HIT'])
								for p in range(dmg * 3):
									self.particles.append({'X': self.aim.x, 'Y': self.aim.y, 'RADIUS': round(random.randint(3,5)), 'DIRECTION': round(random.randint(0,360)), 'SPEED': round(random.randint(2,6))})
								self.hitisplay(10, i['MASK'], str(act[2]), (200, 0, 0))
								if i['HEALTH'] != 1: i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE'])+ '_stand.png')
								i['HP'] -= act[2]
								self.hits += 1
								self.tdmg += act[2]

							#CHECK WIN
							if i['HP'] <= 0:
								self.ch_ton.play(resources.SOUND['SCREAM_' + i['FILE'].upper()])
								while i['FADE'] > 0:
									i['FADE'] -= 1
									self.run()
								if i['ITEM'] != None:
									prb = round(random.randint(0,100))
									if prb > i['ITEM'][1]:
										self.inv.add(0,i['ITEM'][0])
										self.ch_sfx.play(resources.SOUND['ITEM_GET'])
										self.notification('Adquiriu ' + database.ITEMS[i['ITEM'][0]][0],(255, 255, 255))
								i['FIGHTING'] = False

						#CHECK DEATH
						if self.fig[pl]['HP'] <= 0:
							self.mnu = 1
							self.fig[pl]['HEALTH'] = 9
							self.ch_ton.play(resources.SOUND['INCONSCIOUS'])
							self.dialog([self.fig[pl]['NAME'] + database.BATTLE[31]])
							del self.fig[pl]

						i['SPRITE'] = pygame.image.load('Sprites/frk_' + (i['FILE']).lower() + '_stand.png')

					else: 
						self.ch_sfx.play(resources.SOUND['MISS'])
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
				self.ch_sfx.play(resources.SOUND['DAMAGE_1'])
				self.hpl += dmg[p]
			self.mnu = 1

		if self.turn == len(self.fig): self.fight()

		#VICTORY
		dth = 0
		for d in self.foe:
			if d['HP'] <= 0: dth += 1
		if dth == len(self.foe):
			self.ch_msc.fadeout(500)
			if len(self.foe) >= 10 or self.foe[0]['TYPE'] == 'boss': self.ch_ton.play(resources.SOUND['BATTLE_BOSS_WON'])
			elif self.hpl == 0: self.ch_ton.play(resources.SOUND['BATTLE_PERFECT'])
			else: self.ch_ton.play(resources.SOUND['BATTLE_WON'])
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
			for i in range(len(resources.PARTY[resources.FORMATION])):
				resources.CHARACTERS[i]['XP'] += self.xp
				plux = int(100/(resources.CHARACTERS[i]['NEXTLEVEL'][resources.CHARACTERS[i]['LEVEL']]/resources.CHARACTERS[i]['XP']))
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
							self.ch_ton.play(resources.SOUND['LEVEL_UP'],-1)
							acc = 35
							while self.mnu > -350:
								self.mnu -= acc
								self.run()
							pl = True
						self.barxp[i] = 0
						resources.CHARACTERS[resources.PARTY[resources.FORMATION][i]]['LEVEL'] += 1
						resources.CHARACTERS[resources.PARTY[resources.FORMATION][i]]['HP'] += resources.CHARACTERS[resources.PARTY[resources.FORMATION][i]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][i]]['LEVEL'] - 1] - resources.CHARACTERS[resources.PARTY[resources.FORMATION][i]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][i]]['LEVEL']]
						resources.CHARACTERS[resources.PARTY[resources.FORMATION][i]]['XP'] = 0
						plux -= 100
				resources.SCENE = 1
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
			self.player[0]['PAUSE'] = 0
			self.transiction(False, 0)

		#GAME OVER
		dth = 0
		for d in self.fig:
			if d['HP'] <= 0: dth += 1
		if dth == len(self.fig):
			self.ch_msc.fadeout(500)
			self.ch_ton.play(resources.SOUND['BATTLE_LOST'])
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
			resources.load_data()
			resources.PX = 315
			resources.PY = 200
			resources.MONEY -= 100 * len(resources.PARTY[resources.FORMATION])
			for i in resources.PARTY[resources.FORMATION]:
				resources.CHARACTERS[i]['HP'] = resources.CHARACTERS[i]['VITALITY'][resources.CHARACTERS[i]['LEVEL']]
				resources.CHARACTERS[i]['HEALTH'] = 0
			self.__init__()
			if resources.CHAPTER > 0: self.rendermap('hospital_0')
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
			while self.effgif < len(resources.SPRITES['ATTACKIMATION_' + str(wh)]):
				for event in pygame.event.get():
					self.pressed = pygame.key.get_pressed()
					if self.pressed[resources.ACT[0]] and self.effgif == len(resources.SPRITES['ATTACKIMATION_' + str(wh)]):
						ddg = True
				self.run()
				self.effgif += 0.5
		else:
			while True:
				for event in pygame.event.get():
					self.pressed = pygame.key.get_pressed()
					if self.pressed[resources.ACT[0]] and self.effgif > 4.0:
						counter = True
				if counter == False: self.effgif += 0.25
				if counter == True: self.effgif -= 0.25
				print(self.effgif)

				if self.effgif == len(resources.SPRITES['ATTACKIMATION_' + str(wh)]): ddg = False; break
				elif self.effgif == 0.0: ddg = True; break
				self.run()

		self.effttack = None
		self.effgif = 0

		return ddg

	def rendermap(self, mp):
		if mp == 'rodoviary':  self.map = pytmx.load_pygame('Maps/' + mp + '.tmx'); resources.MAP = 0
		elif mp[1:8] == 'highway':  self.map = pytmx.load_pygame('Maps/' + mp[1:11] + '.tmx'); resources.MAP = int(mp[0]) + 1; self.cityname = database.CITIES[resources.MAP]
		else: self.map = pytmx.load_pygame('Maps/' + mp + '.tmx')
		self.room = mp
		self.cam.x = 0
		self.cam.y = 0
		self.tilmap = [[],[],[],[],[],[],[]]
		self.objects = [[0,0,self.player[0]['RECT'].y]]
		self.tilrect = [[],[],[],[],[],[]]
		self.en = []
		self.foe = []
		self.npcs = []
		self.vehicles = []
		self.portals = []
		self.signs = []
		self.lights = []
		self.particles = []
		self.loadingif = 0
		self.bbm = 0
		self.player[0]['NODES'] = []

		#DRAW MAP
		for i in range(3):
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

								try: t = self.map.get_tile_properties(x, y, i)['TYPE'].upper()
								except: t = 'CLOTH'

								try: self.map.get_tile_properties(x, y, i).objects
								except: pass

								if t.startswith('BACKGROUND'):
									if len(self.tilmap[int(t[10])]) < a + 1:
										self.tilmap[int(t[10])].append(pygame.Surface((self.map.width * self.map.tilewidth,self.map.height * self.map.tileheight), pygame.SRCALPHA, 32))
									self.tilmap[int(t[10])][a].blit(image, (x * self.map.tilewidth - self.cam.x, y * self.map.tileheight - self.cam.y))
								elif t not in ['CARRY','HOLD','HIDEON','HIDEOFF']: self.tilmap[i][a].blit(image, (x * self.map.tilewidth - self.cam.x, y * self.map.tileheight - self.cam.y))

								if i < 2 and a == 0:
									if t in ['CARRY','HOLD']: self.tilrect[2].append([t,pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight,self.map.tilewidth,self.map.tileheight),image])
									elif t == 'WALL': self.tilrect[3].append([t,pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight,self.map.tilewidth,self.map.tileheight)])
									#elif t == 'MIRROR': self.tilrect[4].append([t,pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight,self.map.tilewidth,self.map.tileheight)])
									elif t.startswith('BACKGROUND') == False: self.tilrect[i].append([t,pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight,self.map.tilewidth,self.map.tileheight)])
								else:
									if t.startswith('HIDE'): self.tilrect[4].append([t,pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight,int(self.map.tilewidth),int(self.map.tileheight))])
								self.loading()
						elif i == 0: self.tilrect[3].append(['WALL',pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight,self.map.tilewidth,self.map.tileheight)])
		for lyr in self.map.layers:
			#NPCS
			if lyr.name == 'NPC':
				for i in lyr:
					obj = self.map.get_object_by_name(i.name)
					npc = {'N': int(i.name[4:]), 'RECT': pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)), 'TYPE': 0, 'INDEX': '000000', 'WHO': '',
					'GIF': 0.0,'BLINK': 100,'HEAD': 'BLANKD_0000','SPRITE': 'STANDD_000','MOVE': 'fixed','DIRECTION': 3,'SPD': 0, 'PAUSE': 0,
					'JUMP': 0,'GRAVITY': -5,'TIME': 20,'FOLLOW': None,'FOLLEND': 0,'FOLLMOV': '','TALKING': False,'SWIM': None,'HOLD': None}

					add = False
					if obj.type == 'None': npc['TYPE'] = None; add = True
					elif obj.type.startswith('scene'): npc['TYPE'] = obj.type; add = True
					elif obj.type.startswith('if'):
						if resources.SCENE == int(obj.type[2:]): npc['TYPE'] = 0; add = True
					else: npc['TYPE'] = int(obj.type); add = True

					for pr in obj.properties.items():
						if pr[0] == 'INDEX':
							npc['INDEX'] = pr[1]
							npc['HEAD'] = 'BLANKD_' + pr[1][0:3] + pr[1][5]
							npc['SPRITE'] = 'STANDD_' + pr[1][3:6]
						if pr[0] == 'WHO': npc['WHO'] = pr[1]
						if pr[0] == 'DIRECTION': npc['DIRECTION'] = int(pr[1]); npc['MOVE'] = 'stand'
						if pr[0] == 'MOVE': npc['MOVE'] = pr[1]

					if add == True:
						self.npcs.append(npc)
						self.objects.append([2,int(i.name[4:]),int(obj.y)])
			#VEICHLES
			if lyr.name == 'VEHICLES':
				ind = 0
				for i in lyr:
					obj = self.map.get_object_by_name(i.name)
					vh = database.VEHICLES['moto_' + str(obj.type)].copy()
					vh['RECT'] = pygame.Rect(float(obj.x), float(obj.y), 60, 10)
					vh['INDEX'] = int(obj.type)
					vh['N'] = ind
					self.vehicles.append(vh)
					self.objects.append([3,ind,int(obj.y)])
					ind += 1
			#PORTALS
			if lyr.name == 'PORTAL':
				ind = 0
				for i in lyr:
					obj = self.map.get_object_by_name(i.name)
					dt = {'N': ind, 'RECT': pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height)), 'TYPE': int(obj.type), 'PX': obj.properties['PX'], 'PY': obj.properties['PY'], 'MAP': obj.properties['MAP']}
					if obj.properties['TIME'].startswith('key'):
						dt['OPENING'] = obj.properties['TIME'][0:3]; dt['CLOSURE'] = obj.properties['TIME'][3:7]
					elif obj.properties['TIME'] != 'none':
						dt['OPENING'] = [int(obj.properties['TIME'][0:2]),int(obj.properties['TIME'][2:4])]; dt['CLOSURE'] = [int(obj.properties['TIME'][4:6]),int(obj.properties['TIME'][6:8])]
					else:
						dt['OPENING'] = None; dt['CLOSURE'] = None
					if len(obj.properties) > 4: dt['MUSIC'] = obj.properties['MUSIC']
					else: dt['MUSIC'] = None
					self.portals.append(dt)
					self.objects.append([4,ind,int(obj.y)])
					ind += 1
			#SIGNS
			if lyr.name == 'SIGNS':
				ind = 0
				for i in lyr:
					obj = self.map.get_object_by_name(i.name)
					self.signs.append({'N': ind, 'RECT': pygame.Rect(int(obj.x), int(obj.y), len(obj.type) * 10, int(obj.height)), 'TEXT': obj.type})
					self.objects.append([5,ind,int(obj.y)])
					ind += 1
			#LIGHTS
			if lyr.name == 'LIGHTS':
				ind = 0
				for i in lyr:
					obj = self.map.get_object_by_name(i.name)
					img = pygame.Surface((int(obj.width),int(obj.height)),pygame.SRCALPHA)
					for r in range(math.floor(obj.height/2)):
						srf = pygame.Surface((obj.width,obj.height),pygame.SRCALPHA)
						pygame.draw.circle(srf, (255, 255, 255, r), (math.floor(obj.width/2),math.floor(obj.height/2)), r)
						#pygame.draw.ellipse(srf, (255, 208, 0, r * 2), pygame.Rect(r,r,int(obj.width/2) - r,int(obj.height/2) - r),1)
						img.blit(srf,(0,0))
					self.lights.append({'N': ind, 'TYPE': obj.type, 'IMAGE': img, 'RECT': pygame.Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height))})
					self.objects.append([6,ind,self.map.height * self.map.tileheight])
					ind += 1
			self.loading()

		#ENEMIES
		for prp in self.map.properties.items():
			if prp[0] == 'ENEMIES':
				for i in self.map.properties['ENEMIES']:
					if i == '-': lst.append(self.map.properties['ENEMIES'][st:en]); st += en + 1
					en += 1
				for i in range(round(random.randint(3,10))):
					wh = lst[round(random.randint(0,len(lst) - 1))]
					self.en.append(database.FREAKS[wh].copy())
					self.en[i]['FILE'] = wh
					self.en[i]['SPRITE'] = pygame.image.load('Sprites/frk_' + (self.en[i]['FILE']) + '_stand.png')
					siz = pygame.image.load('Sprites/frk_' + self.en[i]['FILE'] + '_mini.png').get_rect()
					self.en[i]['RECT'] = pygame.Rect(self.tilrect[round(random.randint(0, len(self.tilrect[0])))][1].x,self.tilrect[round(random.randint(0, len(self.tilrect[0])))][1].y,siz.width,siz.height)
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
			elif prp[0] == 'SIGNAL':
				self.signal = self.map.properties['SIGNAL']

		self.loadingif = None

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
							self.display.blit(resources.SPRITES['EFFECT_' + str(i['HEALTH'])][math.floor(i['EFFECT'])], (i['MASK'].x + 5, i['MASK'].y - 10))
							i['EFFECT'] += 0.5
							if i['EFFECT'] >= len(resources.SPRITES['EFFECT_' + str(i['HEALTH'])]): i['EFFECT'] = 0.0
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

				while p < len(resources.PARTY[resources.FORMATION]):
					if p == self.turn:
						pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(p * 120,0,120,100))
						self.display.blit(self.mininfo.render(resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['NAME'].lower(), True, (0,0,0)), (10 + p * 120, 10))
					else: 
						self.display.blit(self.mininfo.render(resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['NAME'].lower(), True, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2])), (10 + p * 120, 10))

					#LIFE BAR
					pygame.draw.rect(self.display, (10, 10, 10), pygame.Rect(10 + p * 120,40,100,20))
					if resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HP'] > 0:
						minush = int(98/(resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['LEVEL']]/resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HP']))
					else: minush = 0
					if self.barhp[p] > minush:
						self.ch_sfx.play(resources.SOUND['HP_LOSS'])
						self.barhp[p] -= 1
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(11 + p * 120,41,98,18))
					if resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HP'] > resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['LEVEL']]/5: hpcol = (0, 255, 0)
					elif resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HP'] > 0:
						hpcol = (255, 0, 0)
						low = True
					else: hpcol = (255, 0, 0)
					if low == True:
						if self.ch_ton.get_busy() == False: self.ch_ton.play(resources.SOUND['HP_LOW'])
					if self.barhp[p] > 0: pygame.draw.rect(self.display, (255,255,0), pygame.Rect(11 + p * 120,41,self.barhp[p],18))
					if resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HP'] > 0:
						pygame.draw.rect(self.display, hpcol, pygame.Rect(11 + p * 120,41,int(98/(resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['LEVEL']]/resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HP'])),18))
					if resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HEALTH'] > 1:
						self.display.blit(pygame.image.load('Sprites/hl_' + str(resources.CHARACTERS[resources.PARTY[resources.FORMATION][p]]['HEALTH']) + '.png'), (14 + p * 120, 44))

					#AMMO BAR
					if self.equip[p] < 4:
						if int(database.INVENTORY[resources.PARTY[resources.FORMATION][p]][4][self.equip[p] + 1][1]) > 0:
							minush = int(98/(database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][p]][4][self.equip[p] + 1][0]][5]['CAPACITY']/int(database.INVENTORY[resources.PARTY[resources.FORMATION][p]][4][self.equip[p] + 1][1])))
						else: minush = 0
						if self.barpp[p][self.equip[p]] > minush:
							self.barpp[p][self.equip[p]] -= 1
						pygame.draw.rect(self.display, (10, 10, 10), pygame.Rect(10 + p * 120,70,100,20))
						pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(11 + p * 120,71,98,18))
						pygame.draw.rect(self.display, (0, 100, 255), pygame.Rect(11 + p * 120,71,self.barpp[p][self.equip[p]],18))
					p += 1

				if self.turn < len(resources.PARTY[resources.FORMATION]) and self.turn >= 0:
					#TIME BAR:
					pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(0,302,int(600/(100/self.btime)),10))
					if ce > 0 and self.mnu < 3 and self.turn < len(self.fig): self.btime -= 0.5
					if self.btime == 0:
						self.turn = len(self.fig)
						self.fight()

					#OPTIONS
					if self.mnu == 1:
						x = 0
						for i in database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][1:]:
							if self.equip[self.turn] == x: pygame.draw.rect(self.display, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(118 + x * 35,338,32,32))
							else: pygame.draw.rect(self.display, (255,255,255), pygame.Rect(118 + x * 35,338,32,32))
							pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(120 + x * 35,340,28,28))
							if database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][x + 1][0] != '_':
								self.display.blit(pygame.image.load('Sprites/Items/it_' + database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][x + 1][0] + '.png'), (120 + x * 35, 340))
							x += 1

						if self.equip[self.turn] == 4: pygame.draw.rect(self.display, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(304,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(304,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_tactical.png'), (304, 338))

						if self.equip[self.turn] == 5: pygame.draw.rect(self.display, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(339,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(339,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_talk.png'), (339, 338))

						if self.equip[self.turn] == 6: pygame.draw.rect(self.display, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(374,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(374,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_guard.png'), (374, 338))

						if self.equip[self.turn] == 7: pygame.draw.rect(self.display, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(409,338,30,30))
						else: pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(409,338,30,30))
						self.display.blit(pygame.image.load('Sprites/e_run.png'), (409, 338))

						self.display.blit(pygame.image.load('Sprites/e_invphn.png'), (442, 338))

					#AIM BAR
					elif self.mnu == 2:
						if self.equip[self.turn] < 4:
							if resources.CHARACTERS[resources.PARTY[resources.FORMATION][self.turn]]['HEALTH'] == 9:
								prb = random.randint(0,10)
								if prb > 5: self.aim.x += round(random.randint(30,60))
								if prb < 5: self.aim.x -= round(random.randint(30,60))
							else: self.aim.x += 20 - self.pagi[self.turn]
							if self.aim.x > 500 - self.patt[self.turn]:
								self.aim.x = 100 + self.patt[self.turn]
							chk = False
							for i in database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][1:]:
								if i.startswith('aim') == True: chk = True; break
							if chk == True:
								self.display.blit(pygame.image.load('Sprites/aim_' + str(database.ITEMS[i][5]) + '.png'), (self.aim.x - 15, self.aim.y))
							else:
								self.display.blit(pygame.image.load('Sprites/aim_0.png'), (self.aim.x-15, self.aim.y))
							self.display.blit(pygame.image.load('Sprites/' + database.INVENTORY[resources.PARTY[resources.FORMATION][self.turn]][4][self.equip[self.turn] + 1][0] + '.png'), (150 + int(self.aim.x/2), 255))

					#TACTICS
						elif self.equip[self.turn] == 4:
							x = 0
							for i in resources.TACTICAL:
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
				self.display.blit(resources.SPRITES['ATTACKIMATION_' + str(self.effttack)][math.floor(self.effgif)], (200,200))

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

					for i in range(len(resources.PARTY[resources.FORMATION])):
						self.display.blit(pygame.image.load('Sprites/who_' + str(resources.PARTY[resources.FORMATION][i]) + '.png'), (100 + self.mnu, 120 + i * 30))
						pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(130 + self.mnu,120 + i * 30,100,20))
						if self.barxp[i] > 0: pygame.draw.rect(self.display, (0, 255, 100), pygame.Rect(130 + self.mnu,120 + i * 30,self.barxp[i],20))

					self.display.blit(self.mininfo.render(resources.CHARACTERS[0]['NAME'].lower(), True, (255,255,255)), (800 + self.mnu * 2, 70))
					self.display.blit(self.monotype.render(database.BATTLE[14] + str(resources.CHARACTERS[0]['LEVEL']) + ' !', True, (255,255,255)), (800 + self.mnu * 2, 100))
					self.display.blit(self.mininfo.render(database.BATTLE[39] + ' +' + str(resources.CHARACTERS[0]['STRENGHT'][resources.CHARACTERS[0]['LEVEL']] - resources.CHARACTERS[0]['STRENGHT'][resources.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 200))
					self.display.blit(self.mininfo.render(database.BATTLE[40] + ' +' + str(resources.CHARACTERS[0]['ATTACK'][resources.CHARACTERS[0]['LEVEL']] - resources.CHARACTERS[0]['ATTACK'][resources.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 230))
					self.display.blit(self.mininfo.render(database.BATTLE[41] + ' +' + str(resources.CHARACTERS[0]['AGILITY'][resources.CHARACTERS[0]['LEVEL']] - resources.CHARACTERS[0]['AGILITY'][resources.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 260))
					self.display.blit(self.mininfo.render(database.BATTLE[42] + ' +' + str(resources.CHARACTERS[0]['RESISTANCE'][resources.CHARACTERS[0]['LEVEL']] - resources.CHARACTERS[0]['RESISTANCE'][resources.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 290))
					self.display.blit(self.mininfo.render(database.BATTLE[43] + ' +' + str(resources.CHARACTERS[0]['VITALITY'][resources.CHARACTERS[0]['LEVEL']] - resources.CHARACTERS[0]['VITALITY'][resources.CHARACTERS[0]['LEVEL'] - 1]), True, (255,255,255)), (900 + self.mnu * 2, 320))

				elif self.turn == -5:
					self.display.blit(self.mininfo.render(database.BATTLE[8], True, (255,255,255)), (200 + self.mnu, 70))
					self.display.blit(self.monotype.render('-$' + str(resources.MONEY), True, (255,255,255)), (200 + self.mnu, 120))

		elif self.battle == False:
			#TILED MAP
			if len(self.tilmap[3]) > 0: self.display.blit(self.tilmap[3][math.floor(self.tilemation)], (0, 0))
			if len(self.tilmap[4]) > 0: self.display.blit(self.tilmap[4][math.floor(self.tilemation)], (-math.floor(self.cam.x/5), -math.floor(self.cam.y/5)))
			if len(self.tilmap[5]) > 0: self.display.blit(self.tilmap[5][math.floor(self.tilemation)], (-math.floor(self.cam.x/2), -math.floor(self.cam.y/2)))
			self.display.blit(self.tilmap[0][math.floor(self.tilemation)], (-self.cam.x, -self.cam.y))
			self.display.blit(self.tilmap[1][math.floor(self.tilemation)], (-self.cam.x, -self.cam.y))
			for i in self.tilrect[2]: self.display.blit(i[2], (i[1].x - self.cam.x, i[1].y - self.cam.y))

			'''for i in self.tilrect[4]:
				srf = pygame.Surface((20,20))
				srf.blit(self.display,(-i[1].x,-i[1].y))
				self.display.blit(srf,(i[1].x + 6,i[1].y + 6))'''

			#TILEMATION
			if self.player[0]['PAUSE'] < 2: self.tilemation += 0.1
			if self.tilemation >= 2.0: self.tilemation = 0.0

			#DEPTH
			dpth = 0
			for i in range(len(self.objects)):
				if i!= len(self.objects) - 1:
					if self.objects[i][2] > self.objects[i + 1][2]:
						self.objects.insert(i, self.objects[i + 1])
						del self.objects[i + 2]

			for y in self.objects:
				if y[0] == 0:
					if self.rectdebug == True: pygame.draw.rect(self.display, (0,0,255), pygame.Rect(i['RECT'].x - self.cam.x, i['RECT'].y - self.cam.y, i['RECT'].width, i['RECT'].height))
					#PLAYER
					for i in self.player:
						self.people(i,True)
						#CONDITIONS
						if resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HEALTH'] > 1:
							if resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SHK'] == 0:
								pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(i['RECT'].x - self.cam.x + 10 + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SHK'],i['RECT'].y - self.cam.y - 40,16,13))
							else: pygame.draw.rect(self.display, (255,10,10), pygame.Rect(i['RECT'].x - self.cam.x + 10 + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SHK'],i['RECT'].y - self.cam.y - 40,16,13))
							self.display.blit(pygame.image.load('Sprites/hl_' + str(resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HEALTH']) + '.png'), (i['RECT'].x - self.cam.x + 10 + resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['SHK'],i['RECT'].y - self.cam.y - 40))

						y[2] = i['RECT'].y

						#TILE COLISION
						if i['STEP'] > 0: i['STEP'] -= 1
						elif i['STEP'] == 0 and resources.MAP > 0:
							for t in range(2):
								for tr in self.tilrect[t]:
									if self.colide(i['RECT'],tr[1]) and i['SPD'] > 0 and self.dlgfa > 0 and i['PAUSE'] == 0:
										if self.driving == 0:
											if tr[0].startswith('JUMP') and i['DIRECTION'] == int(tr[0][4]) and i['GRAVITY'] == -5:
												i['GRAVITY'] = 4.5
												i['STEP'] = 0
												self.ch_sfx.play(resources.SOUND['FALL'])
											elif tr[0] != 'WALL' and tr[0] != 'NONE'  and tr[0].startswith('JUMP') == False and i['JUMP'] == 0:
												self.ch_stp.stop()
												self.ch_stp.play(resources.SOUND['STEP_' + tr[0]])
												if tr[0] == 'WATER':
													if i['SWIM'] == None: i['SWIM'] = 0.0
												else: i['SWIM'] = None
										elif tr[0] != 'WALL' and tr[0].startswith('JUMP') == False and i['JUMP'] == 0:
											self.ch_stp.stop()
											self.ch_stp.play(resources.SOUND['STEP_VEHICLE'])
										i['STEP'] = math.floor(40/i['SPD'])
				#OBJECTS
				if y[0] == 1:
					for i in range(len(self.en)):
						if self.en[i]['HP'] > 0 and i == y[1]: self.enemy(i)
				elif y[0] == 2:
					for i in self.npcs:
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
								if resources.MAP != 0:
									pygame.draw.rect(self.display, (250, 250, 250), pygame.Rect(i['RECT'].x - self.cam.x, i['RECT'].y - self.cam.y, i['RECT'].width, i['RECT'].height))
									self.display.blit(self.monotype.render(database.SIGNS[i['TEXT']], True, (0,0,0)), (i['RECT'].x - self.cam.x,i['RECT'].y - self.cam.y))
								else: self.display.blit(self.monotype.render(i['TEXT'], True, (250,250,250)), (i['RECT'].x - self.cam.x - math.floor(self.cam.x/5),i['RECT'].y - self.cam.y - math.floor(self.cam.y/5)))
							y[2] = i['RECT'].y

			#OVER TILES & CLOUDS
			if resources.MAP > 0:
				self.display.blit(self.tilmap[2][math.floor(self.tilemation)], (-self.cam.x, -self.cam.y))
			else:
				self.bbm += 0.2
				if math.floor(self.bbm) > (self.map.width * self.map.tilewidth): self.bbm = 0.0
				self.display.blit(self.tilmap[2][math.floor(self.tilemation)], (math.floor(self.bbm) - self.cam.x, -self.cam.y))
				self.display.blit(self.tilmap[2][math.floor(self.tilemation)], (math.floor(self.bbm) - (self.map.width * self.map.tilewidth) - self.cam.x, -self.cam.y))
			'''for t in self.tilrect[4 + math.floor(self.tilemation)]:
				if self.colide(t[1],self.cam): self.display.blit(t[2], (t[1].x - self.cam.x, t[1].y - self.cam.y))'''

			#DAYTIME & WEATHER
			if resources.TIME[0] > 18: tim = 100
			elif resources.TIME[0] > 6: tim = 0
			else: tim = 100
			srf = pygame.Surface((self.displayzw,self.displayzh))
			srf.set_alpha(tim)
			srf.fill((0, 58, 160))
			if self.map.properties['INTERIOR'] == '0': self.display.blit(srf, (0,0))
			if len(self.tilmap[6]) > 0: self.display.blit(self.tilmap[6][math.floor(self.tilemation)], (0, 0))

			#LIGHTS
			for y in self.objects:
				if y[0] == 6:
					for i in self.lights:
						if i['N'] == y[1]:
							if self.colide(i['RECT'], self.cam):
								self.display.blit(i['IMAGE'], (i['RECT'].x - self.cam.x,i['RECT'].y - self.cam.y))
			#RAIN
			if self.map.properties['INTERIOR'] == '0' and resources.WEATHER == 1:
				for i in range(3): self.particles.append({'X': round(random.randint(self.cam.x,self.cam.x + self.cam.width)), 'Y': self.cam.y - int(self.cam.height/2), 'RADIUS': 2, 'DIRECTION': 90, 'SPEED': 20})
				if len(self.particles) > 0:
					for p in range(len(self.particles)):
						if self.particles[p]['Y'] > self.cam.y + self.cam.height:
							del self.particles[p]; break
					for p in self.particles:
						p['X'] += int(math.cos(p['DIRECTION']) * p['SPEED'])
						p['Y'] += int(math.sin(p['DIRECTION']) * p['SPEED'])
						pygame.draw.rect(self.display, (10, 50, 255), (p['X'],p['Y'],p['RADIUS'],p['RADIUS']))

			#HIDE PLACES
			if self.tilhide == False and self.tilalpha > 0: self.tilalpha -= 20
			if self.tilhide == True and self.tilalpha < 255: self.tilalpha += 20
			if self.tilalpha < 0: self.tilalpha = 0
			if self.tilalpha > 255: self.tilalpha = 255
			al = 255 - self.tilalpha
			for i in self.tilrect[4]:
				srf = pygame.Surface((i[1].width,i[1].height))
				if i[0].endswith('ON'): srf.set_alpha(al); srf.fill((0,0,0)); self.display.blit(srf, (i[1].x - self.cam.x,i[1].y - self.cam.y))
				if i[0].endswith('OFF'): srf.set_alpha(self.tilalpha); srf.fill((0,0,0)); self.display.blit(srf, (i[1].x - self.cam.x,i[1].y - self.cam.y))

			#MINI MAP
			if resources.MINIMAP == True:
				try:
					pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,self.displayzh - (106 * int(self.displayzh/400)),106 * int(self.displayzw/600),106 * int(self.displayzh/400)))
					self.display.blit(self.minimap(resources.MAP, self.player[0]['RECT'].x, self.player[0]['RECT'].y, self.displayzw, self.displayzh, self.signal), (3 * int(self.displayzh/400),self.displayzh - (103 * int(self.displayzh/400))))
					self.display.blit(pygame.image.load('Sprites/mp_player.png'), (48 * int(self.displayzh/400),self.displayzh - (59 * int(self.displayzh/400))))
				except: pass

			#DRIVING BARS
			if self.driving > 0:
				pygame.draw.rect(self.display, (10,10,10), pygame.Rect(20,20,100,20))
				if resources.GAS >= 1: pygame.draw.rect(self.display, (255,155,66), pygame.Rect(20,20,int(100/(self.vehicles[self.driving - 1]['CAPACITY']/round(resources.GAS))),20))
				pygame.draw.rect(self.display, (10,10,10), pygame.Rect(20,42,100,20))
				if self.player[0]['SPD'] > 0: pygame.draw.rect(self.display, (0,255,0), pygame.Rect(20,42,int(100/(20/self.player[0]['SPD'])),20))

		#HEALTH DAMAGE
		for i in resources.PARTY[resources.FORMATION]:
			if resources.CHARACTERS[i]['HEALTH'] in [4,5,6,7,16,17,18,19,20,21] and self.dlgfa > 0:
				resources.CHARACTERS[i]['DMGTIM'] -= 1
				if resources.CHARACTERS[i]['DMGTIM'] == 0:
					resources.CHARACTERS[i]['DMGTIM'] = 100
					resources.CHARACTERS[i]['SHK'] = 3
					resources.CHARACTERS[i]['HP'] -= 1

					'''dth = 0
					for d in self.fig:
						if d['HP'] <= 0: dth += 1
					if dth == len(self.fig):'''
					if resources.CHARACTERS[i]['HP'] <= 0:
						resources.CHARACTERS[i]['HEALTH'] = 0
						self.ch_msc.fadeout(500)
						self.ch_ton.play(resources.SOUND['BATTLE_LOST'])
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
						resources.PX = 315
						resources.PY = 200
						resources.MONEY -= 100 * len(resources.PARTY[resources.FORMATION])
						for w in resources.PARTY[resources.FORMATION]:
							resources.CHARACTERS[w]['HP'] = resources.CHARACTERS[w]['VITALITY'][resources.CHARACTERS[w]['LEVEL']]
							resources.CHARACTERS[w]['HEALTH'] = 0
						self.__init__()
						self.rendermap('hospital_0')
						self.transiction(False, 0)

					self.ch_ton.play(resources.SOUND['DAMAGE_1'])
				if resources.CHARACTERS[i]['SHK'] > 0: resources.CHARACTERS[i]['SHK'] = -resources.CHARACTERS[i]['SHK']
				elif resources.CHARACTERS[i]['SHK'] < 0: resources.CHARACTERS[i]['SHK'] = -resources.CHARACTERS[i]['SHK'] - 1

		#BLACK BARS
		if self.battle == False and self.winbar > 0:
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

		#CITY NAME
		if self.cityname != '' and self.winbar >= 50:
			self.display.blit(self.monotype.render(database.CITIES[resources.MAP - 1], True, (250,250,250)), (420, 360))

		#PORTALGO
		if self.portalgo != {}:
			for i in self.portalgo:
				if i['RECT'].width == 24: self.display.blit(pygame.image.load('Sprites/door_01.png'), (i['RECT'].x - self.cam.x, i['RECT'].y - self.cam.y))
				if i['RECT'].width == 48: self.display.blit(pygame.image.load('Sprites/door_11.png'), (i['RECT'].x - self.cam.x, i['RECT'].y - self.cam.y))

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
			if self.phofa == 320: self.ch_sfx.play(resources.SOUND['PHONE_UNLOCK'])
			if self.phofa < 360: self.phofa += 40
		else:
			if self.phofa == 360: self.ch_sfx.play(resources.SOUND['PHONE_LOCK'])
			if self.phofa > 0: self.phofa -= 40
		if self.phofa == 360 and resources.BATTERY > 1.0:
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

		#NAMING & DEBUG
		if self.nmenu.show == True:
			self.display.blit(self.nmenu.run(), (200, 100))

		#RADIOPLAY
		if self.radonoff == True:
			pygame.draw.rect(self.display, (255, 0, 135), pygame.Rect(0,0,180,50))
			self.display.blit(self.monotype.render('Tocando:', True, (0, 0, 0)), (10, 5))
			self.display.blit(self.monotype.render(resources.RADIO[str(math.floor(self.fm/20))][self.msc][:-4], True, (0, 0, 0)), (10, 25))
		if pygame.mixer.music.get_busy() == False and self.radonoff == True:
			self.msc += 1
			if self.msc > len(resources.RADIO[str(round(self.fm/20))]) - 1: self.msc = 0
			if resources.RADIO[str(round(self.fm/20))] != []:
				pygame.mixer.music.load('Songs/FM_' + str(round(self.fm/20)) + '/' + resources.RADIO[str(round(self.fm/20))][self.msc])
				pygame.mixer.music.play()

		#DIALOG
		if self.dlgfa < 500 and resources.SCENE != -1 and self.nmenu.show == False:
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
							pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(20,225 - self.dlgy,5 + lng,5))
							pygame.draw.polygon(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), ((25,225 - self.dlgy),(45,225 - self.dlgy),(25,235 - self.dlgy)))
							pygame.draw.polygon(self.display, (0, 0, 0), ((25,221 - self.dlgy),(45,221 - self.dlgy),(25,231 - self.dlgy)))
						else:
							if self.lopt == opt:
								pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(578 - lng,200 - self.dlgy,5 + lng,25))
								pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(578 - lng,225 - self.dlgy,5 + lng,5))
								pygame.draw.polygon(self.display, (0, 0, 0), ((558,225 - self.dlgy),(578,225 - self.dlgy),(578,235 - self.dlgy)))
								pygame.draw.polygon(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), ((558,221 - self.dlgy),(578,221 - self.dlgy),(578,231 - self.dlgy)))
							else:
								pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(578 - lng,200 - self.dlgy,5 + lng,25))
								pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(578 - lng,225 - self.dlgy,5 + lng,5))
								pygame.draw.polygon(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), ((558,225 - self.dlgy),(578,225 - self.dlgy),(578,235 - self.dlgy)))
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
				if resources.MORALITY > 0:
					pygame.draw.rect(self.display, (255,255,0), pygame.Rect(-90 + self.notx,45,int(70/(10/resources.MORALITY)),20))
				if resources.MORALITY < 0:
					pygame.draw.rect(self.display, (175,0,0), pygame.Rect(-int(70/(10/resources.MORALITY)) - 160 + self.notx,45,int(70/(10/resources.MORALITY)),20))
				pygame.draw.line(self.display, (255,255,255), (-90 + self.notx,42),(-90 + self.notx,68),2)

		#TUTORIALS
		if self.tutorial['OUTPUT'] != []:
			nxt = False
			if self.tutorial['GO'] > 0 and self.phone == self.tutorial['GO']: self.tutorial['TIME'] = self.tutorial['WAIT']; nxt = True

			if self.tutorial['TIME'] < self.tutorial['WAIT']:
				if self.tutorial['FADE'] < 200: self.tutorial['FADE'] += 20
			elif self.tutorial['TIME'] >= self.tutorial['WAIT']: nxt = True
			if nxt == True:
				if self.tutorial['NEXT'] != '':
					self.tutorial = {'TEXT': database.TUTORIALS[self.tutorial['NEXT']].copy(), 'OUTPUT': [], 'FADE': 200, 'TIME': 0, 'WAIT': 300, 'NEXT': '','GO': 0}
					for j in self.tutorial['TEXT']:
						if isinstance(j,list):
							if j[0] == 'phone':
								self.tutorial['GO'] = j[1]
								if len(j) > 2: self.tutorial['NEXT'] = j[2]
							if j[0] == 'wait':
								self.tutorial['WAIT'] = j[1]
								if len(j) > 2: self.tutorial['NEXT'] = j[2]
							if j[0] == 'image':
								self.tutorial['OUTPUT'].append(j)
						else: self.tutorial['OUTPUT'].append(j)
				else:
					self.tutorial['GO'] = 0
					if self.tutorial['FADE'] > 0: self.tutorial['FADE'] -= 10
					else: self.tutorial['OUTPUT'] = []

			if self.tutorial['GO'] == 0: self.tutorial['TIME'] += 1
			pygame.draw.rect(self.display, (250,250,250), pygame.Rect(578 - self.tutorial['FADE'],18,self.tutorial['FADE'] + 4,int(self.tutorial['FADE']/2) + 4))
			pygame.draw.rect(self.display, (10,10,10), pygame.Rect(580 - self.tutorial['FADE'],20,self.tutorial['FADE'],int(self.tutorial['FADE']/2)))
			if self.tutorial['FADE'] == 200:
				x = 0
				y = 0
				sid = 0
				end = 0
				ky = [resources.UP[0],resources.DOWN[0],resources.LEFT[0],resources.RIGHT[0],resources.ACT[0],resources.RUN[0],resources.BAG[0],resources.PHONE[0]]
				for j in self.tutorial['OUTPUT']:
					if isinstance(j,str): self.display.blit(self.monotype.render(j, True, (250, 250, 250)), (385 + x,25 + y))
					elif isinstance(j,list) and j[0] == 'image': self.display.blit(pygame.image.load('Sprites/' + j[1] + '.png'), (520 + x,25 + y))
					elif j == 0:
						for i in range(end): sid += 1
						x = 0
						y += 20
					else:
						if ky[j - 1] == pygame.K_LSHIFT: out = 'À'
						elif ky[j - 1] == pygame.K_RSHIFT: out = 'À'
						elif ky[j - 1] == pygame.K_LCTRL: out = 'Á'
						elif ky[j - 1] == pygame.K_RCTRL: out = 'Á'
						elif ky[j - 1] == pygame.K_LALT: out = 'Â'
						elif ky[j - 1] == pygame.K_RALT: out = 'Â'
						elif ky[j - 1] == pygame.K_BACKSPACE: out = 'Ã'
						elif ky[j - 1] == pygame.K_RETURN: out = 'Ä'
						elif ky[j - 1] == pygame.K_UP: out = 'È'
						elif ky[j - 1] == pygame.K_LEFT: out = 'É'
						elif ky[j - 1] == pygame.K_DOWN: out = 'Ê'
						elif ky[j - 1] == pygame.K_RIGHT: out = 'Ë'
						else: out = pygame.key.name(ky[j - 1]).upper()
						self.display.blit(self.controlkeys.render(out, True, (250, 250, 250)), (385 + x,30 + y))
						for l in self.tutorial['OUTPUT'][sid:end]:
							if l in ['m','w','M','Q','T','U','V','W','Y','?']: x += 8
							elif l in ['f','r']: x += 6
							elif l in ['J']: x += 5
							elif l in ['l']: x += 4
							elif l in ['i','I','!','.',',']: x += 2
							else: x += 7
					end += 1

		#CHAPTER NAME
		if resources.SCENE == -1:
			'''arr = pygame.surfarray.pixels3d(self.display)
			arr[:,:,0] = 255
			arr[:,:,1] -= 50
			arr[:,:,2] -= 50'''
			srf = pygame.Surface((self.displayzw,self.displayzh))
			srf.set_alpha(200)
			srf.fill((221, 0, 0))
			self.display.blit(srf, (0,0))
			pygame.draw.rect(self.display, (250,250,250), pygame.Rect(0,160,600,80))
			self.display.blit(self.mininfo.render(database.CHAPTERS[resources.CHAPTER][0].lower(), True, (10, 10, 10)), (10, 200))
			pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(0,167,600,3))
			pygame.draw.rect(self.display, (10,10,10), pygame.Rect(0,170,600,22))
			pygame.draw.rect(self.display, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(0,192,600,3))
			self.display.blit(self.monotype.render(database.CHAPTERS[resources.CHAPTER][1], True, (250, 250, 250)), (10, 170))

		#CAMERA
		if (self.map.width * self.map.tilewidth) > self.displayzw:
			if self.speakin == 0: self.cam.x += int((self.player[0]['RECT'].x  - self.cam.x - self.displayzw/2)/15)
			else: self.cam.x += int((self.speakin.x  - self.cam.x - self.displayzw/2)/15)

			if self.cam.x < 0: self.cam.x = 0
			if self.cam.x > (self.map.width * self.map.tilewidth) - self.displayzw: self.cam.x = (self.map.width * self.map.tilewidth) - self.displayzw
		else: self.cam.x = -int((self.displayzw - (self.map.width * self.map.tilewidth))/2)

		if (self.map.height * self.map.tileheight) > self.displayzh:
			if self.speakin == 0: self.cam.y += int((self.player[0]['RECT'].y  - self.cam.y - self.displayzh/2)/15)
			else: self.cam.y += int((self.speakin.y  - self.cam.y - self.displayzh/2)/15)

			if self.cam.y < 0: self.cam.y = 0
			if self.cam.y > (self.map.height * self.map.tileheight) - self.displayzh: self.cam.y = (self.map.height * self.map.tileheight) - self.displayzh
		else: self.cam.y = -int((self.displayzh - (self.map.height * self.map.tileheight))/2)

		if pygame.display.get_active():
			if self.ch_msc.get_busy() == False: self.ch_msc.unpause()
			if self.ch_rad.get_busy() == False: self.ch_rad.unpause()
			if self.ch_rng.get_busy() == False: self.ch_rng.unpause()
			self.screen.blit(pygame.transform.scale(self.display, (self.windoww, self.windowh)), (self.displayx, self.displayy))
			pygame.display.flip()
		else:
			self.ch_msc.pause()
			self.ch_rad.pause()
			self.ch_rng.pause()

	def loading(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		self.screen.fill((0,0,0),pygame.Rect(1120,720,30,30))
		if self.loadingif != None:
			self.loadingif += 0.01
			if str(self.loadingif)[2] == '0': upd = True
			else: upd = False
			if self.loadingif >= 8.0: self.loadingif = 0.0
		if upd == True:
			self.screen.blit(pygame.image.load('Sprites/loading_' + str(math.floor(self.loadingif)) + '.png'), (1120, 720))
			pygame.display.update(pygame.Rect(1120,720,30,30))

	def run(self):
		if self.FPS > 0: self.glock.tick(self.FPS)
		if self.nmenu.show == False:
			self.events()
		self.draw()

		#DATETIME
		if self.sleepin == False:
			resources.TIME[2] += 1
			for i in resources.PARTY[resources.FORMATION]:
				ph = self.inv.find(i,'phone')
				if ph != None:
					bt = float(ph[1][0:3])
					bt -= 0.05
			if self.phone > 0:
				if resources.CHAPTER > 0: resources.BATTERY -= 0.05
				elif resources.SCENE > 0: resources.BATTERY -= 0.05
		else:
			resources.TIME[1] += 5
			resources.BATTERY -= 2.5

		if resources.BATTERY < 1.0:
			if self.radonoff == True:
				self.radonoff = False
				self.ch_ton.stop()
				pygame.mixer.music.stop()
			resources.BATTERY = 1.0
		if resources.TIME[2] >= 60:
			resources.TIME[1] += 1
			resources.TIME[2] = 0

		if resources.TIME[1] >= 60:
			resources.TIME[0] += 1
			resources.TIME[1] = 0

			for p in resources.PARTY[resources.FORMATION]:
				if resources.CHARACTERS[p]['HUNGER'] == 0: resources.CHARACTERS[p]['HEALTH'] = 6
				else: resources.CHARACTERS[p]['HUNGER'] -= 1
				if resources.CHARACTERS[p]['THIRST'] == 0: resources.CHARACTERS[p]['HEALTH'] = 7
				else: resources.CHARACTERS[p]['THIRST'] -= 1
				if resources.CHARACTERS[p]['SLEEP'] == 0: resources.CHARACTERS[p]['HEALTH'] = 8
				else: resources.CHARACTERS[p]['SLEEP'] -= 1
			print(resources.CHARACTERS[1]['HUNGER'])
			print(resources.CHARACTERS[1]['THIRST'])
			print(resources.CHARACTERS[1]['SLEEP'])


		if resources.TIME[0] >= 24:
			resources.DATE[0] += 1
			resources.DATE[3] += 1
			resources.TIME[0] = 0

		if resources.DATE[0] >= 30:
			resources.DATE[1] += 1
			resources.DATE[0] = 1

		if resources.DATE[1] >= 12:
			resources.DATE[2] += 1
			resources.DATE[1] = 1

		if resources.DATE[3] > 7:
			resources.DATE[3] = 1

		#WAITIME
		for i in range(len(self.waitime)):
			if self.waitime[i][1] <= resources.TIME[0] and self.waitime[i][2] <= resources.TIME[1] and self.dlgfa > 0 and self.battle == False:
				if self.waitime[i][0] == 'sun':
					resources.WEATHER = 0
					tm = resources.TIME[1] + 5
					hm = resources.TIME[0]
					if tm > 60: tm -= 60; hm += 1
					self.waitime.append(['rain',hm,tm])
				elif self.waitime[i][0] == 'rain':
					resources.WEATHER = 1
					tm = resources.TIME[1] + 5
					hm = resources.TIME[0]
					if tm > 60: tm -= 60; hm += 1
					self.waitime.append(['sun',hm,tm])
				elif self.waitime[i][0].startswith('repellent'):
					resources.CHARACTERS[int(self.waitime[i][0][9])]['HEALTH'] = 0
				elif self.waitime[i][0].startswith('cal'):
					self.ch_ton.play(resources.SOUND['CALLING'],-1)
					self.ch_rng.play(resources.SOUND['RINGTONE_' + str(self.phn.pbg)],-1)
					if self.radonoff == True: pygame.mixer.music.pause()
					if self.phone > 0: self.phone = 17
					self.nb = self.waitime[i][0][3:]
					tm = resources.TIME[1] + 5
					hm = resources.TIME[0]
					if tm > 60: tm -= 60; hm += 1
					self.waitime.append(['cutcal',hm,tm])
				elif self.waitime[i][0].startswith('cutcal'):
					if self.nb != '':
						self.ch_ton.stop()
						self.ch_rng.stop()
						self.nb = ''
						if self.phone == 17: self.phone = 1
				elif self.waitime[i][0].startswith('maicon'):
					self.npcs.append({'N': len(self.npcs), 'RECT': pygame.Rect(self.player[0]['RECT'].x - 20, self.player[0]['RECT'].y, 0, 0), 'TYPE': 4, 'INDEX': 0, 'WHO': 'MAICON', 'IMAGE': 0.0,'MOVE': 'fixed','DIRECTION': 3})
					self.objects.append([3,len(self.npcs),self.player[0]['RECT'].y])
				elif self.waitime[i][0].startswith('mercador'):
					self.npcs.append({'N': len(self.npcs), 'RECT': pygame.Rect(self.player[0]['RECT'].x - 20, self.player[0]['RECT'].y, 0, 0), 'TYPE': 3, 'INDEX': 0, 'WHO': 'MERCATOR', 'IMAGE': 0.0,'MOVE': 'fixed','DIRECTION': 3})
					self.objects.append([3,len(self.npcs),self.player[0]['RECT'].y])
				elif self.waitime[i][0].startswith('pizza'):
					self.npcs.append({'N': len(self.npcs), 'RECT': pygame.Rect(self.player[0]['RECT'].x - 20, self.player[0]['RECT'].y, 0, 0), 'TYPE': 0, 'WHO': self.waitime[i][0][9:].upper(), 'INDEX': 0,'IMAGE': 0.0,'MOVE': 'fixed','DIRECTION': 3})
					self.objects.append([3,len(self.npcs),self.player[0]['RECT'].y])
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
						if int(i[1][2:4]) <= resources.DATE[1]:
							if int(i[1][0:2]) <= resources.DATE[0]:
								i[0] += '_wasted' 

		resources.GAMETIME += self.glock.get_rawtime()

l = Loading()
while l.classrun == True: l.run()

t = Title()
while True:
	if resources.GAMETIME != 0:
		while t.classrun == True: t.run()
	else: resources.new_data()

	g = Game()
	if resources.GAMETIME > 0: g.transiction(False, 0)
	while g.classrun: g.run()
	resources.CHAPTER += 1
	t.msc.play(resources.SONGS['FATE_OCCURRENCES'],-1)
	t.classrun = True
	t.winbar = 50
	t.mnu = 5