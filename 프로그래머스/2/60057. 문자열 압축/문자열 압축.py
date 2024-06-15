from collections import deque

def solution(s):
    answer = len(s)
    
    for i in range(1, (len(s) // 2) + 1):
        start_i = 0
        stack = []
        total_str = []
        
        flag = True
        while flag:
            if start_i + i > len(s):
                cur_str = s[start_i:]
                flag = False
            else:
                cur_str = s[start_i:start_i+i]
                if start_i + i == len(s):
                    flag = False
            start_i += i
            #print("cur_str " + cur_str)
            
            if stack:
                if stack[-1] == cur_str:
                    stack.append(cur_str)
                else:
                    count = 0
                    while stack:
                        count += 1
                        pre_str = stack.pop()
                    stack.append(cur_str)
                    if count == 1:
                        total_str.append(pre_str)
                    else:
                        total_str.append(str(count) + pre_str)
            else:
                stack.append(cur_str)
        
        if stack:
            count = 0
            while stack:
                count += 1
                pre_str = stack.pop()
            if count == 1:
                total_str.append(pre_str)
            else:
                total_str.append(str(count) + pre_str)
        
        total = ''.join(total_str)
        #print("total_str " + total)
        answer = min(answer, len(total))
        
    return answer
            
       
        