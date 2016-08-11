import re
import os
import operator

def main():
	infile = open( os.path.join( os.path.abspath(__file__ + "/../../"), 'GeekShed', '#dtdgb.log'), 'r')
	nameFreq = {}
	nameCount = {}
	totalTalks = 0
	throbCount = 0
	for line in infile:
		res = re.search("<.*?>", line)
		if res:
			name = res.group(0)[1:-1]
			if name in nameFreq:
				nameFreq[name] += 1
				totalTalks += 1
			else:
				nameFreq[name] = 1
		
		if re.search('throb', line):
			throbCount += 1
		
	print("Throb Count: {}\n".format(throbCount) )
	
	for key in nameFreq:
		nameCount[key] = float(nameFreq[key]) / totalTalks
	for key in nameFreq:
		if nameCount[key] > 0.01:
			print("{}: {} ({:.2%})".format(key.ljust(20), nameFreq[key], nameCount[key]) )
	
	print("total talks: {}".format(totalTalks) )

main()