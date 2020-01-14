import random

def organize_game():
    # one door will have the money, the others will have nothing:
    door_contents=[1,0,0]

    #the random.shuffle() function shuffles the indices of the list
    random.shuffle(door_contents)

    for i in range(0,len(door_contents)):
        if door_contents[i]==1:
            winning_door=i

    #return the list of door contents and the number of the winning door
    return door_contents,winning_door

def game_times():
    #the door numbers go from 0 to 2, they coresponf to the "door contents"
    door_nums=[0,1,2]

    # runs the prevously written function, to organize the game_times
    # which puts
    door_contents,winning_door=organize_game()

    # Simulated a contestant. The contestant will make a choice from 0 to 2,
    # corresponding to the door numbers
    door_chosen=random.choice(door_nums)

    # make a list of the unavailable doors to be opened by the host
    unavailable_doors=[door_chosen, winning_door]

    # using sets to find the door number left over

    door_to_open=set(door_nums)

    # we can use the pop() function to pop it out of the set, and
    # make it
    door_to_open= door_to_open.pop()

    opened_door=door_nums[door_to_open]

    switched_win=False
    stayed_win=False

    unavailable_doors=[door_chosen, door_to_open]
    switched_choice=set(door_nums).difference(unavailable_doors)

    # switched_choice is correctly a set, so we need to use the pop() function
    # to pop the number out of the set.
    #switched_choice should be a set of 1
    switched_choice=switched_choice.pop()

    if door_contents[switched_choice]==1:

        switched_win=True

    if door_contents[switched_choice]==1:

        stayed_win=True

    return int(switch)

def monte_carlo(N):
    switched_win=0
    stayed_win=0
    for game_num in range(0,N):

        switched_win, stayed_win = game_times()

        if switched_win == 1:
            total_switched_wins+= 1

        if stayed_win == 1:
            total_stayed_wins +=1

    print(f"Out of {N} plays")

    print(f"Switched with precentage = {(total_switched_wins/N)*100} %")
    print(f"Switched with precentage = {(total_stayed_wins/N)*100} %")
'''list1=[1,1,1,1,1,1,5,6,7]
print(set(list1))
list2=[1,6,7]
list3=[]'''
game_times()
