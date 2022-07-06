def student_solution(list1):
    new_list = set(list1)
    new_list.remove(max(new_list))
    return list1
