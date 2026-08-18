def solution(arr):
    answer = []
    for num in arr:
        if not answer or answer[-1] != num: # 마지막 원소 보는게 Python에서는 answer[-1]로 쓰임
            answer.append(num)
    return answer