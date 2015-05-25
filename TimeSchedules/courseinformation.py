__author__ = 'Christopher'
from course import Course


courseHistory = {'autumn': {}, 'winter': {}, 'spring': {}, 'summer': {}}


def readCourses(filename, year, quarter):
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
                coursenum = courseandname[0][-3:]
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
                    courseEnrolled = courseinfo[7].split("/")[0]
                    courseCapacity = courseinfo[7].split("/")[1]
                    courseInstructor = courseinfo[6]
                    # create new course object
                    newCourse = Course(coursesln, coursenum, courseandname[1], quarter,
                                       courseDays, courseTime, courseInstructor, courseEnrolled, courseCapacity)
                    # if the quarter has the course, add to the existing list, otherwise append to list
                    if coursenum in courseHistory[quarter]:
                        # check if the year exists
                        if year not in courseHistory[quarter][coursenum]:
                            courseHistory[quarter][coursenum][year] = []
                        # add to list
                        courseHistory[quarter][coursenum][year].append(newCourse)
                    else:
                        # add year and course to result
                        courseHistory[quarter][coursenum] = {year: []}
                        courseHistory[quarter][coursenum][year].append(newCourse)
            # keep reading lines
            line = input.readline()
        else:
            break

# read in year 2010
readCourses("2010-01-Fall-CSS.tsv", 2010, "autumn")
readCourses("2010-02-Spring-CSS.tsv", 2010, "spring")
readCourses("2010-03-Winter-CSS.tsv", 2010, "winter")
readCourses("2010-04-Summer-CSS.tsv", 2010, "summer")

# read in year 2011
readCourses("2011-01-Fall-CSS.tsv", 2011, "autumn")
readCourses("2011-02-Winter-CSS.tsv", 2011, "winter")
readCourses("2011-03-Spring-CSS.tsv", 2011, "spring")
readCourses("2011-04-Summer-CSS.tsv", 2011, "summer")

# read in year 2012
readCourses("2012-01-Fall-CSS.tsv", 2012, "autumn")
readCourses("2012-02-Winter-CSS.tsv", 2012, "winter")
readCourses("2012-03-Spring-CSS.tsv", 2012, "spring")
readCourses("2012-04-Summer-CSS.tsv", 2012, "summer")

# read in year 2013
readCourses("2013-01-Fall-CSS.tsv", 2013, "autumn")
readCourses("2013-02-Winter-CSS.tsv", 2013, "winter")
readCourses("2013-03-Spring-CSS.tsv", 2013, "spring")
readCourses("2013-04-Summer-CSS.tsv", 2013, "summer")

# read in year 2014
readCourses("2014-01-Fall-CSS.tsv", 2014, "autumn")
readCourses("2014-02-Winter-CSS.tsv", 2014, "winter")
readCourses("2014-03-Spring-CSS.tsv", 2014, "spring")
readCourses("2014-04-Summer-CSS.tsv", 2014, "summer")

# read in year 2015
readCourses("2015-01-Fall-CSS.tsv", 2015, "autumn")
readCourses("2015-02-Winter-CSS.tsv", 2015, "winter")
readCourses("2015-03-Spring-CSS.tsv", 2015, "spring")
#readCourses("2015-04-Summer-CSS.tsv", 2015, "summer")

# Print out entire course stored
for quarter in courseHistory:
    print quarter
    for coursenum in courseHistory[quarter]:
        print str(coursenum)
        for year in courseHistory[quarter][coursenum]:
            print "\t" + str(year)
            for course in courseHistory[quarter][coursenum][year]:
                print "\t\t" + str(course.sln) + "\t" + str(course.days) + "\t" + str(course.time) + "\t" + str(course.enrolled) + "/" + str(course.capacity)