"""
Using the card dictionary from earlier in this chapter, create a simple card game that deals
two players three cards each. The player with the highest card wins. If there is a tie, then
compare the second highest card and, if necessary, the third highest. If all three cards have
the same value, then the game is a draw
"""
deck = [{'value':i, 'suit':c} for c in ['spades', 'clubs', 'hearts', 'diamonds'] for i in range(2,15)]
from random import 