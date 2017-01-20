#coding by Pasindu Weerasinghe
def insersionsort(list):
    length=len(list)
    for i in range (1,length):
        temp=list[i]
        j=i-1
        while temp<list[j] and j>=0:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=temp
    return list

b=[5,8,7,97,2,4,8,10]
print(insersionsort(b))
