# -*- coding: utf-8 -*-
import random
import pygame
import math
import sys
import resources
import os

if resources.FILES[3] != []:
	if resources.FILES[3][0] == 'PT': import database_PT as database
	if resources.FILES[3][0] == 'EN': import database_EN as database
else: import database_PT as database

class Debug:
	def __init__(self):
		self.scr = pygame.Surface((1200,50))
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 15)
		self.classrun = True
		self.cmd = ''
		self.goto = ''
		self.dlg = []

	def command(self):
		if self.cmd.startswith('goto'):
			self.goto = self.cmd[5:]
		if self.cmd.startswith('dialog -l'):
			self.dlg = database.DIALOGS[self.cmd[13:]][10:11]
		if self.cmd.startswith('dialog -n'):
			self.dlg = [self.cmd[10:]]
		if self.cmd.startswith('dialogs'):
			database.load_dialogs()
		if self.cmd.startswith('hp'):
			resources.CHARACTERS[int(cmd[3])]['HP'] = int(cmd[5])
		if self.cmd.startswith('hair'):
			resources.CHARACTERS[int(cmd[5])]['HAIR'] = cmd[7:]
		if self.cmd.startswith('costume'):
			resources.CHARACTERS[int(cmd[8])]['COSTUME'] = cmd[10:]
		if self.cmd.startswith('chapter'):
			resources.CHAPTER = int(cmd[8:])
		if self.cmd.startswith('money'):
			resources.MONEY = int(cmd[6:])
		if self.cmd.startswith('atm'):
			resources.ATM = int(cmd[4:])
		if self.cmd.startswith('credit'):
			resources.CREDIT = int(cmd[7:])
		if self.cmd.startswith('battery'):
			resources.BATTERY = int(cmd[8:])
		if self.cmd.startswith('time'):
			try: resources.TIME = [int(cmd[5:7]),int(cmd[7:9]),int(cmd[9:11])]
			except: print('Please, input time like XX-XX-XX')
		if self.cmd.startswith('date'):
			try: resources.DATE = [int(cmd[5:7]),int(cmd[7:9]),int(cmd[9:11]),int(cmd[11:13])]
			except: print('Please, input date like XX-XX-XX-XX')
		if self.cmd.startswith('party'):
			try: resources.PARTY[resources.FORMATION] = [int(cmd[6]),int(cmd[7]),int(cmd[8]),int(cmd[9])]
			except: print('Please, input party formation like "X-X-X-X"')
		if self.cmd == 'rect': self.rectdebug = not self.rectdebug
		if self.cmd == 'health':
			try: resources.CHARACTERS[resources.PARTY[resources.FORMATION][0]]['HEALTH'] = int(cmd[7:])
			except: print('Invalid health value')
		self.cmd = ''

	def draw(self):
		self.scr.fill((0,0,0))
		self.scr.blit(self.fnt.render(self.cmd,True,(250,250,250)),(10,10))
		return self.scr

	def run(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.classrun = False
				elif event.key == pygame.K_BACKSPACE:
					self.cmd = self.cmd[:-1]
				else: self.cmd += event.unicode

class Naming:
	def __init__(self):
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 15)
		self.ch_sfx = pygame.mixer.Channel(1)
		self.ch_ton = pygame.mixer.Channel(2)
		self.wdw = pygame.Surface((200, 200))
		pygame.draw.rect(self.wdw, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(0,0,200,200))
		for x in range(20):
			for y in range(20):
				self.wdw.blit(pygame.image.load('Sprites/border_' + str(resources.BORDER) + '.png'), (x * 10, y * 10))
		self.show = False
		self.scr = pygame.Surface((180,180))
		self.blink = 0.0
		self.bt = ''
		self.name = ['','','','','','']
		self.lame = ['','','','','','']
		self.ninput = True
		self.ind = 0
		self.lopt = 0
		self.did = 0
		self.tim = 3

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if self.ninput == True:
				if self.ind < 6:
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							if self.lopt == 0:
								if len(self.name[self.ind]) > 0: self.lopt = 1; self.ch_ton.play(resources.SOUND['MENU_GO'])
								else: self.ch_sfx.play(resources.SOUND['ERROR'])
							else:
								if len(self.lame[self.ind]) > 0: self.lopt = 0; self.ind += 1; self.ch_ton.play(resources.SOUND['TEXT_ENTER'])
								else: self.ch_sfx.play(resources.SOUND['ERROR'])
						elif event.key == pygame.K_BACKSPACE:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							if self.lopt == 0:
								if len(self.name[self.ind]) > 0: self.name[self.ind] = self.name[self.ind][:-1]
								elif self.ind > 0: self.ind -= 1; self.lopt = 0
							if self.lopt == 1:
								if len(self.lame[self.ind]) > 0: self.lame[self.ind] = self.lame[self.ind][:-1]
								else: self.lopt = 0
						else:
							self.ch_sfx.play(resources.SOUND['TEXT_INPUT'])
							if self.lopt == 0 and len(self.name[self.ind]) < 10: self.name[self.ind] += event.unicode
							if self.lopt == 1 and len(self.lame[self.ind]) < 10: self.lame[self.ind] += event.unicode
				else:
					self.pressed = pygame.key.get_pressed()
					if self.pressed[resources.LEFT]: self.lopt = 0; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.RIGHT]: self.lopt = 1; self.ch_sfx.play(resources.SOUND['MENU_HOR'])
					if self.pressed[resources.ACT]:
						if self.lopt == 0:
							self.ch_sfx.play(resources.SOUND['FILE_NEW'])
							for i in range(len(self.name)):
								resources.CHARACTERS[i]['NAME'] = self.name[i]
								resources.CHARACTERS[i]['LASTNAME'] = self.lame[i]
							resources.save_data()
							resources.save_sett()
							resources.char_entry()
							resources.party_make(0)
							self.show = False
						if self.lopt == 1:
							self.ch_sfx.play(resources.SOUND['MENU_BACK'])
							self.ind = 0
							self.lopt = 0

	def run(self):
		self.scr.fill((0,0,0))

		self.blink += 0.1
		if math.floor(self.blink) == 0: self.bt = ''
		elif math.floor(self.blink) == 1: self.bt = '.'
		else: self.blink = 0.0

		if self.ninput == False:
			resources.CHARACTERS[0]['NAME'] = database.NAMES[0]
			resources.CHARACTERS[0]['LASTNAME'] = database.NAMES[1]
			resources.CHARACTERS[1]['NAME'] = database.NAMES[2]
			resources.CHARACTERS[1]['LASTNAME'] = database.NAMES[3]
			resources.CHARACTERS[2]['NAME'] = database.NAMES[4]
			resources.CHARACTERS[2]['LASTNAME'] = database.NAMES[5]
			resources.CHARACTERS[3]['NAME'] = database.NAMES[6]
			resources.CHARACTERS[3]['LASTNAME'] = database.NAMES[7]
			resources.CHARACTERS[4]['NAME'] = database.NAMES[8]
			resources.CHARACTERS[4]['LASTNAME'] = database.NAMES[9]
			resources.CHARACTERS[5]['NAME'] = database.NAMES[10]
			resources.CHARACTERS[5]['LASTNAME'] = database.NAMES[11]
			if self.ind < 6:
				if self.lopt == 0:
					if self.tim != 0: self.tim -= 1
					else:
						if len(self.name[self.ind]) != len(resources.CHARACTERS[self.ind]['NAME']):
							self.name[self.ind] += resources.CHARACTERS[self.ind]['NAME'][self.did]
							self.ch_sfx.play(pygame.mixer.Sound('SFX/text_input.wav'))
							self.tim = 3
							self.did += 1
						else: self.ch_ton.play(pygame.mixer.Sound('SFX/menu_go.wav')); self.lopt = 1; self.tim = 3; self.did = 0
				if self.lopt == 1:
					if self.tim != 0: self.tim -= 1
					else:
						if len(self.lame[self.ind]) != len(resources.CHARACTERS[self.ind]['LASTNAME']):
							self.lame[self.ind] += resources.CHARACTERS[self.ind]['LASTNAME'][self.did]
							self.ch_sfx.play(pygame.mixer.Sound('SFX/text_input.wav'))
							self.tim = 3
							self.did += 1
						else: self.ch_ton.play(pygame.mixer.Sound('SFX/text_enter.wav')); self.ind += 1; self.lopt = 0; self.tim = 3; self.did = 0
			else:
				self.ch_sfx.play(pygame.mixer.Sound('SFX/file_new.wav'))
				resources.new_data()
				for i in range(len(self.name)):
					resources.CHARACTERS[i]['NAME'] = self.name[i]
					resources.CHARACTERS[i]['LASTNAME'] = self.lame[i]
				resources.save_data()
				resources.save_sett()
				resources.char_entry()
				resources.party_make(0)
				resources.recent_data(2)
				self.show = False
		
		if self.ind < 6:
			l1 = 0
			l2 = 0
			for l in database.MENU[80]:
				if l in ['m','w','M','Q','T','U','V','W','Y','?']: l1 += 8
				elif l in ['f','r']: l1 += 6
				elif l in ['J']: l1 += 5
				elif l in ['l']: l1 += 4
				elif l in ['i','I','!','.',',']: l1 += 2
				else: l1 += 7
			for l in database.MENU[81]:
				if l in ['m','w','M','Q','T','U','V','W','Y','?']: l2 += 8
				elif l in ['f','r']: l2 += 6
				elif l in ['J']: l2 += 5
				elif l in ['l']: l2 += 4
				elif l in ['i','I','!','.',',']: l2 += 2
				else: l2 += 7
			if self.lopt == 0: self.scr.blit(self.fnt.render(database.MENU[80] + ': ' + self.name[self.ind] + self.bt, True, (255, 255, 0)), (80 - l1, 30))
			else: self.scr.blit(self.fnt.render(database.MENU[80] + ': ' + self.name[self.ind], True, (255, 255, 255)), (80 - l1, 30))
			if self.lopt == 1: self.scr.blit(self.fnt.render(database.MENU[81] + ': '+ self.lame[self.ind] + self.bt, True, (255, 255, 0)), (80 - l2, 50))
			else: self.scr.blit(self.fnt.render(database.MENU[81] + ': '+ self.lame[self.ind], True, (255, 255, 255)), (80 - l2, 50))
		else:
			self.scr.blit(self.fnt.render(database.MENU[82], True, (255, 255, 255)), (50, 10))
			y = 0
			for i in range(len(self.name)):
				self.scr.blit(self.fnt.render(self.name[i] + ' ' + self.lame[i], True, (255, 255, 255)), (10, 30 + (20 * y)))
				y += 1

			if self.lopt == 0: self.scr.blit(self.fnt.render(database.MENU[83], True, (255, 255, 0)), (50, 160))
			else: self.scr.blit(self.fnt.render(database.MENU[83], True, (255, 255, 255)), (50, 160))
			if self.lopt == 1: self.scr.blit(self.fnt.render(database.MENU[84], True, (255, 255, 0)), (100, 160))
			else: self.scr.blit(self.fnt.render(database.MENU[84], True, (255, 255, 255)), (100, 160))


		self.wdw.blit(self.scr,(10,10))
		return self.wdw

