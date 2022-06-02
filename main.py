#Rock beats Scissors
#Paper beats Rock
#Scissors beats Paper

import random


def cpu():
    
    return random.choice(['R','P','S'])

    
def moves(pick, user):
    
    if pick == 'R':

       return user , ' (Rock)'

    elif pick == 'P':

        return user , ' (Paper)'

    elif pick == 'S':

        return user , ' (Scissors)'
 


print("Play Rock-Paper-Scissors")
print("Enter R for Rock")
print("Enter P for Paper")
print("Enter S for Scissorrs") 



#set player to False
player = False

while player == False:
    # take input from the user
    choice = input("Enter choice(R, P or S): ").upper()

    # check if choice is one of the 3 options
    if choice in ('R', 'P', 'S'):

        # cpu's random pick
        cpu_pick=cpu()
        player_moves= moves(choice, "Player")
        cpu_moves= moves(cpu_pick, "CPU")

        print(player_moves ," : ",  cpu_moves)   

        
        # compare picks
        if choice == cpu_pick:
            
            print("Oops, there's a tie")

        elif choice == 'R':

            if cpu_pick == "P":
               print("Compter wins: Paper covers Rock")
            else:
               print("You win! Rock smashes scissorrs")

            player = True

    
        elif choice == 'P':

            if cpu_pick == "S":
               print("Compter wins: scissorrs cuts paper")
            else:
               print("You win! Paper covers Rock")

            player = True


        elif choice == 'S':
            if cpu_pick == "R":
               print("Compter wins:Rock smashes scissorrs")
            else:
               print("You win! scissorrs cuts paper")

            player = True

    
    else:

        print("Invalid Input. Input should be R, P or S")
        

    