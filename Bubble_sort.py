#coding by Pasindu Weerasinghe
def bubblesort(list):
    length=len(list)
    while length != 1:
        for i in range (length-1):
            if list[i]>=list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
            else:
                continue
            
        length=length-1
    return list

a=[5,8,7,97,2,4,8,10]
print(bubblesort(a))