class Inventory:
	def __init__(self):
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 10)
		self.wdw = pygame.Surface((400, 300))
		self.wdw.fill((resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]))
		for x in range(40):
			for y in range(30):
				self.wdw.blit(pygame.image.load('Sprites/border_' + str(resources.BORDER) + '.png'), (x * 10, y * 10))

		self.itbor = pygame.Surface((100, 40))
		self.itbor.fill((resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]))
		for x in range(10):
			for y in range(4):
				self.itbor.blit(pygame.image.load('Sprites/border_' + str(resources.BORDER) + '.png'), (1 + (x * 10),1 + (y * 10)))
		self.mnbor = pygame.Surface((60, 40))
		self.mnbor.fill((resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]))
		for x in range(6):
			for y in range(4):
				self.mnbor.blit(pygame.image.load('Sprites/border_' + str(resources.BORDER) + '.png'), (1 + (x * 10),1 + (y * 10)))

		self.scr = pygame.Surface((380,220))
		self.itmov = ''
		self.money = False
		self.scroll = 50
		self.shake = 0
		
	def show(self, opt, lopt, mn, ex):
		self.scr.fill((0,0,0))
		x = 10
		y = 45
		optx = 0
		opty = 0
		mnc = 0

		vlm = 0
		wei = 0

		if self.scroll < (mn * 200):
			self.scroll += 40
		if self.scroll > (mn * 200):
			self.scroll -= 40

		for n in resources.PARTY[resources.FORMATION]:
			self.scr.blit(self.fnt.render(resources.CHARACTERS[n]['NAME'], True, (255, 255, 255)), (10 + (200 * mnc) - self.scroll, 10))
			for j in range(len(database.INVENTORY[n])):
				if opty == 4: y += 5
				for i in database.INVENTORY[n][j]:
					if optx == 1: x += 5

					if optx > 0 and opty < 4:
						if database.INVENTORY[mnc][4][0][0] != '_':
							if opt == optx and lopt == opty and mn == mnc:
								pygame.draw.rect(self.scr, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(x + (200 * mnc) - self.scroll,y,30,30))
							else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(x + (200 * mnc) - self.scroll,y,30,30))
							if i[0] != '_':
								self.scr.blit(pygame.image.load('Sprites/Items/it_' + i[0] + '.png'), (x + (200 * mnc) - self.scroll, y))
								if optx > 0 and opty < 4:
									vlm += database.ITEMS[i[0]][3]
									wei += database.ITEMS[i[0]][4]
					else:
						if opt == optx and lopt == opty and mn == mnc:
							pygame.draw.rect(self.scr, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(x + (200 * mnc) - self.scroll,y,30,30))
						else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(x + (200 * mnc) - self.scroll,y,30,30))
						if i[0] != '_':
							self.scr.blit(pygame.image.load('Sprites/Items/it_' + i[0] + '.png'), (x + (200 * mnc) - self.scroll, y))
							if optx > 0 and opty < 4:
								vlm += database.ITEMS[i[0]][3]
								wei += database.ITEMS[i[0]][4]

					x += 32
					optx += 1
				x = 10
				y += 32
				optx = 0
				opty += 1

			self.scr.blit(self.fnt.render(database.MENU[78] + ':', True, (255, 255, 255)), (75 + 200 * mnc - self.scroll, 10))
			pygame.draw.rect(self.scr, (100, 100, 100), pygame.Rect(115 + (200 * mnc) - self.scroll,12,50,10))
			if vlm > 0 and database.INVENTORY[mnc][4][0][0] != '_': pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(115 + (200 * mnc) - self.scroll,12,int(50/(database.ITEMS[database.INVENTORY[mnc][4][0][0]][3]/vlm)),10))
			self.scr.blit(self.fnt.render(database.MENU[79] + ':', True, (255, 255, 255)), (75 + (200 * mnc) - self.scroll, 25))
			pygame.draw.rect(self.scr, (100, 100, 100), pygame.Rect(115 + (200 * mnc) - self.scroll,27,50,10))
			if wei > 0 and database.INVENTORY[mnc][4][0][0] != '_': pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(115 + (200 * mnc) - self.scroll,27,int(50/(database.ITEMS[database.INVENTORY[mnc][4][0][0]][4]/wei)),10))

			x = 10
			y = 45
			vlm = 0
			wei = 0
			optx = 0
			opty = 0
			mnc += 1
			#pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect((200 * mnc) - self.scroll,10,3,200))

		dscr = database.INVENTORY[resources.PARTY[resources.FORMATION][mn]][lopt][opt][0]
		if self.itmov != '':
			ox = (opt * 32) 
			lox = (lopt * 32)
			if opt > 0: ox += 5
			if lopt == 4: lox += 5
			if self.itmov[0] != 0:
				self.scr.blit(pygame.image.load('Sprites/Items/it_shade.png'), (15 + (mn * 200) + ox - self.scroll,62 + lox))
				self.scr.blit(pygame.image.load('Sprites/Items/it_' + self.itmov[0] + '.png'), (10 + (mn * 200) + ox - self.scroll + self.shake,35 + lox))
			else:
				srf = pygame.Surface((70,40))
				srf.set_alpha(100)
				srf.fill((0, 0, 0))
				self.scr.blit(srf, (25 + (mn * 200) + ox - self.scroll,40 + lox))
				self.scr.blit(self.itbor, (20 + (mn * 200) + ox - self.scroll + self.shake,35 + lox))
				if self.money == True:
					self.scr.blit(self.mnbor, (-35 + (mn * 200) + ox - self.scroll + self.shake,35 + lox))
					pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(-30 + (mn * 200) + ox - self.scroll + self.shake,40 + lox,50,30))
					self.scr.blit(self.fnt.render('$' + str(resources.MONEY), True, (255, 255, 255)), (-25 + (mn * 200) + ox - self.scroll + self.shake,45 + lox))

				if ex == 1: pygame.draw.rect(self.scr, (255,255,255), pygame.Rect(25 + (mn * 200) + ox - self.scroll + self.shake,40 + lox,30,30))
				else: pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(25 + (mn * 200) + ox - self.scroll + self.shake,40 + lox,30,30))
				if ex == 2: pygame.draw.rect(self.scr, (255,255,255), pygame.Rect(55 + (mn * 200) + ox - self.scroll + self.shake,40 + lox,30,30))
				else: pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(55 + (mn * 200) + ox - self.scroll + self.shake,40 + lox,30,30))
				if ex == 3: pygame.draw.rect(self.scr, (255,255,255), pygame.Rect(85 + (mn * 200) + ox - self.scroll + self.shake,40 + lox,30,30))
				else: pygame.draw.rect(self.scr, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(85 + (mn * 200) + ox - self.scroll + self.shake,40 + lox,30,30))
				if self.itmov[1] != '_': self.scr.blit(pygame.image.load('Sprites/Items/it_' + self.itmov[1] + '.png'), (25 + (mn * 200) + ox - self.scroll + self.shake,40 + lox))
				if self.itmov[2] != '_': self.scr.blit(pygame.image.load('Sprites/Items/it_' + self.itmov[2] + '.png'), (55 + (mn * 200) + ox - self.scroll + self.shake,40 + lox))
				self.scr.blit(pygame.image.load('Sprites/e_run.png'), (85 + (mn * 200) + ox - self.scroll + self.shake,40 + lox))
				if ex < 3: dscr = self.itmov[ex]
				else: dscr = '_'

		self.wdw.blit(self.scr, (10,10))
		pygame.draw.rect(self.wdw, (0, 0, 0), pygame.Rect(10,240,380,50))
		if dscr != '_':
			y = 0
			for t in database.ITEMS[dscr][1]:
				self.wdw.blit(self.fnt.render(t, True, (255, 255, 255)), (20, 250 + y))
				y += 15

		if self.shake > 0: self.shake = -self.shake
		elif self.shake < 0: self.shake = -self.shake - 1
		return self.wdw
	
	def deposit(self, opt, lopt, mn, ex):
		self.scr.fill((0,0,0))
		x = 20
		y = 45
		optx = 0
		opty = 0
		mnc = 0

		vlm = 0
		wei = 0

		if mn > 0:
			if self.scroll < (mn * 150):
				self.scroll += 10
		if self.scroll > (mn * 150):
			self.scroll -= 10

		for n in resources.PARTY[resources.FORMATION]:
			self.scr.blit(self.fnt.render(resources.CHARACTERS[n]['NAME'], True, (255, 255, 255)), (20, 10 + (200 * mnc) - self.scroll))
			for j in range(len(database.INVENTORY[n])):
				if opty == 4: y += 5
				for i in database.INVENTORY[n][j]:
					if optx == 1: x += 5

					if optx > 0 and opty < 4:
						if database.INVENTORY[mnc][4][0][0] != '_':
							if opt == optx and lopt == opty and mn == mnc:
								pygame.draw.rect(self.scr, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(x + 2,y + (200 * mnc) - self.scroll,28,28))
							else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(x + 2,y + (200 * mnc) - self.scroll,28,28))
							if i[0] != '_':
								self.scr.blit(pygame.image.load('Sprites/it_' + i[0] + '.png'), (x, y + (200 * mnc) - self.scroll))
								if optx > 0 and opty < 4:
									vlm += database.ITEMS[i[0]][3]
									wei += database.ITEMS[i[0]][4]
					else:
						if opt == optx and lopt == opty and mn == mnc:
							pygame.draw.rect(self.scr, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(x + 2,y + (200 * mnc) - self.scroll,28,28))
						else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(x + 2,y + (200 * mnc) - self.scroll,28,28))
						if i[0] != '_':
							self.scr.blit(pygame.image.load('Sprites/it_' + i[0] + '.png'), (x, y + (200 * mnc) - self.scroll))
							if optx > 0 and opty < 4:
								vlm += database.ITEMS[i[0]][3]
								wei += database.ITEMS[i[0]][4]

					x += 30
					optx += 1
				x = 20
				y += 30
				optx = 0
				opty += 1

			self.scr.blit(self.fnt.render(database.MENU[78] + ':', True, (255, 255, 255)), (85, 10 + (200 * mnc) - self.scroll))
			pygame.draw.rect(self.scr, (100, 100, 100), pygame.Rect(125,12 + (200 * mnc) - self.scroll,50,10))
			if vlm > 0 and database.INVENTORY[mnc][4][0][0] != '_': pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(125,12 + (200 * mnc) - self.scroll,int(50/(database.ITEMS[database.INVENTORY[mnc][4][0][0]][3]/vlm)),10))
			self.scr.blit(self.fnt.render(database.MENU[79] + ':', True, (255, 255, 255)), (85, 25 + (200 * mnc) - self.scroll))
			pygame.draw.rect(self.scr, (100, 100, 100), pygame.Rect(125,27 + (200 * mnc) - self.scroll,50,10))
			if wei > 0 and database.INVENTORY[mnc][4][0][0] != '_': pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(125,27 + (200 * mnc) - self.scroll,int(50/(database.ITEMS[database.INVENTORY[mnc][4][0][0]][4]/wei)),10))

			x = 20
			y = 45
			vlm = 0
			wei = 0
			optx = 0
			opty = 0
			mnc += 1
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(3,(200 * mnc) - self.scroll,200,3))

		if self.itmov != '':
			img = pygame.image.load('Sprites/it_' + self.itmov[0] + '.png')
			img.convert_alpha()
			img.set_alpha(100)
			ox = (opt * 30) 
			lox = (lopt * 30)
			if opt > 0: ox += 5
			if lopt == 4: lox += 5
			self.scr.blit(pygame.image.load('Sprites/it_shade.png'), (25 + ox,62 + lox + (mn * 200) - self.scroll))
			self.scr.blit(img, (20 + ox,35 + lox + (mn * 200) - self.scroll))

		self.wdw.blit(self.scr, (10,10))
		pygame.draw.rect(self.wdw, (0, 0, 0), pygame.Rect(10,240,380,50))
		if database.INVENTORY[resources.PARTY[resources.FORMATION][mn]][lopt][opt][0] != '_':
			y = 0
			for t in database.ITEMS[database.INVENTORY[resources.PARTY[resources.FORMATION][mn]][lopt][opt][0]][1]:
				self.wdw.blit(self.fnt.render(t, True, (255, 255, 255)), (20, 250 + y))
				y += 15
		return self.wdw

	def find(self, where, item):
		fnd = None
		if where != None:
			for y in database.INVENTORY[where]:
				for x in y:
					if x[0] == item and fnd == None: fnd = x
		else:
			for i in database.INVENTORY:
				for y in i:
					for x in y:
						if x[0] == item and fnd == None: fnd = x

		return fnd

	def add(self, where, item, prp='0000'):
		i = 0
		j = 0
		trigg = False
		for y in database.INVENTORY[where]:
			if j != 4:
				for x in y:
					if i != 0 and x[0] == '_' and trigg == False:
						vi = prp
						if item.startswith('food'):
							dd = resources.DATE[0] + int(database.ITEMS[item][6][0:2])
							mm = resources.DATE[1] + int(database.ITEMS[item][6][2:4])
							if dd > 30: dd -= 30; mm += 1
							if mm > 12: dd += 1; mm -= 12
							if dd < 10: dd = '0' + str(dd)
							if mm < 10: mm = '0' + str(mm)
							vi = str(dd) + str(mm)
						database.INVENTORY[where][j][i] = [item,vi,'_','_']
						trigg = True
					i += 1
			j += 1
			i = 0

	def space(self, where, ex=0, opt=None, lopt=None):
		i = 0
		j = 0
		if opt != None:
			if self.itmov[0] != 0:
				vlm = database.ITEMS[self.itmov[0]][3]
				wei = database.ITEMS[self.itmov[0]][4]
			else:
				vlm = database.ITEMS[self.itmov[ex]][3]
				wei = database.ITEMS[self.itmov[ex]][4]
		else:
			vlm = 0
			wei = 0
		trigg = True
		for y in database.INVENTORY[where]:
			if j != 4:
				for x in y:
					if x[0] != '_' and i!= 0:
						vlm += database.ITEMS[x[0]][3]
						wei += database.ITEMS[x[0]][4]
						if vlm > database.ITEMS[database.INVENTORY[where][4][0][0]][3]: trigg = False
						if wei > database.ITEMS[database.INVENTORY[where][4][0][0]][4]: trigg = False
					i += 1
			j += 1
			i = 0

		if lopt == 4: trigg = True
		elif opt == 0: trigg = True
		return trigg

