def selectionsort(list):
    length=len(list)
    while length != 1:
        max=0
        for i in range(1,length):
            if list[i]>list[max]:
                max=i
            else:
                continue
        list[max],list[length-1]=list[length-1],list[max]
        length=length-1
    return list
    
a=[5,8,7,97,2,4,8,10]
print(selectionsort(a))
