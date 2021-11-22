"""
    Implementation of the nodes of the tree of boards used during Monte-Carlo Tree Search.
"""


class Node:
    def __init__(self, state, parent=None):
        self.visits = 1
        self.reward = 0.0
        self.state = state
        self.children = []
        self.children_moves = []
        self.parent = parent

    def add_child(self, child_state, move):
        """ Add a child to the current node """
        child = Node(child_state, parent=self)
        self.children.append(child)
        self.children_moves.append(move)

    def update(self, reward):
        """ Update the node's reward """
        self.reward += reward
        self.visits += 1

    def fully_explored(self):
        """ Check if the node is fully explored (i.e. we cannot add any other children to this node) """
        if len(self.children) == len(self.state.valid_moves()):
            return True
        return False
