"""
    Implementation of the MinMax algorithm with varying depth using alpha-beta pruning.

    The goal of the MiniMax algorithm is to indicate to a player which move to make in order to maximize its chances of
    winning the whole game, assuming that its adversary will try to do the same. According to the description of this
    algorithm, at each turn of a player and starting from the current board game, the code will simulate alternatively
    the possible moves of the player along with the ones of its adversary with the goal of maximizing the chances of
    winning of the first while minimizing the ones of the latter. At each depth of the simulation, the algorithm will
    simulate up to 7 boards, each having a piece dropped in one of the free columns. Through the MonteCarlo Evaluation
    provided each board will be attributed a score. After creating all the boards of the tree, at each depth, a board
    will be selected based on its reward and on the type of node (min or max) starting from the bottom of the tree
    (minimise or maximise the rewards depending on the depth which can be odd or even corresponding to the player or
    its adversary). The final choice is made among the 7 accessible boards from the current one with the score updated
    through the reward procedure described above.

    To get the adversary to play as an optimal player, each of the two players will be in turn considered as the
    maximizing player, hence trying to maximise the reward when a max nodes is encountered.
"""


class Minimax:
    def __init__(self, game):
        self._game = game

    def minimax(self, depth, alpha, beta, maximizingPlayer):
        valid_locations = self._game.valid_moves()
        val = self._game.eval_board(self._game.get_turn())

        if depth == 0 or self._game.get_win() or not valid_locations:
            return None, val

        elif maximizingPlayer:
            val = float("-inf")
            for l in valid_locations:
                self._game.play(l, self._game.get_turn())
                new_score = self.minimax(depth - 1, alpha, beta, False)[1]
                self._game.take_back(l)
                if new_score > val:
                    val = new_score
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
            return l, val

        else:
            val = float("inf")
            for l in valid_locations:
                self._game.play(l, -self._game.get_turn())
                new_score = self.minimax(depth - 1, alpha, beta, True)[1]
                self._game.take_back(l)
                if new_score < val:
                    val = new_score
                beta = min(beta, val)
                if alpha >= beta:
                    break
            return l, val
