# -*- coding: utf-8 -*-
class Settings:
	def __init__(self):
		file = open('settings.db','r')
		self.lang = file.readline()[0:-1]
		self.sfx = file.readline()[0:-1]
		self.msc = file.readline()[0:-1]
		self.up = file.readline()[0:-1]
		self.down = file.readline()[0:-1]
		self.left = file.readline()[0:-1]
		self.right = file.readline()[0:-1]
		self.act = file.readline()[0:-1]
		self.phone = file.readline()[0:-1]
		self.inventory = file.readline()[0:-1]
		self.speed = file.readline()[0:-1]
		self.color = file.readline()
		file.close()

s = Settings()
if s.lang == 'PT': import database_PT as database
if s.lang == 'EN': import database_EN as database

import random
import pygame

class Inventory:
	def __init__(self):
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 10)
		self.invind = 0
		self.invfade = 0
		
	def show(self, opt, lopt, mn, fd):
		self.scr = pygame.Surface((400, 250))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,0,400,250))
		pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(5,5,390,240))
		x = 20
		y = 5
		xx = 0
		optx = 0
		opty = 0
		ind = 0
		scroll = 0
		if opt > 3: scroll += (opt - 3) * 60
		while ind < len(database.PLAYER):
			self.scr.blit(self.fnt.render(database.PLAYER[ind]['NAME'], True, (255, 255, 255)), (20 + xx * ind - scroll, 10))
			for j in database.INVENTORY[ind]:
				if database.INVENTORY[ind][0] != j:
					for i in j:
						if opt == optx and lopt == opty:
							pygame.draw.rect(self.scr, (255, 0, 0), pygame.Rect(x + xx - scroll,y,32,32))
						else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(x + xx - scroll,y,32,32))
						pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(x + xx + 2 - scroll,y + 2,28,28))
						if i != '_':self.scr.blit(pygame.image.load('Sprites/it_' + i + '.png'), (x + xx + 2 - scroll, y))
						x += 35
						optx += 1
				x = 20 + xx
				y += 35
				optx = 0
				opty += 1
			x = 20 + xx
			for e in database.EQUIPMENT[ind]:
				if opt == optx and lopt == opty: pygame.draw.rect(self.scr, (255, 0, 0), pygame.Rect(x + xx - scroll,200,32,32))
				else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(x + xx - scroll,200,32,32))
				pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(x + xx + 2 - scroll,202,28,28))
				if e[0] != '_':self.scr.blit(pygame.image.load('Sprites/it_' + e[0] + '.png'), (x + xx + 2 - scroll, 200))
				x += 35
				optx += 1
			x = 120
			y = 5

			if mn == 2:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect((opt * 35) + 120, (lopt * 35) + 45,160,50))
				pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect((opt * 35) + 122, (lopt * 35) + 50,156,46))
				pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect((opt * 35) + 122, (lopt * 35) + 50 + mn * 25,156,46))
				self.scr.blit(self.fnt.render('usar', True, (200, 200, 200)), ((opt * 35) + 127, (lopt * 35) + 52))
				self.scr.blit(self.fnt.render('trocar', True, (200, 200, 200)), ((opt * 35) + 127, (lopt * 35) + 52 + 28))
				self.scr.blit(self.fnt.render('descartar', True, (200, 200, 200)), ((opt * 35) + 127, (lopt * 35) + 52 + 52))

			ind += 1
			x = 20
			y = 5
			xx = 60 * (ind + 1)
			optx = 0
			opty = 0
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(xx * ind + 80 - scroll,10,3,230))

		return self.scr
			
	def add(self,item):
		i=0
		j=0
		trigg=False
		for y in database.INVENTORY[self.invind]:
			if database.INVENTORY[self.invind][0] != y:
				for x in y:
					if x=='_' and trigg==False:
						database.INVENTORY[self.invind][i][j] = item
						trigg=True
					j+=1
			i+=1
			j=0
			
	def drop(self,i,j):
		database.INVENTORY[self.invind][i][j] = '_'
		
	def info(self,i,j):
		for x in database.ITEMS:
			if x[0]==database.INVENTORY[self.invind][i][j]:
				str=x[0].upper()+'\n\n'+x[1]
				if x[2]==0:str+=' Descartável'
				if x[2]==1:str+=' Equipável'
				print(str)
				
	def equip(self,i,j,ind):
		item=databse.INVENTORY[invind][i][j]
		for x in database.ITEMS:
			if x[0]==item:
				if x[2]==1:
					database.INVENTORY[self.invind][i][j]=database.EQUIPMENT[ind]
					database.EQUIPMENT[ind]=item
		
	def move(self,ii,ij,iinv,fi,fj,finv):
		item = database.INVENTORY[iinv][ii][ij]
		database.INVENTORY[iinv][ii][ij] = database.INVENTORY[finv][fi][fj]
		database.INVENTORY[finv][fi][fj] = item

