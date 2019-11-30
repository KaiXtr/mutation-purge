import database

import random
import pygame

class Inventory:
	def __init__(self):
		self.invind=0
		
	def show(self,ind,dpy):
		pygame.draw.rect(dpy, (255, 255, 255), pygame.Rect(100,60,400,270))
		pygame.draw.rect(dpy, (0, 0, 0), pygame.Rect(105,65,390,260))

		x=120
		y=50
		for j in database.INVENTORY[ind]:
			if database.INVENTORY[ind][0]!=j:
				for i in j:
					pygame.draw.rect(dpy, (255, 255, 255), pygame.Rect(x,y,30,30))
					pygame.draw.rect(dpy, (0, 0, 0), pygame.Rect(x+1,y+1,28,28))
					if i != '_':dpy.blit(pygame.image.load('Sprites/' + i + '.png'), (x, y))
					x+=35
			x=120
			y+=35
			
	def add(self,item):
		i=0
		j=0
		trigg=False
		for y in database.INVENTORY[self.invind]:
			if database.INVENTORY[self.invind][0]!=y:
				for x in y:
					if x=='_' and trigg==False:
						database.INVENTORY[self.invind][i][j]=item
						trigg=True
					j+=1
			i+=1
			j=0
			
	def drop(self,i,j):
		database.INVENTORY[self.invind][i][j]='_'
		
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
		item=database.INVENTORY[iinv][ii][ij]
		database.INVENTORY[iinv][ii][ij]=database.INVENTORY[finv][fi][fj]
		database.INVENTORY[finv][fi][fj]=item

class Shop:
	def __init__(self):
		self.money = database.MONEY
		self.prd = {'munição.38': 10,'comprimidos': 40}
		
	def show(self):
		print('$'+str(self.money)+'\n')
		for i in self.prd:
			print(i+' = $'+str(self.prd[i]))
		print('\nSair\n')
			
	def buy(self, item):
		bb=False
		if self.money >= self.prd[item]:
			i=Inventory()
			for j in database.INVENTORY[0]:
				for x in j:
					if x=='_':
						bb=True
		if bb == True:
			i.add(item)
			self.money -= self.prd[item]
			del self.prd[item]

class Bestiary:
	def __init__(self):
		self.date = '03/03/03'
		self.freaks = database.FREAKS
		self.bestiary = []
		
	def show(self, opt):
		print('---------\n')
		l=self.bestiary[opt]
		att=''
		ht=''
		for i in l['HABILITIES']:
			att+=i[0]+': '+i[1]+'\n '
			if i[2]>0 and i[3]<4:att+='+'
			if i[3]==1:att+=str(i[2])+' VITALIDADE\n\n'
			if i[3]==2:att+=str(i[2])+' ATAQUE\n\n'
			if i[3]==3:att+=str(i[2])+' AGILIDADE\n\n'
			if i[3]==4:
				if i[2]==1:ht='Veneno'
				if i[2]==2:ht='Náusea'
				att+=ht+'\n\n'
		print(l['NAME']+'\n\n'+l['INFO']+'\n\nAGILIDADE: '+str(l['AGILITY'])+'m/s - VITALIDADE: '+str(l['MAXHP'])+'VL\n\nALTURA: '+l['HEIGHT']+'cm - ID: '+l['ID']+' - RG: '+l['DATE']+'\n\n'+att)
		
	def add(self,ind):
		f=self.freaks[ind]
		f['DATE']=self.date
		id=len(self.bestiary)+1
		if id < 10:id='00'+str(id)
		elif id < 100:id='0'+str(id)
		f['ID']=id
		self.bestiary.append(f)

def status():
	print(database.PLAYER[1]['NAME']+' '+database.PLAYER[1]['LASTNAME'])
	print()
	if database.PLAYER[1]['GENDER']=='male':print('♤ - 0067\nA+ - solteiro')
	if database.PLAYER[1]['GENDER']=='female':print('♡ - 0067A+ - solteira')
	if database.PLAYER[1]['GENDER']=='bigender':print('☆ - 0067A+ - solteire')
	if database.PLAYER[1]['GENDER']=='nonbinary':print('◇ - 0067A+ - solteire')

def call(nb,sc,who,pay):
	for i in database.CONTACTS:
		if nb == database.CONTACTS[i]:
			if pay==False:
				if database.CREDIT > 0:
					database.CREDIT -= 1
					for t in database.DIALOGS[nb][sc]:
						print(t)
					database.CALLHIST.append([nb,who])
					break
				else:
					print('No credits...')
			if pay==True:
				if database.MONEY > 0:
					database.MONEY -= 5
					for t in database.DIALOGS[nb][sc]:
						print(t)
					database.CALLHIST.append([nb,who])
					break
				else:
					print('No credits...')

def list(flt):
	for i in database.EMAILS:
		if i[3]==flt:
			print(i[0])
			print(i[1])

def show(opt):
	ml=(database.PLAYER[1]['NAME']+database.PLAYER[1]['LASTNAME']).lower()+'@cmail.com'
	print('DE: '+database.EMAILS[opt][0]+'\nPARA: '+ml+'\n\n'+emails[opt][1]+'\n\n'+database.EMAILS[opt][2])
	database.EMAILS[opt][3]=True
	
def tasks(flt):
	for i in database.TASKS:
		if i[1]==flt:
			print(i[0])
			
def news(day):
	for i in database.NEWS[day]:
		print(i[0]+'\n'+i[1]+'\n\n'+i[2])
	
database.save_game(1)