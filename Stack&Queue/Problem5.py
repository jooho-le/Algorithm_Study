from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waitTruckQueue = deque(truck_weights)
    bridgeQueue = deque([0] * bridge_length)
    weightSum = 0
    
    while weightSum != 0 or waitTruckQueue:
        answer += 1
        base = bridgeQueue.popleft()
        weightSum -= base
        if waitTruckQueue and weightSum + waitTruckQueue[0] <= weight:
            truck = waitTruckQueue.popleft()
            weightSum += truck
            bridgeQueue.append(truck)
        else:
            bridgeQueue.append(0)
    return answer