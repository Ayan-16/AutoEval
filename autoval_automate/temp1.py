#Beginning of Golden Solution
def golden_solution(list1):
    mx = max(list1[0], list1[1])
    secondmax = min(list1[0], list1[1])
    n = len(list1)
    for i in range(2,n):
        if list1[i] > mx:
            secondmax = mx
            mx = list1[i]
        elif list1[i] > secondmax and mx != list1[i]:
            secondmax = list1[i]
        elif mx == secondmax and secondmax != list1[i]:
            secondmax = list1[i]
    return list1

#End of Golden Solution
#Beginning of Student Solution
def student_solution(list1):
    return list1
#End of Student Solution




#Beginning of main method
from itertools import *
import numpy as np
def char_range(c1, c2):
	for c in range(ord(c1), ord(c2)+1):
		yield chr(c)
def checker():
	check_equal=True
	for j in list(map(list,(permutations(range(1,6),3)))):
			if (golden_solution(j)!=student_solution(j)):
				check_equal=False
				print("\"Solution by student is wrong on case:",end=" ")
				print(j,end=" ")
				print("\"},")
				return 0
	if(check_equal==True):
		print("\"Solution by student is correct\"},")
checker()
#End of main method




