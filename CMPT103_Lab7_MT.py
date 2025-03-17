# Mark Tenchavez
# 3083228

# region: Question 1
def list_students(file: str) -> set():
    """
        Purpose: Process the file and extract student id and courses
        Parameter: file as a string that containts data for student and courses
        Return: returns a set of student ID
    """
    # Exception handling
    try:
        with open(file, 'r') as file:
            data_set = file.readlines()
        
        student_id = set()

        for data in data_set:
            # splits data_set into individual list
            line = data.strip().split(',')
            # takes index 0 which is the student id and adds to the student_id set
            for i in line[:1]:
                student_id.add(i)

    except FileNotFoundError:
        print(f'[Errno 2] No such file or directory: \'{file}\'')
        return set()
    
    return student_id

# file = ''
# print(list_students(file))

# file = 'data'
# print(list_students(file))

# file = 'data.txt'
# print(list_students(file))

# students = list_students(file)
# print(len(students))

# endregion

# region: Question 2
def list_courses(file:str) -> set():
    """
        Purpose: Process the file and extract student id and courses
        Parameter: file as a string that containts data for student and courses
        Return: returns a set of courses
    """
    # Exception handling
    try:
        with open(file, 'r') as file:
            data_set = file.readlines()
        
        courses = set()

        for data in data_set:
            # splits data_set into individual list
            line = data.strip().split(',')
            # takes index 1 which is the student id and adds to the courses set
            for i in line[1:]:
                courses.add(i)

    except FileNotFoundError:
        print(f'[Errno 2] No such file or directory: \'{file}\'')
        return set()
    
    return courses

# file = ''
# print(list_courses(file))

# file = 'data'
# print(list_courses(file))

# file = 'data.txt'
# print(list_courses(file))

# courses = list_courses(file)
# print(len(courses))

# endregion

# region: Question 3
def candidate_courses(file:str, student_id:str) -> set():
    """
        Purpose: Process the file and extract student id and courses
        Parameter: file as a string that containts data for student and courses. 
                   student_id as a string 
        Return: returns a set of courses not taken by the student 
    """
    # Exception handling
    try:
        with open(file, 'r') as file:
            data_set = file.readlines()
        
        courses_done = set()
        courses = set()

        # flag student if found or not
        student_found = False
        
        for data in data_set:
            # splits data_set into individual list
            line = data.strip().split(',')
            # takes index 1 which is the student id and adds to the courses set
            for i in line[1:]:
                courses.add(i)
            # if student_id matches number in line, add courses done by studet_id
            if line[0] == student_id:
                student_found = True
                courses_done.add(line[1])

    except FileNotFoundError:
        print(f'[Errno 2] No such file or directory: \'{file}\'')
        return set()
    
    # error for not finding student_id
    if not student_found:
        print(f'Student_id not found. Please try again!')
        return set()

    # needed courses for student_id
    courses_needed = courses - courses_done

    return courses_needed

# file = 'data.txt'
# student_id = ''
# print(candidate_courses(file, student_id))

# file = 'data.txt'
# student_id = '1000'
# print(candidate_courses(file, student_id))

# file = 'data.txt'
# student_id = '1003'
# print(candidate_courses(file, student_id))

# file = 'data.txt'
# student_id = '1001'
# print(candidate_courses(file, student_id))

# endregion

# region: Question 4
def prospective_students(file: str, course_id: str) -> set():
    """
        Purpose: Process the file and extract student id and courses
        Parameter: file as a string that containts data for student and courses. 
                   course_id as a string 
        Return: returns a set of students who have not taken the course
    """
    # Exception handling
    try:
        with open(file, 'r') as file:
            data_set = file.readlines()
        
        students_finished = set()
        students = set()

        # flag student if found or not
        course_found = False
        
        for data in data_set:
            # splits data_set into individual list
            line = data.strip().split(',')
            # takes index 0 which is the students id and adds to the students set
            for i in line[:1]:
                students.add(i)
            # if course_id matches line, add students who finished course_id
            if line[1] == course_id:
                course_found = True
                students_finished.add(line[0])

    except FileNotFoundError:
        print(f'[Errno 2] No such file or directory: \'{file}\'')
        return set()
    
    # error for not finding course_id
    if not course_found:
        print(f'course_id not found. Please try again!')
        return set()

    # students that need the courses
    students_needed = students - students_finished

    return students_needed

# file = 'data.txt'
# course_id = ''
# print(prospective_students(file, course_id))

# file = 'data.txt'
# course_id = 'CMPT100'
# print(prospective_students(file, course_id))

# file = 'data.txt'
# course_id = 'CMPT291'
# print(prospective_students(file, course_id))

# file = 'data.txt'
# course_id = 'CMPT101'
# print(prospective_students(file, course_id))

# endregion