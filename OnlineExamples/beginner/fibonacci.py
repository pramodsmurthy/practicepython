"""
Print fibonacci numbers
"""

def get_next_fibo_num(fibo_list):
    return fibo_list[-1] + fibo_list[-2]

fibo_list = [ 1, 1 ]
num = int(input("Enter the number of fibonacci numbers required: "))
if num == 1:
    print([1])
elif num == 2:
    print(fibo_list)
else:
    count = 0
    while count < num - 2:
        fibo_list.append(get_next_fibo_num(fibo_list))
        count += 1
    print(fibo_list)