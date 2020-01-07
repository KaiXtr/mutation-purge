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
 
import pygame
import os
  
MAP = 'city'
PX = 1276
PY = 1609
TIME = [0,0,0]
DATE = [0,0,0]
SCENE = 0
 
CHAPTERS = ['Duplo Andantes','Quadro por Quadro','Fale Comigo','Lá se vai de novo','Eu quero ser seu']
  
SPRITES = {'UP_Sid': [pygame.image.load('Sprites/hero_walkU_0.png'), pygame.image.load('Sprites/hero_walkU_1.png'), pygame.image.load('Sprites/hero_walkU_2.png'), pygame.image.load('Sprites/hero_walkU_3.png')],\
'DOWN_Sid': [pygame.image.load('Sprites/hero_walkD_0.png'), pygame.image.load('Sprites/hero_walkD_1.png'), pygame.image.load('Sprites/hero_walkD_2.png'), pygame.image.load('Sprites/hero_walkD_3.png')],\
'LEFT_Sid': [pygame.image.load('Sprites/hero_walkL_0.png'), pygame.image.load('Sprites/hero_walkL_1.png'), pygame.image.load('Sprites/hero_walkL_2.png'), pygame.image.load('Sprites/hero_walkL_3.png')],\
'RIGHT_Sid': [pygame.image.load('Sprites/hero_walkR_0.png'), pygame.image.load('Sprites/hero_walkR_1.png'), pygame.image.load('Sprites/hero_walkR_2.png'), pygame.image.load('Sprites/hero_walkR_3.png')]}
  
CHARACTERS = [
{'NAME': 'Sidney','LASTNAME': 'Barreto','GENDER': 'male','ID': '0064','BLOOD': 'A+','CIVIL': 'solteiro','CLASS': 'gunslinger','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [10,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],\
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]},\
 \
{'NAME': 'Jane', 'LASTNAME': 'Oliveira','GENDER': 'female','ID': '0094','BLOOD': 'O-','CIVIL': 'casada','CLASS': 'rifler','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],\
'AGILITY': [1,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]},\
 \
{'NAME': 'Renan', 'LASTNAME': 'Pinheiro','GENDER': 'male','ID': '0042','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'thief','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [20,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],\
'AGILITY': [2,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0,1,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]},\
 \
{'NAME': 'Lúcia', 'LASTNAME': 'Figueiredo','GENDER': 'female','ID': '0013','BLOOD': 'O+','CIVIL': 'viúva','CLASS': 'sniper','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],\
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]},\
 \
{'NAME': 'Diego', 'LASTNAME': 'Donovan','GENDER': 'male','ID': '0120','BLOOD': 'A-','CIVIL': 'solteiro','CLASS': 'gunslinger','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],\
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]},\
 \
{'NAME': 'Bianca', 'LASTNAME': 'Pacheco','GENDER': 'female','ID': '0022','BLOOD': 'O+','CIVIL': 'casada','CLASS': 'doctor','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],\
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]},\
 \
{'NAME': 'Pietra', 'LASTNAME': 'Mendonça','GENDER': 'female','ID': '0150','BLOOD': 'A+','CIVIL': 'solteira','CLASS': 'gunslinger','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],\
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]},\
 \
{'NAME': 'Paulo', 'LASTNAME': 'Sousa','GENDER': 'male','ID': '0001','BLOOD': 'O-','CIVIL': 'casado','CLASS': 'sniper','LEVEL': 0,'HP': 10,'BARHP': 10,'MAXHP': 10,'XP': 0,'MAXXP': 100,'HEALTH': 0,\
'STRENGHT': [0,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5],\
'ATTACK': [30,5,5,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,9],\
'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1,1,1,1.25,1.25,1.5,1.5,1.5,1.5,1.75],\
'RESISTANCE': [0.25,2,2,2,2,2.25,2.25,2.25,2.25,2.25,2.5,2.5,2.5,2.5,2.5,2.75,2.75,2.75,2.75,2.75,3]}
]
 
PLAYER = [CHARACTERS[0].copy(),CHARACTERS[4].copy()]
  
