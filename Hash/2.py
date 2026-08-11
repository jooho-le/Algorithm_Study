## 포켓몬

## 문제 
## N마리의 포켓못 중 N/2마리를 가져감 
## 종류에 따라 번호 부여 되어있음 -> 같은 종류의 포켓몬은 같은 번호
## 최대한 많은 종류의 포켓몬을 포함해 N/2마리를 가지고 싶음
## nums : N마리 포켓몬 종류 번호가 담긴 배열
## 가져간 포켓몬 종류 번호의 개수를 리턴 
## 예시 
## [3,1,2,3]	2
## [3,3,3,2,2,4]	3
## [3,3,3,2,2,2]	2

def solution(nums):
    # 1. set으로 중복 제거
    pokemon_set = set(nums)

    # 2. 서로 다른 폰켓몬 종류 수
    kind_count = len(pokemon_set)

    # 3. 가져갈 수 있는 폰켓몬 수
    select_count = len(nums) // 2

    # 4. 두 값 중 더 작은 값 반환
    return min(kind_count, select_count)