__author__ = 'Christopher'


class Course:
    def __init__(self, sln, number, name, quarter, days, time, instructor, enrolled, capacity, expertise=""):
        self.sln = int(sln) if sln is not None else 0  # Check valid int and default to 0
        self.number = int(number)
        self.name = name
        self.quarter = quarter
        self.days = [day for day in days if len(day) != 0]  # Only include values with length more than 0
        self.time = time
        self.enrolled = int(enrolled) if enrolled is not None and enrolled else 0  # enrollment has to be an int
        self.capacity = int(capacity) if capacity is not None and capacity else 15  # Capacity has to have a value
        self.instructor = instructor
        self.expertise = expertise

    def __str__(self):
        return "SLN: %s\tNumber: %s\tName: %s\tQuarter: %s\tDays: %s\tTime: %s\tInstructor %s\tEnrolled: %s\t\
        Capacity: %s\tExpertise: %s" % \
               (self.sln, self.number, self.name, self.quarter, self.days, self.time, self.instructor.name if self.instructor is not None else None, self.enrolled,
                self.capacity, self.expertise)

    def __repr__(self):
        return "SLN: %s\tNumber: %s\tName: %s\tQuarter: %s\tDays: %s\tTime: %s\tInstructor %s\tEnrolled: %s\t\
        Capacity: %s\tExpertise: %s" % \
               (self.sln, self.number, self.name, self.quarter, self.days, self.time, self.instructor.name if self.instructor is not None else None, self.enrolled,
                self.capacity, self.expertise)

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
        if daysOverlap and self.time != "to be arranged" and course.time != "to be arranged":
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
