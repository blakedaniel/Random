from random import randrange, randint
import os


class vampireBoard():
    def __init__(self):
        self.opened_casket = '| |'
        self.vampire_casket = '|V|'
        self.prev_casket = '|*|'
        self.casket = None

    def _defaultCaskets(self):
        return ' '.join(f'|{i}|' for i in range(1, 8))

    def _beforeAfterCaskets(self, casket_choice):
        before_choice = range(1, self.casket)
        before_choice = ' '.join(f'|{i}|' for i in before_choice)
        casket_choice = f' {casket_choice} '
        after_choice = range(self.casket + 1, 8)
        after_choice = ' '.join(f'|{i}|' for i in after_choice)
        return before_choice + casket_choice + after_choice

    def _choosenCasketOpened(self, vampire=False):
        if vampire:
            casket_choice = self.vampire_casket
        else:
            casket_choice = self.opened_casket
        return self._beforeAfterCaskets(casket_choice)

    def _updatedCaskets(self):
        return self._beforeAfterCaskets(self.prev_casket)


class VampireSlaying():
    def __init__(self):
        self.board = vampireBoard()
        self.days_left = 4
        self.vampire_slayed = False
        self.vampire_casket = randrange(1, 8)

    def instructions(self):
        print('''
        Welcome to Vampire Slayer!
        You are a hero who has been tasked with slaying a vampire.
        The vampire is hiding in one of seven caskets.
        Each day you will choose a casket to open.
        If you open the casket with the vampire, you win.
        If you open the wrong casket, the vampire gets to hide in a new casket.
        You only have four days to slay the vampire.
        Can you think of a strategy to consistently slay the vampire in four days or less?
        Good luck!
        ''')

    def vampireTurn(self):
        if self.vampire_casket == 1:
            self.vampire_casket += 1
        elif self.vampire_casket == 7:
            self.vampire_casket -= 1
        else:
            move = randint(-1, 1)
            self.vampire_casket += move

    def _displayDefaultBoard(self):
        if self.days_left == 4:
            print(self.board._defaultCaskets())
        else:
            print(self.board._updatedCaskets())

    def heroTurn(self):
        self._displayDefaultBoard()

        self.board.casket = input('Casket Choice: ')
        if self.board.casket == 'quit':
            print('quiting...')
            return self.board.casket

        try:
            self.board.casket = int(self.board.casket)
        except:
            print('Invalid response. Please try again. Type <quit> to end game.')
            self.heroTurn()

        if self.board.casket == self.vampire_casket:
            self.vampire_slayed = True
            print(self.board._choosenCasketOpened())
            print('The vampire has been slayed!')
            return
        else:
            self.board._choosenCasketOpened()
            print('The vampire lives another day')

    def play(self):
        while not self.vampire_slayed and self.days_left != 0:
            print(f'{self.days_left} Day Left')
            player_status = self.heroTurn()
            if player_status == 'quit':
                break
            self.vampireTurn()
            print(self.vampire_casket)
            self.days_left -= 1
            os.system('clear')
        if self.vampire_slayed:
            print('You have slayed the vampire!')
        else:
            print('The vampire has escaped.')
        print('See you another day')


vs = VampireSlaying()
vs.play()
