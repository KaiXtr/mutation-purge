# -*- coding: utf-8 -*-
import pygame
import sqlite3
import os
 
def new_data():
    global ID, LANG, SFX, MSC, UP, DOWN, LEFT, RIGHT, ACT, RUN, PHONE, BAG, SPEED, COLOR, INVENTORY, WEATHER, BORDER,\
    FORMATION, MAP, PX, PY, TIME, DATE, CHAPTER, MORALITY, ATM, MONEY, CREDIT, BATTERY, GAS, GAMETIME, CHARACTERS, PARTY, CONTACTS, CALLHIST, INBOX, TASKS, TACTICAL, BESTIARY, ACHIEVEMENTS
 
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
      
    LANG = 'PT'
    SFX = 0.8
    MSC = 0.6
    UP = pygame.K_w
    DOWN = pygame.K_s
    LEFT = pygame.K_a
    RIGHT = pygame.K_d
    ACT = pygame.K_g
    RUN = pygame.K_h
    PHONE = pygame.K_BACKSPACE
    BAG = pygame.K_RETURN
    SPEED = 2
    COLOR = [242,30,30]
    BORDER = 0
      
    MAP = 1
    PX = 184
    PY = 476
    TIME = [0,32,0]
    DATE = [25,12,0,1]
    WEATHER = 0
    CHAPTER = 0
    MORALITY = 0
    GAMETIME = 0
    FORMATION = 0
      
    ATM = 200
    MONEY = 50
    CREDIT = 0
    BATTERY = 360
    GAS = 100.0
     
    for i in range(6):
        CHARACTERS[i]['NAME'] = ''
        CHARACTERS[i]['LASTNAME'] = ''
        CHARACTERS[i]['LEVEL'] = 0
 
    PARTY = [[1]]
    CONTACTS = [['Maicon','923778988'],['Mercador','969696969'],['Pizza Delivery','953478809']]
    CALLHIST = []
    INBOX = []
    TASKS = []
    TACTICAL = [[1,1,1,1]]
    BESTIARY = []
    for i in ACHIEVEMENTS:
        i[2] = 0
        i[3] = ''

    INVENTORY = [
    [[['_','0000','_','_'],['phone','360100','_','_'],['wallet','00005000000300','credit_card','id_card0'],['locksmith1','02020000','key_bedroom','key_vehicle'],['_','0000','_','_']],
    [['amulet1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['clth_jacket1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['ammo.38','0000','_','_'],['_','0000','_','_']],
    [['clth_shirt1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['bag1','0000','_','_'],['gun_revolver.38','0006','aim1','acc_cartridge'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
     
    [[['head_glasses','0000','_','_'],['food_peanut_candy','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['clth_jacket5','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['bag1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
     
    [[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['bag1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
     
    [[['amulet4','0000','_','_'],['repellent1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['amulet5','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['food_coxinha','1103','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['charger','000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['bag1','0000','_','_'],['gun_revolver.38','0006','aim3','acc_gunbutt'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
     
    [[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['bag1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
     
    [[['amulet7','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['amulet6','0000','_','_'],['condiment_ketchup','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['amulet2','0000','_','_'],['_','0000','_','_'],['pill_vitality','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['amulet3','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
    [['bag1','0000','_','_'],['gun_revolver.38','0006','aim2','acc_bandolier'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
    ]
 
    STORAGE = [['bandolier','0000','_','_']]
      
    try:
        com.execute("CREATE TABLE settings (id integer,lang text,sfx integer,msc integer,up text,down text,left text,right text,act text,run text,phone text,inventory text,speed integer,color1 integer,color2 integer,color3 integer,border integer)")
        com.execute("CREATE TABLE data (id integer,gt integer,fr integer,map integer,x integer,y integer,time text,date text,weather integer,chapter integer,morality integer,atm integer,money integer,credit integer,battery integer,gas integer)")
        print('table created')
    except: pass
      
    trg = False
    com.execute("SELECT id FROM settings")
    for i in com.fetchall():
        if i[0] == ID: trg = True
    if trg == True:
        com.execute("DELETE FROM settings WHERE id=" + str(ID))
        com.execute("DELETE FROM data WHERE id=" + str(ID))
     
    print(ID)
    com.execute("INSERT INTO settings VALUES (" + str(ID) + ",'PT',0.8,0.6,'W','S','A','D','G','H','BACKSPACE','RETURN',2,255,255,255,0)")
    com.execute("INSERT INTO data VALUES (" + str(ID) + ",0,0,1,0,0,'0830','1003001',0,0,0,0,0,255,10,10)")
      
    com.execute("DROP TABLE IF EXISTS characters" + str(ID))
    com.execute("CREATE TABLE characters" + str(ID) + " (n integer,name text,lastname text,gender text,level integer,xp integer)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(0,'','','male',0,0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(1,'','','female',0,0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(2,'','','male',0,0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(3,'','','female',0,0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(4,'','','male',0,0)")
    com.execute("INSERT INTO characters" + str(ID) + " VALUES(5,'','','female',0,0)")
    tbl.commit()
      
    com.execute("DROP TABLE IF EXISTS party" + str(ID))
    com.execute("CREATE TABLE party" + str(ID) + " (n integer,p1 integer,p2 integer,p3 integer)")
      
    com.execute("DROP TABLE IF EXISTS contacts" + str(ID))
    com.execute("CREATE TABLE contacts" + str(ID) + " (n integer)")
 
    com.execute("DROP TABLE IF EXISTS callhist" + str(ID))
    com.execute("CREATE TABLE callhist" + str(ID) + " (n integer,w integer)")
 
    com.execute("DROP TABLE IF EXISTS inbox" + str(ID))
    com.execute("CREATE TABLE inbox" + str(ID) + " (n integer,red integer)")
 
    com.execute("DROP TABLE IF EXISTS tasks" + str(ID))
    com.execute("CREATE TABLE tasks" + str(ID) + " (tsk text,don integer)")
 
    com.execute("DROP TABLE IF EXISTS tactical" + str(ID))
    com.execute("CREATE TABLE tactical" + str(ID) + " (n integer,pl1 integer,pl2 integer,pl3 integer,pl4 integer)")
      
    com.execute("DROP TABLE IF EXISTS bestiary" + str(ID))
    com.execute("CREATE TABLE bestiary" + str(ID) + " (idx text,id text,date text)")
      
    com.execute("DROP TABLE IF EXISTS achievements" + str(ID))
    com.execute("CREATE TABLE achievements" + str(ID) + " (idx integer,got integer,date text)")
      
    com.execute("DROP TABLE IF EXISTS inventory" + str(ID))
    com.execute("CREATE TABLE inventory" + str(ID) + " (it1 text,ip1 text,ic11 text,ic21 text,it2 text,ip2 text,ic12 text,ic22 text,it3 text,ip3 text,ic13 text,ic23 text,\
    it4 text,ip4 text,ic14 text,ic24 text,it5 text,ip5 text,ic15 text,ic25 text,it6 text,ip6 text,ic16 text,ic26 text)")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('phone','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('credit_card','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('id_card','0001','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('vest1','0010','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('coxinha','1103','ketchup','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('ammo.38','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('pill_vitality','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('bag1','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('revolver.38','0016','aim1','_','_','0000','_','_','_','0000','_','_','revolver.38','0016','_','_','_','0000','_','_','revolver.38','0016','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    com.execute("INSERT INTO inventory" + str(ID) + " VALUES('_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_','_','0000','_','_')")
    tbl.commit()
 
    com.execute("DROP TABLE IF EXISTS storage" + str(ID))
    com.execute("CREATE TABLE storage" + str(ID) + " (it text,ip text,ic1 text,ic2 text)")
    com.execute("INSERT INTO storage" + str(ID) + " VALUES('bandolier','0000','_','_')")
     
    com.close()
    tbl.close()
  
def load_data():
    global ID, LANG, SFX, MSC, UP, DOWN, LEFT, RIGHT, ACT, RUN, PHONE, BAG, SPEED, COLOR, WEATHER, BORDER,\
    FORMATION, MAP, PX, PY, TIME, DATE, CHAPTER, MORALITY, ATM, MONEY, CREDIT, BATTERY, GAS, GAMETIME, PARTY, CONTACTS, CALLHIST, INBOX, TASKS, TACTICAL, BESTIARY, INVENTORY
      
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
     
    com.execute("SELECT id from settings")
    print(com.fetchall()[0])
    com.execute("SELECT lang FROM settings")
    LANG = com.fetchall()[ID][0]
    com.execute("SELECT sfx FROM settings")
    SFX = com.fetchall()[ID][0]
    com.execute("SELECT msc FROM settings")
    MSC = com.fetchall()[ID][0]
    com.execute("SELECT up FROM settings")
    UP = int(com.fetchall()[ID][0])
    if UP == 'W': UP = pygame.K_w
    com.execute("SELECT down FROM settings")
    DOWN = int(com.fetchall()[ID][0])
    if DOWN == 'S': DOWN = pygame.K_s
    com.execute("SELECT left FROM settings")
    LEFT = int(com.fetchall()[ID][0])
    if LEFT == 'A': LEFT = pygame.K_a
    com.execute("SELECT right FROM settings")
    RIGHT = int(com.fetchall()[ID][0])
    if RIGHT == 'D': RIGHT = pygame.K_d
    com.execute("SELECT act FROM settings")
    ACT = int(com.fetchall()[ID][0])
    if ACT == 'SPACE': ACT = pygame.K_SPACE
    com.execute("SELECT run FROM settings")
    RUN = int(com.fetchall()[ID][0])
    if RUN == 'SPACE': RUN = pygame.K_SPACE
    com.execute("SELECT phone FROM settings")
    PHONE = int(com.fetchall()[ID][0])
    if PHONE == 'BACKSPACE': PHONE = pygame.K_BACKSPACE
    com.execute("SELECT inventory FROM settings")
    BAG = int(com.fetchall()[ID][0])
    com.execute("SELECT speed FROM settings")
    SPEED = com.fetchall()[ID][0]
    com.execute("SELECT color1 FROM settings")
    COLOR[0] = com.fetchall()[ID][0]
    com.execute("SELECT color2 FROM settings")
    COLOR[1] = com.fetchall()[ID][0]
    com.execute("SELECT color3 FROM settings")
    COLOR[2] = com.fetchall()[ID][0]
    com.execute("SELECT border FROM settings")
    BORDER = com.fetchall()[ID][0]
      
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
    DATE = [int(res[0:2]),int(res[2:4]),int(res[4:6]),int(res[6])]
    com.execute("SELECT weather FROM data")
    WEATHER = com.fetchall()[ID][0]
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
        CHARACTERS[i]['XP'] = res[i][5]
      
    com.execute("SELECT * FROM party" + str(ID))
    res = com.fetchall()
    PARTY = []
    for i in res: PARTY.append([i[1],i[2],i[3]])
 
    com.execute("SELECT * FROM contacts" + str(ID))
    res = com.fetchall()
    CONTACTS = []
    for i in res: CONTACTS.append(NUMBERS[i[0]].copy())
 
    com.execute("SELECT * FROM callhist" + str(ID))
    res = com.fetchall()
    CALLHIST = []
    for i in res: CALLHIST.append([i[0],i[1]])
 
    com.execute("SELECT * FROM inbox" + str(ID))
    res = com.fetchall()
    INBOX = []
    for i in res:
        mail = EMAILS[i[0]].copy()
        mail.append(i[1])
        INBOX.append(mail)
 
    com.execute("SELECT * FROM tasks" + str(ID))
    res = com.fetchall()
    TASKS = []
    for i in res: TASKS.append([i[0],i[1]])
          
    com.execute("SELECT * FROM tactical" + str(ID))
    res = com.fetchall()
    TACTICAL = []
    for i in res: TACTICAL.append([i[1],i[2],i[3],i[4]])
      
    com.execute("SELECT * FROM bestiary" + str(ID))
    res = com.fetchall()
    BESTIARY = []
    for i in res:
        apd = FREAKS[i[0]].copy()
        apd['N'] = i[0]
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
     
    '''com.execute("SELECT * FROM inventory"+ str(ID))
    res = com.fetchall()
    itm = 1
    for i in range(len(res)):
        INVENTORY[i][0] = res[i][0]
        for y in range(len(INVENTORY[i])):
            if y != 0:
                for x in range(len(INVENTORY[i][y])):
                    INVENTORY[i][y][x] = res[i][itm]
                    itm += 1
        itm = 1'''
      
    com.close()
    tbl.close()
    CONTACTS = [['Sidney','989074454'],['Jane','991124257'],['Renan','990435671'],['Diego','926148930'],['Bianca','976564008'],['Lúcia','990271802'],['Maicon','923778988'],['Mercador','969696969'],['Pizza Delivery','953478809']]
    TASKS = [['test',False],['yeey',False],['test',False],['wow',False],['yikes',False],['yeeey',False],['lol',False],['test',False],['hau',False]]
    CREDIT = 3
 
def save_data():
    global ID, MAP, PX, PY, TIME, DATE, WEATHER, CHAPTER, MORALITY, ATM, MONEY, CREDIT, BATTERY, GAS, GAMETIME, FORMATION, CHARACTERS, INVENTORY
 
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
    dt = dd + mm + yy + str(DATE[3])
 
    com.execute("""UPDATE data SET gt = :gt,fr = :fr,map = :map,x = :x,y = :y,time = :tm,date = :dt,weather = :weather,chapter = :chapter,morality = :morality,atm = :atm,money =:money,credit = :credit,battery = :battery,gas = :gas WHERE id = :id""",
    {'id': ID,'gt': GAMETIME,'fr': FORMATION,'map': MAP,'x': PX,'y': PY,'tm': ts,'dt': dt,'weather': WEATHER,'chapter': CHAPTER,'morality': MORALITY,'atm': ATM,'money': MONEY,'credit': CREDIT,'battery': BATTERY,'gas': GAS})
    tbl.commit()
 
    for i in range(len(CHARACTERS)):
        com.execute("""UPDATE characters""" + str(ID) + """ SET level = :level, xp = :xp WHERE n = :n""",{'n': i,'level': CHARACTERS[i]['LEVEL'],'xp': CHARACTERS[i]['XP']})
        tbl.commit()
    '''
    for n in range(len(INVENTORY)):
        com.execute("UPDATE inventory" + str(ID) + " SET it1 = :it1")'''
 
    com.close()
    tbl.close()
      
def save_sett():
    global ID, LANG, SFX, MSC, UP, DOWN, LEFT, RIGHT, ACT, RUN, PHONE, BAG, SPEED, COLOR, BORDER
      
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
      
    com.execute("UPDATE settings SET lang = :lang,sfx = :sfx,msc = :msc,up = :up,down = :down,left = :left,right = :right,act = :act,run = :run,phone = :phone,inventory = :inventory,\
        speed = :speed,color1 = :color1,color2 = :color2,color3 = :color3,border = :border WHERE id = :id",
        {'id': ID,'lang': LANG,'sfx': SFX,'msc': MSC,'up': UP,'down': DOWN,'left': LEFT,'right': RIGHT,'act': ACT,'run': RUN,'phone': PHONE,'inventory': BAG,
        'speed': SPEED,'color1': COLOR[0],'color2': COLOR[1],'color3': COLOR[2],'border': BORDER})
    tbl.commit()
      
    com.close()
    tbl.close()
 
def char_entry():
    global ID, CHARACTERS
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
      
    for i in range(len(CHARACTERS)):
        com.execute("UPDATE characters" + str(ID) + " SET name = :name, lastname = :lastname,gender = :gender,level = :level WHERE n = :n",
            {'n': i,'name': CHARACTERS[i]['NAME'],'lastname': CHARACTERS[i]['LASTNAME'],'gender': CHARACTERS[i]['GENDER'],'level': CHARACTERS[i]['LEVEL']})
        tbl.commit()
      
    com.close()
    tbl.close()
      
def party_make(p):
    global ID, PARTY
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
      
    trg = False
    com.execute("SELECT n FROM party" + str(ID))
    for i in com.fetchall():
        if i[0] == trg: trg = True

    if len(PARTY[p]) < 2: PARTY[p].append(0)
    if len(PARTY[p]) < 3: PARTY[p].append(0)
    if trg == False:
        com.execute("DELETE FROM party" + str(ID) + " WHERE n = " + str(p))
    com.execute("INSERT INTO party" + str(ID) + " VALUES(:n,:p1,:p2,:p3)",{'n': p,'p1': PARTY[p][0],'p2': PARTY[p][1],'p3': PARTY[p][2]})
    tbl.commit()
      
    com.close()
    tbl.close()
 
def call_save(c):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
 
    com.execute("INSERT INTO contacts" + str(ID) + " VALUES (:n)",{'n': c})
    tbl.commit()
 
    com.close()
    tbl.close()
 
def hist_save(n,w):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
 
    com.execute("INSERT INTO callhist" + str(ID) + " VALUES (:n,:w)",{'n': n,'w': w})
    tbl.commit()
 
    com.close()
    tbl.close()
 
def inbx_save(e,r):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
 
    com.execute("INSERT INTO inbox" + str(ID) + " VALUES (:n,:red)",{'n': e,'red': r})
    tbl.commit()
 
    com.close()
    tbl.close()
 
def task_save(t,d):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
 
    com.execute("INSERT INTO tasks" + str(ID) + " VALUES (:tsk,:don)",{'tsk': t,'don': d})
    tbl.commit()
 
    com.close()
    tbl.close()
 
def tact_save(t):
    global ID, TACTICAL
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
      
    trg = False
    com.execute("SELECT n FROM tactical" + str(ID))
    for i in com.fetchall():
        if i[0] == t: trg = True
    if trg == False:
        com.execute("DELETE FROM tactical" + str(ID) + " WHERE n = " + str(t))
    com.execute("INSERT INTO tactical" + str(ID) + " VALUES(:n,:p1,:p2,:p3,:p4)",{'n': t,'p1': TACTICAL[t][0],'p2': TACTICAL[t][1],'p3': TACTICAL[t][2],'p4': TACTICAL[t][3]})
    tbl.commit()
      
    com.close()
    tbl.close()
  
def best_regs(f):
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
 
    trg = False
    com.execute("SELECT idx FROM bestiary" + str(ID))
    for i in com.fetchall():
        print(i)
        if i[0] == f['N']: trg = True
    if trg == True:
        com.execute("DELETE FROM bestiary" + str(ID) + " WHERE idx = " + f['N'])
    com.execute("INSERT INTO bestiary" + str(ID) + " VALUES (:idx,:id,:date)",{'idx': f['N'],'id': f['ID'],'date': f['DATE']})
    tbl.commit()
      
    com.close()
    tbl.close()
  
def trophy(i):
    global ID, ACHIEVEMENTS
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
      
    com.execute("INSERT INTO achievements" + str(ID) + " VALUES(:idx,:got,:date)",{'idx': i,'got': ACHIEVEMENTS[i][2],'date': ACHIEVEMENTS[i][3]})
    tbl.commit()
      
    com.close()
    tbl.close()
      
def delete_data():
    global ID
    tbl = sqlite3.connect('userdata.db')
    com = tbl.cursor()
      
    com.execute("DELETE FROM settings WHERE id=" + str(ID))
    com.execute("DELETE FROM data WHERE id=" + str(ID))
    com.execute("DROP TABLE characters" + str(ID))
    com.execute("DROP TABLE party" + str(ID))
    com.execute("DROP TABLE contacts" + str(ID))
    com.execute("DROP TABLE callhist" + str(ID))
    com.execute("DROP TABLE inbox" + str(ID))
    com.execute("DROP TABLE tasks" + str(ID))
    com.execute("DROP TABLE tactical" + str(ID))
    com.execute("DROP TABLE bestiary" + str(ID))
    com.execute("DROP TABLE achievements" + str(ID))
    com.execute("DROP TABLE inventory" + str(ID))
    tbl.commit()
      
    com.close()
    tbl.close()
      
LANG = 'PT'
SFX = 0.8
MSC = 0.6
UP = pygame.K_w
DOWN = pygame.K_s
LEFT = pygame.K_a
RIGHT = pygame.K_d
ACT = pygame.K_g
RUN = pygame.K_h
PHONE = pygame.K_BACKSPACE
BAG = pygame.K_RETURN
SPEED = 2
COLOR = [255,10,10]
BORDER = 0
  
ID = 0
MAP = 0
PX = 0
PY = 0
TIME = [0,0,0]
DATE = [0,0,0,1]
WEATHER = 0
CHAPTER = 0
SCENE = 0
MORALITY = 0
 
SPRITES = {
'BLANKU_000': [],'BLANKDD_000': [],'BLANKD_000': [],'BLANKLD_000': [],'BLANKL_000': [],'BLANKLU_000': [],'BLANKRD_000': [],'BLANKR_000': [],'BLANKRU_000': [],
'BLANKU_001': [],'BLANKDD_001': [],'BLANKD_001': [],'BLANKLD_001': [],'BLANKL_001': [],'BLANKLU_001': [],'BLANKRD_001': [],'BLANKR_001': [],'BLANKRU_001': [],
'BLANKU_010': [],'BLANKDD_010': [],'BLANKD_010': [],'BLANKLD_010': [],'BLANKL_010': [],'BLANKLU_010': [],'BLANKRD_010': [],'BLANKR_010': [],'BLANKRU_010': [],
'BLANKU_011': [],'BLANKDD_011': [],'BLANKD_011': [],'BLANKLD_011': [],'BLANKL_011': [],'BLANKLU_011': [],'BLANKRD_011': [],'BLANKR_011': [],'BLANKRU_011': [],
'BLANKU_020': [],'BLANKDD_020': [],'BLANKD_020': [],'BLANKLD_020': [],'BLANKL_020': [],'BLANKLU_020': [],'BLANKRD_020': [],'BLANKR_020': [],'BLANKRU_020': [],
'BLANKU_021': [],'BLANKDD_021': [],'BLANKD_021': [],'BLANKLD_021': [],'BLANKL_021': [],'BLANKLU_021': [],'BLANKRD_021': [],'BLANKR_021': [],'BLANKRU_021': [],
'BLANKU_030': [],'BLANKDD_030': [],'BLANKD_030': [],'BLANKLD_030': [],'BLANKL_030': [],'BLANKLU_030': [],'BLANKRD_030': [],'BLANKR_030': [],'BLANKRU_030': [],
'BLANKU_031': [],'BLANKDD_031': [],'BLANKD_031': [],'BLANKLD_031': [],'BLANKL_031': [],'BLANKLU_031': [],'BLANKRD_031': [],'BLANKR_031': [],'BLANKRU_031': [],
'BLANKU_040': [],'BLANKDD_040': [],'BLANKD_040': [],'BLANKLD_040': [],'BLANKL_040': [],'BLANKLU_040': [],'BLANKRD_040': [],'BLANKR_040': [],'BLANKRU_040': [],
'BLANKU_041': [],'BLANKDD_041': [],'BLANKD_041': [],'BLANKLD_041': [],'BLANKL_041': [],'BLANKLU_041': [],'BLANKRD_041': [],'BLANKR_041': [],'BLANKRU_041': [],
'BLANKU_050': [],'BLANKDD_050': [],'BLANKD_050': [],'BLANKLD_050': [],'BLANKL_050': [],'BLANKLU_050': [],'BLANKRD_050': [],'BLANKR_050': [],'BLANKRU_050': [],
'BLANKU_051': [],'BLANKDD_051': [],'BLANKD_051': [],'BLANKLD_051': [],'BLANKL_051': [],'BLANKLU_051': [],'BLANKRD_051': [],'BLANKR_051': [],'BLANKRU_051': [],

'PHONE_000': [pygame.image.load('Sprites/body_000_phone.png')],'CALL_000': [pygame.image.load('Sprites/body_000_call.png')],
'STANDU_000': [],'STANDLU_000': [],'STANDL_000': [],'STANDLD_000': [],'STANDD_000': [],'STANDRD_000': [],'STANDR_000': [],'STANDRU_000': [],'JUMPU_000': [],'JUMPD_000': [],
'WALKU_000': [],'WALKLU_000': [],'WALKL_000': [],'WALKLD_000': [],'WALKD_000': [],'WALKRD_000': [],'WALKR_000': [],'WALKRU_000': [],
'RUNU_000': [],'RUNLU_000': [],'RUNL_000': [],'RUNLD_000': [],'RUND_000': [],'RUNRD_000': [],'RUNR_000': [],'RUNRU_000': [],

'PHONE_001': [pygame.image.load('Sprites/body_000_phone.png')],'CALL_001': [pygame.image.load('Sprites/body_000_call.png')],
'STANDU_001': [],'STANDLU_001': [],'STANDL_001': [],'STANDLD_001': [],'STANDD_001': [],'STANDRD_001': [],'STANDR_001': [],'STANDRU_001': [],'JUMPU_001': [],'JUMPD_001': [],
'WALKU_001': [],'WALKLU_001': [],'WALKL_001': [],'WALKLD_001': [],'WALKD_001': [],'WALKRD_001': [],'WALKR_001': [],'WALKRU_001': [],
'RUNU_001': [],'RUNLU_001': [],'RUNL_001': [],'RUNLD_001': [],'RUND_001': [],'RUNRD_001': [],'RUNR_001': [],'RUNRU_001': [],

'ATTACKIMATION_1': [], 'ATTACKIMATION_10': [],
'EFFECT_6': [], 'EFFECT_7': []}

#HEADS
for p in range(6):
    if p < 10: pt = '0' + str(p)
    else: pt = str(p)

    for g in range(2):
        if p not in [2,3,5]:
            SPRITES['BLANKU_' + str(pt) + str(g)].append(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_U.png'))
            for i in range(2): SPRITES['BLANKDD_' + str(pt) + str(g)].append(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_blankDD_' + str(i) + '.png'))
            for i in range(2): SPRITES['BLANKD_' + str(pt) + str(g)].append(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_blankD_' + str(i) + '.png'))
            for i in range(2): SPRITES['BLANKLD_' + str(pt) + str(g)].append(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_blankLD_' + str(i) + '.png'))
            for i in range(2): SPRITES['BLANKL_' + str(pt) + str(g)].append(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_blankH_' + str(i) + '.png'))
            SPRITES['BLANKLU_' + str(pt) + str(g)].append(pygame.transform.flip(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_HU.png'),True,False))
            for i in range(2): SPRITES['BLANKRD_' + str(pt) + str(g)].append(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_blankRD_' + str(i) + '.png'))
            for i in range(2): SPRITES['BLANKR_' + str(pt) + str(g)].append(pygame.transform.flip(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_blankH_' + str(i) + '.png'),True,False))
            SPRITES['BLANKRU_' + str(pt) + str(g)].append(pygame.transform.flip(pygame.image.load('Sprites/head_' + str(pt) + str(g) + '_HU.png'),True,False))
#BODIES
for w in range(1):
    for t in range(1):
        if t < 10: pt = '0' + str(t)
        else: pt = str(t)
        for i in range(4): SPRITES['STANDU_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standU_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDLU_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHU_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDL_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standH_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDLD_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHD_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDD_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standD_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDRU_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHU_' + str(i) + '.png'),True,False))
        for i in range(4): SPRITES['STANDR_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standH_' + str(i) + '.png'),True,False))
        for i in range(4): SPRITES['STANDRD_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHD_' + str(i) + '.png'),True,False))
        for i in range(2): SPRITES['JUMPU_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_jumpU_' + str(i) + '.png'))
        for i in range(2): SPRITES['JUMPD_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_jumpD_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKU_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkU_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKLU_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKL_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKLD_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKD_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkD_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKRU_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['WALKR_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['WALKRD_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['RUNU_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkU_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNLU_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNL_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNLD_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUND_' + str(pt) + str(w)].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkD_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNRU_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['RUNR_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['RUNRD_' + str(pt) + str(w)].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'),True,False))

        #TEMPORAAARIOOO
        for i in range(4): SPRITES['STANDU_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standU_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDLU_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHU_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDL_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standH_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDLD_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHD_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDD_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standD_' + str(i) + '.png'))
        for i in range(4): SPRITES['STANDRU_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHU_' + str(i) + '.png'),True,False))
        for i in range(4): SPRITES['STANDR_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standH_' + str(i) + '.png'),True,False))
        for i in range(4): SPRITES['STANDRD_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_standHD_' + str(i) + '.png'),True,False))
        for i in range(2): SPRITES['JUMPU_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_jumpU_' + str(i) + '.png'))
        for i in range(2): SPRITES['JUMPD_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_jumpD_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKU_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkU_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKLU_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKL_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKLD_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKD_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkD_' + str(i) + '.png'))
        for i in range(8): SPRITES['WALKRU_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['WALKR_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['WALKRD_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['RUNU_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkU_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNLU_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNL_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNLD_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUND_' + str(pt) + '1'].append(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkD_' + str(i) + '.png'))
        for i in range(8): SPRITES['RUNRU_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHU_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['RUNR_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkH_' + str(i) + '.png'),True,False))
        for i in range(8): SPRITES['RUNRD_' + str(pt) + '1'].append(pygame.transform.flip(pygame.image.load('Sprites/body_' + str(pt) + str(w) + '_walkHD_' + str(i) + '.png'),True,False))

for i in range(3): SPRITES['ATTACKIMATION_1'].append(pygame.image.load('Sprites/attackimation_1_' + str(i) + '.png'))
for i in range(3): SPRITES['ATTACKIMATION_10'].append(pygame.image.load('Sprites/attackimation_10_' + str(i) + '.png'))

for i in range(22): SPRITES['EFFECT_6'].append(pygame.image.load('Sprites/eff_6_' + str(i) + '.png'))
for i in range(11): SPRITES['EFFECT_7'].append(pygame.image.load('Sprites/eff_7_' + str(i) + '.png'))
 
pygame.mixer.init()
SOUND = {}
for j in os.listdir('SFX'): SOUND[j[:-4].upper()] = pygame.mixer.Sound('SFX/' + j)
 
SONGS = {
'FATE_OCCURRENCES': pygame.mixer.Sound('Music/fate_occurrences.ogg'),
#'BEYOND_THE_CLOUDS': pygame.mixer.Sound('Music/beyond_the_clouds.wav'), #'SIERRA_STREETS': pygame.mixer.Sound('Music/sierra_streets.wav'),
'HEY_SAM': pygame.mixer.Sound('Music/hey_sam.wav'), 'URBAN_PLAGUE': pygame.mixer.Sound('Music/urban_plague.wav'),
'CIGARUTO': pygame.mixer.Sound('Music/cigaruto.wav'),
'EMOS_HERMANOS': pygame.mixer.Sound('Music/emos_hermanos.wav'),
'ONCE_YOU_BECOME_FOREVER_YOU_ARE': pygame.mixer.Sound('Music/once_you_become_forever_you_are.wav'),
}

PALETTES = [
[(198,57,21),(250,250,250),(91,7,0),(153,33,33)]
]
     
CHARACTERS = [
{'NAME': 'Sidney','LASTNAME': 'Barreto','GENDER': 'male','ID': '0064','BLOOD': 'A+','CIVIL': 'solteiro','CLASS': 'gunslinger',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_coxinha','drink_whisky'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [10,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,22,22,25,25,26,28,30,30,32,33,35],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},
  
{'NAME': 'Jane', 'LASTNAME': 'Oliveira','GENDER': 'female','ID': '0094','BLOOD': 'O-','CIVIL': 'casada','CLASS': 'rifler',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_chesse_bread','food_coffee'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [1,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},
  
{'NAME': 'Renan', 'LASTNAME': 'Pinheiro','GENDER': 'male','ID': '0100','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'thief',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_cola','food_cake_carrot'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [2,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},
 
{'NAME': 'Diego', 'LASTNAME': 'Donovan','GENDER': 'male','ID': '0024','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'gunslinger',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_burguer','food_cola'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [10,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [2,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [40,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},
  
{'NAME': 'Bianca', 'LASTNAME': 'Pacheco','GENDER': 'female','ID': '0120','BLOOD': 'O+','CIVIL': 'casada','CLASS': 'doctor',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_sushi','food_juice_orange'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [10,12,12,15,15,16,18,20,20,22,23,25],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},
 
{'NAME': 'Lúcia', 'LASTNAME': 'Figueiredo','GENDER': 'female','ID': '0013','BLOOD': 'O+','CIVIL': 'viúva','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},

{'NAME': 'Maicon', 'LASTNAME': 'Neves','GENDER': 'male','ID': '0013','BLOOD': 'O+','CIVIL': 'solteiro','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},

{'NAME': 'Iago', 'LASTNAME': 'Dantas','GENDER': 'male','ID': '0013','BLOOD': 'O+','CIVIL': 'comprometido','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},

{'NAME': 'Vinicíus', 'LASTNAME': 'Tavares','GENDER': 'male','ID': '0013','BLOOD': 'O+','CIVIL': 'solteiro','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},

{'NAME': 'João', 'LASTNAME': 'Pedro Lima','GENDER': 'male','ID': '0013','BLOOD': 'O+','CIVIL': 'solteiro','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},

{'NAME': 'Sofia', 'LASTNAME': 'Torres','GENDER': 'female','ID': '0013','BLOOD': 'O+','CIVIL': 'casada','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},

{'NAME': 'Paulo', 'LASTNAME': 'Sousa','GENDER': 'male','ID': '0013','BLOOD': 'O+','CIVIL': 'casado','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0},

{'NAME': 'Pietra', 'LASTNAME': 'Amaral','GENDER': 'female','ID': '0013','BLOOD': 'O+','CIVIL': 'comprometida','CLASS': 'sniper',
'LEVEL': 0,'SKILL': 0,'HP': 0,'BARHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0, 'DMGTIM': 100, 'SHK': 0, 'COSTUME': '000', 'SKIN': '0',
'HUNGER': 720, 'THIRST': 360, 'SLEEP': 1000,
'FAVFOOD': ['food_juice_orange','food_fish'],
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],
'AGILITY': [0,0,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],
'RESISTANCE': [0,0,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3],
'VITALITY': [20,12,12,15,15,16,18,20,20,22,23,25],
'NEXTLEVEL': [100,150,200,300,300,350,450,500,600],
'CARISM': 0, 'INTIMIDATION': 0, 'STAMINA': 0, 'ATLETISM': 0, 'FURTIVITY': 0, 'CRAFTING': 0, 'FORCE': 0, 'MEDICINE': 0, 'IMUNITY': 0, 'COORDENATION': 0}
]

CHAPTERS = [
['Depois do começo', 'prólogo', 'Desde aquele dia, o mundo inteiro havia mudado,', 'Um fato concreto comprovava o que os antigos cientistas', 'e filósofos tentavam nos dizer há muito tempo,',
'pela primeira vez, ali na frente, uma entidade', 'sobrenatural mostrava sua face ao mundo.', '', 'Eles não conseguiriam guardar esse segredo por mais', 'de 100.000 anos, era inviável, ainda mais devido ao',
'surto dos seres que os chamam de anomalias.', '', 'Vários caçadores cumpriam a difícil tarefa de expurgar', 'a praga de anomalias assolando a serra da região', 'sudeste brasileira, esses eram os Mercenários.',
'Eles eram odiados pela população e marginalizados', 'pela sociedade, não tinham mais escolha na vida', 'a não ser arriscá-la. Foram heróis injustiçados e', 'vilões glorificados, tudo começou desde que',
'a polícia civil legalizou o porte de armas a quem', 'quisesse se tornar um Mercenário, embora nem mesmo', 'a própria população soubesse direito o que era isso,', 'Várias teorias da conspiração se espalharam, difamando',
'a incapacidade da polícia de segurar o aumento dos', 'casos de homicídio não registrados, muitos duvidam', 'que esses casos sejam reais, ou que as anomalias', 'realmente existam.', '',
'Tudo isso gira em torno de algo muito maior,', 'mas por agora, eu devo começar pelas histórias', 'que nos uniram nessa descoberta.', '', 'Eu vou contar a minha.'],
 
['Duplo Andantes', 'capítulo I', 'O que tem a dizer sobre essa garota?','','Pietra?','Você já sabia desse lado negro dela?','','Não...eu não fazia idéia...','Começaram a me contar a verdade depois',
'e aí começei a abrir os olhos','','Conhecia ' + CHARACTERS[4]['NAME'] + '?','','Não, a gente a encontrou por acaso...','e não sabia que ela estava','sendo procurada.',
'Você e ' + CHARACTERS[1]['NAME'] + ' já se conheciam?','','Não, nunca nos vimos antes.','','E Vinicius? Já o conhecia?','','Não...quer dizer, mais ou menos','Ele era um criminoso muito procurado pela polícia',
'então todos da cidade o conheciam.','',CHARACTERS[0]['NAME'] + ', sobre as anomalias, você sabia','o que eram?','','Não','','Sabia o real perigo que','elas representavam?','','...','','...','','...não',
'Acho que isso já é suficiente','','Obrigado senhor.','',CHARACTERS[4]['NAME'] + '?','','Sim?','','Pode me dizer com detalhes','o que houve na noite em que','foi abordada?','','Claro.'],
 
['Sangue Verde', 'capítulo II', 'Lamento muito o que houve com você, Dra. ' + CHARACTERS[4]['NAME'] + '.','','Obrigado...','','Você também não entendia com o que estava','mexendo, certo?','',
'Não no momento, com as pesquisas eu consegui','extrair informações importantes das amostras','mas nada que realmente fosse uma descoberta.','','Se permitir, quero que minha equipe forense colete',
'as amostras.','','Ah...não tem problema não...pode pegar.','','Também não conhecia nenhum dos criminosos?','','Não...eu não sou dessa região...','Achava que a serra era um lugar bem tranquilo...',
'Mas parece que existe violência em todo lugar','','Para quê você veio para','Campos do Jordão?','','Vim pesquisar as anomalias','','Eu também, eu vim pelo mesmo motivo','',
'Agora não, ' + CHARACTERS[4]['NAME'] + '.','','Quero que me conte os detalhes da pesquisa mais tarde','','Sim, Sr. Dalibor.','','Seu nome é...','',CHARACTERS[1]['NAME'] + '.','',
'Isso, me conte sua versão dos fatos.'],
 
['Não se meta com a gangue', 'capítulo III'],
 
['Pelo Benefício do Mr. Kite!', 'capítulo IV', ''],
 
['O Passado te Condena', 'capítulo V', ''],

['', 'capítulo VI', ''],
 
['Temporada de caça', 'capítulo VII', ''],
 
['O Crime Não Compensa', 'capítulo VIII', ''],

['Milícia x Meliante', 'capítulo IX', ''],
 
['Não Identificado', 'capítulo X', ''],
 
['Dr. Estanho', 'capítulo XI', ''],
 
['A Verdade Liberta', 'capítulo XII', ''],
 
['Afasta de mim esse Cálice', 'epílogo', '']
]
    
PARTY = [[0,4,3]]
FORMATION = 0
     
ATM = 0
MONEY = 0
CREDIT = 10
BATTERY = 360
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
spirit
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

0 - faz nada
1 - atacar
2 - abaixar ATAQUE
3 - abaixar AGILIDADE
4 - abaixar FORÇA
5 - abaixar RESISTÊNCIA
6 - condição
7 - chamar anomalia
8 - roubar
9 - fugir
10 - charge
 
0 - normal
1 - de costas
2 - repelente (anomalias não o atacam)
3 - fedor (não consegue batalhar)
4 - resfriado (não pode comer)
5 - febre (perde HP no calor)
6 - fome (perde HP por não comer)
7 - sede (perde HP por não beber)
8 - sono (erra fácil)
9 - náusea (erra facilmente)
10 - enjoo (não pode comer)
11 - fraqueza (ataques mais fracos)
12 - cegueira (perde o turno)
13 - preso (perde o turno)
14 - paralisia (perde o turno e não sai sozinho)
15 - inconsciente (não necessariamente sem HP)
16 - parasita (suga o HP)
17 - queimadura (perde HP, mas some)
18 - veneno aracnídeo (perde HP)
19 - veneno antiofídico (perde HP)
20 - veneno escorpiônico (perde HP)
21 - hemorragia (perde HP e não tem cura)
'''
      
FREAKS = {
#ANOMALIES
'ancap': {'NAME': 'Anarcocapitalista','INFO': ['Vamos mesmo tirar sarro de uma ideologia','política utópica? Sim, vamos.'],'HEIGHT': '0,50','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 3,'HP': 12,'RESISTANCE': 0,'PATH': 'stay','HABILITIES': [['Diálogo',['O elemento tenta lhe convencer.'],-5,1,40,1]],'BLOOD': 10,'ITEM': None,'SONG': 'UNBELIEVEBLE_PEOPLE'},

'madladcat': {'NAME': 'Gato Atacado','INFO': ['É um felino sobrenatural que','flutua como um fantasma.','Pequeno e ágil, porém bem frágil.'],'HEIGHT': '0,80','HABITAT': 'jungle','TYPE': 'mammal',
'AGILITY': 5,'HP': 8,'RESISTANCE': 1,'PATH': 'stealth','HABILITIES': [['Morder',['O felino morde o oponente.'],-5,1,40,1],['Arranhar',['O felino usa suas garras,','para atacar o oponente.'],-3,10,40,10],
['Ronronar',['O felino ronrona, mostrando','seu desprezo pela situação.'],0,9,10,1],['Miar',['O felino mia para o além,','chamando outros felinos.'],['madladcat'],7,10,1]],'BLOOD': 10,'ITEM': None,'SONG': 'HEY_SAM'},
   
'lizardshrimp': {'NAME': 'Camaraleão','INFO': ['É um réptil que se fundiu com','um camarão, não se sabe se é um alimento apetitoso.'],'HEIGHT': '0,23','HABITAT': 'jungle','TYPE': 'reptile',
'AGILITY': 4,'HP': 6,'RESISTANCE': 0,'PATH': 'stay','HABILITIES': [['Camuflar',['O réptil se camufla no ambiente,','aumentando sua AGILIDADE.'],2,3],['Língua',['O réptil usa sua língua como','chicote para atacar o oponente.'],-3,1],
['Estalo',['O réptil se estala, criando','um campo de força elétrico.'],-13,1]],'BLOOD': 10,'ITEM': ['camarão',50]},
   
'peacockpigeon': {'NAME': 'Pombo Pavão','INFO': ['Um pombo urbano com uma mutação que o fez desenvolver penas de pavão com olhos reais nas suas pontas. Relativamente ágil, mas fraco.'],'HEIGHT': '0,25','HABITAT': 'urban','TYPE': 'mercenary',
'AGILITY': 3,'HP': 10,'RESISTANCE': 1,'PATH': 'horizontal','HABILITIES': [['Defecar',['A ave defeca no oponente, infectando-o.'],5,6,20,1],['Hipnose',['A ave hipnotiza o oponente com os olhos das penas de pavão, diminuindo sua AGILIDADE.'],-2,3,20,1],
['Bicar',['A ave bica o oponente.'],-4,1,50,1],['Gritar',['A ave grita, com a possibilidade de outra anomalia entrar na batalha.'],['madladcat','peacockpigeon'],7,10,1]],'BLOOD': 20,'ITEM': ['food_peanut_candy',30],'SONG': 'URBAN_PLAGUE'},
     
'crodile': {'NAME': 'Jaré','INFO': ['Um réptil que, graças á uma sílaba a menos em seu nome, perdeu dois de seus membros. Não muito ágil, mas causa muito dano.'],'HEIGHT': '1,90','HABITAT': 'swamp','TYPE': 'reptile',
'AGILITY': 2,'HP': 13,'RESISTANCE': 1,'PATH': 'stay','HABILITIES': [['Morder',['O réptil morde seu oponente'],-6,1],['Esperar',['O réptil aumenta seu ATAQUE.'],1,2],['Bote',['O réptil ataca com uma mordida em avanço.'],-5,1],
['Esconder',['O réptil se esconde no ambiente, aumentando sua AGILIDADE.'],1,3]],'BLOOD': 1},
 
'wingedcan': {'NAME': 'Lata Alada','INFO': ['Uma lata de energético que tenta ser irada e tem o único atributo que prometeu dar á quem o consumisse. É literalmente uma piada.'],'HEIGHT': '0,15','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 10,'HP': 5,'RESISTANCE': 1,'PATH': 'stay','HABILITIES': [['Voar',['Aumenta sua agilidade'],1,3],['Energizar',['Aumenta seu dano de arremesso'],2,2],['Ressaca',['A lata se auto destrói'],0,1],
['Arremessar',['A lata se joga no oponente, se machucando junto.'],-1,1]]},
    
'bunchofeyes': {'NAME': 'Cacho de Olhos','INFO': ['Vários olhos diferentes agrupados que possuem poderes hipnóticos. PS: NÃO É GUARANÁ, NÃO FAÇA SUCO.'],'HEIGHT': '0,30','HABITAT': 'jungle','TYPE': 'plant',
'AGILITY': 2,'HP': 20,'RESISTANCE': 1,'PATH': 'stay','HABILITIES':[['Encarar',['Os olhos começam a encarar o oponente, amedrontando-o e fazendo seu ATAQUE abaixar.'],-1,2],['Atirar',['Um dos olhos se lança no oponente.'],-3,1],
['Plantar',['Um olho se planta no chão com a possibilidade de germinar um novo cacho.'],0,7],['Explodir',['Todos os olhos se soltam num ataque fulminante.'],-7,1]]},
     
'bodybuilderfrog': {'NAME': 'Perereca Mil Grau','INFO': ['Um anfíbio que saiu da metamorfose antes da hora e ao mesmo tempo que manteve a cauda, desenvolveu braços fortes.'],'HEIGHT': '0,70','HABITAT': 'jungle','TYPE': 'aquatic',
'AGILITY': 2,'HP': 20,'RESISTANCE': 1,'PATH': 'follow','HABILITIES':[['Língua',['O anfíbio usa sua língua para chicotear o oponente.'],-5,1],['Porrada',['O anfíbio usa seus braços musculosos para bater no oponente.'],-8,1],
['Veneno',['O anfíbio libera toxinas nas bolsas das suas costas para infectar o oponente.'],1,4],['Salto',['O anfíbio pula pelo ambiente e aumenta sua AGILIDADE.'],2,3]]},
     
'hotman': {'NAME': 'Cremado Cremoso','INFO': ['Um homem que sofreu uma combustão espontânea mas continua vivo graças á mutação.'],'HEIGHT': '1,70','HABITAT': 'urban','TYPE': 'humanoid',
'AGILITY': 5,'HP': 18,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Bater',['O indivíduo bate no oponente.'],-5,1],['Cinzas',['O indivíduo joga cinzas no oponente, abaixando sua AGILIDADE.'],-3,3],
['Dançar',['O indivíduo começa a rebolar e mostrar seu charme.'],0,8],['Infectar',['O indivíduo entra dentro do oponente através das cinzas, diminuindo seu ATAQUE.'],-3,2]]},
   
'spontaneouscombustion': {'NAME': 'Combustão Espontânea','INFO': ['Uma homem normal que teve o azar','de ter essa anomalia, e agora','vive como uma tocha humana.'],'HEIGHT': '1,70','HABITAT': 'urban','TYPE': 'humanoid',
'AGILITY': 5,'HP': 30,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': [['Bater',['O indivíduo bate no oponente.'],-8,1],['Labareda',['O indivíduo sopra uma labareda no','oponente, fazendo ele se queimar.'],3,4],
['Queimadura',['O indivíduo se ilumina tanto que','o oponente perde a visão.'],9,6],['Bolas de Fogo',['O indivíduo arremessa bolas','de fogo que vão te atolar.'],-14,1]]},
     
'crucifiedbiscuit': {'NAME': 'Biscoito Crucificado','INFO': ['Esse ser humano não está em um estado muito bacana...É um biscoito de gengibre possuído preso num crucifixo, parece até coisa de algum filme B!'],'HEIGHT': '0,30','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 8,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Chantily','O possuído jorra chantily venenoso no oponente.',1,4],['Gargalhar','O possuído ri de uma maneira terrorífica, diminuindo o ATAQUE do oponente.',-2,2],
['Bater','O possuído usa seu crucifixo para atacar o oponente.',-8,1],['Perfurar','O possuído perfura o corpo do oponente usando o crucifixo',-10,1]]},
  
'ppap': {'NAME': 'Caneta Azul', 'INFO': ['É um objeto possuído por um fantasma','e agora tem o poder de atormentar as pessoas','com uma música irritante.'],'HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 8,'HP': 15,'RESISTANCE': 0,'PATH': 'follow','HABILITIES': [['Rabiscar',['O elemento se move contra o oponente','e o rabisca o rosto.'],-8,1],['Cantar',['O elemento atormenta o oponente','através de uma canção pertubadora.'],6,4],
['Explodir',['O elemento se estoura, espalhando','tinta na cara do oponente.'],-20,1]],'SONG': 'ppap'},
  
'armedcrab': {'NAME': 'Carangueijo Armado','INFO': ['Um carangueijo que aprendeu a','utilizar uma arma branca.'],'HEIGHT': '0,18','HABITAT': 'urban','TYPE': 'rough',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'emohipster': {'NAME': 'Emo Hipster','INFO': ['A DDA ainda não sabe se esse ser é uma anomalia ou apenas um cara estranho que chegou e parece não achar lugar no corpo que Deus encarnou.'],'HEIGHT': '1,60','HABITAT': 'urban','TYPE': 'humanoid',
'AGILITY': 4,'HP': 20,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Cantar',['O esquisito começa a cantar uma música dos los hermanos com uma guitarra.'],1,4],['Guitarrada',['O esquisito usa sua guitarra para atacar o oponente.'],-10,1],
['Óculos sem lente',['O esquisito põe óculos sem lente para confundir o oponente, abaixando sua AGILIDADE.'],-1,3],['Franja',['O esquisito balança sua franja, aumentando seu ATAQUE.'],2,2]],'SONG': 'EMOS_HERMANOS'},
   
'crush': {'NAME': 'Crush','INFO': ['Não conseguimos coletar muitos','dados dessa anomalia, só sabemos','que é a mais forte nunca derrotada.'],'HEIGHT': '1,60','HABITAT': 'urban','TYPE': 'humanoid',
'AGILITY': 99,'HP': 9999999,'RESISTANCE': 99,'PATH': 'follow','HABILITIES': [['Iludir',['A anomalia usa as palavras','como lanças e ataca o','coração do oponente.'],-99999,1]]},
     
'prettyfish': {'NAME': 'Peixe Galã','INFO': ['Um peixe que abre a boca acima dos limites de sua mandíbula e da biologia, pelo menos ele é admirável.'],'HEIGHT': '1,20','HABITAT': 'swamp','TYPE': 'aquatic',
'AGILITY': 5,'HP': 25,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Aumentar','O peixe aumenta o tamanho da sua face e volta ao normal, assustando o oponente e abaixando seu ATAQUE',-2,2],
['Saltar','O peixe salta na água e chicoteia o oponente com sua cauda',-7,1],['Morder','O peixe morde o oponente com seus dentes limpos e branquinhos.',-9,1],
['Brilhar','O peixe reflete a luz do sol cegando o oponente.',2,4]]},
     
'humanfeet': {'NAME': 'Pé de moleque','INFO': ['É um doce de amendoim delicioso muito comum em festas juninas...não pera. É um membro que se separou do corpo humano e agora consegue viver por conta própria, não confundir com mãozinha da Família Adams.'],'HEIGHT': '0,80','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 5,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Pisar','O membro pisa no oponente com toda sua força.',-10,1],['Chutar','O membro chuta o oponente, mesmo perdendo seu equilíbrio.',-12,1],
['Cura','O membro se cura utilizando uma técnica que não entendemos devido ás limitações de seu corpo.',10,1],['Agachar','O membro concentra a energia dos seus pés e aumenta seu ATAQUE.',5,2]]},
     
'flamencoflamingo': {'NAME': 'Flamingo Flamenguista','INFO': ['Uma ave com a peculiaridade de ter a anomalia FLAMENGO.'],'HEIGHT': '1,20','HABITAT': 'mangue','TYPE': 'flying',
'AGILITY': 7,'HP': 33,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Bolada','A ave chuta uma bola na face do oponente.',-13,1],['Dibre','Lamentamos o erro de ortografia de Sidney, a ave dribla o oponente fazendo sua AGILIDADE aumentar.',3,2],
['Rasteira','A ave ataca o oponente se jogando no chão e derrubando-o.',-10,1],['Gabigol','A ave recruta o profissional jogador de futebol GABIGOL, ganhando a batalha imediatamente.',-50,1]],'SONG': 'ONCE_YOU_BECOME_FOREVER_YOU_ARE'},
  
'cattlefish': {'NAME': 'Peixe Gado','INFO': ['Um búfalo que nadou tanto','que ganhou uma cauda de sereia.','Seria um tipo de Hipocampo?'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'aquatic',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'spidermangue': {'NAME': 'Mangue Aranha','INFO': ['Uma árvore peculiar que possui','pernas no lugar de raízes.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'plant',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'crabman': {'NAME': 'Homem Carangueijo','INFO': ['Um carangueijo gigante que lembra','uma música do Chico Science.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'rough',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
     
'belledoplhine': {'NAME': 'Belle Dolphine','INFO': ['Fruto de uma relação entre uma E-Girl e o Boto.'],'HEIGHT': '2,10','HABITAT': 'jungle','TYPE': 'aquatic',
'AGILITY': 7,'HP': 42,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Ahegao','O mamífero tenta sensualizar o oponente simulando um ato sexual, mas faz o efeito contrário abaixando seu ATAQUE',-3,2],['Água de banho','O mamífero oferece água de banho para o oponente, este o ingere e obtém HERPES.',2,4],
['Nadar','O mamífero nada no ambiente para recuperar sua VITALIDADE.',10,1],['Canto submarino','O mamífero entoa uma canção para chamar uma anomalia para a batalha.',1,5]]},
   
'teresacristinabust': {'NAME': 'Busto de Teresa Cristina','INFO': ['Um busto muito pesado e cheio,','de ódio no seu coração.'],'HEIGHT': '0,80','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 5,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Atacar',['O elemento se joga contra o oponente.'],-10,1],['Esmagar',['O elemento cai em cima','da cabeça do oponente.'],-20,1],['Voar',['O elemento voa ao derredor','do oponente'],0,8]]},
   
'tarsila': {'NAME': 'Tarsila','INFO': ['Um auto retrato da pintora Tarsila do Amaral, te encarando pronta pra acabar com sua raça.','Óleo sobre tela.'],'HEIGHT': '2,20','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 5,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Atacar','A pintura se joga contra o oponente, machucando a si no processo.',-10,1]]},
  
'hipocampus': {'NAME': 'Hipocampo','INFO': ['Um Hipocampo com o','formato de um hipocampo.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'aquatic',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'greenchicken': {'NAME': 'Galinha Verde','INFO': ['Uma ave com a terrível','anomalia INTEGRALISMO.'],'HEIGHT': '2,30','HABITAT': 'urban','TYPE': 'flying',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'captaincatfish': {'NAME': 'Cabeça de Bagre!!','INFO': ['Um homem com cabeça de bagre','e com péssima compreensão de ritmo.'],'HEIGHT': '2,30','HABITAT': 'urban','TYPE': 'humanoid',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'primateman': {'NAME': 'Homem Primata','INFO': ['Um humano que sabe','dançar muito bem.'],'HEIGHT': '2,30','HABITAT': 'mangue','TYPE': 'rough',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'drynwetman': {'NAME': 'Homem Seco e Molhado','INFO': ['Um homem que possui a anomalia de','estar seco e molhado ao mesmo tempo.'],'HEIGHT': '2,30','HABITAT': 'urban','TYPE': 'humanoid',
'AGILITY': 5,'HP': 50,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': []},
  
'mayanman': {'NAME': 'Tim Maia','INFO': ['Um mesoamericano com ótima.','afinação vocal.'],'HEIGHT': '1,80','HABITAT': 'jungle','TYPE': 'humanoid',
'AGILITY': 5,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': []},
  
'elkeys': {'NAME': 'Chaves','INFO': ['Um molho de chaves','que ninguém tem paciência.'],'HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'inorganic',
'AGILITY': 5,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': []},
 
'dorime': {'NAME': 'Dorime','INFO': ['Um ratinho santo que','e divino.'],'HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'mammal',
'AGILITY': 5,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': []},
  
'mecanicmonkey': {'NAME': 'Macaco','INFO': ['Um macaco mecânico portando','um macaco.'],'HEIGHT': '1,80','HABITAT': 'jungle','TYPE': 'mammal',
'AGILITY': 5,'HP': 30,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': []},
     
#CHEFES
'araraucaria': {'NAME': 'Araraucária','INFO': ['Uma árvore animal que possui penas coloridas no lugar de folhas.'],'HEIGHT': '10,2','HABITAT': 'jungle','TYPE':'boss',
'AGILITY': 3,'HP': 60,'RESISTANCE': 3,'PATH': 'follow','HABILITIES': [['Algazarra',['Barulhos estranhos saem das folhas do vegetal, diminuindo o ATAQUE do oponente.'],-1,2],['Fruta',['O vegetal deixa cair uma fruta de um dos galhos.'],-6,1],['Regeneração',['O vegetal drena recursos de suas raízes e recupera 10 HP.'],10,1]]},
    
'torpedosquid': {'NAME': 'Lula Torpedo','INFO': ['Um molusco que antige seus oponentes como um torpedo. Apesar de enorme, forte e resistente, se locomove muito devagar.'],'HEIGHT': '2,10','HABITAT': 'sea','TYPE': 'boss',
'AGILITY': 1,'HP': 50,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Tentáculos','O molusco usa seus tentáculos para atacar seu oponente.',-5,1],['Jato de tinta','O molusco atira um jato de tinta que impossibilita o oponente de atacar.',-5,3],
['Camuflagem','O molusco se disfarça no ambiente, aumentando sua AGILIDADE.',2,3],['Torpedo','O molusco acerta o oponente com um ataque explosivo que acerta todos á volta, super efetivo.',-15,1]]},
 
'giantear': {'NAME': 'Orelhão','INFO': ['Um fungo que realmente existe,','e quis trabalhar pra telefônica.'],'HEIGHT': '1,30','HABITAT': 'urban','TYPE': 'boss',
'AGILITY': 3,'HP': 25,'RESISTANCE': 0,'PATH': 'follow','HABILITIES': [['Soar',['O elemento vibra seus tímpanos,','abaixando a RESISTÊNCIA do oponente.'],-5,4],['Fichas',['O elemento arremessa fichas','do seu cofrinho.'],-10,1],
['Trote',['O elemento te passa um trote,','enganando o oponente e abaixando','sua FORÇA'],1,6],['Ligação',['O elemento faz uma ligação,','chamando outra anomalia.'],2,6]]},
 
'abaporu': {'NAME': 'Abaporu','INFO': ['Uma pintura modernista que criou vida própria e por sinal é canibal.'],'HEIGHT': '2,20','HABITAT': 'urban','TYPE': 'boss',
'AGILITY': 7,'HP': 75,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Pisar','A pintura pisa no oponente esmagando-o.',-13,1],['Fúria','A pintura grita furiosamente aumentando seu ATAQUE.',3,2],
['Proteger','A pintura reforça sua proteção de acrílico sobre a tela',1,6],['Reforço','A pintura chama outra pintura para ajudar na batalha.',1,5]]},
 
'cigaruto': {'NAME': 'Xaruto','INFO': ['Estranhamente lembra um personagem de um anime que não é tão bom quanto Evangelion.'],'HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'boss',
'AGILITY': 20,'HP': 20,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Fumaça ninja','O elemento solta uma fumaça com mais de 100.000 substâncias tóxicas incluindo nicotina e enxofre, envenenando o oponente.',-3,1],['Chama ninja','O elemento sopra uma labareda ardente, incendiando o oponente.',-2,1],
['Xaringan','O elemento usa uma espécime de energia oculta para aumentar seu ATAQUE.',-3,1],['Vaporizar','O elemento se transforma num cigarro eletrônico, relaxando e diminuindo sua AGILIDADE.',-3,1]],'BLOOD': 100,'ITEM': None,'SONG': 'CIGARUTO'},
 
'caesarean': {'NAME': 'Cesariana','INFO': ['Um feto dentro de uma bolha numa cesariana com poderes psíquicos.'],'HEIGHT': '1,00','HABITAT': 'urban','TYPE': 'boss',
'AGILITY': 2,'HP': 10,'RESISTANCE': 1,'PATH': 'follow','HABILITIES': [['Escudo','O feto reforça a resistência da bolha.',1,6],['Cordão Umbilical','O feto drena a energia de sua hospedeira e recupera sua VITALIDADE.',10,1],
['Grito molecular','O feto grita em um nível estratosféricamente alto, agitando as moléculas de seus oponentes.',-15,1],['Líquido Uterino','O feto arremesa o líquido uterino da bolha nos oponentes, confundindo-os e dando NÁUSEA.',2,4]]},
 
#MERCENARIES
'thuga': {'NAME': 'Bandido A','HABITAT': 'urban','TYPE': 'mercenary','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'PATH': 'stay','HABILITIES': [['Atirar','',-8,1,90],['Granada','',-20,1,10]]},

'vinicius': {'NAME': 'Vinícius','HABITAT': 'urban','TYPE': 'mercenary','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'PATH': 'stay','HABILITIES': [['Atirar','',-8,1,90],['Granada','',-20,1,10]]},

'pietra': {'NAME': 'Pietra','HABITAT': 'urban','TYPE': 'mercenary','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'PATH': 'stay','HABILITIES': [['Atirar','',-8,1,90],['Granada','',-20,1,10]]},

'thirdchar': {'NAME': CHARACTERS[2]['NAME'],'HABITAT': 'urban','TYPE': 'mercenary','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'PATH': 'stay','HABILITIES': [['Atirar','',-8,1,90],['Granada','',-20,1,10]]},
 
#OTHER
'target': {'NAME': 'Alvo','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'PATH': 'stay','HABILITIES': [['Fazer nada',0,6]]},
 
}
 
ARMY = [[],[],[],[],[]]
for i in range(40): ARMY[0].append('madladcat')
 
BESTIARY = []
  
TACTICAL = [[1,6],[2,7]]
     
ITEMS = {
#BAGS
'bag1': ['bolsinha',['Guarde seus itens nele e leve para qualquer lugar.','Volume: 5 - Peso: 5'],1000,5,5],
'bag2': ['bolsa',['Guarde seus itens nele e leve para qualquer lugar.','Volume: 10 - Peso: 10'],2500,10,10],
'bag3': ['mochila',['Guarde seus itens nele e leve para qualquer lugar.','Volume: 20 - Peso: 15'],5000,20,15],
'bag4': ['mochila de viagem',['Guarde seus itens nele e leve para qualquer lugar.','Volume: 30 - Peso: 20'],7500,30,20],
'bag5': ['mochilão',['Guarde seus itens nele e leve para qualquer lugar.','Volume: 30 - Peso: 25'],10000,30,25],
'bottle100': ['frasco de sulfúrio 100ml',['Feita especialmente para guardar sangue verde.','Capacidade de 10 inimigos'],200,1,1],
'bottle250': ['garrafa de sulfúrio 250ml',['Feita especialmente para guardar sangue verde.','Capacidade de 25 inimigos'],200,1,1],
'wallet': ['carteira',['Use para guardar seu dinheiro e coisas pequenos,','JAMAIS PERCA ISSO'],50,1,1],
   
#CUSTOM CLOTHES
'head_hairclip': ['xuxinha',['Pra amarrar o cabelo.'],30,1,1,3],
'head_glasses': ['óculos de grau',['Apenas pra quem precisa, senão você','ganha cegueira.'],30,2,1,1],
'head_sunglasses': ['óculos escuros',['Pra proteger do sol.'],30,2,1,2],
'head_cap': ['boné',['Pra proteger do sol e ficar estiloso.'],30,2,1,2],

'clth_shirt1': ['camisa preta',['O traje predileto dos solitários.'],30,4,1,'01'],
'clth_shirt2': ['camisa laranja',['Roupa casual.'],30,4,1,'02'],
'clth_shirt3': ['camisa vermelha',['Roupa casual.'],30,4,1,'03'],

'clth_jacket1': ['jaqueta preta',['Pra dar uma de Ramones.'],30,4,1,'1'],
'clth_jacket2': ['jaqueta verde quadriculada',['A peça de roupa favorita do ' + CHARACTERS[0]['NAME'] + '.'],30,4,1,'2'],
'clth_jacket3': ['jaqueta vermelha qudriculada',['Conhece o Iberê? então.'],30,4,1,'3'],
'clth_jacket4': ['moletom cinza',['Pra aqueles que não tem paciêcia','pra escolher roupa.'],30,4,1,'4'],
'clth_jacket5': ['moletom azul',['Pra aqueles que não tem paciêcia','pra escolher roupa.'],30,4,1,'5'],
'clth_jacket6': ['avental',['Para pesquisadores.'],30,4,1,'6'],

#VESTS
'vest1': ['colete amarelo',['Cuidado pra não pensarem que','é um francês manifestante.'],30,3,1,1,10],
'vest2': ['colete salva-vidas',['Mesmo sem água por perto, protege bastante.'],60,2,1,3,15],
'vest3': ['colete I',['Reduz o dano do advesário','DEFESA: 5 DURAÇÃO: 25'],120,3,1,5,20],
'vest4': ['colete IIA',['Reduz o dano do advesário','DEFESA: 8 DURAÇÃO: 25'],240,3,1,8,25],
'vest5': ['colete II',['Reduz o dano do advesário','DEFESA: 10 DURAÇÃO: 30'],360,3,1,10,30],
'vest6': ['colete IIIA',['Reduz o dano do advesário','DEFESA: 12 DURAÇÃO: 35'],480,3,1,12,35],
'vest7': ['colete III',['Restrito apenas para','policiais de elite.'],600,3,1,16,40],
'vest8': ['colete IV',['Restrito apenas para','policiais de elite.'],720,3,1,20,45],
 
#CHARMS
'amulet1': ['cruz',['Conçede proteção e espanta espíritos.'],20,1,1,5,50],
'amulet2': ['ankh',['Conçede proteção e espanta espíritos.'],20,1,1,10,50],
'amulet3': ['hamsá',['Conçede força e proteção.'],20,1,1,15,50],
'amulet4': ['pentáculo',['Conçede força, proteção e vitalidade.'],20,1,1,20,50],
'amulet5': ['tríscele',['Conçede força, proteção e vitalidade'],20,1,1,25,50],
'amulet6': ['ouroboros',['Conçede força, proteção,','vitalidade e resistência.'],20,1,1,25,50],
'amulet7': ['muiraquitã',['Conçede aumento em todos os atributos.'],20,1,1,25,50],
 
#AMMO
'ammo_tranquiizer': ['tranquilizante',['Munição para pistola que faz','o inimigo adormecer.'],100,2,1,0],
'ammo.12': ['munição.12',[''],200,2,1,12],
'ammo.16': ['munição.16',[''],200,2,1,16],
'ammo.22': ['munição.22',[''],200,2,1,22],
'ammo.32': ['munição.32',[''],200,2,1,32],
'ammo.38': ['munição.38',[''],300,2,1,38],
'ammo.42': ['munição.42',[''],400,2,1,42],
'ammo.44': ['munição.44',[''],200,2,1,44],
'ammo.45': ['munição.45',[''],200,2,1,45],
'ammo.38mm': ['munição 0.38mm',[''],200,2,1,380],
'ammo.5.56mm': ['munição 5.56mm',[''],200,2,1,556],
'ammo_missile': ['míssel',[''],800,5,4,1000],
 
#TOOLS
'tool_crowbar': ['pé de cabra',['Use para abrir portas trancadas.'],50,4,3,{'DAMAGE': 5, 'UNLOCK': 'door'}],
'tool_axe': ['machado',['Use para quebrar madeira.'],50,4,4,{'DAMAGE': 5, 'UNLOCK': 'wood'}],
'tool_hammer': ['marreta',['Use para quebrar vidro.'],50,4,5,{'DAMAGE': 5, 'UNLOCK': 'stone'}],
'tool_shovel': ['pá',['Use para cavar o solo para encontrar itens e abrir passagens.'],50,5,3,{'DAMAGE': 5, 'UNLOCK': 'grass'}],
'tool_chainsaw': ['motoserra',['Use para cortar árvores grandes','e de quebra bancar o Jason.'],50,6,3,{'DAMAGE': 5, 'UNLOCK': 'wood'}],
'tool_lighter': ['isqueiro',['Use para acender bombas','e talvez cigarros, mas não se recomenda.'],6,1,1],
'magnifying_glass': ['lupa',['Use para pesquisar anomalias e registrá-las no Bestiário.'],2,1,1],
'radar': ['radar',['Use para detectar anomalias no mapa.'],300,2,1],
'handcuffs': ['algemas',['Use para capturar anomalias e levá-las para pesquisa.'],50,2,1],
'umbrella': ['guarda-chuva',['Não pegue resfriado meu filho!'],800,5,1],'umbrella_portable': ['guarda-chuva portátil',['Não pegue resfriado meu filho!','Cabe na mochila!'],800,3,1],
   
#MELEE WEAPONS
'melee_broom': ['vassoura',['Não foi feita para se armar, muito menos','para caçar ou voar, mas funciona.',10,5,2,{'DAMAGE': 2}]],
'melee_frying_pan': ['frigideira',['Se não tiver o que usar, ela quebra um galho','e ainda frita um ovo legal.',30,3,2,{'DAMAGE': 4}]],
'melee_bottle': ['garrafa de vidro',['Depois de um drink moderado','é excelente para tacar na cabeça de um nazi.'],10,3,3,{'DAMAGE': 6}],
'melee_bar': ['barra de ferro',['Dá na telha pra descer','o cacete em alguém.'],4,3,3,{'DAMAGE': 8}],
'melee_knife': ['faca',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],300,2,1,{'DAMAGE': 10}],
'melee_fishmonger': ['peixeira',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],500,4,3,{'DAMAGE': 13}],
'melee_cleaver': ['cutelo',['Foi feita para cortar ossos de carnes, mas','serve como uma boa arma também.'],700,3,2,{'DAMAGE': 16}],
'melee_katana': ['katana',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],1000,4,3,{'DAMAGE': 18}],
'melee_whip': ['chicote',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],500,3,3,{'DAMAGE': 14}],
'melee_taser': ['taser',['Porque um verdadeiro meliante','não mata, causa dor.'],1500,1,3,{'DAMAGE': 8}],

#WEAPONS
'gun_revolver.22': ['revólver.22',['Arma de fogo para ataques de curta distância, ela usa munição de','calibre 16.'],2000,3,2,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
'gun_revolver.32': ['revólver.32',['Arma de fogo para ataques de curta distância, ela usa munição de','calibre 16.'],2000,3,2,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
'gun_revolver.38': ['revólver.38',['Arma de fogo para ataques de curta distância, ela usa munição de','calibre 16.'],2000,3,2,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
'gun_revolver.44': ['revólver.44',['Arma de fogo para ataques de curta distância, ela usa munição de','calibre 16.'],2000,3,2,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 5, 'CAPACITY': 6, 'GAUGE': 38}],
  
'gun_pistol': ['pistola',['Arma de fogo para ataques de média distância, ela usa munição de calibre 38.'],2500,3,2,{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 3, 'CAPACITY': 16}],
  
'gun_UZI.22': ['Uzi .22',['Arma de fogo para ataques de média distância.'],4000,3,2,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 1, 'CAPACITY': 10, 'GAUGE': 22}],
'gun_UZI.45': ['Uzi .45',['Arma de fogo para ataques de média distância.'],4000,3,2,{'DAMAGE': 5, 'RECHARGE': 8, 'CADENCY': 1, 'CAPACITY': 16, 'GAUGE': 45}],
  
'gun_shotgun.12': ['espingarda .12',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,4,3,{'DAMAGE': 5, 'RECHARGE': 4, 'CADENCY': 4, 'CAPACITY': 6, 'GAUGE': 12}],
'gun_carbine': ['carabina',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,4,3,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
  
'gun_sniper': ['sniper',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],6000,5,3,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
'gun_shotgun': ['escopeta',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],4000,4,3,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
  
'gun_assault_riffle': ['fuzil de assalto',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],4000,5,3,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
'gun_rifle': ['fuzil',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,5,3,{'DAMAGE': 4, 'RECHARGE': 3, 'CADENCY': 2, 'CAPACITY': 16}],
'gun_AK-47': ['AK-47',['Fuzil para ataques de curta distância, ela usa munição de calibre 16.'],5000,4,3,{'DAMAGE': 7, 'RECHARGE': 3, 'CADENCY': 2, 'CAPACITY': 20, 'GAUGE': 39.0}],
'gun_M16': ['M16',['Fuzil para ataques de curta distância, ela usa munição de calibre 16.'],5000,4,3,{'DAMAGE': 6, 'RECHARGE': 3, 'CADENCY': 1, 'CAPACITY': 30, 'GAUGE': 5.56}],
  
'gun_RPG-7': ['RPG-7',['Bazuca utilizada contra tanques.'],12000,7,5,{'DAMAGE': 50, 'RECHARGE': 10, 'CADENCY': 0, 'CAPACITY': 1, 'GAUGE': 0}],
   
#BATTLE ITEMS
'grenade': ['granada',['Use numa batalha para causar dano á todos os inimigos na tela.'],100,2,3,10,1],
'grenade_smoke': ['granada de fumaça',['Use numa batalha para que todos os inimigos percam AGILIDADE.'],200,2,3,3,4],
'grenade_flash': ['granada de luz',['Use numa batalha para que todos os inimigos percam sua vez.'],500,3,3,1,6],
'pepper_spray': ['spray de pimenta',['Use numa batalha para atordoar um inimigo.'],40,3,1,2,6],
'molotov_cocktail': ['coquetel molotov',['Use numa batalha para causar dano á todos os inimigos','e possivelmente queimá-los.'],40,3,1,2,6],
'horn': ['buzina',['Use numa batalha para atordoar um inimigo.'],40,3,1,2,6],
'extinguisher': ['extintor',['Use num caso de emergência.','...mas não é pra jogar num bulldogue.'],40,4,1,2,6],
'rope': ['corda',['Use em batalhas para prender seus oponentes','ou dentro de cavernas para descer e subir'],70,4,1],
   
#DRUGS
'drug_antibiotic': ['antibiótico',['Use para infeccionar feridas letais e impedir hemorragias, parando de consumir a barra de HP.'],25,2,1,0],
'drug_syrup': ['xarope',['Remédio utilizado para combater resfriados e alergias.'],10,2,1,0],
'drug_tablets': ['comprimidos',['Remédios utilizados para combater náusea.'],30,1,1,0],
'drug_pills': ['pílulas',['Remédios utilizados para combater dor muscular.'],40,1,1,0],
'drug_paracetamol': ['paracetamol',['Medicamento para combater a febre.'],40,2,1,0],
'drug_desloratadin': ['desloratadina',['Medicamento para combater a tontura.'],40,2,1,0],
'drug_pseudoefedrin': ['pseudoefedrina',['Medicamento para combater o resfriado.'],40,2,1,0],
'drug_ibuprofen': ['ibuprofeno',['Medicamento para combater o resfriado e a febre.'],40,2,1,0],
'drug_ciprofloxacin': ['ciprofloxacino',['Antibiótico útil contra conjutivite,','resfriado e febre.'],40,2,1,0],
   
'serum_antiscorpionic': ['soro antiescorpiônico',['Antídoto para combater veneno de escorpiões.'],40,2,1,0],
'serum_antivenom': ['soro antiofídico',['Antídoto para combater veneno de cobras.'],40,2,1,0],
'serum_antiarachnid': ['soro antiaracnídico',['Antídoto para combater veneno de aranhas.'],40,2,1,0],
   
'drug_adrenaline': ['adrenalina',['Remédio utilizado para reviver uma pessoa inconsciente.'],60,2,1,0],

#CONDIMENTS
'condiment_ketchup': ['ketchup',['Condimento muito usado em salgados.'],5,1,1,6,'0100'],
'condiment_sugar': ['açúcar',['Condimento muito usado em doces.'],5,1,1,6,'0100'],
'condiment_salt': ['sal',['Condimento muito usado em refeições.'],5,1,1,6,'0100'],
'condiment_pepper': ['pimenta',['Condimento muito usado em refeições.'],5,1,1,6,'0100'],
'condiment_oregano': ['orégano',['Condimento muito usado em salgados.'],5,1,1,6,'0100'],
'condiment_shoyu': ['shoyu',['Condimento muito usado em refeições.'],5,1,1,6,'0100'],

#DRINK
'drink_water': ['água',['O básico pra te manter de pé','no calor e no cansaço, BEBA ÁGUA.'],8,2,1,10,'0100'],
'drink_juice_orange': ['suco de laranja',['Saudável e nutritivo, o Jailson aprova.'],8,3,1,10,'0100'],
'drink_juice_passion_fruit': ['suco de maracujá',['Saudável e nutritivo, acalma a alma e o espírito.'],8,3,1,10,'0100'],
'drink_coffee': ['café',['Bebida que aumenta a sua energia.'],8,3,1,10,'0100'],
'drink_chocolate': ['chocolate quente',['Vai bem com biscoitos'],8,3,1,10,'0100'],
'drink_milk': ['leite',['Vai bem no café.'],8,3,1,10,'0100'],
'drink_coffeenmilk': ['café com leite',['Bebida preferida do criador','do jogo, foi muito útil.'],8,3,1,10,'0100'],
'drink_energy': ['energético',['Bebida que acelera o metabolismo','e aumenta a energia.'],8,3,1,10,'0100'],
'drink_cola': ['refri',['A bomba calórica que a gente gosta.'],8,3,1,10,'0100'],
'drink_guarana': ['guaraná',['Um suquinho barato e muito açúcarado','mas é bom, não confundir com cachos de olhos.'],8,3,1,10,'0100'],
'drink_beer': ['álcool',['Bebida alcóolica para aumentar a energia','Pelo amor de deus COM MODERAÇÃO.'],8,2,1,10,'0100'],
'drink_whisky': ['whisky',['Bebida alcóolica para aumentar a energia','Pelo amor de deus COM MODERAÇÃO.'],8,2,1,10,'0100'],
'drink_yogurt': ['iogurte',['Delicioso e saudável.'],8,3,1,10,'0100'],
 
#FOOD
'food_orange': ['laranja',['Fruta fácil de se achar','num pomar.'],3,1,1,2,'0100'],
'food_fish': ['pirarucu',['Peixe de água doce.'],3,1,1,2,'0100'],
'food_bread': ['pão',['O alimento matinal de cada dia.'],15,2,2,30,'0300'],
'food_peanut_candy': ['paçoca',['Doce de amendoim, fácil de encontrar em padarias.'],1,1,1,2,'0100'],
'food_peanut_candy': ['paçoca',['Doce de amendoim, fácil de encontrar em padarias.'],1,1,1,2,'0100'],
'food_coxinha': ['coxinha',['Salgado feito com massa frita e recheada com frango, fácil de','encontrar em lanchonetes.'],5,2,1,8,'0100'],
'food_pastry': ['pastel',['Salgado feito com massa frita e recheado com queijo.'],3,2,1,5,'0100'],
'food_puff_pastry': ['pastel folheado',['Salgado feito com várias camadas de massa e queijo.'],6,2,1,12,'0100'],
'food_brigadeiro': ['brigadeiro',['Doce de chocolate.'],2,1,1,3,'0100'],
'food_cheese_bread': ['pão de queijo',['Salgado feito com massa de queijo.'],5,1,1,7,'0100'],
'food_pudding': ['pudim',['Doce feito com leite condensado.'],10,3,1,15,'0300'],
'food_cake_corn': ['bolo de fubá',['Doce feito com ovos, leite, fubá, manteiga, trigo e fermento.'],12,3,2,18,'0500'],
'food_cake_carrot': ['bolo de cenoura',['Doce feito com ovos, leite, fubá, manteiga, trigo e fermento.'],12,3,2,18,'0500'],
'food_cake_chocolate': ['bolo de chocolate',['Doce feito com ovos, leite, fubá, manteiga, trigo e fermento.'],12,3,2,18,'0500'],
'food_packed_lunch': ['marmita',['Tem muitas coisas diferentes dentro, além de ser bem nutritivo!'],15,3,2,30,'0300'],
'food_egg': ['ovo',['Ele te deixa forte pra enfrentar qualquer perigo.'],15,2,2,30,'0300'],
'food_lamen': ['miojo',['O macarrão instantâneo','do cara que mora sozinho.'],15,2,2,30,'0300'],
'food_cookies': ['bolachas',['Biscoito com recheio sempre','foi chamado assim.'],15,2,2,30,'0300'],
'food_snack': ['salgadinhos',['50% do saco é de puro vento.'],15,2,2,30,'0300'],
'food_pizza_mussarella': ['pizza de mussarela',['Quem não gosta de pizza?.'],15,2,2,30,'0300'],
'food_pizza_shaggy': ['pizza de calabresa',['Quem não gosta de pizza?.'],15,2,2,30,'0300'],
'food_pizza_chicken': ['pizza de frango',['Quem não gosta de pizza?.'],15,2,2,30,'0300'],
'food_pizza_4cheese': ['pizza de 4 queijos',['Quem não gosta de pizza?.'],15,2,2,30,'0300'],
 
#WASTED FOOD
'food_coxinha_wasted': ['coxinha fria',['Não é mais tão gostosa quanto antes,','mas é comestível.'],2,1,1,4],
'food_peanut_candy_wasted': ['paçoca esfarelada',['O que antes era um doce maravilhoso','agora são apenas migalhas...'],1,1,1,1],
'food_egg_wasted': ['ovo podre',['ALGUÉM DESTRUIU O MEU OVO'],15,2,2,30],
 
#TRASH
'trash_packing': ['embalagem',['Um papel que não serve pra absolutamente nada','a menos que seja uma esponja amarela.'],8,1,1,10,'0100'],
'trash_bottle': ['garrafa de vidro',['Um item meio perigoso de se levar','nas suas costas,','sabe-se lá o que pode fazer com isso'],8,1,1,10,'0100'],
   
#KEY ITEMS
'key_bedroom': ['chave do quarto',['Se perder vai ficar sem caminha.'],10,1,1],
'key_chest': ['chave de baú',['Use para abrir um compartimento.'],10,1,1],
'key_vehicle': ['chave do veículo',['É o que põe o motor pra funcionar.'],10,1,1],
'key_park': ['chave do parque',['Ela serve pra entrar no parque nacional','onde você achou é outra história.'],10,1,1],
'key_lab': ['chave do laboratório',['Que honra ter as chaves do laboratório Fiocruz!'],10,1,1],
'key_office': ['chave do escritório',['Um homem simpático que deu','ele quer mesmo é ver o circo pegar fogo.'],10,1,1],
'key_cave': ['signo de mercúrio',['Uma placa de ferro com a inscrição','de mercúrio... estranho'],10,1,1],
'dungeon_key': ['chave',['Use dentro de instalações para abrir caminhos.'],10,1,1],
   
#ESSENTIALS
'id_card0': ['identidade',['Mostra suas informações básicas e prova sua autoridade acima','dos civis.'],0,1,1],
'id_card1': ['identidade',['Mostra suas informações básicas e prova sua autoridade acima','dos civis.'],0,1,1],
'id_card2': ['identidade',['Mostra suas informações básicas e prova sua autoridade acima','dos civis.'],0,1,1],
'id_card3': ['identidade',['Mostra suas informações básicas e prova sua autoridade acima','dos civis.'],0,1,1],
'id_card4': ['identidade',['Mostra suas informações básicas e prova sua autoridade acima','dos civis.'],0,1,1],
'id_card5': ['identidade',['Mostra suas informações básicas e prova sua autoridade acima','dos civis.'],0,1,1],
'credit_card': ['cartão de crédito',['Um item muito necessário na vida de um jovem adulto, use nos caixas','de banco, nem imagine em jogar fora!'],0,1,1],
'charger': ['carregador',['Use para carregar seu celular.'],40,1,1],
'portable_charger': ['carregador portátil',['Use para carregar seu celular.'],100,1,1],
'headphone': ['fones de ouvido',['Ao obter um, você consegue escutar o rádio do celular, mas atenção! ele quebra nos momentos mais inesperados.'],60,1,1],
'phone': ['celular',['Mais importante que o cartão só o celular, pode ser usado para fazer','chamadas e receber emails, mas lembre-se de recarregar.'],0,1,1],
 
#PILLS
'pill_strenght': ['suplemento de força',['Aumenta a FORÇA permanentemente em +10.'],500,1,1,0],
'pill_attack': ['suplemento de ataque',['Aumenta o ATAQUE permanentemente em +10.'],500,1,1,1],
'pill_agility': ['suplemento de agilidade',['Aumenta a AGILIDADE permanentemente em +10.'],500,1,1,2],
'pill_resistance': ['suplemento de resistência',['Aumenta a RESISTÊNCIA permanentemente em +10.'],500,1,1,3],
'pill_vitality': ['suplemento de vitalidade',['Aumenta a VITALIDADE em +10'],500,1,1,4],
'pill_mistery': ['suplemento misterioso',['Aumenta um atributo aleatório'],500,1,1,4],
   
#REPELLENTS
'repellent1': ['repelente básico',['Evita anomalias de aparecer por 10 minutos.'],50,2,1,10],
'repellent2': ['super repelente',['Evita anomalias de aparecer por 30 minutos.'],100,2,1,30],
'repellent3': ['ultra repelente',['Evita anomalias de aparecer por 60 minutos.'],250,2,1,60],
   
#ACESSORIES
'aim1': ['mira 1',['Customiza a mira de sua arma.'],200,1,1,1],
'aim2': ['mira 1',['Customiza a mira de sua arma.'],200,1,1,2],
'aim3': ['mira 1',['Customiza a mira de sua arma.'],200,1,1,3],
'aim4': ['mira 1',['Customiza a mira de sua arma.'],200,1,1,4],
'aim5': ['mira 1',['Customiza a mira de sua arma.'],200,1,1,5],
 
'acc_silencer': ['silenciador',['Aumenta o ATAQUE de uma pistola.'],200,1,1,1],
'acc_cartridge': ['cartucho extra',['Aumenta a capacidade da arma.'],100,1,1,2],
'acc_gun_butt': ['coronha',['Aumenta a AGILIDADE da arma.'],100,1,1,3],
'acc_bandolier': ['bandoleira',['Adiciona um espaço extra no inventário.'],100,1,1,3],
 
'locksmith1': ['chaveiro',['Use para guardar até duas chaves.'],10,1,1,3],
'locksmith2': ['chaveiro',['Use para guardar até duas chaves.'],10,1,1,3],
'locksmith3': ['chaveiro',['Use para guardar até duas chaves.'],10,1,1,3],
'locksmith4': ['chaveiro',['Use para guardar até duas chaves.'],10,1,1,3],
'locksmith5': ['chaveiro',['Use para guardar até duas chaves.'],10,1,1,3],
'locksmith6': ['chaveiro',['Use para guardar até duas chaves.'],10,1,1,3],
'locksmith7': ['chaveiro',['Use para guardar até duas chaves.'],10,1,1,3],
 
#CRAFTING
'craft_spring_small': ['mola pequena','',0,1,1],
'craft_fuel': ['combustível','',0,1,1],
'craft_cloth': ['pano','',0,1,1],
'craft_powder': ['pólvora','',0,1,1],
   
#TREASURES
'treasure_vase': ['vaso marajoara',['Um antigo vaso indígena feita da cerâmica do marajó.'],2000,3,3,0],
 
'jewel_emerald': ['esmeralda',['Essa jóia deve custar uma fortuna!'],2000,1,3,0],
'jewel_diamond': ['diamante',['Essa jóia deve custar uma fortuna!'],2000,1,3,0],
'jewel_ruby': ['rubi',['Essa jóia deve custar uma fortuna!'],2000,1,3,0],
'jewel_amethyst': ['ametista',['Essa jóia deve custar uma fortuna!'],2000,1,3,0],
'jewel_sapphire': ['safira',['Essa jóia deve custar uma fortuna!'],2000,1,3,0],
'jewel_opal': ['opala',['Essa jóia deve custar uma fortuna!'],2000,1,3,0],
'jewel_gold': ['ouro',['Essa jóia deve custar uma fortuna!'],2000,1,3,0],
'jewel_quartz': ['quartzo',['Essa jóia deve custar uma fortuna!'],2000,1,3,0]
}
 
INVENTORY = [
[[['_','0000','_','_'],['phone','360100','_','_'],['wallet','00005000000300','credit_card','id_card0'],['locksmith1','02020000','key_bedroom','key_vehicle'],['_','0000','_','_']],
[['amulet1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['clth_jacket1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['ammo.38','0000','_','_'],['_','0000','_','_']],
[['clth_shirt1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['bag1','0000','_','_'],['gun_revolver.38','0006','aim1','acc_cartridge'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
 
[[['head_glasses','0000','_','_'],['food_peanut_candy','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['clth_jacket3','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['bag1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
 
[[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['bag1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
 
[[['amulet4','0000','_','_'],['repellent1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['amulet5','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['food_coxinha','1103','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['charger','000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['bag1','0000','_','_'],['gun_revolver.38','0006','aim3','acc_gunbutt'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
 
[[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['bag1','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
 
[[['amulet7','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['amulet6','0000','_','_'],['condiment_ketchup','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['amulet2','0000','_','_'],['_','0000','_','_'],['pill_vitality','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['amulet3','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']],
[['bag1','0000','_','_'],['gun_revolver.38','0006','aim2','acc_bandolier'],['_','0000','_','_'],['_','0000','_','_'],['_','0000','_','_']]],
]
 
STORAGE = [['jewel_ruby','0000','_','_'],['drink_whisky','1503','_','_']]

CHESTS = {
'1bedroom_202': [False]
}

PRODUCTS = [
[['drink_beer','drink_whisky'],0,0],
[['vest1','repellent1','food_coxinha','pill_vitality','melee_knife','amulet1','aim1'],1,10],
[['grenade','pepper_spray','gun_revolver.38'],1,2],
[['melee_fishmonger','portable_charger','headphone'],4,0]
]
 
VEHICLES = {
'moto_0': {'SPEED': 8, 'ACCELERATION': 0.5, 'CAPACITY': 100, 'GAS': 0.075, 'LIGHTS': 2, 'DIRECTION': 1},
'moto_1': {'SPEED': 10, 'ACCELERATION': 0.25, 'CAPACITY': 100, 'GAS': 0.05, 'LIGHTS': 1, 'DIRECTION': 1}
}
 
NUMBERS = [['Sidney','989074454'],['Jane','991124257'],['Renan','990435671'],['Diego','926148930'],['Bianca','976564008'],['Lúcia','990271802'],
['Maicon','923778988'],['Iago','977904623'],['Sofia','923578103'],['Vinícius','960428331'],['Pietra','940028922'],['Paulo','987690021'],['João Grande','956230401'],
['Pizza Delivery','953478809'],['Correios','909236521'],['Mercador','969696969']]
 
CONTACTS = [['Maicon','923778988'],['Mercador','969696969'],['Pizza Delivery','953478809']]
 
CALLHIST = []
 
EMAILS = [
['prfrj@cmail.com','Caso de anomalia',['Boas novas','','Uma anomalia foi encontrada nos','arredores do Parque Nacional do Itatiaia,','É necessário a eliminação do','indivíduo assim que o possível','','Encontrem seus próprios meios','para adentrar o local.']],
 
['prfrj@cmail.com','Caso de anomalia',['Boas novas','','Uma anomalia foi encontrada nos','arredores da cidade de Resende,','É necessário a eliminação do','indivíduo assim que o possível','','Encontrem seus próprios meios','para adentrar o local.']],
 
['cangaceirostv@cmail.com','Proposta de entrevista',
['Boas novas, ' + CHARACTERS[0]['NAME'] + ' ' + CHARACTERS[0]['LASTNAME'] + '.', ' ', 'Com a repercussão dos casos de', 'anomalias do Departamento de', 'Detenção de Anomalias de',
'Itatiaia, sugerimos uma', 'entrevista com você e dois', 'participantes para o', 'Jornal da Noite.', ' ', 'A entrevista será ás 5:30 PM', 'e será gravado nos estúdios', 'da Cangaceiros TV, na',
'Av. Getúlio Vargas.', ' ', 'Aguardamos sua resposta', 'no local.']],
 
['mendoncapietra7@cmail.com','Oiee',
['Só tô te testando menino']],
]
 
INBOX = []
 
NEWS = [
[
[['Polícia Municipal abre a','renovação da carteira'],'Tereza Rocha',['Em 4 de abril, a Polícia Municipal abriu a renovação da carteira para mercenários. A carteira de identificação de Mercenário é \
obrigatória não só por identificação, mas por questões de segurança, depois que a câmara dos deputados aprovou a reforma armamentista, qualquer cidadão com a identificação de mercenário é livre para portar \
e possuir uma arma de fogo.','',' Recentemente, houveram vários casos de assassinatos não registrados pela polícia, pela incapacidade da polícia de analisar todos os casos separadamente, mercenários tem sido \
recompensados para cuidar desses assassinatos misteriosos.','','Devido a isso os dados de homicídio por armas de fogo aumentaram consideravelmente no estado, isso se deve á facilidade de se obter uma arma e também de \
reduzir a pena de um criminoso para servir ao estado como mercenário. O criminólogo Mauro Fidélis fala sobre a situação.','','"O que a polícia do rio de janeiro fez foi um ato irresponsável e inpensável, pois \
graças á essa facilidade de se armar, vários criminosos podem se aproveitar e utilizá-las para fins maliciosos, e mesmo com tantos casos de homicídios não registrados, o que custava a polícia recrutar mais policiais ou \
fazer uma investigação profunda e mais elaborada á respeito?"','','Sabendo disso, tudo o que podemos esperar é que os mercenários façam bom uso de seu poder bélico.']],
[1,['sex','32',0],['sab','25',1],['dom','22',1],['seg','18',2],['ter','15',3]],
[2,0]
],
 
[
[['Parque Nacional do Itatiaia','é invadido'],'Jéssica Ramone',['Na tarde do dia anterior, um','caso que deixou autoridades','em estado de alerta, foram','filmadas imagens de vândalos',
'invadindo o parque nacional.','','"não é o que se espera','dessa juventude, não é?", diz','Marcelo Marinho, fiscal do','IBAMA e principal supervisor','do parque','',
'O Parque Nacional do Itatiaia','é uma área de preservação','da fauna brasileira protegida','por lei, pois é onde se','encontra o que resta da','mata atlântica, que vem','sofrendo drásticas degradações',
'com o tempo.','','Mas o maior desafio do','parque não são os vândalos,','mas sim os mercenários,','vários invadem locais restritos','atrás das presas e do','dinheiro, colocando em risco',
'a fauna e a flora da','natureza. A PRF já','possui conhecimento de tais','atos ediondos.','','"É lamentável, a gente pensa','que confia mas eles','só mostram que estamos',
'se enganando", diz Paulo Sousa','','O IBAMA, instituição','responsável pelo monitoramento','do parque, emitiu uma nota','avisando que irão reforçar','a segurança no local,',
'policiais militares armados','e cães de guarda são','apenas um pouco do','que os mercenários podem','temer de agora em','diante.']]
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
 
TASKS = []
 
if CHARACTERS[0]['GENDER'] == 'male': gn = 'moço'; prps = 'meu'
elif CHARACTERS[0]['GENDER'] == 'female': gn = 'moça'; prps = 'minha'
else: gn = 'moçe'; prps = 'minhe'
 
if TIME[0] > 17: dt = 'Boa noite'
elif TIME[0] > 11: dt = 'Boa tarde'
elif TIME[0] > 5: dt = 'Bom dia'
else: dt = 'Boa noite'

'''
0 - outro falante
1 - pausar
2 - começo do capítulo
3 - fim do capítulo

0 - ganhar dinheiro
1 - ganhar item
2 - moralidade
3 - marcador do mapa
4 - ligação
5 - novo email
6 - nova tarefa
7 - contato adicionado
8 - troféu
9 - subir de rank
10 - escolha de diálogo
11 - avançar diálogos
12 - voltar diálogos
13 - batalha
14 - exército
15 - música
16 - som
17 - delivery
18 - mudar party
19 - abaixar status
20 - aumentar status
21 - dlgsav
22 - nomear
23 - outro diálogo
24 - mover personagem
25 - emoção do personagem
26 - câmera
27 - esperar
'''
 
DIALOGS = {
'TEST': [['Vou te dar uma tarefa rapaz!',1,[6,'tarefa'],'Fale com outro cara pra cumprir essa tarefa!',1,'Mas também vou te dar meu número!',1,[7,0],0,'Acho que só falta esse email',1,[5,0],'Já tem tudo o que quer','Agora rapa fora!',1]],
 
#OBJECTS
'MIRROR': [['Que peste feia é essa','ah, sou eu',1],['Estou bonita...?',1],['Bigodin finin','Cabelin na régua',1],['Dá pra sair',1],['Sempre arrasando',1],['Tô bem arrumada',1]],
'SIDNEY WARDROBE': [['Qual roupa vou vestir agora?',[10,['Casaco xadrez','Ok'],['Blusa preta de banda','Sempre gostei do HUG'],['Blusa social','Essa tá boa']]]],
'BROKEN CLOCK': [['Isso tá quebrado faz tempo.',1]],
'SIETRA PORTRAIT': [['Essa foto me traz muitas lembranças...',1,'...lembranças ruins.',1],['...',1,'Eles se davam bem...',1]],
'JANAGO PORTRAIT': [['Legal.',1],['Essa foto foi em Búzios',1,'Foi o dia em que nós','começamos a morar juntos',1,'A gente comeu muito camarão naquele dia',1]],
'BED': [['Ah não...',1,'a cama tá bagunçada de novo',1,'...',1,0,'...abracadabra, cama arrumada!',1]],
'PICTURE': [['É uma pintura bonita',1,'não tô entendendo nada','só sei que é bonita',1]],
'DIRTY SINK': [['A pia está cheia de louça suja...',1]],
'DIRTY COOKER': [['Tem arroz frio e uma frigideira engordurada no fogão.',1]],
'EMPTY FRIDGE': [['Água,sachês de ketchup e ovos...',1,'Considero isso uma geladeira vazia.',1],['Tá na de fazer as compras do mês.']],
'JANE FRIDGE': [['A visão do paraíso.',1],['O Iago comprou um monte de sorvete.','Esse idiota me conhece.']],
'OLD PC': [['Esse pc ainda usa Windows XP.',1]],
'MODERN PC': [['No canto da tela diz "Não é genuíno".',1]],
'PC GAMER': [['O teclado LED brilhando me deixa','ma',1,'lu',1,'co.',1]],
'OLD TV': [['O Maicon precisa trocar logo essa TV.',1]],
'PLUG': ['Você pode encaixar um carregador aqui.',1],

#CHESTS
'EMPTY CHEST': ['Não tem nada aqui...',1],
'SIDNEY NIGHTSTAND': [[[1,'food_peanut_candy',0,1]],[0,'Não deveria mexer nas','coisas dos outros',1]],
'HH FRIDGE': [[[1,'drink_beer',0,1]],[0,'Não deveria mexer nas','coisas dos outros',1]],
'TRASH CAN': [[[1,'melee_bottle',0,1]]],
 
#PAPERS & SIGNS
'TAROT POSTER': ['BÚZIOS E CARTAS','Trago seu amor aos seus pés!','978543322'],
'MISSING POSTER': ['PROCURA-SE','Talita Manhães','Se você a viu, favor, ligue para: 992120342'],

#ENEMIES
'IRRATIONAL': ['A anomalia não entende nada do que você tá falando',1],
'TARGET': ['Parece bobo, eu sei','Mas é bom já pegar o jeito da coisa.','Ás vezes você pode negociar com o oponente','E assim poupar sua vida.','Também pode obter informações','Importantes dele',
'Ou mesmo convencê-lo a parar de lutar'],
 
'VINICIUS': [[10,['Eu não quero brigar contigo','Eu também não quero','Mas é preciso'],['Você pode ficar com a recompensa','Você está blefando?',[10,['Vai pegar?','É claro que vou!','...assim que acabar com você!'],['Esqueçe','Agora estou mais invocado!']]]]],
 
'EMOHIPSTER': [[10,['O que você escuta?','conhece aquela banda?','HUG','muito boa',[10,['eu também gosto de HUG!','sério?!','ai meu deus! que legal!'],['já ouvi falar','é muito boa cara','você tem que escutar']]],['se manda daqui ô barbudo!','como é que é?','o que você tem contra barba?',[10,['Nada oxe','é bom mesmo'],['Isso não é barba','mas...eu cuido tanto dela...']]]]],
 
'HOTMAN': [[10,['Cê tá bem mano?','Claro que não né?? Estou queimando feito palha nessa desgraça!'],['Vaza ou meto chumbo','Eu não tenho medo de você'],['A gente não quer nada contigo',
'Mas eu quero','Preciso de sangue!!']]],
 
#PLACES
'REWARD':[['Ei! Você não tem sangue nenhum!','Volte quando tiver pego alguma coisa!',1],['Só isso?','Vou dar sua recompensa, mas poderia ter se esforçado mais',1],['Você conseguiu bastante sangue','Aqui está sua recompensa',1],['Uau! isso é muito sangue!','Aqui está sua recompensa pelo seu trabalho duro!',1]],
'MERCATOR': [['Olá cliente!','Interessado em alguns produtos?',1],['Foi mal cara, mas sem grana, sem acordo.',1],['Espera um pouco cara!','Você tá sem espaço!',1,'Não quer dar para outra pessoa?',1]],
'CASHIER INGRID': [['Os produtos estão nas pratileiras','é só você ir pegar e trazer aqui',1,0,'O quê? você quer que eu vá buscar pra você?!',1],['Você não tem dinheiro?',1,'Sério?',1],['Você tá cheio de coisas...','Não sei se posso deixar levar tudo isso.',1]],
'CASHIER SANDRA': [['Vai pedir alguma coisa?',1],['Você tá sem dinheiro.',1],['Você tá sem espaço',1]],
'CASHIER YASMIN': [['Eu tenho que dormir...','compra logo o que tu quer...',1],['Como é que você leva coisas','que não pode comprar??',1],['Fala sério',1,'Por favor leve só o que puder levar',1]],

'DRITHR SANDRA': [['Licença, aqui é o Drive Thru',1],['Você tá sem dinheiro.',1],['Você tá sem espaço',1]],
 
'FARMACEUTIC': [['Não sabe que remédios comprar?',[10,['Não...','O que você quer tratar?',[10,['Resfriados e alergias','Se você estiver sentindo algum resfriado,','gripe, tontura ou fraqueza, um\
 simples','xarope já basta'],['Infecções e hemorragias','Esses são problemas fortes, mas não muito graves','Para infecções, use o antibiótico correspondente ao tipo de','contaminação.',0,'Se tiver\
  hemorragias, primeiro cicatrize a ferida','e depois ponha um band-aid para','evitar mais saída de sangue'],['Contaminação e Mal-estar','Caso se sinta alguma coisa parecida, pode ser','sinal de envenenamento ou\
   intoxicação, existem','várias pílulas para diversos tipos de tóxicos']],'Mais alguma pergunta?',[12,7]],['Tô de boa','Tudo bem','Se tiver alguma dúvida é só perguntar','Fique á vontade']]]],
 
'HOTEL ATTENDANT': [['Bom dia!','O que deseja?',[10,['Uma noite apenas','O custo é de 20 por pessoa',[10,['Ok','Aqui, seu quarto é o N° 902',[0,'chave',20]],['Deixa pra lá','Volte a hora que quiser']]],
['Estou apenas olhando','Sinta-se á vontade']]]],
    
#CITIZENS DIALOG
'DALIBOR': [['VEM AQUI TODO MUNDO!!',1,0,'Que foi isso?!!',1,0,[26,4],[24,None,(184,370),8],[24,1,(200,330),2],[27,70],'Estão todos os mercenários aqui?',1,0,'Não, tem um lá fora e outro','não chegou ainda',1,0,'Ah pronto',1,'não tenho idade pra essas coisas...',1,
'seguinte...',1,'vamos fazer assim então',1,'você',1,0,'quem, eu?',1,0,'Sim! você!','Pode falar o nome e sobrenome','de vocês seis?',1,[10,['Não ( nomes padrões )','Não sabe?',1,'Era só o que me faltava...',1,
'então a mulher do seu lado','vai me dizer',1,'Beleza?',1,[22,False]],['Sim ( nomear personagens )','Ok','Vai falando',1,[22,True]]],'Muito bom','Quando todos chegarem','Nós vamos dar início ao','interrogatório',1,
[27,20],[26,1],[27,20],'Esquisito',1,'Eu imaginava que um interrogatório','fosse bem mais...',1,'...pesado','digamos assim',1,0,'Verdade...',1,0,[27,30],[21,4,1],[23,'HHBIANCA',1]],
['Chame todo mundo pra','começar as gravações,','por favor',1],['Estão todos aqui',1,'vamos começar?',1,[10,['Espera um pouco','Venha quando','estiver pronta',1],['Podemos','Excelente',1,'Atenção!','Põe essa máquina','pra rodar!',1]]]],

'DDA AGENT 1': [['Tá procurando alguém?',1,[10,['Não','Tudo bem',1,'Se estiver precisando','de ajuda, é só','falar',1],['Sim','Eu vi um homem subindo','as escadas',1,'Deve estar lá','em cima',1]]]],

'DDA AGENT 2': [['Vocês entraram em encrenca',1,'Tem noção do que seus','preciosos olhos testemunharam?',1,[10,['Do que tá falando?','Não se faça de besta!',1,'Espero que tenha','muita coisa pra',
'contar para o','Senhor Dalibor!',1],['Nem imagino','Você não tem noção',1,'Nunca antes se','viu um evento','dessa magnitude',1,'Por isso mesmo','nós precisamos que','vocês contem tudo','pra gente',1],
['Eu tô com pressa','Que isso',1,'Se acalma',1,'Bebe um copo','de água',1,'Você vai ter','bastante tempo','quando falar com','o Senhor Dalibor',1]]]],

'HHSIDNEY': [[0,'Oi, ' + CHARACTERS[0]['NAME'] + '.',1]],

'HHBIANCA': [['O que foi?',1,0,'Era Iago','Perguntou se eu tava bem',0,1,'Ah tá',1,2,'Pelo menos ele se preocupa','com você',1,0,[25,None,'BLANKDD'],'Sim',0,1,[27,100],'Percebeu onde a gente','conseguiu chegar?',
1,0,[25,None,'BLANKLD'],'Como assim?',0,1,'Ás vezes nós não','nos damos conta...',1,'...mas agora a pouco eu','era pesquisadora',1,'E agora além de tudo a gente','sai pra caçar monstros',1,'não é esquisito?',1,
[10,['Não são monstros','Você entendeu o que eu','quis dizer',1],['Muito esquisito','Não é??',1]],'Isso parece até coisa de filme',1,'Mas isso não é errado?',1,[10,['Acho que não','Mas por que?',1,0,
'A gente não está salvando','as pessoas?',1,'Eu acho que isso é o','que importa',0,1],['Eu não ligo','Sei não...',1,'Não gosto dessa coisa de matar','bichinhos',1,0,[24,None,(None,None),5],[25,None,'BLANKL'],'Mas não são bichos, garota!',0,1]],
'Eu sei',1,'Mas mesmo assim...',1,0,'Ei',0,1,'O quê?',1,[10,['Não se culpe por isso',0,'No começo parece que','você está fazendo a coisa','mais cruel do mundo',1,'Se já deve ser difícil',
'pra quem trabalha na polícia','imagine pra gente',1,'Nós apenas estamos fazendo','o que é melhor pra todos',0,1],['Eu já me acostumei',0,'Não ligue para o que os','outros dizem',1,
'Eles não são a gente','pra dizer alguma coisa!',1,'Se estivessem no nosso lugar','fariam o mesmo',0,1]],'Sim, mas...',1,'...',1,'...precisa ser matando...?',1,[21,1,1],[23,'DALIBOR',0]],
[0,'Viu o ' + CHARACTERS[0]['NAME'] + '?',1,0,'Não, não vi...',1,0,'Vê onde ele está, por favor?',1,0,'Tudo bem',1,[18,4]]],

'HHDIEGO': [['Aí pessoal,','licença que vou','pegar algo pra','beber',1,'vai querer algo?',1,[10,['Não, obrigado','Ok então',1],['Qualquer coisa serve','Beleza',1]]]],

'HHLUCY': [['Ei, você viu','se ele já voltou?',1,[10,['Eu ia perguntar isso','É, ele não aparece',1,[10,['Pode procurar ele?','Claro']],['Não vi ele','Ele tá demorando','muito...',1]],'Eu já volto',1]]],
 
'BUS WAITER': [['Esse ônibus demora mesmo',1,'Pego ele todo dia pra','descer a serra até a capital',1,'São só 4h de viagem!',1,2]],
'SQUARE OLD MAN': [['Eu adoro alimentar os pombinhos',1,'ainda mais aqueles que','tem um monte de penas','lindas no rabo',1,[10,['como assim?','elas chegam a hipnotizar...',
'eu fico olhando e perco','a noção do tempo.',1],['legal','são adoráveis',1]]]],
'HOMELESS MAN': [['Pode me dar um trocado','por favor?',1,[10,['...','é sempre assim...',1],['Tudo bem',[0,-1],'Deus te abençoe!',1]]]],
'STREET SWEEPER': [['Hey mano',1,'Posso te falar uma coisa?',1,[10,['É claro','Se estiver com lixo nos','bolsos ou na mochila...',1,'por favor...',1,'...jogue na lixeira',1,
'Não custa nada',1,'Tem uma em cada esquina da cidade',1,'Fechou?',1],['Agora não...','Tá bom então...',1,'não é como se fosse','te dar uma informação','importante que fosse',
'mudar sua vida e seu','jeito de agir',1,'bola pra frente',1]]]],
'YOUNG MOM': [['Meu filho adora brincar','nesse monte de areia',1,'Também gosto porque','o sinal da praça é','muito bom',1,[10,['o quão bom?','quê?',1,[10,['o quão bom?','ah...',
'dá pra ver as notícias','e mexer na internet',1,'não é muita coisa porque','meu celular é de tecla',1,'mal posso esperar ter','um daqueles celulares novos','que você pode tocar',
'na tela',1],['esquece','ah tá',1]]],['não é pra tanto','é o que você pensa',1,'pelo menos é melhor','do que em outras cidades',1],['mas é só aqui?','meio que sim',1,'o sinal só é bom',
'mesmo na praça',1,'mas dá pra usar o sinal','em outros lugares também',1]]]],
'FUNNY KID': [['Iaaaaaaá!',1,'que fofo',1]],
'INFORMED MAN': [['Eu sempre vejo as','notícias na televisão',1,'mas quando a internet está','boa eu vejo no celular','também',1,[10,['deveria ver mais jornais','vai por mim, hoje em',
'dia é mais que necessário',1,'ainda mais com essa onda','de crimes por causa dos mercenários',1,'eles avisam quando tá tendo','caça na região',1],['não gosto muito de notícias',
'mas por que?',1,[10,['É muita violência','eu também acho',1,'mas é a vida',1,'se não se informar, pode','perder muita coisa importante',1],['Não tenho tempo pra isso','Ler um artigo não',
'faz mal cara',1,'não demora muito, é bom','parar a correria do dia','pra ler alguma coisa',1],['É tudo mentira','eu concordo',1,'mas sei lá','quem não mente hoje?','eu faço assim, leio a matéria',
'mas com uma certa desconfiança',1,'eu preciso me informar,','mas se eu sair acreditando','em tudo que vejo,','aí eu posso acabar','espalhando mentiras',1]]]]]],
 
'OLD MAN': [['É bom você sempre','tirar dúvidas com o','entendido do assunto.',1,'Minha filha comprou um','antibiótico e pensou que','era pra beber.',0,'Agora ela tá no hospital...','Essa menina...',1]],
'INJURIED DAUGHTER': [['É bem vergonhoso dizer o motivo',1,'Mas estou internada porque','bebi antibiótico',1,'Devia ter escutado meu pai...',1]],
'PRETTY MOM': [['Minha filha tá me','pertubando pra levar alguns','doces pra ela.',1,'É assim toda hora,','ela vai parar já já.',1]],
'PRESSING CHILD': [['Mãe!','Tem tantos doces aqui!','Eu quero!','Eu quero!','EU QUERO!',1]],
 
'DOCTOR': [['Você sofreu várias fraturas no corpo','A conta dos cuidados foi de $100 por pessoa']],
'WORRIED NURSE': [['Você deveria se cuidar mais','É muito comum te ver por aqui']],
'HINT NURSE': [['Tome cuidado com sua vida!','Não digo por causa da saúde, mas pelo dinheiro',0,'Se não tiver dinheiro da próxima vez, pode','entrar em prejuízo.']],
'PATIENT': [['Eu quero ir pra casa logo','A comida daqui é horrível!']],
'IMPATIENT PATIENT': [['Eu tô na fila desde anteontem','Parece até que nunca anda!']],
 
'BANK GUARD': [['Ponha qualquer objeto de metal que tiver','na caixa ao lado',1]],
'UNLUCKY MAN': [['Não é possível','uma coisa dessas!',1,'O caixa acabou de entrar','em manutenção!',1,'ERA MINHA VEZ!',1]],
'OLD WOMAN': [['Como que faz pra','tirar a telesena aqui?',1]],
    
'NPC': ['Oi...eu te conheço?','Você não deveria estar falando com estranhos','Agora não ' + gn + '! Eu tô com pressa!','Afe, mercenários...','Não quero falar com você','Licença'],
'DOOR': ['Não conheço você','Quem é você?','O que você quer?','Vai embora!'],
    
'HOTEL DOOR': ['Esse é meu quarto','Aqui não é seu quarto, ' + gn, gn + 'está perdido?'],
    
'KONAMI GUY': ['Hey, sabe o que acontece se você apertar cima, cima, baixo, baixo, esquerda, direita, esquerda, direita, B, A e START?','Merda nenhuma!'],
    
#CHARACTERS DIALOG
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
'Eu já tô indo','Deixa que eu pago essa','Sério?','Sim, é por minha conta','Você é demais cara',[6,'Renovar a Carteira']],
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
['Lembra de mim, filho da mãe?','você!','Essa é pra aprender a não mexer comigo!',[9,2],'???','O que você estava fazendo?',[10,[],[]]]],
    
'CHAPTER_2': [['Olá?','...','Eu tô apertada sabe?','j-já vou sair!','Eu espero...','...','Finalmente...','...','...você tá bem?','não.','ah...desculpa...','Você não tem culpa de nada','Por que você tá chorando?',
'Nada demais, sério não precisa se preocupar','...tá bom então...','Só um desgraçado que não liga pra ninguém e só se importa com ele mesmo! Nunca tem tempo pra nada! E ainda cobra de mim!','...é um cara?',
'A gente não se vê faz meses, só conseguimos se falar por telefone, ele sempre diz que vai voltar algum dia mas nunca vem!','Bom...pelo menos ele se importa...','...','...não?','Ele finge que se importa, fica fazendo falsas promessas e me fazendo de otária!',
'É seu namorado?','Não...quer dizer, não mais...ele era...','é complicado...','Você acha que deveria esquecer?','Honestamente...','...','Sim, você deveria','Mas eu ainda gosto dele!',
'Problema seu, você tem que parar de se prender á pessoas que não te fazem feliz, a vida é assim','Nossa que duro','Que nem sua cara bateu no muro','Afe, para!','Tá bom, mas é sério, vai fazer bem pra você, uma hora isso passa',
'...entendi','ok?','ok','Então tira essa lágrima do rosto e vai se divertir, se quiser posso ir contigo, tá sozinha?','Não, mas pode vir','Ah, obrigada!','Você DEVE vir','Eu sei menina, relaxa! Como se chama?',
'A menina que veio te caçar','Que isso garota pera aí...','...','...','...Te caçei','Ah fala sério!','Obrigada por me escutar, mas preciso ir direto para o que interessa','Caramba, eu acabei que tinha criado um laço de amizade aqui!',
'Olha não tem nada a ver comigo, me pediram para fazer isso, tá bom?','Fala logo o que você quer!','Preciso das suas amostras','Elas estão no laboratório','Eu sei que estão no laboratório, você vai me levar até a sala onde estão guardados e entragar para mim',
'Eu não faria isso','Olha, eu não sou burra e sei que se eu atirar aqui dentro vão me prender, mas eu posso muito bem te fazer ir para meu carro com a pistola nas suas costas!','Você não faria isso','Não mesmo, mas adivinha? eu tô fazendo!',
'Ei pera!','...?','Tá vindo alguém!','Rápido se escon-',[13,'pietra']],['']],
 
'CHAPTER_8': [['Olá?','...','Alguém em casa?','...','...','Olá! Em que posso ajudá-los?','Boa tarde senhor, essa fazenda é sua?','Oh sim, é minha desde que meu avô começou a capinar, quando tudo isso ainda era mato!','...mas só tem mato aqui senhor',
'Pois é, faz um bom tempo que não tem ninguém para cuidar da minha fazendinha, só resta eu e minha maloca...','Mas esses animais também são seus?','Ah não, apareceram aí! Não são criatuinhas de Deus?',
'Nossa ' + CHARACTERS[1]['NAME'] + ', tem um Boi Dourado ali!',CHARACTERS[3]['NAME'] + '! Se concentra!','Então...nós somos...','...detetives?','...','...sim! sim, detetive ' + CHARACTERS[3]['NAME'] + ' e minha colega, detetive ' + CHARACTERS[1]['NAME'] + '.',
'Muito prazer, me chamo Hermes, eu já imaginava que fossem pois não tem uma semana que alguém bate na minha porta!','É mesmo?','Sim! vocês não sabem?','Não, viemos de outra cidade','Ah...vieram de onde?','Vargi...','Itatiaia!','Pera, quê?',
'Não é que ele','A gente acabou de vir de Itatiaia, mas estamos indo pra Varginha','É, isso mesmo','Interessante...é porque Policiais vieram aqui perguntando um monte de baboseira...umas presepada que não sei nem o nome!','Geóglifos?',
'Sim, e acho que você gostariam de saber algo a respeito, não é?','Sim, o depoimento dos moradores próximos é muito importante!','Bom, eu não sei nada desses Zoológicos coisa nenhuma, mas por alguma razão todos vem me perguntar','É porque, Sr. Hermes, os Geóglifos estão na sua fazenda',
'Pois é, mas é justamente porque ela está a tanto tempo parada que não me informo dessas coisas entende? Talvez alguma pessoa tenha invadido meus campos e fez esses desenhos no mato!','Hermes...','Olha ' + CHARACTERS[1]['NAME'] + 'Acho que já conseguimos informações o suficiente do Sr. Hermes, e aliás, acho que um vândalo qualquer seria mais suspeito do que qualquer aposentado de meia-idade','Eu trabalho',
'Ah, sério?','Sim, eu vendo artesanato','Boas vendas, Hermes','Muito obrigado...', CHARACTERS[3]['NAME'] + '.',CHARACTERS[3]['NAME'] + '! Muito obrigado pela ajuda de vocês!','O prazer é todo nosso!','...','Por que fez isso?',
'Muita gente já falou com ele, se fizermos perguntas demais ele pode fazer alguma coisa!','O quê? destruir provas?','Exatamente isso','Por que ele faria isso?','É o que estamos tentando descobrir!'],
['Ainda não entendo como foi tão simpático com aquele velho...','Por que? você acha ele mau?','Não...mas eu desconfio dele, não deveria falar desse jeito com ele','Então o que você sugere?','Seja mais duro?!','Não dá pra gente conseguir nada das pessoas sendo duro com elas','Os policiais conseguem',
'Ele é um cara muito suspeito, isso a gente já sabe, mas como ninguém conseguiu tirar provas dele, quer dizer que ele é muito bom em guardar segredo','Eu não sei...acho que a gente devia sequestrar ele',
'Claro que não!','Nossa calma! Eu só tava falando...','...','Então o que a gente vai fazer?','Vamos continuar investigando','Ah sim, claro que sim...','O problema de leigos como você é que eles tentam começar de cima...','Como é que é?','É a verdade',
'Olha me escuta aqui ' + CHARACTERS[3]['LASTNAME'] + '! Você não sabe quem eu sou e de onde eu vim! Então é bom você ficar calado que aí você ganha mais e não caga pela boca!','Ok...']],
 
'VINICIUS': [[[15,'battle_incoming'],'O que tá fazendo aqui?','Quem pergunta sou eu! O que VOCÊ tá fazendo aqui?','Com certeza não é deixar você roubar minha recompensa',0,'E quem disse que ela é sua?','Garoto,melhor sair do meio, ou vai dar\
 muito mal pra nós dois',0,'que assim seja então!',[13,'madladcat','vinicius']]],
'RENAN': [[[15,'battle_incoming'],'Você mexeu com a turma errada cara!','Tá na hora de aprender uma lição!',[14,0]]],
'BIANCA': [['Hey ' + CHARACTERS[0]['NAME'] + ', fique com essa lupa, Eu fiz ela apenas para pesquisar anomalias.','Quando enfrentar uma anomalia que não está registrada no bestiário,','Use-a para registrar a anomalia.',[0,'lupa']]],
'SIDNEY': [['1Não tenho um minuto de paz nessa desgraça!!','2Eu achei que eles iam ficar de boa','1Se tem uma coisa que você tem que saber sobre as pessoas é que elas odeiam pessoas com armas na mão atirando por aí','2Mas você salvou elas! Matou esse...essa...','1...Lata Alada','2Que','1O nome da anomalia','2Noooooosa!','1Vou botar essa no Bestiário','2Tá, mas elas deveriam ter um pouquinho de consideração né?','1Ninguém tem um pingo disso com ninguém da DDA','2Conplicado...','1É gente que nunca viu uma gota de sangue na vida e já ficam chocadas, esse aí é o mesmo pessoal que fica com esses papos de veganismo depois','2hmmm...nah']],
'JANE': [["I don't wanna to","I not in a good mood, you know...",[10,["It's all right?","Oh, no! I just don't want to cause any trouble"],["Fine then","Yeah"],["But you need to do it","Look, since the last time I put my hand on a gun, it wasn't a wise choice!","I don't want people to suffer from my mistakes!","I just mess everything up...",[10,["You don't","I know you are saying this just to chill me down, but I don't want to fool myself","I have to accept this"],["Everyone makes mistakes","But not everyone kills a person, right?",[10,["What?","Oh, you don't know?","Awwww...I should shut my mouth"],["...","..."]]],["It's hard","At least you recognise"]]]],0,'Well, I have to go...','See you later']],
'MATT KAI': [['EU AMO PINK FLOYD','EU AMO PINK FLOYD','EU AMO PINK FLOYD','2Esse é o criador do jogo?','1Ele mesmo','2Sem nexo','1Mó fita']],

#CONTACTS CALL
'989074454': [['Sidney']],
    
'991124257': [['Oi! Sou eu, a Jane']],
  
'990435671': [[[CHARACTERS[1]['NAME']+'! Precisamos de você aqui AGORA!','Eu sei que você saiu e coisa e tal, mas a gente PRECISA DE VOCÊ!','Estamos na Av. Jobim, venha logo!',[4, 'Urgência na Av. Jobim']],
['Caramba '+CHARACTERS[1]['NAME']+', será que você não entende a gravidade da situação??','Só você pode deter essa anomalia!']]],
    
'926148930': [['E aí mano? Beleza?','Então, aquela parada da transferência deu certo, adivinha?','Amanhã á noite eu tô indo pra Nova Friburgo!',0,'Tá tendo umas paradas estranhas lá, e me mandaram examinar','Vamos aproveitar pra gente se ver, beleza?']],
  
'976564008': [['Agora não, ' + CHARACTERS[0]['NAME'] + '! Eu tô trabalhando!','Me ligue depois, estou fazendo coisa importante aqui!']],
  
'940028922': [['Oh, olá! como vai, '+CHARACTERS[0]['NAME']+'?','Tenho andado ocupada esses dias, muita coisa pra fazer...','Não dá pra falar com você agora, desculpa','Me ligue mais tarde, ok?'],
['oie']],
    
'990271802': [['Garoto, o chefe quer te ver o mais cedo possível na delegacia',1,'Espero que não tenha feito merda...',1,'Bláblabla','blablabla','blablabalbala','blablablaba',1,0,'entendeu?',1]],
    
'987690021': [['Paulo']],
  
'953478809': [[dt + ', em que posso ajudar?',[10,['uma pizza grande','já estamos á caminho',1,[17,'pizza',0,3]],['uma pizza média','já estamos á caminho',1,[17,'pizza',3]]]]],
  
'909236521': [[dt + ', correios']],
  
'923778988': [['Alô?',1,CHARACTERS[0]['NAME'] + '! a quanto tempo cara!',1,'Precisando de ajuda em','carregar algumas coisas?',1,'Não tem problema, o pai tá aí','pra resolver já já!',1,[17,'maicon',0,3]]],
  
'969696969': [['Olá ' + prps + ' cliente, em que posso ajudar?','você está a procura de meus serviços?','chegarei em instantes',1,[17,'mercador',0,3]]],
  
'977904623': [['Hey!','Você está bem?','Onde você tá?','O que tá acontecendo?','Você se machucou?',[10,['Eu tô bem','Mesmo?',1,'Ufa...',1],['Fique calmo','Não consigo me acalmar',1]],'Eu estava preocupado','com você',1,
'mas graças a','Deus você está bem',1,'Aquela mulher chamando','vocês aos prantos me','deixou assustado',1,'Você deve estar','cansada depois de','tudo o que passou',1,'Engraçado, não é?',1,'Você mal saiu','dessa coisa de mercenária',
'e já tá na ativa','novamente',1,'Mas assim...',1,'...',[10,['Pode falar','não...','é que...',1,'Não quero que a gente','se afaste de novo',1,'Não agora que tá','tudo dando muito certo',1,'Não precisa ser','que nem seu amigo','mercenário',1,
'ah é, esqueci','de te contar',1,'Eu fiquei sabendo','dele e tudo isso','sobre aquela garota',1,'bem problemático',1,'Não...',1,'Esquece eu só','falei besteira',1,'Só quero que','você não seja','ausente como eu','fui com você',1,'entende?',1,
[10,['Sim','Ainda bem que','entendeu',1],['Não','Esquece isso',1]]],
['Eu já ligo de volta','Tudo bem','Você deve estar','muito ocupada agora',1]]
,'A gente se fala mais','em casa, então',1,'te amo, ok?',1]],
  
'923578103': [['Sofia']],
  
'960428331': [['Vinícius']],
 
'978543322': [['Oi, em que posso ajudar?','Ah...eu já parei de fazer isso há muitos anos','Tchau']],

#ADVICE
'ADVICE': ['Desculpe interromper','Mas é uma história muito longa','para se contar.',1,'Não vai querer continuar amanhã?','Nós gravamos tudo o que você falou',1,'E então?',[10,['Tudo bem','Ótimo','rapazes, guardem suas coisas'],['Espere um pouco','Tá bom então...','vamos prosseguir']]]
}

DLGSAV = {
'1hauntedhouse_0': [0,0,0,0,0],
'1hauntedhouse_1': [0,0],
'1hauntedhouse_2': [0,0],
'1hauntedhouse_3': [0,0],
}

SIGNS = {
'INN': 'pousada', 'PUB': 'bar', 'HOTEL': 'hotel', 'DRUGSTORE': 'drogaria', 'BAKERY': 'padaria', 'BAZAAR': 'bazar', 'MARKET': 'mercado', 'BANK': 'banco','GAS': 'posto','HOSPITAL': 'hospital',
'POLICE': 'delegacia', 'SHOP': 'loja'
}
    
RADIO = {'0': [],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
  
for i in range(0,10):
    for j in os.listdir('Songs/FM_'+str(i)):
        RADIO[str(i)].append(j)
     
MANUAL = [['CONTROLES',['Aperte ' + pygame.key.name(LEFT) + ', ' + pygame.key.name(RIGHT) + ', ' + pygame.key.name(UP) + ' e ' + pygame.key.name(DOWN) + ' para mover seu personagem']],\
['CELULAR',['O celular é o equivalente ao','menu do jogo, acesse-o','apertando ' + pygame.key.name(PHONE) + '.','\
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
    
BATTLE = [' aparece no caminho!',' encurrala você!',' é emboscado!',
'incrível!','errou...','outra vez!',
'vitória!','perfeito!','derrota...','acertos: ','dano total: ','vitalidade perdida: ','bônus de tempo: ',' de experiência',
' foi promovido para o nível ',
' tentou fugir','...mas falhou','...e consegue!',
' vai ',' usa ',' perdeu ',' ganhou ',' de ATAQUE',' de AGIIDADE',' de FORÇA','de RESISTÊNCIA',
' está com resfriado',' está com febre',' está desidratado',' está com náusea',' não consegue se mexer!',' está inconsciente...',' foi atacado por um parasita',
' está queimando!',' foi envenenado!',' está com hemorragia!',
' foi quebrado...',
' entrou na batalha!', 'Mas não funcionou...',
'força','ataque','agilidade','resistência','vitalidade',
'Um exército aparece para te atacar!','maravilhoso!']
  
MENU = ['mapa','chamadas','correios','notícias','rádio','câmera','bestiário','tarefas','status','táticas','conquistas','placar','manual','ajustes','sobre',
'sem conexão','não há contatos','sem créditos...','sem dinheiro...','não há mensagens','sem sinal','nenhuma anomalia registrada','não há tarefas',
'grupos','contatos','histórico','novas','lidas','todas','fazer','feitas','novo grupo',
'créditos: ','chamando...','DE: ','PARA: ','nova tática','VITALIDADE: ','FORÇA: ','ATAQUE: ','AGILIDADE: ','RESISTÊNCIA:',
'RESFRIADO','FEBRE','SEDE','NÁUSEA','PARALISIA','INCONSCIÊNCIA','PARASITA','QUEIMADURA','VENENO','HEMORRAGIA','REFORÇOS','ROUBAR',
'equipamento 1','equipamento 2','equipamento 3','equipamento 4','dialogar','defender','fugir','nova história',
'idioma','sfx','música','mover cima','mover baixo','mover esquerda','mover direita','ato','celular','inventário','velocidade','cor R','cor G','cor B','salvar',
'escolha um botão','volume','peso','Nome','Sobrenome','Tudo certo?','Sim','Não','Tem certeza?','correr','borda','gameplay','áudio','controles','muito lento','lento','médio','rápido','muito rápido']
  
ABOUT = ['MUTATION PURGE','Criado por Matt Kai','Source code por Matt Kai','Feito em Python','Twitter','GitHub','GNU General Public License']
  
SHOP = ['comprar','sair','nada aqui','banco: $','dinheiro: $','sacar','depositar','cancelar','Mercador','vender']
  
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
['Temos um Xeroque Holmes','Complete o esqueleto de todas as anomalias',0,''],
   
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