ATM = 0
MONEY = 200
CREDIT = 10
BATTERY = 3
GAS = 100.0
  
FREAKS = [
#ANOMALIES
{'NAME': 'Madladcat','INFO': ['É um felino sobrenatural que','flutua como um fantasma.','Pequeno e ágil, porém bem frágil.'],'HEIGHT': '0,80','HABITAT': 'jungle','TYPE': 'mammal','AGILITY': 5,'HP': 8,'RESISTANCE': 0,
'HABILITIES': [['Morder',['O felino morde o oponente.'],-4,1],['Ataque de fofura',['O felino mostra sua fofura,','fazendo o ATAQUE do oponente','abaixar.'],-1,2],
['Invisibilidade',['O felino fica intransponível, assim','o oponente é impossibilitado','de acertá-lo por um turno.'],-5,3],['Assustar',['O felino assusta o oponente','fazendo seu ATAQUE cair.'],-3,2]]},
 
{'NAME': 'Lula Torpedo','INFO': 'Um molusco que antige seus oponentes como um torpedo. Apesar de enorme, forte e resistente, se locomove muito devagar.','HEIGHT': '2,10','HABITAT': 'sea','TYPE': 'aquatic','AGILITY': 1,'HP': 50,'RESISTANCE': 1,
'HABILITIES': [['Tentáculos','O molusco usa seus tentáculos para atacar seu oponente.',-5,1],['Jato de tinta','O molusco atira um jato de tinta que impossibilita o oponente de atacar.',-5,3],
['Camuflagem','O molusco se disfarça no ambiente, aumentando sua AGILIDADE.',2,3],['Torpedo','O molusco acerta o oponente com um ataque explosivo que acerta todos á volta, super efetivo.',-15,1]]},
 
{'NAME': 'Pombo Pavão','INFO': 'Um pombo urbano com uma mutação que o fez desenvolver penas de pavão com olhos reais nas suas pontas. Relativamente ágil, mas fraco.','HEIGHT': '0,25','HABITAT': 'urban','TYPE': 'flying','AGILITY': 3,'HP': 10,'RESISTANCE': 1,
'HP': 10,'HABILITIES': [['Defecar','A ave defeca no oponente, infectando-o.',1,4],['Hipnose','A ave hipnotiza o oponente com os olhos das penas de pavão, diminuindo sua AGILIDADE',-2,3],
['Bicar','A ave bica o oponente',-4,1],['Gritar','A ave grita, com a possibilidade de outra anomalia entrar na batalha.',0,5]]},
 
{'NAME': 'Jaré','INFO': 'Um réptil que, graças á uma sílaba a menos em seu nome, perdeu dois de seus membros. Não muito ágil, mas causa muito dano.','HEIGHT': '1,90','HABITAT': 'swamp','TYPE': 'reptile','AGILITY': 2,'HP': 13,'RESISTANCE': 1,
'HABILITIES': [['Morder','O réptil morde seu oponente',-6,1],['Esperar','O réptil aumenta seu ATAQUE.',1,2],['Bote','O réptil ataca com uma mordida em avanço.',-5,1],
['Esconder','O réptil se esconde no ambiente, aumentando sua AGILIDADE',1,3]]},
 
{'NAME': 'Lata Alada','INFO': 'Uma lata de energético que tenta ser irada e tem o único atributo que prometeu dar á quem o consumisse. É literalmente uma piada.','HEIGHT': '0,15','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 3,'HP': 5,'RESISTANCE': 1,
'HABILITIES': [['Voar','Aumenta sua agilidade',1,3],['Energizar','Aumenta seu dano de arremesso',2,2],['Ressaca','A lata se auto destrói',-0,1],
['Arremessar','A lata se joga no oponente, se machucando junto',1,1]]},

{'NAME': 'Cacho de Olhos','INFO': 'Vários olhos diferentes agrupados que possuem poderes hipnóticos. PS: NÃO É GUARANÁ, NÃO FAÇA SUCO.','HEIGHT': '0,30','HABITAT': 'jungle','TYPE': 'plant','AGILITY': 2,'HP': 20,'RESISTANCE': 1,
'HABILITIES':[['Encarar','Os olhos começam a encarar o oponente, amedrontando-o e fazendo seu ATAQUE abaixar.',-1,2],['Atirar','Um dos olhos se lança no oponente.',-3,1],
['Plantar','Um olho se planta no chão com a possibilidade de germinar um novo cacho.',0,5],['Explodir','Todos os olhos se soltam num ataque fulminante.',-7,1]]},
 
{'NAME': 'Perereca Mil Grau','INFO': 'Um anfíbio que saiu da metamorfose antes da hora e ao mesmo tempo que manteve a cauda, desenvolveu braços fortes.','HEIGHT': '0,70','HABITAT': 'jungle','TYPE': 'aquatic','AGILITY': 2,'HP': 20,'RESISTANCE': 1,
'HABILITIES':[['Língua','O anfíbio usa sua língua para chicotear o oponente.',-5,1],['Porrada','O anfíbio usa seus braços musculosos para bater no oponente.',-8,1],
['Veneno','O anfíbio libera toxinas nas bolsas das suas costas para infectar o oponente.',1,4],['Salto','O anfíbio pula pelo ambiente e aumenta sua AGILIDADE',2,3]]},
 
{'NAME': 'Cremado Cremoso','INFO': 'Um homem que sofreu uma combustão espontânea mas continua vivo graças á mutação.','HEIGHT': '1,70','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 5,'HP': 18,'RESISTANCE': 1,
'HABILITIES': [['Bater','O indivíduo bate no oponente.',-5,1],['Cinzas','O indivíduo joga cinzas no oponente, abaixando sua AGILIDADE.',-3,3],
['Dançar','O indivíduo começa a rebolar e mostrar seu charme.',0,6],['Infectar','O indivíduo entra dentro do oponente através das cinzas, diminuindo seu ATAQUE.',-3,2]]},
 
{'NAME': 'Biscoito Crucificado','INFO': 'Esse ser humano não está em um estado muito bacana...É um biscoito de gengibre possuído preso num crucifixo, parece até coisa de algum filme B!','HEIGHT': '0,30','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 8,'HP': 30,'RESISTANCE': 1,
'HABILITIES': [['Chantily','O possuído jorra chantily venenoso no oponente.',1,4],['Gargalhar','O possuído ri de uma maneira terrorífica, diminuindo o ATAQUE do oponente.',-2,2],
['Bater','O possuído usa seu crucifixo para atacar o oponente.',-8,1],['Perfurar','O possuído perfura o corpo do oponente usando o crucifixo',-10,1]]},
 
{'NAME': 'EMO HIPSTER','INFO': 'A DDA ainda não sabe se esse ser é uma anomalia ou apenas um cara estranho que chegou e parece não achar lugar no corpo que Deus encarnou.','HEIGHT': '1,60','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 4,'HP': 20,'RESISTANCE': 1,
'HABILITIES': [['Cantar','O esquisito começa a cantar uma música dos los hermanos com uma guitarra.',1,4],['Guitarrada','O esquisito usa sua guitarra para atacar o oponente.',-10,1],
['Óculos sem lente','O esquisito põe óculos sem lente para confundir o oponente, abaixando sua AGILIDADE.',-1,3],['Franja','O esquisito balança sua franja, aumentando seu ATAQUE.',2,2]]},
 
{'NAME': 'Peixe Galã','INFO': 'Um peixe que abre a boca acima dos limites de sua mandíbula e da biologia, pelo menos ele é admirável.','HEIGHT': '1,20','HABITAT': 'swamp','TYPE': 'aquatic','AGILITY': 5,'HP': 25,'RESISTANCE': 1,
'HABILITIES': [['Aumentar','O peixe aumenta o tamanho da sua face e volta ao normal, assustando o oponente e abaixando seu ATAQUE',-2,2],
['Saltar','O peixe salta na água e chicoteia o oponente com sua cauda',-7,1],['Morder','O peixe morde o oponente com seus dentes limpos e branquinhos.',-9,1],
['Brilhar','O peixe reflete a luz do sol cegando o oponente.',2,4]]},
 
{'NAME': 'Pé de moleque','INFO': 'É um doce de amendoim delicioso muito comum em festas juninas...não pera. É um membro que se separou do corpo humano e agora consegue viver por conta própria, não co fundir com mãozinha da Família Adams.','HEIGHT': '0,80','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': [['Pisar','O membro pisa no oponente com toda sua força.',-10,1],['Chutar','O membro chuta o oponente, mesmo perdendo seu equilíbrio.',-12,1],
['Cura','O membro se cura utilizando uma técnica que não entendemos devido ás limitações de seu corpo.',10,1],['Agachar','O membro concentra a energia dos seus pés e aumenta seu ATAQUE.',5,2]]},
 
{'NAME': 'Flamingo Flamenguista','INFO': 'Uma ave com a peculiaridade de ter a anomalia FLAMENGO.','HEIGHT': '1,20','HABITAT': 'swamp','TYPE': 'flying','AGILITY': 7,'HP': 33,'RESISTANCE': 1,
'HABILITIES': [['Bolada','A ave chuta uma bola na face do oponente.',-13,1],['Dibre','Lamentamos o erro de ortografia de Sidney, a ave dribla o oponente fazendo sua AGILIDADE aumentar.',3,2],
['Rasteira','A ave ataca o oponente se jogando no chão e derrubando-o.',-10,1],['Gabigol','A ave recruta o profissional jogador de futebol GABIGOL, ganhando a batalha imediatamente.',-50,1]]},
 
{'NAME': 'Belle Dolphine','INFO': 'Fruto de uma relação entre uma E-Girl e o Boto.','HEIGHT': '2,10','HABITAT': 'jungle','TYPE': 'aquatic','AGILITY': 7,'HP': 42,'RESISTANCE': 1,
'HABILITIES': [['Ahegao','O mamífero tenta sensualizar o oponente simulando um ato sexual, mas faz o efeito contrário abaixando seu ATAQUE',-3,2],['Água de banho','O mamífero oferece água de banho para o oponente, este o ingere e obtém HERPES.',2,4],
['Nadar','O mamífero nada no ambiente para recuperar sua VITALIDADE.',10,1],['Canto submarino','O mamífero entoa uma canção para chamar uma anomalia para a batalha.',1,5]]},
 
{'NAME': 'Tarsila','INFO': 'Um auto retrato da pintora Tarsila do Amaral, te encarando pronta pra acabar com sua raça. Óleo sobre tela.','HEIGHT': '2,20','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 5,'HP': 30,'RESISTANCE': 1,
'HABILITIES': [['Atacar','A pintura se joga contra o oponente, machucando a si no processo.',-10,1]]},
 
#CHEFES
{'NAME': 'Lula Torpedo','INFO': 'Um molusco que antige seus oponentes como um torpedo. Apesar de enorme, forte e resistente, se locomove muito devagar.','HEIGHT': '2,10','HABITAT': 'sea','TYPE': 'aquatic','AGILITY': 1,'HP': 50,'RESISTANCE': 1,
'HABILITIES': [['Tentáculos','O molusco usa seus tentáculos para atacar seu oponente.',-5,1],['Jato de tinta','O molusco atira um jato de tinta que impossibilita o oponente de atacar.',-5,3],
['Camuflagem','O molusco se disfarça no ambiente, aumentando sua AGILIDADE.',2,3],['Torpedo','O molusco acerta o oponente com um ataque explosivo que acerta todos á volta, super efetivo.',-15,1]]},
 
{'NAME': 'Abaporu','INFO': 'Uma pintura modernista que criou vida própria e por sinal é canibal.','HEIGHT': '2,20','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 7,'HP': 75,'RESISTANCE': 1,
'HABILITIES': [['Pisar','A pintura pisa no oponente esmagando-o.',-13,1],['Fúria','A pintura grita furiosamente aumentando seu ATAQUE.',3,2],
['Proteger','A pintura reforça sua proteção de acrílico sobre a tela',1,6],['Reforço','A pintura chama outra pintura para ajudar na batalha.',1,5]]},
 
{'NAME': 'Xaruto','INFO': 'Estranhamente lembra um personagem de um anime que não é tão bom quanto Evangelion.','HEIGHT': '0,10','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 20,'HP': 1,'RESISTANCE': 1,
'HABILITIES': [['Fumaça ninja','O elemento solta uma fumaça com mais de 100.000 substâncias tóxicas incluindo nicotina e enxofre, envenenando o oponente.',1,4],['Chama ninja','O elemento sopra uma labareda ardente, incendiando o oponente.',3,4],
['Xaringan','O elemento usa uma espécime de energia oculta para aumentar seu ATAQUE.',10,2],['Vaporizar','O elemento se transforma num cigarro eletrônico, relaxando e diminuindo sua AGILIDADE.',-10,-2]]},
 
{'NAME': 'Cesariana','INFO': 'Um feto dentro de uma bolha numa cesariana com poderes psíquicos.','HEIGHT': '1,00','HABITAT': 'urban','TYPE': 'psychic','AGILITY': 2,'HP': 10,'RESISTANCE': 1,
'HABILITIES': [['Escudo','O feto reforça a resistência da bolha.',1,6],['Cordão Umbilical','O feto drena a energia de sua hospedeira e recupera sua VITALIDADE.',10,1],
['Grito molecular','O feto grita em um nível estratosféricamente alto, agitando as moléculas de seus oponentes.',-15,1],['Líquido Uterino','O feto arremesa o líquido uterino da bolha nos oponentes, confundindo-os e dando NÁUSEA.',2,4]]},
 
#MERCENARIES
{'NAME': 'Vinícius','HABITAT': 'urban','TYPE': 'humanoid','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'HABILITIES': [['Atirar',-8,1],['Granada',-20,1]]},
 
#OTHER
{'NAME': 'Alvo','HABITAT': 'urban','TYPE': 'inorganic','AGILITY': 2,'HP': 30,'RESISTANCE': 2,'HABILITIES': [['Fazer nada',-2,1]]},
 
]
 
BESTIARY = []
 
TACTICAL = [[1,6],[2,7]]
  
#MOCHILAS
ITEMS = [
['bolsinha',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 2x2.'],1000,0,22],
['bolsa',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 3x2.'],2500,0,32],
['mochila',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 3x3.'],5000,0,33],
['mochila de viagem',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 3x4.'],7500,0,34],
['mochilão',['Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 4x4.'],10000,0,44],
#ROUPAS
['colete',['Ao equipá-lo você diminui o dano tomado pelos seus inimigos em 3'],120,1,3],
['blindagem',['Ao equipá-lo você diminui o dano tomado pelos seus inimigos em 6'],400,1,6],
#MUNIÇÃO
['tranquilizante',['Munição para pistola que faz o inimigo adormecer.'],100,0],
['munição.16',['Munição para pistola de calibre 16, use no meio de uma batalha','para recarregá-la.'],200,2,0],
['munição.38',['Munição para pistola de calibre 38, use no meio de uma batalha','para recarregá-la.'],300,2,1],
['munição.42',['Munição para pistola de calibre 42, use no meio de uma batalha','para recarregá-la.'],400,2,2],
['munição de bazuca',['Munição para basuca, use no meio de uma batalha','para recarregá-la.'],800,2,3],
#ITENS DE BATALHA
['granada',['Use numa batalha para causar dano á todos os inimigos na tela.'],100,3],
['granada de fumaça',['Use numa batalha para que todos os inimigos percam AGILIDADE.'],200,3],
['granada de luz',['Use numa batalha para que todos os inimigos percam sua vez.'],500,3],
['spray de pimenta',['Use numa batalha para atordoar um inimigo.'],40,3],
#REMÉDIOS
['antibiótico',['Use para infeccionar feridas letais e impedir hemorragias, parando de consumir a barra de HP.'],25,4],
['xarope',['Remédio utilizado para combater resfriados e alergias.'],10,4,1],
['comprimidos',['Remédios utilizados para combater náusea.'],30,4,2],
['pílulas',['Remédios utilizados para combater dor muscular.'],40,4,3],
['adrenalina',['Remédio utilizado para reviver uma pessoa inconsciente.'],60,4,5],
#ARMAS BRANCAS
['faca',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],800,5,{'DAMAGE': 5, 'RECHARGE': 0, 'CAPACITY': 0}],
['peixeira',['Útil para ataques corpo-a-corpo, pode ser tão letal','quanto uma arma de fogo.'],1000,5,{'DAMAGE': 8, 'RECHARGE': 0, 'CAPACITY': 0}],
#ARMAS DE FOGO
['revólver',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],2000,5,{'DAMAGE': 4, 'RECHARGE': 3, 'CAPACITY': 3}],
['pistola',['Arma de fogo para ataques de média distância, ela usa munição de calibre 38.'],2500,5,{'DAMAGE': 4, 'RECHARGE': 1, 'CAPACITY': 8}],
['UZI',['Arma de fogo para ataques de média distância, ela usa munição de calibre 16.'],4000,5,{'DAMAGE': 4,'RECHARGE': 0.5,'CAPACITY': 20}],
['carabina',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['sniper',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],6000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['escopeta',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],4000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['fuzil de assalto',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],4000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['fuzil',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['lança granadas',['Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.'],5000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
['bazuca',['Arma de fogo para ataques de longa distância, ela usa munição de basuca.'],12000,5,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],
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
#SUPLEMENTOS
['suplemento de ataque',['Aumenta o ATAQUE permanentemente em +1.'],50,10,0],
['suplemento de agilidade',['Aumenta a AGILIDADE permanentemente em +1.'],50,10,1],
['suplemento de resistência',['Aumenta a RESISTÊNCIA permanentemente em +1.'],50,10,2],
['suplemento de vitalidade',['Aumenta a VITALIDADE MÁXIMA em +5'],50,10,3],
#REPELENTES
['repelente básico',['Evita anomalias de aparecer por 1 minuto.'],50,11,3600],
['super repelente',['Evita anomalias de aparecer por 3 minutos.'],100,11,10800],
['ultra repelente',['Evita anomalias de aparecer por 7 minutos.'],250,11,25200],
#ACESSÓRIOS
['mira laser',['Melhora a PRECISÃO de um fuzil ou metralhadora.'],200,12,0],
['mira laser',['Melhora a PRECISÃO de um fuzil ou metralhadora.'],200,12,0],
#TESOUROS
['vaso marajoara',['Um antigo vaso indígena feita da cerâmica do marajó.'],2000,13,0],
]
 
EQUIPMENT = [
[['pistola',{'DAMAGE': 3, 'CADENCY': 1, 'CAPACITY': 8},[]],['carabina',{'DAMAGE': 7, 'CADENCY': 3, 'CAPACITY': 3},[]],'_','_'],
[['pistola',{'DAMAGE': 3, 'CADENCY': 1, 'CAPACITY': 8},[]],['carabina',{'DAMAGE': 7, 'CADENCY': 3, 'CAPACITY': 3},[]],'_','_'],
]
  
INVENTORY = [['_',['_','_','_'],['_','_','_'],['_','_','_'],['_','_','_']],['_',['_','_'],['_','_']]]
 
VEHICLES = {
'moto_0': {'SPEED': 8, 'ACCELERATION': 0.5, 'CAPACITY': 100, 'GAS': 0.075, 'LIGHTS': 2, 'DIRECTION': 1},
'moto_1': {'SPEED': 10, 'ACCELERATION': 0.25, 'CAPACITY': 100, 'GAS': 0.05, 'LIGHTS': 1, 'DIRECTION': 1}
}
  
def load_game(slt):
    global MAP, PX, PY, ATM, MONEY, CREDIT, BATTERY
    file=open(str(slt)+'userdata.db','r')
    step=0
    dct=''
    x=0
    y=0
    z=0
    SCENE = file.readline()[0:-1]
    TIME[0] = int(file.readline()[0:-1])
    TIME[1] = int(file.readline()[0:-1])
    for line in file:
        if line=='-\n':step+=1
        if step==0:
            d=0
            for i in line:
                if i==':':break
                else:d+=1
            k=line[0:d]
            v=line[d+2:len(line)-1]
            try:v=int(v)
            except:pass
            PLAYER[0][k]=v
        elif step==1:
            MAP = file.readline()[0:-1]
            PX = int(file.readline()[0:-1])
            PY = int(file.readline()[0:-1])
            DATE[0] = int(file.readline()[0:-1])
            DATE[1] = int(file.readline()[0:-1])
            ATM = int(file.readline()[0:-1])
            MONEY = int(file.readline()[0:-1])
            CREDIT = int(file.readline()[0:-1])
            BATTERY = int(file.readline()[0:-1])
            GAS = float(file.readline()[0:-1])
        elif step==2:
            if line!='-\n':
                if y==0:
                    INVENTORY[x][y]=line[0:-1]
                    y+=1
                else:
                    INVENTORY[x][y][z]=line[0:-1]
                    z+=1
                if z==len(INVENTORY[x][y]):
                    z=0
                    y+=1
                if y==len(INVENTORY[x]):
                    y=0
                    x+=1
                if x==len(INVENTORY):
                    x=0
                    y=0
                    z=0
        elif step==3:
            if line!='-\n':
                EQUIPMENT[x][y]=[line[0:-1]]
                for i in ITEMS:
                    if i[0]==line[0:-1]:    
                        EQUIPMENT[x][y].append(i[3])
                y+=1
                if y==len(EQUIPMENT[x]):
                    y=0
                    x+=1
                if x==len(EQUIPMENT):
                    x=0
                    y=0
  
    file.close()
  
load_game(1)
  
def save_game(slt):
    file=open(str(slt) + 'userdata.db','w')
    file.write(str(SCENE) + '\n')
    file.write(str(TIME[0]) + '\n')
    file.write(str(TIME[1]) + '\n')
    for l in PLAYER[0]:
        if l=='ATTACK': break
        file.write(l+': ' + str(PLAYER[0][l]) + '\n')
    file.write('-\n')
    file.write(MAP + '\n')
    file.write(str(PX) + '\n')
    file.write(str(PY) + '\n')
    file.write(str(DATE[0]) + '\n')
    file.write(str(DATE[1]) + '\n')
    file.write(str(ATM) + '\n')
    file.write(str(MONEY) + '\n')
    file.write(str(CREDIT) + '\n')
    file.write(str(BATTERY) + '\n')
    file.write(str(GAS) + '\n')
    file.write('-\n')
    for l in INVENTORY:
        for j in l:
            if l[0]==j:
                file.write(j + '\n')
                continue
            for i in j:
                file.write(i + '\n')
    file.close()
     
s = Settings()
 
CONTACTS = [['Sidney','989074454'],['Lúcia','990271802'],['Renan','990435671'],['Pietra','940028922'],['Paulo','987690021'],['Jane','991124257'],['Bianca','976564008'],['Diego','926148930'],
['Pizza Delivery','953478809'],['Correios','909236521'],['Maicon','923778988'],['Mercador','969696969'],['Iago','977904623'],['Sofia','923578103'],['Vinícius','960428331']]
  
CALLHIST = [['990271802',True]]
  
EMAILS = [['ddarj@cmail.com','Hello World!',
['This is a test'],
True],

['cangaceirostv@cmail.com','Proposta de entrevista',
['Boas novas, ' + PLAYER[0]['NAME'] + ' ' + PLAYER[0]['LASTNAME'] + '.',
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

if PLAYER[0]['GENDER'] == 'male': gn='Moço'
elif PLAYER[0]['GENDER'] == 'female': gn='Moça'
else: gn='Moçe'
 
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
#PLACES
'CASHIER': [['Os produtos estão nas pratileiras','é só você ir pegar e trazer aqui',0,'O quê? você quer que eu vá buscar pra você?!']],
 
'FARMACEUTIC': [['Não sabe que remédios comprar?',[10,['Não...','O que você quer tratar?',[10,['Resfriados e alergias','Se você estiver sentindo algum resfriado,','gripe, tontura ou fraqueza, um\
 simples','xarope já basta'],['Infecções e hemorragias','Esses são problemas fortes, mas não muito graves','Para infecções, use o antibiótico correspondente ao tipo de','contaminação.',0,'Se tiver\
  hemorragias, primeiro cicatrize a ferida','e depois ponha um band-aid para','evitar mais saída de sangue'],['Contaminação e Mal-estar','Caso se sinta alguma coisa parecida, pode ser','sinal de envenenamento ou\
   intoxicação, existem','várias pílulas para diversos tipos de tóxicos']],'Mais alguma pergunta?',[12]],['Tô de boa','Tudo bem','Se tiver alguma dúvida é só perguntar','Fique á vontade']]]],
    
'SECURITY': [['Ponha qualquer objeto de metal que tiver','na caixa ao lado']],
 
'HOTEL ATTENDANT': [['Bom dia!','O que deseja?',[10,['Uma noite apenas','O custo é de 20 por pessoa',[10,['Ok','Aqui, seu quarto é o N° 902',[0,'chave',20]],['Deixa pra lá','Volte a hora que quiser']]],
['Estou apenas olhando','Sinta-se á vontade']]]],
 
'NURSE': [['Você deveria se cuidar mais','É muito comum te ver por aqui']],
 
#ENEMIES
'IRRATIONAL': ['A anomalia não entende nada do que você tá falando'],
'Cremado Cremoso': [[10,['Cê tá bem mano?','Claro que não né?? Estou queimando feito palha nessa desgraça!'],['Vaza ou meto chumbo','Eu não tenho medo de você'],['A gente não quer nada contigo',
'Mas eu quero','Preciso de sangue!!']]],
 
#CONTACTS CALL
'989074454': [['Sidney']],
 
'991124257': [['Oi! Sou eu, a Jane']],
'990435671': [[[CHARACTERS[1]['NAME']+'! Precisamos de você aqui AGORA!','Eu sei que você saiu e coisa e tal, mas a gente PRECISA DE VOCÊ!','Estamos na Av. Jobim, venha logo!',[4, 'Urgência na Av. Jobim']],
['Caramba '+CHARACTERS[1]['NAME']+', será que você não entende a gravidade da situação??','Só você pode deter essa anomalia!']]],
 
'926148930': [['E aí mano? Beleza?','Então, aquela parada da transferência deu certo, adivinha?','Amanhã á noite eu tô indo pra Nova Friburgo!',0,'Tá tendo umas paradas estranhas lá, e me mandaram examinar','Vamos aproveitar pra gente se ver, beleza?']],
 
'940028922': [['Oh, olá! como vai, '+CHARACTERS[0]['NAME']+'?','Tenho andado ocupada esses dias, muita coisa pra fazer...','Não dá pra falar com você agora, desculpa','Me ligue mais tarde, ok?'],
['oie']],
 
'990271802': [['Garoto, o chefe quer te ver o mais cedo possível na delegacia','Espero que não tenha feito merda...']],
 
'987690021': [['Paulo']],
 
#CITIZENS DIALOG
'WORRIED MAN': [[[10,['O que está havendo?','Eu não faço idéia!'],['Estou com eles','Oh, desculpe...',[8,1,1]]]]],
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
 
'BIANCA': [['Hey ' + PLAYER[0]['NAME'] + ', fique com essa lupa, Eu fiz ela apenas para pesquisar anomalias.','Quando enfrentar uma anomalia que não está registrada no bestiário,','Use-a para registrar a anomalia.',[0,'lupa']]],
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
['1',['sex','23'],['sab','20'],['dom','18'],['seg','17'],['ter','19']],
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
  
MANUAL = [['CONTROLES',['Aperte '+s.left+', '+s.right+', '+s.up+' e '+s.down+' para mover seu personagem']],\
['CELULAR',['O celular é o equivalente ao','menu do jogo, acesse-o','apertando ' + s.phone+'.','\
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

ACHIEVEMENTS = [
['Conquistador','Ganhar todos os troféus',False]
]