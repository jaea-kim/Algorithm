def solution(survey, choices):
    choiceN = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    points = {"R": 0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for s, c in zip(survey, choices):
        if c < 4:
            points[s[0]] = points[s[0]] + choiceN[c]
        elif c > 4:
            points[s[1]] = points[s[1]] + choiceN[c]
    
    indicators = ["RT", "CF", "JM", "AN"]  
    answer = ""

    for i,j in indicators:
        if points[i] < points[j]:
            answer = answer + j;
        else:
            answer = answer + i;
    
    return answer