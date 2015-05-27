__author__ = 'Christopher'
import random

class Scheduler:

    def __init__(self, Schedule, Professors):
        self.Schedule = Schedule
        self.Professors = Professors

    def fillschedule(self):
        """
        Takes the Schedule and Professors and fills the courses with professors if possible
        :return: None
        """
        # make lists of full-time and part time professors
        fulltime = [professor for professor in self.Professors if professor.fullTime]
        parttime = [professor for professor in self.Professors if not professor.fullTime]

        # shuffle professors
        random.shuffle(fulltime)
        # iterate through professors
        for professor in fulltime:
            # loop until professor is full of courses
            professorAvailable = True
            professorNotCompatCount = 0
            while professorAvailable:
                # Select one class from each quarter at a time
                for quarter in self.Schedule.courses:
                    # get the current course allotment of the professor
                    allotment = 0
                    for coursequarter in professor.teaching:
                        for course in professor.teaching[coursequarter]:
                            courseLevel = course.number/100
                            if courseLevel == 1:
                                allotment += 0.5
                            else:
                                allotment += 1.0
                    # if the professor can't teach anymore, break loop to the next professor
                    # Also check if the professor has gone through 4 loops without compatible courses
                    if allotment >= professor.classamount or professorNotCompatCount == 4:
                        professorAvailable = False
                        break
                    courses = self.Schedule.courses[quarter]
                    # get only courses where professor has an expertise
                    compatiblecourses = [course for course in courses if course.expertise in professor.expertise and course.instructor == None]
                    if len(compatiblecourses) == 0:
                        professorNotCompatCount += 1
                        break
                    # shuffle courses 
                    random.shuffle(compatiblecourses)
                    # find a course that the professor can teach and if the professor is able to teach
                    # check if professor has reached the limit
                    for course in compatiblecourses:
                        # check if the course overlaps with any existing professor courses in the quarter
                        for existingcourse in professor.teaching[quarter]:
                            if course.courseTimeOverlap(existingcourse):
                                continue
                        courseLevel = course.number/100
                        if courseLevel == 1:
                            if professor.classamount - allotment >= 0.5:
                                course.instructor = professor
                                professor.teaching[quarter].append(course)
                        else:
                            if professor.classamount - allotment >= 1.0:
                                course.instructor = professor
                                professor.teaching[quarter].append(course)
                        break
                    # break
        # At this point, remaining courses need to be populated with available part time instructors
        for professor in parttime:
            # TO DO
            break
            #shuffle professors
            random.shuffle(parttime)
            # iterate through professors
            remainingProfs = len(parttime)
            professorNotCompatCount = [0 for i in xrange(len(parttime))]
            i = -1
            while remainingProfs > 0:
                for professor in parttime:
                    i = (i + 1) % len(parttime)
                    # get the current course allotment of the professor
                    allotment = 0
                    for coursequarter in professor.teaching:
                        for course in professor.teaching[coursequarter]:
                            courseLevel = course.number/100
                            if courseLevel == 1:
                                allotment += 0.5
                            else:
                                allotment += 1.0
                    # if the professor can't teach anymore, break loop to the next professor
                    # Also check if the professor has gone through 4 loops without compatible courses
                    if allotment >= professor.classamount or professorNotCompatCount[i] >= 4:
                        remainingProfs -= 1
                        continue
                    # get only courses where professor has an expertise
                    compatiblecourses = [course for course in courses if course.expertise in professor.expertise and course.instructor == None]
                    if len(compatiblecourses) == 0:
                        professorNotCompatCount += 1
                        continue
                    # shuffle courses 
                    random.shuffle(compatiblecourses)
                    # find a course that the professor can teach and if the professor is able to teach
                    # check if professor has reached the limit
                    for course in compatiblecourses:
                        # check if the course overlaps with any existing professor courses in the quarter
                        for existingcourse in professor.teaching[quarter]:
                            if course.courseTimeOverlap(existingcourse):
                                continue
                        courseLevel = course.number/100
                        if courseLevel == 1:
                            if professor.classamount - allotment >= 0.5:
                                course.instructor = professor
                                professor.teaching[quarter].append(course)
                        else:
                            if professor.classamount - allotment >= 1.0:
                                course.instructor = professor
                                professor.teaching[quarter].append(course)
                        break
                        