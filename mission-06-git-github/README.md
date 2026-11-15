# Mission 6 — Git and GitHub

## 1. Task / objective
The mission asked me to understand version control, stage and commit changes, create a branch, open a Pull Request, and explain the collaboration workflow. I also had to write a glossary of Git commands in my own words.

## 2. Work completed
I practised the basic Git workflow, created a branch called update-about, added a "My Learning" section to the root README on that branch, published the branch to GitHub, opened a Pull Request, and wrote a Git command glossary.

### Task 6.1 — The basic Git workflow

| Git operation | What it does in my own words |
|---|---|
| Check repository status (`git status`) | Shows which files have changed, which are staged and which are not tracked yet |
| Stage selected changes (`git add`) | Chooses which changes will go into the next commit, so I can pick one file at a time |
| Create a commit (`git commit -m`) | Saves a snapshot of the staged changes with a message that says what I did |
| View commit history (`git log --oneline`) | Lists my earlier commits, newest first, each with a short code and message |

**Difference between staging and committing:** Staging chooses which changes will be saved, and committing actually saves them in the history. In `git status`, the file moved from "not staged" to "to be committed" after `git add`, and it disappeared from the list after `git commit`.

### Task 6.2 — Create and use a branch
- Branch name: update-about
- I created the branch, opened the root README.md, and added a section called "My Learning" describing [2 or 3] things I have learned so far.
- I checked the status, staged README.md, committed it with the message "Add My Learning section to README", and published the branch to GitHub.
- `git branch` showed update-about with a star next to it, so I knew I was on the new branch.

### Task 6.3 — Create a Pull Request
- I opened my repository on GitHub and compared update-about with main.
- I created a Pull Request titled "Add My Learning section to README" with a short description of the change.
- On the Files changed tab, only the root README.md was different.
- **PR status:** [Merged, because my instructor asked me to merge it] OR [Open and not merged, because I was not asked to merge it].
- [If merged: I then switched to main on my computer and used `git pull` to bring the latest changes.]

### Task 6.4 — My Git command glossary

| Operation | Command | In my own words |
|---|---|---|
| Initialise a repository | `git init` | Starts Git tracking in a folder |
| Check status | `git status` | Shows what has changed and what is staged |
| Stage changes | `git add` | Picks the changes for the next commit |
| Commit changes | `git commit -m` | Saves a snapshot with a message |
| View history | `git log --oneline` | Lists past commits, newest first |
| Create or list branches | `git switch -c` / `git branch` | Makes a new branch, or shows all branches and which one I am on |
| Switch branches | `git switch` | Moves me to a different branch |
| Publish changes | `git push` | Uploads my commits to GitHub |
| Retrieve remote changes | `git pull` | Downloads new changes from GitHub onto my computer |

## 3. Commands / tools used
- `git status`: checks which files are changed or staged
- `git add`: stages a file for the next commit
- `git commit -m`: saves a snapshot with a message
- `git log --oneline`: shows the commit history in short form
- `git switch -c update-about`: creates a new branch and moves onto it
- `git branch`: lists branches and shows which one I am on
- `git switch main`: moves back to the main branch
- `git push -u origin update-about`: publishes the new branch to GitHub
- `git pull`: brings the latest changes from GitHub onto my computer [only if used]
- Tools: Terminal, VS Code and the GitHub website

## 4. My understanding
Git is a version control system. It records changes to files so I can look at earlier versions and work safely. GitHub is a website that hosts Git repositories online. Staging chooses which changes go into the next snapshot, and committing saves that snapshot. A branch is a separate line of work, so I can change things without touching main. A Pull Request is a request on GitHub to review the changes on a branch and add them to main. They are useful when many people work on the same project, because everyone can work on their own branch and the changes get reviewed before they join main.

## 5. Difficulties faced
When I created the update-about branch, I was not sure which README.md to edit, because every mission folder has one and the project root has one too.

## 6. How I resolved them
I checked the file path at the top of the VS Code tab and ran `git status` before committing. It showed only the root README.md as modified, so I knew I had edited the right file.

## 7. Evidence / files
- README.md in mission-06-git-github, containing my notes and glossary
- Branch on GitHub: update-about
- Pull Request on GitHub: "Add My Learning section to README" ([merged / open])
- My Learning section in the root README.md

## 8. Commit details
- Commit on branch update-about: "Add My Learning section to README"
- Mission 6 commit on main: "Complete Git and GitHub collaboration mission"
The work was pushed to GitHub and the commits are visible there.