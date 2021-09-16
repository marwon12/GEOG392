## Lab 2
## Marwon Haridi

## Part 1
## Take the following list and multiply all list items together.
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
total = 1
for x in range(0, len(part1)):
    total = total*part1[x]
print ("The total off multiplying all the elements in the list is:",total)

## Part 2
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
sum = 0
for x in range(0, len(part2)):
    sum = sum + part2[x]
print ("The sum off all the elements in the list is:",sum)

## Part 3
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
evenSum = 0
for x in range(0, len(part3)):
    if (part3[x] % 2 == 0):
        evenSum = evenSum + part3[x]
print ("The sum off all even elements in the list is:",evenSum)