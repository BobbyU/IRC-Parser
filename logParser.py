import re
import os
import operator

def main():
	infile = open( os.path.join( os.path.abspath(__file__ + "/../../"), 'GeekShed', '#dtdgb.log'), 'r')    #find log file
	nameFreq = {}    #dict with names and number of talks
	nameCount = {}    #dict with names and percent of talks
	totalTalks = 0
	throbCount = 0
	for line in infile:    #for each line in the log
		res = re.search("<.*?>", line)   #use regex to find the speaker
		if res:                          #if there is one...
			name = res.group(0)[1:-1]    #remove the "brackets" from the string
			if name in nameFreq:         #if the name is already in the dict
				nameFreq[name] += 1      #then add one to their 
				totalTalks += 1
			else:                        #if not,
				nameFreq[name] = 1       #init their place in the dict
				totalTalks += 1
		
		if re.search('throb', line):     #count those throbbers
			throbCount += 1
		
	print("Throb Count: {}\n".format(throbCount) )    # print throb count
	
	for key in nameFreq:    #calculate percentages
		nameCount[key] = float(nameFreq[key]) / totalTalks
	for key in nameFreq:    #print each name and values
		if nameCount[key] > 0.01:    #if they've talked enough
			print("{}: {} ({:.2%})".format(key.ljust(20), nameFreq[key], nameCount[key]) )
	
	print("total talks: {}".format(totalTalks) )

main()