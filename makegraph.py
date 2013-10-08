

def main(): 
	f = open('winterstale.txt','r')
	out = open('output.txt','w')
	for line in f:
		if len(line.split()) > 0:
			firstword = line.split()[0]
			if firstword=="ACT":
				out.write("\n ===>"+line)
			elif firstword=="SCENE":
				out.write("\n"+line)
			elif line.isupper():
				out.write(line)
	f.close()
	out.close()








if __name__ == "__main__": 
	main()
