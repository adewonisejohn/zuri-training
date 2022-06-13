import random
game_chars = ['R', 'P', 'S']
user = ("")
cpu = ("")
while  True:
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors: ").upper()
    cpu = random.choice(game_chars)
    player_moves = str()
    cpu_moves = str()
    if user == "R":
         player_moves ="ROCK"
    elif user == "P":
        player_moves = "PAPER"   
    else:
         player_moves = "SCISSORS"
    if cpu == "R":
         cpu_moves ="ROCK"
    elif cpu == "P":
        cpu_moves = "PAPER"   
    else:
         cpu_moves = "SCISSORS"
    print("PLAYER is {} : CPU is {}".format(player_moves,cpu_moves))
    if user in game_chars:
        if (user == 'R' and cpu == 'S') or (user == 'S' and cpu == 'P') or (user == 'P' and cpu == 'R'):
            print("User Won")
            break
        elif user == cpu:
            print('Stalemate....Try again')
            continue
        else:
            print("CPU Won") 
            break
    else:
        print("Invalid character")
    continue
    

