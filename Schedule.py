__author__ = 'Christopher'

class Schedule:

    def __init__(self):
        self.courses = {"autumn": [], "winter": [], "spring": [], "summer": []}

    def addCourse(self, Course, quarter):
        if quarter in self.courses:
            self.courses[quarter].append(Course)

    def sortQuarters(self):
        for quater in self.courses:
            self.courses[quater].sort()

    def __str__(self):
        selfString = ""
        for quarter in self.courses:
            selfString += "=====" + quarter + "=====" + "\n"
            for course in self.courses[quarter]:
                selfString += course.__str__() + "\n"
        return selfString

    def unassignedCourses(self):
        unassigned = []
        for quarter in self.courses:
            for course in self.courses[quarter]:
                if course.instructor is None and course.expertise != "Capstone":
                    unassigned.append(course)
        return unassigned