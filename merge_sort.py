#coding by Pasindu Weerasinghe
def mergesort(list1,list2):
    list3=[]
    a=0
    b=0
    while  a != len(list1) or   b != len(list2):
        if b==len(list2) and a<len(list1):
            list3.append(list1[a])
            a+=1
        elif a==len(list1) and b<len(list2):
            list3.append(list2[b])
            b+=1
        elif list1[a]<list2[b]:
            list3.append(list1[a])
            a+=1
        else:
            list3.append(list2[b])
            b+=1
    return list3

a=[3,5,9,22]
b=[0,12,20,40,60]

print(mergesort(a,b))
