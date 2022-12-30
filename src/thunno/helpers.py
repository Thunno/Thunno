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

def az_track(string, ind):
    azs = 0
    ind -= 1
    while ind >= 0:
        if string[ind] in 'AaZz':
            azs += 1
        else:
            break
        ind -= 1
    return azs % 2

def removeNone(l):
    return Stack([x for x in l if x is not None])

def numberToBaseDigits(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def f(d, l):
    if l < len(d):
        return d[l]
    return chr(32 + l)

def numberToBase(num, base):
    if base <= 0:
        return str(num)
    if base == 1:
        return num * '0'
    digits = st.digits + st.ascii_uppercase + st.ascii_lowercase + '+/'
    return ''.join(map(lambda L: f(digits, L), numberToBaseDigits(num, base)))

def primeFactors(num):
    return [i for i in range(2, num+1) if num % i == 0 and all(i % n for n in range(2, i))]

def nextPrime(num):
    while True:
        if all(num % i for i in range(2, num)):
            return num
        num += 1

def fromListOfDigits(num, base):
    r = 0
    for x, y in enumerate(reversed(num)):
        r += base**x * int(y)
    return r

def gcd(l):
    if not l:
        return 0
    for x in reversed(range(1, max(l))):
        if all(y % x == 0 for y in l):
            return x

def lcm(l):
    if not l:
        return 0
    i = max(l)
    while 1:
        i += 1
        if all(i % x == 0 for x in l):
            return i

def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def nPr(n, r):
    f = math.factorial
    return f(n) // f(n-r)

def primeFactorisation(num):
    r = []
    i = 2
    while num > 1:
        if num % i == 0:
            r.append(i)
            num //= i
        else:
            i += 1
    return r

def primes_up_to(num):
    i = 2
    while i <= num:
        if all(i % x for x in range(2, i)):
            yield i
        i += 1

def primeFactorExponents(num):
    factors = primeFactorisation(num)
    return [factors.count(prime) for prime in primes_up_to(max(factors))]

def toRomanNumerals(num):
    ret = ''
    if num < 0:
        num = -num
        ret += '-'
    symbols = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    for s, n in symbols.items():
        while num >= n:
            ret += s
            num -= n
    return ret

def fromRomanNumerals(s):
    ret = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == 'M':
            ret += 1000
        elif c == 'D':
            ret += 500
        elif c == 'L':
            ret += 50
        elif c == 'V':
            ret += 5
        elif c == 'C':
            i += 1
            if s[i] == 'M':
                ret += 900
            else:
                i -= 1
        elif c == 'X':
            i += 1
            if s[i] == 'C':
                ret += 90
            else:
                i -= 1
        elif c == 'I':
            i += 1
            if s[i] == 'X':
                ret += 9
            else:
                i -= 1
        i += 1
    return ret

class TerminateProgramError(BaseException):
    pass

class Stack(list):
    def push(self, item):
        self.insert(0, item)
    def rmv(self, *items):
        for item in items:
            if item in self:
                self.remove(item)