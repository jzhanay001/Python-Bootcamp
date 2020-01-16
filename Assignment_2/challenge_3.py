def extract_num(string):
    str_num = []

    for char in string:
        if char.isdigit() is True:
            str_num+=char


    length=len(str_num)
    int_num=[]

    if length != 0:
        for i in range(0,length):
            int_list=int(str_num[i])
            int_num.append(int_list)

    return int_num

Input_list = extract_num ("Pi is approximately")

print(Input_list)
