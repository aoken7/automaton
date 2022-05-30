import argparse
import random
import argparse
from xmlrpc.client import Boolean
import numpy as np
import matplotlib.pyplot as plt


class Automaton():
    def __init__(self, _rule_number: int, x_size: int = 60, y_size: int = 10, is_rand_init=False) -> None:
        self.rule_number = _rule_number
        self.rule = self.gen_rule()
        self.bin_flag = self.to_bin(_rule_number)
        self.board = self.board_init(x_size, y_size, is_rand_init)

    def board_init(self, x_size, y_size, is_rand):
        board = np.zeros((y_size, x_size), dtype=int)

        if is_rand:
            board[0][x_size//2] = 1
        else:
            for i in range(len(board[1])):
                board[0][i] = random.randint(0, 1)

        return board

    def board_plot(self):

        plt.figure(figsize=(20, 15))
        ax = plt.gca()

        ax.axis("off")

        plt.imshow(self.board, cmap=plt.cm.binary)
        plt.title("Automaton Rule : " + str(self.rule_number))
        plt.show()

    def to_bin(self, num: int, pad: int = 8):
        bi_num = bin(num)[2:]
        bi_num_paded = str('0' * (pad - len(bi_num))) + bi_num
        return bi_num_paded

    def gen_rule(self):
        rule = [self.to_bin(i, 3) for i in range(8)]
        rule.reverse()
        return rule

    def paint_check(self, x, y) -> Boolean:
        lstr = list(map(str, (self.board[y-1][x-1:x+2])))
        mass = "".join(lstr)

        for i in range(len(self.rule)):
            if self.rule[i] == mass:
                if self.bin_flag[i] == '1':
                    return True
                else:
                    return False

        return False

    def automaton(self) -> None:

        for y in range(1, len(self.board)):
            for x in range(1, len(self.board[0])-1):
                if self.paint_check(x, y):
                    self.board[y][x] = 1

        self.board_plot()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('rule',help='automaton rule. 0 ~ 255',type=int)
    parser.add_argument('--xsize',type=int, default=200)
    parser.add_argument('--ysize', type=int, default=200)
    parser.add_argument('--isrand', type=int, default=False)
    args = parser.parse_args()

    a = Automaton(args.rule, args.xsize , args.ysize, args.isrand)
    a.automaton()
