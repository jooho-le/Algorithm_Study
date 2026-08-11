## 문제 

## 전화번호 목록 중 한 번호가 다른 번호의 접두어인 경우를 확인 
## phone_book : 전화번호 배열 -> solution함수의 매개변수 
## 어떤 번화가 다른 번호의 접두어인 경우가 있으면 -> false, 없으면 -> true 반환 

def solution(phone_book):
    phone_set = set(phone_book)

    for phone in phone_book:
        for i in range(1, len(phone)):
            prefix = phone[:i]

            if prefix in phone_set:
                return False

    return True