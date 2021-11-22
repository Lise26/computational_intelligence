from collections import Counter
import numpy as np
import copy


class Game:
    def __init__(self, rows=6, cols=7):
        self._rows = rows
        self._cols = cols
        self._nb = 4
        self._board = None
        self._starter = None
        self._turn = None
        self._won = None
        self.last_move = None
        self.create_game()

    def create_game(self):
        """Creates the game state (board and variables)"""
        self._board = self._board = np.zeros((self._cols, self._rows), dtype=np.byte)
        self._starter = 1
        self._turn = self._starter
        self._won = None

    def valid_moves(self):
        """Returns columns where a disc may be played"""
        return [n for n in range(self._cols) if self._board[n, self._rows - 1] == 0]

    def play(self, column, player):
        """Updates `board` as `player` drops a disc in `column`"""
        (index,) = next((i for i, v in np.ndenumerate(self._board[column]) if v == 0))
        self._board[column, index] = player
        self.last_move = [column, index]

    def take_back(self, column):
        """Updates `board` removing top disc from `column`"""
        (index,) = [i for i, v in np.ndenumerate(self._board[column]) if v != 0][-1]
        self._board[column, index] = 0
        self.last_move = None

    def four_in_a_row(self, player):
        """Checks if `player` has a 4-piece line"""
        return (
            any(
                all(self._board[c, r] == player)
                for c in range(self._cols)
                for r in (list(range(n, n + self._nb)) for n in range(self._rows - self._nb + 1))
            )
            or any(
                all(self._board[c, r] == player)
                for r in range(self._rows)
                for c in (list(range(n, n + self._nb)) for n in range(self._cols - self._nb + 1))
            )
            or any(
                np.all(self._board[diag] == player)
                for diag in (
                    (range(ro, ro + self._nb), range(co, co + self._nb))
                    for ro in range(0, self._cols - self._nb + 1)
                    for co in range(0, self._rows - self._nb + 1)
                )
            )
            or any(
                np.all(self._board[diag] == player)
                for diag in (
                    (range(ro, ro + self._nb), range(co + self._nb - 1, co - 1, -1))
                    for ro in range(0, self._cols - self._nb + 1)
                    for co in range(0, self._rows - self._nb + 1)
                )
            )
        )

    def move(self, move):
        self.play(move, self._turn)
        score = self.eval_board(self._turn)
        if score == 1 or score == -1:
            self._won = score
        self._turn = - self._turn

    def _mc(self, player):
        board = self._board.copy()
        p = -player
        while self.valid_moves():
            p = -p
            c = np.random.choice(self.valid_moves())
            self.play(c, p)
            if self.four_in_a_row(p):
                self._board = board
                return p
        self._board = board
        return 0

    def montecarlo(self, player):
        montecarlo_samples = 100
        cnt = Counter(self._mc(player) for _ in range(montecarlo_samples))
        return (cnt[1] - cnt[-1]) / montecarlo_samples

    def eval_board(self, player):
        if self.four_in_a_row(1):
            return 1
        elif self.four_in_a_row(-1):
            return -1
        else:
            return self.montecarlo(player)

    def copy_state(self):
        return copy.deepcopy(self)

    def get_win(self):
        return self._won

    def get_turn(self):
        return self._turn

    def get_board(self):
        return self._board.copy()
