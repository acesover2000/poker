from operator import itemgetter
from straight import straightfinder

cards=[[1,2],[2,3],[3,3],[5,2],[4,4],[6,2],[3,1],[2,1]]




def evalHand(cards):
    cards.sort(key=itemgetter(0),reverse=True)
    print(f'{cards = }')
    print(set(i[0] for i in cards))
    valcounter=[]
    for i in set(i[0] for i in cards):
        count = 0
        for a in cards:
            if i==a[0]:
                count = count+1
        valcounter.append([i,count])
    valcounter.sort(key=itemgetter(1,0),reverse=True)
    print(f'{cards = }     {valcounter = }')
    print(valcounter)
    if valcounter[0][1] == 5:
        print(f"5 of a kind {valcounter[0][0]}'s (you cheater)")
    elif valcounter[0][1] == 4:
        print(f"4 of a kind {valcounter[0][0]}'s")
    elif valcounter[0][1] == 3 and valcounter[1][1] == 2:
        print(f"full house {valcounter[0][0]}'s full of {valcounter[1][0]}'s")
    elif straightfinder(cards)[0]:
        print(f'{straightfinder(cards) = }')
        print(f'Straight! {straightfinder(cards)[1]}')
    elif valcounter[0][1] == 3:
        print(f"3 of a kind {valcounter[0][0]}'s")
    elif valcounter[0][1] == 2 and valcounter[1][1] == 2:
        print(f"Two pair {valcounter[0][0]}'s and {valcounter[1][0]}'s")
    elif valcounter[0][1] == 2:
        print(f"Pair of {valcounter[0][0]}'s")
    else:
        print(f"High card, {valcounter[0][0]}")
evalHand(cards)
