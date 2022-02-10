
import os,json,random

class wordle_game():

    def load(self,path_to_file):
        try:
            with open(path_to_file,'r') as file:
                return json.load(file)
        except:
            print('file missing')
            return []

    def get_words(self):
        wordfile = os.path.join(self.directory,'words.json')

        words = self.load(wordfile)
        words = [w.upper() for w in words] 
        return words

    def get_letters(self):
        letterfile = os.path.join(self.directory,'words.json')
        return self.load(letterfile)

    def print_table(self,guesses,try_results):
        print('-'*30)
        for i in range(6):
            result_print = '| '
            for j in range(5):
                result_print = result_print + guesses[i][j] + try_results[i][j] + ' | '
            print(result_print)
        print('-'*30)


    def guess_word(self):

        guesses = [
            '?????',
            '?????',
            '?????',
            '?????',
            '?????',
            '?????',
        ]

        try_results = [
            ['⬜','⬜','⬜','⬜','⬜'],
            ['⬜','⬜','⬜','⬜','⬜'],
            ['⬜','⬜','⬜','⬜','⬜'],
            ['⬜','⬜','⬜','⬜','⬜'],
            ['⬜','⬜','⬜','⬜','⬜'],
            ['⬜','⬜','⬜','⬜','⬜']
        ]

        for i in range(0,6):
            print('try {}'.format(i+1))
            
            guess = input('enter 5 letter word:\n')
            guess = guess.upper().strip()
            while guess not in self.words:
                print('invalid word, try again')
                guess = input('enter 5 letter word:\n')
                guess = guess.upper().strip()
            
            guesses[i] = guess

            for j in range(5):

                guess_letter = guess[j]
                word_letter = self.word[j]

                try_results[i][j] = '⬛'

                if guess_letter in self.word:
                    try_results[i][j] = '🟨'

                if guess_letter == word_letter:
                    try_results[i][j] = '🟩'
            

            # result_print = ''
            # for j in range(5):
            #     result_print = result_print + guess[j] + try_results[i][j] + ' | '
            # print(result_print)

            self.print_table(guesses,try_results)


            if guess == self.word:
                print('!!! WIN !!!')
                break

        input('hit enter to close program')
            

            


    def __init__(self):

        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.words = self.get_words()
        self.word = random.choice(self.words)
        self.letters = self.get_letters()

        self.guess_word()


if __name__ == "__main__":

    # if 'a' in 'poiagh':
    #     print('has a')

    # quit()

    wordle_game()

        


