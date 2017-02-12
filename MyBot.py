import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random
import logging

logging.basicConfig(filename='output.log',level=logging.DEBUG)

myID, game_map = hlt.get_init()
hlt.send_init("MyPythonBot")

def assign_move(square):
    if square.strength == 0:
        return Move(square, STILL)
    else:
        return Move(square, random.choice((NORTH, EAST, SOUTH, WEST)))

while True:
    game_map.get_frame()
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    logging.debug(moves)
    hlt.send_frame(moves)
