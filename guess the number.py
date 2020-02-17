#guess the number


winning_number = 66

print("This is number guessing game")
input_number = int(input("guess the number between 1 to 100 :  "))

guess = 1
game_over = False

while not game_over:
    if (winning_number == input_number):
        print("Winner Winner Panner Dinner")
        print("You done in ", guess, "guess")
        game_over = True
    else:
        if(input_number < winning_number):
            print("Guess any larger number")
            guess +=1
            input_number = int(input("guess again: "))
        else:
            print("Guess any samller number ")
            guess +=1
            input_number = int(input("guess again: "))
