import math
from typing import *


def handle_input_flags(inputs: str, flags: Union[str, List[str]]) -> (list, list):
    ''' This function takes in the input as a string, and the flags as a string or list of strings,
        and handles the flags, returning the final stack which will be passed to the run function. '''

    stack = []
    
    # W flag (Whole input)
    # Without the W flag, each line of input is taken separately
    # With the W flag, the whole input is taken as a multi-line string
    
    if 'W' in flags:
        inputs = [inputs]
    else:
        inputs = inputs.splitlines()

    # E flag (Don't Evaluate)
    # Without the E flag, the program tries to evaluate each input
    # With the E flag, each input is kept as the original string

    if 'E' not in flags:
        new_input = []
        for inp in inputs:
            try:
                new_input.append(eval(inp))
            except:
                new_input.append(inp)
        inputs = new_input[:]

    # D flag (Duplicate Input)
    # This can be used multiple times
    # For each time it is used, the input list is appended to the stack
    
    stack.extend(inputs * flags.count('D'))

    # Z flag (Push Zero)
    # This can be used multiple times
    # For each time it is used, 0 is prepended to the stack

    stack = [0] * flags.count('Z') + stack

    # O flag (Push One)
    # This can be used multiple times
    # For each time it is used, 1 is prepended to the stack

    stack = [1] * flags.count('O') + stack

    # T flag (Push Ten)
    # This can be used multiple times
    # For each time it is used, 10 is prepended to the stack

    stack = [10] * flags.count('T') + stack
    
    # H flag (Push One Hundred)
    # This can be used multiple times
    # For each time it is used, 100 is prepended to the stack

    stack = [100] * flags.count('H') + stack

    # t flag (Push One Thousand)
    # This can be used multiple times
    # For each time it is used, 1000 is prepended to the stack

    stack = [1000] * flags.count('t') + stack

    # L flag (Length of Input)
    # This can be used multiple times
    # For each time it is used, the length of the input is prepended to the stack

    stack = [len(inputs)] * flags.count('L') + stack

    # B flag (Convert To Byte Array)
    # With the B flag, any strings will be converted to a byte array

    if 'B' in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, str):
                new_input.append([ord(c) for c in inp])
            else:
                new_input.append(inp)
        inputs = new_input[:]

    # + flag (Add One)
    # This can be used multiple times
    # For each time it is used, any numbers will be incremented by one
        
    if '+' in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, (int, float)):
                new_input.append(inp + flags.count('+'))
            else:
                new_input.append(inp)
        inputs = new_input[:]

    # - flag (Subtract One)
    # This can be used multiple times
    # For each time it is used, any numbers will be decremented by one
        
    if '-' in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, (int, float)):
                new_input.append(inp - flags.count('-'))
            else:
                new_input.append(inp)
        inputs = new_input[:]

    # * flag (Multiply)
    # This can be used multiple times
    # For each time it is used, any numbers will be multiplied
        
    if '*' in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, (int, float)):
                new_input.append(inp * (flags.count('*') + 1))
            else:
                new_input.append(inp)
        inputs = new_input[:]

    # * flag (Divide)
    # This can be used multiple times
    # For each time it is used, any numbers will be divided
        
    if '*' in flags:
        new_input = []
        for inp in inputs:
            if isinstance(inp, (int, float)):
                new_input.append(inp / (flags.count('/') + 1))
            else:
                new_input.append(inp)
        inputs = new_input[:]

    return inputs, stack


def handle_output_flags(stack: list, vars: Dict[str, Any], flags: Union[str, List[str]]) -> None:
    ''' This function will take in the stack and variable dictionary which is returned by the run function,
        and apply the flags which are passed into it. This function will print whatever is needed, and return None. '''
    
    if not stack:
        stack = [0]

    # R flag (Remove the Top Item)
    # This can be used multiple times
    # For each time it is used, the top item is removed
    stack = stack[flags.count('R'):]
    

    if not stack:
        stack = [0]

    # X flag (Push X)
    # This can be used multiple times
    # For each time it is used, the variable X is pushed

    stack = [vars['x']] * flags.count('X') + stack

    # Y flag (Push Y)
    # This can be used multiple times
    # For each time it is used, the variable Y is pushed

    stack = [vars['y']] * flags.count('Y') + stack
    
    # K flag (Push the Stack)
    # With this flag, a copy of the whole stack is prepended to the stack

    if 'K' in flags:
        stack = [stack[:]] + stack

    # J flag (Join By Empty Strings)
    # With this flag the top of the stack is joined by ""
    # If the top of the stack is not an iterable, it is converted to a string and pushed

    if 'J' in flags:
        try:
            stack = [''.join(map(str, stack[0]))] + stack
        except:
            stack = [str(stack[0])] + stack

    # j flag (Join By Spaces)
    # With this flag the top of the stack is joined by " "
    # If the top of the stack is not an iterable, it is converted to a string and pushed

    if 'j' in flags:
        try:
            stack = [' '.join(map(str, stack[0]))] + stack
        except:
            stack = [str(stack[0])] + stack

    # N flag (Join By Newlines)
    # With this flag the top of the stack is joined by "\n"
    # If the top of the stack is not an iterable, it is converted to a string and pushed

    if 'N' in flags:
        try:
            stack = ['\n'.join(map(str, stack[0]))] + stack
        except:
            stack = [str(stack[0])] + stack

    # S flag (Sum the Stack)
    # With this flag any numbers in the stack are summed, and the result is pushed

    if 'S' in flags:
        nums = []
        for item in stack:
            if isinstance(item, (int, float)):
                nums.append(item)
        stack = [sum(nums)] + stack

    # P flag (Product of the Stack)
    # With this flag any numbers in the stack are multiplied, and the result is pushed

    if 'P' in flags:
        nums = []
        for item in stack:
            if isinstance(item, (int, float)):
                nums.append(item)
        stack = [math.prod(nums)] + stack

    # d flag (Don't Print)
    # With this flag nothing is printed at the end

    if 'd' not in flags:
        print(stack[0])
