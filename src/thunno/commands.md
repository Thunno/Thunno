# List of commands in Thunno

* `a` represents the value at the top of the stack
* `b` represents the second value on the stack
* `c` represents the third value on the stack

|Command|Elements Popped|Explanation|
|-|-|-|
|`b`|`a`|Binary. Push `bin(a)`|
|`c`|`a`, `b`|Count. Count the occurrences of `a` in b|
|`d`|`a`|Digits/characters of `a`|
|`e`|`a`|Map. Usage `e CODE E`|
|`f`|`a`|Factors of `a`, including 1 and `a`|
|`g`|`a`, `b`|Regex. Push `findall(a, b)`|
|`h`|`a`|Hexadecimal. Push `hex(a)`|
|`i`|`a`|Convert `a` to integer|
|`j`|`a`, `b`|Join. Push `b.join(a)`|
|`k`|`a`, `b`|Index of `b` in `a`|
|`l`||Empty list. Push `[]`|
|`m`|`a`|Minimum. Push `min(a)`|
|`n`|`a`|Negate. Push `-a`|
|`o`|`a`|Inverse. Push `1/a`|
|`p`|`a`, `b`|Greater than or equal to. Push `b >= a`|
|`q`|`a`, `b`|Less than or equal to. Push `b <= a`|
|`r`|`a`|Reverse `a`|
|`s`|`a`, `b`|Swap. `b` will now be on top|
|`t`|`a`|Square root. Push `sqrt(a)`|
|`u`|`a`|Uppercase. Push `a.upper()`|
|`v`|`a`|Filter out None from `a`|
|`x`||Push the variable `x`. Defaults to 0|
|`y`||Push the variable `y`. Defaults to 1|
|`B`|`a`|Convert `a` from binary to integer|
|`C`|`a`|Character. Push `chr(a)`|
|`D`|`a`|Duplicate. Push `a` twice after popping|
|`E`||(End of map: `e`)|
|`F`|`a`|Factorial. Push `a!`|
|`G`|`a`, `b`|Filter. Discard all `b` from a.|
|`H`|`a`|Convert `a` from hexadecimal to integer|
|`I`||Push the input list|
|`J`|`a`|Join. Push `''.join(a)`|
|`K`|`a`|Pop. No-op after popping `a`|
|`L`|`a`|Length. Push `len(a)`|
|`M`|`a`|Maximum. Push `max(a)`|
|`N`|`a`|Prime check. Push `is_prime(a)`|
|`O`|`a`|Ordinal. Push `ord(a)`|
|`P`|`a`|Product. Push the elemental product of `a`|
|`Q`|`a`, `b`|Not equal to. Push `b != a`|
|`R`|`a`|Range. Push `[0, 1, ..., a-1]`|
|`S`|`a`|Sum. Push `sum(a)`|
|`T`|`a`, `b`|Append. Append `a` to `b`|
|`U`|`a`|Lowercase. Push `a.lower()`|
|`V`|`a`|Eval. Evaluate `a` as Python code|
|`X`|`a`|Set `x` to `a`|
|`Y`|`a`|Set `y` to `a`|
|`.`|`a`|Apply the next command to the elements of `a`|
|`+`|`a`, `b`|Addition. Push `b + a`|
|`-`|`a`, `b`|Subtraction. Push `b - a`|
|`*`|`a`, `b`|Multiplication. Push `b * a`|
|`/`|`a`, `b`|Division. Push `b / a`|
|`,`|`a`, `b`|Integer division. Push `b // a`|
|`^`|`a`, `b`|Exponentiation. Push `b ** a`|
|`%`|`a`, `b`|Modulus. Push `b % a`|
|`_`|`a`, `b`|Swapped subtraction. Push `a - b`|
|``\``|`a`, `b`|Swapped division. Push `a / b`|
|`\|`|`a`, `b`|Swapped integer division. Push `a // b`|
|`@`|`a`, `b`|Swapped exponentiation. Push `a ** b`|
|`$`|`a`, `b`|Swapped modulus. Push `a % b`|
|`:`|`a`, `b`|Two-input range (start, stop)|
|`;`|`a`, `b`, `c`|Three-input range (start, stop, step)|
|`=`|`a`, `b`|Equals. Push `b == a`|
|`>`|`a`, `b`|Greater than. Push `b > a`|
|`<`|`a`, `b`|Less than. Push `b < a`|
|`&`|`a`, `b`|And. Push `b and a`|
|`~`|`a`, `b`|Or. Push `b or a`|
|<code>`</code>|`a`, `b`|Xor. Push `b ^ a`|
|`!`|`a`|Not. Push `not a`|
|`{`|`a`|For loop. Usage `{ CODE }`|
|`}`||(End of for loop: `{`)|
|`[`||Infinite loop. Usage `[ CODE ]`|
|`]`||(End of infinite loop: `[`)|
|`)`||Break from a loop|
|`?`|`a`|If. If `a` is truthy, run the following code|
|`(`||Else/Endif. Usage `? IF_TRUTHY ( IF_FALSY (`|
|`#`||(Start of a comment. Everything up to the next newline is ignored.)|
|`AA`|`a`|Average. Push `sum(a) / len(a)`|
|`AB`|`a`, `b`|Convert `b` to base `a`|
|`AC`|`a`|Cosine (degrees). Push `cos(a)`|
|`AD`|`a`, `b`|Absolute difference. Push `abs(b - a)`|
|`AE`|`a`|Enumerate. Push `[[0, a[0]], [1, [a[1]]], ...]`|
|`AF`|`a`|Prime factors. Push the unique prime factors of `a`|
|`AG`|`a`, `b`|GCD. Push `gcd(a, b)`|
|`AH`|`a`, `b`|Indexing (1-based, modular). Push `b[a-1]`|
|`AI`|`a`, `b`|Indexing (0-based, modular). Push `b[a]`|
|`AJ`|`a`|First element. Push `a[0]`|
|`AK`|`a`|Last element. Push `a[-1]`|
|`AL`|`a`, `b`|LCM. Push `lcm(a, b)`|
|`AM`|`a`, `b`|Maximum. Push `max(a, b)`|
|`AN`|`a`|Next prime. Push the smallest prime greater than `a`|
|`AO`|`a`, `b`|Hypotenuse. Push `sqrt(a**2 + b**2)`|
|`AP`|`a`, `b`|Split `b` into `a` roughly equal chunks (left-heavy)|
|`AQ`||(For ATO.) Run the rest of the code for each of the inputs|
|`AR`|`a`, `b`, `c`|Replace all instances of `b` with `a` in `c`|
|`AS`|`a`|Sine (degrees). Push `sin(a)`|
|`AT`|`a`|Tangent (degrees). Push `tan(a)`|
|`AU`|`a`|Convert `a` from degrees to radians|
|`AV`|`a`|Convert `a` from radians to degrees|
|`AW`|`a`|Logarithm. Push `log_10(a)`|
|`AX`|`a`|Exponent. Push `e**a`|
|`AY`|`a`, `b`|Logarithm. Push `log_a(b)`|
|`AZ`||Uppercase alphabet. Push `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`|
|`Aa`|`a`|Median. If needed, the mean of the middle two is given|
|`Ab`|`a`, `b`|Convert `b` from base `a`|
|`Ac`|`a`|Inverse cosine (degrees). Push `arccos(a)`|
|`Ad`|`a`, `b`|Get `b` as an integer from `a` list of digits in base `a`|
|`Ae`||Euler's Number. Push `2.718281828459045`|
|`Af`|`a`|Filter from `a` where result is truthy. Usage `Af CODE Ah`|
|`Ag`|`a`|GCD from a list. Push `gcd(*a)`|
|`Ah`||(End of filter: `Af`)|
|`Ai`|`a`|First `a` integers where result is truthy. Usage `Ai CODE Aj`|
|`Aj`||(End of first n integers: Ai)|
|`Ak`|`a`|`a`th integer where result is truthy. Usage `Ak CODE Am`|
|`Al`|`a`|LCM from a list. Push `lcm(*a)`|
|`Am`||(End of `a`th integer: `Ak`)|
|`An`||First integer where result is truthy. Usage `An CODE Ao`|
|`Ao`||(End of first integer: `An`)|
|`Ap`|`a`, `b`|Split `b` into chunks of length `a` (leftover in separate chunk)|
|`Aq`|`a`, `b`|Containment. Push `a in b`|
|`Ar`|`a`, `b`, `c`|Replace all instances of regex `b` with `a` in `c`|
|`As`|`a`|Inverse sine (degrees). Push `arcsin(a)`|
|`At`|`a`|Inverse tangent (degrees). Push `arctan(a)`|
|`Au`|`a`|Dump the contents of `a` onto the stack|
|`Av`|`a`|Evaluate `a` as Thunno code|
|`Aw`||Pi. Push `3.141592653589793`|
|`Ax`||Assign `a` to `x` without popping|
|`Ay`||Assign `a` to `y` without popping|
|`Az`||Lowercase alphabet. Push `'abcdefghijklmnopqrstuvwxyz'`|
|`A+`|`a`, `b`|Literal addition (no vectorising). Push `b + a`|
|`A-`|`a`, `b`|Literal subtraction (no vectorising). Push `b - a`|
|`A*`|`a`, `b`|Literal multiplication (no vectorising). Push `b * a`|
|`A/`|`a`, `b`|Literal division (no vectorising). Push `b / a`|
|`A@`|`a`, `b`|Literal matrix multiplication (no vectorising). Push `b @ a`|
|`A<`|`a`, `b`|Literal less than (no vectorising). Push `b < a`|
|`A>`|`a`, `b`|Literal greater than (no vectorising). Push `b > a`|
|`A\|`|`a`, `b`|Literal bitwise or (no vectorising). Push `b \| a`|
|`A&`|`a`, `b`|Literal bitwise and (no vectorising). Push `b & a`|
|`A^`|`a`, `b`|Literal xor (no vectorising). Push `b ^ a`|
|`A%`|`a`, `b`|Literal modulus (no vectorising). Push `b % a`|
|`A=`|`a`, `b`|Literal equality (no vectorising). Push `b == a`|
|`A!`|`a`, `b`|Literal inequality (no vectorising). Push `b != a`|
|`A~`|`a`|Literal bitwise not (no vectorising). Push `~a`|
|`A?`|`a`|If. If `a` is truthy, run the following code|
|`A:`||Else. Otherwise, run the following code|
|`A;`||Endif. Usage `A? IF_TRUTHY A: IF_FALSY A;`|
|`A{`|`a`|Enumerated loop. Usage `A{ CODE A}`|
|`A}`||(End of enumerated loop: `A{`)|
|`A[`||Infinite loop. Usage `A[ CODE A]`|
|`A]`||(End of infinite loop: `A[`)|
|`A(`|`a`, `b`|Zipped map. Usage `A( CODE A)`|
|`A)`||(End of zipped map: `A(`)|
|`A$`||Push the first input|
|<code>A`</code>||Push the last input|
|`A,`|`a`|Push the ath input|
|`A.`|`a`|Push the ath-last input|
|`A#`||Push the length of the input list|
|`A"`||Formatted string literal|
|`A'`||Formatted string literal|
|`A_`||Space character. Push `' '`|
|``A\``||Newline character, Push `'\n'`|
|`A1`||Push `16`|
|`A2`||Push `32`|
|`A3`||Push `64`|
|`A4`||Push `128`|
|`A5`||Push `256`|
|`A6`||Push `512`|
|`A7`||Push `1024`|
|`A8`||Push `2048`|
|`A9`||Push `4096`|
|`A0`||Push `8192`|
|`aA`||Push `10`|
|`aB`||Push `15`|
|`aC`||Push `20`|
|`aD`||Push `25`|
|`aE`||Push `30`|
|`aF`||Push `35`|
|`aG`||Push `40`|
|`aH`||Push `45`|
|`aI`||Push `50`|
|`aJ`||Push `55`|
|`aK`||Push `60`|
|`aL`||Push `65`|
|`aM`||Push `70`|
|`aN`||Push `75`|
|`aO`||Push `80`|
|`aP`||Push `85`|
|`aQ`||Push `90`|
|`aR`||Push `95`|
|`aS`||Push `100`|
|`aT`||Push `105`|
|`aU`||Push `110`|
|`aV`||Push `115`|
|`aW`||Push `120`|
|`aX`||Push `125`|
|`aY`||Push `130`|
|`aZ`||Push `135`|
|`aa`||Push `140`|
|`ab`||Push `145`|
|`ac`||Push `150`|
|`ad`||Push `155`|
|`ae`||Push `160`|
|`af`||Push `165`|
|`ag`||Push `170`|
|`ah`||Push `175`|
|`ai`||Push `180`|
|`aj`||Push `185`|
|`ak`||Push `190`|
|`al`||Push `195`|
|`am`||Push `200`|
|`an`||Push `205`|
|`ao`||Push `210`|
|`ap`||Push `215`|
|`aq`||Push `220`|
|`ar`||Push `225`|
|`as`||Push `230`|
|`at`||Push `235`|
|`au`||Push `240`|
|`av`||Push `245`|
|`aw`||Push `250`|
|`ax`||Push `255`|
|`ay`||Push `260`|
|`az`||Push `265`|
|`a0`||Push `270`|
|`a1`||Push `275`|
|`a2`||Push `280`|
|`a3`||Push `285`|
|`a4`||Push `290`|
|`a5`||Push `295`|
|`a6`||Push `300`|
|`a7`||Push `305`|
|`a8`||Push `310`|
|`a9`||Push `315`|
|`a`&nbsp;&nbsp;`\n`||Push `320`|
|<code>a</code>&nbsp;<code>(space)</code>||Push `325`|
|`a!`||Push `330`|
|`a"`||Push `335`|
|`a#`||Push `340`|
|`a$`||Push `345`|
|`a%`||Push `350`|
|`a&`||Push `355`|
|`a'`||Push `360`|
|`a(`||Push `365`|
|`a)`||Push `370`|
|`a*`||Push `375`|
|`a+`||Push `380`|
|`a,`||Push `385`|
|`a-`||Push `390`|
|`a.`||Push `395`|
|`a/`||Push `400`|
|`a:`||Push `455`|
|`a;`||Push `460`|
|`a<`||Push `465`|
|`a=`||Push `470`|
|`a>`||Push `475`|
|`a?`||Push `480`|
|`a@`||Push `485`|
|`a[`||Push `620`|
|``a\``||Push `625`|
|`a]`||Push `630`|
|`a^`||Push `635`|
|`a_`||Push `640`|
|<code>a`</code>||Push `645`|
|`a{`||Push `780`|
|`a\|`||Push `785`|
|`a}`||Push `790`|
|`a~`||Push `795`|
|`ZA`|`a`|Absolute value. Push `abs(a)`|
|`ZB`|`a`|Python-style boolean. Push `bool(a)`|
|`ZC`|`a`, `b`|Combinations. Push `nCr(b, a)`|
|`ZD`|`a`|Convert `a` from a list of digits in base 10 to an integer|
|`ZE`|`a`, `b`|Push `b.endswith(a)`|
|`ZF`|`a`|Prime factorisation of `a`|
|`ZG`|`a`, `b`|Extend/truncate `b` to length `a`|
|`ZH`|`a`|Head. Push `a[:-1]`|
|`ZI`|`a`|Double. Push `a * 2`|
|`ZJ`|`a`|Triple. Push `a * 3`|
|`ZK`|`a`|Print `a`|
|`ZL`|`a`|Print `a` without a trailing newline|
|`ZM`||Push the stack|
|`ZN`|`a`, `b`|Prepend `a` to `b`|
|`ZO`|`a`|Wrap. Push `[a]`|
|`ZP`|`a`, `b`|Pair. Push `[b, a]`|
|`ZQ`||Terminate the program|
|`ZR`|`a`, `b`|Move `a` elements from the front of `b` to the back|
|`ZS`|`a`, `b`|Move `a` elements from the back of `b` to the front|
|`ZT`|`a`|Tail. Push `a[1:]`|
|`ZU`|`a`|Push the unique elements of `a`|
|`ZV`|`a`, `b`|Push `b.startswith(a)`|
|`ZW`|`a`|Case. Push `0` if lowercase, `1` if uppercase, `-1` otherwise|
|`ZX`|`a`|Toggle the case of `a`|
|`ZY`|`a`|Encode/decode `a` with the ROT-13 cipher|
|`ZZ`|`a`, `b`|Zip `a` and `b`|
|`Za`|`a`|Push `all(a)`|
|`Zb`|`a`|Push `any(a)`|
|`Zc`|`a`|Halve. Push `a/2`|
|`Zd`|`a`|Square. Push `a**2`|
|`Ze`|`a`|Cube. Push `a**3`|
|`Zf`|`a`|Repeat the following code `a` times. Usage `Zf CODE Zg`|
|`Zg`||(End of repeat: `Zf`)|
|`Zh`|`a`|Exponents of the prime factorisation of `a`|
|`Zi`|`a`, `b`|Split `b` on `a`|
|`Zj`|`a`, `b`|Partition `b` on `a`|
|`Zk`|`a`, `b`|Uninterleave `b` with length `a`|
|`Zl`|`a`|Uninterleave `a` with length 2|
|`Zm`|`a`|Push `ceil(a)`|
|`Zn`|`a`|Push `floor(a)`|
|`Zo`|`a`|Modal value in `a`|
|`Zp`|`a`, `b`|Permutations. Push `nPr(b, a)`|
|`Zq`|`a`|Is `a` a palindome?|
|`Zr`|`a`|Range. Push `max(a) - min(a)`|
|`Zs`|`a`, `b`, `c`|Swap `b` and `c`|
|`Zt`|`a`|Transpose `a`|
|`Zu`|`a`, `b`|Round `b` to `a` decimal places|
|`Zv`|`a`|Round `a` to the nearest integer|
|`Zw`|`a`|Push a random element of `a`|
|`Zx`|`a`, `b`|Remove the first `a` elements from `b`|
|`Zy`|`a`, `b`|Remove the last `a` elements from `b`|
|`Zz`|`a`, `b`, `c`|Zip `b` and `c`, filling empty cells with `a`|
|`Z!`|`a`, `b`|Cartesian product of `a` and `b`|
|`Z"`||Push the next two characters as a string|
|`Z'`||Push the next three characters as a string|
|`Z#`||Ignore the next character|
|`Z$`||Push the input list, sorted|
|`Z%`||Push the input list, reversed|
|`Z&`||Push the input list, all converted to string|
|`Z(`||Push the input list, all converted to float|
|`Z)`||Push the input list, all converted to integer|
|`Z*`||Push the product of the input list|
|`Z+`||Push the sum of the input list|
|`Z,`||Push the first input plus one|
|`Z-`||Push the first input minus one|
|`Z.`||Push the first input doubled|
|`Z/`||Push the first input halved|
|`Z:`||Push the maximum input|
|`Z;`||Push the minimum input|
|`Z<`||Push the last input minus one|
|`Z=`||Are all the inputs equal?|
|`Z>`||Push the last input plus one|
|`Z?`||Is the first input truthy?|
|`Z[`||Push the first two inputs|
|``Z\``||Push the truthy inputs|
|`Z]`||Push the last two inputs|
|`Z^`||Push the inputs which are not equal to the first input|
|`Z_`||Push the inputs which are not equal to the last input|
|<code>Z`</code>||Push the unique inputs|
|`Z{`||Push the first three inputs|
|`Z\|`||Push the falsy inputs|
|`Z}`||Push the last three inputs|
|`Z~`||Push the logical not of each input|
|`Z1`||Push `10`|
|`Z2`||Push `100`|
|`Z3`||Push `1000`|
|`Z4`||Push `10000`|
|`Z5`||Push `100000`|
|`Z6`||Push `1000000`|
|`Z7`||Push `10000000`|
|`Z8`||Push `100000000`|
|`Z9`||Push `1000000000`|
|`Z0`||Push `10000000000`|
|`zA`|`a`|Negative absolute value. Push `-abs(a)`|
|`zB`|`a`|Convert `a` to octal|
|`zC`||Push the ASCII codepage (32-126 inclusive) as a string|
|`zD`|`a`, `b`|Divmod. Push `[b // a, b % a]`|
|`zE`||Swapped divmod. Push `[a // b, a % b]`|
|`zF`|`a`|Push every factorial less than `a`|
|`zG`|`a`|Group `a` by the result. Usage `zF CODE zG`|
|`zH`||(End of group: `zF`)|
|`zI`|`a`, `b`|Push every index in `b` where the element equals `a`|
|`zJ`|`a`|Push `'\n'.join(a)`|
|`zK`|`a`, `b`|Push `b.zfill(a)`|
|`zL`|`a`, `b`|Push `b.ljust(a)`|
|`zM`||Maximum of the stack|
|`zN`|`a`|Push `a.isnumeric()`|
|`zO`|`a`|Push `a.isalpha`|
|`zP`|`a`, `b`|Permutations of `b` with length `a`|
|`zQ`|`a`, `b`|Combinations of `b` with length `a`|
|`zR`|`a`, `b`|Combinations of `b` with length `a` with replacement|
|`zS`|`a`|Cartesian product of the elements of `a`|
|`zT`|`a`|Type of `a`: `0` = `int`; `1` = `float`; `2` = `str`; `3` = `list`|
|`zU`|`a`|Push `a.capitalize()`|
|`zV`|`a`|Push `a.title()`|
|`zX`||Push `x * 2`|
|`zY`||Push `y * 2`|
|`zZ`|`a`|Push `zip(*a)`|
|`za`|`a`|Sign. Push: `1` if `a > 0`; `-1` if `a < 0`; `0` if `a == 0`|
|`zb`|`a`|Is `a` a strictly increasing sequence?|
|`zc`|`a`|Is `a` a strictly decreasing sequence?|
|`zd`||Push the source code (doexn't work in loops)|
|`ze`|`a`|Are all the elements of `a` equal?|
|`zf`||Push `False`|
|`zg`|`a`, `b`|String index of right-most `a` in `b`|
|`zh`|`a`, `b`|List index of right-most `a` in `b`|
|`zi`|`a`|Integer square root of `a`|
|`zj`|`a`, `b`|List concatenation. Push `a + b`|
|`zk`|`a`|Append `reversed(a)` to `a`|
|`zl`|`a`, `b`|String difference. Push `ord(b) - ord(a)`|
|`zm`|`a`, `b`|String sum. Push `ord(b) + ord(a)`|
|`zn`|`a`|Push `[max(a), min(a)]`|
|`zo`|`a`|Push `a.isdigit()`|
|`zp`|`a`|Push `a.isprintable()`|
|`zq`|`a`|Are all the elements of `a` different?|
|`zr`|`a`|Push `range(len(a))`|
|`zs`|`a`, `b`, `c`|Swap `a` and `c`|
|`zt`|`a`|Triplicate. Push `a` thrice after popping|
|`zu`|`a`|Quadruplicate. Push `a` four times after popping|
|`zv`|`a`|Convert `a` to a Roman numeral|
|`zx`|`a`|Convert `a` from a Roman numeral|
|`zy`|`a`|Group `a` by consecutive items|
|`zz`|`a`|Zip `a` with itself|
|`z!`||Push `1` and then the first input|
|`z"`||Push the next four characters as a string|
|`z'`||Push the next five characters as a string|
|`z#`||Ignore the next two characters|
|`z$`|`a`, `b`|Zipped swapped modulus. Push `[a[0] % b[0], a[1] % b[1], ...]`|
|`z%`|`a`, `b`|Zipped modulus. Push `[b[0] % a[0], b[1] % a[1], ...]`|
|`z&`|`a`, `b`|Zipped `and`. Push `[b[0] and a[0], b[1] and a[1], ...]`|
|`z(`|`a`|Running sum of `a`. Push `[a[0], a[0] + a[1], ...]`|
|`z)`|`a`|Running product of `a`. Push `[a[0], a[0] * a[1], ...]`|
|`z*`|`a`, `b`|Zipped multiplication. Push `[b[0] * a[0], b[1] * a[1], ...]`|
|`z+`|`a`, `b`|Zipped addition. Push `[b[0] + a[0], b[1] + a[1], ...]`|
|`z,`|`a`, `b`|Zipped integer division. Push `[b[0] // a[0], b[1] // a[1], ...]`|
|`z-`|`a`, `b`|Zipped subtraction. Push `[b[0] - a[0], b[1] - a[1], ...]`|
|`z.`|`a`, `b`|Apply the next command to the zipped elements of `a` and `b`|
|`z/`|`a`, `b`|Zipped division. Push `[b[0] / a[0], b[1] / a[1], ...]`|
|`z:`|`a`|Sort `a`|
|`z;`|`a`|Reverse-sort `a`|
|`z<`|`a`, `b`|Zipped less than. Push `[b[0] < a[0], b[1] < a[1], ...]`|
|`z=`|`a`, `b`|Zipped equality. Push `[b[0] == a[0], b[1] == a[1], ...]`|
|`z>`|`a`, `b`|Zipped greater than. Push `[b[0] > a[0], b[1] > a[1], ...]`|
|`z?`|`a`|Convert all elements of `a` to booleans.|
|`z*`|`a`, `b`|Zipped swapped exponentiation. Push `[a[0] ** b[0], a[1] ** b[1], ...]`|
|`z[`|`a`|Forward-differences of `a`. Push `[a[1] - a[0], a[2] - a[1], ...]`|
|``z\``|`a`, `b`|Zipped swapped division. Push `[a[0] / b[0], a[1] / b[1], ...]`|
|`z]`|`a`|Forward-quotients of `a`. Push `[a[1] / a[0], a[2] / a[1], ...]`|
|`z^`|`a`, `b`|Zipped exponentiation. Push `[b[0] ** a[0], b[1] ** a[1], ...]`|
|`z_`|`a`, `b`|Zipped swapped subtraction. Push `[a[0] - b[0], a[1] - b[1], ...]`|
|<code>z`</code>|`a`, `b`|Zipped `xor`. Push `[b[0] ^ a[0], b[1] ^ a[1], ...]`|
|`z{`|`a`|Forward-sums of `a`. Push `[a[1] + a[0], a[2] + a[1], ...]`|
|`z\|`|`a`, `b`|Zipped swapped integer division. Push `[a[0] // b[0], a[1] // b[1], ...]`|
|`z}`|`a`|Forward-products of `a`. Push `[a[1] * a[0], a[2] * a[1], ...]`|
|`z~`|`a`, `b`|Zipped `or`. Push `[b[0] or a[0], b[1] or a[1], ...]`|
|`z0`||Push the first input|
|`z1`||Push the second input|
|`z2`||Push the third input|
|`z3`||Push the fourth input|
|`z4`||Push the fifth input|
|`z5`||Push the sixth input|
|`z6`||Push the seventh input|
|`z7`||Push the eigth input|
|`z8`||Push the ninth input|
|`z9`||Push the tenth input|

***

<sub>**MIT License**</sub>

<sub>Copyright (c) 2023 Rujul Nayak</sub>

<sub>Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:</sub>

<sub>The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.</sub>

<sub>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.</sub>