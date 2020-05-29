import re
import os
import operator
from datetime import datetime, timedelta

def main():
	infile = open( os.path.join( os.getenv('APPDATA'), 'HexChat', 'logs', 'GeekShed', '#JFDom.log'), 'r', encoding="utf8")    #find log file
	nameFreq = {}    #dict with names and number of talks
	nameCount = {}    #dict with names and percent of talks
	wordCount = {}    #dict with names and number of words
	totalTalks = 0
	totalWords = 0
	throbCount = 0
	roostCount = 0
	booshCount = 0
	throbCounter = {}
	roostCounter = {}
	booshCounter = {}
	numOfDays = 0
	lastTime = datetime.fromordinal(1)
	print(datetime.today())
	for line in infile:    #for each line in the log
		res = re.search("<.*?>", line)   #use regex to find the speaker
		res2 = re.search("/HELP", line)  #make sure it's not a help line
		if res and not res2:                          #if someone is talking
			timestmp = datetime.strptime(line[0:15], "%b %d %H:%M:%S") + timedelta(days = 42369)
			if timestmp.day != lastTime.day:
				numOfDays += 1
				lastTime = timestmp
			name = res.group(0)[1:-1].lower()    #remove the "brackets" from the string
			if name in nameFreq:         #if the name is already in the dict
				nameFreq[name] += 1      #then add one to their 
			else:                        #if not,
				nameFreq[name] = 1       #init their place in the dict
				throbCounter[name] = 0
				roostCounter[name] = 0
				booshCounter[name] = 0
				wordCount[name] = 0
			totalTalks += 1
			totalWords += line.split().__len__()
			wordCount[name] += line.split().__len__()
			
			throbsInThisLine = line.lower().count('throb') #count those throbbers
			throbCount += throbsInThisLine
			booshsInThisLine = line.count('BOOSH') +  line.count('HSOOB')#count BOOSH
			booshCount += booshsInThisLine
			if name.lower().count('throb') > 0:
				throbCounter[name] += (throbsInThisLine - 1)
				throbCount -= 1
			else:
				throbCounter[name] += throbsInThisLine
			roostsInThisLine = line.lower().count('roost') #count those roosts
			roostCount += roostsInThisLine
			if name.lower().count('rooster') > 0:
				roostCounter[name] += (roostsInThisLine - 1)
				roostCount -= 1
			else:
				roostCounter[name] += roostsInThisLine
			if name.lower().count('BOOSH') > 0:
				booshCounter[name] += (booshsInThisLine - 1)
				booshCount -= 1
			else:
				booshCounter[name] += booshsInThisLine
	
	for key in nameFreq:    #calculate percentages
		nameCount[key] = float(nameFreq[key]) / totalTalks
		
	print("{} {} {}  Roosts  Throbs  BOOSHes".format("Name".ljust(20), "Talks".ljust(15), "Avg Words"))
	for i in range(0,len(nameFreq)):    #print each name and values
		maxKey = max(nameFreq, key=nameFreq.get)    #get the entry with the most talks
		if nameCount[maxKey] > 0.01:    #if they've talked enough
			print("{} {:4} ({:6.2%})   {:8.4F}    {:2}      {:2}      {:2}".format(maxKey.ljust(20), nameFreq[maxKey], nameCount[maxKey], (wordCount[maxKey]/nameFreq[maxKey]), roostCounter[maxKey], throbCounter[maxKey], booshCounter[maxKey]) )
			del nameCount[maxKey]
			del nameFreq[maxKey]
			del throbCounter[maxKey]
	
	print("total talks: {}".format(totalTalks) )      # print total talks
	print("Roost Count: {}".format(roostCount) )    # print roost count
	print("Throb Count: {}".format(throbCount) )    # print throb count
	print("BOOSH Count: {}".format(booshCount) )    # print BOOSH count
	print("Word Count: {}".format(totalWords) )    # print word count
	print("Average words per talk: {:.4}".format(totalWords/totalTalks) )    # print average words per talk
	print("Average Talks per day: {:.4}\n".format(totalTalks/numOfDays) )

main()