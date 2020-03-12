import argparse
parser = argparse.ArgumentParser(description='PyChess: Python Chess with pretraind AlphaZero')
parser.add_argument('-g', '--gui', default=True, action='store_false', help='Use GUI version of PyChess. Default: True')
parser.add_argument('-i', '--assist', default=False, action='store_true',  help='Enable AI assist for human player. Default: False')
parser.add_argument('-m', '--mode', type=int, default=0, choices=[0,1,2], help='Play mode: 0 - human vs AI, 1 - AI vs AI, 2 - human vs human')
args = parser.parse_args()

print(args)
