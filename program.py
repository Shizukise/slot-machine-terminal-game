import random

ourSymbols = {1 : "$" , 2 : "Ace", 3 : "Pot", 4 : "Cereja", 5 : "K", 6 : "j", 7: "Poker"}

print(" ")
print(" ")
print(" ")

print("Welcome to Terminal Casino!")
print("---------------------------")
print("You will be playing our slot machine!")

print(" ")
print(" ")

player1name = input("First, please tell me your name : ")

print(" ")

acc_balance = int(input("Enjoy the slot machine! How much do you want to deposit? "))

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


def prize(play):
    for symbol in play:
        if play.count(symbol) == 3:
            return "Jackpot"
        elif play.count(symbol) > 1:
            return "Two of a Kind"
    else:
        return "Better luck next time" 
   
#prize variable below, contains the function prize that takes as parameter the variable with the symbols converted. 


#print(slotrow)
#print(slotrow)
#print(prize)






class Player:
     

    def __init__(self,name, balance):
          
        self.balance = balance
        self.name = name

    def welcoming(self):
        print("--------------------------------------------------------")
        print(" ")
        print("Hello {name}! Your current balance is {balance}.".format(name = self.name, balance = self.balance))



class SlotGame:


    def __init__(self,player,saldo,):
         
        self.player = player
        self.saldo = saldo
        self.bet = 0


    #here we will store the row of symbols converted to a string already in a variable, and depending on the string we get,
    #the multiplier differs.

    def place_bet(self,margin,):
        
        margin = self.saldo
        cbalance = margin
        print(slotrow)
        print(multiplier)
        if player_bet <= cbalance and multiplier == "Better luck next time":
            cbalance = cbalance - player_bet
            self.saldo = cbalance
            print("Your current balance is {n}.".format(n = cbalance))
            print(" ")
            return self.saldo
        elif player_bet <= cbalance and multiplier == "Two of a Kind":
            cbalance += (player_bet * 1.50)
            print("You got {pot} from your bet!".format(pot = int(player_bet * 1.50)))
            print(" ")
            self.saldo = cbalance
            print("Your current balance is {n}.".format(n = cbalance))
            return self.saldo
        elif player_bet <= cbalance and multiplier == "Jackpot":
            cbalance += ( player_bet * 2)
            print("You got {pot} from your bet!".format(pot = int(player_bet * 2)))
            print(" ")
            self.saldo = cbalance
            print("Your current balance is {n}.".format(n = cbalance))
            print(" ")
            return self.saldo
        elif player_bet > cbalance:
             return "You have insufficient funds for this bet."



player1 = Player(player1name,player_balance)
player1.welcoming()

game1 = SlotGame(player1,player1.balance)

print(" ")

player_input = input("Do you want to bet? ")

print(" ")




if player_input == "yes".lower() or player_input == "y".lower():
    
    count = int(input("How many rolls you want to go for? "))
    print(" ")
    player_bet = int(input("How much do you want to bet? "))
    print(" ")
    print("Excelent! you will be rolling the slot machine {count} times!".format(count = count))
    print(" ")
    while count > 0:
        for fois in range(0,count):
            play = rowscore()
            slotrow = symbolconversion(play)
            multiplier =  prize(symbolconversion(play))
            game1.place_bet(game1.player)
            count = count - 1
else:
        print("You can come back and play anytime you want")

print(" ")
print(" ")
print(" ")

print("Your final balance is {balance}!".format(balance = game1.saldo))
