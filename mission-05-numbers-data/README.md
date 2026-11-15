# Mission 5 — Numbers and data

## 1. Task / objective
The mission asked me to convert numbers between decimal, binary and hexadecimal by hand, verify the results with Python, build a small number converter program, and explain how text is stored using character encoding.

## 2. Work completed
I converted seven numbers by hand and showed my working. I checked all of them in the Python interactive environment, then wrote number_converter.py and tested it with three numbers. Finally I found ASCII codes for two letters and answered questions about text encoding.

### Task 5.1 — Convert numbers by hand

**1. Decimal 13 to binary**

| Division by 2 | Quotient | Remainder |
|---|---|---|
| 13 ÷ 2 | 6 | 1 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Reading the remainders from bottom to top gives 1101.
Answer: 13₁₀ = 1101₂

**2. Decimal 25 to binary**

| Division by 2 | Quotient | Remainder |
|---|---|---|
| 25 ÷ 2 | 12 | 1 |
| 12 ÷ 2 | 6 | 0 |
| 6 ÷ 2 | 3 | 0 |
| 3 ÷ 2 | 1 | 1 |
| 1 ÷ 2 | 0 | 1 |

Reading the remainders from bottom to top gives 11001.
Answer: 25₁₀ = 11001₂

**3. Binary 1010 to decimal**
1010 = (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)
     = 8 + 0 + 2 + 0
     = 10
Answer: 1010₂ = 10₁₀

**4. Binary 1101 to decimal**
1101 = (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)
     = 8 + 4 + 0 + 1
     = 13
Answer: 1101₂ = 13₁₀

**5. Hexadecimal A to decimal**
In hexadecimal, A = 10.
Answer: A₁₆ = 10₁₀

**6. Hexadecimal 1F to decimal**
In hexadecimal, F = 15.
1F = (1 × 16¹) + (15 × 16⁰)
   = 16 + 15
   = 31
Answer: 1F₁₆ = 31₁₀

**7. Binary 1111 to hexadecimal**
The binary number is one group of four digits.
1111 = 8 + 4 + 2 + 1 = 15
In hexadecimal, 15 = F.
Answer: 1111₂ = F₁₆

**Summary**

| # | Conversion | Answer |
|---|---|---|
| 1 | Decimal 13 to binary | 1101 |
| 2 | Decimal 25 to binary | 11001 |
| 3 | Binary 1010 to decimal | 10 |
| 4 | Binary 1101 to decimal | 13 |
| 5 | Hexadecimal A to decimal | 10 |
| 6 | Hexadecimal 1F to decimal | 31 |
| 7 | Binary 1111 to hexadecimal | F |

### Task 5.2 — Verify using Python
I opened the Python interactive environment with `python3` and used built-in functions to check each manual answer.

| Expression tested | Result | Matches my manual answer? |
|---|---|---|
| bin(13) | '0b1101' | Yes |
| bin(25) | '0b11001' | Yes |
| int("1010", 2) | 10 | Yes |
| int("1101", 2) | 13 | Yes |
| int("A", 16) | 10 | Yes |
| int("1F", 16) | 31 | Yes |
| hex(15) | '0xf' | Yes |

The 0b at the start of a binary result and the 0x at the start of a hex result only show which number system is used. They are not part of the value.

### Task 5.3 — Build a small number converter
I wrote number_converter.py. It asks for a positive decimal number, then prints the binary and hexadecimal forms.

Code:

    text = input("Enter a positive decimal number: ")
    number = int(text)

    binary = bin(number)[2:]
    hexadecimal = hex(number)[2:]

    print("Binary:", binary)
    print("Hexadecimal:", hexadecimal)

I ran it with `python3 number_converter.py` and tested three numbers:

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | 1101 | d |
| 25 | 11001 | 19 |
| 255 | 11111111 | ff |

**How it works:** `input()` always returns text, so `int()` turns it into a whole number. `bin()` converts the number to binary and `hex()` converts it to hexadecimal. Both add a prefix (0b or 0x), so `[2:]` skips the first two characters to leave only the digits.

### Task 5.4 — How is text stored?

| Character | ASCII decimal code |
|---|---|
| A | 65 |
| a | 97 |

**Why a computer needs an encoding standard:** A computer stores everything as numbers, so everyone must agree which number stands for which character. Without a standard, the same text could look like nonsense on a different computer.

**A character not in basic ASCII:** The rupee sign ₹. `ord("₹")` gave 8377, which is above 127, the highest code in basic ASCII.

**ASCII vs UTF-8:** ASCII covers a small basic set of characters, while UTF-8 can represent a much wider range, including symbols and many languages.

## 3. Commands / tools used
- `python3`: opens the Python interactive environment
- `bin()`: converts a decimal number to binary
- `hex()`: converts a decimal number to hexadecimal
- `int(text, base)`: converts text written in another base to a decimal number
- `input()`: asks the user to type a value
- `ord()`: gives the number code for a character
- `python3 number_converter.py`: runs my converter program
- `exit()`: leaves the Python environment
- Tools: Terminal and VS Code

## 4. My understanding
Computers store everything as bits, which are 0s and 1s. Binary uses base 2 and hexadecimal uses base 16, and every conversion is about place values: in binary the places are 1, 2, 4, 8, and in hexadecimal they are 1, 16, 256. To go from decimal to binary I divide by 2 and read the remainders from bottom to top. My converter uses `input()` to get a number as text, `int()` to make it a real number, and `bin()` and `hex()` to show it in the other systems. Text is stored as numbers too, so an encoding standard like ASCII or UTF-8 is needed to agree which number means which character.

## 5. Difficulties faced
When I tested my converter, I wrote the wrong binary output for 25 in my notes. I wrote 1101, but my hand working gave 11001.

## 6. How I resolved them
I compared my notes with my hand working and ran the program again with 25. It printed 11001, so I corrected my notes.

## 7. Evidence / files
- README.md in mission-05-numbers-data
- number_converter.py in mission-05-numbers-data

## 8. Commit details
Commit message: "Build number converter and practise data representation"
The work was pushed to GitHub and the commit is visible there.