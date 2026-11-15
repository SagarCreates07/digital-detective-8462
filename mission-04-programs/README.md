# Mission 4 — How programs run

## 1. Task / objective
The mission asked me to write and run a simple Python program, and then compare how a compiler and an interpreter translate or run programs.

## 2. Work completed
I created a file called hello.py with a one-line program that prints a message, and ran it using Python 3 from Terminal. Then I filled in a comparison table of compiler and interpreter and explained the difference.

### Task 4.1 — Create and run a Python program
hello.py contains one line that displays "Hello from Python". I ran it with `python3 hello.py` and the message appeared in Terminal.

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates the whole program before it runs | Reads and runs the program line by line while it runs |
| Typical output | A separate file the computer can run directly (machine code) | No separate file, the result appears as the program runs |
| One example | C compiler (gcc) | Python interpreter (python3) |
| One advantage | The finished program usually runs faster | Easy to test small changes quickly |

**Difference in my own words:** A compiler translates the whole program into machine code before it runs, so the finished program usually runs fast. An interpreter runs the code line by line as it goes, which makes it easier to test changes. I ran hello.py with the Python interpreter and the message appeared straight away without creating a separate file.

## 3. Commands / tools used
- `touch hello.py`: creates the empty Python file
- `python3 hello.py`: runs the file using the Python 3 interpreter
- `print()`: the Python function that displays text on the screen
- Tools: Terminal and VS Code

## 4. My understanding
A program is a set of instructions written in a language like Python. The computer needs them translated before it can run them. A compiler does the translation for the whole program first, while an interpreter translates and runs it as it goes. Python is usually run with an interpreter. Real languages can mix both ideas, so the difference is not always strict.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- hello.py in mission-04-programs
- README.md in mission-04-programs

## 8. Commit details
Commit message: "Compare compilers and interpreters"
The work was pushed to GitHub and the commit is visible there.