import random
import os
from display_hangman import display_hangman

def get_word():
    file_path = os.path.abspath(__file__)
    cur_dir = os.path.dirname(file_path)
    with open(os.path.join(cur_dir, 'fruits.txt')) as f:
        word = random.choice(f.readlines()).upper()
        return word.strip()

def play(word):
    word_completion = '_ ' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(f'Let\'s play Hangman!' )
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    
    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'You have already tried {guess} letter')
            elif guess not in word:
                print(f'{guess} is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Good job, {guess} is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion.split())
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ' '.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed {guess} word.')
            elif guess != word:
                print(f'{guess} is not the word.')
                tries -= 1
                guessed_words.append(guess)
            else:
                 guessed = True
                 word_completion = word
        else:
            print('Not a valid guess.')
            
        print(display_hangman(tries))
        print(word_completion)
        print(f'{tries} tries remain.')
        print('\n')
    if guessed:
        print('Congrats, you guessed the word. You win')
    else:
        print(f'Sorry, you ran out of tries. The word was {word}. Maybe next time!')
    
        
if __name__ == '__main__':
    word = get_word()
    print(len(word))
    play(word)
    while input('Play Again?(Y/N) ').upper() =='Y':
        word = get_word()
        play(word)
        