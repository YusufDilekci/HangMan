from man_shape import logo_hangman, stages
from operations import Words

used_letters = []

hang = Words()
hang.get_word()


print(f"{logo_hangman}\n")

#testing
print(hang.word)


go_on = True
while go_on: 
    hang.show_word_stage()
    
    if "_" not in hang.close_word:
            print("Congralutaions, You find the word!")
            go_on = False
    else:
        char = input("Please enter a letter: ").lower()
        if char not in used_letters: 
            if char in hang.word:
                hang.set_word(char)
            else:
                hang.lose_right()
                hang.show_word_stage()
            if hang.rights == 0:
                print("Sorry, You lose the game")
                go_on = False
        else:
            print("You already got this letter. Try again")

