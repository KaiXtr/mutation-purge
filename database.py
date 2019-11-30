SETTINGS = {'SFX': 100,'MUSIC': 100,'UP': 'W','DOWN': 'S','LEFT': 'A','RIGHT': 'D','ACT': 'J','LANGUAGE': 'PT','SPEED': 2,'STYLE': 'GREEN'}

PLAYER = ['','']

PLAYER[0] = {'NAME': 'Sidney','LASTNAME': 'Barreto','GENDER': 'male','LEVEL': 0,'HP': 80, 'MAXHP': 100,'XP': 1,'MAXXP': 100,'HEALTH': 0,\
'ATTACK': [3,4],'AGILITY': [2,2],'RESISTANCE': [2,2.5]}

PLAYER[1] = {'NAME': 'Sandra', 'LASTNAME': 'Oliveira','GENDER': 'female','LEVEL': 0,'HP': 80, 'MAXHP': 100,'XP': 1,'MAXXP': 100,'HEALTH': 0,\
'ATTACK': [0,5,5,5,6,6,8,8,8,8,8,10],'AGILITY': [0,0.25,0.25,0.5,0.5,0.5,0.5,0.75],'RESISTANCE': [2,2.5]}

ATM = 300
MONEY = 200
CREDIT = 10

FREAKS = [{'NAME': 'Madladcat','INFO': 'É um felino sobrenatural que flutua como um fantasma. Pequeno e ágil, porém bem frágil.','HEIGHT': '0,80','AGILITY': 5,'MAXHP': 8,\
'HABILITIES': [['Morder','O felino morde o oponente.',-3,1],['Ataque de fofura','O felino mostra sua fofura fazendo o ATAQUE do oponente abaixar.',-1,2],\
['Invisibilidade','O felino fica intransponível, assim o oponente é impossibilitado de acertá-lo por um turno.',-5,3],['Assustar','O felino assusta o oponente fazendo seu ATAQUE cair.',-3,2]]},\
\
{'NAME': 'Lula Torpedo','INFO': 'Um molusco que antige seus oponentes como um torpedo. Apesar de enorme, forte e resistente, se locomove muito devagar.','HEIGHT': '2,10','AGILITY': 1,'MAXHP': 50,\
'HABILITIES': [['Tentáculos','O molusco usa seus tentáculos para atacar seu oponente.',-5,1],['Jato de tinta','O molusco atira um jato de tinta que impossibilita o oponente de atacar.',-5,3],\
['Camuflagem','O molusco se disfarça no ambiente, aumentando sua AGILIDADE.',2,3],['Torpedo','O molusco acerta o oponente com um ataque explosivo que acerta todos á volta, super efetivo.',-15,1]]},\
\
{'NAME': 'Pombo Pavão','INFO': 'Um pombo urbano com uma mutação que o fez desenvolver penas de pavão com olhos reais nas suas pontas. Relativamente ágil, mas fraco.','HEIGHT': '0,25','AGILITY': 3,\
'MAXHP': 10,'HABILITIES': [['Defecar','A ave defeca no oponente, infectando-o.',1,4],['Hipnose','A ave hipnotiza o oponente com os olhos das penas de pavão, diminuindo sua AGILIDADE',-2,3],\
['Bicar','A ave bica o oponente',-3,1],['Gritar','A ave grita, com a possibilidade de outra anomalia entrar na batalha.',0,5]]},\
\
{'NAME': 'Jaré','INFO': 'Um réptil que, graças á uma sílaba a menos em seu nome, perdeu dois de seus membros. Não muito ágil, mas causa muito dano.','HEIGHT': '1,90','AGILITY': 2,'MAXHP': 13,\
'HABILITIES': [['Morder','O réptil morde seu oponente',-6,1],['Esperar','O réptil aumenta seu ATAQUE.',1,2],['Bote','O réptil ataca com uma mordida em avanço.',-5,1],\
['Esconder','O réptil se esconde no ambiente, aumentando sua AGILIDADE',1,3]]},\
\
{'NAME': 'Lata Alada','INFO': 'Uma lata de energético que tenta ser irada e tem o único atributo que prometeu dar á quem o consumisse. É literalmente uma piada.','HEIGHT': '0,15','AGILITY': 3,'MAXHP': 5,\
'HABILITIES': [['Voar','Aumenta sua agilidade',1,3],['Energizar','Aumenta seu dano de arremesso',2,2],['Ressaca','A lata se auto destrói',-0,1],\
['Arremessar','A lata se joga no oponente, se machucando junto',1,1]]},\
\
{'NAME': 'Cacho de Olhos','INFO': 'Vários olhos diferentes agrupados que possuem poderes hipnóticos. PS: NÃO É GUARANÁ, NÃO FAÇA SUCO.','HEIGHT': '0,30','AGILITY': 2,'MAXHP': 20,\
'HABILITIES':[['Encarar','Os olhos começam a encarar o oponente, amedrontando-o e fazendo seu ATAQUE abaixar.',-1,2],['Atirar','Um dos olhos se lança no oponente.',-3,1],\
['Plantar','Um olho se planta no chão com a possibilidade de germinar um novo cacho.',0,5],['Explodir','Todos os olhos se soltam num ataque fulminante.',-7,1]]},\
\
{'NAME': 'Perereca Mil Grau','INFO': 'Um anfíbio que saiu da metamorfose antes da hora e ao mesmo tempo que manteve a cauda, desenvolveu braços fortes.','HEIGHT': '0,70','AGILITY': 2,'MAXHP': 20,\
'HABILITIES':[['Língua','O anfíbio usa sua língua para chicotear o oponente.',-5,1],['Porrada','O anfíbio usa seus braços musculosos para bater no oponente.',-8,1],\
['Veneno','O anfíbio libera toxinas nas bolsas das suas costas para infectar o oponente.',1,4],['Salto','O anfíbio pula pelo ambiente e aumenta sua AGILIDADE',2,3]]},\
\
{'NAME': 'Cremado Cremoso','INFO': 'Um homem que sofreu uma combustão espontânea mas continua vivo graças á mutação.','HEIGHT': '1,70','AGILITY': 5,'MAXHP': 18,\
'HABILITIES': [['Bater','O indivíduo bate no oponente.',-5,1],['Cinzas','O indivíduo joga cinzas no oponente, abaixando sua AGILIDADE.',-3,3],\
['Dançar','O indivíduo começa a rebolar e mostrar seu charme.',0,6],['Infectar','O indivíduo entra dentro do oponente através das cinzas, diminuindo seu ATAQUE.',-3,2]]},\
\
{'NAME': 'Biscoito Crucificado','INFO': 'Esse ser humano não está em um estado muito bacana...É um biscoito de gengibre possuído preso num crucifixo, parece até coisa de algum filme B!','HEIGHT': '0,30','AGILITY': 8,'MAXHP': 30,\
'HABILITIES': [['Chantily','O possuído jorra chantily venenoso no oponente.',1,4],['Gargalhar','O possuído ri de uma maneira terrorífica, diminuindo o ATAQUE do oponente.',-2,2],\
['Bater','O possuído usa seu crucifixo para atacar o oponente.',-8,1],['Perfurar','O possuído perfura o corpo do oponente usando o crucifixo',-10,1]]},\
\
{'NAME': 'EMO HIPSTER','INFO': 'A DDA ainda não sabe se esse ser é uma anomalia ou apenas um cara estranho que chegou e parece não achar lugar no corpo que Deus encarnou.','HEIGHT': '1,60','AGILITY': 4,'MAXHP': 20,\
'HABILITIES': [['Cantar','O esquisito começa a cantar uma música dos los hermanos com uma guitarra.',1,4],['Guitarrada','O esquisito usa sua guitarra para atacar o oponente.',-10,1],\
['Óculos sem lente','O esquisito põe óculos sem lente para confundir o oponente, abaixando sua AGILIDADE.',-1,3],['Franja','O esquisito balança sua franja, aumentando seu ATAQUE.',2,2]]},\
\
{'NAME': 'Peixe Galã','INFO': 'Um peixe que abre a boca acima dos limites de sua mandíbula e da biologia, pelo menos ele é admirável.','HEIGHT': '1,20','AGILITY': 5,'MAXHP': 25,\
'HABILITIES': [['Aumentar','O peixe aumenta o tamanho da sua face e volta ao normal, assustando o oponente e abaixando seu ATAQUE',-2,2],\
['Saltar','O peixe salta na água e chicoteia o oponente com sua cauda',-7,1],['Morder','O peixe morde o oponente com seus dentes limpos e branquinhos.',-9,1],\
['Brilhar','O peixe reflete a luz do sol cegando o oponente.',2,4]]},\
\
{'NAME': 'Pé de moleque','INFO': 'É um doce de amendoim delicioso muito comum em festas juninas...não pera. É um membro que se separou do corpo humano e agora consegue viver por conta própria, não co fundir com mãozinha da Família Adams.','HEIGHT': '0,80','AGILITY': 5,'MAXHP': 30,\
'HABILITIES': [['Pisar','O membro pisa no oponente com toda sua força.',-10,1],['Chutar','O membro chuta o oponente, mesmo perdendo seu equilíbrio.',-12,1],\
['Cura','O membro se cura utilizando uma técnica que não entendemos devido ás limitações de seu corpo.',10,1],['Agachar','O membro concentra a energia dos seus pés e aumenta seu ATAQUE.',5,2]]},\
\
{'NAME': 'Xaruto','INFO': 'Estranhamente lembra um personagem de um anime que não é tão bom quanto Evangelion.','HEIGHT': '0,10','AGILITY': 20,'MAXHP': 1,\
'HABILITIES': [['Fumaça ninja','O elemento solta uma fumaça com mais de 100.000 substâncias tóxicas incluindo nicotina e enxofre, envenenando o oponente.',1,4],['Chama ninja','O elemento sopra uma labareda ardente, incendiando o oponente.',3,4],\
['Xaringan','O elemento usa uma espécime de energia oculta para aumentar seu ATAQUE.',10,2],['Vaporizar','O elemento se transforma num cigarro eletrônico, relaxando e diminuindo sua AGILIDADE.',-10,-2]]},\
\
{'NAME': 'Flamingo Flamenguista','INFO': 'Uma ave com a peculiaridade de ter a anomalia FLAMENGO.','HEIGHT': '1,20','AGILITY': 7,'MAXHP': 33,\
'HABILITIES': [['Bolada','A ave chuta uma bola na face do oponente.',-13,1],['Dibre','Lamentamos o erro de ortografia de Sidney, a ave dribla o oponente fazendo sua AGILIDADE aumentar.',3,2],\
['Rasteira','A ave ataca o oponente se jogando no chão e derrubando-o.',-10,1],['Gabigol','A ave recruta o profissional jogador de futebol GABIGOL, ganhando a batalha imediatamente.',-50,1]]},\
\
{'NAME': 'Cesariana','INFO': 'Um feto dentro de uma bolha numa cesariana com poderes psíquicos.','HEIGHT': '1,00','AGILITY': 2,'MAXHP': 10,\
'HABILITIES': [['Escudo','O feto reforça a resistência da bolha.',1,6],['Cordão Umbilical','O feto drena a energia de sua hospedeira e recupera sua VITALIDADE.',10,1],\
['Grito molecular','O feto grita em um nível estratosféricamente alto, agitando as moléculas de seus oponentes.',-15,1],['Líquido Uterino','O feto arremesa o líquido uterino da bolha nos oponentes, confundindo-os e dando NÁUSEA.',2,4]]},\
\
{'NAME': 'Belle Dolphine','INFO': 'Fruto de uma relação entre uma E-Girl e o Boto.','HEIGHT': '2,10','AGILITY': 7,'MAXHP': 42,\
'HABILITIES': [['Ahegao','O mamífero tenta sensualizar o oponente simulando um ato sexual, mas faz o efeito contrário abaixando seu ATAQUE',-3,2],['Água de banho','O mamífero oferece água de banho para o oponente, este o ingere e obtém HERPES.',2,4],\
['Nadar','O mamífero nada no ambiente para recuperar sua VITALIDADE.',10,1],['Canto submarino','O mamífero entoa uma canção para chamar uma anomalia para a batalha.',1,5]]},\
\
{'NAME': 'Abaporu','INFO': 'Uma pintura modernista que criou vida própria e por sinal é canibal.','HEIGHT': '2,20','AGILITY': 7,'MAXHP': 75,\
'HABILITIES': [['Pisar','A pintura pisa no oponente esmagando-o.',-13,1],['Fúria','A pintura grita furiosamente aumentando seu ATAQUE.',3,2],\
['Proteger','A pintura reforça sua proteção de acrílico sobre a tela',1,6],['Reforço','A pintura chama outra pintura para ajudar na batalha.',1,5]]},\
\
{'NAME': 'Tarsila','INFO': 'Um auto retrato da pintora Tarsila do Amaral, te encarando pronta pra acabar com sua raça. Óleo sobre tela.','HEIGHT': '2,20','AGILITY': 5,'MAXHP': 30,\
'HABILITIES': [['Atacar','A pintura se joga contra o oponente, machucando a si no processo.',-10,1]]}]

