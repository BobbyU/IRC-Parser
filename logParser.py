import re
import os
import operator

def main():
	infile = open( os.path.join( os.path.abspath(__file__ + "/../../"), 'GeekShed', '#dtdgb.log'), 'r')    #find log file
	nameFreq = {}    #dict with names and number of talks
	nameCount = {}    #dict with names and percent of talks
	totalTalks = 0
	throbCount = 0
	throbCounter = {}
	for line in infile:    #for each line in the log
		res = re.search("<.*?>", line)   #use regex to find the speaker
		if res:                          #if someone is talking
			name = res.group(0)[1:-1].lower()    #remove the "brackets" from the string
			if name in nameFreq:         #if the name is already in the dict
				nameFreq[name] += 1      #then add one to their 
			else:                        #if not,
				nameFreq[name] = 1       #init their place in the dict
				throbCounter[name] = 0
			totalTalks += 1
			
			throbsInThisLine = line.lower().count('throb') #count those throbbers
			throbCount += throbsInThisLine
			throbCounter[name] += throbsInThisLine
	
	for key in nameFreq:    #calculate percentages
		nameCount[key] = float(nameFreq[key]) / totalTalks
	for i in range(0,len(nameFreq)):    #print each name and values
		maxKey = max(nameFreq, key=nameFreq.get)    #get the entry with the most talks
		if nameCount[maxKey] > 0.01:    #if they've talked enough
			print("{}: {} ({:.2%}) Throbs: {}".format(maxKey.ljust(20), nameFreq[maxKey], nameCount[maxKey], throbCounter[maxKey]) )
			del nameCount[maxKey]
			del nameFreq[maxKey]
			del throbCounter[maxKey]
	
	print("total talks: {}".format(totalTalks) )      # print total talks
	print("Throb Count: {}\n".format(throbCount) )    # print throb count

main()