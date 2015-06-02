__author__ = 'Christopher'
import numpy

from course import Course


class CourseHistory:
    """
    CourseHistory object stores historical data of UWB CSS courses for review.
    
    Terms: 
        Enrollment: The number of students enrolled in any course.
        Capacity: The maximum number of students that can be enrolled in a course
        Occupancy: Defined as enrollment/capacity.  Should be <100%
    """
    DEFAULT_ENROLLMENT = 0.80  # Default enrollment percentage for a new course


    def __init__(self):
        """
        New coursehistory is initialized by creating a dictionary of quarters, and 
        a yearly increase percentage value that represents the expected yearly increase
        in student population.
        """
        self.courseData = {'autumn': {}, 'winter': {}, 'spring': {}, 'summer': {}}
        self.yearlyIncrease = 0.10

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
                return numpy.random.binomial(courseCapacity, max(0, min(percent + self.yearlyIncrease, 1)))

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
                return numpy.random.binomial(courseCapacity, max(0, min(percent + self.yearlyIncrease, 1)))
            else:
                # This is a new course, return a default value
                return numpy.random.binomial(courseCapacity, self.DEFAULT_ENROLLMENT)

    def printData(self):
        """
        Prints the data contained within the course history object.
        
        Iterate through each quarter for each course number in this quarter,
        printing out the relevant information for the course
        
        Inputs: 
            None
        Return:
            None
        """
        # Print out entire course stored
        for quarter in self.courseData:
            print quarter
            for coursenum in self.courseData[quarter]:
                print str(coursenum)
                for year in self.courseData[quarter][coursenum]:
                    print "\t" + str(year)
                    for course in self.courseData[quarter][coursenum][year]:
                        print "\t\t" + str(course.sln) + "\t" + str(course.days) + "\t" + str(course.time) + "\t" + str(course.enrolled) + "/" + str(course.capacity)

    def studentEnrollmentHistory(self):
        """
        Calculate the enrollment, capacity, and occupancy for each quarter and year.
        
        Ignores the capstone defined courses, and creates a dictionary storing enrollment
        data for each year.  
        
        Occupancy is defined as enrollment / capacity
        
        Inputs:
            None
        Returns:
            A dictionary of years, each year storing the enrollment and capacity across
            all courses defined that year. 
        """
        # Ignore courses in this list (capstones, special topics)
        capstonecourses = [499, 498, 497, 198, 199, 600, 700]
        #Prepare return value
        enrollmentYears = {}
        #Iterate through each quarter
        for quarter in self.courseData:
            #Iterate through each course
            for coursenum in self.courseData[quarter]:
                #iterate through each year                
                for year in self.courseData[quarter][coursenum]:
                    for course in self.courseData[quarter][coursenum][year]:
                        #if we're reached the next year, start with values at 0
                        if year not in enrollmentYears:
                            enrollmentYears[year] = [0, 0]
                        # if a course to count, add the enrollment and capacity
                        if course.number not in capstonecourses:
                            enrollmentYears[year][0] += course.enrolled
                            enrollmentYears[year][1] += course.capacity
        # Return dictionary of all years enrollment data
        return enrollmentYears

    def updateAnnualIncrease(self):
        """
        Calculate the average annual change in student population based on 
        historical enrollment data.
        
        For each year in the historical enrollment data we calculate the average
        enrollment and capacity, and then compare with the previous year to 
        calculate the difference in population from year to year.  The list of
        yearly changes is stored in the CourseHistory object's yearlyIncrease list.
        
        Inputs: 
            None
        Returns: 
            None
        """

        #Run and store the annual enrollment data
        enrollmentData = self.studentEnrollmentHistory()
        
        #Initialize a list for average occupancy
        averages = []
        
        #for each year in historical, store the average occupancy in the average list
        for year in enrollmentData:
            averages.append(float(enrollmentData[year][0])/float(enrollmentData[year][1]))
        
        #Initialize a list for differences from year to year
        differences = []
        
        #For each pair of back to back years, calculate the difference in occupancy
        for i in range(len(averages) - 1):
            differences.append(averages[i + 1] - averages[i])
            
        #Store the difference data in the object's yearly increase data
        self.yearlyIncrease = float(sum(differences))/float(len(differences))

    def addCourse(self, Course, quarter, year):
        """
        Adds a course to the course history list given the quarter and year.
        
        Checks to see if the course already isnt in the quarter and year given, 
        then adds it to the list of historical course data.
        
        Inputs:
            *course: The course to attempt to add
            *quarter: which quarter is this course part of
            *year: which year is this course taking place
            
        Returns: 
            none
        """
        if Course.number not in self.courseData[quarter]:
            self.courseData[quarter][Course.number] = {year: []}
        if year not in self.courseData[quarter][Course.number]:
            self.courseData[quarter][Course.number][year] = []
        self.courseData[quarter][Course.number][year].append(Course)
