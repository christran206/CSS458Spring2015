__author__ = 'Christopher'

class Course:
    
    """
    Course object.

    Course object defines a course in the UWB CSS Program.  A course has a SLN,
    course number, name, quarter, days, time, instructor, amount of students enrolled,
    maximum student capacity, and the expertise of the class.  

    We store the given input file of course as a list of course objects and the
    assign instructors to courses by matching expertises.  
    """
    
    def __init__(self, sln, number, name, quarter, days, time, instructor, enrolled, capacity, expertise=""):
        """
        Course is initialized by assigning passed data to be stored within
        
        Inputs: 
            *SLN: The SLN of the course
            *number: the course number
            *name: The course name
            *quarter: which quarter the course is held
            *days: Days of the week the course is taught
            *time: The times the course is taught
            *instructor: assigned professor to teach the course
            *enrolled: current enrollment of the course
            *capacity: Max capacity of the course
            *expertise: The defined expertise of the course. Defaults to blank
        
        Returns:
            A new course object with above defined data
        
        """
        self.sln = int(sln) if sln is not None else 0  # Check valid int and default to 0
        self.number = int(number)
        self.name = name
        self.quarter = quarter
        self.days = [day.upper() for day in days if len(day) != 0]  # Only include values with length more than 0
        self.time = time
        self.enrolled = int(enrolled) if enrolled is not None and enrolled else 0  # enrollment has to be an int
        self.capacity = int(capacity) if capacity is not None and capacity else 15  # Capacity has to have a value
        self.instructor = instructor
        self.expertise = expertise

    def __str__(self):
        """
        String method for course
        
        Course is represented as the SLN, Number, name, quarter, days, time, instructor,
        enrollment, capacity, and expertise.
        """
        
        return "SLN: %s\tNumber: %s\tName: %s\tQuarter: %s\tDays: %s\tTime: %s\tInstructor %s\tEnrolled: %s\t\
        Capacity: %s\tExpertise: %s" % \
               (self.sln, self.number, self.name, self.quarter, self.days, self.time, self.instructor.name if self.instructor is not None else None, self.enrolled,
                self.capacity, self.expertise)

    def __repr__(self):
        """
        String representation method for course
        
        Course is represented as the SLN, Number, name, quarter, days, time, instructor,
        enrollment, capacity, and expertise.
        """
        
        return "SLN: %s\tNumber: %s\tName: %s\tQuarter: %s\tDays: %s\tTime: %s\tInstructor %s\tEnrolled: %s\t\
        Capacity: %s\tExpertise: %s" % \
               (self.sln, self.number, self.name, self.quarter, self.days, self.time, self.instructor.name if self.instructor is not None else None, self.enrolled,
                self.capacity, self.expertise)

    def __lt__(self, other):
        """
        Lessthan method for course.
        
        One course is defined to be less than another if the course number is 
        less than the other's
        
        Inputs:
            *other: the other course to compare
            
        Return:
            True if this is less than other, false if not
        """
        return self.number < other.number

    def courseTimeOverlap(self, course):
        """
        Determines if two courses overlap in time
        :param course: Course to compare against
        :return: True if the times overlap, false if they don't
        """
        # Check if days overlap
        daysOverlap = False
        for day in self.days:
            if day in course.days:
                daysOverlap = True
                break

        # Check if this course and the passed in course have a time
        if daysOverlap and self.time and course.time and self.time != "to be arranged" and course.time != "to be arranged":
            # get start and end time of this course object
            thisStart = int(self.time.split("-")[0])
            thisEnd = int(self.time.split("-")[1])
            # get startand end time of the passed in course
            compareStart = int(course.time.split("-")[0])
            compareEnd = int(course.time.split("-")[1])
            # Check if this start time is between the times of the course to compare
            if compareStart <= thisStart <= compareEnd:
                return True
            # Check if this end time is between the times of the course to compare
            elif compareStart <= thisEnd <= compareEnd:
                return True
        return False

    def courseOverlap(self, time):
        """
        Determines if the course time overlaps with a start and end as a string
        :param time: String with two values split with a "-"
        :return: true if times overlap, false if they don't
        """
        # Check if this course and the passed in course have a time
        if self.time and time and self.time != "to be arranged" and time != "to be arranged":
            # get start and end time of this course object
            thisStart = int(self.time.split("-")[0])
            thisEnd = int(self.time.split("-")[1])
            # get startand end time of the passed in course
            compareStart = int(time.split("-")[0]) if time else 0
            compareEnd = int(time.split("-")[1]) if time else 0
            # Check if this start time is between the times of the course to compare
            if compareStart <= thisStart <= compareEnd:
                return True
            # Check if this end time is between the times of the course to compare
            elif compareStart <= thisEnd <= compareEnd:
                return True
        return False
