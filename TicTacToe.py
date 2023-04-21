# ticTacToe.py
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.placement = 0
        self.placements = set()

    # player chooses, can add AI/computer coding here
    def choose(self):
        print('\n' + 'To quit game, enter QUIT')
        if self.name == 'x':
            while True:
                self.placement = input(self.name + ', pick your placement! ')
                match self.placement:
                    case 'QUIT':
                        break
                    case _ as num if (int(num) >= 1) and (int(num) <= 9):
                        self.placement = int(self.placement)
                        return
                    case _:
                        error_msg = 'Placement must be an available integer 1 - 9. Please try again.'
                        print(error_msg)
        else:
            min_ = min(game.available_placements)
            max_ = max(game.available_placements)
            self.placement = random.randrange(start=min_, stop=max_ + 1)


class Game:
    def __init__(self):
        # defining instances of two players
        self.player_x = Player('x')
        self.player_o = Player('o')
        self.current_player = self.player_x

        # all main placement sets/dictionaries
        # Played, available , and current are empty at start
        self.starting_placements = set(range(1, 10))
        self.played_placements = self.player_x.placements.union(self.player_o.placements)
        self.available_placements = self.starting_placements.difference(self.played_placements)
        self.current_placements = {}

        # for start of game, fill current_placements dictionary with starting
        # placement options
        for placement in self.starting_placements:
            self.current_placements[placement] = placement

        # digits defining the bottom of the tic tac toe board, will be used
        # to define up-down, left-right wins
        self.columns = {1, 2, 3}

        # create up-down and left-to right win cases
        up_down = []
        left_right = []

        for column in self.columns:
            ud = {column, column + 3, column + 6}
            if column == 1:
                for row in ud:
                    lr = {row, row + 1, row + 2}
                    left_right.append(lr)
            up_down.append(ud)

        # defined winning cases
        self.wins = {
            'up_down': up_down,
            'left_right': left_right,
            'tleft_bright': [{3, 5, 7}],
            'bleft_tright': [{1, 5, 9}],
        }

        self.end_game = False

    # switch from one player to another player
    def playerswitch(self):
        match self.current_player:
            case self.player_x:
                self.current_player = self.player_o
            case self.player_o:
                self.current_player = self.player_x

    # display board based on currently played placements
    def displayboard(self):
        v3 = (7, 4, 1)
        for v in v3:
            box_1 = str(self.current_placements[v])
            box_2 = str(self.current_placements[v + 1])
            box_3 = str(self.current_placements[v + 2])
            print(f'[{box_1}] [{box_2}] [{box_3}]')

    # update played and available placements based on most
    # recent player placements
    def updatesets(self):
        self.played_placements = self.player_x.placements.union(self.player_o.placements)
        self.available_placements = self.starting_placements.difference(self.played_placements)

    # request player placement, check that placement is valid
    # if so add to player placements
    def choosevalidateadd(self):
        self.updatesets()
        while True:
            self.current_player.choose()
            if self.current_player.placement == 'QUIT':
                break
            elif self.current_player.placement not in self.current_placements.values():
                print('Placement must be an available integer 1 - 9. Please try again.')
            else:
                self.current_player.placements.add(self.current_player.placement)
                self.current_placements[self.current_player.placement] = self.current_player.name
                self.updatesets()
                return

    def checkendgame(self):
        # check if player wants to quit, then end game if so
        if self.current_player.placement == 'QUIT':
            print('\n' + 'Goodbye and thanks for playing!')
            self.end_game = True
            return

        # checking player's placements against win cases
        for win_cases in self.wins.values():
            for win_case in win_cases:
                if win_case.issubset(self.current_player.placements):
                    self.end_game = True
                    break
        # if winner exists, display winner and winning board
        if (self.end_game == True) and (self.current_player.placement != 'QUIT'):
            self.displayboard()
            print(self.current_player.name + ' wins!')

        # display tie, if tie
        elif len(self.available_placements) == 0:
            self.displayboard()
            self.end_game = True
            print('Tied game. You both win!')


if __name__ == '__main__':
    game = Game()
    while game.end_game == False:
        game.displayboard()
        game.choosevalidateadd()
        game.checkendgame()
        game.playerswitch()
else:
    print('TicTacToe has be executed when imported and may not work properly')
