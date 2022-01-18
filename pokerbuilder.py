import random
from os import system
from colorama import init, Fore, Back, Style

# a=b'hellothere'

# for i in a:
#     print(i)

menutext="""***** Make a move cowboy *****

1) Next Turn
2) Deal a Card and bet 10
3) deal the flop
q) quit
"""

init()

def banner():
    # system('cls')
    with open("menus/menu1.txt", 'r') as f:
        banner = f.read()
        print(banner)
    

def builddeck():
    cardnums=[1,2,3,4,5,6,7,8,9,10,11,12,13]
    cardsuits=[1,2,3,4]
    deck=[]
    for num in cardnums:
        for suit in cardsuits:
            deck.append([num,suit])
    print(deck)
    return(deck)

def printCards(a):
    output=""
    for i in a:
        if i[0]==1:
            value="A"
        elif i[0]==10:
            value="T"
        elif i[0]==11:
            value="J"
        elif i[0]==12:
            value="Q"
        elif i[0]==13:
            value="K"
        else:
            value = str(i[0])
        if i[1]==1:
            suit="♥"
            col=f'{Fore.RED}'
        if i[1]==2:
            suit="♣"
            col=f'{Fore.BLACK}'
        if i[1]==3:
            suit="♦"
            col=f'{Fore.RED}'
        if i[1]==4:
            suit="♤"
            col=f'{Fore.BLACK}'
            
        # print(f'{value} of {suit}', end = " ")
        back=f'{Back.WHITE}'
        output=output+f'{back}{Fore.BLACK}{value}{col}{suit}{Style.RESET_ALL} '
    return(output)
    


class board:
    def __init__(self):
        self.cards=[]
        self.balance=0


class deck:

    def __init__(self):
        self.cards = builddeck()
        print('self.cards=builddeck()')
    
    def shuffle(self):
    
        random.shuffle(self.cards)

    def deal(self, target):
        a=self.cards.pop()
        target.cards.append(a)



    
class player:
    def __init__(self):
        self.balance=500
        self.cards=[]

    def betTen(self,target):
        self.balance=self.balance-10
        target.balance=target.balance+10



a = deck()
a.shuffle()
rob = player()
rob.balance=50
pit=board()

banner()
loopquitter=0
print('\r\n\r\n\r\n')


while loopquitter !='q':
    system('cls')
    banner()
    # print("The Deck!\r\n")
    # print(printCards(a.cards))
    print("Your Hand!\r\n")
    print(printCards(rob.cards))
    print('\r\n')
    print(f"Rob's balance is: {rob.balance}")
    print(f"Board's balance is {pit.balance}")
    print(f"Board's cards are: {printCards(pit.cards)}", end="")
    print('\r\n')
    print(menutext)
    # print(f'Output: {printCards(rob.cards)}')
    loopquitter=input("enter the next move: ")
    if loopquitter=="2":
        a.deal(rob)
        rob.betTen(pit)
    if loopquitter=="3":
        for i in range(3):
            a.deal(pit)
        