#accept 3 subjets marks if student gets min 30 in all subjects then find average else print fail
sub1,sub2,sub3=map(int,input().split())
print(sub1,sub2,sub3)
tm=sub1+sub2+sub3
print("Total marks are : ",tm)
avg=tm/3
print("Average marks are: ",avg)
if avg>=75:
    print("A Grade")
elif avg<60 and avg>75:
    print("B Grade")
elif avg>45 and avg<60:
    print("C Grade")
elif avg>30 and avg<45:
    print("D Grade")
else :
    print("f")
