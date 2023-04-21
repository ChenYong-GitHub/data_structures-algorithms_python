def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort2(left) + [pivot] + quick_sort2(right)
    
    
def quick_sort3(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    middle = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else :
            right.append(x)
    return quick_sort3(left) + middle + quick_sort3(right)
                

# test demo 1
# * It is very important
# ! hello 
# ? TODO what are you nongshanie?
# TODO let go!
# @param this param 
arr1 = [1, 6, 7, -3, -6, 2]   
quick_sort(arr1)
print(quick_sort(arr1))

arr2 = [1, 1, 6, 7, -3, -6, 2]   
print(quick_sort2(arr2))

print(quick_sort3(arr2))