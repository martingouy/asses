def PE_old(p,c):
	#p -> proba
	#c -> choix  0= choix sur 1= choix lotterie

	if c == 0:
		return  p + (1 - p)/4
	else:
		return p / 4



def PE(min_interval,max_interval,p,choix):
	#min_interval=0; p=0.75; max_interval=1
	
    liste=[min_interval,max_interval]
    if choix==1:
        max_interval=p #la borne max est remplacee par la nouvelle valeur
        p=round(p/4,2) #au premier abord, on divise p par 4
        if p<min_interval:
            p=round(min_interval+(max_interval-min_interval)/4,2) 
        liste=[min_interval,max_interval] #pas la peine de renvoyer la valeur de p car max_interval=p
        return({"interval": liste,"proba": p})
    else:
        min_interval=p
        p=round(max_interval-(max_interval-min_interval)/4,2)
        liste=[min_interval,max_interval]
        return({"interval": liste,"proba": p})
