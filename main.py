
# ******************************
# Make your Code
# ******************************
list=[]
minval=10000000000000
maxval=-1
totalInps=0
totalSum=0
while totalInps<5:
    inp=int(input("Value?"))
    totalSum=totalSum+inp
    list.append(inp)
    if list[totalInps]>maxval:
        maxval=list[totalInps]
    if list[totalInps]<minval:
        minval=list[totalInps]
    totalInps=totalInps+1
totalSum=totalSum-maxval-minval
print(totalSum)
