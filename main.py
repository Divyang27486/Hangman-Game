import random
import hangman_words
import Hangman_Photos
import Hangman_art

print(Hangman_art.start)
Word = (random.choice(hangman_words.word_list)).lower()
for i in range(len(Word)):
    print("_", end="")
Game_Over = False
Correct_letters = []
Lives = 6
while not Game_Over:
    Final_Word = ""
    Guess_Letter = input("\nGuess a letter:").lower()
    for letter in Word:
        if letter == Guess_Letter:
            Final_Word += Guess_Letter
            Correct_letters.append(Guess_Letter)
        elif letter in Correct_letters:
            Final_Word += letter
            print("You already guess this letter")
        else:
            Final_Word += "_"
    if Guess_Letter not in Word:
        Lives -= 1
        print(f"{Guess_Letter}, It is not in the Word")
    print(Final_Word)
    print(Lives, "/6")
    print(Hangman_Photos.HANGMANPICS[6-Lives])

    if "_" not in Final_Word:
        Game_Over = True
        print("You Won")
    elif Lives == 0:
        Game_Over = True
        print("You lost")
