##------------------------------------------------------------------------------
## CSS 458 Final Project
## Christopher Tran, Jason Dailey, Kevin Parker
## Methods to import classes and faculty
##------------------------------------------------------------------------------
import numpy as N

def assignProfessors(professors, courses):
    
    """
    Loop through professors and assign professors classes up to specified limit
    
    Inputs:
        professors - The list of professors, and all relevant data
        courses - The list of courses, and all relevant data
    
    """
    for professor in professors:
        numCredits = 0
        #need professor object
        availableCourses = specialty(professor, courses)
        quarter = 0
        #quarter: 0=fall, 1=winter, 2=spring, 3=summer
        while numCredits < (professor.classamount) * 5: #5-credit classes
            credits = addClass(professor, availableCourses, quarter)
            quarter = (quarter + 1) % 4 #Rotates thru the 4 quarters
            numCredits += credits
    

def specialty(professor, courses): 
    """
    Loop through the courses, finding ones the professor can teach
    
    Outputs:
        A shortened course list specific to the professor's specialties
    
    """
    autumn = []
    winter = []
    spring = []
    summer = []
    
    for course in courses:
        if course.expertise == professor.expertise[0] or \
            course.expertise == professor.expertise[1] or \
            course.expertise == professor.expertise[2]:
                n = course.quarter
                if n == 'Autumn':
                    autumn.append(course)
                elif n == 'Winter':
                    winter.append(course)
                elif n == 'Spring':
                    spring.append(course)
                elif n == 'Summer':
                    summer.append(course)
                
                
    return (autumn, winter, spring, summer)
    
    
def addClass(professor, availableCourses, quarter):
    """
    Marks a professor as an instructor for a class in the list
    
    Inputs:
        professor - The current professor to assign to a class
        availableCourses - The list of courses the prof specializes in
        quarter - The quarter to assign the professor a class (0=Fall, 1=Winter,
        3=Spring, 4=Summer)
        
    Outputs:
        The number of credits of the class assigned
    """
    availableCourses[quarter][0].instructor = professor
        
    return availableCourses[quarter][0].credits