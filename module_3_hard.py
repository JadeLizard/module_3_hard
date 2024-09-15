def summ(data):
    result = 0
    if isinstance(data, (int, float)):
        result += data
    elif isinstance(data, str):
        result += len(data)
    elif isinstance(data, (list, tuple, set)):
        for el in data:
            result += summ(el)
    elif isinstance(data, dict):
        for i in data.items():
            result += summ(i)
    return result

data = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
print(summ(data))
