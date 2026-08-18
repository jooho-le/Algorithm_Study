import math

def solution(progresses, speeds):
    answer = []
    solList = []
    counter = 0
    
    for prog, speed in zip(progresses, speeds):
        solList.append(math.ceil((100 - prog)/speed))
    
    baseDay = solList[0]    
    
    for day in solList:
        
        if day <= baseDay: 
            counter+=1
        else:
            answer.append(counter)
            counter = 1
            baseDay = day
            
    answer.append(counter)
            
    return answer