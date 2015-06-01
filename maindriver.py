__author__ = 'Christopher'
from CourseHistory import CourseHistory
from Schedule import Schedule
from Scheduler import Scheduler
import dataImport

<<<<<<< HEAD
##------------------------------------------------------------------------------
## The main driver for our scheduler program takes multiple steps to aggregate
## historical course data, load in current data, and work thorugh the current 
## data to create the best fit schedules for future years based on the historical
## data and estimations on how population will continue to grow going into the
## future.
##
## 1) Read in all historical course data.  Currently we read annual course data
## from 2010 - 2014. This is stored in a CourseHistory object called "history"
##
## 2) Print out the historical enrollment data for these years
##
## 3) Load the provided course data and professor data into lists of course and
## professor objects.
##
## 4) Copy the list of courses into a new annual schedule for 2015
##
## 5) Run the scheduler method for this schedule, assigning courses to professors
##
## 6) Print out the list of professors with their assigned courses. This includes
## adding new full or part time faculty based on if there is a high number of
## courses with the same expertise assigned that need to be enrolled
##
## 7) Print out the list of classes that did not get professors assigned. Also
## print out the number of unassigned courses
##
## 8) Loop for the next year.  As we move forward, more courses may be added as 
## the student population grows.  We attempt to keep occupancy at the same level
## it has been historically, so based on student growth, we add courses as the
## existing courses get filled.  When there are enough courses of a type that
## do not get professors assigned, we will look to hire more faculty to keep up.
##------------------------------------------------------------------------------

=======
"""
======================Time Schedule History======================
This section should be used to identify the files and the appropriate year\quarter to input historic data
Only TSV(Tab Delimited) Files are supported

TSV Format
Course Rows
1. Course number with CSS Prefix
2. Course Name
Course Instance Row (Every course should have one or more Course Instance Row)
1. Blank
2. SLN Number
3. Section Code
4. Credits
5. Days formatted as abbreviations(M,T,W,TH,F,S,SU) and are comma delimited if more than one day is identified
6. Time of the course in military(24H) formatted as Start-End
7. Location of the course to be taught
8. The instructor of the course
9. Enrollment information formatted as RegisteredStudents/StudentCapacity
"""
>>>>>>> cb785e408f5b149e53671a5b915073d2e11f7433
# Create Course History and read all data files
history = CourseHistory()
# read in year 2010
history.readCourses(".\\TimeSchedules\\2010-01-Fall-CSS.tsv", 2010, "autumn")
history.readCourses(".\\TimeSchedules\\2010-02-Spring-CSS.tsv", 2010, "spring")
history.readCourses(".\\TimeSchedules\\2010-03-Winter-CSS.tsv", 2010, "winter")
history.readCourses(".\\TimeSchedules\\2010-04-Summer-CSS.tsv", 2010, "summer")

# read in year 2011
history.readCourses(".\\TimeSchedules\\2011-01-Fall-CSS.tsv", 2011, "autumn")
history.readCourses(".\\TimeSchedules\\2011-02-Winter-CSS.tsv", 2011, "winter")
history.readCourses(".\\TimeSchedules\\2011-03-Spring-CSS.tsv", 2011, "spring")
history.readCourses(".\\TimeSchedules\\2011-04-Summer-CSS.tsv", 2011, "summer")

# read in year 2012
history.readCourses(".\\TimeSchedules\\2012-01-Fall-CSS.tsv", 2012, "autumn")
history.readCourses(".\\TimeSchedules\\2012-02-Winter-CSS.tsv", 2012, "winter")
history.readCourses(".\\TimeSchedules\\2012-03-Spring-CSS.tsv", 2012, "spring")
history.readCourses(".\\TimeSchedules\\2012-04-Summer-CSS.tsv", 2012, "summer")

# read in year 2013
history.readCourses(".\\TimeSchedules\\2013-01-Fall-CSS.tsv", 2013, "autumn")
history.readCourses(".\\TimeSchedules\\2013-02-Winter-CSS.tsv", 2013, "winter")
history.readCourses(".\\TimeSchedules\\2013-03-Spring-CSS.tsv", 2013, "spring")
history.readCourses(".\\TimeSchedules\\2013-04-Summer-CSS.tsv", 2013, "summer")

# read in year 2014
history.readCourses(".\\TimeSchedules\\2014-01-Fall-CSS.tsv", 2014, "autumn")
history.readCourses(".\\TimeSchedules\\2014-02-Winter-CSS.tsv", 2014, "winter")
history.readCourses(".\\TimeSchedules\\2014-03-Spring-CSS.tsv", 2014, "spring")
history.readCourses(".\\TimeSchedules\\2014-04-Summer-CSS.tsv", 2014, "summer")

