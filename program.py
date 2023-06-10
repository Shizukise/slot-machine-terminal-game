import random

ourSymbols = {1 : "$" , 2 : "Ace", 3 : "Pot", 4 : "Cereja", 5 : "K", 6 : "j", 7: "Poker"}

class SlotPlay:

    def __init__(self,number,symbol,bonus,jackpot):
        

        self.symbol = symbol
        self.bonus = bonus
        self.jackpot = jackpot
        self.number = number

####  vvvv  Function to give us 3 random number, numbers that later will be converted to symbols
    def rowscore(self):
        scores = []
        scores.append(random.randint(1, 7))
        scores.append(random.randint(1, 7))
        scores.append(random.randint(1, 7))
        return scores
### vvv convert the random number list into a random symbol combination
    def symbolconversion(self,ourlist):
        play = []
        for number in ourlist:
           if number in ourSymbols:
               play.append(ourSymbols[number])
        return play
               




#below needs and object of this class done to work
moneysymbol = SlotPlay(1,"%",3,7)
score = moneysymbol.rowscore()

print(score)

#we use the symbolconversion function with the rowscore function as parameter


playrow = moneysymbol.symbolconversion(score)

test = [3,3,3]

#trying to make the prize action for duplicates and 3 in a row

def prize(play):
    for symbol in play:
        if play.count(symbol) == 3:
            return "Jackpot"
        elif play.count(symbol) > 1:
            return "Two of a Kind"
    else:
        return "Better luck next time" 
      

print(prize(playrow))


