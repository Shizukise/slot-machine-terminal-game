import random

ourSymbols = {1 : "$" , 2 : "Ace", 3 : "Pot", 4 : "Cereja", 5 : "K", 6 : "j", 7: "Poker"}


acc_balance = int(input("Enjoy the slot machine! First, how much do you want to deposit? "))

#print(balance)
player_balance = acc_balance

#function to retrieve 3 random numbers from 1 to 7

def rowscore():
        scores = []
        scores.append(random.randint(1, 7))
        scores.append(random.randint(1, 7))
        scores.append(random.randint(1, 7))
        return scores

#function to convert the numbers into our slot symbols

def symbolconversion(ourlist):
        play = []
        for number in ourlist:
           if number in ourSymbols:
               play.append(ourSymbols[number])
        return play

#variable to hold the 3 random numbers
#play = rowscore()

#variable that contains the result of converting the numbers into symbols
#slotrow = symbolconversion(play)

def prize(play):
    for symbol in play:
        if play.count(symbol) == 3:
            return "Jackpot"
        elif play.count(symbol) > 1:
            return "Two of a Kind"
    else:
        return "Better luck next time" 
   
#prize variable below, contains the function prize that takes as parameter the variable with the symbols converted. 
#prize = prize(play)

#print(slotrow)
#print(slotrow)
#print(prize)


class Player:
     

    def __init__(self,name, balance):
          
        self.balance = balance
        self.name = name

    def welcoming(self):
        print("Hello {name}! Your current balance is {balance}".format(name = self.name, balance = self.balance))















player1 = Player("Maikal",player_balance)
player1.welcoming()

