"""README"""
#This python script was tested using Python version 2.7

"""Question 1"""
"""(a)Write a python tuple of the year, month, and day of your birth"""
#assign the year, month, and day of your birth to a tuple
myBirthdateTuple = (1990,1,9)

#assign my answer to (a) to a string
answerAString = "myBirthdateTuple = (1990,1,9)"

#print answer for (a) as a string
print("Question 1(a) answer: " + answerAString)


"""(b)Write a python list of the year, month, and day of your best friend's birth"""
#assign the year, month, and day of your best friend's birth to a list
bestFriendsBirthdateList = [1990,6,23]

#assign my answer to (b) to a string
answerBString = "bestFriendsBirthdateList = [1990,6,23]"

#print answer for (b) as a string
print("Question 1(b) answer: " + answerBString)

"""(c)Why is a list better than a tuple to store your friend'sinformation in?"""
#assign my answer to (c) to a string
answerCString = "\nA list is mutable, whereas a tuple is immutable.\nThis means that we can change the contents of the list,\nbut we wouldn't be able to if it was stored as a tuple.\nMy birthdate will never change,\nso it is best stored in an immutable structure.\nMy best friend, however, may change.\nThus the need for a data structure that can be changed.\n"

#print answer for (c) as a string
print("Question 1(c) answer: " + answerCString)

"""Question 2"""
"""Write a python function to loop which: 1 Asks the user to provide examples of five (5) pieces of data: an integer, a string, and a float. 2 Prints out which one of these types of data it is. 3 Prints an error if it is of type tuple."""
#note, the assignment mentions (5) different data types but only provides examples for (3). I will add in data of type: bool and type: complex to meet the (5) types outlined initially.

#define the function
def userInputDataTypeCheck():
    #initialize an iterator for userInput loop
    userInputs = 0
    #define a maximum number of userInputs 
    maxUserInputs = 5
    while userInputs < maxUserInputs:
        #prompt the user for input
        print("Input an integer, a string (include quotation marks!), a float, a bool, or a complex number")
        #assign the users input to a variable
        userInput = input()
        #try to print the data type for userInput
        if(type(userInput) != tuple):
             #print out the data type for userInput
             print(type(userInput))
        else:
             #print an error
             print("The data entered was a tuple, please enter a valid data type")
        
        #increment userInputs
        userInputs += 1

#execute the function
userInputDataTypeCheck()
    

"""Question 3"""
"""Create a dictionary which can be used to look up the translation of the names(in English)of the numbers 0-9 in Spanish, French,German, Dutch, and oneother language."""

#create English to Spanish dictionary
engToSpanish = {'zero':'cero', 'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro', 'five': 'cinco', 'six': 'seis', 'seven': 'siete', 'eight': 'ocho', 'nine': 'nueve'}
#create English to French dictionary
engToFrench = {'zero':'zero', 'one': 'un', 'two': 'deux', 'three': 'trois', 'four': 'quatre', 'five': 'cinq', 'six': 'six', 'seven': 'sept', 'eight': 'huit', 'nine': 'neuf'}
#create English to German dictionary
engToGerman = {'zero':'null', 'one': 'eins', 'two': 'zwei', 'three': 'drei', 'four': 'vier', 'five': 'funf', 'six': 'sechs', 'seven': 'sieben', 'eight': 'acht', 'nine': 'neun'}
#create English to Dutch dictionary
engToDutch = {'zero':'nul', 'one': 'een', 'two': 'twee', 'three': 'drie', 'four': 'vier', 'five': 'vijf', 'six': 'zes', 'seven': 'zeven', 'eight': 'acht', 'nine': 'negen'}
#create English to Norwegian dictionary
engToFrench = {'zero':'null', 'one': 'en', 'two': 'to', 'three': 'tre', 'four': 'fire', 'five': 'fem', 'six': 'seks' 'seven': 'sju', 'eight': 'atte', 'nine': 'ni'}

#create a single dictionary that includes all 5 languages
languageDict = {'numbers':[0,1,2,3,4,5,6,7,8,9], 'english':['zero','one','two','three','four','five','six','seven','eight,','nine'],'spanish':['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve'],'french':['un','deux','trois','quatre','cinq','six','sept','huit','neuf'],'german':['null','eins','zwui','drei','vier','funf','six']}

