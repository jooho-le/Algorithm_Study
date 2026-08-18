def solution(s):
    answer = True
    solStack = []
    
    for bracket in s:
        if bracket == '(':
            solStack.append(bracket)
        else:
            if(not solStack): # 어치파 else 구문 들어온 시점부터 )인게 확정이니 굳이 조건문에 넣을 필요 없다...
                answer = False
                break
            solStack.pop()
            
    if solStack:
        answer = False

    return answer