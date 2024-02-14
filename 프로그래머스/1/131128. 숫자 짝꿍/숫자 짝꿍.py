def solution(X, Y):
    # 짝궁.. 중복 가능 짝궁을 큰수대로 나열
    count_X = {}
    count_Y = {}
    for x in X:
        count_X[x] = count_X.get(x, 0) + 1
    for y in Y:
        count_Y[y] = count_Y.get(y, 0) + 1
    
    answer = []
    
    for n in "9876543210":
        if n in count_X and n in count_Y:
            min_count = min(count_X[n], count_Y[n])
            answer.extend([n] * min_count)
    
    if not answer:
        return "-1"
    
    if answer[0] == "0":
        return "0"
    
    return ''.join(answer)