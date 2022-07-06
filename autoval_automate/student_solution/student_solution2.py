
    
def student_solution(list1):
    secondmax = min(list1[0], list1[1])
    mx = max(list1[0], list1[1])
    for i in range(2,len(list1)):
        if list1[i] < mx:
            secondmax = mx
            mx = list1[i]
        elif list1[i] < secondmax and mx != list1[i]:
            secondmax = list1[i]
        elif mx == secondmax and secondmax != list1[i]:
            secondmax = list1[i]
    return list1