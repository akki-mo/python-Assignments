def get_unique_elements(input_list):
    unique_elements = []
    encountered = set() 
    for num in input_list:
        if num not in encountered:
            unique_elements.append(num)
            encountered.add(num)
    return unique_elements


input_list = [1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8]
unique_elements = get_unique_elements(input_list)
print(unique_elements)
