def sum_L_H_odd(list):
    
    length=len(list)
    odd_list=[]

    for i in range(0,length):

        if list[i] % 2 != 0:

            odd_list.append(list[i])

    if len(odd_list) != 0:

        min_odd=min(odd_list)
        max_odd=max(odd_list)

    else:

        min_odd=0
        max_odd=0

    total_odd_sum=min_odd+max_odd
    return total_odd_sum

print(sum_L_H_odd([1,3,5,7,9]))
