# _*_ coding: utf-8 _*_   # --> chinese user must firstly declare coding 
# Quick Python Script Explanation for Programmers 
import os

def main(): 
    print('Hello world!')
    print('this jerry\'s greet.')

    foo(5, 10)

    print('=' * 10)
    print('excute ' + os.getcwd())

    counter = 0
    counter += 1
    food = ['apple', 'orange', 'banana']
    for i in food:
        print('i like ' + i)

    print('count to 10')
    for i in range(10):
        print(i)

def foo(param1, param2):
    res = param1+param2
    print('%s + %s = %s' %(param1,param2,res))
    if res < 50:
        print('this')
    elif (res>=50) and ((param1==42) or (param2==24)):
        print('that')
    else:
        print('and...')
    return res
    

if __name__=='__main__':
    main()
