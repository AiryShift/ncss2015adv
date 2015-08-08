def list_calculator(list1, list2, operator):
    if operator == '+':
        return [i + j for i, j in zip(list1, list2)]
    return [i - j for i, j in zip(list1, list2)]
