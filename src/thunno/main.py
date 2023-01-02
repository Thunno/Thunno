from thunno import flags
from thunno import run
import sys


def execute(code, inputs, flags_list):
    inputs, stack = flags.handle_input_flags(inputs, flags_list)
    stack, vars, _ = run.run(code, inputs, stack)
    flags.handle_output_flags(stack, vars, flags_list)


def from_filename(filename, flags_list):
    try:
        with open(filename) as f:
            execute(f.read(), sys.stdin.read(), ''.join(flags_list))
    except:
        sys.stderr.write('[THUNNO]: No such file ' + repr(filename))


def not_from_filename():
    print('Thunno Interpreter')
    print('\nFlags:')
    flags_list = input()
    code = ''
    print('\nHeader:')
    inp = input()
    while inp:
        code += inp + '\n'
        inp = input()
    print('\nCode:')
    inp = input()
    while inp:
        code += inp + '\n'
        inp = input()
    print('\nFooter:')
    inp = input()
    while inp:
        code += inp + '\n'
        inp = input()
    inputs = ''
    print('\nInput:')
    inp = input()
    while inp:
        inputs += inp + '\n'
        inp = input()
    execute(code, inputs, flags_list)

def cmdline():
    args = sys.argv[1:]
    if not args:
        not_from_filename()
    else:
        from_filename(args[0], args[1:])
