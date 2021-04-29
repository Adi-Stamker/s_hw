# targil 4
# check if id valid
def check_id(id):
    string = id[0:8]
    temp = 1
    sum = 0
    x = 0
    for num in string:
        x = int(num)*temp
        if x > 9:
            x = x % 10 + int(x / 10)
        sum += x
        if temp == 1:
            temp = 2
        else:
            temp = 1

    round_num = sum - sum % 10 + 10

    if round_num - sum == int(id[8]):
        return True
    return False


id = '543700421'
if check_id(id):
    print("ID is valid")
else:
    print("ID is not valid")