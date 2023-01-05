from thunno import flags
from thunno import run
import sys


THUNNO_VERSION = "1.2.1"


def execute(code, inputs, flags_list):
    inputs, stack = flags.handle_input_flags(inputs, flags_list)
    stack, vars, _ = run.run(code, inputs, stack)
    flags.handle_output_flags(stack, vars, flags_list)


def from_filename(filename, flags_list):
    sys.stderr.write('Thunno, v' + THUNNO_VERSION + '\n')
    try:
        with open(filename) as f:
            execute(f.read(), sys.stdin.read(), ''.join(flags_list))
    except Exception as E:
        sys.stderr.write('An error occurred -' + repr(E))


def not_from_filename():
    print('Thunno Interpreter (v' + THUNNO_VERSION + ')')
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
    print('\nOutput:')
    execute(code, inputs, flags_list)

def cmdline():
    args = sys.argv[1:]
    if not args:
        not_from_filename()
    else:
        from_filename(args[0], args[1:])
