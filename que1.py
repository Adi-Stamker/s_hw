# sum of list a 1.a
def sum_list1():
    sum_nums = 0
    num = input('Enter number or stop:')
    while num != "stop":
        sum_nums += int(num)
        num = input('Enter Number or stop:')
    print("sum of list: ", sum_nums)

# sum of list b 1.b
def sum_list2():
    lst = input('Enter list of numbers (divided by ,):')
    ans = lst.split(',')
    sum_nums = 0
    for item in ans:
        sum_nums+= int(item)
    print("sum of list: ", sum_nums)

sum_list1()
sum_list2()