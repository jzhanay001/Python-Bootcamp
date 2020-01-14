counter=0
while counter <= 0:
    print(counter)
    counter += 1

# range(start, stop, increment)
print("using three inputs to range()")
for number in range(0,5,1):#exclusive
    print(number)

print("using one input to range()")
for number in range(5):#exclusive
    print(number)

for number in range(0,5+1):#inclusive
    print(number)
