# targil 3
# shorten string
def short_str():
    stri = input('Enter string:')
    new_str = ''
    count = 1
    for i in range(len(stri) - 1):
        if stri[i] == stri[i+1]:
            count+=1
        else:
            new_str+= stri[i] + str(count)
            count = 1
    if len(stri):
        new_str+= stri[-1] + str(count)
    print ("new string is: " + new_str)

short_str()