#from __future__ import print_function
import random
"""
def parseData(fname):
  for l in urllib.urlopen(fname):
     yield eval(l)
"""

def currWordFormat(status):
    currWord = ""
    for ch in status:
	if(ch == "_"):
	    currWord += "_ "
	elif(ch == " "):
	    currWord += "  "
	else:
	    currWord += ch + " "
    return currWord

def initialization(word):
    init_word = []
    for ch in word:
        if ch.isalpha():
	    init_word += ["_"]
	else:
	    init_word += [ch]
    return init_word
	   
def progress(word, status, selection):
    for i in xrange(len(word)):
        if selection == word[i]:
	    status[i] = selection
    return status
	    
def isWin(status):
    return not "_" in status

def retrieve_input():
    selection = raw_input("Enter your guess here: ")
    selection = selection.lower()
    error_flag = True
    while(error_flag):
       if len(selection) != 1:
          print "Guess should be 1 character only"
	  error_flag = True
	  
       else:
           error_flag = False

       if not selection.isalpha():
          print "Guess should be a letter"
	  error_flag = True
      
       elif not error_flag:
           error_flag = False
       
       if error_flag:
          selection = raw_input("Enter your guess here: ")
	  selection = selection.lower()
    
    assert(len(selection) == 1 and selection.isalpha())
    return selection
       

myfile = open("countries.txt", 'r')
listNames = []
for line in myfile:
	listNames.append(line[:len(line)-2])

num = random.randint(0, len(listNames)-1)
wordChosen = listNames[num].lower()
game_status = initialization(wordChosen)

print currWordFormat(game_status)
while(not isWin(game_status)):
    chosen_char = retrieve_input()
    game_status = progress(wordChosen, game_status, chosen_char)
    print currWordFormat(game_status)

print "End of game"
#print listNames[num]
#print len(listNames[num])
#print printCurrWord(listNames[num])
