cards=[[1,2],[2,3],[3,3],[1,4],[5,3],[6,2],[10,2],[3,2],[4,1],[7,1]]

with open('logs.txt','w') as f:
    pass

def logme(text):
    with open('logs.txt','a') as f:
        f.write(f'{text}\r')
    


def HighStraightFromVals(vals):
    # print(f'{vals = }')
    stacked=[]
    for i in range(len(vals)):
        stacked.append([vals[i]+i])
    # print(f'{stacked =}')
    for i in range(len(stacked)):
        try:
            for j in range(1,6):
                # print(f'if {stacked[i]}!={stacked[i+j]}:')
                if stacked[i]!=stacked[i+j]:
                    straight=False
                    break
                else:
                    straight=True
            if straight:
                logme(f'found a straight, {vals[i]} high')
                return([True,vals[i]])
                break
        except Exception as e:
            pass
    return([False,None])

        

def straightfinder(hand):
    # print(f'{hand =}')
    valslist=[]
    selectedstraight=[]
    for i in range(len(hand)):
        valslist.append(hand[i][0])
    b=list(set(sorted(valslist)))
    b.reverse()
    response=HighStraightFromVals(b)
    # print(f'{response = }')
    straightcounter=0
    if response[0]:
        for i in range(5):
            for j in hand:
                # print(f'if i[0]==response[1]+straightcounter:  {j[0]}=={response[1]}+{straightcounter}')
                if j[0]==response[1]-straightcounter:
                    selectedstraight.append(j)
                    straightcounter=straightcounter+1
                    # print(selectedstraight)
                    break
    print(selectedstraight)
    return([True,selectedstraight])

