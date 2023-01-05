# VERSION 1.2.0
# Jan 5th 2023

'''
MIT License

Copyright (c) 2023 Rujul Nayak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import re
import math
import string as st
import statistics
import random
import itertools

from thunno.helpers import *

def run(code, input_list, stack=(), vars=None):
    if vars is None:
        vars = {'x': 0, 'y': 1}
    stack = Stack(list(stack) + list(input_list))
    index = 0
    while index < len(code):
        char = code[index]
        a, b, c = (stack + [0, 0, 0])[:3]
        if char in '0123456789.':
            string = char
            index += 1
            try:
                while code[index] in '0123456789.':
                    string += code[index]
                    index += 1
            except:
                pass
            index -= 1
            try:
                while string[0] == '0':
                    stack.push(0)
                    try:
                        string = string[1:]
                    except:
                        break
                if string == '.':
                    index += 1
                    next = code[index]
                    if next in 'aAzZ':
                        index += 1
                        next += code[index]
                    stack.rmv(a)
                    if isinstance(a, int):
                        x = range(a)
                    elif isinstance(a, list):
                        x = a.copy()
                    else:
                        x = str(a)
                    lst = []
                    for i in x:
                        stack, vars, br = run(next, input_list, [i] + stack, vars)
                        if br:
                            break
                        lst.append(stack[0])
                        stack.pop(0)
                    stack.push(lst)
                else:
                    stack.push(eval(string))
            except:
                pass
        elif char == '"':
            string = char
            index += 1
            try:
                while code[index] != '"':
                    string += code[index]
                    index += 1
                string += code[index]
            except:
                string += '"'
            stack.push(eval(string))
        elif char == "'":
            index += 1
            stack.push(code[index])
        elif char == 'b':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(bin(int(i))[2:])
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(bin(int(a))[2:])
                except:
                    stack.push(None)
        elif char == 'c':
            stack.rmv(a, b)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(b.count(i))
                    except:
                        l.append(str(b).count(str(i)))
                stack.push(l)
            else:
                try:
                    stack.push(b.count(a))
                except:
                    stack.push(str(b).count(str(a)))
        elif char == 'd':
            stack.rmv(a)
            if isinstance(a, list):
                lst = []
                for i in a:
                    if isinstance(i, int):
                        lst.append([int(d) if d in '0123456789' else d for d in str(i)])
                    else:
                        lst.append(list(str(i)))
                stack.push(lst) 
            else:
                if isinstance(a, int):
                    stack.push([int(d) if d in '0123456789' else d for d in str(a)])
                else:
                    stack.push(list(str(a)))
        elif char == 'e':
            stack.rmv(a)
            string = ''
            index += 1
            try:
                while code[index] != 'E' or az_track(code, index):
                    string += code[index]
                    index += 1
            except:
                pass
            l = []
            if isinstance(a, int):
                x = range(a)
            elif isinstance(a, list):
                x = a.copy()
            else:
                x = str(a)
            for i in x:
                stack, vars, br = run(string, input_list, [i] + stack, vars)
                if br:
                    break
                l.append(stack[0])
                stack.pop(0)
            stack.push(l)
        elif char == 'f':
            stack.rmv(a)
            f = lambda n: [x for x in range(1, n+1) if n%x==0]
            if isinstance(a, list):
                stack.push([f(i) for i in a])
            else:
                stack.push(f(a))
        elif char == 'g':
            stack.rmv(a)
            string = ''
            index += 1
            try:
                while code[index] != 'k' or az_track(code, index):
                    string += code[index]
                    index += 1
            except:
                pass
            l = []
            if isinstance(a, int):
                x = range(a)
            elif isinstance(a, list):
                x = a.copy()
            else:
                x = str(a)
            for i in x:
                stack, vars, br = run(string, input_list, [i] + stack, vars)
                if br:
                    break
                if stack[0]:
                    l.append(i)
                stack.pop(0)
            stack.push(l)
        elif char == 'h':
            stack.rmv(a)
            if isinstance(a, list):
                lst = []
                for i in a:
                    try:
                        lst.append(hex(int(i))[2:])
                    except:
                        lst.append(None)
                stack.push(lst)
            else:
                try:
                    stack.push(hex(int(a))[2:])
                except:
                    stack.push(None)
        elif char == 'i':
            stack.rmv(a)
            if isinstance(a, list):
                lst = []
                for i in a:
                    try:
                        lst.append(int(i))
                    except:
                        lst.append(None)
                stack.push(lst)
            else:
                try:
                    stack.push(int(i))
                except:
                    stack.push(None)
        elif char == 'j':
            stack.rmv(a, b)
            try:
                stack.push(str(b).join(map(str, a)))
            except:
                stack.push(str(a))
        elif char == 'k':
            pass # This command doesn't do anything
        elif char == 'l':
            stack.push([])
        elif char == 'm':
            if not isinstance(a, list):
                A = stack.copy()
            else:
                stack.rmv(a)
                A = a.copy()
            l = []
            for i in A:
                if isinstance(i, (int, float)):
                    l.append(i)
                else:
                    try:
                        l.append(float(i))
                    except:
                        pass
            try:
                stack.push(min(l))
            except:
                stack.push(None)
        elif char == 'n':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(-i)
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(-a)
                except:
                    stack.push(None)
        elif char == 'o':
            stack.rmv(a)
            if isinstance(a, list):
                lst = []
                for i in a:
                    try:
                        lst.append(1/float(i))
                    except:
                        lst.append(None)
                stack.push(lst)
            else:
                try:
                    stack.push(1/float(a))
                except:
                    stack.push(None)
        elif char == 'p':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j >= i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b >= i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i >= a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b >= a)
                    except:
                        stack.push(None)
        elif char == 'q':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j <= i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b <= i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i <= a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b <= a)
                    except:
                        stack.push(None)
        elif char == 'r':
            stack.rmv(a)
            if isinstance(a, list):
                stack.push(list(reversed(a)))
            elif isinstance(a, int):
                stack.push(int(str(a)[::-1]))
            else:
                stack.push(str(a)[::-1])
        elif char == 's':
            stack.rmv(a, b)
            stack.push(a)
            stack.push(b)
        elif char == 't':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(math.sqrt(float(i)))
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(math.sqrt(float(a)))
                except:
                    stack.push(None)
        elif char == 'u':
            stack.rmv(a)
            if isinstance(a, list):
                stack.push([str(i).upper() for i in a])
            else:
                stack.push(str(a).upper())
        elif char == 'v':
            if isinstance(a, list):
                stack.rmv(a)
                stack.push([i for i in a if i is not None])
            else:
                while None in stack:
                    stack.rmv(None)
        elif char == 'w':
            if isinstance(a, list):
                stack.rmv(a)
                stack.push([i for i in a if i])
            else:
                stack.push(a)
        elif char == 'x':
            stack.push(vars.get('x', 0))
        elif char == 'y':
            stack.push(vars.get('y', 1))
        elif char == 'B':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(int(str(i), 2))
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(int(str(a), 2))
                except:
                    stack.push(None)
        elif char == 'C':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(chr(int(i)))
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(chr(int(a)))
                except:
                    stack.push(None)
        elif char == 'D':
            stack.push(a)
        elif char == 'E':
            pass # This command doesn't do anything
        elif char == 'F':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(math.factorial(int(i)))
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(math.factorial(int(a)))
                except:
                    stack.push(None)
        elif char == 'G':
            stack.rmv(a, b)
            if isinstance(a, list):
                stack.push([[i for i in b if i != j] for j in a])
            else:
                stack.push([i for i in b if i != a])
        elif char == 'H':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(int(str(i), 16))
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(int(str(a), 16))
                except:
                    stack.push(None)
        elif char == 'I':
            stack.push(input_list)
        elif char == 'J':
            stack.rmv(a)
            if isinstance(a, list):
                stack.push(''.join(map(str, a)))
            else:
                stack.push(str(a))
        elif char == 'K':
            stack.rmv(a)
        elif char == 'L':
            stack.rmv(a)
            try:
                stack.push(len(a))
            except:
                stack.push(len(str(a)))
        elif char == 'M':
            if not isinstance(a, list):
                A = stack.copy()
            else:
                stack.rmv(a)
                A = a.copy()
            l = []
            for i in A:
                if isinstance(i, (int, float)):
                    l.append(i)
                else:
                    try:
                        l.append(float(i))
                    except:
                        pass
            try:
                stack.push(max(l))
            except:
                stack.push(None)
        elif char == 'N':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(all(i % j != 0 for j in range(2, i)) and i >= 2)
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(all(a % j != 0 for j in range(2, a)) and a >= 2)
                except Exception as E:
                    stack.push(None)
        elif char == 'O':
            stack.rmv(a)
            if isinstance(a, list):
                stack.push([[ord(c) for c in str(i)] for i in a])
            else:
                stack.push([ord(c) for c in str(a)])
        elif char == 'P':
            if isinstance(a, list):
                stack.rmv(a)
                try:
                    stack.push(math.prod(a))
                except:
                    stack.push(None)
            else:
                try:
                    stack.push(math.prod(stack.copy()))
                except:
                    stack.push(None)
        elif char == 'Q':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j != i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b != i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i != a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b != a)
                    except:
                        stack.push(None)
        elif char == 'R':
            stack.rmv(a)
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(list(range(int(i))))
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(list(range(int(a))))
                except:
                    stack.push(None)
        elif char == 'S':
            if isinstance(a, list):
                stack.rmv(a)
                try:
                    if not a:
                        stack.push(0)
                    else:
                        stack.push(sum(a[1:], a[0]))
                except:
                    stack.push(None)
            else:
                try:
                    if not stack:
                        stack.push(0)
                    else:
                        stack.push(sum(stack.copy()[1:], stack.copy()[0]))
                except:
                    stack.push(None)
        elif char == 'T':
            stack.rmv(a, b)
            if isinstance(b, list):
                stack.rmv(b)
                stack.push(b + [a])
            else:
                stack.push([a])
        elif char == 'U':
            stack.rmv(a)
            if isinstance(a, list):
                stack.push([str(i).lower() for i in a])
            else:
                stack.push(str(a).lower())
        elif char == 'V':
            stack.rmv(a)
            d = {'a': a, 'b': b, 'c': c, 's': stack, 'x': vars.get('x', 0), 'y': vars.get('y', 1)}
            if isinstance(a, list):
                l = []
                for i in a:
                    try:
                        l.append(eval(str(i), d))
                    except:
                        l.append(None)
                stack.push(l)
            else:
                try:
                    stack.push(eval(str(a), d))
                except:
                    stack.push(None)
        elif char == 'X':
            stack.rmv(a)
            vars['x'] = a
        elif char == 'Y':
            stack.rmv(a)
            vars['y'] = a
        elif char == '+':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j + i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b + i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i + a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b + a)
                    except:
                        stack.push(None)
        elif char == '-':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j - i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b - i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i - a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b - a)
                    except:
                        stack.push(None)
        elif char == '*':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j * i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b * i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i * a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b * a)
                    except:
                        stack.push(None)
        elif char == '/':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j / i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b / i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i / a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b / a)
                    except:
                        stack.push(None)
        elif char == '_':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(i - j)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(i - b)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(a - i)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(a - b)
                    except:
                        stack.push(None)
        elif char == '\\':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(i / j)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(i / b)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(a / i)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(a / b)
                    except:
                        stack.push(None)
        elif char == ',':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j // i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b // i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i // a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b // a)
                    except:
                        stack.push(None)
        elif char == '|':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(i // j)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(i // b)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(a // i)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(a // b)
                    except:
                        stack.push(None)
        elif char == '^':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j ** i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b ** i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i ** a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b ** a)
                    except:
                        stack.push(None)
        elif char == '@':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(i ** j)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(i ** b)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(a ** i)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(a ** b)
                    except:
                        stack.push(None)
        elif char == '%':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j % i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b % i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i % a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b % a)
                    except:
                        stack.push(None)
        elif char == '$':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(i % j)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(i % b)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(a % i)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(a % b)
                    except:
                        stack.push(None)
        elif char == ':':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(list(range(int(j), int(i))))
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(list(range(int(b), int(i))))
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(list(range(int(i), int(a))))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(list(range(int(b), int(a))))
                    except:
                        stack.push(None)
        elif char == ';':
            stack.rmv(a, b, c)
            try:
                stack.push(list(range(int(c), int(b), int(a))))
            except:
                stack.push(None)
        elif char == '=':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j == i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b == i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i == a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b == a)
                    except:
                        stack.push(None)
        elif char == '>':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j > i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b > i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i > a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b > a)
                    except:
                        stack.push(None)
        elif char == '<':
            stack.rmv(a, b)
            if isinstance(a, list):
                if isinstance(b, list):
                    lst = []
                    for j in b:
                        lst.append([])
                        for i in a:
                            try:
                                lst[-1].append(j < i)
                            except:
                                lst[-1].append(None)
                    stack.push(lst)
                else:
                    lst = []
                    for i in a:
                        try:
                            lst.append(b < i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            else:
                if isinstance(b, list):
                    lst = []
                    for i in b:
                        try:
                            lst.append(i < a)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b < a)
                    except:
                        stack.push(None)
        elif char == '&':
            stack.rmv(a, b)
            stack.push(b and a)
        elif char == '~':
            stack.rmv(a, b)
            stack.push(b or a)
        elif char == '`':
            stack.rmv(a, b)
            stack.push(bool(b) ^ bool(a))
        elif char == '!':
            stack.rmv(a)
            stack.push(not a)
        elif char == '#':
            while code[index] != '\n':
                index += 1
        elif char == '{':
            stack.rmv(a)
            string = ''
            index += 1
            try:
                while code[index] != '}' or az_track(code, index):
                    string += code[index]
                    index += 1
            except:
                pass
            if isinstance(a, int):
                x = range(a)
            elif isinstance(a, list):
                x = a.copy()
            else:
                x = str(a)
            for i in x:
                stack, vars, br = run(string, input_list, [i] + stack, vars)
                if br:
                    break
        elif char == '}':
            pass # This command doesn't do anything
        elif char == '[':
            string = ''
            index += 1
            try:
                while code[index] != ']' or az_track(code, index):
                    string += code[index]
                    index += 1
            except:
                pass
            while True:
                stack, vars, br = run(string, input_list, stack, vars)
                if br:
                    break
        elif char == ']':
            pass # This command doesn't do anything
        elif char == ')':
            return removeNone(stack), vars, True
        elif char == '?':
            stack.rmv(a)
            truthy = ''
            falsy = ''
            index += 1
            try:
                while code[index] != ')' or az_track(code, index):
                    truthy += code[index]
                    index += 1
                index += 1
                while code[index] != ')' or az_track(code, index):
                    falsy += code[index]
                    index += 1
            except:
                pass
            if a:
                stack, vars, _ = run(truthy, input_list, stack, vars)
            else:
                stack, vars, _ = run(falsy, input_list, stack, vars)
        elif char == '(':
            pass # This command doesn't do anything
        elif char == 'A':
            index += 1
            next = code[index]
            if next == 'A':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(a)
                else:
                    try:
                        stack.push(sum(a) / len(a))
                    except:
                        stack.push(None)
            elif next == 'B':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(numberToBase(j, i))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(numberToBase(b, i))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(numberToBase(i, a))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(numberToBase(b, a))
                        except:
                            stack.push(None)
            elif next == 'C':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.cos(math.radians(float(i))))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.cos(math.radians(float(a))))
                    except:
                        stack.push(None)
            elif next == 'D':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(abs(j - i))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(abs(b - i))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(abs(i - a))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(abs(b - a))
                        except:
                            stack.push(None)
            elif next == 'E':
                stack.rmv(a)
                if not isinstance(a, (list, str)):
                    stack.push([0, a])
                else:
                    stack.push(list(map(list, enumerate(a))))
            elif next == 'F':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(primeFactors(int(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(primeFactors(int(a)))
                    except:
                        stack.push(None)
            elif next == 'G':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(math.gcd(int(i), int(j)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(math.gcd(int(i), int(b)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(math.gcd(int(a), int(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(math.gcd(int(a), int(b)))
                        except:
                            stack.push(None)
            elif next == 'H':
                stack.rmv(a, b)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(b[(i-1) % len(b)])
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b[(a-1) % len(b)])
                    except:
                        stack.push(None)
            elif next == 'I':
                stack.rmv(a, b)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(b[i % len(b)])
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b[a % len(b)])
                    except:
                        stack.push(None)
            elif next == 'J':
                stack.rmv(a)
                try:
                    stack.push(a[0])
                except:
                    stack.push(None)
            elif next == 'K':
                stack.rmv(a)
                try:
                    stack.push(a[-1])
                except:
                    stack.push(None)
            elif next == 'L':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(math.lcm(int(i), int(j)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(math.lcm(int(i), int(b)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(math.lcm(int(a), int(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(math.lcm(int(a), int(b)))
                        except:
                            stack.push(None)
            elif next == 'M':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(max([i, j]))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(max([i, b]))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(max([a, i]))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(max([a, b]))
                        except:
                            stack.push(None)
            elif next == 'N':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(nextPrime(int(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(nextPrime(int(a)))
                    except:
                        stack.push(None)
            elif next == 'O':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(math.hypot(float(i), float(j)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(math.hypot(float(i), float(b)))
                                
                            except:
                                lst.append(None)
                                
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(math.hypot(float(a), float(i)))
                                
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(math.hypot(float(a), float(b)))
                        except:
                            stack.push(None)
            elif next == 'P':
                stack.rmv(a, b)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            x, y = divmod(len(b), int(i))
                            k = 0
                            r = []
                            while k < len(b):
                                r.append(b[k:k+x+(y>0)])
                                k += x+(y>0)
                                if y > 0:
                                    y -= 1
                            lst.append(r)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        x, y = divmod(len(b), int(a))
                        k = 0
                        r = []
                        while k < len(b):
                            r.append(b[k:k+x+(y>0)])
                            k += x+(y>0)
                            if y > 0:
                                y -= 1
                        stack.push(r)
                    except:
                        stack.push(None)
            elif next == 'Q':
                for i in input_list:
                    try:
                        print(i, '-->', run(code[index+1:], [i], stack, vars)[0][0])
                    except:
                        print(i, '-->')
                index = len(code)
            elif next == 'R':
                stack.rmv(a, b, c)
                if isinstance(c, list):
                    stack.push([str(i).replace(str(b), str(a)) for i in c])
                else:
                    stack.push(str(c).replace(str(b), str(a)))
            elif next == 'S':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.sin(math.radians(float(i))))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.sin(math.radians(float(a))))
                    except:
                        stack.push(None)
            elif next == 'T':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.tan(math.radians(float(i))))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.tan(math.radians(float(a))))
                    except:
                        stack.push(None)
            elif next == 'U':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.radians(float(i)))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.radians(float(a)))
                    except:
                        stack.push(None)
            elif next == 'V':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.degrees(float(i)))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.degrees(float(a)))
                    except:
                        stack.push(None)
            elif next == 'W':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.log(float(i), 10))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.log(float(a), 10))
                    except:
                        stack.push(None)
            elif next == 'X':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.exp(float(i)))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.exp(float(a)))
                    except:
                        stack.push(None)
            elif next == 'Y':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(math.log(float(j), float(i)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(math.log(float(b), float(i)))
                                
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(math.log(float(i), float(a)))
                                
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(math.log(float(b), float(a)))
                        except:
                            stack.push(None)
            elif next == 'Z':
                stack.push(st.ascii_uppercase)
            elif next == 'a':
                stack.rmv(a)
                try:
                    stack.push(statistics.median(a))
                except:
                    stack.push(None)
            elif next == 'b':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(int(str(j), i))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(int(str(b), i))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(int(str(i), a))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(int(str(b), a))
                        except:
                            stack.push(None)
            elif next == 'c':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.degrees(math.acos(float(i))))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.degrees(math.acos(float(a))))
                    except:
                        stack.push(None)
            elif next == 'd':
                stack.rmv(a, b)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(fromListOfDigits(b, i))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(fromListOfDigits(b, a))
                    except:
                        stack.push(None)
            elif next == 'e':
                stack.push(math.e)
            elif next == 'f':
                stack.rmv(a, b)
                try:
                    stack.push(re.findall(str(a), str(b)))
                except:
                    stack.push([])
            elif next == 'g':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(None)
                else:
                    l = []
                    for i in a:
                        try:
                            l.append(int(i))
                        except:
                            pass
                    stack.push(gcd(l))
            elif next == 'h':
                stack.rmv(a, b)
                try:
                    stack.push(a.index(b))
                except:
                    stack.push(-1)
            elif next == 'i':
                try:
                    x = int(a)
                except:
                    x = 1
                stack.rmv(a)
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == 'j' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                except:
                    pass
                index += 1
                i = 1
                l = []
                while True:
                    stack, vars, br = run(string, input_list, [i] + stack, vars)
                    if br:
                        break
                    if stack[0]:
                        x -= 1
                        l.append(i)
                    if x == 0:
                        break
                    stack.pop(0)
                    i += 1
                stack.push(l)
            elif next == 'j':
                pass # This command doesn't do anything
            elif next == 'k':
                try:
                    x = int(a)
                except:
                    x = 1
                stack.rmv(a)
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == 'm' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                except:
                    pass
                index += 1
                i = 1
                while True:
                    stack, vars, br = run(string, input_list, [i] + stack, vars)
                    if br:
                        break
                    if stack[0]:
                        x -= 1
                    if x == 0:
                        stack.push(i)
                        break
                    stack.pop(0)
                    i += 1
            elif next == 'l':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(None)
                else:
                    l = []
                    for i in a:
                        try:
                            l.append(int(i))
                        except:
                            pass
                    stack.push(lcm(l))
            elif next == 'm':
                pass # This command doesn't do anything
            elif next == 'n':
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == 'o' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                except:
                    pass
                index += 1
                i = 1
                while True:
                    stack, vars, br = run(string, input_list, [i] + stack, vars)
                    if br:
                        break
                    if stack[0]:
                        stack.push(i)
                        break
                    stack.pop(0)
                    i += 1
            elif next == 'o':
                pass # This command doesn't do anything
            elif next == 'p':
                stack.rmv(a, b)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append([b[x:x+int(i)] for x in range(0, len(b), int(i))])
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push([b[x:x+int(a)] for x in range(0, len(b), int(a))])
                    except:
                        stack.push(None)
            elif next == 'q':
                stack.rmv(a, b)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(i in b)
                        except:
                            lst.append(str(a) in str(b))
                    stack.push(lst)
                else:
                    try:
                        stack.push(a in b)
                    except:
                        stack.push(str(a) in str(b))
            elif next == 'r':
                stack.rmv(a, b, c)
                if isinstance(c, list):
                    stack.push([re.sub(str(b), str(a), str(i)) for i in c])
                else:
                    stack.push(re.sub(str(b), str(a), str(c)))
            elif next == 's':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.degrees(math.asin(float(i))))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.degrees(math.asin(float(a))))
                    except:
                        stack.push(None)
            elif next == 't':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(math.degrees(math.atan(float(i))))
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(math.degrees(math.atan(float(a))))
                    except:
                        stack.push(None)
            elif next == 'u':
                stack.rmv(a)
                try:
                    for i in a:
                        stack.push(i)
                except:
                    stack.push(a)
            elif next == 'v':
                stack.rmv(a)
                try:
                    stack, vars, br = run(str(a), input_list, [], vars)
                except:
                    pass
            elif next == 'w':
                stack.push(math.pi)
            elif next == 'x':
                vars['x'] = a
            elif next == 'y':
                vars['y'] = a
            elif next == 'z':
                stack.push(st.ascii_lowercase)
            elif next in '+-*/@<>|&^%':
                stack.rmv(a, b)
                try:
                    stack.push(eval(repr(b) + ' ' + next + ' ' + repr(a)))
                except:
                    stack.push(None)
            elif next == '~':
                stack.rmv(a)
                try:
                    stack.push(~a)
                except:
                    stack.push(None)
            elif next == '=':
                stack.rmv(a, b)
                stack.push(b == a)
            elif next == '!':
                stack.rmv(a, b)
                stack.push(b != a)
            elif next == '?':
                stack.rmv(a)
                truthy = ''
                falsy = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == ':' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        truthy += code[index]
                        index += 1
                    index += 2
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == ';' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        falsy += code[index]
                        index += 1
                    index += 1
                except:
                    pass
                if a:
                    stack, vars, _ = run(truthy, input_list, stack, vars)
                else:
                    stack, vars, _ = run(falsy, input_list, stack, vars)
            elif next == ':':
                pass # This command doesn't do anything
            elif next == ';':
                pass # This command doesn't do anything
            elif next == '[':
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == ']' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                    index += 1
                except:
                    pass
                while True:
                    stack, vars, br = run(string, input_list, stack, vars)
                    if br:
                        break
            elif next == '$':
                try:
                    stack.push(input_list[0])
                except:
                    pass
            elif next == '`':
                try:
                    stack.push(input_list[-1])
                except:
                    pass
            elif next == '#':
                stack.push(len(input_list))
            elif next == ',':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(input_list[int(a) % len(input_list)])
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(input_list[int(a) % len(input_list)])
                    except:
                        stack.push(None)
            elif next == '.':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(input_list[-int(a) % len(input_list)])
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(input_list[-int(a) % len(input_list)])
                    except:
                        stack.push(None)
            elif next == '{':
                stack.rmv(a)
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == '}' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                    index += 1
                except:
                    pass
                if isinstance(a, int):
                    x = range(a)
                elif isinstance(a, list):
                    x = a.copy()
                else:
                    x = str(a)
                for i, j in enumerate(x):
                    stack, vars, br = run(string, input_list, [j, i] + stack, vars)
                    if br:
                        break
            elif next == '}':
                pass # This command doesn't do anything
            elif next == '(':
                stack.rmv(a, b)
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'A':
                            try:
                                if code[index + 1] == ')' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                    index += 1
                except:
                    pass
                for i, j in zip(a, b):
                    stack, vars, br = run(string, input_list, [[i, j]] + stack, vars)
                    if br:
                        break
            elif next in ('"', "'"):
                d = {'a': a, 'b': b, 'c': c, 's': stack, 'x': vars.get('x', 0), 'y': vars.get('y', 1)}
                string = next
                index += 1
                try:
                    while code[index] != next:
                        string += code[index]
                        index += 1
                    string += code[index]
                except:
                    string += next
                stack.push(eval(string).format(**d))
            elif next == '_':
                stack.push(' ')
            elif next == '\\':
                stack.push('\n')
            elif next == '1':
                stack.push(16)
            elif next == '2':
                stack.push(32)
            elif next == '3':
                stack.push(64)
            elif next == '4':
                stack.push(128)
            elif next == '5':
                stack.push(256)
            elif next == '6':
                stack.push(512)
            elif next == '7':
                stack.push(1024)
            elif next == '8':
                stack.push(2048)
            elif next == '9':
                stack.push(4096)
            elif next == '0':
                stack.push(8192)
        elif char == 'a':
            index += 1
            next = code[index]
            d = {
                'A': 10, 'B': 15, 'C': 20, 'D': 25, 'E': 30, 'F': 35, 'G': 40, 'H': 45,
                'I': 50, 'J': 55, 'K': 60, 'L': 65, 'M': 70, 'N': 75, 'O': 80, 'P': 85,
                'Q': 90, 'R': 95, 'S': 100, 'T': 105, 'U': 110, 'V': 115, 'W': 120, 'X': 125,
                'Y': 130, 'Z': 135, 'a': 140, 'b': 145, 'c': 150, 'd': 155, 'e': 160, 'f': 165,
                'g': 170, 'h': 175, 'i': 180, 'j': 185, 'k': 190, 'l': 195,'m': 200, 'n': 205,
                'o': 210, 'p': 215, 'q': 220, 'r': 225,'s': 230, 't': 235, 'u': 240, 'v': 245,
                'w': 250, 'x': 255, 'y': 260, 'z': 265, '0': 270, '1': 275, '2': 280, '3': 285,
                '4': 290, '5': 295, '6': 300, '7': 305, '8': 310, '9': 315, '\n': 320, ' ': 325,
                '!': 330, '"': 335, '#': 340, '$': 345, '%': 350, '&': 355, "'": 360, '(': 365,
                ')': 370, '*': 375, '+': 380, ',': 385, '-': 390, '.': 395, '/': 400, ':': 455,
                ';': 460, '<': 465, '=': 470, '>': 475, '?': 480, '@': 485, '[': 620, '\\': 625,
                ']': 630, '^': 635, '_': 640, '`': 645, '{': 780, '|': 785, '}': 790, '~': 795
            }
            if next in d.keys():
                stack.push(d[next])
            else:
                stack.push(next)
        elif char == 'Z':
            index += 1
            next = code[index]
            if next == 'A':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(abs(i))
                        except:
                            try:
                                lst.append(abs(int(i)))
                            except:
                                try:
                                    lst.append(abs(float(i)))
                                except:
                                    lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(abs(a))
                    except:
                        try:
                            stack.push(abs(int(a)))
                        except:
                            try:
                                stack.push(abs(float(a)))
                            except:
                                stack.push(None)
            elif next == 'B':
                stack.rmv(a)
                stack.push(bool(a))
            elif next == 'C':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(nCr(j, i))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(nCr(b, i))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(nCr(i, a))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(nCr(b, a))
                        except:
                            stack.push(None)
            elif next == 'D':
                stack.rmv(a)
                try:
                    stack.push(fromListOfDigits(list(map(int, a)), 10))
                except:
                    try:
                        stack.push(int(a))
                    except:
                        stack.push(None)
            elif next == 'E':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(str(j).endswith(str(i)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(str(b).endswith(str(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(str(i).endswith(str(a)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(str(b).endswith(str(a)))
                        except:
                            stack.push(None)
            elif next == 'F':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(primeFactorisation(int(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(primeFactorisation(int(a)))
                    except:
                        stack.push(None)
            elif next == 'G':
                stack.rmv(a, b)
                if isinstance(a, list):
                    l = len(a)
                else:
                    try:
                        l = int(a)
                    except:
                        l = len(str(a))
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if not x:
                    stack.push(x)
                else:
                    if len(x) >= l:
                        stack.push(x[:l])
                    else:
                        i = 0
                        while len(x) < l:
                            if isinstance(x, list):
                                x.append(x[i])
                            else:
                                x += x[i]
                            i += 1
                        stack.push(x)
            elif next == 'H':
                stack.rmv(a)
                try:
                    stack.push(a[:-1])
                except:
                    stack.push(str(a)[:-1])
            elif next == 'I':
                stack.rmv(a)
                try:
                    stack.push(a*2)
                except:
                    stack.push(str(a)*2)
            elif next == 'J':
                stack.rmv(a)
                try:
                    stack.push(a*3)
                except:
                    stack.push(str(a)*3)
            elif next == 'K':
                stack.rmv(a)
                print(a)
            elif next == 'L':
                stack.rmv(a)
                print(a, end='')
            elif next == 'M':
                stack.push(list(stack).copy())
            elif next == 'N':
                stack.rmv(a, b)
                if isinstance(b, list):
                    stack.rmv(b)
                    stack.push([a] + b)
                else:
                    stack.push([a])
            elif next == 'O':
                stack.rmv(a)
                stack.push([a])
            elif next == 'P':
                stack.rmv(a, b)
                stack.push([b, a])
            elif next == 'Q':
                raise TerminateProgramError
            elif next == 'R':
                stack.rmv(a, b)
                if isinstance(a, list):
                    l = len(a)
                else:
                    try:
                        l = int(a)
                    except:
                        l = len(str(a))
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if not x:
                    stack.push(x)
                else:
                    while l > 0:
                        if isinstance(x, list):
                            x.append(x.pop(0))
                        else:
                            x += x[0]
                            x = x[1:]
                        l -= 1
                    stack.push(x)
            elif next == 'S':
                stack.rmv(a, b)
                if isinstance(a, list):
                    l = len(a)
                else:
                    try:
                        l = int(a)
                    except:
                        l = len(str(a))
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if not x:
                    stack.push(x)
                else:
                    while l > 0:
                        if isinstance(x, list):
                            x.insert(0, x.pop(-1))
                        else:
                            x = x[-1] + x
                            x = x[:-1]
                        l -= 1
                    stack.push(x)
            elif next == 'T':
                stack.rmv(a)
                try:
                    stack.push(a[1:])
                except:
                    stack.push(str(a)[1:])
            elif next == 'U':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push([a])
                else:
                    lst = []
                    for i in a:
                        if i not in lst:
                            lst.append(i)
                    stack.push(lst)
            elif next == 'V':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(str(j).startswith(str(i)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(str(b).startswith(str(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(str(i).startswith(str(a)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(str(b).startswith(str(a)))
                        except:
                            stack.push(None)
            elif next == 'W':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append([])
                        for c in str(i):
                            if c in st.ascii_lowercase:
                                lst[-1].append(0)
                            elif c in st.ascii_uppercase:
                                lst[-1].append(1)
                            else:
                                lst[-1].append(-1)
                    stack.push(lst)
                else:
                    lst = []
                    for c in str(a):
                        if c in st.ascii_lowercase:
                            lst.append(0)
                        elif c in st.ascii_uppercase:
                            lst.append(1)
                        else:
                            lst.append(-1)
                    stack.push(lst)
            elif next == 'X':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append('')
                        for c in str(i):
                            if c in st.ascii_lowercase:
                                lst[-1] += chr(ord(c) - 32)
                            elif c in st.ascii_uppercase:
                                lst[-1] += chr(ord(c) + 32)
                            else:
                                lst[-1] += c
                    stack.push(lst)
                else:
                    s = ''
                    for c in str(a):
                        if c in st.ascii_lowercase:
                            s += chr(ord(c) - 32)
                        elif c in st.ascii_uppercase:
                            s += chr(ord(c) + 32)
                        else:
                            s += c
                    stack.push(s)
            elif next == 'Y':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append('')
                        for c in str(i):
                            if ord('A') <= ord(c.upper()) <= ord('M'):
                                lst[-1] += chr(ord(c) + 13)
                            elif ord('N') <= ord(c.upper()) <= ord('Z'):
                                lst[-1] += chr(ord(c) - 13)
                            else:
                                lst[-1] += c
                    stack.push(lst)
                else:
                    s = ''
                    for c in str(a):
                        if ord('A') <= ord(c.upper()) <= ord('M'):
                            s += chr(ord(c) + 13)
                        elif ord('N') <= ord(c.upper()) <= ord('Z'):
                            s += chr(ord(c) - 13)
                        else:
                            s += c
                    stack.push(s)
            elif next == 'Z':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = str(b)
                else:
                    y = b.copy()
                stack.push(list(map(list, zip(x, y))))
            elif next == 'a':
                stack.rmv(a)
                if isinstance(a, list):
                    stack.push(all(a))
                else:
                    stack.push(bool(a))
            elif next == 'b':
                stack.rmv(a)
                if isinstance(a, list):
                    stack.push(any(a))
                else:
                    stack.push(bool(a))
            elif next == 'c':
                stack.rmv(a)
                try:
                    stack.push(float(a)/2)
                except:
                    stack.push(a)
            elif next == 'd':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(i**2)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(a**2)
                    except:
                        stack.push(None)
            elif next == 'e':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(i**3)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(a**3)
                    except:
                        stack.push(None)
            elif next == 'f':
                stack.rmv(a)
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'Z':
                            try:
                                if code[index + 1] == 'g' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                    index += 1
                except:
                    pass
                try:
                    x = int(a)
                except:
                    try:
                        x = len(a)
                    except:
                        x = len(str(a))
                for i in range(x):
                    stack, vars, br = run(string, input_list, stack, vars)
                    if br:
                        break
            elif next == 'g':
                pass # This command doesn't do anything
            elif next == 'h':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(primeFactorExponents(int(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(primeFactorExponents(int(a)))
                    except:
                        stack.push(None)
            elif next == 'i':
                stack.rmv(a, b)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        l.append(str(b).split(str(i)))
                    stack.push(l)
                else:
                    stack.push(str(b).split(str(a)))
            elif next == 'j':
                stack.rmv(a, b)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        l.append(list(str(b).partition(str(i))))
                    stack.push(l)
                else:
                    stack.push(list(str(b).partition(str(a))))
            elif next == 'k':
                stack.rmv(a, b)
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append([])
                        try:
                            y = int(i)
                        except:
                            try:
                                y = len(i)
                            except:
                                y = len(str(i))
                        for j in range(y):
                            lst[-1].append(x[j%len(x)::y])
                    stack.push(lst)
                else:
                    lst = []
                    try:
                        y = int(a)
                    except:
                        try:
                            y = len(a)
                        except:
                            y = len(str(a))
                    for j in range(y):
                        lst.append(x[j%len(x)::y])
                    stack.push(lst)
            elif next == 'l':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                stack.push([x[0::2], x[1::2]])
            elif next == 'm':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(math.ceil(float(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(math.ceil(float(a)))
                    except:
                        stack.push(None)
            elif next == 'n':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(math.floor(float(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(math.floor(float(a)))
                    except:
                        stack.push(None)
            elif next == 'o':
                stack.rmv(a)
                if (not isinstance(a, (list, str))) or (not a):
                    stack.push(a)
                else:
                    stack.push(max({i: a.count(i) for i in a}.items(), key=lambda x: x[1])[0])
            elif next == 'p':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(nPr(j, i))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(nPr(b, i))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(nPr(i, a))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(nPr(b, a))
                        except:
                            stack.push(None)
            elif next == 'q':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                stack.push(x == x[::-1])
            elif next == 'r':
                stack.rmv(a)
                if (not isinstance(a, list)) or (not a):
                    stack.push(a)
                else:
                    try:
                        stack.push(max(a) - min(a))
                    except:
                        stack.push([max(a), min(a)])
            elif next == 's':
                stack.rmv(a, b, c)
                stack.push(b)
                stack.push(c)
                stack.push(a)
            elif next == 't':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(list(str(a)))
                else:
                    x = []
                    for i in a:
                        if not isinstance(i, list):
                            x.append(str(i))
                        else:
                            x.append(i.copy())
                    lst = []
                    for j in range(max(map(len, x))):
                        lst.append([])
                        for k in x:
                            try:
                                lst[-1].append(k[j % len(k)])
                            except:
                                lst[-1].append(k)
                    stack.push(lst)
            elif next == 'u':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(round(float(j), int(i)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(round(float(b), int(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(round(float(i), int(a)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(round(float(b), int(a)))
                        except:
                            stack.push(None)
            elif next == 'v':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(round(float(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(round(float(a)))
                    except:
                        stack.push(None)
            elif next == 'w':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                if not x:
                    stack.push(x)
                else:
                    stack.push(random.choice(x))
            elif next == 'x':
                stack.rmv(a, b)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(b[int(i)%len(b):])
                        except:
                            try:
                                lst.append(str(b)[int(i)%len(str(b)):])
                            except:
                                lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b[int(a)%len(b):])
                    except:
                        try:
                            stack.push(str(b)[int(a)%len(str(b)):])
                        except:
                            stack.push(None)
            elif next == 'y':
                stack.rmv(a, b)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(b[:-(int(i)%len(b))])
                        except:
                            try:
                                lst.append(str(b)[:-(int(i)%len(str(b)))])
                            except:
                                lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(b[:-(int(a)%len(b))])
                    except:
                        try:
                            stack.push(str(b)[:-(int(a)%len(str(b)))])
                        except:
                            stack.push(None)
            elif next == 'z':
                stack.rmv(a, b, c)
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if not isinstance(c, list):
                    y = str(c)
                else:
                    y = c.copy()
                stack.push(list(map(list, itertools.zip_longest(x, y, fillvalue=a))))
            elif next == '!':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = str(b)
                else:
                    y = b.copy()
                stack.push(list(map(list, itertools.product(x, y))))
            elif next == '"':
                index += 2
                stack.push(code[index-1:index+1])
            elif next == '\'':
                index += 3
                stack.push(code[index-2:index+1])
            elif next == '#':
                index += 1
            elif next == '$':
                stack.push(list(sorted(input_list)))
            elif next == '%':
                stack.push(list(reversed(input_list)))
            elif next == '&':
                stack.push(list(map(str, input_list)))
            elif next == '(':
                stack.push(list(map(float, input_list)))
            elif next == ')':
                stack.push(list(map(int, input_list)))
            elif next == '*':
                try:
                    stack.push(math.prod(input_list))
                except:
                    stack.push(input_list)
            elif next == '+':
                try:
                    stack.push(sum(input_list[1:], input_list[0]))
                except:
                    stack.push(input_list)
            elif next == ',':
                try:
                    stack.push(input_list[0] + 1)
                except:
                    try:
                        stack.push(input_list[0])
                    except:
                        stack.push(input_list)
            elif next == '-':
                try:
                    stack.push(input_list[0] - 1)
                except:
                    try:
                        stack.push(input_list[0])
                    except:
                        stack.push(input_list)
            elif next == '.':
                try:
                    stack.push(input_list[0] * 2)
                except:
                    try:
                        stack.push(input_list[0])
                    except:
                        stack.push(input_list)
            elif next == '/':
                try:
                    stack.push(input_list[0] / 2)
                except:
                    try:
                        stack.push(input_list[0])
                    except:
                        stack.push(input_list)
            elif next == ':':
                try:
                    stack.push(max(input_list))
                except:
                    stack.push(input_list)
            elif next == ';':
                try:
                    stack.push(min(input_list))
                except:
                    stack.push(input_list)
            elif next == '<':
                try:
                    stack.push(input_list[-1] - 1)
                except:
                    try:
                        stack.push(input_list[-1])
                    except:
                        stack.push(input_list)
            elif next == '=':
                if not input_list:
                    stack.push(True)
                else:
                    stack.push(all(i == input_list[0] for i in input_list[1:]))
            elif next == '>':
                try:
                    stack.push(input_list[-1] + 1)
                except:
                    try:
                        stack.push(input_list[-1])
                    except:
                        stack.push(input_list)
            elif next == '?':
                try:
                    stack.push(bool(input_list[0]))
                except:
                    stack.push(False)
            elif next == '@':
                try:
                    stack.push(bool(input_list[-1]))
                except:
                    stack.push(False)
            elif next == '[':
                stack.push(input_list[:2])
            elif next == '\\':
                stack.push(list(filter(bool, input_list)))
            elif next == ']':
                stack.push(input_list[-2:])
            elif next == '^':
                try:
                    stack.push(list(filter(lambda x: x != input_list[0], input_list)))
                except:
                    stack.push(input_list)
            elif next == '_':
                try:
                    stack.push(list(filter(lambda x: x!= input_list[-1], input_list)))
                except:
                    stack.push(input_list)
            elif next == '`':
                lst = []
                for i in input_list:
                    if i not in lst:
                        lst.append(i)
                stack.push(lst)
            elif next == '{':
                stack.push(input_list[:3])
            elif next == '|':
                stack.push(list(filter(lambda x: not x, input_list)))
            elif next == '}':
                stack.push(input_list[-3:])
            elif next == '~':
                stack.push([not x for x in input_list])
            elif next == '1':
                stack.push(10 ** 1)
            elif next == '2':
                stack.push(10 ** 2)
            elif next == '3':
                stack.push(10 ** 3)
            elif next == '4':
                stack.push(10 ** 4)
            elif next == '5':
                stack.push(10 ** 5)
            elif next == '6':
                stack.push(10 ** 6)
            elif next == '7':
                stack.push(10 ** 7)
            elif next == '8':
                stack.push(10 ** 8)
            elif next == '9':
                stack.push(10 ** 9)
            elif next == '0':
                stack.push(10 ** 10)
        elif char == 'z':
            index += 1
            next = code[index]
            if next == 'A':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(-abs(i))
                        except:
                            try:
                                lst.append(-abs(int(i)))
                            except:
                                try:
                                    lst.append(-abs(float(i)))
                                except:
                                    lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(-abs(a))
                    except:
                        try:
                            stack.push(-abs(int(a)))
                        except:
                            try:
                                stack.push(-abs(float(a)))
                            except:
                                stack.push(None)
            elif next == 'B':
                stack.rmv(a)
                if isinstance(a, list):
                    l = []
                    for i in a:
                        try:
                            l.append(oct(int(i))[2:])
                        except:
                            l.append(None)
                    stack.push(l)
                else:
                    try:
                        stack.push(oct(int(a))[2:])
                    except:
                        stack.push(None)
            elif next == 'C':
                stack.push(''.join(chr(i) for i in range(32, 127)))
            elif next == 'D':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(list(divmod(j, i)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(list(divmod(b, i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(list(divmod(i, a)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(list(divmod(b, a)))
                        except:
                            stack.push(None)
            elif next == 'E':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(list(divmod(i, j)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(list(divmod(i, b)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(list(divmod(a, i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(list(divmod(a, b)))
                        except:
                            stack.push(None)
            elif next == 'F':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            x = int(i)
                        except:
                            try:
                                x = len(i)
                            except:
                                x = len(str(i))
                        j = 1
                        k = 2
                        l = []
                        while j < x:
                            l.append(j)
                            j *= k
                            k += 1
                        lst.append(l)
                    stack.push(lst)
                else:
                    try:
                        x = int(a)
                    except:
                        try:
                            x = len(a)
                        except:
                            x = len(str(a))
                    j = 1
                    k = 2
                    l = []
                    while j < x:
                        l.append(j)
                        j *= k
                        k += 1
                    stack.push(l)
            elif next == 'G':
                stack.rmv(a)
                string = ''
                index += 1
                try:
                    while 1:
                        if code[index] == 'z':
                            try:
                                if code[index + 1] == 'H' or az_track(code, index + 1):
                                    break
                            except:
                                pass
                        string += code[index]
                        index += 1
                except:
                    pass
                index += 1
                if not isinstance(a, list):
                    x = list(str(a))
                else:
                    x = a.copy()
                lst = [[]]
                last_result = None
                if isinstance(a, int):
                    x = range(a)
                elif isinstance(a, list):
                    x = a.copy()
                else:
                    x = str(a)
                for i in x:
                    stack, vars, _ = run(string, input_list, [i] + stack, vars)
                    if stack[0] == last_result:
                        lst[-1].append(i)
                    else:
                        lst.append([i])
                    last_result = stack[0]
                    stack.pop(0)
                if lst[0] == []:
                    lst = lst[1:]
                stack.push(lst)
            elif next == 'H':
                pass # This command doesn't do anything
            elif next == 'I':
                stack.rmv(a, b)
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                stack.push([i for i, j in enumerate(b) if j == a])
            elif next == 'J':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                stack.push('\n'.join(map(str, x)))
            elif next == 'K':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(str(j).zfill(int(i)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(str(b).zfill(int(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(str(i).zfill(int(a)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(str(b).zfill(int(a)))
                        except:
                            stack.push(None)
            elif next == 'L':
                stack.rmv(a, b, c)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(str(c).ljust(-int(i), str(j)) if int(i) < 0 else str(c).rjust(int(i), str(j)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(str(c).ljust(-int(i), str(b)) if int(i) < 0 else str(c).rjust(int(i), str(b)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(str(c).ljust(-int(a), str(i)) if int(a) < 0 else str(c).rjust(int(a), str(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(str(c).ljust(-int(a), str(b)) if int(a) < 0 else str(c).rjust(int(a), str(b)))
                        except:
                            stack.push(None)
            elif next == 'M':
                l = []
                for i in stack.copy():
                    try:
                        l.append(i)
                    except:
                        try:
                            l.append(float(i))
                        except:
                            l.append(None)
                try:
                    stack.push(max(stack.copy()))
                except:
                    try:
                        stack.push(max(l))
                    except:
                        stack.push(None)
            elif next == 'N':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append(str(i).isnumeric())
                    stack.push(lst)
                else:
                    stack.push(str(a).isnumeric())
            elif next == 'O':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append(str(i).isalpha())
                    stack.push(lst)
                else:
                    stack.push(str(a).isalpha())
            elif next == 'P':
                stack.rmv(a, b)
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(list(map(list, itertools.permutations(b, int(i)))))
                        except:
                            lst.append(list(map(list, itertools.permutations(b))))
                    stack.push(lst)
                else:
                    try:
                        stack.push(list(map(list, itertools.permutations(b, int(a)))))
                    except:
                        stack.push(list(map(list, itertools.permutations(b))))
            elif next == 'Q':
                stack.rmv(a, b)
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(list(map(list, itertools.combinations(b, int(i)))))
                        except:
                            try:
                                lst.append(list(b))
                            except:
                                lst.append(list(str(b)))
                    stack.push(lst)
                else:
                    try:
                        stack.push(list(map(list, itertools.combinations(b, int(a)))))
                    except:
                        try:
                            stack.push(list(b))
                        except:
                            stack.push(list(str(b)))
            elif next == 'R':
                stack.rmv(a, b)
                if not isinstance(b, list):
                    x = str(b)
                else:
                    x = b.copy()
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(list(map(list, itertools.combinations_with_replacement(b, int(i)))))
                        except:
                            try:
                                lst.append(list(b))
                            except:
                                lst.append(list(str(b)))
                    stack.push(lst)
                else:
                    try:
                        stack.push(list(map(list, itertools.combinations_with_replacement(b, int(a)))))
                    except:
                        try:
                            stack.push(list(b))
                        except:
                            stack.push(list(str(b)))
            elif next == 'S':
                stack.rmv(a)
                try:
                    stack.push(list(map(list, itertools.product(*a))))
                except:
                    stack.push(None)
            elif next == 'T':
                stack.rmv(a)
                if isinstance(a, int):
                    stack.push(0)
                elif isinstance(a, float):
                    stack.push(1)
                elif isinstance(a, str):
                    stack.push(2)
                elif isinstance(a, list):
                    stack.push(3)
                else:
                    stack.push(-1)
            elif next == 'U':
                stack.rmv(a)
                if isinstance(a, list):
                    stack.push([str(i).capitalize() for i in a])
                else:
                    stack.push(str(a).capitalize())
            elif next == 'V':
                stack.rmv(a)
                if isinstance(a, list):
                    stack.push([str(i).title() for i in a])
                else:
                    stack.push(str(a).title())
            elif next == 'X':
                stack.push(vars['x'] * 2)
            elif next == 'Y':
                stack.push(vars['y'] * 2)
            elif next == 'Z':
                stack.rmv(a)
                try:
                    stack.push(list(map(list, zip(*a))))
                except:
                    stack.push(a)
            elif next == 'a':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            if float(i) > 0:
                                lst.append(1)
                            elif float(i) < 0:
                                lst.append(-1)
                            else:
                                lst.append(0)
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        if float(a) > 0:
                            stack.push(1)
                        elif float(a) < 0:
                            stack.push(-1)
                        else:
                            stack.push(0)
                    except:
                        stack.push(None)
            elif next == 'b':
                stack.rmv(a)
                if not isinstance(a, (list, str)):
                    stack.push(None)
                if not a:
                    stack.push(a)
                else:
                    last = a[0]
                    for i in a[1:]:
                        try:
                            condition = i <= last
                        except:
                            try:
                                condition = float(i) <= float(last)
                            except:
                                condition = str(i) <= str(last)
                        if condition:
                            stack.push(False)
                            break
                        last = i
                    else:
                        stack.push(True)
            elif next == 'c':
                stack.rmv(a)
                if not isinstance(a, (list, str)):
                    stack.push(None)
                if not a:
                    stack.push(a)
                else:
                    last = a[0]
                    for i in a[1:]:
                        try:
                            condition = i <= last
                        except:
                            try:
                                condition = float(i) >= float(last)
                            except:
                                condition = str(i) >= str(last)
                        if condition:
                            stack.push(False)
                            break
                        last = i
                    else:
                        stack.push(True)
            elif next == 'd':
                stack.push(code)
            elif next == 'e':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                if not x:
                    stack.push(x)
                else:
                    stack.push(all(i == x[0] for i in x))
            elif next == 'f':
                stack.rmv(a)
                if isinstance(a, int):
                    stack = Stack(stack[a % len(stack):] + stack[:a % len(stack)])
            elif next == 'g':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append(str(j).rfind(str(i)))
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append(str(b).rfind(str(i)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append(str(i).rfind(str(a)))
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push(str(b).rfind(str(a)))
                        except:
                            stack.push(None)
            elif next == 'h':
                stack.rmv(a, b)
                if not isinstance(b, list):
                    x = list(str(b))
                else:
                    x = b.copy()
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(max(loc for loc, val in enumerate(x) if val == i))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(max(loc for loc, val in enumerate(x) if val == a))
                    except:
                        stack.push(None)
            elif next == 'i':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(math.isqrt(float(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(math.isqrt(float(a)))
                    except:
                        stack.push(None)
            elif next == 'j':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                stack.push(x + y)
            elif next == 'k':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                stack.push(a + a[::-1])
            elif next == 'l':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append([ord(x) - ord(y) for x, y in zip(str(j), str(i))])
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append([ord(x) - ord(y) for x, y in zip(str(b), str(i))])
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append([ord(x) - ord(y) for x, y in zip(str(i), str(a))])
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push([ord(x) - ord(y) for x, y in zip(str(b), str(a))])
                        except:
                            stack.push(None)
            elif next == 'm':
                stack.rmv(a, b)
                if isinstance(a, list):
                    if isinstance(b, list):
                        lst = []
                        for j in b:
                            lst.append([])
                            for i in a:
                                try:
                                    lst[-1].append([ord(x) + ord(y) for x, y in zip(str(j), str(i))])
                                except:
                                    lst[-1].append(None)
                        stack.push(lst)
                    else:
                        lst = []
                        for i in a:
                            try:
                                lst.append([ord(x) + ord(y) for x, y in zip(str(b), str(i))])
                            except:
                                lst.append(None)
                        stack.push(lst)
                else:
                    if isinstance(b, list):
                        lst = []
                        for i in b:
                            try:
                                lst.append([ord(x) + ord(y) for x, y in zip(str(i), str(a))])
                            except:
                                lst.append(None)
                        stack.push(lst)
                    else:
                        try:
                            stack.push([ord(x) + ord(y) for x, y in zip(str(b), str(a))])
                        except:
                            stack.push(None)
            elif next == 'n':
                if not isinstance(a, list):
                    A = stack.copy()
                else:
                    stack.rmv(a)
                    A = a.copy()
                l = []
                for i in A:
                    if isinstance(i, (int, float)):
                        l.append(i)
                    else:
                        try:
                            l.append(float(i))
                        except:
                            pass
                try:
                    stack.push([max(l), min(l)])
                except:
                    stack.push(None)
            elif next == 'o':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append(str(i).isdigit())
                    stack.push(lst)
                else:
                    stack.push(str(a).isdigit())
            elif next == 'p':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        lst.append(str(i).isprintable())
                    stack.push(lst)
                else:
                    stack.push(str(a).isprintable())
            elif next == 'q':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = list(str(a))
                else:
                    x = a.copy()
                if not x:
                    stack.push(x)
                else:
                    stack.push(list(set(x)) == x)
            elif next == 'r':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                stack.push(list(range(len(x))))
            elif next == 's':
                stack.rmv(a, b, c)
                stack.push(a)
                stack.push(b)
                stack.push(c)
            elif next == 't':
                stack.push(a)
                stack.push(a)
            elif next == 'u':
                stack.push(a)
                stack.push(a)
                stack.push(a)
            elif next == 'v':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(toRomanNumerals(int(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(toRomanNumerals(int(a)))
                    except:
                        stack.push(None)
            elif next == 'x':
                stack.rmv(a)
                if isinstance(a, list):
                    lst = []
                    for i in a:
                        try:
                            lst.append(fromRomanNumerals(str(i)))
                        except:
                            lst.append(None)
                    stack.push(lst)
                else:
                    try:
                        stack.push(fromRomanNumerals(str(a)))
                    except:
                        stack.push(None)
            elif next == 'y':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = list(str(a))
                else:
                    x = a.copy()
                lst = [[]]
                last_result = None
                for i in a:
                    if i == last_result:
                        lst[-1].append(i)
                    else:
                        lst.append([i])
                    last_result = i
                if lst[0] == []:
                    lst = lst[1:]
                stack.push(lst)
            elif next == 'z':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = list(str(a))
                else:
                    x = a.copy()
                stack.push(list(map(list, zip(a, a))))
            elif next == '!':
                stack.push(1)
                try:
                    stack.push(input_list[0])
                except:
                    pass
            elif next == '"':
                index += 4
                stack.push(code[index-3:index+1])
            elif next == '\'':
                index += 5
                stack.push(code[index-4:index+1])
            elif next == '#':
                index += 2
            elif next == '$':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(i % j)
                    except:
                        lst.append(None)
            elif next == '%':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j % i)
                    except:
                        lst.append(None)
                stack.push(lst)
            elif next == '&':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j and i)
                    except:
                        lst.append(None)
                stack.push(lst)
            elif next == '(':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                if not x:
                    stack.push(a)
                else:
                    lst = [x[0]]
                    for i in x[1:]:
                        try:
                            lst.append(lst[-1] + i)
                        except:
                            lst.append(lst[-1])
                    stack.push(lst)
            elif next == ')':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = str(a)
                else:
                    x = a.copy()
                if not x:
                    stack.push(a)
                else:
                    lst = [x[0]]
                    for i in x[1:]:
                        try:
                            lst.append(lst[-1] * i)
                        except:
                            lst.append(lst[-1])
                    stack.push(lst)
            elif next == '*':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j * i)
                    except:
                        lst.append(None)
                stack.push(lst)
            elif next == '+':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j + i)
                    except:
                        lst.append(None)
                stack.push(lst)
            elif next == ',':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j // i)
                    except:
                        lst.append(None)
            elif next == '-':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j - i)
                    except:
                        lst.append(None)
            elif next == '.':
                index += 1
                next = code[index]
                if next in 'aAzZ':
                    index += 1
                    next += code[index]
                stack.rmv(a, b)
                lst = []
                for i, j in zip(a, b):
                    stack, vars, br = run(next, input_list, [i, j] + stack, vars)
                    if br:
                        break
                    lst.append(stack[0])
                    stack.pop(0)
                stack.push(lst)
            elif next == '/':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j / i)
                    except:
                        lst.append(None)
            elif next == ':':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = list(str(a))
                else:
                    x = a.copy()
                stack.push(list(sorted(x)))
            elif next == ';':
                stack.rmv(a)
                if not isinstance(a, list):
                    x = list(str(a))
                else:
                    x = a.copy()
                stack.push(list(sorted(x))[::-1])
            elif next == '<':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j < i)
                    except:
                        lst.append(None)
            elif next == '=':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j == i)
                    except:
                        lst.append(None)
            elif next == '>':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j > i)
                    except:
                        lst.append(None)
            elif next == '?':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(bool(a))
                else:
                    stack.push([bool(i) for i in a])
            elif next == '@':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(i ** j)
                    except:
                        lst.append(None)
            elif next == '[':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(a)
                else:
                    lst = []
                    for i, j in zip(a, a[1:]):
                        try:
                            lst.append(j - i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            elif next == '\\':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(i / j)
                    except:
                        lst.append(None)
            elif next == ']':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(a)
                else:
                    lst = []
                    for i, j in zip(a, a[1:]):
                        try:
                            lst.append(j / i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            elif next == '^':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j ** i)
                    except:
                        lst.append(None)
            elif next == '_':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(i - j)
                    except:
                        lst.append(None)
            elif next == '`':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(bool(j) ^ bool(i))
                    except:
                        lst.append(None)
            elif next == '{':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(a)
                else:
                    lst = []
                    for i, j in zip(a, a[1:]):
                        try:
                            lst.append(j + i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            elif next == '|':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(i // j)
                    except:
                        lst.append(None)
            elif next == '}':
                stack.rmv(a)
                if not isinstance(a, list):
                    stack.push(a)
                else:
                    lst = []
                    for i, j in zip(a, a[1:]):
                        try:
                            lst.append(j * i)
                        except:
                            lst.append(None)
                    stack.push(lst)
            elif next == '~':
                stack.rmv(a, b)
                if not isinstance(a, list):
                    x = [a]
                else:
                    x = a.copy()
                if not isinstance(b, list):
                    y = [b]
                else:
                    y = b.copy()
                lst = []
                for i, j in zip(x, y):
                    try:
                        lst.append(j or i)
                    except:
                        lst.append(None)
            elif next in '0123456789':
                try:
                    stack.push(input_list[int(next)])
                except:
                    stack.push(input_list)
        index += 1
    return removeNone(stack), vars, False
