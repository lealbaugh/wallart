

def main(): 
	f = open('winterstale.txt','r')
	out = open('output.txt','w')
	for line in f:
		if len(line.split()) > 0:
			firstword = line.split()[0]
			if firstword=="ACT":
				currentact = line.split()[1]
			elif firstword=="SCENE":
				currentscene = "\nAct "+currentact+", Scene "+line.split()[1]+":\n"
				out.write(currentscene)
				players = []
			elif line.isupper():
				discard = False
				for existing in players:
					if line == existing:
						discard = True
				if discard == False:
					players.append(line)
					out.write(line)
	f.close()
	out.close()








if __name__ == "__main__": 
	main()
