import re
import os
import operator

def main():
	infile = open( os.path.join( os.path.abspath(__file__ + "/../../"), 'GeekShed', '#dtdgb.log'), 'r')    #find log file
	nameFreq = {}    #dict with names and number of talks
	nameCount = {}    #dict with names and percent of talks
	wordCount = {}    #dict with names and number of words
	totalTalks = 0
	totalWords = 0
	throbCount = 0
	roostCount = 0
	throbCounter = {}
	roostCounter = {}
	#bPipe = 0
	for line in infile:    #for each line in the log
		res = re.search("<.*?>", line)   #use regex to find the speaker
		if res:                          #if someone is talking
			name = res.group(0)[1:-1].lower()    #remove the "brackets" from the string
			if name in nameFreq:         #if the name is already in the dict
				nameFreq[name] += 1      #then add one to their 
			else:                        #if not,
				nameFreq[name] = 1       #init their place in the dict
				throbCounter[name] = 0
				roostCounter[name] = 0
				wordCount[name] = 0
			totalTalks += 1
			totalWords += line.split().__len__()
			wordCount[name] += line.split().__len__()
			
			throbsInThisLine = line.lower().count('throb') #count those throbbers
			throbCount += throbsInThisLine
			if name.lower().count('throb') > 0:
				throbCounter[name] += (throbsInThisLine - 1)
				throbCount -= 1
			else:
				throbCounter[name] += throbsInThisLine
			roostsInThisLine = line.lower().count('roost') #count those roosts
			roostCount += roostsInThisLine
			if name.lower() == 'rooster':
				roostCounter[name] += (roostsInThisLine - 1)
				roostCount -= 1
			else:
				roostCounter[name] += roostsInThisLine
		#elif line[13] == "*":
		#	if line.lower().count('broken pipe') > 0:
		#		bPipe += 1
	
	for key in nameFreq:    #calculate percentages
		nameCount[key] = float(nameFreq[key]) / totalTalks
		
	print("{} {} {}  Roosts  Throbs".format("Name".ljust(20), "Talks".ljust(13), "Avg Words"))
	for i in range(0,len(nameFreq)):    #print each name and values
		maxKey = max(nameFreq, key=nameFreq.get)    #get the entry with the most talks
		if nameCount[maxKey] > 0.01:    #if they've talked enough
			print("{} {:4} ({:2.2%}) {:9} {:7} {:7}".format(maxKey.ljust(20), nameFreq[maxKey], nameCount[maxKey], (wordCount[maxKey]/nameFreq[maxKey]), roostCounter[maxKey], throbCounter[maxKey]) )
			del nameCount[maxKey]
			del nameFreq[maxKey]
			del throbCounter[maxKey]
	
	print("total talks: {}".format(totalTalks) )      # print total talks
	print("Roost Count: {}".format(roostCount) )    # print roost count
	print("Throb Count: {}".format(throbCount) )    # print throb count
	print("Average words per talk: {}\n".format(totalWords/totalTalks) )    # print average words per talk

main()