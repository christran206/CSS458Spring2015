__author__ = 'Christopher'
import random
import copy
import uuid
from course import Course
from professor import Professor


class Scheduler:
    
    """
    Scheduler class handles scheduling of professors to courses. 

    Is initialized by storing a given schedule, list of professors, and course history.
    Then stores two copies of the schedule and list of professors.  One as an original
    and one to manipulate. 
    
    Scheduler contains a predefined list of available quarters, and thresholds
    for when we need to hire new full time or part time staff.

    """
    QUARTERS = ["autumn", "winter", "spring", "summer"]
    NEEDNEWFULLSTAFF = 9
    NEEDNEWPARTSTAFF = 3

    def __init__(self, Schedule, Professors, CourseHistory):
        """
        Scheduler object is initialzied with a passed schedule, list of professors,
        course history.  Creates clones of the schedule and professors to store as well.
        
        """
        self.Schedule = Schedule
        self.Professors = Professors
        self.CourseHistory = CourseHistory
        self.OriginalSchedule = copy.deepcopy(Schedule)
        self.OriginalProfessors = copy.deepcopy(Professors)

    def randomScheduling(self, year, iterations=500):
        """
        Run the scheduling method we've created a selected number of times.
        Also adds the completed schedule data to the course history we track.
        """
        # Fill a schedule the passed number of iterations times
        for i in range(iterations):
            self.fillschedule()
        # For each course in each quarter, add the data to the course history
        for quarter in self.Schedule.courses:
            for course in self.Schedule.courses[quarter]:
                self.CourseHistory.addCourse(course, quarter, year)

    def fillschedule(self):
        """
        Takes the Schedule and Professors and fills the courses with professors if possible
        
        Based on class discussions, we assign all full time professors to courses
        first, then fill in remaining courses with the given part time professors. 
        
        To provide an element of randomness to which professors (full time and 
        part time) get to pick courses first, we shuffule the list of professors 
        before scheduling.  This means any professor in each of the full time and 
        part time lists has a chance of getting first pick or last pick during any
        iteration.
        
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
                course.enrolled = self.CourseHistory.getCourseEnrollment(course.number, course.time, course.capacity,
                                                                         course.quarter)

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
                            courseLevel = course.number / 100
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
                    compatiblecourses = [course for course in courses if
                                         course.expertise in professor.expertise and course.instructor == None]
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
                        courseLevel = course.number / 100
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
                            courseLevel = course.number / 100
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
                    compatiblecourses = [course for course in courses if
                                         course.expertise in professor.expertise and course.instructor == None]
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
                        courseLevel = course.number / 100
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

    def prepareNextYearSchedule(self, popuationIncreasePercent=0.05):
        """
        Clean up data and prepare list of courses, requirements for next year's schedule
        
        After completing a schedule, we look at the list of unassigned courses
        to determine the expertises that were left open.  This is used to determine
        if we need to hire more part time or full time professors by comparing
        how many of any expertise were left unfilled to the thresholds for each.
        
        We then determine if we need to add more courses to the next year's schedule
        by viewing occupancy of the current year (enrollment/capacity). If the occupancy 
        is above a threshold, we add courses at randomly selected days/times of the
        type of course that was considered full. The threshold is defined by the passed
        value of student growth.
        
        Lastly, we clean up data that was used to manipulate the schedule by clearing
        the courses a professor is assigned and adding the new list of courses
        to the schedule so we can run again.
        
        Inputs:
            *populationIncreasePercent: The expected growth of the CSS student 
            population for the next year.  Defaults to 5%
            
        Returns:
            None
        """
        self.Schedule = copy.deepcopy(self.Schedule)
        # Hire new professors based on the unassigned courses
        unassignedCourses = self.Schedule.unassignedCourses()
        neededExpertise = {}
        # collect the expertise and number of classes
        for course in unassignedCourses:
            if course.expertise not in neededExpertise:
                neededExpertise[course.expertise] = 1
            else:
                neededExpertise[course.expertise] += 1
        for expertise in neededExpertise:
            if neededExpertise[expertise] >= self.NEEDNEWFULLSTAFF:
                self.Professors.append(Professor(uuid.uuid1(), True, 6.0, 0, expertise))
            else:
                self.Professors.append(Professor(uuid.uuid1(), False, 3.0, 0, expertise))
        # Determine if there is a need for additional classes
        # Check every class, if the enrollment is at a threshold, add a class of the same number and\or level
        coursestoadd = {"autumn": [], "winter": [], "spring": [], "summer": []}
        for quarter in self.Schedule.courses:
            for course in self.Schedule.courses[quarter]:
                if course.number not in [newcourse.number for newcourse in coursestoadd[quarter]]:
                    if float(course.enrolled)/float(course.capacity) >= 1 - popuationIncreasePercent:
                        days = [["M", "W"], ["T", "TH"]]
                        capacity = [30, 45, 60]
                        random.shuffle(days)
                        random.shuffle(capacity)
                        coursestoadd[quarter].append(
                            Course(None, course.number, None, course.quarter, days[0], course.time,
                                   None, 0, capacity[0], course.expertise))

                    # Empty the schedule for the next iteration
                course.instructor = None
                course.enrolled = 0
        for professor in self.Professors:
            # empty the courses professor is teaching
            professor.teaching = {"autumn": [], "winter": [], "spring": [], "summer": []}
        # add the new courses to the schedule for next iteration
        for quarter in coursestoadd:
            for course in coursestoadd[quarter]:
                self.Schedule.addCourse(course, quarter)
                self.Schedule.sortQuarters()
        self.OriginalSchedule = copy.deepcopy(self.Schedule)
        self.OriginalProfessors = copy.deepcopy(self.Professors)
