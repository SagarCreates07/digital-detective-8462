## 1. Task / objective
The mission asked me to use the command line to look at folders, create and manage practice files, understand flags and pipes, and explain what a package manager does.

## 2. Work completed
I practised nine basic Terminal operations, made a terminal-practice folder with a text file and a backup, compared a normal listing with a detailed one, used a pipe, and checked for Homebrew.

## Task 2.1 — Basic Terminal operations

| Operation / command name | What it does | What I observed |
|---|---|---|
| Current-directory display (`pwd`) | Shows the full path of the folder I am in | It printed the path ending in mission-02-terminal, with my username shown as [redacted] |
| Directory listing (`ls`) | Lists the files and folders in the current location | It showed README.md |
| Detailed listing (`ls -l`) | Lists the same items with extra details like permissions, size and date | Each item appeared on its own line with permissions, size and the date it was changed |
| Change directory (`cd`) | Moves me to another folder | After `cd ..` the path changed to the parent folder, and `cd mission-02-terminal` brought me back |
| Create directory (`mkdir`) | Makes a new folder | A folder called practice appeared when I ran `ls` |
| Create empty file (`touch`) | Makes a new empty file | original.txt was created inside practice and had nothing in it |
| Copy file (`cp`) | Makes a duplicate of a file under a new name | There were two files, original.txt and copy.txt |
| Move / rename file (`mv`) | Changes a file's name or moves it to another place | copy.txt was gone and renamed.txt appeared in its place |
| Display file contents (`cat`) | Prints what is written inside a file | It showed the line I added with `echo` |

## Task 2.2 — Practise file changes safely

I created a folder called terminal-practice inside mission-02-terminal and worked only inside it. I made notes.txt with one line, added a second line without removing the first, and used cat to confirm both lines were there. Then I made a backup copy of the file and renamed the backup to notes-saved.txt.

**Replacing vs adding:** Using > replaces everything in the file with the new text, so the old content is lost. Using >> adds the new text to the end and keeps what was already there. When I tested > on the backup file, only the new line was left.

**Copying vs moving:** Copying makes a second file and the original stays where it is. Moving (or renaming) does not make a second file, so the old name is gone. After cp I had two files, and after mv the old name disappeared and the new name appeared.

**What the current-directory display shows:** It shows the full path of the folder I am working in, so I know exactly where I am in the computer. I replaced my username with [redacted] for privacy.

**Why directory listing is useful:** It shows me which files and folders are in my current location. I can check that a command worked, for example that a new file was created or renamed.

## Task 2.3 — Flags and pipes

**Normal listing (ls):** It showed only the visible files and folders in the project folder, such as README.md and the mission folders. It did not show hidden items.

**Detailed listing with hidden files and readable sizes (ls -lah):** It showed one item per line with permissions, owner, size and the date changed. Hidden items starting with a dot, like .git, now appeared. Sizes were written in a readable form like 4.0K. (Owner and group names are [redacted] for privacy.)

**What changed and why:** A flag is an extra option that changes how a command behaves. The -l flag gives the long, detailed format. The -a flag includes hidden files. The -h flag makes file sizes readable for people instead of showing raw numbers. I used all three together as -lah.

**Pipe (ls -l | head -n 3):** The pipe symbol | takes the output of the command on its left and sends it to the command on its right instead of printing it. Here the left side, ls -l, produced the detailed listing. The right side, head -n 3, kept only the first 3 lines of it. So I saw a short part of the listing instead of the whole thing.

## Task 2.4 — Package managers

**Command used:** `brew --version` and `brew list`

**What I observed:** Homebrew was installed and showed its version number. `brew list` showed the packages installed through it.

**Why package managers are useful:** A package manager installs, updates and removes software using simple commands, so I don't have to find and set up each program by hand. It also keeps everything in one place, which makes updating or removing a program easier and less likely to go wrong.

## 3. Commands / tools used
- `pwd`: shows the folder I am in
- `ls`, `ls -l`, `ls -lah`: list files in different levels of detail
- `cd`: moves between folders
- `mkdir`: makes a folder
- `touch`: makes an empty file
- `echo` with `>` and `>>`: writes text into a file, replacing or adding
- `cp`: copies a file
- `mv`: moves or renames a file
- `cat`: shows a file's contents
- `head` and the pipe `|`: show only the first lines of another command's output
- `brew --version`, `brew list`: check Homebrew and see what it manages
- Tools: Terminal and VS Code

## 4. My understanding
Terminal lets me control the computer by typing commands. Flags change how a command works, such as `-l` for more detail. A pipe lets one command's output become another command's input. I also learned that `>` replaces a file's text while `>>` adds to it, and that copying keeps the original while moving does not. Package managers make installing and updating software easier.

## 5. Difficulties faced
I got an "Operation not permitted" message when I ran `ls` in the wrong place.

## 6. How I resolved them
I moved back into my project folder, and I checked the Terminal folder permission in macOS settings. I did not use administrator commands.

## 7. Evidence / files
- README.md in mission-02-terminal
- terminal-practice folder with notes.txt and notes-saved.txt

## 8. Commit details
Commit message: "Complete Terminal and file management mission"
The work was pushed to GitHub and the commit is visible there.