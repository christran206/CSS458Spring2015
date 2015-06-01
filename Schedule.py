__author__ = 'Christopher'




class Schedule:
    """
    Schedule object defines an annual schedule of courses in the program.

    Schedule object consists of a dictionary defining courses that are part of
    either the autumn, winter, spring, or summar quarter.  

    After courses are added to a schedule, we use a scheduler method to assign
    available professors to courses within the schedule. 
    """

    def __init__(self):
        """
        Schedule object is initialized by creating blank dictionary of quarters.
        """
        self.courses = {"autumn": [], "winter": [], "spring": [], "summer": []}

    def addCourse(self, Course, quarter):
        """
        Adds a given course to the schedule, based on given quarter.
        
        If the given quarter is valid in this schedule, append the passed course
        to the schedules dictionary of courses, under the correct quarter.
        
         Inputs:
             *Course: The course to append if valid
             *quarter: The quarter to assign this course to
         
         Returns:
             None         
        """
        if quarter in self.courses:
            self.courses[quarter].append(Course)

    def sortQuarters(self):
        """
        Sorts the courses in each quarter of the schedule.
        
        Calls sorth method for the list of courses in each quarter defined by
        this schedule.
        
        Inputs:
            None
        Returns:
            None
        """
        for quater in self.courses:
            self.courses[quater].sort()

    def __str__(self):
        """
        String output method for schedule object. 
        
        Schedule is output by listing each course contained within each quarter.

        Inputs:
            None
        Returns:
            None              
        
        """
        selfString = ""
        for quarter in self.courses:
            selfString += "=====" + quarter + "=====" + "\n"
            for course in self.courses[quarter]:
                selfString += course.__str__() + "\n"
        return selfString

    def unassignedCourses(self):
        """
        Returns a list of courses that do not have a professor assigned.
        
        Method is used when calling the scheduler method to determine which
        courses are left without a professor unassigned.  Once the schedule is 
        complete, also is used to display the remaining courses that were unable
        to be filled. 
        
        In our implementation we chose to ignore capstone level courses, and 
        instead only focus on courses that had a specific defined expertise and
        regularly scheduled days and times.
        
        Inputs:
            None
        Returns:
            list of courses across all quarters contained within this schedule
            that do not have a professor assigned
        """
        unassigned = []
        for quarter in self.courses:
            for course in self.courses[quarter]:
                #Ignore courses that are defined as capstone type courses
                if course.instructor is None and course.expertise != "Capstone":
                    unassigned.append(course)
        return unassigned