
# Python Assignment Sorter
Final Project for ITP 116: Accelerated Programming in Python.


## Objectives
Implement an assignment sorting program for practice with lists, comparison operators, and file I/O in Python. 
## Goals
The goal of this project is to create a Python program that takes in a txt file of assignments and sorts them based on their due dates. The program should display the sorted assignments and their corresponding due dates in a chart format.
## Overall Description
The program will read in a txt file that contains a list of assignments with their respective course names and due dates. The program will then sort the assignments by their due dates and display them in a chart format. The chart will have three columns: the first column will display the course names, the second column will display the assignment names, and the third column will display the due dates. For displaying the chart, you are allowed to import the python library, “prettytable.”
## Sample Output
If the input file contains:

```
MATH 126, Homework 5, 4/20/23
ENGL 101, Essay 3, 4/25/23
PHYS 121, Lab report 2, 5/1/23
CHEM 123, Quiz 4, 5/5/23
```

The program should output the following chart:
```
+-------------+---------------+-------------------+
| Course Name |  Assignments  | Deadlines (sorted) |
+-------------+---------------+-------------------+
|   MATH 126  |   Homework 5  |      4/20/23      |
|   ENGL 101  |     Essay 3   |      4/25/23      |
|   PHYS 121  |  Lab report 2 |      5/1/23       |
|   CHEM 123  |     Quiz 4    |      5/5/23       |
+-------------+---------------+-------------------+
```
