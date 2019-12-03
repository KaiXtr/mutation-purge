# -*- coding: utf-8 -*-
import database
import menu

import pygame
import pytmx
import random
import sys

class TiledMap():
    def __init__(self):
        self.gameMap = pytmx.load_pygame("Maps/city.tmx", pixelalpha=True)
        self.mapwidth = self.gameMap.tilewidth * self.gameMap.width
        self.mapheight = self.gameMap.tileheight * self.gameMap.height

    def render(self, surface):
        for layer in self.gameMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.gameMap.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))

    def make_map(self):
        mapSurface = pygame.Surface((self.mapwidth, self.mapheight))
        self.render(mapSurface)
        return mapSurface

	def rendermap(self, mp):
		self.map = pytmx.load_pygame('Maps/'+mp+'.tmx')
		self.tilmap = pygame.Surface((self.map.width*self.map.tilewidth,self.map.height*self.map.tileheight))
		for x in range(0, self.map.width):
			for y in range(0, self.map.height):
				self.tilmap.blit(self.map.get_tile_image(x, y, 0), (x*self.map.tilewidth-self.cam_x, y*self.map.tileheight-self.cam_y))
class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		self.display = pygame.Surface((600, 400))
		pygame.display.set_caption('Mutation Purge')
		self.dlgt = 50
		self.FPS = 60

		self.sound = False
		self.pressed = pygame.key.get_pressed()
		self.font = pygame.font.SysFont("calibri", 30)
		self.cam_x = 0
		self.cam_y = 0

		self.dlg = ''
		self.battle = False
		self.bbg = ''
		self.btime = 100
		self.hits = 0
		self.tdmg = 0
		self.hpl = 0
		self.tbt = 0
		self.inventory = False
		self.phone = 0
		self.winbar = 0
		self.turn = -1
		self.opt = 1
		self.mnu = 1
		self.aimx = 300
		self.pp=[]
		x=0
		for i in database.PLAYER:
			self.pp.append([])
			for j in database.EQUIPMENT[x]:
				try:self.pp[x].append(j[1]['CAPACITY'])
				except:pass
			self.pp[x].append(0)
			self.pp[x].append(0)
			x+=1
		self.player_rect = pygame.Rect(100,100,10,16)
		self.player_spd = 3
		self.player_sprite = [pygame.image.load('Sprites/hero_walkD_0.png')]
		self.player_gif = 1
		self.player_mov = False
		self.player_color = (100, 100, 100)

		self.en = []
		self.en_rect = pygame.Rect(0,0,10,16)
		self.en.append(database.FREAKS[0])
		self.en[0]['HP'] = self.en[0]['MAXHP']
		self.en[0]['SPRITE']=pygame.image.load('Sprites/' + (self.en[0]['NAME']).lower() + '_stand.png')
		self.en.append(database.FREAKS[0])
		self.en[1]['HP'] = self.en[1]['MAXHP']
		self.en[1]['SPRITE']=pygame.image.load('Sprites/' + (self.en[1]['NAME']).lower() + '_stand.png')

		TiledMap().rendermap('city')

		pygame.mixer.music.load('Music/City.mp3')
		if self.sound == True: pygame.mixer.music.play(-1)

	def enemy(self, frk):
		if self.en_rect.x - self.cam_x < self.player_rect.x - self.cam_x: self.en_rect.x+=2
		if self.en_rect.x - self.cam_x > self.player_rect.x - self.cam_x: self.en_rect.x-=2
		if self.en_rect.y - self.cam_y < self.player_rect.y - self.cam_y: self.en_rect.y+=2
		if self.en_rect.y - self.cam_y > self.player_rect.y - self.cam_y: self.en_rect.y-=2

		if self.colide(self.en_rect, self.player_rect) == True:
			self.patt=[]
			self.pagi=[]
			self.tatt=[]
			self.tagi=[]
			self.player_mov = False
			self.opt = 0
			self.bbg = pygame.image.load('Backgrounds/mountains.png')
			for i in database.PLAYER:
				self.patt.append(i['ATTACK'][i['LEVEL']])
				self.pagi.append(i['AGILITY'][i['LEVEL']])
				self.tatt.append(0)
				self.tagi.append(0)
			self.battle = True
			self.transiction(True, 100)
			self.dialog([self.en[0]['NAME'] + ' aparece!!']); self.turn=0

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/' + (self.en[0]['NAME']).lower() + '_mini.png'), (self.en_rect.x - self.cam_x, self.en_rect.y - self.cam_y))

	def npc(self, x, y, ndg):
		rect = pygame.Rect(x,y,60,60)
		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[pygame.K_SPACE]:
					self.dialog(database.DIALOGS['NPC_'+str(ndg)][0])

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/npc.png'), (rect.x+30-self.cam_x, rect.y+30-self.cam_y))

	def chest(self, x, y, rwd):
		rect = pygame.Rect(x,y,60,60)
		if self.colide(self.player_rect, rect) == True:
			for event in pygame.event.get():
				if self.pressed[pygame.K_SPACE]:
					self.dialog(['Você achou '+rwd])
					menu.Inventory().add(rwd)

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/chest.png'), (rect.x+30-self.cam_x, rect.y+30-self.cam_y))

	def portal(self, x, y, mp):
		rect = pygame.Rect(x,y,20,40)
		if self.colide(self.player_rect, rect) == True:
			self.rendermap(mp)

		if self.battle == False: self.display.blit(pygame.image.load('Sprites/door.png'), (rect.x-self.cam_x, rect.y-self.cam_y))

	def colide(self, i1, i2):
		if i1.x - self.cam_x > i2.x - self.cam_x and i1.x - self.cam_x < i2.x - self.cam_x + i2.width or i1.x - self.cam_x + i1.width > i2.x - self.cam_x and i1.x - self.cam_x + i1.width < i2.x - self.cam_x + i2.width:
			if i1.y - self.cam_y > i2.y - self.cam_y and i1.y - self.cam_y < i2.y - self.cam_y + i2.height or i1.y - self.cam_y + i1.height > i2.y - self.cam_y and i1.y - self.cam_y + i1.height < i2.y - self.cam_y + i2.height:
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
					#DEBUG
					if self.pressed[pygame.K_UP]: database.PLAYER[self.turn]['LEVEL'] += 1

					if self.pressed[pygame.K_SPACE]:
						self.fight(self.turn)
						self.turn += 1
						self.mnu = 1
						if self.turn == len(database.PLAYER):
							self.fight(self.turn)
				elif self.mnu == 1:
					if self.pressed[pygame.K_LEFT]: self.opt -=1
					if self.pressed[pygame.K_RIGHT]: self.opt +=1
				
					if self.opt < 0: self.opt = 4
					if self.opt > 4: self.opt = 0

					if self.pressed[pygame.K_SPACE]:
						if self.opt < 4:
							if self.pp[self.turn][self.opt] > 0:
								self.mnu = 2
							else:
								self.dialog(['Você não tem munição!'])
						elif self.opt == 4:
							self.fight(self.turn)
							self.fight(len(database.PLAYER))

			#MENU OPTIONS
			if self.pressed[pygame.K_RETURN]:
				self.inventory = not self.inventory
				if self.inventory == False: self.player_spd = 3
				if self.inventory == True: self.player_spd = 0

			if self.inventory == True:
				if self.pressed[pygame.K_LEFT]: self.opt -=1
				if self.pressed[pygame.K_RIGHT]: self.opt +=1

				if self.opt < 0: self.opt = 0
				#if self.opt > 4: self.opt = 0

			if self.pressed[pygame.K_BACKSPACE]: self.phone += 1

		#PLAYER MOVEMENT
		if self.battle == False:
			self.player_mov = False
			self.pressed = pygame.key.get_pressed()
			if self.pressed[pygame.K_UP]: self.player_mov = True; self.player_rect.y -= self.player_spd; self.player_sprite = database.SPRITES['UP_Sid']
			elif self.pressed[pygame.K_DOWN]: self.player_mov = True; self.player_rect.y += self.player_spd; self.player_sprite = database.SPRITES['DOWN_Sid']
			if self.pressed[pygame.K_LEFT]: self.player_mov = True; self.player_rect.x -= self.player_spd; self.player_sprite = database.SPRITES['LEFT_Sid']
			elif self.pressed[pygame.K_RIGHT]: self.player_mov = True; self.player_rect.x += self.player_spd; self.player_sprite = database.SPRITES['RIGHT_Sid']

	def dialog(self, txt):
		dlg = ''
		ind = 0
		#self.draw()
		pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(100,60,1000,200))
		pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(105,65,990,190))
		for l in txt:
			for i in l:
				dlg+=i
				self.screen.blit(self.font.render(dlg, True, (200, 200, 200)), (150, 110 + ind))
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

	def fight(self, turn):
		#PLAYERS TURN
		if turn < len(database.PLAYER):
			self.mnu = 3
			if self.opt < 4:
				self.pp[self.turn][self.opt] -= 1
				if self.aimx > 299 and self.aimx < 351:
					dmg = int(random.randint(database.EQUIPMENT[self.turn][self.opt][1]['DAMAGE'] - 2, database.EQUIPMENT[self.turn][self.opt][1]['DAMAGE'] + 2))
					self.en[self.turn]['SPRITE']=pygame.image.load('Sprites/' + (self.en[self.turn]['NAME']).lower() + '_damage.png')
					self.dialog([self.en[self.turn]['NAME'] + ' tomou ' + str(dmg) + ' de dano'])
					self.en[self.turn]['HP'] -= dmg
					self.hits += 1
					self.tdmg += dmg
				else: self.dialog(['errou...'])

			elif self.opt == 4:
				self.dialog([database.PLAYER[self.turn]['NAME'] + ' tenta fugir'])
				run = round(random.randint(0,100))
				if run > 49:
					self.dialog(['...e consegue!'])
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
					self.dialog(['Mas não conseguiu...'])

			#CHECK WIN - LEVEL UP
			if self.en[self.turn]['HP'] <= 0:
				self.dialog([self.en[self.turn]['NAME'] + ' foi derrotado'])
				pygame.mixer.Sound('SFX/victory.ogg').play()
				self.transiction(True, 210)
				self.tbt += round(self.btime/10)
				xp = ((self.hits*self.tdmg)-self.hpl+self.tbt)/len(database.PLAYER)
				self.dialog(['VITÓRIA','hits: '+str(self.hits),'x total damage: '+str(self.tdmg),'- lost vitality: '+str(self.hpl),'+ time bonus: '+str(self.tbt),'players: '+str(len(database.PLAYER)),'= '+str(xp)+' experience'])
				database.PLAYER[self.turn]['XP'] += xp
				if database.PLAYER[self.turn]['XP'] >= database.PLAYER[self.turn]['MAXXP']:
					database.PLAYER[self.turn]['LEVEL'] += 1
					database.PLAYER[self.turn]['XP'] = 1
					database.PLAYER[self.turn]['MAXXP'] *= 2
					self.dialog(['SUBIU PARA O NÍVEL ' + str(database.PLAYER[self.turn]['LEVEL'])])
				self.turn = 0
				self.hits = 0
				self.tdmg = 0
				self.hpl = 0
				self.tbt = 0
				self.battle = False
				self.opt = 1
				self.transiction(False, 0)
			self.mnu = 0

		#ENEMIES TURN
		else:
			self.tbt += round(self.btime/10)
			self.btime = 100
			self.turn = 0
			self.mnu = 3
			for i in self.en:
				opt = int(random.randint(0,4))
				if opt > 3:opt = 3
				act=i['HABILITIES'][opt]
				dd=i['NAME'] + ' usa ' + act[0]
				i['SPRITE']=pygame.image.load('Sprites/' + (i['NAME']).lower() + '_attack.png')
				pl=int(random.randint(0,len(database.PLAYER)-1))
				if act[3] == 2 and self.tatt ==2: act=i['HABILITIES'][0]
				if act[3] == 3 and self.tagi ==2: act=i['HABILITIES'][0]

				if act[3] == 1:
					if act[2] < 0:
						database.PLAYER[pl]['HP']+=act[2]
						self.dialog([dd, database.PLAYER[pl]['NAME'] + ' tomou ' + str(act[2]) + ' de dano'])
						self.hpl += act[2]
					elif act[2] > 0:
						i['HP'] += act[2]
				elif act[3] == 2:
					if act[2] < 0:
						if self.tatt[pl] < 2:
							self.patt[pl] += act[2]
							self.dialog([dd, database.PLAYER[pl]['NAME'] + ' perdeu ' + str(act[2]) + ' de ATAQUE'])
							self.tatt[pl] += 1
					elif act[2] > 0:
						act[2] += act[2]
				elif act[3] == 3:
					if act[2] < 0:
						if self.tagi[self.turn]<2:
							self.pagi[self.turn]+=act[2]
							self.dialog([dd, database.PLAYER[pl]['NAME'] + ' perdeu ' + str(act[2]) + ' de AGILIDADE'])
							self.tagi[self.turn]+=1
					elif act[2] > 0:
						i['AGILITY']+=act[2]
				elif act[3] == 4:	
					database.PLAYER[pl]['HEALTH']=act[2]
					if act[2] == 1:self.dialog([dd, database.PLAYER[pl]['NAME'] + ' foi envenenado'])
					if act[2] == 2:self.dialog([dd, database.PLAYER[pl]['NAME'] + ' está com náusea'])

				if database.PLAYER[pl]['HP'] <= 0:
					self.dialog([database.PLAYER[pl]['NAME'] + ' desmaiou...'])
					self.transiction(True, 200)
					self.turn = 0
					self.battle = False
					database.PLAYER[pl]['HP'] = database.PLAYER[pl]['MAXHP']
					database.PLAYER[pl]['BARHP'] = database.PLAYER[pl]['MAXHP']

				i['SPRITE']=pygame.image.load('Sprites/' + (i['NAME']).lower() + '_stand.png')
			self.turn = 0
			self.mnu = 1
			self.aimx = 100 + database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]

	def draw(self):
		self.display.fill((0, 0, 200))
		self.screen.blit(self.tilmap, (0-self.cam_x, 0-self.cam_y))

		#BATTLE
		if self.battle == True:
			self.display.blit(self.bbg, (0, 0))
			enx=0
			for i in self.en:
				self.display.blit(i['SPRITE'], (230+enx, 180))
				print(str(enx)+'- '+str(i['HP']))
				enx+=80

			#BLACK BARS
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,0,600,self.winbar))
			pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(0,400,600,-self.winbar))

			#PLAYER BARS
			if self.winbar==100:
				if self.turn < len(database.PLAYER) and self.turn!=-1:
					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,10,100,20))
					while float(database.PLAYER[0]['BARHP']) > float(database.PLAYER[0]['HP']):
						#database.PLAYER[0]['BARHP'] -= ['RESISTANCE'][database.PLAYER[0]['LEVEL']]
						if database.PLAYER[0]['BARHP']>0:pygame.draw.rect(self.display, (255, 255, 0), pygame.Rect(10,10,int(100/(database.PLAYER[0]['MAXHP']/database.PLAYER[0]['BARHP'])),20))
					if database.PLAYER[0]['HP']>database.PLAYER[0]['MAXHP']/5:pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(10,10,int(100/(database.PLAYER[0]['MAXHP']/database.PLAYER[0]['HP'])),20))
					elif database.PLAYER[0]['HP']>0:pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(10,10,int(100/(database.PLAYER[0]['MAXHP']/database.PLAYER[0]['HP'])),20))

					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,40,100,20))
					if self.opt != 4:
						if self.pp[self.turn][self.opt] > 0:pygame.draw.rect(self.display, (0, 100, 255), pygame.Rect(10,40,int(100/(database.EQUIPMENT[self.turn][self.opt][1]['CAPACITY']/self.pp[self.turn][self.opt])),20))

					pygame.draw.rect(self.display, (50, 50, 50), pygame.Rect(10,70,100,20))
					if database.PLAYER[0]['XP']>0:pygame.draw.rect(self.display, (0, 255, 100), pygame.Rect(10,70,int(100/(database.PLAYER[0]['MAXXP']/database.PLAYER[0]['XP'])),20))

				if self.turn < len(database.PLAYER) and self.turn!=-1:
					#TIME BAR
					if self.mnu < 3:
						pygame.draw.rect(self.display, (255, 0, 255), pygame.Rect(0,302,int(600/(100/self.btime)),10))
						self.btime -= 0.5
						if self.btime == 0:
							self.fight(len(database.PLAYER))

					#OPTIONS
					if self.mnu == 1:
						x=0
						for i in database.EQUIPMENT[self.turn]:
							if self.opt == x:pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(118+x*35,338,32,32))
							else:pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(118+x*35,338,32,32))
							pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(120+x*35,340,28,28))
							if i[0] != '_':self.display.blit(pygame.image.load('Sprites/' + i[0] + '.png'), (120+x*35, 340))
							x+=1

						if self.opt == 4:pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(400,338,32,32))
						else:pygame.draw.rect(self.display, (255, 255, 255), pygame.Rect(400,338,32,32))
						pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(402,340,28,28))
						self.display.blit(pygame.image.load('Sprites/run.png'), (402, 340))

					#AIM BAR
					elif self.mnu == 2:
						if self.opt < 4:
							self.aimx += 12 - database.PLAYER[self.turn]['AGILITY'][database.PLAYER[self.turn]['LEVEL']]
							if self.aimx > 500 - database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]: self.aimx = 100 + database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']]
							self.display.blit(pygame.image.load('Sprites/aim.png'), (self.aimx, 200))
							pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(100 + database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']],200,3,8))
							pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(500 - database.PLAYER[self.turn]['ATTACK'][database.PLAYER[self.turn]['LEVEL']],200,3,8))

		#MAP
		elif self.battle == False:
			#self.map = TiledMap()
			#self.map_img = self.map.make_map()
			#self.map_rect = self.map_img.get_rect()
			#for x in range(0, 22):
			#	for y in range(0, 15):
			#		self.display.blit(self.map.get_tile_image(x, y, 0), (x*30-self.cam_x, y*30-self.cam_y))

			#OBJECTS
			#self.colorhero = pygame.PixelArray.surface(self.player_sprite[self.player_gif//len(self.player_sprite)])
			#self.colorhero.replace((65,146,85), (255,56,59))
			self.display.blit(self.player_sprite[self.player_gif//len(self.player_sprite)], (self.player_rect.x-self.cam_x, self.player_rect.y-self.cam_y))
			if self.en[0]['HP']>0:self.enemy(0)
			self.npc(300,100,1)
			self.chest(400,200,'paçoca')
			self.portal(500,200,'drugstore')

		#INVENTORY
		if self.inventory == True:
			inv = menu.Inventory()
			inv.show(self.display, self.opt)

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
		self.cam_x += (self.player_rect.x  - self.cam_x - 300)/12
		self.cam_y += (self.player_rect.y  - self.cam_y - 200)/12

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