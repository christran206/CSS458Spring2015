##------------------------------------------------------------------------------
## NOT WORKING YET
##
## CSS 458 Final Project
## Christopher Tran, Jason Dailey, Kevin Parker
## Methods to import classes and faculty
##------------------------------------------------------------------------------
import numpy as N

def assignProfessors(professors, courses):
    
    """
    Loop through professors and assign professors classes up to specified limit
    
    Inputs:
        *professors - The list of professors, and all relevant data
        *courses - The list of courses, and all relevant data
        
    Outputs:
        A multi-level dictionary containing course info and assigned professor
    
    """
    for professor in professors:
        numClasses = 0
        #need professor object
        availableCourses = specialty(professor, courses)
        while numClasses < professor[2]:
            addClass(professor, availableCourses)
        #   availableCourses = specialty(professor, courses)
        #a = 0

    schedule = 0
    return schedule

def specialty(professor, courses):
    """
    Loop through the courses, finding ones the professor can teach
    
    Outputs:
        A shortened course list specific to the professor's specialties
    
    """
    summer = [4]
    autumn = [1]
    winter = [2]
    spring = [3]
    for course in courses:
        if course[5] == professor[4] or \
            course[5] == professor[5] or \
            course[5] == professor[6]:
                n = course[4]
                if n == 'Autumn':
                    autumn.append(course)
                elif n == 'Winter':
                    winter.append(course)
                elif n == 'Spring':
                    spring.append(course)
                elif n == 'Summer':
                    summer.append(course)
                
                
    return (autumn, winter, spring, summer)
    
def addClass(professor, availableCourses):
    """
    Marks a professor as an instructor for a class in the list
    
    """
    return 0