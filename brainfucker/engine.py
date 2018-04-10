from __future__ import print_function
from builtins import input
import sys
import os
import time
# rows, columns = os.popen('stty size', 'r').read().split()

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def evaluator(command_string):
    memory = {}
    op_pointer = 0
    mem_pointer = 0
    stack = []
    while op_pointer < len(command_string):
        if mem_pointer < -1:
            raise RuntimeError("Trying to access negative memory block.")
        command = command_string[op_pointer]
        # print(command_string)
        # print(' '*op_pointer + '^')
        print('command:',command,'\nmemory:',memory,'\nmem_pointer:',mem_pointer,'\nop_pointer:',op_pointer,'\nstack:',stack)
        # time.sleep(0.05)
        # input()
        print((CURSOR_UP_ONE + ERASE_LINE)*9)
        if command == '>':
            mem_pointer += 1
        elif command == '<':
            mem_pointer -= 1
        elif command == '+':
            memory[mem_pointer] = memory.setdefault(mem_pointer, 0) + 1
        elif command == '-':
            memory[mem_pointer] = memory.setdefault(mem_pointer, 0) - 1
        elif command == '.':
            print(chr(memory[mem_pointer]),end='')
        elif command == ',':
            memory[mem_pointer] = ord(input()[0])
        elif command == ']' and memory.get(mem_pointer, 0) != 0:
            op_pointer = stack.pop()
            continue
        elif command == ']' and memory.get(mem_pointer, 0) == 0:
            stack.pop()
        elif command == '[' and memory.get(mem_pointer, 0) == 0:
            counter = 0
            pos_skip = 1
            found_matching = False
            while op_pointer + pos_skip < len(command_string):
                # print(command_string)
                # print(' '*(op_pointer+pos_skip) + '^')
                # print('command:',command,'\nmemory:',memory,'\nmem_pointer:',mem_pointer,'\nop_pointer:',op_pointer,'\nstack:',stack,'\npos_skip:',pos_skip,'\ncounter:',counter)
                # input()
                # print((CURSOR_UP_ONE + ERASE_LINE)*11)
                com = command_string[op_pointer+pos_skip]
                if com == ']':
                    if counter == 0:
                        op_pointer += pos_skip+1
                        found_matching = True
                        break
                    else:
                        counter -= 1
                elif com == '[':
                    counter += 1
                pos_skip += 1
            if found_matching:
                continue
        elif command == '[' and memory.get(mem_pointer, 0) != 0:
            stack.append(op_pointer)
        op_pointer += 1

if __name__ == '__main__':
    a = sys.argv[-1]
    for i in set(a):
        if i not in ['+','-',',','.','[',']','<','>']:
            a = a.replace(i,'')
    evaluator(a)
