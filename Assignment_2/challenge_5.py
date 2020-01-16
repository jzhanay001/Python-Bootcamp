def sum_4(list):
    first_4_sum=sum(list[:4])
    last_4_sum=sum(list[1:5])
    New_list=[first_4_sum,last_4_sum]
    return New_list

print(sum_4([2,4,6,8,10]))
