# Mission 3 — Understand the operating system

## 1. Task / objective
The mission asked me to explore my operating system, look at running processes, understand paths and file permissions, and explain what an operating system is responsible for.

## 2. Work completed
I used Terminal commands to check my macOS version, my account, my storage and a snapshot of system activity. I viewed the running process list, practised absolute and relative paths, read file permissions, and filled in a table of OS responsibilities.

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | My observation (privacy-safe) |
|---|---|---|
| Operating system / system details (`sw_vers`) | Shows the name and version of the operating system | It showed macOS and its version number |
| Current account identity (`whoami`) | Shows the username of the account that is logged in | It printed my username, which I replaced with [redacted] |
| Available and used storage (`df -h`) | Shows total, used and free disk space | The main disk showed its total size, used space and free space in readable units |
| System activity snapshot (`top -l 1 \| head -n 10`) | Shows a one-time picture of what the computer is doing | The first lines showed the number of processes and the CPU and memory use at that moment |

### Task 3.2 — Understand processes
I opened Google Chrome and viewed the running process list in Activity Monitor.

**What is a process?** A process is a program that is currently running.
**What does the PID column represent?** The PID is a unique number the operating system gives to each running process, so it can tell them apart.

| Process name | Type | PID |
|---|---|---|
| Google Chrome | Application | [71943] |
| Finder | Background / system process | [667] |

Many processes were running even though I had opened only one app.

### Task 3.3 — Understand paths and permissions
I moved between my assignment folder and a subfolder with `cd` and `cd ..`, and used `pwd` to see my location change.

**Absolute vs relative path:** An absolute path is the full location starting from the root of the computer. A relative path starts from the folder I am currently in.
- Absolute example: `/Users/[redacted]/Desktop/digital-detective-8462/mission-02-terminal/README.md`
- Relative example: `mission-02-terminal/README.md`

I ran `ls -l notes.txt` in terminal-practice. The owner's permission letters were `rw-`.

| Permission | Meaning | Can the owner do it? |
|---|---|---|
| r (read) | The contents can be read | Yes |
| w (write) | The file can be changed | Yes |
| x (execute) | The file can be run | No |

I did not change any permissions.

### Task 3.4 — Operating-system responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| Process management | The OS starts and stops programs and decides which one uses the CPU at each moment | Chrome and VS Code run together and the OS shares the CPU between them |
| Memory management | The OS gives each program some RAM while it runs and takes it back when it closes | RAM is freed when I quit an app |
| Device management | The OS controls hardware so programs can use it | When I type, the OS reads the keyboard and passes the letters to the app |
| File management | The OS keeps files and folders organised and lets me create, open and delete them | I created notes.txt and found it again later |
| User interface / shell | The OS gives me a way to use the computer, with windows or by typing commands | I used Terminal to run `ls` |
| Security and permissions | The OS controls who can read, change or run files | My file had rw-, so I can read and write it but not run it |

## 3. Commands / tools used
- `sw_vers`: shows the macOS name and version
- `whoami`: shows the current account name (I redacted the output)
- `df -h`: shows disk space in readable units
- `top -l 1 | head -n 10`: shows one snapshot of system activity, limited to 10 lines
- Activity Monitor: shows running processes and their PIDs
- `pwd`, `cd`, `cd ..`: show and change my location
- `ls -l`: shows file details including permissions
- Tools: Terminal, Activity Monitor and VS Code

## 4. My understanding
The operating system manages the computer and its resources, and gives programs a way to use the hardware. A process is a running program, and each has its own PID. I learned that absolute paths start from the root, while relative paths depend on where I am. I also learned to read permissions: r means read, w means write and x means execute. The OS handles process, memory, device and file management, the user interface, and security.

## 5. Difficulties faced
At first I was not sure which part of the `ls -l` line showed the owner's permissions.

## 6. How I resolved them
I learned that the first character is the type and the next three letters are the owner's permissions. Then I checked my own file's line.

## 7. Evidence / files
- README.md in mission-03-operating-system, containing all four task tables and notes
- Usernames and device names are replaced with [redacted]

## 8. Commit details
Commit message: "Document operating system and file management"
The work was pushed to GitHub and the commit is visible there.