## 의상

## 문제 
## 매일 다른 옷을 조합하여 입음 
## 종류 : 얼굴, 상의, 하의, 겉옷
## 각 종류별로 최대 1가지의 의상만 착용 
## 착용한 의상 일부가 겹치더라도 다른 의상이 겹치지 않거나, 의상을 추가로 더 착용한 경우 가능
## 하루 최소 한개의 의상을 입음 
## clothes : 가지고 있는 의상인 2차원 배열 
## 서로 다른 옷의 조합의 수를 리턴하는 solution함수 작성

## clothes = [의상의 이름, 의상의 종류] , 모든 원소는 문자열 
## 의상의 수 : 1 <= <=30
## 같은 이름의 의상 없음 

## 입출력 예
## [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
## -> 
## 1. yellow_hat
## 2. blue_sunglasses
## 3. green_turban
## 4. yellow_hat + blue_sunglasses
## 5. green_turban + blue_sunglasses

## [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3
## -> 
## 1. crow_mask
## 2. blue_sunglasses
## 3. smoky_makeup

def solution(clothes):
    counts = {}

    # 1. 의상 종류별 빈도수 계산
    for name, category in clothes:
        counts[category] = counts.get(category, 0) + 1

    # 2. 조합 계산
    answer = 1

    for count in counts.values():
        answer *= (count + 1)

    # 3. 아무것도 입지 않는 경우 제외
    return answer - 1