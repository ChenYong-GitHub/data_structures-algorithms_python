def merge_sort(arr):
    # 如果列表为空或只有一个元素，则无需排序
    if len(arr) <= 1:
        return arr
    
    # 分割列表为两个子列表
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 递归调用归并排序函数，对两个子列表分别排序
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # 合并两个已排序的子列表
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i, j = 0, 0
    # 合并两个已排序的子列表
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 将剩余的元素添加到结果列表中
    result += left[i:]
    result += right[j:]
    return result



arr = [4, 2, 6, -4, -6, 66]
sorted_arr = merge_sort(arr)
print(sorted_arr)