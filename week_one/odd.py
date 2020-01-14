N=int(input("Enter an upper limit:"))
print("Using for loop")
for number in range(1,N+1):
    if number%2!=0:
        print(number)

counter=1

print("Using While loop")
while counter<=N:
    if counter%2!=0:
        print(counter)
    counter+=1
