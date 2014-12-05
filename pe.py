def PE(p,c):
	#p -> proba
	#c -> choix  0= choix sur 1= choix lotterie

	if c == 0:
		return  p + (1 - p)/4
	else:
		return p / 4
