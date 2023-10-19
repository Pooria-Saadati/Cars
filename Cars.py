loop, length = input().split(" ")
numofcars = input()
loop = int(loop)
length = int(length)
numofcars = int(numofcars)
timeloss = dict()
speed = dict()
for i in range(0,numofcars):
    x, y = input().split(" ")
    int(x)
    int(y)
    timeloss[i] = x
    speed[i] = y
resault = dict()
for i in range(0,numofcars):
    resault[int(timeloss[i]) + (loop * length)/int(speed[i])] = i
    # print(resault[i])
print(1+resault[min(resault)])