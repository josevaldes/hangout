import random
import string
from image_steps import images_steps


def select_topic():
    dictList = ["Animals", "Countries", "Names"]
    print "     Topics Available: "
    for elem in dictList:
        print "          " + elem
    topic = raw_input("Select the topic of your preference: ")
    
    while not topic in dictList:
       topic = raw_input("Sorry, I didn't get your option, write it again: ").lower()
    return topic.lower()

def setting_speed_mode():
    difficulty = raw_input("Select the difficulty of gallow building speed:\n Easy   Medium   Hard\n\n")
    difficulty = difficulty.lower()
    possible_opt = {"easy":1, "medium":2, "hard":3}
    while not difficulty in possible_opt:
       difficulty = raw_input("Sorry, I didn't get your option, write it again: ").lower()
    return possible_opt[difficulty]

def setting_word_mode(max_length):
    difficulty = raw_input("Select the difficulty of word:\n Easy   Medium   Hard\n\n")
    difficulty = difficulty.lower()
    first_bound  = (max_length / 3) 
    second_bound = 2 * first_bound
    possible_opt = {"easy":range(0,first_bound), "medium":range(first_bound,second_bound), "hard":range(second_bound, max_length)}
    while not difficulty in possible_opt:
       difficulty = raw_input("Sorry, I didn't get your option, write it again: ").lower()
    return possible_opt[difficulty]

def selecting_word(options,difficulty):
    index = random.randint(0, len(options) -1)
    while not len(options[index]) in difficulty:
        index = random.randint(0, len(options)-1)
    return options[index]

def starting_pt(step, max_range):
#    assert step == 2 
#    assert max_range == 10
    initial_pt = max_range
    while initial_pt >= step:
        initial_pt -= step
#    assert initial_pt == 0
    return initial_pt

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

def update_errors(ch, word, errors, step):
    if not ch in word:
       errors += step
    return errors

def isLost(errors, max_errors):
    return errors == max_errors

print "Welcome to Hangout"
mytopic = select_topic()
myfile = open("dictionaries/"+ mytopic + ".txt", 'r')
max_length = 0
listNames = []
for line in myfile:
        currWord = line.split('\r\n')[0]
	listNames.append(currWord)
	max_length = max(max_length, len(currWord))

factor = setting_speed_mode()
word_factor = setting_word_mode(max_length)
#num = random.randint(0, len(listNames)-1)
wordChosen = selecting_word(listNames, word_factor).upper()
game_status = initialization(wordChosen)
chars_available   = list(string.uppercase)
num_errors = starting_pt(factor, len(images_steps) - 1)

print currWordFormat(game_status) 
print images_steps[num_errors]
print "Available Options:"
print str(chars_available) 

while not isWin(game_status) and not isLost(num_errors, len(images_steps)-1):
    chosen_char = retrieve_input(chars_available)
    chars_available.remove(chosen_char)
    game_status = progress(wordChosen, game_status, chosen_char)
    num_errors  = update_errors(chosen_char, wordChosen, num_errors, factor)
    print currWordFormat(game_status) 
    print images_steps[num_errors]
    print "Available Options:"
    print chars_available

if isWin(game_status):
    print "Congratulations, you win"

else:
    print "Sorry, you went to the gallow"
    print "The word was: " + wordChosen
    print "GAME OVER"
