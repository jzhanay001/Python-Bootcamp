# the goal of this script is to sum up all the numbers between
# N and M (inclusively), where N and M are both user inputs

N=int(input("Enter an lower limit:"))
M=int(input("Enter an upper limit:"))
print("Using for loop")
sum=0
for number in range(N,M+1): #[N,M)
    sum+=number
print(sum)

print("Using while loop")
sum1=0
while N<=M:
    sum1+=N
    N+=1
print(sum1)
