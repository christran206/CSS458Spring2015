##------------------------------------------------------------------------------
## CSS 458 Final Project
## Christopher Tran, Jason Dailey, Kevin Parker
## Methods to import classes and faculty
##------------------------------------------------------------------------------
import numpy as N
from professor import Professor
from course import Course

"""
Data import class provides two methods, one for importing classes and one for faculty.

The courses and faculty are provided to us as CSV files.  Each method opens
the respective CSV, reads the data into an array, then this array is iterated 
through while we make a new object (course or professor) from each row.  Each
of these new objects is appended to a list of similar types of objects.  

We then use these lists to run through the scheduling methods to create schedules
for future quarters. 
"""


def importCourses(path='classes.csv', delimit=',', datatype='str', header=1):
    
    """
    Import courses generates a list of course objects from a data file
    
    Inputs:
        *path - The path to the course data file
        *delimiter - the delimiter between each column of data
        *type - type of data to import as
        *header - number of rows at top to ignore for header data
        
    Outputs:
        A list of course objects defined by the data in the input file
    
    """
    
    # Generate an array from the input file of course details
    courses = N.genfromtxt(path, delimiter=delimit, dtype=datatype, skip_header=header)
    
    # Prepare a list of courses to return
    courseList = []
    
    # Iterate through each row in array, creating new course objects
    for i in xrange(N.shape(courses)[0]):
        nextCourse = Course(None, courses[i][0], None, courses[i][4].lower(), courses[i][2].split("/"), courses[i][1], None, 0, courses[i][3], courses[i][5])
        
        # Append each course to the course list
        courseList.append(nextCourse)
               
    # Return the list
    return courseList

def importFaculty(path='faculty.csv', delimit=',', datatype='str', header=1):
    
    """
    Import Faculty generates a list of professor objects from input file.
    
    Inputs:
        *path - The path to the course data file
        *delimiter - the delimiter between each column of data
        *type - type of data to import as
        *header - number of rows at top to ignore for header data
        
    Outputs:
        A list of professor objects defined by the data in the input file.
    
    """
    
    # Generate an array of data from the file at input path
    faculty = N.genfromtxt(path, delimiter=delimit, dtype=datatype, skip_header=header)
    
    # Create a list of professors to return
    professors = []
    
    # Iterate through the faculty array, creating a professor object for each
    for i in xrange(N.shape(faculty)[0]):
        nextFac = Professor(faculty[i][0], faculty[i][1] == 'Y', float(faculty[i][2]), int(faculty[i][3]), faculty[i][4])
        
        # Append each new professor to the list of professors
        professors.append(nextFac)
        
    # Return professors
    return professors
