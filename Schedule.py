__author__ = 'Christopher'

class Schedule:

    def __init__(self):
        self.courses = {"autumn": [], "winter": [], "spring": [], "summer": []}

    def addCourse(self, Course, quarter):
        if quarter in self.courses:
            self.courses[quarter].append(Course)

    def __str__(self):
        selfString = ""
        for quarter in self.courses:
            selfString += "=====" +  quarter + "=====" + "\n"
            for course in self.courses[quarter]:
                selfString += course.__str__()
        return selfString
