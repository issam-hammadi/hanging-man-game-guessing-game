import time,re


# printing the structure of the hanging man and the dashes
def printing(chances):

    if chances == 9:
        print("-------\n")  # the 1 chance
    if chances == 8:
        print("|\n|\n|\n-------\n")  # the 2 chance
    if chances == 7:
        print("-------\n|\n|\n|\n-------\n")  # the 3 chance
    if chances == 6:
        print("-------\n|     |\n|\n|\n-------\n")  # the 4 chance
    if chances == 5:
        print("-------\n|     |\n|     o\n|\n-------\n")  # the 5 chance
    if chances == 4:
        print("-------\n|     |\n|     o\n|     |\n------|\n")  # the 6 chance
    if chances == 3:
        print("-------\n|     |\n|     o\n|    \|\n------|\n")  # the 7 chance(the left hand)
    if chances == 2:
        print("-------\n|     |\n|     o\n|    \|/\n------|\n")  # the 8 chance(the right hand)
    if chances == 1:
        print("-------\n|     |\n|     o\n|    \|/\n-----/|\n")  # the 9 chance(the left leg)
    if chances == 0:
        print("-------\n|     |\n|     o\n|    \|/\n-----/|\\") #  the game over
        print("***********************\n    GAME OVER BABE ")
        return 'GAME OVER'
    print("*******************************************************")


# Function to check first if the input of the player is valid or not
def inputFunction(player1, player2):
    letter = input(f"{player2} enter a valid letter:")
    letter = letter.lower()
    letterCheck = re.compile(r'[a-z]',re.DOTALL | re.VERBOSE| re.IGNORECASE)
    mo = letterCheck.findall(letter)
    if len(mo) == 1:
        return mo
    else:
        return inputFunction(player1, player2)

# The starting function that let the first player enter his word
def gameStarted(player1, player2):
    list = []
    print(f'{player1}, enter the secret word and  {player2} please close your eyes!!! >')
    word = input(">")
    print("\n" * 50)
    word = word.lower()
    length = len(word)
    list.append(word)
    list.append(length)
    turn = 1
    list.append(turn)
    return list

#  A function that replace the letter entered if it exists in the free dashes
def replacing(letter, word):
    scoring = "_" * len(word)
    scoringList = []
    for i in scoring:
        scoringList.append(i)
    index = 0
    for i in word:
        if i == letter:
            scoringList[index] = letter
        else:
            pass
        index += 1
    newScoring = ''.join(scoringList)
    return newScoring


def replacing2(oldScoring, newScoring):
    oldScoringList = []
    newScoringList = []
    for i in oldScoring:
        oldScoringList.append(i)
    for j in newScoring:
        newScoringList.append(j)
    index = 0
    for i in oldScoringList:
        if i == newScoringList[index]:
            pass
        else:
            if i == '_':
                pass
            else:
                newScoringList[index] = i
        index += 1
    newScoring = ''.join(newScoringList)
    return newScoring


# A function that returns either a letter is already tested or not
def alreadyTested(letter, list):
    for i in list:
        if i == letter:
            return 1
        else:
            pass
    return 0


# winning Function / it does not return a game over statement
def winningCheck(newScoring):
    for i in newScoring:
        if i == "_":
            return 0
        else:
            pass
    return 1

# the function that checks either there was a change to let the chances = cte or chances -= 1
def changes(oldScoring, newScoring):
    if oldScoring == newScoring:
        return 0
    else:
        return 1

def turn(player1, player2, turn):
    if turn == 1:
        turn = 2
        print(f'turn of {player2} : being the word guesser.')
    else:
        turn = 1
        print(f'turn of {player1} : being the word teller. ')



def main(player1, player2, score1, score2):
    # putting it all together
    #the chances
    chances = 10
    # asking the 1rst player to enter the mysterious word
    list = gameStarted(player1, player2)
    word = list[0]
    # printing the number of the letters in the secret word
    val = len(word)
    oldScoring = '_' * val
    print(oldScoring)

    # initialisation of the list of the letters tested
    lettersTested = ["nothing"]
    # asking the player 2 to enter his/her guess
    letter = inputFunction(player1, player2)
    let = letter[0]
    # lettersTested.append(letter)
    # replacing the first letter in the mysterious word if the player 2 make the guess right
    newScoring = replacing(let, word)
    checkVal = changes(oldScoring, newScoring)
    if checkVal == 1:
        pass
    else:
        chances -= 1
    print(newScoring)
    print(f"you still have {chances} chances !!")
    printing(chances)
    lettersTested[0] = let
    print(f"the list of the letters already tried is {lettersTested}")
    oldScoring = newScoring
    while winningCheck(newScoring) == 0 and chances != 0:
        letter = inputFunction(player1, player2)
        let = letter[0]
        val = alreadyTested(let, lettersTested)
        while val == 1:
            print("ERROR: you have already tried this letter!!")
            letter = inputFunction(player1, player2)
            let = letter[0]
            val = alreadyTested(let, lettersTested)
        # adding the letter in the letters tested list
        lettersTested.append(let)
        newScoring = replacing(let, word)
        newScoring = replacing2(oldScoring, newScoring)
        checkingVal = changes(oldScoring, newScoring)
        if checkingVal == 1:
            pass
        else:
            chances -= 1
        oldScoring = newScoring
        print(newScoring)
        print(f"you still have {chances} chances !!")
        printing(chances)
        print(f"the list of the letters already tried is {lettersTested}")
    if chances == 0:
        print(f"{player1} won!!!")
        score1 = score1 + 1
    else:
        print(f"{player2} won!!!")
        score2 = score2 + 1
    print(f'the score of {player1} = {score1}')
    print(f"the score of {player2} = {score2}")
    temp = player1
    player1 = player2
    player2 = temp
    temp = score1
    score1 = score2
    score2 = temp
    return main(player1, player2, score1, score2)

# the main program
score1 = 0
score2 = 0
print("Hey guys this is the hanging game game, i hope you enjoy it you and your opponent XD!!")
player1 = input("player 1: the word teller, please enter your name =>")
player2 = input("player 2: the word guesser, please enter your name =>")
print(f"""*******************************************************************
okay {player1} and {player2} ,here we go, bellow are the rules:
+ Words without spaces are the only accepted ones.
+ No numbers at the word are accepted.
+ ONLY LETTERS""")

main(player1, player2, score1, score2)
