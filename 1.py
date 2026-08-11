## 완주하지 못한 선수 

## 문제 
## 단 한명 제외하고 모든 선수가 마라톤 완주 
## 참여한 선수 이름 배열 : participant
## 완주한 선수 이름 배열 : completion
## 완주하지 못한 선수 이름을 return하는 solution함수 작성 
## completion길이 + 1 = participant길이
## 참가자중 동명이인 존재 가능 
## 참가자 이름 = 알파벳 소문자 

def solution(participant, completion):
    participant_count = {}
    completion_count = {}

    # 참가자 빈도수 계산
    for name in participant:
        participant_count[name] = participant_count.get(name, 0) + 1

    # 완주자 빈도수 계산
    for name in completion:
        completion_count[name] = completion_count.get(name, 0) + 1

    # 참가자 수 - 완주자 수가 1인 선수 찾기
    for name in participant_count:
        if participant_count[name] - completion_count.get(name, 0) == 1:
            return name