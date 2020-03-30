import json
from difflib import get_close_matches
data = json.load(open('data.json'))
char = 'y'
def definiton(word):
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys())) > 0:
		print ("did you mean %s ?" % get_close_matches(word,data.keys())[0])
		decide = input("press Y or N : ")
		if decide == 'Y' or decide == 'y' :
				return data [get_close_matches(word,data.keys())[0]]
		elif decide =='N' or decide =='n':
				return ("No definiton found!!")
		else:	
				print('invalid input')
	else:
		return ("No definiton found!!")			
		 

while (char=='y'or char=='Y'):
	word = input("Enter the word you want to search : ")
	result = definiton(word)
	print ("word: ",word)
	print ("definiton: ",result)
	char = input("Press Y to search for another word : ")
		
