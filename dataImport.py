##------------------------------------------------------------------------------
## CSS 458 Final Project
## Christopher Tran, Jason Dailey, Kevin Parker
## Methods to import classes and faculty
##------------------------------------------------------------------------------
import numpy as N

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
    
    return courses

def importFaculty(path ='faculty.csv', delimit = ',', type = 'str', header = 1):
    
    """
    Import Faculty generates a numpy array of faculty from a data file
    
    Inputs:
        *path - The path to the course data file
        *delimiter - the delimiter between each column of data
        *type - type of data to import as
        *header - number of rows at top to ignore for header data
        
    Outputs:
        A details x number of faculty numpy array of faculty information
    
    """
    
    faculty = N.genfromtxt(path, delimiter = delimit, \
    dtype = type, skip_header=header)
    
    return faculty


