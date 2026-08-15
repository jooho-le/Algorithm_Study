import collections
import math

def solution(clothes):
    answer = 0
    solDict = collections.Counter(style for _ , style in clothes)
    answer = math.prod(num + 1 for num in solDict.values()) - 1
    
    return answer