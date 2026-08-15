def solution(phone_book):
    answer = True
    solSet = set(phone_book)
    
    for number in phone_book:
        for i in range(1,len(number)):
            if number[:i] in solSet:
                answer = False
                break;
    
    return answer