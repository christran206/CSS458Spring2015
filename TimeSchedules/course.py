__author__ = 'Christopher'

class Course:

    def __init__(self, sln, number, name, quarter, days, time, instructor, enrolled, capacity):
        self.sln = sln
        self.number = number
        self.name = name
        self.quarter = quarter
        self.days = days
        self.time = time
        self.enrolled = enrolled
        self.capacity = capacity
        self.instructor = instructor
        
    def next(self, number, time, days, capacity, quarter, expertise):
        self.number = number
        self.time = time
        self.days = days
        self.capacity = capacity
        self.quarter = quarter
        self.expertise = expertise
        


