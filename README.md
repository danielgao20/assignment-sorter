
# Python Assignment Sorter
Final Project for ITP 116: Accelerated Programming in Python.

## Inspiration
To be completed.

## Objectives
Implement an assignment sorting program for practice with lists, comparison operators, and file I/O in Python. 
## Goals
The goal of this project is to create a Python program that takes in a txt file of assignments and sorts them based on their due dates. The program should display the sorted assignments and their corresponding due dates in a chart format.
## Overall Description
The program will read in a txt file that contains a list of assignments with their respective course names and due dates. The program will then sort the assignments by their due dates and display them in a chart format. The chart will have three columns: the first column will display the course names, the second column will display the assignment names, and the third column will display the due dates. For displaying the chart, you are allowed to import the python library, “prettytable.”
## Sample Output
If the input file contains:

```
CSE 142, Programming Assignment 2, 5/17/23
PHYS 121, Lab Report 3, 5/1/23
MATH 124, Quiz 6, 5/10/23
CHEM 142, Lab Report 2, 5/3/23
CSE 143, Homework 7, 5/8/23
ECON 200, Term Paper, 5/13/23
MATH 126, Midterm Exam, 5/12/23
PHYS 121, Homework 4, 4/29/23
ENGL 131, Essay 3, 5/20/23
CSE 142, Lab 5, 5/15/23
MATH 125, Homework 7, 5/19/23
CHEM 142, Quiz 4, 4/28/23
CSE 143, Lab 7, 5/18/23
ENGL 131, Presentation, 5/6/23
MATH 124, Homework 6, 5/22/23
PHYS 121, Quiz 3, 4/26/23
ECON 200, Quiz 3, 5/24/23
MATH 126, Homework 8, 5/25/23
CHEM 142, Lab Report 3, 5/2/23
CSE 142, Homework 6, 5/23/23
MATH 125, Quiz 5, 5/21/23
ENGL 131, Essay 4, 5/27/23
CSE 143, Programming Assignment 3, 5/26/23
PHYS 121, Homework 5, 5/5/23
ECON 200, Homework 5, 5/11/23
MATH 124, Midterm Exam, 5/14/23
CHEM 142, Quiz 5, 5/28/23
CSE 142, Lab 6, 5/30/23
MATH 125, Homework 8, 6/1/23
ENGL 131, Final Exam, 6/2/23
```

The program should output the following chart:
```
+-------------+--------------------------+-------------------+
| Course Name |        Assignment        | Deadline (sorted) |
+-------------+--------------------------+-------------------+
|   PHYS 121  |          Quiz 3          |      4/26/23      |
|   CHEM 142  |          Quiz 4          |      4/28/23      |
|   PHYS 121  |        Homework 4        |      4/29/23      |
|   PHYS 121  |       Lab Report 3       |       5/1/23      |
|   CHEM 142  |       Lab Report 3       |       5/2/23      |
|   CHEM 142  |       Lab Report 2       |       5/3/23      |
|   PHYS 121  |        Homework 5        |       5/5/23      |
|   ENGL 131  |       Presentation       |       5/6/23      |
|   CSE 143   |        Homework 7        |       5/8/23      |
|   MATH 124  |          Quiz 6          |      5/10/23      |
|   ECON 200  |        Homework 5        |      5/11/23      |
|   MATH 126  |       Midterm Exam       |      5/12/23      |
|   ECON 200  |        Term Paper        |      5/13/23      |
|   MATH 124  |       Midterm Exam       |      5/14/23      |
|   CSE 142   |          Lab 5           |      5/15/23      |
|   CSE 142   | Programming Assignment 2 |      5/17/23      |
|   CSE 143   |          Lab 7           |      5/18/23      |
|   MATH 125  |        Homework 7        |      5/19/23      |
|   ENGL 131  |         Essay 3          |      5/20/23      |
|   MATH 125  |          Quiz 5          |      5/21/23      |
|   MATH 124  |        Homework 6        |      5/22/23      |
|   CSE 142   |        Homework 6        |      5/23/23      |
|   ECON 200  |          Quiz 3          |      5/24/23      |
|   MATH 126  |        Homework 8        |      5/25/23      |
|   CSE 143   | Programming Assignment 3 |      5/26/23      |
|   ENGL 131  |         Essay 4          |      5/27/23      |
|   CHEM 142  |          Quiz 5          |      5/28/23      |
|   CSE 142   |          Lab 6           |      5/30/23      |
|   MATH 125  |        Homework 8        |       6/1/23      |
|   ENGL 131  |        Final Exam        |       6/2/23      |
+-------------+--------------------------+-------------------+
```
