secret_word = "Soumo"
guess = " "
guess_count = 0
guess_limit = 6
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the guess word : ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Sorry , You Lose the game, Better luck next time!")
else:
    print("You won the game , Congo")