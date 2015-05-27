__author__ = 'Christopher'
import numpy

from Course import Course


class CourseHistory:
    DEFAULT_ENROLLMENT = 0.80 # Default enrollment percentage for a new course

    def __init__(self):
        self.courseData = {'autumn': {}, 'winter': {}, 'spring': {}, 'summer': {}}

    def readCourses(self, filename, year, quarter):
        """
        Reads Course data from a properly formatted file with course information from UWB Time Schedule

        Parses each SLN and stores necessary data
        :param filename: name of feile
        :param year: Year of the term
        :param quarter: name of quarter as a string (autumn, winter, spring, summer)
        :return: None
        """
        input = open(filename)
        # read a line from file
        line = input.readline()

        # Read lines until file is empty
        while True:
            # check if it's empty
            if line:
                # Check if line begins with CSS
                if line.startswith("CSS"):
                    # split course number and name
                    courseandname = line.split("\t")
                    # get course number
                    coursenum = int(courseandname[0][-3:])
                else:
                    # split course info by tabs
                    courseinfo = line.split("\t")
                    # get the course SLN to check for a valid course offering
                    coursesln = courseinfo[1].split(" ")[0]
                    # if it's a digit, then parse remaining formation
                    if coursesln.isdigit():
                        # Get data from course
                        courseDays = courseinfo[3].split(",")
                        courseTime = courseinfo[4]
                        courseEnrolled = int(courseinfo[7].split("/")[0])
                        courseCapacity = int(courseinfo[7].split("/")[1])
                        courseInstructor = courseinfo[6]
                        # create new course object
                        newCourse = Course(coursesln, coursenum, courseandname[1], quarter,
                                           courseDays, courseTime, courseInstructor, courseEnrolled, courseCapacity)
                        # if the quarter has the course, add to the existing list, otherwise append to list
                        if coursenum in self.courseData[quarter]:
                            # check if the year exists
                            if year not in self.courseData[quarter][coursenum]:
                                self.courseData[quarter][coursenum][year] = []
                            # add to list
                            self.courseData[quarter][coursenum][year].append(newCourse)
                        else:
                            # add year and course to result
                            self.courseData[quarter][coursenum] = {year: []}
                            self.courseData[quarter][coursenum][year].append(newCourse)
                # keep reading lines
                line = input.readline()
            else:
                break

    def getCourseEnrollment(self, courseNum, courseTime, courseCapacity, courseQuarter = "none"):
        """
        Returns a
        :param courseNum: Course Number
        :param courseCapacity: Number of students the class is allocated to take
        :param courseQuarter: Optional: Quarter of the term
        :return: A number with the indicated enrollment
        """

        # Check if a quarter has been identified , if not, all data from all quarters need to be parsed
        if courseQuarter != "none":
            # determine for specific quarter
            # determine if the course has been offered in the specific quarter before
            if courseNum not in self.courseData[courseQuarter]:
                # course was never offered in this quarter, recall the function without the quarter
                return self.getCourseEnrollment(courseNum, courseTime, courseCapacity)
            else:
                # get the course history
                targetCourses = self.courseData[courseQuarter][courseNum]
                # Check if any courses overlap in time
                overlappingCourses = []
                # parse each year
                for year in targetCourses:
                    # parse each course
                    for course in targetCourses[year]:
                        # if times overlap, add to the overlapping courses
                        if course.courseOverlap(courseTime):
                            # Need to remove all classes with zero enrollment from history check due to a class
                            # that is likely removed from officialschedule
                            if int(course.enrolled) != 0:
                                overlappingCourses.append(course)
                # if there are overlapping courses, determine the average of all courses
                enrollPercent = []
                if len(overlappingCourses) != 0:
                    # get the average enrollment percentage
                    for course in overlappingCourses:
                        enrollPercent.append(float(course.enrolled)/float(course.capacity))
                else:
                    # no overlapping courses, use all courses
                    for year in targetCourses:
                        for course in targetCourses[year]:
                            enrollPercent.append(float(course.enrolled)/float(course.capacity))
                # average the percentages
                percent = sum(enrollPercent)/float(len(enrollPercent))
                # return a discrete number using binomial random number
                return numpy.random.binomial(courseCapacity, percent)

        else:
            # Parse all data from all quarters
            allCourses = []
            enrollPercent = []
            # get all courses contained
            for quarter in self.courseData:
                # Check if the course was offered in the particular quarter
                if courseNum in self.courseData[quarter]:
                    # Add all courses into a list
                    for year in self.courseData[quarter][courseNum]:
                        for course in self.courseData[quarter][courseNum][year]:
                            allCourses.append(course)
            # check if any exist
            if len(allCourses) != 0:
                for course in allCourses:
                    enrollPercent.append(float(course.enrolled)/float(course.capacity))
                percent = sum(enrollPercent)/float(len(enrollPercent))
                return numpy.random.binomial(courseCapacity, percent)
            else:
                # This is a new course, return a default value
                return numpy.random.binomial(courseCapacity, self.DEFAULT_ENROLLMENT)

    def printData(self):
        # Print out entire course stored
        for quarter in self.courseData:
            print quarter
            for coursenum in self.courseData[quarter]:
                print str(coursenum)
                for year in self.courseData[quarter][coursenum]:
                    print "\t" + str(year)
                    for course in self.courseData[quarter][coursenum][year]:
                        print "\t\t" + str(course.sln) + "\t" + str(course.days) + "\t" + str(course.time) + "\t" + str(course.enrolled) + "/" + str(course.capacity)