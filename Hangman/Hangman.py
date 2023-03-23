from random import choices

f_open = open("Hangman_words.txt", "r")
words_list = [line.strip() for line in f_open.readlines()]
f_open.close()
print(words_list)

rand_choice = choices(words_list)
choice = rand_choice[0]

place_holder = ["_" for char in choice]

print("HangMan:\nYou Should fill the blank spaces below!")
for _ in place_holder:
    print(_, end=" ")
print()

fault = 0
succeed_round = 0
while True:
    guessed_letter = input("Guess a letter: ")
    
    if fault == len(choice) / 2 :
        print("YOU LOST!")
        print(f"The word was: {choice}")
        break
    
    if guessed_letter in choice:
        indexes = [index for index in range(len(choice)) 
                   if choice.startswith(guessed_letter, index)]
        for index in indexes:
            place_holder[index] = guessed_letter
        print("Nice Job!")
        for index in place_holder:
            print(index, end= " ")
        print()
        succeed_round += 1
    
    elif guessed_letter not in choice:
        print("Nope! It's not there.\n")
        for index in place_holder:
            print(index, end= " ")
        print()
        fault += 1
    
    if place_holder == list(choice):
        print("YOU WON!\nThe word is:", end=" ")
        print(f"\t{choice.capitalize()}")
        print(f"You guessed it in {succeed_round + fault} Trys.")
        break
    
    print("\n\n")
    print(f"Next round:")