class Shop:
	def __init__(self):
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 10)
		
	def products(self, opt, lopt, lst):
		self.scr = pygame.Surface((400, 250))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,0,400,250))
		pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(5,5,390,240))

		self.scr.blit(self.fnt.render('$' + str(database.MONEY), True, (255, 255, 255)), (20, 10))

		y = 0
		for i in lst:
			if lopt == y:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,33 + (y * 12),370,12))
				self.scr.blit(self.fnt.render('$' + str(i[2]) + ' - ' + i[0], True, (0, 0, 0)), (20, 30 + (y * 12)))
				self.scr.blit(self.fnt.render(str(opt) + 'x', True, (0, 0, 0)), (360, 30 + (y * 12)))
			else:
				self.scr.blit(self.fnt.render('$' + str(i[2]) + ' - ' + i[0], True, (255, 255, 255)), (20, 30 + (y * 12)))
				self.scr.blit(self.fnt.render(str(opt) + 'x', True, (255, 255, 255)), (360, 30 + (y * 12)))
			y += 1

		if lopt != len(lst):
			l = 0
			for j in lst[lopt][1]:
				self.scr.blit(self.fnt.render(j, True, (255, 255, 255)), (20,200 + (l * 10)))
				l += 1

		if lopt == y:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,33 + (y * 12),370,12))
			self.scr.blit(self.fnt.render('sair', True, (0, 0, 0)), (20, 30 + (y * 12)))
		else: self.scr.blit(self.fnt.render('sair', True, (255, 255, 255)), (20, 30 + (y * 12)))

		return self.scr

	def buy(self, opt, lopt, lst):
		self.scr = pygame.Surface((400, 250))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,0,400,250))
		pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(5,5,390,240))

		self.scr.blit(self.fnt.render('$' + str(database.MONEY), True, (255, 255, 255)), (20, 10))

		y = 0
		cost = 0
		for i in lst:
			self.scr.blit(self.fnt.render('$' + str(i[2]) + ' - ' + i[0], True, (255, 255, 255)), (20, 30 + (y * 10)))
			cost += i[2]
			y += 1
		self.scr.blit(self.fnt.render('= -' + str(cost), True, (255, 255, 255)), (20, 30 + (y * 10)))
		if database.MONEY - cost >= 0: self.scr.blit(self.fnt.render('= ' + str(database.MONEY - cost), True, (255, 255, 255)), (20, 30 + (y * 30)))
		if database.MONEY - cost < 0: self.scr.blit(self.fnt.render('= ' + str(database.MONEY - cost), True, (255, 10, 10)), (20, 30 + (y * 30)))

		if lopt == 0:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,203,370,12))
			self.scr.blit(self.fnt.render('comprar', True, (0,0,0)), (20, 200))
		else: self.scr.blit(self.fnt.render('comprar', True, (255, 255, 255)), (20, 200))

		if lopt == 1:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,215,370,12)); tcol = (0,0,0)
			self.scr.blit(self.fnt.render('cancelar', True, (0, 0, 0)), (20, 212))
		else: self.scr.blit(self.fnt.render('cancelar', True, (255, 255, 255)), (20, 212))

		return self.scr

	def bank(self, opt, lopt, mn):
		self.scr = pygame.Surface((400, 250))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,0,400,250))
		pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(5,5,390,240))

		self.scr.blit(self.fnt.render('BANCO: $' + str(database.ATM), True, (255, 255, 255)), (20, 10))
		self.scr.blit(self.fnt.render('DINHEIRO: $' + str(database.MONEY), True, (255, 255, 255)), (20, 30))

		if mn == 2:
			if lopt == 0:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,203,370,12))
				self.scr.blit(self.fnt.render('sacar', True, (0,0,0)), (20, 200))
			else: self.scr.blit(self.fnt.render('sacar', True, (255, 255, 255)), (20, 200))

			if lopt == 1:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,215,370,12)); tcol = (0,0,0)
				self.scr.blit(self.fnt.render('depositar', True, (0, 0, 0)), (20, 212))
			else: self.scr.blit(self.fnt.render('depositar', True, (255, 255, 255)), (20, 212))

			if lopt == 2:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15,227,370,12)); tcol = (0,0,0)
				self.scr.blit(self.fnt.render('cancelar', True, (0, 0, 0)), (20, 224))
			else: self.scr.blit(self.fnt.render('cancelar', True, (255, 255, 255)), (20, 224))
		elif mn == 12:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(15 + (opt * 7),210,370,3))
			self.scr.blit(self.fnt.render(str(database.ATM), True, (255,255,255)), (20, 200))

		return self.scr

