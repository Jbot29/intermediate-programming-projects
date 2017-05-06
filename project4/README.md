# Project 4: Create a File System and simple terminal emulator.

We can think about a filesystem as an upside down tree. A nested data structure where branches
can have subbranches.

On a unix based system the root is /

There can then be directories and files underneath each path.

/
users/
     steve/
          budget.csv
     racheal/
          books.txt
lib/
   shared/
         man.so


## Part one

We are going to build a simple terminal shell emulator that has an in memory filesystem.

* The user sees a prompt "$>" where they can enter on of the following commands.

* When the user starts the FS already has a basic structure with directories and files. You can
use the example above or whatever. 

ls
pwd
cd <name>|..|.



## Part Two

Add new functionality to create new directories, and files.

* mkdir - Allow the user to create a directory.
* touch - Creates a new file.
* Allow commands to work with ../../<name> or absolute path names

## Part Three

Allow the user to add and view file data.

* echo - use echo plus piping to be able to append a string to a file
* cat - cat dumps the files data
