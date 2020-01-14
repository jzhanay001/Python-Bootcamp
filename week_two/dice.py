'''def dice_roll():
    """
    returns a coin flip- random integer between 0 and 1
    if 1 - the coin lands on head
    if 0 - the coin lands on tail
    """

    return(random.randint(1,6) )#equal chance of being on head or tails'''

def roll_dice():
        """
        returns a coin flip- random integer between 0 and 1
        if 1 - the coin lands on head
        if 0 - the coin lands on tail
        """

        return(random.randint(1,dice_max) )#equal chance of being on head or tails
def monte_carlo(n):
    pass
    """
    performs a monte_carlo simulation of a coin flip
    [Param]\t n (int)- number of samples
    [Return]\t None- prints out the results of the simulation
    """
    one_count=0
    two_count=0
    three_count=0
    four_count=0
    five_count=0
    six_count=0
    exp_count=0


    while exp_count < n:        #for i in range (0,n)
        result = dice_roll()
        if result == 1:
            one_count +=1
        elif result == 2:
            two_count +=1
        elif result == 3:
            three_count +=1
        elif result == 4:
            four_count +=1
        elif result == 5:
            five_count +=1
        elif result == 6:
            six_count +=1
        exp_count+=1
    #msg=f"There were {head_count/n * 100} % heads"
    #print(msg)
    #msg=f"There were {head_count/n *  100} % tails"
    #print(msg)

#monte_carlo(10000)
#help(monte_carlo)
#Another way
def monte_carlo_with_lists(N,dice_max=6):
    results=[]
    for exp in range (0,N):
        results.append(roll_dice(dice_max))

    print(f"{N} experiments were performed")

    for outcome in range(1,dice_max+1):
        count=results.count(outcome) # Ex list=[1,1,1,5] count=list.count(1) is 3
        msg=f"The probability of {outcome}={(count/N*100)} %"
        print(msg)

dice_max=10
print(f"The probability should converge to {1/dice_max * 100} %")
monte_carlo_with_lists(10000,dice_max)
