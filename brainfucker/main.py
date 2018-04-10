import sys
from engine import evaluator

if __name__ == '__main__':
    filename = sys.argv[-1]
    f = open(filename)
    command_string = f.read()
    f.close()
    for i in set(command_string):
        if i not in ['+', '-', ',', '.', '[', ']', '<', '>']:
            command_string = command_string.replace(i, '')
    evaluator(command_string)
    print()
