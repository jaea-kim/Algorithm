from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = [sum1, sum2]
    
    target = (total[0] + total[1]) // 2
    
    if (total[0] + total[1]) % 2 != 0:
        return -1 
    
    index = 1
    answer = [0, 0]
    for i in range(2):
        q = [deque(queue1), deque(queue2)]
        count = 0
        while count <= 2 * len(queue1) + 2:
            if total[i] > target:
                v = q[i].popleft()
                q[index].append(v)
                total[i] -= v
                count += 1
            elif total[i] < target:
                v = q[index].popleft()
                q[i].append(v)
                total[i] += v
                count += 1
            else:
                answer[i] = count
                break
                
        if total[i] != target:
            return -1
        
        index = 0
    
    return min(answer)