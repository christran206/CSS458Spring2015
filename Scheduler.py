__author__ = 'Christopher'
import random
import copy
import sys

class Scheduler:
    QUARTERS = ["autumn", "spring", "winter", "summer"]

    def __init__(self, Schedule, Professors, CourseHistory):
        self.Schedule = Schedule
        self.Professors = Professors
        self.CourseHistory = CourseHistory
        self.OriginalSchedule = copy.deepcopy(Schedule)
        self.OriginalProfessors = copy.deepcopy(Professors)

    def randomScheduling(self, year, iterations=500):
        for i in range(iterations):
            self.fillschedule()
        for quarter in self.Schedule.courses:
            for course in self.Schedule.courses[quarter]:
                self.CourseHistory.addCourse(course, quarter, year)

    def fillschedule(self):
        """
        Takes the Schedule and Professors and fills the courses with professors if possible
        :return: None
        """
        tempSchedule = copy.deepcopy(self.OriginalSchedule)
        tempProfessors = copy.deepcopy(self.OriginalProfessors)

        # make lists of full-time and part time professors
        fulltime = [professor for professor in tempProfessors if professor.fullTime]
        parttime = [professor for professor in tempProfessors if not professor.fullTime]

        # Get enrollment for all courses
        for quarter in tempSchedule.courses:
            for course in tempSchedule.courses[quarter]:
                course.enrolled = self.CourseHistory.getCourseEnrollment(course.number, course.time, course.capacity, course.quarter)

        # shuffle professors
        random.shuffle(fulltime)
        # iterate through professors
        for professor in fulltime:
            # loop until professor is full of courses
            firstRun = True
            professorAvailable = True
            professorNotCompatCount = 0
            tempquarter = self.QUARTERS
            while professorAvailable:
                # Select one class from each quarter at a time
                if not firstRun:
                    random.shuffle(tempquarter)
                for quarter in tempquarter:
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
                    courses = tempSchedule.courses[quarter]
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
                        courseConflict = False
                        for existingcourse in professor.teaching[quarter]:
                            if course.courseTimeOverlap(existingcourse):
                                courseConflict = True
                                break
                        if courseConflict:
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
                firstRun = False
        # At this point, remaining courses need to be populated with available part time instructors
        # shuffle professors
        random.shuffle(parttime)

        for professor in parttime:
            # loop until professor is full of courses
            firstRun = True
            professorAvailable = True
            professorNotCompatCount = 0
            tempquarter = self.QUARTERS
            while professorAvailable:
                # Select one class from each quarter at a time
                if not firstRun:
                    random.shuffle(tempquarter)
                for quarter in tempquarter:
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
                    courses = tempSchedule.courses[quarter]
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
                        courseConflict = False
                        for existingcourse in professor.teaching[quarter]:
                            if course.courseTimeOverlap(existingcourse):
                                courseConflict = True
                                break
                        if courseConflict:
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
                firstRun = False
        if len(tempSchedule.unassignedCourses()) < len(self.Schedule.unassignedCourses()):
            self.Schedule.courses = tempSchedule.courses
            self.Professors = tempProfessors