EQUIPMENT = [[['pistola',{'DAMAGE': 3, 'RECHARGE': 1, 'CAPACITY': 8}],['carabina',{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],'_','_'],\
[['pistola',{'DAMAGE': 3, 'RECHARGE': 1, 'CAPACITY': 8}],['carabina',{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],'_','_'],\
[['pistola',{'DAMAGE': 3, 'RECHARGE': 1, 'CAPACITY': 8}],['carabina',{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],'_','_']]

INVENTORY = [['_',['_','_','_'],['_','_','_'],['_','_','_'],['_','_','_']],['_',['_','_'],['_','_']]]

ITEMS = [['bolsa','Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 2x2.',1],\
['mochila','Guarde seus itens nele e leve para qualquer lugar, ou guarde para uso futuro, possui capacidade de 3x4.',1],\
['colete','Ao equipá-lo você diminui o dano tomado pelos seus inimigos',1],\
['munição.38','Munição para pistola de calibre 38, use no meio de uma batalha para recarregá-la.',0],\
['granada','Use numa batalha para causar dano á todos os inimigos na tela.',0],\
['antibiótico','Use para infeccionar feridas letais e impedir hemorragias, parando de consumir a barra de HP.',0],\
['comprimidos','Remédios utilizados para combater resfriado e envenenamento',0],\
['faca','Útil para ataques corpo-a-corpo, pode ser tão letal quanto uma arma de fogo.',1,{'DAMAGE': 4, 'RECHARGE': 0, 'CAPACITY': 0}],\
['pistola','Arma de fogo para ataques de média distância, ela usa munição de calibre 38.',1,{'DAMAGE': 3, 'RECHARGE': 1, 'CAPACITY': 8}],\
['carabina','Arma de fogo para ataques de curta distância, ela usa munição de calibre 16.',1,{'DAMAGE': 7, 'RECHARGE': 3, 'CAPACITY': 3}],\
['cookie','Restaura 5 HP',0],['identidade','Mostra suas informações básicas e prova sua autoridade acima dos civis',1],\
['paçoca','Doce de amendoim, fácil de encontrar em padarias.',3,2],\
['coxinha','Salgado feito com massa frita e recheada com frango, fácil de encontrar em lanchonetes.',3,8],\
['pastel','Salgado feito com massa frita e recheado com queijo.',3,5],\
['pastel folheado','Salgado feito com várias camadas de massa e queijo.',3,12],\
['brigadeiro','Doce de chocolate.',3,3],\
['café','Bebida quente que aumenta a energia.',3,10],\
['pão de queijo','Salgado feito com massa de queijo.',3,7],\
['pudim','Doce feito com leite condensado.',4,15],\
['bolo de fubá','Doce feito com ovos, leite, fubá, manteiga, trigo e fermento.',4,18],\
['cartão de crédito','Um item muito necessário na vida de um jovem adulto, use nos caixas de banco, nem imagine em jogar fora!',2],\
['carregador portátil','Use para carregar seu celular',2],\
['fones de ouvido','Ao obter um, você consegue escutar o rádio do celular, mas atenção! ele quebra nos momentos mais inesperados.',1],\
['celular','Mais importante que o cartão só o celular, pode ser usado para fazer chamadas e receber emails, mas lembre-se de recarregar',2]]

def load_game(slt):
	file=open(str(slt)+'userdata.db','r')
	step=0
	x=0
	y=0
	z=0
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
			PLAYER[1][k]=v
		elif step==1:
			ATM=file.readline()[0:-1]
			MONEY=file.readline()[0:-1]
			CREDIT=file.readline()[0:-1]
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
	file.close()

def save_game(slt):
	file=open(str(slt)+'userdata.db','w')
	for l in PLAYER[1]:
		if l=='ATTACK':break
		file.write(l+': '+str(PLAYER[1][l])+'\n')
	file.write('-\n')
	file.write('ATM: '+str(ATM)+'\n')
	file.write('MONEY: '+str(MONEY)+'\n')
	file.write('CREDIT: '+str(CREDIT)+'\n')
	file.write('-\n')
	for l in INVENTORY:
		for j in l:
			if l[0]==j:
				file.write(j+'\n')
				continue
			for i in j:
				file.write(i+'\n')
	file.close()
	
load_game(1)

CONTACTS = {'Renan': '990435671','Pietra': '940028922','Paulo': '987690021','Jane': '991124257','Bianca': '976564008','Diego': '926148930'}

CALLHIST = []

EMAILS = [['ddarj@cmail.com','Hello World!','This is a test',False],\
['cangaceirostv@cmail.com','Proposta de entrevista','Boas novas, '+PLAYER[1]['NAME']+' '+PLAYER[1]['LASTNAME']+'.\n\nCom a repercussão dos casos de anomalias do Departamento de Detenção de Anomalias de Itatiaia, sugerimos uma entrevista com você e dois participantes para o Jornal da Noite.\n\nA entrevista será ás 5:30 PM e será gravado nos estúdios da Cangaceiros TV, na Av. Getúlio Vargas.\n\nAguardamos sua resposta no local.',False],\
['gleicyrocha7@cmail.com','Oiee','Só tô te testando menino',False]]

TASKS = [['Poltergeist na Av. Jobim',False],['Entrevista na Cangaceiros TV',False],['Encontrar a aprendiz',False],['Tirar o crachá da DDA',True]]

NEWS = [[['Relato de assombração em residência','Jéssica Ramone','Ás 11:30 da noite passada, moradores de Itatiaia relataram um caso incomum entre vários da polícia, \
foi registrado um caso de uma assombração (vulgo Poltergeist) na casa de Maria Elisângela das Dores, 35 anos.\n\n"Não sabia o que fazer, eu nunca imaginei que assombrações\
 ou fantasmas realmente existissem, sempre achei que eram apenas contos de criança.", diz Maria Elisângela.\n\nApesar de inesperado e muito estranho, o relato foi comprovado \
 por filmagens do Departamento de Detenção de Anomalias de Itatiaia, além dos danos causados pela assombração na casa e nos moradores da região.\n\nAparentemente este não é o \
 único relato de moradores a respeito de uma assombração, foram registrados 5 relatos em um único mês e 12 em 3 meses, mas se as investigações persistirem este pode ser o \
 primeiro relato de uma assombração no país.'],\
['Engarrafamento','Gisele Peres','Muito trânsito']],\
[['Dia 2','Gisele Peres','Muito sol'],['FLA x FLU','Gustavo Pinhão','Muito disputado']]]

MANUAL = [['CONTROLES\n\nAperte '+SETTINGS['LEFT']+', '+SETTINGS['RIGHT']+', '+SETTINGS['UP']+' e '+SETTINGS['DOWN']+' para mover seu personagem'],\
['CELULAR\n\nO celular é o equivalente ao menu do jogo, acesse-o apertando '+SETTINGS['ACT']+'.\n\nAtente-se á carga do celular: ao se esgotar, você fica incapacitado de utilizá-lo, para carregar, use o carregador. Utilize carregadores portáteis ao se afastar da área urbana.\
\n\nOs créditos servem para fazer ligações, recarregue-os na farmácia, fora da área urbana, os créditos também são gastos ao usar aplicativos que usam internet.\n\n\
Na barra superior do celular, aparecem informações de data, hora, sinal, créditos e carga. Esses são os aplicativos que pode usar:\n\n\
MAPA: ver o mapa da cidade, traçar rotas e ver informações dos locais. Não mostra as regiões florestais.\n\n\
CHAMADAS: ver os contatos salvos, histórico de ligações e fazer chamadas. Quanto mais longa for a chamada, mais créditos são gastos.\
\n\nEMAIL: ver emails enviados da agência e outras instituições.\n\n\
NOTÍCIAS: ver as últimas notícias da região, podem aparecer casos resolvidos e casos para resolver.\n\n\
RÁDIO: escutar música aleatória de 4 estações diferentes, ao se afastar da área urbana não é possível utilizá-lo. É necessário um fone de ouvido para usá-lo.\n\n\
CÂMERA: tirar capturas de tela e ver capturas salvas.\n\n\
TAREFAS: ver missões e casos já cumpridos ou para cumprir.\n\n\
STATUS: ver as informações completas dos atributos do jogador.\n\n\
BESTIÁRIO: banco de dados da agência onde se registram todas as anomalias.\n\n\
AJUDA: ler o manual completo do jogo.\n\n\
CONFIGURAÇÕES: editar opções de som, imagem, controles, idioma e etc.\n\n\
SALVAR: salva o progresso atual do jogo.'],\
['BATALHA\n\nPara vencer uma batalha, você deve derrotar todos os inimigos da tela ao mesmo tempo que deve se defender dos ataques inimigos.\n\n\
HP: A barra vermelha mostra seu HP, ela pode ser maior dependendo do seu nível de VITALIDADE, a barra diminui com o ataque inimigo e uma barra amarela diminui lentamente com ela, baseada no nível de RESISTÊNCIA.\n\n\
PP: Mostra a quantidade de munição para as armas de fogo, sendo a barra diferente para cada arma.\n\n\
XP: Seu nível de experiência, quanto mais experiente for nas batalhas, maior seu grau dentro da agência.\n\n\
Numa batalha, aparecem como opções os itens equipados, mas você também pode abrir seu inventário e fugir da batalha. Seu desempenho ao atacar é baseado nos seus atributos, \
ao mesmo tempo em que os inimigos também possuem seus atributos para defender, sendo esses: \n\n\
ATAQUE: distância dos extremos da barra\n\n\
AGILIDADE: velocidade do cursor da barra\n\n\
RESISTÊNCIA: velocidade de consumo da barra de HP\n\n'],\
['LOCAIS']]

DIALOGS = {'990435671': [[PLAYER[1]['NAME']+'! Precisamos de você aqui AGORA!','Parece que é um poltergeist, estamos na Av. Jobim, venha logo!'],['Porra '+PLAYER[1]['NAME']+', será que você não entende a gravidade da situação??','Só você pode deter essa anomalia!']],\
'940028922': [['Oh, olá! como vai, '+PLAYER[1]['NAME']+'?','Tenho andado ocupada esses dias, muita coisa pra fazer...','Não dá pra falar com você agora, desculpa','Me ligue mais tarde, ok?'],['oie']]}