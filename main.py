
# ******************************
# Make your Code
# *****************************
numbers=[]
minval=1000000000000000
maxval=-1000000000000000
totalInps=0
totalSum=0
while totalInps<5:
    inp=int(input("Value?"))
    totalSum=totalSum+inp
    numbers.append(inp)
    if numbers[totalInps]>maxval:
        maxval=numbers[totalInps]
    if numbers[totalInps]<minval:
        minval=numbers[totalInps]
    totalInps=totalInps+1
totalSum=totalSum-maxval-minval
print(totalSum)