# read in year 2015
# history.readCourses(".\\TimeSchedules\\2015-01-Fall-CSS.tsv", 2015, "autumn")
# history.readCourses(".\\TimeSchedules\\2015-02-Winter-CSS.tsv", 2015, "winter")
# history.readCourses(".\\TimeSchedules\\2015-03-Spring-CSS.tsv", 2015, "spring")

"""
This function updates the static set 10% yearly increase of enrollment to the average increase of all historic data
"""


# print out enrollment history values for each year
simYears = [2015, 2016, 2017, 2018, 2019, 2020]
# Create the given schedule to fill
givenSchedule = Schedule()

"""
Import of schedule to begin simulation
"""
importCourses = dataImport.importCourses()
for course in importCourses:
    givenSchedule.addCourse(course, course.quarter)
givenSchedule.sortQuarters()
importProfessors = dataImport.importFaculty()
scheduler = Scheduler(givenSchedule, importProfessors, history)
<<<<<<< HEAD
scheduler.randomScheduling(year=2015, iterations=250)

print "==============PROFESSORS AND COURSES=============="
for professor in scheduler.Professors:
    print professor

print "==============UNASSIGNED COURSES=============="
unassigned = givenSchedule.unassignedCourses()
for course in unassigned:
    print(course)

print len(unassigned)

print(scheduler.Schedule)

# Iterate For the next year
# print out enrollment history values for each year
enrollHistory = history.studentEnrollmentHistory()
print "==============COURSE HISTORY=============="
for year in enrollHistory:
    print year
    print "\tEnrolled: " + str(enrollHistory[year][0]) + "\tTotal Capacity: " + str(enrollHistory[year][1]) + "\t" + str(round(float(enrollHistory[year][0])/float(enrollHistory[year][1]) * 100, 1)) + "%"
=======
>>>>>>> cb785e408f5b149e53671a5b915073d2e11f7433


<<<<<<< HEAD
print "==============PROFESSORS AND COURSES=============="
for professor in scheduler.Professors:
    print professor

print "==============UNASSIGNED COURSES=============="
unassigned = givenSchedule.unassignedCourses()
for course in unassigned:
    print(course)

print len(unassigned)

print(scheduler.Schedule)

# Iterate For the next year
# print out enrollment history values for each year
enrollHistory = history.studentEnrollmentHistory()
print "==============COURSE HISTORY=============="
for year in enrollHistory:
    print year
    print "\tEnrolled: " + str(enrollHistory[year][0]) + "\tTotal Capacity: " + str(enrollHistory[year][1]) + "\t" + str(round(float(enrollHistory[year][0])/float(enrollHistory[year][1]) * 100, 1)) + "%"

history.updateAnnualIncrease()
scheduler.prepareNextYearSchedule()
scheduler.randomScheduling(year=2017, iterations=250)

print "==============PROFESSORS AND COURSES=============="
for professor in scheduler.Professors:
    print professor

print "==============UNASSIGNED COURSES=============="
unassigned = givenSchedule.unassignedCourses()
for course in unassigned:
    print(course)

print len(unassigned)

print(scheduler.Schedule)

# Iterate For the next year
# print out enrollment history values for each year
enrollHistory = history.studentEnrollmentHistory()
print "==============COURSE HISTORY=============="
for year in enrollHistory:
    print year
    print "\tEnrolled: " + str(enrollHistory[year][0]) + "\tTotal Capacity: " + str(enrollHistory[year][1]) + "\t" + str(round(float(enrollHistory[year][0])/float(enrollHistory[year][1]) * 100, 1)) + "%"
=======
for simYear in simYears:
    history.updateAnnualIncrease()
    print ""
    scheduler.randomScheduling(year=simYear, iterations=250)
    print "==========PROFESSORS AND COURSES=========="
    for professor in scheduler.Professors:
        print professor
    print "========END PROFESSORS AND COURSES========"
    print ""
    print "============UNASSIGNED COURSES============"
    unassigned = givenSchedule.unassignedCourses()
    for course in unassigned:
        print(course)
    print ""
    print "Number of unassigned Courses: " + str(len(unassigned))

    print "==============ANNUAL SCHEDULE============="
    print(scheduler.Schedule)
    # Prepare Schedule for next iteration
    enrollHistory = history.studentEnrollmentHistory()
    print "==============COURSE HISTORY=============="
    for year in enrollHistory:
        print year
        print "\tEnrolled: " + str(enrollHistory[year][0]) + "\tTotal Capacity: " + str(enrollHistory[year][1]) + "\t" + str(round(float(enrollHistory[year][0])/float(enrollHistory[year][1]) * 100, 1)) + "%"
    print "============END COURSE HISTORY============"
    scheduler.prepareNextYearSchedule()
>>>>>>> cb785e408f5b149e53671a5b915073d2e11f7433
