if __name__ == '__main__':
    n = int(input())   # step 1: read number of students
    student_marks = {} # step 2: create an empty dictionary
    
    # step 3: read n lines of student data
    for _ in range(n):
        line = input().split()              # split line by spaces
        name, scores = line[0], line[1:]    # first item is name, rest are marks
        scores = list(map(float, scores))   # convert marks to numbers (float)
        student_marks[name] = scores        # store in dictionary
    
    query_name = input()  # step 4: read which student we want
    
    # step 5: calculate average
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    # step 6: print with 2 decimal places
    print("{:.2f}".format(avg))
