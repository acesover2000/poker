mylist = ["a","b","c","d","e","f","g","h"]

def printCards(bundle):
    print(bundle)
    a=0
    for i in bundle:
        print(f'{a}\t{i}')
        a=a+1


class Master:
    def __init__(self):
        self.inventory=mylist
    
    def givecard(self,target):
        a=self.inventory.pop()
        target.inventory.append(a)
        print(f"Popping self.inventory.pop(): {a}")


class Player:
    def __init__(self):
        self.inventory=[]
    
    # def addCard(self,card):
    #     self.inventory.append(card)

b={}
for i in range(2):
    b[i]=Player()

deck=Master()
print("deck has")
printCards(deck.inventory)

for i in b:
    print(f"Player {i} has {printCards(b[i].inventory)}")
print(b[0].inventory)
deck.givecard(b[0])
print(b[0].inventory)

print("deck has")
printCards(deck.inventory)

for i in b:
    print(f"Player {i} has {printCards(b[i].inventory)}")