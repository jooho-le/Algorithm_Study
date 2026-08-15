def solution(participant, completion):
    answer = ''
    solDict = {}
    for i in participant:
        solDict[i] = solDict.get(i,0) + 1
    
    for i in completion:
        solDict[i] -= 1
    
    for name,solCount in solDict.items():
        if solCount != 0:
            answer = name
            break
            
    return answer
