# NAME: <Daniel Gao>
# ID: <6765756413>
# DATE: 2023-05-03
# DESCRIPTION: ITP Final Project, implement an assignment sorting program for practice with lists, comparison operators,
#               and file I/O in Python.

# function to read in assignments from a file and store them in a list of dictionaries
def read_assignments(filename):
    """
    read in assignments from a file and store them in a list of dictionaries.
    """
    assignments = []
    with open(filename, 'r') as f:  # open the file for reading
        for line in f:  # loop over each line in the file
            line = line.strip()  # remove any leading/trailing whitespace
            if line:  # skip any empty lines
                # split the line into its components and store them in a dictionary
                course, assignment, deadline_str = line.split(', ')
                deadline = deadline_str.split('/')
                assignments.append({'course': course, 'assignment': assignment, 'month': int(deadline[0]),
                                    'day': int(deadline[1]), 'year': int(deadline[2])})
    return assignments


# function to sort assignments by deadline
def sort_assignments(assignments):
    """
    sort a list of dictionaries representing assignments by their deadline date.
    """
    for i in range(len(assignments)):
        for j in range(i + 1, len(assignments)):
            # compare the deadlines of the current assignment and the next assignment
            if assignments[j]['year'] < assignments[i]['year'] or \
                (assignments[j]['year'] == assignments[i]['year'] and
                 assignments[j]['month'] < assignments[i]['month']) or \
                (assignments[j]['year'] == assignments[i]['year'] and
                 assignments[j]['month'] == assignments[i]['month'] and
                 assignments[j]['day'] < assignments[i]['day']):
                # swap the assignments if the next one is due sooner than the current one
                assignments[i], assignments[j] = assignments[j], assignments[i]
    return assignments


# function to display assignments in a nice table format
def display_assignments(assignments):
    """
    Display a list of assignments in a formatted table with columns for course name, assignment name, and
    deadline date sorted by earliest deadline first.
    """
    # determine the maximum length of each column
    max_course_len = max([len(assignment['course']) for assignment in assignments])
    max_assignment_len = max([len(assignment['assignment']) for assignment in assignments])

    # create the header and separator lines for the table
    header = f"| {'Course Name':<{max_course_len}} | {'Assignment':<{max_assignment_len}} | {'Deadline':<10} |"
    separator = f"+{'-'*(max_course_len+2)}+{'-'*(max_assignment_len+2)}+{'-'*12}+"

    # print out the header and separator lines
    print(separator)
    print(header)
    print(separator)

    # loop over each assignment and print it in a row of the table
    for assignment in assignments:
        deadline_str = f"{assignment['month']}/{assignment['day']}/{assignment['year'] % 100:02d}"
        row = f"| {assignment['course']:<{max_course_len}} | {assignment['assignment']:<{max_assignment_len}} |" \
              f" {deadline_str:<10} |"
        print(row)
    print(separator)


# main program logic
def main():
    print("Assignment Sorter")
    filename = input('Enter the name of the file containing assignments: ')
    # read in the assignments from the file
    assignments = read_assignments(filename)
    # sort the assignments by deadline
    sorted_assignments = sort_assignments(assignments)
    # display the assignments in a table format
    display_assignments(sorted_assignments)


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()



