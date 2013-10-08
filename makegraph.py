

def main(): 
	source = open('winterstale.txt','r')
	scenesfile = open('scenes.txt','w')
	for line in source:
		if len(line.split()) > 0:
			firstword = line.split()[0]
			if firstword=="ACT":
				currentact = line.split()[1]
			elif firstword=="SCENE":
				currentscene = "\nAct "+currentact+", Scene "+line.split()[1]+":\n"
				scenesfile.write(currentscene)
				players = []
			elif line.isupper():
				discard = False
				for existing in players:
					if line == existing:
						discard = True
				if discard == False:
					players.append(line)
					scenesfile.write(line)
	source.close()
	scenesfile.close()
	castlist = open('scenes.txt','r')
	playersfile = open('players.txt','w')
	players = []
	for line in castlist:
	
		if len(line.split()) > 0:
			firstword = line.split()[0]
			if firstword !="Act":
				discard = False
				for existing in players:
					if firstword == existing:
						discard = True
				if discard == False:
					players.append(firstword)
	for item in players:
		playersfile.write(item+"\n")
	
	castlist.close()
	playersfile.close()









if __name__ == "__main__": 
	main()
