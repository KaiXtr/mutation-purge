# -*- coding: utf-8 -*-
import pygame
import sqlite3
import os
 
def new_data():
    global ID, LANG, SFX, MSC, UP, DOWN, LEFT, RIGHT, ACT, PHONE, BAG, SPEED, COLOR, \
    FORMATION, MAP, PX, PY, TIME, DATE, CHAPTER, MORALITY, ATM, MONEY, CREDIT, BATTERY, GAS, GAMETIME, CHARACTERS, PARTY, TACTICAL, BESTIARY, ACHIEVEMENTS

    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    LANG = 'PT'
    SFX = 0.8
    MSC = 0.6
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d
    ACT = pygame.K_SPACE
    PHONE = pygame.K_BACKSPACE
    BAG = pygame.K_RETURN
    SPEED = 2
    COLOR = 255
     
    MAP = 1
    PX = 0
    PY = 0
    TIME = [8,30,0]
    DATE = [10,3,0]
    CHAPTER = 0
    MORALITY = 0
    GAMETIME = 0
    FORMATION = 0
     
    ATM = 200
    MONEY = 50
    CREDIT = 0
    BATTERY = 1
    GAS = 100.0
     
    CHARACTERS = [
    {'NAME': 'Sidney','LASTNAME': 'Barreto','GENDER': 'male','ID': '0064','BLOOD': 'A+','CIVIL': 'solteiro','CLASS': 'gunslinger','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
    'FAVFOOD': ['coxinha','whisky'],
    'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
    'ATTACK': [10,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
    'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
    'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
    'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]},
     
    {'NAME': 'Jane', 'LASTNAME': 'Oliveira','GENDER': 'female','ID': '0094','BLOOD': 'O-','CIVIL': 'casada','CLASS': 'rifler','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
    'FAVFOOD': ['pão de queijo','café'],
    'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
    'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
    'AGILITY': [1,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
    'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
    'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]},
     
    {'NAME': 'Renan', 'LASTNAME': 'Pinheiro','GENDER': 'male','ID': '0042','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'thief','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
    'FAVFOOD': ['refrigerante','bolo'],
    'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
    'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
    'AGILITY': [2,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
    'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
    'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]},
     
    {'NAME': 'Lúcia', 'LASTNAME': 'Figueiredo','GENDER': 'female','ID': '0013','BLOOD': 'O+','CIVIL': 'viúva','CLASS': 'sniper','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
    'FAVFOOD': ['suco de laranja','peixe'],
    'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
    'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
    'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
    'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
    'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]},
     
    {'NAME': 'Diego', 'LASTNAME': 'Donovan','GENDER': 'male','ID': '0120','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'gunslinger','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
    'FAVFOOD': ['hamburguer','refrigerante'],
    'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
    'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
    'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
    'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
    'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]},
     
    {'NAME': 'Bianca', 'LASTNAME': 'Pacheco','GENDER': 'female','ID': '0022','BLOOD': 'O+','CIVIL': 'casada','CLASS': 'doctor','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
    'FAVFOOD': ['sushi','suco de maracujá'],
    'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
    'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
    'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
    'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
    'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]}
    ]
    PARTY = [[0,4,3]]
    TACTICAL = []
    BESTIARY = []
    for i in ACHIEVEMENTS:
        i[2] = 0
        i[3] = ''
     
    try:
        com.execute("CREATE TABLE settings (id integer,lang text,sfx integer,msc integer,up text,down text,left text,right text,act text,phone text,inventory text,speed integer,color integer)")
        com.execute("CREATE TABLE data (id integer,gt integer,fr integer,map integer,x integer,y integer,time text,date text,chapter integer,morality integer,atm integer,money integer,credit integer,battery integer,gas integer)")
    except: pass
     
    trg = False
    com.execute("SELECT id FROM settings")
    for i in com.fetchall():
        if i[0] == ID: trg = True
    if trg == True:
        com.execute("DELETE FROM settings WHERE id=" + str(ID))
        com.execute("DELETE FROM data WHERE id=" + str(ID))
         
    com.execute("INSERT INTO settings VALUES (" + str(ID) + ",'PT',0.8,0.6,'W','S','A','D','SPACE','BACKSPACE','RETURN',2,0)")
    com.execute("INSERT INTO data VALUES (" + str(ID) + ",0,0,1,0,0,'0000','000000',0,0,0,0,0,0,0)")
     
    com.execute("DROP TABLE IF EXISTS characters" + str(ID))
    com.execute("CREATE TABLE characters" + str(ID) + " (n integer,name text,lastname text,gender text,level integer)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(0,'Sidney','Barreto','male',0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(1,'Jane','Oliveira','female',0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(2,'Renan','Pinheiro','male',0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(3,'Bianca','Pacheco','female',0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(4,'Diego','Donovan','male',0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(5,'Lúcia','Figueiredo','female',0)")
     
    com.execute("DROP TABLE IF EXISTS party" + str(ID))
    com.execute("CREATE TABLE party" + str(ID) + " (n integer,p1 integer,p2 integer,p3 integer)")
     
    com.execute("DROP TABLE IF EXISTS tactical" + str(ID))
    com.execute("CREATE TABLE tactical" + str(ID) + " (n integer,pl1 integer,pl2 integer,pl3 integer)")
     
    com.execute("DROP TABLE IF EXISTS bestiary" + str(ID))
    com.execute("CREATE TABLE bestiary" + str(ID) + " (idx integer,id text,date text)")
     
    com.execute("DROP TABLE IF EXISTS achievements" + str(ID))
    com.execute("CREATE TABLE achievements" + str(ID) + " (idx integer,got integer,date text)")
     
    com.execute("DROP TABLE IF EXISTS inventory" + str(ID))
    com.execute("CREATE TABLE inventory" + str(ID) + " (cl1,cl2,cl3,cl4)")
    tbl.commit()
     
    tbl.close()
 
def load_data():
    global ID, LANG, SFX, MSC, UP, DOWN, LEFT, RIGHT, ACT, PHONE, BAG, SPEED, COLOR, \
    FORMATION, MAP, PX, PY, TIME, DATE, CHAPTER, MORALITY, ATM, MONEY, CREDIT, BATTERY, GAS, GAMETIME, PARTY, TACTICAL, BESTIARY
     
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    com.execute("SELECT lang FROM settings")
    LANG = com.fetchall()[ID][0]
    com.execute("SELECT sfx FROM settings")
    SFX = com.fetchall()[ID][0]
    com.execute("SELECT msc FROM settings")
    MSC = com.fetchall()[ID][0]
    com.execute("SELECT up FROM settings")
    UP = com.fetchall()[ID][0]
    com.execute("SELECT down FROM settings")
    DOWN = com.fetchall()[ID][0]
    com.execute("SELECT left FROM settings")
    LEFT = com.fetchall()[ID][0]
    com.execute("SELECT right FROM settings")
    RIGHT = com.fetchall()[ID][0]
    com.execute("SELECT act FROM settings")
    ACT = com.fetchall()[ID][0]
    com.execute("SELECT phone FROM settings")
    PHONE = com.fetchall()[ID][0]
    com.execute("SELECT inventory FROM settings")
    BAG = com.fetchall()[ID][0]
    com.execute("SELECT speed FROM settings")
    SPEED = com.fetchall()[ID][0]
    com.execute("SELECT color FROM settings")
    COLOR = com.fetchall()[ID][0]
     
    com.execute("SELECT gt FROM data")
    GAMETIME = com.fetchall()[ID][0]
    com.execute("SELECT fr FROM data")
    FORMATION = com.fetchall()[ID][0]
    com.execute("SELECT map FROM data")
    MAP = com.fetchall()[ID][0]
    com.execute("SELECT x FROM data")
    PX = com.fetchall()[ID][0]
    com.execute("SELECT y FROM data")
    PY = com.fetchall()[ID][0]
    com.execute("SELECT time FROM data")
    res = com.fetchall()[ID][0]
    TIME = [int(res[0:2]),int(res[2:4]),0]
    com.execute("SELECT date FROM data")
    res = com.fetchall()[ID][0]
    DATE = [int(res[0:2]),int(res[2:4]),int(res[4:6])]
    com.execute("SELECT chapter FROM data")
    CHAPTER = com.fetchall()[ID][0]
    com.execute("SELECT morality FROM data")
    MORALITY = com.fetchall()[ID][0]
    com.execute("SELECT atm FROM data")
    ATM = com.fetchall()[ID][0]
    com.execute("SELECT money FROM data")
    MONEY = com.fetchall()[ID][0]
    com.execute("SELECT credit FROM data")
    CREDIT = com.fetchall()[ID][0]
    com.execute("SELECT battery FROM data")
    BATTERY = com.fetchall()[ID][0]
    com.execute("SELECT gas FROM data")
    GAS = com.fetchall()[ID][0]
     
    com.execute("SELECT * FROM characters" + str(ID))
    res = com.fetchall()
    for i in range(len(CHARACTERS)):
        CHARACTERS[i]['NAME'] = res[i][1]
        CHARACTERS[i]['LASTNAME'] = res[i][2]
        CHARACTERS[i]['GENDER'] = res[i][3]
        CHARACTERS[i]['LEVEL'] = res[i][4]
     
    com.execute("SELECT * FROM party" + str(ID))
    res = com.fetchall()
    PARTY = []
    for i in res:
        PARTY.append([i[1],i[2],i[3]])
         
    com.execute("SELECT * FROM tactical" + str(ID))
    res = com.fetchall()
    TACTICAL = []
    for i in res:
        TACTICAL.append([i[1],i[2],i[3]])
     
    com.execute("SELECT * FROM bestiary" + str(ID))
    res = com.fetchall()
    BESTIARY = []
    for i in res:
        apd = FREAKS[i[0]].copy()
        apd['ID'] = i[1]
        apd['DATE'] = i[2]
        BESTIARY.append(apd)
     
    com.execute("SELECT * FROM achievements"+ str(ID))
    res = com.fetchall()
    for i in res:
        ACHIEVEMENTS[i[0]][2] = i[1]
        ACHIEVEMENTS[i[0]][3] = i[2]
    if res == []:
        for i in ACHIEVEMENTS:
            i[2] = 0
            i[3] = ''
         
    com.execute("DROP TABLE IF EXISTS inventory")
    com.execute("CREATE TABLE inventory (cl1,cl2,cl3,cl4)")
     
    com.execute("INSERT INTO inventory VALUES ('revolver .38','_','analgésico','_')")
    com.execute("INSERT INTO inventory VALUES ('paçoca','faca','_','colete IIA')")
    com.execute("INSERT INTO inventory VALUES ('_','_','lupa','_')")
    com.execute("INSERT INTO inventory VALUES ('M16','_','munição .38','munição .12')")
    tbl.commit()
     
    tbl.close()
     
def save_data():
    global ID, LANG, SFX, MSC, UP, DOWN, LEFT, RIGHT, ACT, PHONE, BAG, SPEED, COLOR, \
    MAP, PX, PY, TIME, DATE, CHAPTER, MORALITY, ATM, MONEY, CREDIT, BATTERY, GAS, GAMETIME
     
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    if TIME[0] < 10: hr = '0' + str(TIME[0])
    else: hr = str(TIME[0])
    if TIME[1] < 10: mn = '0' + str(TIME[1])
    else: mn = str(TIME[1])
    ts = hr + mn
     
    if DATE[0] < 10: dd = '0' + str(DATE[0])
    else: dd = str(DATE[0])
    if DATE[1] < 10: mm = '0' + str(DATE[1])
    else: mm = str(DATE[1])
    if DATE[2] < 10: yy = '0' + str(DATE[2])
    else: yy = str(DATE[2])
    dt = dd + mm + yy
     
    com.execute("UPDATE settings SET lang = :lang,sfx = :sfx,msc = :msc,up = :up,down = :down,left = :left,right = :right,act = :act,phone = :phone,inventory = :inventory,speed = :speed,color = :color WHERE id = :id",
        {'id': ID,'lang': LANG,'sfx': SFX,'msc': MSC,'up': UP,'down': DOWN,'left': LEFT,'right': RIGHT,'act': ACT,'phone': PHONE,'inventory': BAG,'speed': SPEED,'color': COLOR})
    tbl.commit()
     
    com.execute("UPDATE data SET gt = :gt,fr = :fr,map = :map,x = :x,y = :y,time = :time,date = :date,chapter = :chapter,morality = :morality,atm = :atm,money =:money,credit = :credit,battery = :battery,gas = :gas WHERE id = :id",
        {'id': ID,'gt': GAMETIME,'fr': FORMATION,'map': MAP,'x': PX,'y': PX,'time': ts,'date': dt,'chapter': CHAPTER,'morality': MORALITY,'atm': ATM,'money': MONEY,'credit': CREDIT,'battery': BATTERY,'gas': GAS})
    tbl.commit()
     
    for i in range(len(CHARACTERS)):
        com.execute("UPDATE characters" + str(ID) + " SET level = :level WHERE n = :n",{'n': i,'level': CHARACTERS[i]['LEVEL']})
    tbl.commit()
     
    tbl.close()
     
def char_entry():
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    for i in range(len(CHARACTERS)):
        com.execute("UPDATE characters" + str(ID) + " SET name = :name, lastname = :lastname,gender = :gender,level = :level WHERE n = :n",
            {'n': i,'name': CHARACTERS[i]['NAME'],'lastname': CHARACTERS[i]['LASTNAME'],'gender': CHARACTERS[i]['GENDER'],'level': CHARACTERS[i]['LEVEL']})
    tbl.commit()
     
    tbl.close()
     
def party_make(p):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    trg = False
    com.execute("SELECT n FROM party" + str(ID))
    for i in com.fetchall():
        if i[0] == t: trg = True
    if trg == False:
        com.execute("DELETE FROM party" + str(ID) + " WHERE n = " + str(p))
    com.execute("INSERT INTO party" + str(ID) + " VALUES(:n,:p1,:p2,:p3)",{'n': p,'p1': PARTY[p][0],'p2': PARTY[p][1],'p3': PARTY[p][2]})
    tbl.commit()
     
    tbl.close()
 
def tact_save(t):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    trg = False
    com.execute("SELECT n FROM tactical" + str(ID))
    for i in com.fetchall():
        if i[0] == t: trg = True
    if trg == False:
        com.execute("DELETE FROM tactical" + str(ID) + " WHERE n = " + str(t))
    com.execute("INSERT INTO tactical" + str(ID) + " VALUES(:n,:p1,:p2,:p3)",{'n': t,'p1': TACTICAL[t][0],'p2': TACTICAL[t][1],'p3': TACTICAL[t][2]})
    tbl.commit()
     
    tbl.close()
 
def best_regs(f):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    trg = False
    com.execute("SELECT idx FROM bestiary" + str(ID))
    for i in com.fetchall():
        if i[0] == f: trg = True
    if trg == False:
        com.execute("DELETE FROM bestiary" + str(ID) + " WHERE idx = " + str(f))
    com.execute("INSERT INTO bestiary" + str(ID) + " VALUES (:idx,:id,:date)",{'idx': f,'id': BESTIARY[f]['ID'],'date': BESTIARY[f]['DATE']})
    tbl.commit()
     
    tbl.close()
 
def trophy(i):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    com.execute("INSERT INTO achievements" + str(ID) + " VALUES(:idx,:got,:date)",{'idx': i,'got': ACHIEVEMENTS[i][2],'date': ACHIEVEMENTS[i][3]})
    tbl.commit()
     
    tbl.close()
     
def delete_data():
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    com.execute("DELETE FROM settings WHERE id=" + str(ID))
    com.execute("DELETE FROM data WHERE id=" + str(ID))
    com.execute("DROP TABLE characters" + str(ID))
    com.execute("DROP TABLE party" + str(ID))
    com.execute("DROP TABLE tactical" + str(ID))
    com.execute("DROP TABLE bestiary" + str(ID))
    com.execute("DROP TABLE achievements" + str(ID))
    com.execute("DROP TABLE inventory" + str(ID))
    tbl.commit()
     
    tbl.close()
     
LANG = 'PT'
SFX = 0.8
MSC = 0.6
UP = 'W'
DOWN = 'S'
LEFT = 'A'
RIGHT = 'D'
ACT = 'SPACE'
PHONE = 'BACKSPACE'
BAG = 'RETURN'
SPEED = 2
COLOR = 255
 
'''
1 - itatiaia
2 - resende
3 - petropolis
4 - nova friburgo
'''
 
ID = 0
MAP = 0
PX = 0
PY = 0
TIME = [0,0,0]
DATE = [0,0,0]
SCENE = 0
MORALITY = 0
   
CHAPTERS = [
['Depois do começo',
'Desde aquele dia, o mundo inteiro havia mudado,',
'Um fato concreto comprovava o que os antigos cientistas',
'e filósofos tentavam nos dizer há muito tempo,',
'Pela primeira vez, ali na frente, uma entidade',
'sobrenatural mostrava sua face ao mundo.',
'Eles não conseguiriam guardar esse segredo por mais',
'de 100.000 anos, era inviável, ainda mais devido ao',
'surto dos seres que os chamam de anomalias.',
'Vários caçadores cumpriam a difícil tarefa de expurgar',
'a praga de anomalias assolando a serra da região',
'sudoeste brasileira, esses eram os Mercenários.',
'Eles eram odiados pela população e marginalizados',
'pela sociedade, não tinham mais escolha na vida',
'a não ser arriscá-la. Foram heróis injustiçados e',
'vilões glorificados, tudo começou desde que',
'a polícia civil legalizou o porte de armas a quem',
'quisesse se tornar um Mercenário, embora nem mesmo',
'a própria população soubesse direito o que era isso,',
'Várias teorias da conspiração se espalharam, difamando',
'a incapacidade da polícia de segurar o aumento dos',
'casos de homicídio não registrados, muitos duvidam',
'que esses casos sejam reais, ou que as anomalias',
'realmente existam.',
'Tudo isso gira em torno de algo muito maior,',
'mas por agora, eu devo começar pelas histórias',
'que nos uniram nessa descoberta.',
'Eu vou contar a minha'
],
 
['Duplo Andantes',''],
['Quadro por Quadro',''],
['Fale Comigo',''],
['Lá se vai de novo',''],
['Eu quero ser seu','']
]
 
SPRITES = {'UP_Sid': [pygame.image.load('Sprites/hero_walkU_0.png'), pygame.image.load('Sprites/hero_walkU_1.png'), pygame.image.load('Sprites/hero_walkU_2.png'), pygame.image.load('Sprites/hero_walkU_3.png')],\
'DOWN_Sid': [pygame.image.load('Sprites/hero_walkD_0.png'), pygame.image.load('Sprites/hero_walkD_1.png'), pygame.image.load('Sprites/hero_walkD_2.png'), pygame.image.load('Sprites/hero_walkD_3.png')],\
'LEFT_Sid': [pygame.image.load('Sprites/hero_walkL_0.png'), pygame.image.load('Sprites/hero_walkL_1.png'), pygame.image.load('Sprites/hero_walkL_2.png'), pygame.image.load('Sprites/hero_walkL_3.png')],\
'RIGHT_Sid': [pygame.image.load('Sprites/hero_walkR_0.png'), pygame.image.load('Sprites/hero_walkR_1.png'), pygame.image.load('Sprites/hero_walkR_2.png'), pygame.image.load('Sprites/hero_walkR_3.png')]}
 
    
CHARACTERS = [
{'NAME': 'Sidney','LASTNAME': 'Barreto','GENDER': 'male','ID': '0064','BLOOD': 'A+','CIVIL': 'solteiro','CLASS': 'gunslinger','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
'FAVFOOD': ['coxinha','whisky'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [10,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,22,22,25,25,26,28,30,30,32,33,35]},
 
{'NAME': 'Jane', 'LASTNAME': 'Oliveira','GENDER': 'female','ID': '0094','BLOOD': 'O-','CIVIL': 'casada','CLASS': 'rifler','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
'FAVFOOD': ['pão de queijo','café'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [1,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]},
 
{'NAME': 'Renan', 'LASTNAME': 'Pinheiro','GENDER': 'male','ID': '0100','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'thief','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
'FAVFOOD': ['refrigerante','bolo'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [2,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]},
 
{'NAME': 'Lúcia', 'LASTNAME': 'Figueiredo','GENDER': 'female','ID': '0013','BLOOD': 'O+','CIVIL': 'viúva','CLASS': 'sniper','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
'FAVFOOD': ['suco de laranja','peixe'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25]},
 
{'NAME': 'Diego', 'LASTNAME': 'Donovan','GENDER': 'male','ID': '0024','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'gunslinger','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
'FAVFOOD': ['hamburguer','refrigerante'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [100,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [2,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [40,12,12,15,15,16,18,20,20,22,23,25]},
 
{'NAME': 'Bianca', 'LASTNAME': 'Pacheco','GENDER': 'female','ID': '0120','BLOOD': 'O+','CIVIL': 'casada','CLASS': 'doctor','LEVEL': 0,'SKILL': 0,'HP': 10,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,
'FAVFOOD': ['sushi','suco de maracujá'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25]}
]
   
PARTY = [[0,4,3]]
    
ATM = 0
MONEY = 0
CREDIT = 10
BATTERY = 3
GAS = 100.0

'''
HABITATS
jungle
urban
seaside
mountains
swamp
restinga
savanna-cerrado
manguezal
araucarias
  
TYPE
mammal
reptile
flying
aquatic
plant
psychic
humanoid
inorganic
fire
alien
nature
electric
  
1 - atacar
2 - abaixar ATAQUE
3 - abaixar AGILIDADE
4 - abaixar FORÇA
5 - abaixar RESISTÊNCIA
6 - condição
7 - chamar anomalia
8 - roubar
9 - faz nada
 
 - resfriado (não pode comer)
 - febre (perde HP no calor)
 - sede (perde HP por não beber)
 - náusea (erra facilmente)
 - preso (perde o turno)
 - inconsciente (não necessariamente sem HP)
 - parasita (suga o HP)
 - queimadura (perde HP, mas some)
 - veneno aracnídeo (perde HP)
 - veneno antiofídico (perde HP)
 - veneno escorpiônico (perde HP)
 - hemorragia (perde HP e não tem cura)
'''
     
FREAKS = [
#ANOMALIES
{'NAME': 'Madladcat','INFO': ['É um felino sobrenatural que','flutua como um fantasma.','Pequeno e ágil, porém bem frágil.'],'HEIGHT': '0,80','HABITAT': 'jungle','TYPE': 'mammal','AGILITY': 5,'HP': 8,'RESISTANCE': 1,
'HABILITIES': [['Morder',['O felino morde o oponente.'],-15,1],['Arranhar',['O felino usa suas garras,','para atacar o oponente.'],-3,1],
['Ronronar',['O felino ronrona, mostrando','seu desprezo pela situação.'],0,6],['Miar',['O felino mia para o além,','chamando outros felinos.'],0,5]]},
  
{'NAME': 'Camaraleão','INFO': ['É um réptil que se fundiu com','um camarão, não se sabe se é um alimento apetitoso.'],'HEIGHT': '0,23','HABITAT': 'swamp','TYPE': 'reptile','AGILITY': 6,'HP': 6,'RESISTANCE': 0,
'HABILITIES': [['Camuflar',['O réptil se camufla no ambiente,','aumentando sua AGILIDADE.'],2,3],['Língua',['O réptil usa sua língua como','chicote para atacar o oponente.'],-3,1],
['Estalo',['O réptil se estala, criando','um campo de força elétrico.'],-13,1]],'ITEM': 'camarão'},
  
{'NAME': 'Pombo Pavão','INFO': ['Um pombo urbano com uma mutação que o fez desenvolver penas de pavão com olhos reais nas suas pontas. Relativamente ágil, mas fraco.'],'HEIGHT': '0,25','HABITAT': 'urban','TYPE': 'flying','AGILITY': 3,'HP': 10,'RESISTANCE': 1,
'HP': 10,'HABILITIES': [['Defecar',['A ave defeca no oponente, infectando-o.'],8,6],['Hipnose',['A ave hipnotiza o oponente com os olhos das penas de pavão, diminuindo sua AGILIDADE.'],-2,3],
['Bicar',['A ave bica o oponente.'],-4,1],['Gritar',['A ave grita, com a possibilidade de outra anomalia entrar na batalha.'],0,7]]},
    
{'NAME': 'Jaré','INFO': ['Um réptil que, graças á uma sílaba a menos em seu nome, perdeu dois de seus membros. Não muito ágil, mas causa muito dano.'],'HEIGHT': '1,90','HABITAT': 'swamp','TYPE': 'reptile','AGILITY': 2,'HP': 13,'RESISTANCE': 1,
'HABILITIES': [['Morder',['O réptil morde seu oponente'],-6,1],['Esperar',['O réptil aumenta seu ATAQUE.'],1,2],['Bote',['O réptil ataca com uma mordida em avanço.'],-5,1],
['Esconder',['O réptil se esconde no ambiente, aumentando sua AGILIDADE.'],1,3]]},
    
{'NAME': 'Lata Alada','INFO': ['Uma lata de energético que tenta ser irada e tem o único atributo que prometeu dar á quem o consumisse. É literalmente uma piada.'],'HEIGHT': '0,15','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 10,'HP': 5,'RESISTANCE': 1,
'HABILITIES': [['Voar',['Aumenta sua agilidade'],1,3],['Energizar',['Aumenta seu dano de arremesso'],2,2],['Ressaca',['A lata se auto destrói'],0,1],
['Arremessar',['A lata se joga no oponente, se machucando junto.'],-1,1]]},
   
{'NAME': 'Cacho de Olhos','INFO': ['Vários olhos diferentes agrupados que possuem poderes hipnóticos. PS: NÃO É GUARANÁ, NÃO FAÇA SUCO.'],'HEIGHT': '0,30','HABITAT': 'jungle','TYPE': 'plant','AGILITY': 2,'HP': 20,'RESISTANCE': 1,
'HABILITIES':[['Encarar',['Os olhos começam a encarar o oponente, amedrontando-o e fazendo seu ATAQUE abaixar.'],-1,2],['Atirar',['Um dos olhos se lança no oponente.'],-3,1],
['Plantar',['Um olho se planta no chão com a possibilidade de germinar um novo cacho.'],0,7],['Explodir',['Todos os olhos se soltam num ataque fulminante.'],-7,1]]},
    
{'NAME': 'Perereca Mil Grau','INFO': ['Um anfíbio que saiu da metamorfose antes da hora e ao mesmo tempo que manteve a cauda, desenvolveu braços fortes.'],'HEIGHT': '0,70','HABITAT': 'jungle','TYPE': 'aquatic','AGILITY': 2,'HP': 20,'RESISTANCE': 1,
'HABILITIES':[['Língua',['O anfíbio usa sua língua para chicotear o oponente.'],-5,1],['Porrada',['O anfíbio usa seus braços musculosos para bater no oponente.'],-8,1],
['Veneno',['O anfíbio libera toxinas nas bolsas das suas costas para infectar o oponente.'],1,4],['Salto',['O anfíbio pula pelo ambiente e aumenta sua AGILIDADE.'],2,3]]},
    
{'NAME': 'Cremado Cremoso','INFO': ['Um homem que sofreu uma combustão espontânea mas continua vivo graças á mutação.'],'HEIGHT': '1,70','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 5,'HP': 18,'RESISTANCE': 1,
'HABILITIES': [['Bater',['O indivíduo bate no oponente.'],-5,1],['Cinzas',['O indivíduo joga cinzas no oponente, abaixando sua AGILIDADE.'],-3,3],
['Dançar',['O indivíduo começa a rebolar e mostrar seu charme.'],0,8],['Infectar',['O indivíduo entra dentro do oponente através das cinzas, diminuindo seu ATAQUE.'],-3,2]]},
  
{'NAME': 'Combustão Espontânea','INFO': ['Uma homem normal que teve o azar','de ter essa anomalia, e agora','vive como uma tocha humana.'],'HEIGHT': '1,70','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 5,'HP': 30,'RESISTANCE': 3,
'HABILITIES': [['Bater',['O indivíduo bate no oponente.'],-8,1],['Labareda',['O indivíduo sopra uma labareda no','oponente, fazendo ele se queimar.'],3,4],
['Queimadura',['O indivíduo se ilumina tanto que','o oponente perde a visão.'],9,6],['Bolas de Fogo',['O indivíduo arremessa bolas','de fogo que vão te atolar.'],-14,1]]},
    
{'NAME': 'Biscoito Crucificado','INFO': 'Esse ser humano não está em um estado muito bacana...É um biscoito de gengibre possuído preso num crucifixo, parece até coisa de algum filme B!','HEIGHT': '0,30','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 8,'HP': 30,'RESISTANCE': 1,
'HABILITIES': [['Chantily','O possuído jorra chantily venenoso no oponente.',1,4],['Gargalhar','O possuído ri de uma maneira terrorífica, diminuindo o ATAQUE do oponente.',-2,2],
['Bater','O possuído usa seu crucifixo para atacar o oponente.',-8,1],['Perfurar','O possuído perfura o corpo do oponente usando o crucifixo',-10,1]]},
 
{'NAME': 'Caneta Azul','INFO': ['É um objeto possuído por um fantasma','e agora tem o poder de atormentar as pessoas','com uma música irritante.'],'HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 8,'HP': 15,'RESISTANCE': 0,
'HABILITIES': [['Rabiscar',['O elemento se move contra o oponente','e o rabisca o rosto.'],-8,1],['Cantar',['O elemento atormenta o oponente','através de uma canção pertubadora.'],6,4],
['Explodir',['O elemento se estoura, espalhando','tinta na cara do oponente.'],-20,1]]},
 
{'NAME': 'Carangueijo Armado','INFO': ['Um carangueijo que aprendeu a','utilizar uma arma branca.'],'HEIGHT': '0,18','HABITAT': 'urban','TYPE': 'rough','AGILITY': 5,'HP': 50,'RESISTANCE': 3,
'HABILITIES': []},
 
{'NAME': 'Emo Hipster','INFO': ['A DDA ainda não sabe se esse ser é uma anomalia ou apenas um cara estranho que chegou e parece não achar lugar no corpo que Deus encarnou.'],'HEIGHT': '1,60','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 4,'HP': 20,'RESISTANCE': 1,
'HABILITIES': [['Cantar',['O esquisito começa a cantar uma música dos los hermanos com uma guitarra.'],1,4],['Guitarrada',['O esquisito usa sua guitarra para atacar o oponente.'],-10,1],
['Óculos sem lente',['O esquisito põe óculos sem lente para confundir o oponente, abaixando sua AGILIDADE.'],-1,3],['Franja',['O esquisito balança sua franja, aumentando seu ATAQUE.'],2,2]]},
  
{'NAME': 'Crush','INFO': ['Não conseguimos coletar muitos','dados dessa anomalia, só sabemos','que é a mais forte nunca derrotada.'],'HEIGHT': '1,60','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 99,'HP': 9999999,'RESISTANCE': 99,
'HABILITIES': [['Iludir',['A anomalia usa as palavras','como lanças e ataca o','coração do oponente.'],-99999,1]]},
    
{'NAME': 'Peixe Galã','INFO': 'Um peixe que abre a boca acima dos limites de sua mandíbula e da biologia, pelo menos ele é admirável.','HEIGHT': '1,20','HABITAT': 'swamp','TYPE': 'aquatic','AGILITY': 5,'HP': 25,'RESISTANCE': 1,
'HABILITIES': [['Aumentar','O peixe aumenta o tamanho da sua face e volta ao normal, assustando o oponente e abaixando seu ATAQUE',-2,2],
['Saltar','O peixe salta na água e chicoteia o oponente com sua cauda',-7,1],['Morder','O peixe morde o oponente com seus dentes limpos e branquinhos.',-9,1],
['Brilhar','O peixe reflete a luz do sol cegando o oponente.',2,4]]},
    
{'NAME': 'Pé de moleque','INFO': 'É um doce de amendoim delicioso muito comum em festas juninas...não pera. É um membro que se separou do corpo humano e agora consegue viver por conta própria, não confundir com mãozinha da Família Adams.','HEIGHT': '0,80','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': [['Pisar','O membro pisa no oponente com toda sua força.',-10,1],['Chutar','O membro chuta o oponente, mesmo perdendo seu equilíbrio.',-12,1],
['Cura','O membro se cura utilizando uma técnica que não entendemos devido ás limitações de seu corpo.',10,1],['Agachar','O membro concentra a energia dos seus pés e aumenta seu ATAQUE.',5,2]]},
    
{'NAME': 'Flamingo Flamenguista','INFO': 'Uma ave com a peculiaridade de ter a anomalia FLAMENGO.','HEIGHT': '1,20','HABITAT': 'mangue','TYPE': 'flying','AGILITY': 7,'HP': 33,'RESISTANCE': 1,
'HABILITIES': [['Bolada','A ave chuta uma bola na face do oponente.',-13,1],['Dibre','Lamentamos o erro de ortografia de Sidney, a ave dribla o oponente fazendo sua AGILIDADE aumentar.',3,2],
['Rasteira','A ave ataca o oponente se jogando no chão e derrubando-o.',-10,1],['Gabigol','A ave recruta o profissional jogador de futebol GABIGOL, ganhando a batalha imediatamente.',-50,1]]},
 
{'NAME': 'Peixe Gado','INFO': ['Um búfalo que nadou tanto','que ganhou uma cauda de sereia.','Seria um tipo de Hipocampo?'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'aquatic','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
 
{'NAME': 'Mangue Aranha','INFO': ['Uma árvore peculiar que possui','pernas no lugar de raízes.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'plant','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
 
{'NAME': 'Homem Carangueijo','INFO': ['Um carangueijo gigante que lembra','uma música do Chico Science.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'rough','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
    
{'NAME': 'Belle Dolphine','INFO': 'Fruto de uma relação entre uma E-Girl e o Boto.','HEIGHT': '2,10','HABITAT': 'jungle','TYPE': 'aquatic','AGILITY': 7,'HP': 42,'RESISTANCE': 1,
'HABILITIES': [['Ahegao','O mamífero tenta sensualizar o oponente simulando um ato sexual, mas faz o efeito contrário abaixando seu ATAQUE',-3,2],['Água de banho','O mamífero oferece água de banho para o oponente, este o ingere e obtém HERPES.',2,4],
['Nadar','O mamífero nada no ambiente para recuperar sua VITALIDADE.',10,1],['Canto submarino','O mamífero entoa uma canção para chamar uma anomalia para a batalha.',1,5]]},
  
{'NAME': 'Busto de Teresa Cristina','INFO': ['Um busto muito pesado e cheio,','de ódio no seu coração.'],'HEIGHT': '0,80','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': [['Atacar',['O elemento se joga contra o oponente.'],-10,1],['Esmagar',['O elemento cai em cima','da cabeça do oponente.'],-20,1],['Voar',['O elemento voa ao derredor','do oponente'],0,8]]},
  
{'NAME': 'Tarsila','INFO': 'Um auto retrato da pintora Tarsila do Amaral, te encarando pronta pra acabar com sua raça. Óleo sobre tela.','HEIGHT': '2,20','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': [['Atacar','A pintura se joga contra o oponente, machucando a si no processo.',-10,1]]},
 
{'NAME': 'Hipocampo','INFO': ['Um Hipocampo com o','formato de um hipocampo.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'aquatic','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
 
{'NAME': 'Galinha Verde','INFO': ['Uma ave com a terrível','anomalia INTEGRALISMO.'],'HEIGHT': '2,30','HABITAT': 'urban','TYPE': 'flying','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
 
{'NAME': 'Cabeça de Bagre!!','INFO': ['Um homem com cabeça de bagre','e com péssima compreensão de ritmo.'],'HEIGHT': '2,30','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
 
{'NAME': 'Homem Primata','INFO': ['Um humano que sabe','dançar muito bem.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'rough','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
 
{'NAME': 'Homem Seco e Molhado','INFO': ['Um homem que possui a anomalia de','estar seco e molhado ao mesmo tempo.'],'HEIGHT': '2,30','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 5,'HP': 50,'RESISTANCE': 3,'HABILITIES': []},
 
{'NAME': 'Tim Maia','INFO': ['Um mesoamericano com ótima.','afinação vocal.'],'HEIGHT': '1,80','HABITAT': 'jungle','TYPE': 'humanoid','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': []},
 
{'NAME': 'Chaves','INFO': ['Um molho de chaves','que ninguém tem paciência.'],'HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': []},
 
{'NAME': 'Macaco','INFO': ['Um macaco mecânico portando','um macaco.'],'HEIGHT': '1,80','HABITAT': 'jungle','TYPE': 'mammal','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': []},
    
#CHEFES
{'NAME': 'Araraucária','INFO': ['Uma árvore animal que possui penas coloridas no lugar de folhas.'],'HEIGHT': '10,2','HABITAT': 'jungle','TYPE':'plant','AGILITY': 3,'HP': 60,'RESISTANCE': 3,
'HABILITIES': [['Algazarra',['Barulhos estranhos saem das folhas do vegetal, diminuindo o ATAQUE do oponente.'],-1,2],['Fruta',['O vegetal deixa cair uma fruta de um dos galhos.'],-6,1],['Regeneração',['O vegetal drena recursos de suas raízes e recupera 10 HP.'],10,1]]},
   
{'NAME': 'Lula Torpedo','INFO': 'Um molusco que antige seus oponentes como um torpedo. Apesar de enorme, forte e resistente, se locomove muito devagar.','HEIGHT': '2,10','HABITAT': 'sea','TYPE': 'aquatic','AGILITY': 1,'HP': 50,'RESISTANCE': 1,
'HABILITIES': [['Tentáculos','O molusco usa seus tentáculos para atacar seu oponente.',-5,1],['Jato de tinta','O molusco atira um jato de tinta que impossibilita o oponente de atacar.',-5,3],
['Camuflagem','O molusco se disfarça no ambiente, aumentando sua AGILIDADE.',2,3],['Torpedo','O molusco acerta o oponente com um ataque explosivo que acerta todos á volta, super efetivo.',-15,1]]},
  
{'NAME': 'Orelhão','INFO': ['Um fungo que realmente existe,','e quis trabalhar pra telefônica.'],'HEIGHT': '1,30','HABITAT': 'urban','TYPE': 'psychic','AGILITY': 3,'HP': 25,'RESISTANCE': 0,
'HABILITIES': [['Soar',['O elemento vibra seus tímpanos,','abaixando a RESISTÊNCIA do oponente.'],-5,4],['Fichas',['O elemento arremessa fichas','do seu cofrinho.'],-10,1],
['Trote',['O elemento te passa um trote,','enganando o oponente e abaixando','sua FORÇA'],1,6],['Ligação',['O elemento faz uma ligação,','chamando outra anomalia.'],2,6]]},
    
{'NAME': 'Abaporu','INFO': 'Uma pintura modernista que criou vida própria e por sinal é canibal.','HEIGHT': '2,20','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 7,'HP': 75,'RESISTANCE': 1,
'HABILITIES': [['Pisar','A pintura pisa no oponente esmagando-o.',-13,1],['Fúria','A pintura grita furiosamente aumentando seu ATAQUE.',3,2],
['Proteger','A pintura reforça sua proteção de acrílico sobre a tela',1,6],['Reforço','A pintura chama outra pintura para ajudar na batalha.',1,5]]},
    
{'NAME': 'Xaruto','INFO': 'Estranhamente lembra um personagem de um anime que não é tão bom quanto Evangelion.','HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 20,'HP': 20,'RESISTANCE': 1,
'HABILITIES': [['Fumaça ninja','O elemento solta uma fumaça com mais de 100.000 substâncias tóxicas incluindo nicotina e enxofre, envenenando o oponente.',1,4],['Chama ninja','O elemento sopra uma labareda ardente, incendiando o oponente.',3,4],
['Xaringan','O elemento usa uma espécime de energia oculta para aumentar seu ATAQUE.',10,2],['Vaporizar','O elemento se transforma num cigarro eletrônico, relaxando e diminuindo sua AGILIDADE.',-10,-2]]},
    
{'NAME': 'Cesariana','INFO': 'Um feto dentro de uma bolha numa cesariana com poderes psíquicos.','HEIGHT': '1,00','HABITAT': 'urban','TYPE': 'psychic','AGILITY': 2,'HP': 10,'RESISTANCE': 1,
'HABILITIES': [['Escudo','O feto reforça a resistência da bolha.',1,6],['Cordão Umbilical','O feto drena a energia de sua hospedeira e recupera sua VITALIDADE.',10,1],
['Grito molecular','O feto grita em um nível estratosféricamente alto, agitando as moléculas de seus oponentes.',-15,1],['Líquido Uterino','O feto arremesa o líquido uterino da bolha nos oponentes, confundindo-os e dando NÁUSEA.',2,4]]},
    
#MERCENARIES
{'NAME': 'Vinícius','HABITAT': 'urban','TYPE': 'mercenary','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'HABILITIES': [['Atirar',-8,1],['Granada',-20,1]]},
    
#OTHER
{'NAME': 'Alvo','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'HABILITIES': [['Fazer nada',0,6]]},
    
]
   
BESTIARY = []
 
'''
0 - nada
1 - equip1
2 - equip2
3 - equip3
4 - equip4
5 - dialog
6 - guard
7 - run
'''
TACTICAL = [[1,6],[2,7]]
    
#MOCHILAS
ITEMS = [
['bolsinha',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 2x2.'],1000,0,22],
['bolsa',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 3x2.'],2500,0,32],
['mochila',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 3x3.'],5000,0,33],
['mochila de viagem',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 3x4.'],7500,0,34],
['mochilão',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 4x4.'],10000,0,44],
  
#ROUPAS
['colete amarelo',[''],30,1,1,10],
['colete salva-vidas',[''],60,1,3,15],
['colete I',[''],120,1,5,20],
['colete IIA',[''],240,1,8,25],
['colete II',[''],360,1,10,30],
['colete IIIA',[''],480,1,12,35],
['colete III',[''],600,1,16,40],
['colete IV',[''],720,1,20,45],
  
#MUNIÇÃO
['tranquilizante',['Munição para pistola que faz o inimigo adormecer.'],100,0],
['munição.12',[''],200,2,0],
['munição.16',[''],200,2,0],
['munição.22',[''],200,2,0],
['munição.32',[''],200,2,0],
['munição.38',[''],300,2,1],
['munição.42',[''],400,2,2],
['munição.44',[''],200,2,0],
['munição.45',[''],200,2,0],
['munição 0.38mm',[''],200,2,0],
['munição 5.56mm',[''],200,2,0],
['míssel',[''],800,2,3],
  
#ARMAS BRANCAS
['faca',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],800,5,{'DAMAGE': 5}],
['peixeira',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],1000,5,{'DAMAGE': 8,}],
['cutelo',['Foi feita para cortar ossos de carnes, mas','serve como uma boa arma também.'],1200,5,{'DAMAGE': 10,}],
  
#ARMAS DE FOGO
['revólver .22',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],2000,6,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
['revólver .32',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],2000,6,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
['revólver .38',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],2000,6,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
['revólver .44',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],2000,6,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
 
['pistola',['Arma de fogo para ataques de média distância, ela usa munição de calibre 38.'],2500,6,{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16}],
 
['Uzi .22',['Arma de fogo para ataques de média distância.'],4000,6,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 1, 'CAPACITY': 10, 'GAUGE': 22}],
['Uzi .45',['Arma de fogo para ataques de média distância.'],4000,6,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 1, 'CAPACITY': 16, 'GAUGE': 45}],
 
['espingarda .12',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,5,{'DAMAGE': 5, 'RECHARGE': 4, 'CADENCY': 4, 'CAPACITY': 6, 'GAUGE': 12}],
['carabina',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
 
['sniper',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],6000,6,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['escopeta',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],4000,6,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
 
['fuzil de assalto',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],4000,6,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['fuzil',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,6,{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 2, 'CAPACITY': 16}],
['AK-47',['Fuzil para ataques de curta distância, ela usa munição de calibre 16.'],5000,6,{'DAMAGE': 7, 'RECHARGE': 3, 'CADENCY': 2, 'CAPACITY': 20, 'GAUGE': 39.0}],
['M16',['Fuzil para ataques de curta distância, ela usa munição de calibre 16.'],5000,6,{'DAMAGE': 6, 'RECHARGE': 3, 'CADENCY': 1, 'CAPACITY': 30, 'GAUGE': 5.56}],
 
['RPG-7',['Bazuca utilizada contra tanques.'],12000,6,{'DAMAGE': 50, 'RECHARGE': 10, 'CADENCY': 0, 'CAPACITY': 1, 'GAUGE': 0}],
  
#ITENS DE BATALHA
['granada',['Use numa batalha para causar dano á todos os inimigos na tela.'],100,3],
['granada de fumaça',['Use numa batalha para que todos os inimigos percam AGILIDADE.'],200,3],
['granada de luz',['Use numa batalha para que todos os inimigos percam sua vez.'],500,3],
['spray de pimenta',['Use numa batalha para atordoar um inimigo.'],40,3],
  
#REMÉDIOS
['antibiótico',['Use para infeccionar feridas letais e impedir hemorragias, parando de consumir a barra de HP.'],25,4,0],
['xarope',['Remédio utilizado para combater resfriados e alergias.'],10,4,1],
['comprimidos',['Remédios utilizados para combater náusea.'],30,4,2],
['pílulas',['Remédios utilizados para combater dor muscular.'],40,4,3],
['paracetamol',['Medicamento para combater a febre.'],40,4,4],
['desloratadina',['Medicamento para combater a tontura.'],40,4,6],
['pseudoefedrina',['Medicamento para combater o resfriado.'],40,4,6],
['ibuprofeno',['Medicamento para combater o resfriado e a febre.'],40,4,7],
['ciprofloxacino',['Antibiótico útil contra conjutivite,','resfriado e febre.'],40,4,6],
  
['soro antiescorpiônico',['Antídoto para combater veneno de escorpiões.'],40,4,6],
['soro antiofídico',['Antídoto para combater veneno de cobras.'],40,4,6],
['soro antiaracnídico',['Antídoto para combater veneno de aranhas.'],40,4,6],
  
['adrenalina',['Remédio utilizado para reviver uma pessoa inconsciente.'],60,4,5],
  
#ALIMENTOS
['pacoca',['Doce de amendoim, fácil de encontrar em padarias.'],1,9,2],
['coxinha',['Salgado feito com massa frita e recheada com frango, fácil de encontrar em lanchonetes.'],5,9,8],
['pastel',['Salgado feito com massa frita e recheado com queijo.'],3,5],
['pastel folheado',['Salgado feito com várias camadas de massa e queijo.'],6,12],
['brigadeiro',['Doce de chocolate.'],2,9,3],
['café',['Bebida quente que aumenta a energia.'],8,9,10],
['pão de queijo',['Salgado feito com massa de queijo.'],5,9,7],
['pudim',['Doce feito com leite condensado.'],10,9,15],
['bolo de fubá',['Doce feito com ovos, leite, fubá, manteiga, trigo e fermento.'],12,9,18],
['marmita',['Tem muitas coisas diferentes dentro, além de ser bem nutritivo!'],15,9,30],
  
#FERRAMENTAS
['pé de cabra',['Use para abrir portas trancadas'],50,6],
['lupa',['Use para pesquisar anomalias e registrá-las no Bestiário.'],5,6],
['radar',['Use para detectar anomalias no mapa.'],300,6],
['algemas',['Use para capturar anomalias e levá-las para pesquisa.'],50,6],
['frasco de sulfúrio 100ml',['Feita especialmente para guardar sangue verde. Capacidade de 10 inimigos'],200,6],
['garrafa de sulfúrio 250ml',['Feita especialmente para guardar sangue verde. Capacidade de 25 inimigos'],200,6],
['óculos',['Use para que pessoas com problemas de visão consigam ler.'],800,6],
  
#ITENS DE QUEST
['corda',['Use dentro de cavernas para descer e subir grandes alturas.'],70,7],
['chave',['Use dentro de instalações para abrir caminhos.'],10,7],
  
#ESSENCIAIS
['chaves',['Use para acessar seu quarto ou hospedagem.'],0,8,0],
['identidade',['Mostra suas informações básicas e prova sua autoridade acima dos civis.'],0,8],
['cartão de crédito',['Um item muito necessário na vida de um jovem adulto, use nos caixas de banco, nem imagine em jogar fora!'],0,8],
['carregador portátil',['Use para carregar seu celular.'],40,8],
['fones de ouvido',['Ao obter um, você consegue escutar o rádio do celular, mas atenção! ele quebra nos momentos mais inesperados.'],60,8],
['celular',['Mais importante que o cartão só o celular, pode ser usado para fazer chamadas e receber emails, mas lembre-se de recarregar.'],0,8],
  
#SUPLEMENTOS
['suplemento de força',['Aumenta a FORÇA permanentemente em +10.'],50,10,0],
['suplemento de ataque',['Aumenta o ATAQUE permanentemente em +10.'],50,10,1],
['suplemento de agilidade',['Aumenta a AGILIDADE permanentemente em +10.'],50,10,2],
['suplemento de resistência',['Aumenta a RESISTÊNCIA permanentemente em +10.'],50,10,3],
['suplemento de vitalidade',['Aumenta a VITALIDADE em +10'],50,10,4],
  
#REPELENTES
['repelente básico',['Evita anomalias de aparecer por 1 minuto.'],50,11,3600],
['super repelente',['Evita anomalias de aparecer por 3 minutos.'],100,11,10800],
['ultra repelente',['Evita anomalias de aparecer por 7 minutos.'],250,11,25200],
  
#ACESSÓRIOS
['mira laser',['Melhora a PRECISÃO de um fuzil ou metralhadora.'],200,13,0],
['silenciador',['Aumenta o ATAQUE de uma pistola.'],200,13,1],
['cartucho extra',['Aumenta a capacidade da arma'],100,13,2],
['coronha',['Aumenta a AGILIDADE da arma'],100,13,3],
['bandoleira',['Aumenta a estabilidade da arma'],100,13,3],
  
#CONFECÇÃO
['mola pequena','',0,14],
  
#TESOUROS
['vaso marajoara',['Um antigo vaso indígena feita da cerâmica do marajó.'],2000,15,0],
]

ARMOR = [
['colete I',5,20],
[],
['colete I',5,20],
]
   
EQUIPMENT = [
[['pistola',{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16, 'GAUGE': 38},['mira laser',5]],['carabina',{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16, 'GAUGE': 38},['coronha',5]],'_','_'],
[['pistola',{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16, 'GAUGE': 38},['silenciador',5]],['carabina',{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16, 'GAUGE': 38},['bandoleira',5]],'_','_'],
[['pistola',{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16, 'GAUGE': 38},['cartucho extra',5]],['carabina',{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16, 'GAUGE': 38},[]],'_','_'],
]
    
INVENTORY = [['_',['_','_','_'],['_','_','_'],['_','_','_'],['_','_','_']],['_',['_','_'],['_','_']]]
   
VEHICLES = {
'moto_0': {'SPEED': 8, 'ACCELERATION': 0.5, 'CAPACITY': 100, 'GAS': 0.075, 'LIGHTS': 2, 'DIRECTION': 1},
'moto_1': {'SPEED': 10, 'ACCELERATION': 0.25, 'CAPACITY': 100, 'GAS': 0.05, 'LIGHTS': 1, 'DIRECTION': 1}
}
   
CONTACTS = [['Sidney','989074454'],['Lúcia','990271802'],['Renan','990435671'],['Pietra','940028922'],['Paulo','987690021'],['Jane','991124257'],['Bianca','976564008'],['Diego','926148930'],
['Pizza Delivery','953478809'],['Correios','909236521'],['Maicon','923778988'],['Mercador','969696969'],['Iago','977904623'],['Sofia','923578103'],['Vinícius','960428331']]
    
CALLHIST = [['990271802',True]]
    
EMAILS = [['ddarj@cmail.com','Hello World!',
['This is a test'],
True],
  
['cangaceirostv@cmail.com','Proposta de entrevista',
['Boas novas, ' + CHARACTERS[0]['NAME'] + ' ' + CHARACTERS[0]['LASTNAME'] + '.',
' ',
'Com a repercussão dos casos de',
'anomalias do Departamento de',
'Detenção de Anomalias de',
'Itatiaia, sugerimos uma',
'entrevista com você e dois',
'participantes para o',
'Jornal da Noite.',
' ',
'A entrevista será ás 5:30 PM',
'e será gravado nos estúdios',
'da Cangaceiros TV, na',
'Av. Getúlio Vargas.',
' ',
'Aguardamos sua resposta',
'no local.'],
False],
  
['mendoncapietra7@cmail.com','Oiee',
['Só tô te testando menino'],
False],
  
['mendoncapietra7@cmail.com','Oiee',
['Só tô te testando menino'],
False]
]
   
INBOX = []
    
TASKS = [['Entrevista na Cangaceiros TV',False],['Encontrar a aprendiz',False],['Tirar o crachá da DDA',True]]
  
if CHARACTERS[0]['GENDER'] == 'male': gn = 'moço'; prps = 'meu'
elif CHARACTERS[0]['GENDER'] == 'female': gn = 'moça'; prps = 'minha'
else: gn = 'moçe'; prps = 'minhe'
 
if TIME[0] > 17: dt = 'Boa noite'
elif TIME[0] > 11: dt = 'Boa tarde'
elif TIME[0] > 5: dt = 'Bom dia'
else: dt = 'Boa noite'
   
'''
0 - obter item
1 - marcador do mapa
2 - ligação
3 - email
4 - tarefa
5 - bestiario
6 - troféu
7 - rank
8 - mover personagem
9 - esperar
10 - opções de fala
11 - pular falas
12 - repetir fala
13 - batalha
14 - falantes
15 - emoção
'''
    
DIALOGS = {
#OBJECTS
'MIRROR': [['Que peste feia é essa','ah, sou eu'],['Estou bonita...?'],['Bigodin finin','Cabelin na régua'],['Sempre arrasando'],['Tô bem arrumada'],['Dá pra sair']],
'SIDNEY WARDROBE': [['Qual roupa vou vestir agora?',[10,['Casaco xadrez','Ok'],['Blusa preta de banda','Sempre gostei do HUG'],['Blusa social','Essa tá boa']]]],
'BROKEN CLOCK': [['Isso tá quebrado faz tempo.']],
'SIETRA PORTRAIT': [['Essa foto me traz muitas lembranças...','...lembranças ruins.'],['...','Eles se davam bem...']],
'JANAGO PORTRAIT': [['Legal.'],['Essa foto foi em Búzios,','Foi o dia em que nós começamos a morar juntos.']],
'BED': [['Ah não...','a cama tá bagunçada de novo','...',0,'...abracadabra, cama arrumada!']],
'PICTURE': [['É uma pintura bonita','não tô entendendo nada','só sei que é bonita']],
'DIRTY SINK': [['A pia está cheia de louça suja...']],
'DIRTY COOKER': [['Tem arroz frio e uma frigideira engordurada no fogão.']],
'EMPTY FRIDGE': [['Água,sachês de ketchup e ovos...','Considero isso uma geladeira vazia.'],['Tá na de fazer as compras do mês.']],
'FRIDGE': [['A visão do paraíso.'],['O Iago comprou um monte de sorvete.','Esse idiota me conhece.']],
'OLD PC': [['Esse pc ainda usa Windows XP.']],
'MODERN PC': [['No canto da tela diz "Não é genuíno".']],
'PC GAMER': [['O teclado LED brilhando me deixa','ma-lu-co.']],
'OLD TV': [['O Maicon precisa trocar logo essa TV.']],

#PAPERS & SIGNS
'TAROT POSTER': ['BÚZIOS E CARTAS','Trago seu amor aos seus pés!','978543322'],
'MISSING POSTER': ['PROCURA-SE','Talita Manhães','Se você a viu, favor, ligue para: 992120342'],

#CHESTS
'SIDNEY NIGHTSTAND': [[[0,'pacoca',0]]],
 
#PLACES
'CASHIER INGRID': [['Os produtos estão nas pratileiras','é só você ir pegar e trazer aqui',0,'O quê? você quer que eu vá buscar pra você?!']],
'CASHIER SANDRA': [['Vai pedir alguma coisa?']],
'CASHIER YASMIN': [['Eu tenho que dormir...','compra logo o que tu quer...']],
   
'FARMACEUTIC': [['Não sabe que remédios comprar?',[10,['Não...','O que você quer tratar?',[10,['Resfriados e alergias','Se você estiver sentindo algum resfriado,','gripe, tontura ou fraqueza, um\
 simples','xarope já basta'],['Infecções e hemorragias','Esses são problemas fortes, mas não muito graves','Para infecções, use o antibiótico correspondente ao tipo de','contaminação.',0,'Se tiver\
  hemorragias, primeiro cicatrize a ferida','e depois ponha um band-aid para','evitar mais saída de sangue'],['Contaminação e Mal-estar','Caso se sinta alguma coisa parecida, pode ser','sinal de envenenamento ou\
   intoxicação, existem','várias pílulas para diversos tipos de tóxicos']],'Mais alguma pergunta?',[12,3]],['Tô de boa','Tudo bem','Se tiver alguma dúvida é só perguntar','Fique á vontade']]]],
   
'HOTEL ATTENDANT': [['Bom dia!','O que deseja?',[10,['Uma noite apenas','O custo é de 20 por pessoa',[10,['Ok','Aqui, seu quarto é o N° 902',[0,'chave',20]],['Deixa pra lá','Volte a hora que quiser']]],
['Estou apenas olhando','Sinta-se á vontade']]]],
   
#ENEMIES
'IRRATIONAL': ['A anomalia não entende nada do que você tá falando'],
'Alvo': ['Parece bobo, eu sei','Mas é bom já pegar o jeito da coisa.','Ás vezes você pode negociar com o oponente','E assim poupar sua vida.','Também pode obter informações','Importantes dele',
'Ou mesmo convencê-lo a parar de lutar'],
  
'Vinícius': [[10,['Eu não quero brigar contigo','Eu também não quero','Mas é preciso'],['Você pode ficar com a recompensa','Você está blefando?',[10,['Vai pegar?','É claro que vou!','...assim que acabar com você!'],['Esqueçe','Agora estou mais invocado!']]]]],
  
'Cremado Cremoso': [[10,['Cê tá bem mano?','Claro que não né?? Estou queimando feito palha nessa desgraça!'],['Vaza ou meto chumbo','Eu não tenho medo de você'],['A gente não quer nada contigo',
'Mas eu quero','Preciso de sangue!!']]],
   
#CONTACTS CALL
'989074454': [['Sidney']],
   
'991124257': [['Oi! Sou eu, a Jane']],
 
'990435671': [[[CHARACTERS[1]['NAME']+'! Precisamos de você aqui AGORA!','Eu sei que você saiu e coisa e tal, mas a gente PRECISA DE VOCÊ!','Estamos na Av. Jobim, venha logo!',[4, 'Urgência na Av. Jobim']],
['Caramba '+CHARACTERS[1]['NAME']+', será que você não entende a gravidade da situação??','Só você pode deter essa anomalia!']]],
   
'926148930': [['E aí mano? Beleza?','Então, aquela parada da transferência deu certo, adivinha?','Amanhã á noite eu tô indo pra Nova Friburgo!',0,'Tá tendo umas paradas estranhas lá, e me mandaram examinar','Vamos aproveitar pra gente se ver, beleza?']],
 
'976564008': [['Agora não, ' + CHARACTERS[0]['NAME'] + '! Eu tô trabalhando!','Me ligue depois, estou fazendo coisa importante aqui!']],
 
'940028922': [['Oh, olá! como vai, '+CHARACTERS[0]['NAME']+'?','Tenho andado ocupada esses dias, muita coisa pra fazer...','Não dá pra falar com você agora, desculpa','Me ligue mais tarde, ok?'],
['oie']],
   
'990271802': [['Garoto, o chefe quer te ver o mais cedo possível na delegacia','Espero que não tenha feito merda...']],
   
'987690021': [['Paulo']],
 
'953478809': [[dt + ', em que posso ajudar?',[10,['uma pizza grande','já estamos á caminho'],['uma pizza média','já estamos á caminho']]]],
 
'909236521': [[dt + ', correios']],
 
'923778988': [[CHARACTERS[0]['NAME'] + ', melhor repensar a vida que tá levando','não quero ser duro, mas eu tô preocupado contigo mano','* sidney desligou *']],
 
'969696969': [['Olá ' + prps + ' cliente, em que posso ajudar?']],
 
'977904623': [['Iago']],
 
'923578103': [['Sofia']],
 
'960428331': [['Vinícius']],

'978543322': [['Oi, em que posso ajudar?','Ah...eu já parei de fazer isso há muitos anos','Tchau']],
   
#CITIZENS DIALOG
'WORRIED MAN': [[[10,['O que está havendo?','Eu não faço idéia!'],['Estou com eles','Oh, desculpe...',[8,1,1]]]]],

'OLD MAN': [['É bom você sempre tirar dúvidas com o entendido do assunto.','Minha filha comprou um antibiótico e pensou que era pra beber.',0,'Agora ela tá no hospital...','Essa menina...']],
'INJURIED DAUGHTER': [['É bem vergonhoso dizer o motivo','Mas estou internada porque bebi antibiótico','Devia ter escutado meu pai...']],
'PRETTY MOM': [['Minha filha tá me pertubando pra levar alguns doces pra ela.','É assim toda hora, ela vai parar já já.']],
'PRESSING CHILD': [['Mãe! Tem tantos doces aqui!','Eu quero! Eu quero! EU QUERO!']],

'DOCTOR': [['Você sofreu várias fraturas no corpo','A conta dos cuidados foi de $100 por pessoa']],
'WORRIED NURSE': [['Você deveria se cuidar mais','É muito comum te ver por aqui']],
'HINT NURSE': [['Tome cuidado com sua vida!','Não digo por causa da saúde, mas pelo dinheiro',0,'Se não tiver dinheiro da próxima vez, pode','entrar em prejuízo.']],
'PATIENT': [['Eu quero ir pra casa logo','A comida daqui é horrível!']],
'IMPATIENT PATIENT': [['Eu tô na fila desde anteontem','Parece até que nunca anda!']],

'BANK GUARD': [['Ponha qualquer objeto de metal que tiver','na caixa ao lado']],
'UNLUCKY MAN': [['Não é possível uma coisa dessas!','O caixa acabou de entrar em manutenção!','ERA MINHA VEZ!']],
'OLD WOMAN': [['Como que faz pra tirar a telesena aqui?']],

'NPC_1': [['Meu nome é Francisco Irineu','Eu odeio meu nome...'],['Hey, você é o cara que expurgou aquele poltergeist?']],
   
'NPC': ['Oi...eu te conheço?','Você não deveria estar falando com estranhos','Agora não ' + gn + '! Eu tô com pressa!','Afe, mercenários...','Não quero falar com você','Licença'],
'DOOR': ['Não conheço você','Quem é você?','O que você quer?','Vai embora!'],
   
'HOTEL DOOR': ['Esse é meu quarto','Aqui não é seu quarto, ' + gn, gn + 'está perdido?'],
   
'KONAMI GUY': ['Hey, sabe o que acontece se você apertar cima, cima, baixo, baixo, esquerda, direita, esquerda, direita, B, A e START?','Merda nenhuma!'],
   
#CHARACTERS DIALOG
'TEST': [['this is a test, DUDE!',[0,'pacoca',0],'map marker',[1,10,10],'calls',[2,7,True],'tasks',[4,'Test'],'bestiary',[5,0],'trophies',[6,0],'rank',[7],'move',[8,1],
'wait',[9,100],'choose',[10,['option a','got a'],['option b','got b']],'jump',[11,1],'i never appear','repeat?',[10,['sure',[12,3]],['please no','fine']],'battle',[13,0],'end!']],
  
'PROLOGUE': [['Hey?','...','Está me ouvindo?','hm?','Você entendeu o que eu disse?','Pra ser sincera, não','...','Estava pensando, com a cabeça em outro lugar...','...sobre o quê você estava pensando?','...eu...eu fiz\
 coisas...','...','...eu fiz coisas que...tantas coisas...que não...pensei direito','...','...eu me arrependo tanto, nada disso deveria ter acontecido, foi tudo por causa de uma briga, e eu trouxe essa desgraça\
 pra minha vida...eu achei que poderia ajudar nós dois, achei que eu seria aquela que iria nos tirar do buraco...','...','...mas no final eu só afundei ainda mais....','é natural pensar coisas assim, mas tente sempre\
 se lembrar que o que você fez você não fez por mal, você estava querendo ajudar, achar uma solução','...sim...','isso não te anima?','nem um pouco...porque eu atrapalhei ao invés de ajudar...não fui inteligente','é\
 difícil','muito...mesmo...','...','você está fazendo atitutes inteligentes agora, está procurando ajuda, reconhecendo seu erro, se afastando daquilo que te traz problema','...sim...','você precisa\
 continuar assim','...','ei','?','me prometa de que você nunca mais vai voltar a pegar em uma arma, certo?','certo! certo!','nem que um monstro apareça no mato ou um bandido invada sua casa, nunca, NUNCA MAIS, encoste\
 em nenhum arma!','...','está me ouvindo?','sim','ótimo...','...','já está na hora de ir','não pode ficar mais um pouco?','desculpa, mas pode continuar amanhã, eu também tenho sanidade mental','claro, \
desculpa...',[2,'990435671',True]]],
   
'CHAPTER1': [['Então...como tá o trampo?','Que trampo?','Você sabe, o de mercenário','...','Tá muito puxado?','...bastante','Acho que já ouviu alguns comentários sobre eles','Sim...até demais, mas nem ligo',
'Como não?','Mano, foi graças á essa vida que tô onde tô agora, não vou deixar que alguns comentários mudem minha cabeça. Eu gosto do que faço','Sim, mas seria melhor você arranjar\
 alguma outra coisa né?','Isso até eu quero né','Então por que você não sai dessa?','Porque não dá cara! Não vão contratar alguém com ficha suja','Ah, é mesmo...','Além do mais eu já me garanto onde eu tô, se eu trocar de\
  emprego posso ser demitido de novo','Já passou perrengue demais, não é?','Sim','...sei não, ainda acho melhor você fazer alguma outra coisa, esse negócio de matar e arriscar a própria vida','Que vida?','...','...','...',
'Eu já tô indo','Deixa que eu pago essa','Sério?','Sim, é por minha conta','Você é demais cara'],
['Teria sido melhor ficar lá no bar',11,'BORA LOGO!','!','NÃO TENHO O DIA TODO!','...','Que saco...','...','Que demora','...','Pra você ver né, até pra isso tem toda essa baboseira','Hã? Ah, sim, sim, sim...','Era pra\
 ser um negócio rapidinho...tranquilo, de boa, mas não! Eu sou obrigada a ficar aqui esperando!','Eu já tô até acostumado','Ai não ia me acostumar nunquinha, deus me livre','É que já é coisa da rotina, todo ano tem isso',
'É?','Ahã...só que agora saiu mais cedo, geralmente é só lá pra setembro','Você mercenário?','Sou','Ah, pra saber dessas coisas...','Por que? você não é?','Não, mas daqui a pouco já tô virando uma!','Mas aqui\
 não é onde renova a carteira?','Não,disseram que o registro é aqui também','onde?','no último guinchê','Ah sim, agora eu vi','Vem cá, e como é essa coisa toda de mercenário, matar pessoas...','A gente não mata\
 pessoas','Ah sim, desculpa...','Não,  tudo bem, é normal','Então o que vocês fazem exatamente?','Olha, a primeira coisa que você deve saber se quiser virar mercenária, é que certas coisas são totalmente confidenciais',
'Uh! sério?','Sim, sigiloso','Tipo homens de preto né?','Não é pra tanto, mas é tipo','Mas eu achava que era só matar e ganhar dinheiro!','ihhhh...vai sonhando, é um bicho chato','Sério?','Quer dizer, tirando toda a\
 diversão, ainda é um trabalho, tem que estar sempre disposto, te chamam na hora que querem, é cansativo, tem os chefes, a gente recebe pouco...','QUÊ?','fala baixo!','desculpa','...','...recebe pouco?','depende do quanto\
 você caça','Ah...então se eu caço bastante','ganha bastante, isso aí','Mas o que vocês caçam exatamente?','segredo','Ah! deixa disso! fala logo!','Se quiser saber mesmo, vai ter que esperar até lá dentro','tá\
 bom então...ô Agente G','...','Beleza James Bond','tá já chega','ei já tá na sua vez','ah sim'],
['Então esse é seu nome?','Sim...' + CHARACTERS[1]['NAME'] + CHARACTERS[1]['LASTNAME'],
'Ok...Prazer ' + CHARACTERS[1]['NAME'],'Prazer','Então...o que tem que fazer agora?','Bom, agora você pode pegar sua primeira arma ali, e se quiser já pode treinar um pouco de tiro','Você vem comigo?',
'Não...eu já tenho que ir','Ah por favor! Eu não entendo das coisas aqui!','...','please!',[10,['Tá bom','YASS','Não se empolga, tá','Então tá, onde que pega o brinquedinho?','Me segue',[11,1]],['Agora não','Tudo bem então...\
A gente se vê por aí','Eu tô aqui todo dia','Beleza!','...','Ah! eu só posso vir aqui nos sábados!','Beleza!','Tchau!','Essa garota tá querendo alguma coisa comigo...',[11,3]]]],
['É aqui que faz o treinamento?','exatamente','Ok...','...','me ensina a atirar?','Tudo bem',[9,2],'Primeiro põe esses óculos aí','esses?','sim, agora mira, não põe muito perto senão machuca o olho','ah sim',
'e...aperta o gatilho',[13,'Alvo']],
['Nossa, mandou muito','Eu sou demais!','Não sério, você já atirou antes?','Um pouquinho','Um pouquinho?!','Tá, eu sei atirar','Se você já sabia atirar, por que pediu minha ajuda?','Vai saber',
'Ai,ai...','Faz muito tempo já, começei quando...',[3,EMAILS[0].copy()],'Pera aí rapidinho','O que foi?','Chegou email','...','Desculpa ' + CHARACTERS[0]['NAME'] + ', eu tenho que ir!','De novo?',
'É um caso pra resolver','agora?','É o que eu te falei antes','Posso ir com você?','Vai devagar querida, eu tô em outro nível','Por que não posso ir?','Muita coisa ainda, muita coisa, te explico depois','Pera aí! Mizera...'],
['O que tá fazendo aqui?','Quem pergunta sou eu! O que VOCÊ tá fazendo aqui?','Com certeza não é deixar você roubar minha recompensa','E quem disse que ela é sua?','Garoto,melhor sair do meio, ou vai dar\
 muito mal pra nós dois','que assim seja então!',[13,'Araraucária','Vinicius']],
['Lembra de mim, filho da mãe?','você!','Essa é pra aprender a não mexer comigo!',[9,2],'???','O que você estava fazendo?',[10,[],[]]]],
   
'CHAPTER2': [],
   
'BIANCA': [['Hey ' + CHARACTERS[0]['NAME'] + ', fique com essa lupa, Eu fiz ela apenas para pesquisar anomalias.','Quando enfrentar uma anomalia que não está registrada no bestiário,','Use-a para registrar a anomalia.',[0,'lupa']]],
'SIDNEY': [['1Não tenho um minuto de paz nessa desgraça!!','2Eu achei que eles iam ficar de boa','1Se tem uma coisa que você tem que saber sobre as pessoas é que elas odeiam pessoas com armas na mão atirando por aí','2Mas você salvou elas! Matou esse...essa...','1...Lata Alada','2Que','1O nome da anomalia','2Noooooosa!','1Vou botar essa no Bestiário','2Tá, mas elas deveriam ter um pouquinho de consideração né?','1Ninguém tem um pingo disso com ninguém da DDA','2Conplicado...','1É gente que nunca viu uma gota de sangue na vida e já ficam chocadas, esse aí é o mesmo pessoal que fica com esses papos de veganismo depois','2hmmm...nah']],
'JANE': [["I don't wanna to","I not in a good mood, you know...",[10,["It's all right?","Oh, no! I just don't want to cause any trouble"],["Fine then","Yeah"],["But you need to do it","Look, since the last time I put my hand on a gun, it wasn't a wise choice!","I don't want people to suffer from my mistakes!","I just mess everything up...",[10,["You don't","I know you are saying this just to chill me down, but I don't want to fool myself","I have to accept this"],["Everyone makes mistakes","But not everyone kills a person, right?",[10,["What?","Oh, you don't know?","Awwww...I should shut my mouth"],["...","..."]]],["It's hard","At least you recognise"]]]],0,'Well, I have to go...','See you later']],
'MATT KAI': [['EU AMO PINK FLOYD','EU AMO PINK FLOYD','EU AMO PINK FLOYD','2Esse é o criador do jogo?','1Ele mesmo','2Sem nexo','1Mó fita']]
}
    
NEWS = [
[
[['Polícia Municipal abre a','renovação da carteira'],'Tereza Rocha',['Em 4 de abril, a Polícia Municipal abriu a renovação da carteira para mercenários. A carteira de identificação de Mercenário é \
obrigatória não só por identificação, mas por questões de segurança, depois que a câmara dos deputados aprovou a reforma armamentista, qualquer cidadão com a identificação de mercenário é livre para portar \
e possuir uma arma de fogo.','',' Recentemente, houveram vários casos de assassinatos não registrados pela polícia, pela incapacidade da polícia de analisar todos os casos separadamente, mercenários tem sido \
recompensados para cuidar desses assassinatos misteriosos.','','Devido a isso os dados de homicídio por armas de fogo aumentaram consideravelmente no estado, isso se deve á facilidade de se obter uma arma e também de \
reduzir a pena de um criminoso para servir ao estado como mercenário. O criminólogo Mauro Fidélis fala sobre a situação.','','"O que a polícia do rio de janeiro fez foi um ato irresponsável e inpensável, pois \
graças á essa facilidade de se armar, vários criminosos podem se aproveitar e utilizá-las para fins maliciosos, e mesmo com tantos casos de homicídios não registrados, o que custava a polícia recrutar mais policiais ou\ fazer uma investigação profunda e mais elaborada á respeito?"','','Sabendo disso, tudo o que podemos esperar é que os mercenários façam bom uso de seu poder bélico.']],
[1,['sex','23'],['sab','20'],['dom','18'],['seg','17'],['ter','19']],
],
   
[
[['Relato de assombração em Itatiaia','pode ser verdadeiro'],'Jéssica Ramone',['Ás 11:30 da noite passada,','moradores de Itatiaia relataram','um caso incomum entre vários','da polícia, \
foi registrado um','caso de uma assombração','(vulgo Poltergeist) na casa de','Maria Elisângela das Dores,','35 anos.','','"Não sabia o que fazer, eu nunca','imaginei que assombrações\
 ou','fantasmas realmente existissem,','sempre achei que eram apenas','contos de criança.", diz','Maria Elisângela.','','Apesar de inesperado e muito','estranho, o relato foi comprovado','\
por filmagens do Departamento','de Detenção de Anomalias de','Itatiaia, além dos danos','causados pela assombração na','casa e nos moradores da região.','','Aparentemente este não é o','\
único relato de moradores a','respeito de uma assombração,','foram registrados 5 relatos em','um único mês e 12 em 3 meses, mas','se as investigações persistirem','este pode ser o \
primeiro','relato confirmado de uma','assombração no país.']],
[['Engarrafamento na zona sul'],'Gisele Peres',['Muito trânsito']]
],
   
[
[['Museu Histórico de Petrópolis','é fechado por assombrações'],'Jéssica Ramone',['Na terça feira passada do dia 13 de Novembro, visitantes do Museu Imperial presenciaram uma cena assustadora, \
As exposições começaram a atacar os visitantes, como é relatado por vários entrevistados.','"Foi começando devagar, uma pintura ia se despendurando da parede...uma estátua começava a piscar...\
e quando percebe estão fechando os corredores e chamando os seguranças."','']],\
[['FLA x FLU'],'Gustavo Pinhão',['Muito disputado']]
]
   
]
   
RADIO = {'0': [],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'11':[],'12':[],'13':[],'14':[],'15':[],'16':[],'17':[]}
 
for i in range(0,18):
    for j in os.listdir('Songs/FM_'+str(i)):
        RADIO[str(i)].append(j)
    
MANUAL = [['CONTROLES',['Aperte '+LEFT+', '+RIGHT+', '+UP+' e '+DOWN+' para mover seu personagem']],\
['CELULAR',['O celular é o equivalente ao','menu do jogo, acesse-o','apertando ' +PHONE+'.','\
','Na barra superior do celular,','aparecem informações de data,','hora, sinal e carga.','\
','Atente-se á carga do celular:','ao se esgotar, você fica','incapacitado de utilizá-lo, para','carregar, use o carregador.','Utilize carregadores portáteis','ao se afastar da área urbana.','\
','Os créditos servem para fazer','ligações, recarregue-os na','farmácia.','\
','Fora da área urbana, o sinal',' pode diminuir, e alguns','aplicativos estarão indisponíveis.','\
','Esses são os aplicativos que','pode usar:','\
','MAPA: ver o mapa da cidade,','traçar rotas e ver informações','dos locais. Não mostra as','regiões florestais.','\
','CHAMADAS: ver os contatos','salvos, histórico de ligações','e fazer chamadas. Quanto mais','longa for a chamada, mais','créditos são gastos.','\
','EMAIL: ver emails enviados da','agência e outras instituições.','\
','NOTÍCIAS: ver as últimas notícias','da região, podem aparecer casos','resolvidos e casos para resolver.','\
','RÁDIO: escutar música aleatória','de várias estações diferentes,','ao se afastar da área urbana','não é possível utilizá-lo.','É necessário um fone de','ouvido para usá-lo.','\
','CÂMERA: tirar capturas de tela e','ver capturas salvas.','\
','TAREFAS: ver missões e casos','já cumpridos ou para cumprir.','\
','STATUS: ver as informações','completas dos atributos','do jogador.','\
','BESTIÁRIO: banco de dados da','agência onde se registram','todas as anomalias.','\
','CONQUISTAS: ver todas as',' conquistas do jogo.','\
','PLACAR: ver sua posição no','placar do jogo.','\
','AJUDA: ler o manual completo','do jogo.','\
','CONFIGURAÇÕES: editar opções','de som, imagem, controles,','idioma e etc.','\
','SOBRE: ver créditos e liçenca GNU.','\
','SALVAR: salva o progresso','atual do jogo.']],\
['BATALHA',['Para vencer uma batalha, você deve derrotar todos os inimigos da tela ao mesmo tempo que deve se defender dos ataques inimigos.','\
HP: A barra vermelha mostra seu HP, ela pode ser maior dependendo do seu nível de VITALIDADE, a barra diminui com o ataque inimigo e uma barra amarela diminui lentamente com ela, baseada no nível de RESISTÊNCIA.\n\n\
PP: Mostra a quantidade de munição para as armas de fogo, sendo a barra diferente para cada arma.','\
XP: Seu nível de experiência, quanto mais experiente for nas batalhas, maior seu grau dentro da agência.','\
Numa batalha, aparecem como opções os itens equipados, mas você também pode abrir seu inventário e fugir da batalha. Seu desempenho ao atacar é baseado nos seus atributos, \
ao mesmo tempo em que os inimigos também possuem seus atributos para defender, sendo esses: ','\
ATAQUE: distância dos extremos da barra','\
AGILIDADE: velocidade do cursor da barra','\
RESISTÊNCIA: velocidade de consumo da barra de HP','']],\
['LOCAIS',['']]]
  
PRODUCTS = [
[10,12,5,17,22,45,50,61,64],
[10,12,5,17,22,45,50,61,64],
[10,12,5,17,22,45,50,61,64],
[10,12,5,17,22,45,50,61,64],
[49,50,51,54]
]
   
BATTLE = [
' aparece no caminho!',' encurrala você!',' é emboscado!',
'incrível!','errou...','sem dano',
'VITÓRIA','acertos: ','dano total: ','vitalidade perdida: ','bônus de tempo: ','jogadores: ',' de experiência',
' subiu de nível!',
' tentou fugir','...mas falhou','...e consegue!',
' vai ',' usa ',' perdeu ',' ganhou ',' de ATAQUE',' de AGIIDADE',
' foi envenenado',' está com náuseas',' foi infectado',
' está inconsciente...','DERROTA'
]
 
MENU = ['mapa','chamadas','correios','notícias','rádio','câmera','bestiário','tarefas','carteira','conquistas','placar','manual','ajustes','sobre','salvar',
'sem conexão','não há contatos','sem créditos...','sem dinheiro...','não há mensagens','sem sinal','nenhuma anomalia registrada','não há tarefas',
'telefone','contatos','histórico','novas','lidas','todas','fazer','feitas',
'créditos: ','chamando...','DE: ','PARA: ','VITALIDADE: ','ATAQUE: ','AGILIDADE: ','VENENO','NÁUSEA']
 
ABOUT = ['MUTATION PURGE','Criado por Matt Kai','Source code por Matt Kai','Feito em Python','Twitter','GitHub','GNU General Public License']
 
SHOP = ['comprar','sair','nada aqui','banco: $','dinheiro: $','sacar','depositar','cancelar']
 
DISCLAIMER = ['Esta é uma obra de ficção,','e quaisquer semelhanças com','acontecimentos reais são','mera coincidência.','',
'Uma certa porcentagem da','população sofre de condições','como eplepsia e convulsões,','por isso sempre consulte','seu médico antes de jogar']

ACHIEVEMENTS = [
['Zerado','Ganhar todos os troféus',0,''],
  
['YAS','Fique na 1 posição do placar',0,''],
['Meh','Fique na 2 posição do placar',0,''],
['Bruh','Fique na 3 posição do placar',0,''],
  
['Piloto','Vencer 10 corridas',0,''],
['Fúria da Estrada','Vencer 50 corridas',0,''],
['Corredor da Noite','Vencer 100 corridas',0,''],
  
['Exterminador','Expurgue 100 anomalias',0,''],
['Terror dos imundos','Expurgue 500 anomalias',0,''],
['Purificador','Expurgue 1000 anomalias',0,''],
  
['Espadachim','Compre todas as armas brancas',0,''],
['Arsenal Pesado','Compre todas as armas de fogo',0,''],
['Por Precaução','Compre todos os coletes',0,''],
['Os 6 Lendários','Eleve o nível de todos ao 100',0,''],
  
['Sociável','Registre todos os contatos',0,''],
['O Caçador de Mitos','Registre todas as anomalias no Bestiário',0,''],
  
['Não que eu me orgulhe disso','Roube um caixa',0,''],
['Zé Droguinha','Roube um veículo',0,''],
['Vergonha da Profission','Mate um cidadão',0,''],
['Traíra','Fuja da polícia',0,''],
  
['Eu Sou a Lenda','Derrote uma anomalia maior apenas usando armas brancas',0,''],
['Meros Insetos','Vença 5 batalhas consecutivas sem tomar dano',0,''],
['Salmos 91:7','Vença um exército sem tomar dano',0,''],
['Fugir é sabedoria','Fuja de uma batalha 20 vezes',0,''],
['Podre de Rico','Consiga 1.000.000.000 em dinheiro vivo',0,'']
]