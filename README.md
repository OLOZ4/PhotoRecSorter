# PhotoRecSorter

The purpose of these files are to quickly manage your recovered files and put them in folders coresponding to their file extentions.
For example file test.txt will go to folder named txt.

USAGE:

First, edit main.py file and change:
recup_dir - to path to your recup directories. Make sure, that it ends with recup_dir.
destination - change it to your destination directory. 
k - change it to number of directories you have

In array "file_types" I have written a few most popular file extnetions, program will search for files with these extentions.
Well it's inefficent, so I created "ExtentionFinder.py". By using this script you will save a lot of time by only searching files with extentions that only exist.

All you need to do is in file ExtentionFinder.py change "folder_prefix" variable to your recup directory. Make sure it ends with recup_dir.
Then execute ExtentionFinder.py. It will output all file extentions that are in your recup directories. Copy the output to main.py "file_types" array and that's it!
Launch main.py

You could also specify manually what type of files you would like to sort by manually filling "file_types" array in main.py 