class Bestiary:
	def __init__(self):
		self.date = '03/03/03'
		self.freaks = database.FREAKS
		self.bestiary = []
		
	def add(self,ind):
		f=self.freaks[ind]
		f['DATE']=self.date
		id=len(self.bestiary)+1
		if id < 10:id='00'+str(id)
		elif id < 40:id='0'+str(id)
		f['ID']=id
		self.bestiary.append(f)

class Phone:
	def __init__(self):
		self.scr = pygame.Surface((180,250))
		self.fnt = pygame.font.Font('Fonts/monotype.ttf', 10)
		self.ttl = pygame.font.Font('Fonts/pixel-font.ttf', 25)
		self.dtt = pygame.font.Font('Fonts/datetype.ttf', 10)
		self.pbg = 2

	def apps(self, hr, dt, sg, bt, opt, lopt):
		scroll = 0
		if lopt > 2: scroll += (lopt - 2) * 60
		self.scr.blit(pygame.image.load('Backgrounds/phone_'+str(self.pbg)+'.png'), (0, 0))

		self.scr.blit(pygame.image.load('Sprites/ph.png'), (4 + opt * 60, 20 + lopt * 60 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_maps.png'), (7, 23 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_call.png'), (67, 23 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_mail.png'), (127, 23 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_news.png'), (7, 83 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_radi.png'), (67, 83 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_camr.png'), (127, 83 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_best.png'), (7, 143 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_task.png'), (67, 143 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_stts.png'), (127, 143 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_achi.png'), (7, 203 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_rank.png'), (67, 203 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_help.png'), (127, 203 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_sett.png'), (7, 263 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_info.png'), (67, 263 - scroll))
		self.scr.blit(pygame.image.load('Sprites/ph_save.png'), (127, 263 - scroll))

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,0,180,18))
		hour = ['','']
		if hr[0] < 10: hour[0] = '0' + str(hr[0])
		else: hour[0] = str(hr[0])
		if hr[1] < 10: hour[1] = '0' + str(hr[1])
		else: hour[1] = str(hr[1])
		self.scr.blit(self.dtt.render(hour[0] + ':' + hour[1], True, (255, 255, 255)), (75, 4))
		day = ['','','']
		if dt[0] < 10: day[0] = '0' + str(dt[0])
		else: day[0] = str(dt[0])
		if dt[1] < 10: day[1] = '0' + str(dt[1])
		else: day[1] = str(dt[1])
		if dt[2] < 10: day[2] = '0' + str(dt[2])
		else: day[2] = str(dt[2])
		self.scr.blit(self.dtt.render(day[0] + '/' + day[1] + '/' + day[2], True, (255, 255, 255)), (3, 4))

		self.scr.blit(pygame.image.load('Sprites/signal_' + str(sg) + '.png'), (130, 6))
		self.scr.blit(pygame.image.load('Sprites/battery_' + str(bt) + '.png'), (150, 2))

		return self.scr

	def map(self, mp, x, y, zoom, sg):
		if sg > 0:
			mim = pygame.image.load('Maps/' + mp +'.png')
			pygame.transform.scale(mim, (zoom,zoom))
			self.scr.blit(mim, (int(-x) + 50, int(-y) + 50))
		else: self.scr.blit(self.fnt.render('sem conexão', True, (255, 255, 255)), (25, 200))

		pygame.draw.rect(self.scr, (140, 255, 253), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('map', True, (0, 0, 0)), (5, 5))

		return self.scr

	def contacts(self, flt, opt, mnu):
		if flt == 0: em = database.CONTACTS
		if flt == 1: em = database.CONTACTS
		if flt == 2: em = database.CALLHIST

		scroll = 0
		if opt > 2: scroll += (opt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if mnu == 0:
			y = 0
			for i in em:
				if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - scroll,180,50))
				else: pygame.draw.rect(self.scr, (15, 255, 0), pygame.Rect(0,66 + y - scroll,180,50))
				self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 76 + y - scroll))
				if flt == 1: self.scr.blit(self.fnt.render(i[1], True, (0, 0, 0)), (10, 86 + y - scroll))
				if flt == 2: self.scr.blit(pygame.image.load('Sprites/who_' + str(i[1]).lower() + '.png'), (160, 86 + y - scroll))
				y += 51
			if y == 0:
				self.scr.blit(self.fnt.render('não há contatos', True, (255, 255, 255)), (50, 140))

			pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
			if flt == 0:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,45,60,20))
				self.scr.blit(self.fnt.render('telefone', True, (0, 0, 0)), (8, 47))
			else: self.scr.blit(self.fnt.render('telefone', True, (255, 255, 255)), (8, 47))
			if flt == 1:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(60,45,60,20))
				self.scr.blit(self.fnt.render('contatos', True, (0, 0, 0)), (70, 47))
			else: self.scr.blit(self.fnt.render('contatos', True, (255, 255, 255)), (70, 47))
			if flt == 2:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(120,45,60,20))
				self.scr.blit(self.fnt.render('histórico', True, (0, 0, 0)), (130, 47))
			else: self.scr.blit(self.fnt.render('histórico', True, (255, 255, 255)), (130, 47))

		elif mnu == 1:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
			self.scr.blit(self.fnt.render(em[opt][0], True, (0, 0, 0)), (15, 55))
			self.scr.blit(self.fnt.render(em[opt][1], True, (0, 0, 0)), (15, 90))
			self.scr.blit(self.fnt.render('créditos: ' + str(database.CREDIT), True, (0, 0, 0)), (15, 120))
			self.scr.blit(self.fnt.render('chamando...', True, (0, 0, 0)), (15, 140))

		pygame.draw.rect(self.scr, (15, 255, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('contacts', True, (0, 0, 0)), (5, 5))

		return self.scr

	def call(self,nb,sc,who,pay):
		for i in database.CONTACTS:
			if nb == i[1]:
				if pay==False:
					if database.CREDIT > 0:
						database.CREDIT -= 1
						database.CALLHIST.insert(0,[nb,who])
						return database.DIALOGS[nb][sc]
						break
					else:
						return ['Sem créditos...']
				if pay==True:
					if database.MONEY > 0:
						database.MONEY -= 5
						database.CALLHIST.insert(0,[nb,who])
						return database.DIALOGS[nb][sc]
						break
					else:
						return ['Sem dinheiro...']

	def email(self, flt, opt, mnu, sg):
		self.e_read = []
		self.e_unread = []
		for i in database.EMAILS:
			if i[3] == True:
				self.e_read.append(i)
			if i[3] == False:
				self.e_unread.append(i)
				
		if flt == 0: em = self.e_unread
		if flt == 1: em = self.e_read
		if flt == 2: em = database.EMAILS

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0:
			if mnu == 0:
				scroll = 0
				if opt > 2: scroll += (opt - 2) * 51

				y = 0
				for i in em:
					if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - scroll,180,50))
					else: pygame.draw.rect(self.scr, (255, 221, 0), pygame.Rect(0,66 + y,180,50))
					self.scr.blit(self.fnt.render(i[1], True, (0, 0, 0)), (10, 76 + y - scroll))
					self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 86 + y - scroll))
					y += 51
				if y == 0:
					self.scr.blit(self.fnt.render('não há mensagens', True, (255, 255, 255)), (255, 140))

				pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
				if flt == 0:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,45,60,20))
					self.scr.blit(self.fnt.render('novas', True, (0, 0, 0)), (12, 47))
				else: self.scr.blit(self.fnt.render('novas', True, (255, 255, 255)), (12, 47))
				if flt == 1:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(60,45,60,20))
					self.scr.blit(self.fnt.render('lidas', True, (0, 0, 0)), (75, 47))
				else: self.scr.blit(self.fnt.render('lidas', True, (255, 255, 255)), (75, 47))
				if flt == 2:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(120,45,60,20))
					self.scr.blit(self.fnt.render('todas', True, (0, 0, 0)), (132, 47))
				else: self.scr.blit(self.fnt.render('todas', True, (255, 255, 255)), (132, 47))

			elif mnu > 0:
				scroll = (mnu - 1) * 3
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
				self.scr.blit(self.fnt.render(em[opt][1], True, (0, 0, 0)), (15, 55 - scroll))
				self.scr.blit(self.fnt.render('DE: ' + em[opt][0], True, (0, 0, 0)), (15, 85 - scroll))
				self.scr.blit(self.fnt.render('PARA: ' + (database.PLAYER[0]['NAME'] + database.PLAYER[0]['LASTNAME']).lower() + '@cmail.com', True, (0, 0, 0)), (15, 100 - scroll))
				y = 0
				for l in em[opt][2]:
					self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (15, 130 + y - scroll))
					y += 15
		else: self.scr.blit(self.fnt.render('sem conexão', True, (255, 255, 255)), (25, 200))

		pygame.draw.rect(self.scr, (255, 221, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('email', True, (0, 0, 0)), (5, 5))

		return self.scr

	def news(self, opt, mnu, sg):
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		print(mnu)
		print(opt)
		if sg > 0:
			if mnu == 0:
				scroll = 0
				if opt > 2: scroll += (opt - 2) * 51
				y = 0
				hei = 0
				for i in database.NEWS[database.DATE[0] - 1]:
					for l in i[0]: hei += 20
					hei += 20
					if opt != y: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + (y * hei) - scroll,180,50 + (y * hei)))
					else: pygame.draw.rect(self.scr, (219, 49, 37), pygame.Rect(0,41 + (y * hei),180,50 + (y * hei)))
					yi = 0
					for l in i[0]:
						self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 46 + (y * hei) - scroll + yi))
						yi += 15
					self.scr.blit(self.fnt.render(i[1], True, (0, 0, 0)), (10, 52 + (y * hei) - scroll + yi))
					y += 1
					hei = 0

			elif mnu > 0:
				scroll = (mnu - 1) * 3
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
				y = 0
				for l in database.NEWS[database.DATE[0] - 1][opt][0]:
					self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 50 + y - scroll))
					y += 15
				self.scr.blit(self.fnt.render(database.NEWS[database.DATE[0] - 1][opt][1], True, (0, 0, 0)), (10, 55 + y - scroll))
				for l in database.NEWS[database.DATE[0] - 1][opt][2]:
					self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 100 + y - scroll))
					y += 15
		else: self.scr.blit(self.fnt.render('sem conexão', True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (219, 49, 37), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('news', True, (0, 0, 0)), (5, 5))

		return self.scr

	def radio(self, fm, msc):
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if fm/10 in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
			if database.RADIO[str(round(fm/10))] != []:
				pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66,180,50))
				pygame.draw.rect(self.scr, (255, 0, 135), pygame.Rect(0,66,180,50))
				self.scr.blit(self.fnt.render(database.RADIO[str(round(fm/10))][msc][:-4], True, (0, 0, 0)), (10, 76))
			else: self.scr.blit(self.fnt.render('sem sinal', True, (255, 255, 255)), (70, 140))
		else: self.scr.blit(self.fnt.render('sem sinal', True, (255, 255, 255)), (70, 140))

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
		f = 0
		for i in range(18):
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0 + f,50,1,16))
			f += 10
		pygame.draw.rect(self.scr, (255, 0, 0), pygame.Rect(0 + fm,50,4,16))
		self.scr.blit(self.fnt.render(str(fm/10), True, (255, 255, 255)), (70, 20))

		pygame.draw.rect(self.scr, (255, 0, 135), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('radio', True, (0, 0, 0)), (5, 5))

		return self.scr

	def camera(self):
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('camera', True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		return self.scr

	def bestiary(self, opt, lopt, mnu, sg):
		scroll = 0
		if opt > 2: scroll += (opt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0:
			if len(database.BESTIARY) > 0:
				if mnu == 0:
					y = 0
					for i in database.BESTIARY:
						if lopt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y - scroll,180,50))
						else: pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(0,41 + y - scroll,180,50))
						self.scr.blit(self.fnt.render(i['NAME'], True, (0, 0, 0)), (10, 51 + y - scroll))
						y += 51

				if mnu == 1:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
					pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(5,243,83,3))
					self.scr.blit(self.fnt.render(database.BESTIARY[opt]['NAME'], True, (0, 0, 0)), (10, 55))
					self.scr.blit(pygame.image.load('Sprites/' + database.BESTIARY[opt]['NAME'] + '_stand.png'), (60, 70))
					self.scr.blit(self.fnt.render('ID: ' + database.BESTIARY[opt]['ID'], True, (0, 0, 0)), (10, 160))
					self.scr.blit(self.fnt.render('RG: ' + database.BESTIARY[opt]['DATE'], True, (0, 0, 0)), (50, 160))
					self.scr.blit(self.fnt.render('HG: ' + database.BESTIARY[opt]['HEIGHT'], True, (0, 0, 0)), (100, 160))

					j = 0
					for l in database.BESTIARY[opt]['INFO']:
						self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 170 + j))
						j += 15

				if mnu == 2:
					pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
					pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(92,243,83,3))
					pygame.draw.rect(self.scr, (0, 0, 0), pygame.Rect(10,50,160,77))

					y = 0
					for i in database.BESTIARY[opt]['HABILITIES']:
						if lopt != y/19: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(11,51 + y,158,18))
						else: pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(11,51 + y,158,18))
						self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (20, 53 + y))
						y += 19

					j = 0
					for l in database.BESTIARY[opt]['HABILITIES'][lopt][1]:
						self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (10, 140 + j))
						j += 15

					if database.BESTIARY[opt]['HABILITIES'][lopt][3] == 1: dmg = 'VITALIDADE: ' + str(database.BESTIARY[opt]['HABILITIES'][lopt][2])
					if database.BESTIARY[opt]['HABILITIES'][lopt][3] == 2: dmg = 'ATAQUE: ' + str(database.BESTIARY[opt]['HABILITIES'][lopt][2])
					if database.BESTIARY[opt]['HABILITIES'][lopt][3] == 3: dmg = 'AGILIDADE: ' + str(database.BESTIARY[opt]['HABILITIES'][lopt][2])
					if database.BESTIARY[opt]['HABILITIES'][lopt][3] == 4:
						if database.BESTIARY[opt]['HABILITIES'][lopt][2] == 1: dmg = 'VENENO'
						if database.BESTIARY[opt]['HABILITIES'][lopt][2] == 1: dmg = 'NÁUSEA'

					self.scr.blit(self.fnt.render(dmg, True, (0, 0, 0)), (20, 210))
			else: self.scr.blit(self.fnt.render('nenhuma anomalia registrada', True, (255, 255, 255)), (10, 140))
		else: self.scr.blit(self.fnt.render('sem conexão', True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (134, 0, 211), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('bestiary', True, (0, 0, 0)), (5, 5))

		return self.scr

	def task(self, flt, opt, mnu):
		self.t_unmark = []
		self.t_mark = []
		for i in database.TASKS:
			if i[1] == True:
				self.t_mark.append(i)
			if i[1] == False:
				self.t_unmark.append(i)

		if flt == 0: em = self.t_unmark
		if flt == 1: em = self.t_mark
		if flt == 2: em = database.TASKS

		scroll = 0
		if opt > 4: scroll += (opt - 4) * 31
			
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		y = 0
		for i in em:
			if opt != y/31: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - scroll,180,30))
			else: pygame.draw.rect(self.scr, (255, 123, 0), pygame.Rect(0,66 + y - scroll,180,30))
			self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 73 + y - scroll))
			y += 31
		if y == 0:
			self.scr.blit(self.fnt.render('não há tarefas', True, (255, 255, 255)), (45, 140))

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,26))
		if flt == 0:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,45,60,20))
			self.scr.blit(self.fnt.render('fazer', True, (0, 0, 0)), (12, 47))
		else: self.scr.blit(self.fnt.render('fazer', True, (255, 255, 255)), (12, 47))
		if flt == 1:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(60,45,60,20))
			self.scr.blit(self.fnt.render('feitas', True, (0, 0, 0)), (75, 47))
		else: self.scr.blit(self.fnt.render('feitas', True, (255, 255, 255)), (75, 47))
		if flt == 2:
			pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(120,45,60,20))
			self.scr.blit(self.fnt.render('todas', True, (0, 0, 0)), (132, 47))
		else: self.scr.blit(self.fnt.render('todas', True, (255, 255, 255)), (132, 47))

		pygame.draw.rect(self.scr, (255, 123, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('tasks', True, (0, 0, 0)), (5, 5))

		return self.scr

	def status(self, p):
		pygame.draw.rect(self.scr, (150, 150, 150), pygame.Rect(40,0,400,140))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(45,5,390,130))
		self.scr.blit(self.fnt.render(database.PLAYER[p]['NAME']+' '+database.PLAYER[p]['LASTNAME'], True, (0, 0, 0)), (115, 75))
		self.scr.blit(pygame.image.load('Sprites/gn_' + database.PLAYER[p]['GENDER'] + '.png'), (115, 125))
		self.scr.blit(self.fnt.render(str(database.PLAYER[p]['ID']), True, (0, 0, 0)), (150, 50))
		self.scr.blit(self.fnt.render(database.PLAYER[p]['BLOOD'], True, (0, 0, 0)), (115, 150))
		self.scr.blit(self.fnt.render(database.PLAYER[p]['CIVIL'], True, (0, 0, 0)), (170, 150))

		return self.scr

	def achievements(self, opt, sg):
		scroll = 0
		if opt > 2: scroll += (opt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0:
			y = 0
			for i in database.ACHIEVEMENTS:
				if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,66 + y - scroll,180,50))
				else: pygame.draw.rect(self.scr, (255, 191, 0), pygame.Rect(0,66 + y - scroll,180,50))
				self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 76 + y - scroll))
				self.scr.blit(self.fnt.render(i[1], True, (0, 0, 0)), (10, 86 + y - scroll))
				y += 51

		else: self.scr.blit(self.fnt.render('sem conexão', True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (255, 191, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('achievements', True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		return self.scr

	def ranking(self, opt, sg):
		scroll = 0
		if opt > 2: scroll += (opt - 2) * 51

		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if sg > 0: pass
		else: self.scr.blit(self.fnt.render('sem conexão', True, (255, 255, 255)), (25, 140))

		pygame.draw.rect(self.scr, (55, 255, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('rank', True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		return self.scr

	def help(self, opt, mnu):
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		if mnu == 0:
			scroll = 0
			if opt > 2: scroll += (opt - 2) * 51
			y = 0
			for i in database.MANUAL:
				if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y - scroll,180,50))
				else: pygame.draw.rect(self.scr, (137, 50, 0), pygame.Rect(0,41 + y - scroll,180,50))
				self.scr.blit(self.fnt.render(i[0], True, (0, 0, 0)), (10, 51 + y - scroll))
				y += 51

		if mnu > 0:
			scroll = (mnu - 1) * 3
			pygame.draw.rect(self.scr,(255, 255, 255), pygame.Rect(5,45,170,200))
			self.scr.blit(self.fnt.render(database.MANUAL[opt][0], True, (0, 0, 0)), (70, 55 - scroll))
			y = 0
			for l in database.MANUAL[opt][1]:
				self.scr.blit(self.fnt.render(l, True, (0, 0, 0)), (15, 80 + y - scroll))
				y += 15

		pygame.draw.rect(self.scr, (137, 50, 0), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('help', True, (0, 0, 0)), (5, 5))

		return self.scr

	def settings(self, opt):
		pygame.draw.rect(self.scr, (91, 91, 91), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('settings', True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		return self.scr

	def info(self, opt):
		pygame.draw.rect(self.scr, (193, 193, 193), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('info', True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,45,170,200))
		self.scr.blit(self.fnt.render('MUTATION PURGE', True, (0, 0, 0)), (40, 55))
		self.scr.blit(self.fnt.render('Criado por Matt Kai', True, (0, 0, 0)), (15, 80))
		self.scr.blit(self.fnt.render('Source code por Matt Kai', True, (0, 0, 0)), (15, 95))
		self.scr.blit(self.fnt.render('Feito em Python', True, (0, 0, 0)), (15, 110))

		if opt == 0: pygame.draw.rect(self.scr, (193, 193, 193), pygame.Rect(5,160,170,20))
		else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,160,170,20))
		self.scr.blit(self.fnt.render('Twitter', True, (0, 0, 0)), (10, 164))
		if opt == 1: pygame.draw.rect(self.scr, (193, 193, 193), pygame.Rect(5,181,170,20))
		else: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(5,181,170,20))
		self.scr.blit(self.fnt.render('GitHub', True, (0, 0, 0)), (10, 185))

		self.scr.blit(self.fnt.render('GNU General Public License', True, (0, 0, 0)), (20, 220))

		return self.scr

	def save(self, opt, sg):
		pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,0,180,40))
		self.scr.blit(self.ttl.render('save', True, (0, 0, 0)), (5, 5))
		pygame.draw.rect(self.scr, (10, 10, 10), pygame.Rect(0,40,180,210))

		if sg > 0:
			y = 0
			for i in range(1,4):
				file = open(str(i)+'userdata.db','r')
				sc = int(file.readline()[0:-1])
				dy = int(file.readline()[0:-1])
				mt = int(file.readline()[0:-1])
				file.close()
				if opt != y/51: pygame.draw.rect(self.scr, (255, 255, 255), pygame.Rect(0,41 + y,180,50))
				else: pygame.draw.rect(self.scr, (255, 255, 10), pygame.Rect(0,41 + y,180,50))
				self.scr.blit(self.fnt.render(str(database.CHAPTERS[sc]), True, (0, 0, 0)), (10, 51 + y))
				self.scr.blit(self.fnt.render(str(dy) + ':' + str(mt), True, (0, 0, 0)), (130, 51 + y))
				y += 51
		else: self.scr.blit(self.fnt.render('sem conexão', True, (255, 255, 255)), (25, 140))

		return self.scr
