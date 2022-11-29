#biggest of four numbers
a=int(input('enter number:'))
b=int(input('enter number:'))
c=int(input('enter number:'))
d=int(input('enter number:'))
if a>b:
    if a>c:
        if a>d:
            print('a is big')
if b>c & b>d & b>a:
    print('b is big')
if c>d & c>a & c>b:
    print('c is big')
if d>a & d>b & d>c:
    print('d is big')
