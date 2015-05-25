##------------------------------------------------------------------------------
## CSS 458 Final Project
## Christopher Tran, Jason Dailey, Kevin Parker
## Methods to import classes and faculty
##------------------------------------------------------------------------------
import numpy as N
from professor import Professor
from TimeSchedules.course import Course

def importCourses(path ='classes.csv', delimit = ',', type = 'str', header = 1):
    
    """
    Import courses generates a numpy array of courses from a data file
    
    Inputs:
        *path - The path to the course data file
        *delimiter - the delimiter between each column of data
        *type - type of data to import as
        *header - number of rows at top to ignore for header data
        
    Outputs:
        A details x number of courses numpy array of course data
    
    """
    
    courses = N.genfromtxt(path, delimiter = delimit, \
    dtype = type, skip_header=header)
    
    courseList = []
    
    
       
    return courses

def importFaculty(path ='faculty.csv', delimit = ',', type = 'str', header = 1):
    
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
    faculty = N.genfromtxt(path, delimiter = delimit, \
    dtype = type, skip_header=header)
    
    # Create a list of professors to return
    professors = []
    
    # Iterate through the faculty array, creating a professor object for each
    for i in xrange(N.shape(faculty)[0]):
        nextFac = Professor(faculty[i][0],faculty[i][1],float(faculty[i][2]), \
        int(faculty[i][3]), faculty[i][4], faculty[i][6], faculty[i][6])
        
        # Append each new professor to the list of professors
        professors.append(nextFac)
        
    # Return professors
    return professors


