import random
import string

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

def retrieve_input(possible_ans):
    selection = raw_input("Enter your guess here: ")
    selection = selection.upper()
    error_flag = True
    while(error_flag):
       if not selection in possible_ans:
          print "Selection is not a valid one"
          selection = raw_input("Enter your guess here: ")
	  selection = selection.upper()
       
       else:
          error_flag = False
    
    assert(len(selection) == 1 and selection.isalpha())
    return selection
       

myfile = open("countries.txt", 'r')
listNames = []
for line in myfile:
	listNames.append(line[:len(line)-2])

num = random.randint(0, len(listNames)-1)
wordChosen = listNames[num].upper()
game_status = initialization(wordChosen)
chars_available   = list(string.uppercase)

print currWordFormat(game_status)
print "Available Options:"
print chars_available

while(not isWin(game_status)):
    chosen_char = retrieve_input(chars_available)
    chars_available.remove(chosen_char)
    game_status = progress(wordChosen, game_status, chosen_char)
    print currWordFormat(game_status)
    print "Available Options:"
    print chars_available

print "End of game"
