""" 4
****
*  *
*  *
****
"""
while True:
    num = int(input('请输入数字:'))
    if num == 1:
        print('*')
    if num == 2:
        print('**')
    print('*'*num)
    for item in range(num-2):
        print('*'+' '*(num-2) + '*')
    print('*'*num)