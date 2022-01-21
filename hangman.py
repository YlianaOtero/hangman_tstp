import random

def hangman():
    list_of_words = ["cat", "dog", "program", "king", "shirt", "movie", "books", "horror", "shining", "seller", "cup", "pushing"]
    max = len(list_of_words) - 1
    randitem = random.randint(0, max)
    word = list_of_words[randitem]
    wrong = 0
    stages = ["",
             "__________          ",
             "|                   ",
             "|          |        ",
             "|          0        ",
             "|         /|\       ",
             "|         / \       ",
             "|                   "
              ]
    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in remaining_letters:
                cind = remaining_letters.index(char)
                board[cind] = char
                remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(stages[0: e])))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
        if not win:
            print("\n".join(stages[0: wrong]))
            print("You lose! It was {}.".format(word))

#(*Modify your Hangman game, so your program randomly selects the word to guess from a list of words.*)
