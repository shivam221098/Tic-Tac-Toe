import random
from abc import ABC, abstractmethod


class Player:
    # 3.
    def __init__(self, mark, player_type):
        self.mark = mark
        self.opp_mark = "O" if mark == "X" else "X"
        self.player_type = player_type


