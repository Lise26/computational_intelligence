"""
    Implementation of the Monte Carlo Tree Search algorithm.

    This algorithm performs series of selection, expansion, random simulation and backpropagation for a given number of
    iterations (the more iterations, the better the result, but the slower the execution).
    A reward system is implemented allowing to decide the best move to make next.
"""

import numpy as np
import math


class MonteCarlo:
    def __init__(self, game):
        self._game = game

    def monte_carlo_tree_search(self, iterations, root, exploration_parameter):
        """ Monte-Carlo Tree Search algorithm """
        for i in range(iterations):
            node, turn = self.selection(root, 1, exploration_parameter)
            reward = self.simulation(node.state, turn)
            self.backpropagation(node, reward, turn)

        ans = self.best_child(root, 0)
        return ans.state.last_move[0]

    def selection(self, node, turn, exploration_parameter):
        """ Expand a node and take the best child until a winning state is reached """
        while not node.state.last_move or not node.state.four_in_a_row(state.get_board()[state.last_move]):
            if not node.fully_explored():
                return self.expansion(node), -turn
            else:
                node = self.best_child(node, exploration_parameter)
                turn *= -1

        return node, turn

    def expansion(self, node):
        """ Add a child state to the node """
        valid_locations = node.state.valid_moves()
        for col in valid_locations:
            if col not in node.children_moves:
                new_state = node.state.copy_state()
                new_state.move(col)
                break

        node.add_child(new_state, col)
        return node.children[-1]

    def simulation(self, state_init, turn):
        """ Simulates random moves until the game is won by someone and returns a reward """
        state = state_init.copy_state()
        while not state.last_move or not state.four_in_a_row(state.get_board()[state.last_move]):
            free_cols = state.valid_moves()
            col = random.choice(free_cols)
            state.move(col)
            turn *= -1

        reward_bool = state.four_in_a_row(state.get_board()[state.last_move])
        if reward_bool and turn == -1:
            reward = 1
        elif reward_bool and turn == 1:
            reward = -1
        else:
            reward = 0
        return reward

    def backpropagation(self, node, reward, turn):
        """ Update the rewards of all the ancestors of a node """
        while node is not None:
            node.visits += 1
            node.reward -= turn*reward
            node = node.parent
            turn *= -1
        return

    def best_child(self, node, exploration_parameter):
        """ Returns the best child of a node based on a scoring system proposed by Auer, Cesa-Bianchi and Fischer """
        best_score = float('-inf')
        best_children = []
        for c in node.children:
            exploitation = c.reward / c.visits
            exploration = math.sqrt(math.log(2.0*node.visits)/float(c.visits))
            score = exploitation + exploration_parameter*exploration
            if score == best_score:
                best_children.append(c)
            if score > best_score:
                best_children = [c]
                best_score = score
        res = np.random.choice(best_children)
        return res
