#using while loop
pos=1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    else:
        return false
list=[5,8,4,6,9,2]
n=int(input('enter the no u want to search'))

if search(list, n):
    print('found at',pos)
else:
    print('not found')
