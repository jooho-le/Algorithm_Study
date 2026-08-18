from collections import deque

def solution(priorities, location):
    answer = 0
    solQueue = deque([(idx, num) for idx, num in enumerate(priorities)])
    
    while solQueue:
        base = solQueue.popleft()
        if solQueue and max([t[1] for t in solQueue]) > base[1]:
            solQueue.append(base)
        else:
            answer +=1
            if base[0] == location:
                return answer