import random

rock = "rock"
paper = "paper"
scisors = "scisors"

pc_Score = 0
player_Score = 0
while True:
  #the main loop to play which checks who gets to three scores first.
    pc_choice = random.choices([rock, paper, scisors])
    pc_play = pc_choice[0]
    player_play = input("Player 1, enter your choice: ")

    while player_play != "rock" and player_play != "paper" and player_play != "scisors":
        print("Invalid choice")
        player_play = input("Player 1, enter another choice: ")

    print(pc_play, player_play)

    if pc_play == player_play:
        print(f"You tied this time. PC: {pc_Score} You: {player_Score}!")

    if (player_play == "rock" and pc_play == "scisors") or (player_play == "paper" and pc_play == "rock") or (player_play == "scisors" and pc_play == "paper"):
        print(f"You won the this time. PC: {pc_Score} You: {player_Score+1}!")
        player_Score += 1

    if (pc_play == "rock" and player_play == "scisors") or (pc_play == "paper" and player_play == "rock") or (pc_play == "scisors" and player_play == "paper"):
        print(f"You lost this time. PC: {pc_Score+1} You: {player_Score}!")
        pc_Score += 1

    if player_Score == 3:
        print("YOU WON!")
        break
    
    if pc_Score == 3:
        print("YOU LOST!")
        break
