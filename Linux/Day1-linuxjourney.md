# Day 01 – Shell & Basic Linux Commands

## Introduction to the Shell

The shell is a command-line interface that allows users to interact directly with the operating system. It accepts typed commands, processes them, and communicates with the kernel to execute those commands.

A terminal is a program that opens a shell session. When you open your terminal, you are interacting with the shell.

Most Linux distributions use Bash (Bourne Again Shell) as the default shell.

The shell prompt (usually `$`) indicates that the shell is ready to accept commands from the user.

---

## Commands Learned and Practiced

### 1. `pwd`

`pwd` stands for Print Working Directory.  
It displays the absolute path of the current working directory.

```bash
pwd
```

---

### 2. `cd`

`cd` stands for Change Directory. It is used to navigate between directories.

Before using `cd`, it is important to understand:

- Absolute path – The full path starting from the root directory (`/`)
- Relative path – A path relative to your current directory

Example using an absolute path:

```bash
cd /home/samuel/Downloads/Gologin
```

Example using a relative path:

```bash
cd appimage
```

Useful navigation shortcuts:

- `.` → Current directory  
- `..` → Parent directory  
- `~` → Home directory  
- `-` → Previous directory  

---

### 3. `ls`

`ls` lists files and directories in the current directory.

```bash
ls
```

Common flags:

- `-a` → Shows hidden files (files starting with `.`)
- `-l` → Displays detailed information (long format)
- `-r` → Lists files in reverse order

Flags can be combined:

```bash
ls -la
```

---

### 4. `touch`

`touch` has multiple uses depending on how it is used.

Creating a new file:

```bash
touch file.txt
```

If the file already exists, `touch` updates its timestamp to the current time.

Advanced usage:

Set a file’s timestamp to match another file:

```bash
touch -r file1.txt file2.txt
```

Set a specific date and time:

```bash
touch -d "2026-02-12 10:00" file.txt
```

---

### 5. `file`

The `file` command provides information about the type of a file based on its content.

```bash
file filename
```

It analyzes the file content rather than relying only on file extensions.

---

### 6. `cat`

`cat` stands for concatenate. It can be used in several ways.

View file contents:

```bash
cat myfile.txt
```

Display multiple files together:

```bash
cat file1.txt file2.txt
```

Create a new file using redirection:

```bash
cat > newfile.txt
```

Common flags:

- `-n` → Numbers all output lines
- `-b` → Numbers only non-empty lines

---

### 7. `history`

The `history` command displays previously executed commands.

```bash
history
```

Useful shortcuts:

- Up arrow (↑) → Scroll through previous commands
- `!!` → Execute the most recent command again

Common flags:

- `-c` → Clear command history
- `-w` → Write history to file
- `-d <number>` → Delete a specific command from history

---

### 8. `cp`

`cp` is used to copy files and directories.

Basic syntax:

```bash
cp [source] [destination]
```

Basic file copying:

```bash
cp file.txt backup.txt
```

Copying directories recursively:

```bash
cp -r folder1 folder2
```

Wildcards allow copying multiple files using patterns:

- `*` → Matches any number of characters
- `?` → Matches a single character
- `[]` → Matches specific characters

Example:

```bash
cp *.jpg /home/samuel/Pictures
```

Common flags:

- `-r` → Recursive (copy directories)
- `-i` → Interactive (ask before overwrite)
- `-f` → Force overwrite
- `-p` → Preserve file attributes (timestamps, ownership, permissions)

---

## Key Concepts Learned

- Linux is case-sensitive.
- The shell communicates with the kernel to execute commands.
- The Linux file system follows a hierarchical structure.
- Commands can accept options (flags) to modify their behavior.
- Absolute and relative paths determine how navigation works.

---

## Practice Summary

During this session, I:

- Navigated between directories using both absolute and relative paths
- Created and modified files
- Copied files and directories
- Used wildcards for bulk operations
- Reviewed and reused command history

This session strengthened my understanding of how the Linux shell works and how basic file system operations are performed.

