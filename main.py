def sort(elements):
    i = 0
    while i < len(elements):

        j = 0
        while j < len(elements) - 1:

            if elements[j] > elements[j+1]:
                temporary_element = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temporary_element
            j += 1
        i += 1

    return elements


none_sorted_elements = [3, 2, 4, 1]
print('Before: ' + str(none_sorted_elements))
sorted_elements = sort(none_sorted_elements)
print('After:  ' + str(sorted_elements))
