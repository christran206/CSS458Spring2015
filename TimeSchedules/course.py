__author__ = 'Christopher'

class Course:

    def __init__(self, sln, number, name, quarter, days, time, instructor, enrolled, capacity, expertise = ""):
        self.sln = sln
        self.number = number
        self.name = name
        self.quarter = quarter
        self.days = days
        self.time = time
        self.enrolled = enrolled
        self.capacity = capacity
        self.instructor = instructor
        self.expertise = expertise 
   

    def courseTimeOverlap(self, course):
        """
        Determines if two courses overlap in time
        :param course: Course to compare against
        :return: True if the times overlap, false if they don't
        """
        # Check if this course and the passed in course have a time
        if self.time != "to be arranged" and course.time != "to be arranged":
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
        if self.time != "to be arranged" and time != "to be arranged":
            # get start and end time of this course object
            thisStart = int(self.time.split("-")[0])
            thisEnd = int(self.time.split("-")[1])
            # get startand end time of the passed in course
            compareStart = int(time.split("-")[0])
            compareEnd = int(time.split("-")[1])
            # Check if this start time is between the times of the course to compare
            if compareStart <= thisStart <= compareEnd:
                return True
            # Check if this end time is between the times of the course to compare
            elif compareStart <= thisEnd <= compareEnd:
                return True
        return False