class Shop:
	def __init__(self):
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 10)
		self.pxf = pygame.font.Font('Fonts/pixel-font.ttf', 20)
		self.dtt = pygame.font.Font('Fonts/datetype.ttf', 10)
		self.wdw = pygame.Surface((400, 250))
		pygame.draw.rect(self.wdw, (resources.COLOR[0],resources.COLOR[1],resources.COLOR[2]), pygame.Rect(0,0,400,250))
		for x in range(40):
			for y in range(25):
				self.wdw.blit(pygame.image.load('Sprites/border_' + str(resources.BORDER) + '.png'), (x * 10, y * 10))
		self.scr = pygame.Surface((380,230))
		
	def products(self, opt, lopt, lst):
		self.scr.fill((10,10,10))

		self.scr.blit(self.fnt.render('$' + str(resources.MONEY), True, (255, 255, 255)), (20, 10))

		y = 0
		for i in lst:
			if lopt == y:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,33 + (y * 12),370,12))
				self.scr.blit(self.fnt.render('$' + str(database.ITEMS[i][2]) + ' - ' + database.ITEMS[i][0], True, (0, 0, 0)), (20, 30 + (y * 12)))
				self.scr.blit(self.fnt.render(str(opt) + 'x', True, (0, 0, 0)), (360, 30 + (y * 12)))
			else:
				self.scr.blit(self.fnt.render('$' + str(database.ITEMS[i][2]) + ' - ' + database.ITEMS[i][0], True, (255, 255, 255)), (20, 30 + (y * 12)))
				self.scr.blit(self.fnt.render(str(opt) + 'x', True, (255, 255, 255)), (360, 30 + (y * 12)))
			y += 1

		if lopt != len(lst):
			l = 0
			for j in database.ITEMS[lst[lopt]][1]:
				self.scr.blit(self.fnt.render(j, True, (255, 255, 255)), (20,200 + (l * 10)))
				l += 1

		if lopt == y:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,33 + (y * 12),370,12))
			self.scr.blit(self.fnt.render(database.SHOP[1], True, (0, 0, 0)), (20, 30 + (y * 12)))
		else: self.scr.blit(self.fnt.render(database.SHOP[1], True, (255, 255, 255)), (20, 30 + (y * 12)))

		self.wdw.blit(self.scr, (10,10))
		return self.wdw

	def buy(self, opt, lopt, lst):
		self.scr.fill((10,10,10))

		pygame.draw.line(self.scr, (255, 255, 255), (5,15),(395,15),2)
		pygame.draw.line(self.scr, (255, 255, 255), (300,15),(300,230),2)
		pygame.draw.line(self.scr, (255, 255, 255), (300,160),(395,160),2)
		pygame.draw.line(self.scr, (255, 255, 255), (300,180),(395,180),2)
		pygame.draw.line(self.scr, (255, 255, 255), (5,200),(395,200),2)
		pygame.draw.line(self.scr, (255, 255, 255), (5,230),(395,230),2)

		y = 0
		cost = 0
		if len(lst) > 0:
			for i in lst:
				self.scr.blit(self.fnt.render('$' + str(database.ITEMS[i][2]) + ' - ' + database.ITEMS[i][0], True, (255, 255, 255)), (20, 25 + (y * 15)))
				cost += database.ITEMS[i][2]
				y += 1

		self.scr.blit(self.fnt.render('valor: ' + str(resources.MONEY), True, (255, 255, 255)), (305, 165))
		self.scr.blit(self.fnt.render('total: ' + str(cost), True, (255, 255, 255)), (305, 185))
		if resources.MONEY - cost > 0: pcol = (0,255,0)
		else: pcol = (255,0,0)
		self.scr.blit(self.fnt.render('troco: ' + str(resources.MONEY - cost), True, pcol), (305, 205))
		self.scr.blit(self.fnt.render('atendente: ', True, (255, 255, 255)), (10, 230))
		self.scr.blit(self.fnt.render('hora: ' + str(resources.TIME[0]) + ': ' + str(resources.TIME[1]), True, (255, 255, 255)), (200, 230))
		self.scr.blit(self.fnt.render('data: ' + str(resources.DATE[0]) + '/ ' + str(resources.DATE[1]), True, (255, 255, 255)), (300, 230))

		if lopt == 0:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,204,300,12))
			self.scr.blit(self.fnt.render(database.SHOP[0], True, (0,0,0)), (10, 201))
		else: self.scr.blit(self.fnt.render(database.SHOP[0], True, (255, 255, 255)), (10, 201))

		if lopt == 1:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,216,300,12)); tcol = (0,0,0)
			self.scr.blit(self.fnt.render(database.SHOP[7], True, (0, 0, 0)), (10, 213))
		else: self.scr.blit(self.fnt.render(database.SHOP[7], True, (255, 255, 255)), (10, 213))

		self.wdw.blit(self.scr, (10,10))
		return self.wdw

	def mercator(self, opt, lopt, lst, prm):
		self.scr.fill((10,10,10))

		self.scr.blit(self.fnt.render('$' + str(resources.MONEY), True, (255, 255, 255)), (20, 10))

		if opt == 0: self.scr.blit(self.fnt.render(database.SHOP[8], True, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2])), (20, 30))
		else: self.scr.blit(self.fnt.render(database.SHOP[8], True, (255,255,255)), (20, 30))
		x = 1
		for i in resources.PARTY[resources.FORMATION]:
			if opt == x: self.scr.blit(self.fnt.render(resources.CHARACTERS[i]['NAME'], True, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2])), (20 + (x * 60), 30))
			else: self.scr.blit(self.fnt.render(resources.CHARACTERS[i]['NAME'], True, (255,255,255)), (20 + (x * 60), 30))
			x += 1

		y = 0
		for i in lst:
			if opt == 0:
				if prm > 0:
					prc = database.ITEMS[i][2] - int(database.ITEMS[i][2]/prm)
				else: prc = database.ITEMS[i][2]
				if lopt == y:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,50 + (y * 15),370,15))
					self.scr.blit(self.fnt.render('$' + str(prc) + ' - ' + database.ITEMS[i][0], True, (0, 0, 0)), (20, 50 + (y * 15)))
				else:
					self.scr.blit(self.fnt.render('$' + str(prc) + ' - ' + database.ITEMS[i][0], True, (255, 255, 255)), (20, 50 + (y * 15)))
				if prm > 0:
					pygame.draw.rect(self.scr, (255, 170, 0), pygame.Rect(350,50 + (y * 15),30,20))
					self.scr.blit(self.dtt.render(str(prm) + '%', True, (255, 255, 255)), (350, 50 + (y * 15)))
				y += 1
			elif i[0] == resources.PARTY[resources.FORMATION][opt - 1]:
				if lopt == y:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,50 + (y * 15),370,15))
					self.scr.blit(self.fnt.render('$' + str(int(database.ITEMS[database.INVENTORY[i[0]][i[1]][i[2]][0]][2]/2)) + ' - ' + database.ITEMS[database.INVENTORY[i[0]][i[1]][i[2]][0]][0], True, (0, 0, 0)), (20, 50 + (y * 15)))
				else:
					self.scr.blit(self.fnt.render('$' + str(int(database.ITEMS[database.INVENTORY[i[0]][i[1]][i[2]][0]][2]/2)) + ' - ' + database.ITEMS[database.INVENTORY[i[0]][i[1]][i[2]][0]][0], True, (255, 255, 255)), (20, 50 + (y * 15)))
				y += 1

		if lopt != len(lst):
			l = 0
			if opt == 0:
				for j in database.ITEMS[lst[lopt]][1]:
					self.scr.blit(self.fnt.render(j, True, (255, 255, 255)), (20,200 + (l * 15)))
					l += 1
			else:
				for t in database.ITEMS[database.INVENTORY[lst[lopt][0]][lst[lopt][1]][lst[lopt][2]][0]][1]:
					self.scr.blit(self.fnt.render(t, True, (255, 255, 255)), (20,200 + (l * 15)))
					l += 1

		if lopt == y:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,50 + (y * 15),370,15))
			self.scr.blit(self.fnt.render(database.SHOP[1], True, (0, 0, 0)), (20, 50 + (y * 15)))
		else: self.scr.blit(self.fnt.render(database.SHOP[1], True, (255, 255, 255)), (20, 50 + (y * 15)))

		self.wdw.blit(self.scr, (10,10))
		return self.wdw

	def bank(self, opt, lopt, mn, ext):
		self.scr.fill((234,234,234))

		if mn == 3:
			if lopt == 0:
				pygame.draw.rect(self.scr, (94, 137, 255), pygame.Rect(5,120,200,30))
				self.scr.blit(self.pxf.render(database.SHOP[5], True, (0,0,0)), (10, 120))
			else:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,120,200,30))
				self.scr.blit(self.pxf.render(database.SHOP[5], True, (0, 0, 0)), (10, 120))

			if lopt == 1:
				pygame.draw.rect(self.scr, (94, 137, 255), pygame.Rect(5,160,200,30))
				self.scr.blit(self.pxf.render(database.SHOP[6], True, (0, 0, 0)), (10, 160))
			else:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,160,200,30))
				self.scr.blit(self.pxf.render(database.SHOP[6], True, (0, 0, 0)), (10, 160))

			if lopt == 2:
				pygame.draw.rect(self.scr, (94, 137, 255), pygame.Rect(5,200,200,30))
				self.scr.blit(self.pxf.render(database.SHOP[7], True, (0, 0, 0)), (10, 200))
			else:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,200,200,30))
				self.scr.blit(self.pxf.render(database.SHOP[7], True, (0, 0, 0)), (10, 200))

		else:
			pygame.draw.rect(self.scr, (94, 137, 255), pygame.Rect(80,80,200,110))
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(110,90,130,27))
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(110,120,130,27))
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(110,150,130,27))
			pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(120 + opt * 6,135,5,2))

			self.scr.blit(self.pxf.render(str(resources.ATM), True, (0,0,0)), (120, 90))
			self.scr.blit(self.pxf.render(str(ext[0]) + str(ext[1]) + str(ext[2]) + str(ext[3]) + str(ext[4]) + str(ext[5]), True, (0,0,0)), (120, 120))
			self.scr.blit(self.pxf.render(str(resources.MONEY), True, (0,0,0)), (120, 150))

		self.wdw.blit(self.scr, (10,10))
		return self.wdw

