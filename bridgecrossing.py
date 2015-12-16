initList =[10,2,1,5]
notCrossed=sorted(initList)
crossed=[]
crossing=[]
n=len(initList)

def sendFastestOver():
    notCrossed.sort()
    crossing.extend([notCrossed[1]])
    crossed.extend([notCrossed[0],notCrossed[1]]) 
    notCrossed.remove(notCrossed[0])
    notCrossed.remove(notCrossed[0])
    m=len(notCrossed)
    
def sendFastestBack():
    crossed.sort()
    crossing.extend([crossed[0]])
    notCrossed.extend([crossed[0]]) 
    crossed.remove(crossed[0])
    m=len(notCrossed)
 
def sendSlowestOver():
    notCrossed.sort()
    crossing.extend([notCrossed[-1]])
    crossed.extend([notCrossed[-1]])
    crossed.extend([notCrossed[-2]])
    for x in range(2):
        notCrossed.remove(notCrossed[-1]) 
    
#while len(crossed)<n:
    #sendFastestOver()
    #sendFastestBack()
    #sendSlowestOver()
    #sendFastestBack()

sendFastestOver()
sendFastestBack()
sendSlowestOver()
sendFastestBack()
sendFastestOver()

print(sum(crossing))
print(notCrossed)
print(crossing)
print(crossed)
