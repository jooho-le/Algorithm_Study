
def solution(prices):
    answer = [0] * len(prices)
    solStack = []
    
    for i in range(len(prices)):
        while solStack and prices[solStack[-1]] > prices[i]:
            idx = solStack.pop()
            answer[idx] = i - idx
        solStack.append(i)
        
    while solStack:
        idx = solStack.pop()
        answer[idx] = (len(prices)-1) - idx
        
    return answer