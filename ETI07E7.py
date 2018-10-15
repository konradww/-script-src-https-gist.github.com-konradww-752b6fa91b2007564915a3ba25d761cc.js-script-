my_list = []
f = open("test1.txt", "r")
for counter, value in enumerate(f):
    if counter == 0:
        total_item, size1, size2 = map(int, value.split())
    else:
        item1, item2 = map(int, (value.split()))
        my_list.append([item1, item2])
print(my_list)
print('*' * 100)
my_list = (sorted(my_list, key= (lambda x: x[0]), reverse=True))


def packing(size_packing, total_item):
    result = []
    size = int(size_packing)
    min_size_items = []
    max_point_items = []

    for i in range(0,len(total_item)):
        while size > 0 and len(total_item) != 0:
            if len(max_point_items) == 0:
                max_point_items.append(total_item[0])
            else:
                if total_item[i][0] > max_point_items[-1][0]:
                    max_point_items[-1][0] = total_item[i][0]
                elif total_item[i][0] == max_point_items[-1][0]:
                    max_point_items.append(total_item[i])
                else:
                    pass

            min_size_items = (sorted(max_point_items, key=(lambda x: x[1])))
            if size >= min_size_items[0][1]:
                size = size - min_size_items[0][1]
                result.append(min_size_items[0])
                total_item.remove(min_size_items[0])
                max_point_items.remove(min_size_items[0])
                min_size_items.remove(min_size_items[0])
            else:
                pass


    return result

print(packing(size1, my_list))


