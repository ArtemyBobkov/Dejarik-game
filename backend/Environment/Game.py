from typing import List

from Environment.Field import Field
from Figures.Fighter import Fighter
from Figures.Figure import Figure
from Figures.Guard import Guard
from Figures.Hunter import Hunter
from Figures.Pet import Pet
from Utils import NUM_SECTORS, parse_state

import pygtrie


class Game:

    def __init__(self):
        figs_1 = Game.create_figures_for_player(1)
        figs_2 = Game.create_figures_for_player(2)
        self.field = Field(figs_1, figs_2)
        self.history = pygtrie.PrefixSet()
        self.step_number = 0
        self.cur_states = pygtrie.PrefixSet()

    @staticmethod
    def create_figures_for_player(player_number: int) -> List[Figure]:
        if player_number == 1:
            return [Hunter(1, (2, 0)), Guard(1, (2, 1)), Fighter(1, (2, 2)), Pet(1, (2, 4))]
        if player_number == 2:
            return [Hunter(2, (2, NUM_SECTORS - 1)), Guard(2, (2, NUM_SECTORS - 2)),
                    Fighter(2, (2, NUM_SECTORS - 3)), Pet(2, (2, NUM_SECTORS - 5))]
        raise ValueError("wrong argument for creating figures")

    def make_step(self):
        new_states = pygtrie.PrefixSet()
        for state in self.cur_states:
            self.field.load_state(parse_state(state))


    def run(self):
        while self.step_number < 5:
            print()