class Phone:
	def __init__(self):
		self.scr = pygame.Surface((180,232))
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 10)
		self.ttl = pygame.font.Font('Fonts/pixel-font.ttf', 25)
		self.dtt = pygame.font.Font('Fonts/datetype.ttf', 8)
		self.pbg = resources.PARTY[resources.FORMATION][0]
		self.scroll = 0

	def bar(self, sg):
		self.bsc = pygame.Surface((180,18))
		self.bsc.fill((10,10,10))

		hour = ['','']
		if resources.TIME[0] < 10: hour[0] = '0' + str(resources.TIME[0])
		else: hour[0] = str(resources.TIME[0])
		if resources.TIME[1] < 10: hour[1] = '0' + str(resources.TIME[1])
		else: hour[1] = str(resources.TIME[1])
		self.bsc.blit(self.dtt.render(hour[0] + ':' + hour[1], True, (255, 255, 255)), (75, 4))
		day = ['','','']
		if resources.DATE[0] < 10: day[0] = '0' + str(resources.DATE[0])
		else: day[0] = str(resources.DATE[0])
		if resources.DATE[1] < 10: day[1] = '0' + str(resources.DATE[1])
		else: day[1] = str(resources.DATE[1])
		if resources.DATE[2] < 10: day[2] = '0' + str(resources.DATE[2])
		else: day[2] = str(resources.DATE[2])
		self.bsc.blit(self.dtt.render(day[0] + '/' + day[1] + '/' + day[2], True, (255, 255, 255)), (3, 4))

		self.bsc.blit(pygame.image.load('Sprites/signal_' + str(sg) + '.png'), (130, 6))
		self.bsc.blit(pygame.image.load('Sprites/battery_0.png'), (150, 2))
		if resources.BATTERY > 100.0: pygame.draw.rect(self.bsc, (255, 255, 255), pygame.Rect(173 - int(18/(360/resources.BATTERY)),5,int(18/(360/resources.BATTERY)),7))
		elif resources.BATTERY > 1.0: pygame.draw.rect(self.bsc, (255, 10, 10), pygame.Rect(173 - int(18/(360/resources.BATTERY)),5,int(18/(360/resources.BATTERY)),7))

		return self.bsc

	def apps(self, opt, lopt):
		self.scr.fill((0,0,0))

		if lopt > 2:
			if self.scroll < (lopt - 2) * 60:
				self.scroll += 10
		elif lopt > 0 and lopt < 3:
			if self.scroll > (lopt - 1) * 60:
				self.scroll -= 10
		elif lopt == 0 and self.scroll > 0:
			self.scroll -= 10

		self.scr.blit(pygame.image.load('Backgrounds/phone_' + str(self.pbg) + '.png'), (0, 0))

		if opt == 0 and lopt == 0: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_maps.png'), (50, 50)), (4, 2 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_maps.png'), (7, 5 - self.scroll))
		if opt == 1 and lopt == 0: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_call.png'), (50, 50)), (64, 2 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_call.png'), (67, 5 - self.scroll))
		if opt == 2 and lopt == 0: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_mail.png'), (50, 50)), (124, 2 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_mail.png'), (127, 5 - self.scroll))
		if opt == 0 and lopt == 1: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_news.png'), (50, 50)), (4, 62 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_news.png'), (7, 65 - self.scroll))
		if opt == 1 and lopt == 1: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_radi.png'), (50, 50)), (64, 62 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_radi.png'), (67, 65 - self.scroll))
		if opt == 2 and lopt == 1: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_camr.png'), (50, 50)), (124, 62 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_camr.png'), (127, 65 - self.scroll))
		if opt == 0 and lopt == 2: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_best.png'), (50, 50)), (4, 122 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_best.png'), (7, 125 - self.scroll))
		if opt == 1 and lopt == 2: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_task.png'), (50, 50)), (64, 122 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_task.png'), (67, 125 - self.scroll))
		if opt == 2 and lopt == 2: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_stts.png'), (50, 50)), (124, 122 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_stts.png'), (127, 125 - self.scroll))
		if opt == 0 and lopt == 3: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_tact.png'), (50, 50)), (4, 182 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_tact.png'), (7, 185 - self.scroll))
		if opt == 1 and lopt == 3: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_achi.png'), (50, 50)), (64, 182 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_achi.png'), (67, 185 - self.scroll))
		if opt == 2 and lopt == 3: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_rank.png'), (50, 50)), (124, 182 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_rank.png'), (127, 185 - self.scroll))
		if opt == 0 and lopt == 4: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_help.png'), (50, 50)), (4, 242 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_help.png'), (7, 245 - self.scroll))
		if opt == 1 and lopt == 4: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_sett.png'), (50, 50)), (64, 242 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_sett.png'), (67, 245 - self.scroll))
		if opt == 2 and lopt == 4: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_info.png'), (50, 50)), (124, 242 - self.scroll))
		else: self.scr.blit(pygame.image.load('Sprites/ph_info.png'), (127, 245 - self.scroll))
		#if opt == 0 and lopt == 5: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/ph_save.png'), (50, 50)), (4, 320 - self.scroll))
		#else: self.scr.blit(pygame.image.load('Sprites/ph_save.png'), (7, 323 - self.scroll))

		return self.scr

	def map(self, mp, x, y, zoom, sg):
		if sg > 0:
			try:
				mim = pygame.image.load('Maps/' + mp + '.png')
				pygame.transform.scale(mim, (zoom,zoom))
				self.scr.blit(mim, (int(-x) + 50, int(-y) + 50))
			except: pass
		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 200))

		pygame.draw.rect(self.scr, (140, 255, 253), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[0], True, (0, 0, 0)), (5, 4))

		return self.scr

	def contacts(self, flt, opt, mnu):
		if flt == 0: em = resources.PARTY
		if flt == 1: em = database.CONTACTS
		if flt == 2: em = database.CALLHIST

		print(self.scroll)
		if opt > 2:
			if self.scroll < (opt - 2) * 51:
				self.scroll += 5.1
		elif opt > 0 and opt < len(em) - 1:
			if self.scroll > (opt - 1) * 51:
				self.scroll -= 5.1
		elif opt == 0:
			if self.scroll > 0:
				self.scroll -= 5.1

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		y = 0
		for i in em:
			if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - self.scroll,180,50))
			else: pygame.draw.rect(self.scr, (15, 255, 0), pygame.Rect(0,66 + y - self.scroll,180,50))

			if flt > 0: self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 76 + y - self.scroll))
			else:
				if opt == y/51:
					if mnu == 1: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(118,74 + y - self.scroll,24,24))
					self.scr.blit(pygame.image.load('Sprites/tc_9.png'), (120, 76 + y - self.scroll))
					if mnu == 2: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(140,74 + y - self.scroll,24,24))
					self.scr.blit(pygame.image.load('Sprites/tc_8.png'), (142, 76 + y - self.scroll))
					if mnu == 3: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(8,74 + y - self.scroll,24,24))
					if mnu == 4: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(30,74 + y - self.scroll,24,24))
					if mnu == 5: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(52,74 + y - self.scroll,24,24))

				x = 0
				for p in i:
					self.scr.blit(pygame.image.load('Sprites/who_' + str(p) + '.png'), (10 + x, 76 + y - self.scroll))
					x += 22

			if flt == 0: self.scr.blit(self.fnt.render('grupo ' + str(int((y + 51)/51)), True, (0, 0, 0)), (10, 96 + y - self.scroll))
			if flt == 1: self.scr.blit(self.fnt.render(i[1], True, (0, 0, 0)), (10, 86 + y - self.scroll))
			if flt == 2: self.scr.blit(pygame.image.load('Sprites/who_' + str(i[1]).lower() + '.png'), (160, 86 + y - self.scroll))
			y += 51
		if flt == 0:
			if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - self.scroll,180,50))
			else: pygame.draw.rect(self.scr, (15, 255, 0), pygame.Rect(0,66 + y - self.scroll,180,50))
			self.scr.blit(self.fnt.render(database.MENU[31], True, (0, 0, 0)), (10, 76 + y - self.scroll))
		if y == 0 and flt == 1:
			self.scr.blit(self.fnt.render(database.MENU[16], True, (255, 255, 255)), (50, 140))

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
		if flt == 0:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,45,60,20))
			self.scr.blit(self.fnt.render(database.MENU[23], True, (0, 0, 0)), (8, 47))
		else: self.scr.blit(self.fnt.render(database.MENU[23], True, (255, 255, 255)), (8, 47))
		if flt == 1:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(60,45,60,20))
			self.scr.blit(self.fnt.render(database.MENU[24], True, (0, 0, 0)), (70, 47))
		else: self.scr.blit(self.fnt.render(database.MENU[24], True, (255, 255, 255)), (70, 47))
		if flt == 2:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(120,45,60,20))
			self.scr.blit(self.fnt.render(database.MENU[25], True, (0, 0, 0)), (130, 47))
		else: self.scr.blit(self.fnt.render(database.MENU[25], True, (255, 255, 255)), (130, 47))

		pygame.draw.rect(self.scr, (15, 255, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[1], True, (0, 0, 0)), (5, 5))

		return self.scr

	def email(self, flt, opt, mnu, sg):
		self.e_read = []
		self.e_unread = []
		for i in resources.INBOX:
			if i[3] == 1:
				self.e_read.append(i)
			if i[3] == 0:
				self.e_unread.append(i)
				
		if flt == 0: em = self.e_unread
		if flt == 1: em = self.e_read
		if flt == 2: em = resources.INBOX

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0:
			if mnu == 0:
				self.scroll = 0
				if opt > 2: self.scroll += (opt - 2) * 51

				y = 0
				for i in em:
					if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - self.scroll,180,50))
					else: pygame.draw.rect(self.scr, (255, 221, 0), pygame.Rect(0,66 + y,180,50))
					self.scr.blit(self.fnt.render(i[1], True, (0, 0, 0)), (10, 76 + y - self.scroll))
					self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 86 + y - self.scroll))
					y += 51
				if y == 0:
					self.scr.blit(self.fnt.render(database.MENU[19], True, (255, 255, 255)), (255, 140))

				pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
				if flt == 0:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,45,60,20))
					self.scr.blit(self.fnt.render(database.MENU[26], True, (0, 0, 0)), (12, 47))
				else: self.scr.blit(self.fnt.render(database.MENU[26], True, (255, 255, 255)), (12, 47))
				if flt == 1:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(60,45,60,20))
					self.scr.blit(self.fnt.render(database.MENU[27], True, (0, 0, 0)), (75, 47))
				else: self.scr.blit(self.fnt.render(database.MENU[27], True, (255, 255, 255)), (75, 47))
				if flt == 2:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(120,45,60,20))
					self.scr.blit(self.fnt.render(database.MENU[28], True, (0, 0, 0)), (132, 47))
				else: self.scr.blit(self.fnt.render(database.MENU[28], True, (255, 255, 255)), (132, 47))

			elif mnu > 0:
				self.scroll = (mnu - 1) * 3
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
				self.scr.blit(self.fnt.render(em[opt][1], True, (0, 0, 0)), (15, 55 - self.scroll))
				self.scr.blit(self.fnt.render(database.MENU[34] + em[opt][0], True, (0, 0, 0)), (15, 85 - self.scroll))
				self.scr.blit(self.fnt.render(database.MENU[35] + (resources.CHARACTERS[resources.PARTY[0][0]]['NAME'] + resources.CHARACTERS[resources.PARTY[0][0]]['LASTNAME']).lower() + '@cmail.com', True, (0, 0, 0)), (15, 100 - self.scroll))
				y = 0
				for l in em[opt][2]:
					self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (15, 130 + y - self.scroll))
					y += 15
		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 200))

		pygame.draw.rect(self.scr, (255, 221, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[2], True, (0, 0, 0)), (5, 5))

		return self.scr

	def news(self, opt, mnu, sg):
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		print(mnu)
		print(opt)
		if sg > 0:
			if mnu == 0:
				self.scroll = 0
				if opt > 2: self.scroll += (opt - 2) * 51
				y = 0
				hei = 0
				for i in database.NEWS[resources.DATE[0] - 1]:
					if isinstance(i[0],str):
						for l in i[0]: hei += 20
						hei += 20
						if opt != y: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + (y * hei) - self.scroll,180,50 + (y * hei)))
						else: pygame.draw.rect(self.scr, (219, 49, 37), pygame.Rect(0,41 + (y * hei),180,50 + (y * hei)))
						yi = 0
						for l in i[0]:
							self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 46 + (y * hei) - self.scroll + yi))
							yi += 15
						self.scr.blit(self.fnt.render(i[1], True, (0, 0, 0)), (10, 52 + (y * hei) - self.scroll + yi))
						y += 1
						hei = 0
					elif i[0] == 1:
						pygame.draw.rect(self.scr, (219, 49, 37), pygame.Rect(0,41 + (y * hei),180,50 + (y * hei)))
						self.scr.blit(self.fnt.render(i[1][0], True, (0, 0, 0)), (10, 46 + (y * hei) - self.scroll))
						self.scr.blit(self.fnt.render(i[1][1], True, (0, 0, 0)), (10, 56 + (y * hei) - self.scroll))

			elif mnu > 0:
				self.scroll = (mnu - 1) * 3
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
				y = 0
				for l in database.NEWS[resources.DATE[0] - 1][opt][0]:
					self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 50 + y - self.scroll))
					y += 15
				self.scr.blit(self.fnt.render(database.NEWS[resources.DATE[0] - 1][opt][1], True, (0, 0, 0)), (10, 55 + y - self.scroll))
				for l in database.NEWS[resources.DATE[0] - 1][opt][2]:
					self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 100 + y - self.scroll))
					y += 15
		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (219, 49, 37), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[3], True, (0, 0, 0)), (5, 5))

		return self.scr

	def radio(self, fm, msc):
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if resources.RADIO[str(math.floor(fm/20))] != []:
			pygame.draw.rect(self.scr, (255, 0, 135), pygame.Rect(0,66,180,50))
			self.scr.blit(self.fnt.render(resources.RADIO[str(math.floor(fm/20))][msc][:-4], True, (0, 0, 0)), (10, 76))
		else: self.scr.blit(self.fnt.render(database.MENU[20], True, (255, 255, 255)), (70, 140))

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
		f = 0
		for i in range(9):
			pygame.draw.line(self.scr, (255, 255, 255), (0 + f,50),(0 + f,65),1)
			pygame.draw.line(self.scr, (255, 255, 255), (10 + f,55),(10 + f,65),1)
			f += 20
		pygame.draw.rect(self.scr, (255, 0, 0), pygame.Rect(0 + fm,50,4,16))
		self.scr.blit(self.fnt.render(str(fm/10), True, (255, 255, 255)), (70, 20))

		pygame.draw.rect(self.scr, (255, 0, 135), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[4], True, (0, 0, 0)), (5, 5))

		return self.scr

	def camera(self, opt, sg):
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[5], True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		if sg > 0:
			y = 0
			print(resources.FILES)
			for i in range(len(resources.FILES[0])):
				if opt != y: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + (y * 51),180,50))
				else: pygame.draw.rect(self.scr, (255, 255, 10), pygame.Rect(0,41 + (y * 51),180,50))
				self.scr.blit(self.fnt.render(database.CHAPTERS[resources.FILES[1][i]][0], True, (0, 0, 0)), (10, 51 + (y * 51)))
				ss = math.floor(resources.FILES[2][i]/1000)
				mm = 0
				hh = 0
				while ss > 60: ss -= 60; mm += 1
				while mm > 60: mm -= 60; hh += 1
				if ss < 10: ss = '0' + str(ss)
				else: ss = str(ss)
				if mm < 10: mm = '0' + str(mm)
				else: mm = str(mm)
				if hh < 10: hh = '0' + str(hh)
				else: hh = str(hh)
				self.scr.blit(self.fnt.render(hh + ' : ' + mm + ' : ' + ss, True, (0, 0, 0)), (10, 61 + (y * 51)))
				y += 1

			if opt != y: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + (y * 51),180,50))
			else: pygame.draw.rect(self.scr, (255, 255, 10), pygame.Rect(0,41 + (y * 51),180,50))
			self.scr.blit(self.fnt.render(database.MENU[61], True, (0, 0, 0)), (10, 51 + (y * 51)))

		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 140))

		return self.scr

	def bestiary(self, opt, lopt, mnu, sg):
		self.scroll = 0
		if opt > 2: self.scroll += (opt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0:
			if len(database.BESTIARY) > 0:
				if mnu == 0:
					y = 0
					for i in database.BESTIARY:
						if lopt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y - self.scroll,180,50))
						else: pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(0,41 + y - self.scroll,180,50))
						self.scr.blit(self.fnt.render(database.FREAKS[i['N']]['NAME'], True, (0, 0, 0)), (10, 51 + y - self.scroll))
						y += 51

				if mnu == 1:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
					pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(5,243,83,3))
					self.scr.blit(self.fnt.render(database.FREAKS[database.BESTIARY[opt]['N']]['NAME'], True, (0, 0, 0)), (10, 55))
					self.scr.blit(pygame.image.load('Sprites/' + database.BESTIARY[opt]['N'] + '_stand.png'), (60, 70))
					self.scr.blit(self.fnt.render('ID: ' + database.BESTIARY[opt]['ID'], True, (0, 0, 0)), (20, 160))
					self.scr.blit(self.fnt.render('RG: ' + database.BESTIARY[opt]['DATE'], True, (0, 0, 0)), (60, 160))
					self.scr.blit(self.fnt.render('HG: ' + database.FREAKS[database.BESTIARY[opt]['N']]['HEIGHT'], True, (0, 0, 0)), (110, 160))

					j = 0
					for l in database.FREAKS[database.BESTIARY[opt]['N']]['INFO']:
						self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 180 + j))
						j += 15

				if mnu == 2:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
					pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(92,243,83,3))
					pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(10,50,160,77))

					y = 0
					for i in database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES']:
						if lopt != y/19: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(11,51 + y,158,18))
						else: pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(11,51 + y,158,18))
						self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (20, 53 + y))
						y += 19

					j = 0
					for l in database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][1]:
						self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 140 + j))
						j += 15

					if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 1: dmg = database.MENU[37] + str(database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2])
					elif database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 2: dmg = database.MENU[38] + str(database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2])
					elif database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 3: dmg = database.MENU[39] + str(database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2])
					elif database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 4: dmg = database.MENU[40] + str(database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2])
					elif database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 5: dmg = database.MENU[41] + str(database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2])
					elif database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 6:
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 4: dmg = database.MENU[42]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 5: dmg = database.MENU[43]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 6: dmg = database.MENU[44]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 7: dmg = database.MENU[45]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 8: dmg = database.MENU[46]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 9: dmg = database.MENU[47]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 10: dmg = database.MENU[48]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 11: dmg = database.MENU[49]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] in (12,13,14): dmg = database.MENU[50]
						if database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][2] == 15: dmg = database.MENU[51]
					elif database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 7: dmg = database.MENU[52]
					elif database.FREAKS[database.BESTIARY[opt]['N']]['HABILITIES'][lopt][3] == 8: dmg = database.MENU[53]
					else: dmg = ''

					self.scr.blit(self.fnt.render(dmg, True, (0, 0, 0)), (20, 210))
			else: self.scr.blit(self.fnt.render(database.MENU[21], True, (255, 255, 255)), (10, 140))
		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[6], True, (0, 0, 0)), (5, 5))

		return self.scr

	def task(self, flt, opt, mnu):
		self.t_unmark = []
		self.t_mark = []
		for i in resources.TASKS:
			if i[1] == 1:
				self.t_mark.append(i)
			if i[1] == 0:
				self.t_unmark.append(i)

		if flt == 0: em = self.t_unmark
		if flt == 1: em = self.t_mark
		if flt == 2: em = resources.TASKS

		if opt > 2:
			if self.scroll < (opt - 2) * 31:
				self.scroll += 6.2
		elif opt > 0 and opt < len(em) - 1:
			if self.scroll > (opt - 1) * 31:
				self.scroll -= 6.2
		elif opt == 0 and self.scroll > 0:
			self.scroll -= 6.2
			
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		y = 0
		for i in em:
			if opt != y/31: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 123, 0), pygame.Rect(0,66 + y - self.scroll,180,30))
			self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 73 + y - self.scroll))
			y += 31
		if y == 0:
			self.scr.blit(self.fnt.render(database.MENU[22], True, (255, 255, 255)), (45, 140))

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
		if flt == 0:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,45,60,20))
			self.scr.blit(self.fnt.render(database.MENU[29], True, (0, 0, 0)), (12, 47))
		else: self.scr.blit(self.fnt.render(database.MENU[29], True, (255, 255, 255)), (12, 47))
		if flt == 1:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(60,45,60,20))
			self.scr.blit(self.fnt.render(database.MENU[30], True, (0, 0, 0)), (75, 47))
		else: self.scr.blit(self.fnt.render(database.MENU[30], True, (255, 255, 255)), (75, 47))
		if flt == 2:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(120,45,60,20))
			self.scr.blit(self.fnt.render(database.MENU[28], True, (0, 0, 0)), (132, 47))
		else: self.scr.blit(self.fnt.render(database.MENU[28], True, (255, 255, 255)), (132, 47))

		pygame.draw.rect(self.scr, (255, 123, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[7], True, (0, 0, 0)), (5, 5))

		return self.scr

	def status(self, opt):
		self.scroll = 0
		if opt > 2: self.scroll += (opt - 2) * 60

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		x = 0
		for i in resources.PARTY[resources.FORMATION]:
			if opt == x/60:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0 + x - self.scroll,45,60,20))
				self.scr.blit(self.fnt.render(resources.CHARACTERS[i]['NAME'], True, (0, 0, 0)), (8 + x - self.scroll, 47))
			else: self.scr.blit(self.fnt.render(resources.CHARACTERS[i]['NAME'], True, (255, 255, 255)), (8 + x - self.scroll, 47))
			x += 60

		self.scr.blit(pygame.image.load('Sprites/who_' + str(resources.PARTY[resources.FORMATION][opt]) + '.png'), (10, 74))
		self.scr.blit(self.fnt.render(resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['NAME'] + ' ' + resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LASTNAME'], True, (255, 255, 255)), (35, 76))
		self.scr.blit(self.fnt.render(str(resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['ID']), True, (255, 255, 255)), (10, 96))
		self.scr.blit(pygame.image.load('Sprites/gn_' + resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['GENDER'] + '.png'), (70, 96))
		self.scr.blit(self.fnt.render(resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['BLOOD'], True, (255, 255, 255)), (50, 96))

		self.scr.blit(self.fnt.render('level ' + str(resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']), True, (255, 255, 255)), (10, 115))
		self.scr.blit(self.fnt.render('hp:', True, (255, 255, 255)), (10, 130))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(30,135,100,10))
		if resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['HP'] > 0:
			pygame.draw.rect(self.scr, (0, 255, 0), pygame.Rect(30,135,int(100/(resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['VITALITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']]/resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['HP'])),10))
		self.scr.blit(self.fnt.render('xp:', True, (255, 255, 255)), (10, 145))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(30,150,100,10))
		if resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['XP'] > 0:
			pygame.draw.rect(self.scr, (0, 255, 0), pygame.Rect(30,150,int(100/(resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['MAXXP']/resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['XP'])),10))
		self.scr.blit(self.fnt.render('st:', True, (255, 255, 255)), (10, 160))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(30,165,100,10))
		if resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['STRENGHT'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']] > 0:
			pygame.draw.rect(self.scr, (0, 255, 0), pygame.Rect(30,165,int(100/(100/resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['STRENGHT'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']])),10))
		self.scr.blit(self.fnt.render('at:', True, (255, 255, 255)), (10, 175))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(30,180,100,10))
		if resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['ATTACK'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']] > 0:
			pygame.draw.rect(self.scr, (0, 255, 0), pygame.Rect(30,180,int(100/(100/resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['ATTACK'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']])),10))
		self.scr.blit(self.fnt.render('ag:', True, (255, 255, 255)), (10, 190))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(30,195,100,10))
		if resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['AGILITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']] > 0:
			pygame.draw.rect(self.scr, (0, 255, 0), pygame.Rect(30,195,int(100/(100/resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['AGILITY'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']])),10))
		self.scr.blit(self.fnt.render('rs:', True, (255, 255, 255)), (10, 205))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(30,210,100,10))
		if resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['RESISTANCE'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']] > 0:
			pygame.draw.rect(self.scr, (0, 255, 0), pygame.Rect(30,210,int(100/(100/resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['RESISTANCE'][resources.CHARACTERS[resources.PARTY[resources.FORMATION][opt]]['LEVEL']])),10))

		pygame.draw.rect(self.scr, (255, 0, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[8], True, (0, 0, 0)), (5, 5))

		return self.scr

	def tactics(self, opt, lopt, mnu, sg):
		self.scroll = 0
		if lopt > 2: self.scroll += (lopt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0:
			y = 0
			for i in database.TACTICAL:
				if i != []:
					if lopt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y - self.scroll,180,50))
					else: pygame.draw.rect(self.scr, (33, 75, 127), pygame.Rect(0,41 + y - self.scroll,180,50))

					if mnu > 0 and lopt == y/51:
						if mnu < 5:
							pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(8 + (mnu - 1) * 22,49 + y - self.scroll,24,24))
							if i[mnu - 1] == 1: self.scr.blit(self.fnt.render(database.MENU[54], True, (0, 0, 0)), (10, 70 + y - self.scroll))
							if i[mnu - 1] == 2: self.scr.blit(self.fnt.render(database.MENU[55], True, (0, 0, 0)), (10, 70 + y - self.scroll))
							if i[mnu - 1] == 3: self.scr.blit(self.fnt.render(database.MENU[56], True, (0, 0, 0)), (10, 70 + y - self.scroll))
							if i[mnu - 1] == 4: self.scr.blit(self.fnt.render(database.MENU[57], True, (0, 0, 0)), (10, 70 + y - self.scroll))
							if i[mnu - 1] == 5: self.scr.blit(self.fnt.render(database.MENU[58], True, (0, 0, 0)), (10, 70 + y - self.scroll))
							if i[mnu - 1] == 6: self.scr.blit(self.fnt.render(database.MENU[59], True, (0, 0, 0)), (10, 70 + y - self.scroll))
							if i[mnu - 1] == 7: self.scr.blit(self.fnt.render(database.MENU[60], True, (0, 0, 0)), (10, 70 + y - self.scroll))
						else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(118,49 + y - self.scroll,24,24))
						self.scr.blit(pygame.image.load('Sprites/tc_8.png'), (120, 51 + y - self.scroll))

					self.scr.blit(pygame.image.load('Sprites/tc_' + str(i[0]) + '.png'), (10, 51 + y - self.scroll))
					self.scr.blit(pygame.image.load('Sprites/tc_' + str(i[1]) + '.png'), (32, 51 + y - self.scroll))
					self.scr.blit(pygame.image.load('Sprites/tc_' + str(i[2]) + '.png'), (54, 51 + y - self.scroll))
					self.scr.blit(pygame.image.load('Sprites/tc_' + str(i[3]) + '.png'), (76, 51 + y - self.scroll))
				y += 51

			if lopt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y - self.scroll,180,50))
			else: pygame.draw.rect(self.scr, (33, 75, 127), pygame.Rect(0,41 + y - self.scroll,180,50))
			self.scr.blit(self.fnt.render(database.MENU[36], True, (0, 0, 0)), (20, 50 + y - self.scroll))

		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (33, 75, 127), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[9], True, (0, 0, 0)), (5, 5))

		return self.scr

	def achievements(self, opt, sg):
		self.scroll = 0
		if opt > 2: self.scroll += (opt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0:
			y = 0
			for i in database.ACHIEVEMENTS:
				if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y - self.scroll,180,50))
				else: pygame.draw.rect(self.scr, (255, 191, 0), pygame.Rect(0,41 + y - self.scroll,180,50))

				if i[2] == True: tcol = (0,0,0)
				else: tcol = (80,80,80)
				self.scr.blit(self.fnt.render(i[0], True, tcol), (10, 51 + y - self.scroll))
				self.scr.blit(self.fnt.render(i[1], True, tcol), (10, 65 + y - self.scroll))
				y += 51

		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (255, 191, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[10], True, (0, 0, 0)), (5, 5))

		return self.scr

	def ranking(self, opt, sg):
		self.scroll = 0
		if opt > 2: self.scroll += (opt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0: pass
		else: self.scr.blit(self.fnt.render(database.MENU[15], True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (55, 255, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[11], True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		return self.scr

	def help(self, opt, mnu):
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if mnu == 0:
			self.scroll = 0
			if opt > 2: self.scroll += (opt - 2) * 51
			y = 0
			for i in database.MANUAL:
				if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y - self.scroll,180,50))
				else: pygame.draw.rect(self.scr, (137, 50, 0), pygame.Rect(0,41 + y - self.scroll,180,50))
				self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 51 + y - self.scroll))
				y += 51

		if mnu > 0:
			self.scroll = (mnu - 1) * 3
			pygame.draw.rect(self.scr,(255, 255, 255), pygame.Rect(5,45,170,200))
			self.scr.blit(self.fnt.render(database.MANUAL[opt][0], True, (0, 0, 0)), (70, 55 - self.scroll))
			y = 0
			for l in database.MANUAL[opt][1]:
				self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (15, 80 + y - self.scroll))
				y += 15

		pygame.draw.rect(self.scr, (137, 50, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[12], True, (0, 0, 0)), (5, 5))

		return self.scr

	def settings(self, opt, mnu, trg):
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		if mnu == 0:
			self.scroll = 0
			if opt == 0: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,41 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 - self.scroll,180,30))
			self.scr.blit(self.fnt.render(database.MENU[88], True, (0,0,0)), (10, 49 - self.scroll))

			if opt == 1: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,72 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,72 - self.scroll,180,30))
			self.scr.blit(self.fnt.render(database.MENU[89], True, (0,0,0)), (10, 80 - self.scroll))

			if opt == 2: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,103 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,103 - self.scroll,180,30))
			self.scr.blit(self.fnt.render(database.MENU[90], True, (0,0,0)), (10, 111 - self.scroll))

			if opt == 3: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,134 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,134 - self.scroll,180,30))
			self.scr.blit(self.fnt.render(database.MENU[76], True, (0,0,0)), (10, 142 - self.scroll))

		if mnu == 1:
			if opt == 0:
				if self.scroll > 0:
					self.scroll -= 10
			elif opt == 5:
				if self.scroll < 60:
					self.scroll += 10
			elif opt == 2:
				if self.scroll > 0:
					self.scroll -= 10
			elif opt == 7:
				if self.scroll < 60:
					self.scroll += 10

			if opt == 0: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,41 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 - self.scroll,180,30))
			self.scr.blit(self.fnt.render(database.MENU[62] + ': ' + resources.LANG, True, (0,0,0)), (10, 51 - self.scroll))

			if opt == 1: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,72 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,72 - self.scroll,180,30))
			if resources.SPEED == 5: txt = database.MENU[91]
			if resources.SPEED == 4: txt = database.MENU[92]
			if resources.SPEED == 3: txt = database.MENU[93]
			if resources.SPEED == 2: txt = database.MENU[94]
			if resources.SPEED == 1: txt = database.MENU[95]
			self.scr.blit(self.fnt.render(database.MENU[72] + ': ' + txt, True, (0,0,0)), (10, 82 - self.scroll))
			
			if opt == 2: pygame.draw.rect(self.scr, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(0,103 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,103 - self.scroll,180,30))
			pygame.draw.rect(self.scr, (210, 210, 210), pygame.Rect(60,113 - self.scroll,110,10))
			pygame.draw.rect(self.scr, (110,110,110), pygame.Rect(60 + int(100/(242/resources.COLOR[0])),113 - self.scroll,10,10))
			self.scr.blit(self.fnt.render(database.MENU[73] + ':', True, (0,0,0)), (10, 111 - self.scroll))

			if opt == 3: pygame.draw.rect(self.scr, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(0,134 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,134 - self.scroll,180,30))
			pygame.draw.rect(self.scr, (210, 210, 210), pygame.Rect(60,144 - self.scroll,110,10))
			pygame.draw.rect(self.scr, (110,110,110), pygame.Rect(60 + int(100/(242/resources.COLOR[1])),144 - self.scroll,10,10))
			self.scr.blit(self.fnt.render(database.MENU[74] + ':', True, (0,0,0)), (10, 142 - self.scroll))

			if opt == 4: pygame.draw.rect(self.scr, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(0,165 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,165 - self.scroll,180,30))
			pygame.draw.rect(self.scr, (210, 210, 210), pygame.Rect(60,175 - self.scroll,110,10))
			pygame.draw.rect(self.scr, (110,110,110), pygame.Rect(60 + int(100/(242/resources.COLOR[2])),175 - self.scroll,10,10))
			self.scr.blit(self.fnt.render(database.MENU[75] + ':', True, (0,0,0)), (10, 171 - self.scroll))

			if opt == 5: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,196 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,196 - self.scroll,180,30))
			self.scr.blit(self.fnt.render(database.MENU[87] + ': ', True, (0,0,0)), (10, 204 - self.scroll))
			pygame.draw.rect(self.scr, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(60,196 - self.scroll,120,30))
			for i in range(12):
				for y in range(3): self.scr.blit(pygame.image.load('Sprites/border_' + str(resources.BORDER) + '.png'), (60 + i * 10, 196 + (y * 10) - self.scroll))

			if opt == 6: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,227 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,227 - self.scroll,180,30))
			pygame.draw.rect(self.scr, (210, 210, 210), pygame.Rect(75,237 - self.scroll,80,10))
			if resources.CENSORSHIP == False: pygame.draw.rect(self.scr, (255,61,61), pygame.Rect(115,237 - self.scroll,40,10))
			if resources.CENSORSHIP == True: pygame.draw.rect(self.scr, (140,255,124), pygame.Rect(75,237 - self.scroll,40,10))
			self.scr.blit(self.fnt.render(database.MENU[96] + ': ', True, (0,0,0)), (10, 233 - self.scroll))

			if opt == 7: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,258 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,258 - self.scroll,180,30))
			pygame.draw.rect(self.scr, (210, 210, 210), pygame.Rect(75,268 - self.scroll,80,10))
			if resources.HINT == False: pygame.draw.rect(self.scr, (255,61,61), pygame.Rect(115,268 - self.scroll,40,10))
			if resources.HINT == True: pygame.draw.rect(self.scr, (140,255,124), pygame.Rect(75,268 - self.scroll,40,10))
			self.scr.blit(self.fnt.render(database.MENU[97] + ': ', True, (0,0,0)), (10, 264 - self.scroll))

		if mnu == 2:
			self.scroll = 0
			if opt == 0: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,41 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 - self.scroll,180,30))
			pygame.draw.rect(self.scr, (210, 210, 210), pygame.Rect(60,51 - self.scroll,110,10))
			pygame.draw.rect(self.scr, (110, 110, 110), pygame.Rect(60 + (resources.SFX * 100),51 - self.scroll,10,10))
			self.scr.blit(self.fnt.render(database.MENU[63], True, (0,0,0)), (10, 49 - self.scroll))

			if opt == 1: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,72 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,72 - self.scroll,180,30))
			pygame.draw.rect(self.scr, (210, 210, 210), pygame.Rect(60,82 - self.scroll,110,10))
			pygame.draw.rect(self.scr, (110, 110, 110), pygame.Rect(60 + (resources.MSC * 100),82 - self.scroll,10,10))
			self.scr.blit(self.fnt.render(database.MENU[64], True, (0,0,0)), (10, 80 - self.scroll))

		if mnu == 3:
			if opt == 0:
				if self.scroll > 0:
					self.scroll -= 10
			elif opt == 5:
				if self.scroll < 60:
					self.scroll += 10
			elif opt == 2:
				if self.scroll > 0:
					self.scroll -= 10
			elif opt == 7:
				if self.scroll < 60:
					self.scroll += 10

			if opt == 0: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,41 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[65] + ': ' + pygame.key.name(resources.UP[0]), True, (0,0,0)), (10, 51 - self.scroll))
			elif opt == 0: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 51 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[65] + ': ' + pygame.key.name(resources.UP[0]), True, (0,0,0)), (10, 51 - self.scroll))

			if opt == 1: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,72 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,72 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[66] + ': ' + pygame.key.name(resources.DOWN[0]), True, (0,0,0)), (10, 82 - self.scroll))
			elif opt == 1: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 82 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[66] + ': ' + pygame.key.name(resources.DOWN[0]), True, (0,0,0)), (10, 82 - self.scroll))

			if opt == 2: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,103 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,103 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[67] + ': ' + pygame.key.name(resources.LEFT[0]), True, (0,0,0)), (10, 113 - self.scroll))
			elif opt == 2: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 113 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[67] + ': ' + pygame.key.name(resources.LEFT[0]), True, (0,0,0)), (10, 113 - self.scroll))
			
			if opt == 3: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,134 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,134 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[68] + ': ' + pygame.key.name(resources.RIGHT[0]), True, (0,0,0)), (10, 144 - self.scroll))
			elif opt == 3: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 144 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[68] + ': ' + pygame.key.name(resources.RIGHT[0]), True, (0,0,0)), (10, 144 - self.scroll))
			
			if opt == 4: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,165 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,165 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[69] + ': ' + pygame.key.name(resources.ACT[0]), True, (0,0,0)), (10, 175 - self.scroll))
			elif opt == 4: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 175 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[69] + ': ' + pygame.key.name(resources.ACT[0]), True, (0,0,0)), (10, 175 - self.scroll))

			if opt == 5: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,196 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,196 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[86] + ': ' + pygame.key.name(resources.RUN[0]), True, (0,0,0)), (10, 206 - self.scroll))
			elif opt == 5: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 206 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[86] + ': ' + pygame.key.name(resources.RUN[0]), True, (0,0,0)), (10, 206 - self.scroll))
			
			if opt == 6: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,227 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,227 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[70] + ': ' + pygame.key.name(resources.PHONE[0]), True, (0,0,0)), (10, 237 - self.scroll))
			elif opt == 6: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 237 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[70] + ': ' + pygame.key.name(resources.PHONE[0]), True, (0,0,0)), (10, 237 - self.scroll))
			
			if opt == 7: pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,258 - self.scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,258 - self.scroll,180,30))
			if trg == 0: self.scr.blit(self.fnt.render(database.MENU[71] + ': ' + pygame.key.name(resources.BAG[0]), True, (0,0,0)), (10, 268 - self.scroll))
			elif opt == 7: self.scr.blit(self.fnt.render(database.MENU[77], True, (0,0,0)), (10, 268 - self.scroll))
			else: self.scr.blit(self.fnt.render(database.MENU[71] + ': ' + pygame.key.name(resources.BAG[0]), True, (0,0,0)), (10, 268 - self.scroll))

		pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[13], True, (0, 0, 0)), (5, 5))

		return self.scr

	def info(self, opt):
		pygame.draw.rect(self.scr, (193, 193, 193), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render(database.MENU[14], True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,195))
		self.scr.blit(self.fnt.render(database.ABOUT[0], True, (0, 0, 0)), (40, 55))
		self.scr.blit(self.fnt.render(database.ABOUT[1], True, (0, 0, 0)), (15, 80))
		self.scr.blit(self.fnt.render(database.ABOUT[2], True, (0, 0, 0)), (15, 95))
		self.scr.blit(self.fnt.render(database.ABOUT[3], True, (0, 0, 0)), (15, 110))

		if opt == 0: pygame.draw.rect(self.scr, (193, 193, 193), pygame.Rect(5,139,170,20))
		else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,139,170,20))
		self.scr.blit(self.fnt.render(database.ABOUT[4], True, (0, 0, 0)), (10, 143))
		if opt == 1: pygame.draw.rect(self.scr, (193, 193, 193), pygame.Rect(5,160,170,20))
		else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,160,170,20))
		self.scr.blit(self.fnt.render(database.ABOUT[5], True, (0, 0, 0)), (10, 164))

		self.scr.blit(self.fnt.render(database.ABOUT[6], True, (0, 0, 0)), (20, 200))

		return self.scr

	def call(self, opt, nb):
		num = 0
		for i in database.NUMBERS:
			if i[1] == nb: break
			num += 1
		self.scr.blit(pygame.image.load('Backgrounds/call_' + nb + '.png'), (0, 90))
		pygame.draw.rect(self.scr, (resources.COLOR[0], resources.COLOR[1], resources.COLOR[2]), pygame.Rect(0,0,180,90))
		self.scr.blit(self.fnt.render(database.NUMBERS[num][0], True, (255, 255, 255)), (50, 10))
		self.scr.blit(self.fnt.render(nb, True, (255, 255, 255)), (50, 20))
		self.scr.blit(self.fnt.render(database.MENU[32] + str(resources.CREDIT), True, (255, 255, 255)), (50, 40))
		self.scr.blit(self.fnt.render(database.MENU[33], True, (255, 255, 255)), (50, 60))

		if opt == 0: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/cl_ys.png'), (40, 40)), (25, 185))
		else: self.scr.blit(pygame.image.load('Sprites/cl_ys.png'), (30, 190))
		if opt == 1: self.scr.blit(pygame.transform.scale(pygame.image.load('Sprites/cl_no.png'), (40, 40)), (125, 185))
		else: self.scr.blit(pygame.image.load('Sprites/cl_no.png'), (130, 190))

		return self.scr
