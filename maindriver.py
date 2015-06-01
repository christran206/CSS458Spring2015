__author__ = 'Christopher'
from CourseHistory import CourseHistory
from Schedule import Schedule
from Scheduler import Scheduler
import dataImport

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

history.updateAnnualIncrease()

# print out enrollment history values for each year
enrollHistory = history.studentEnrollmentHistory()
print "==============COURSE HISTORY=============="
for year in enrollHistory:
    print year
    print "\tEnrolled: " + str(enrollHistory[year][0]) + "\tTotal Capacity: " + str(enrollHistory[year][1]) + "\t" + str(round(float(enrollHistory[year][0])/float(enrollHistory[year][1]) * 100, 1)) + "%"

# Create the given schedule to fill
givenSchedule = Schedule()

importCourses = dataImport.importCourses()
for course in importCourses:
    givenSchedule.addCourse(course, course.quarter)
givenSchedule.sortQuarters()

importProfessors = dataImport.importFaculty()

scheduler = Scheduler(givenSchedule, importProfessors, history)
scheduler.randomScheduling(year=2015, iterations=10)

print "==============PROFESSORS AND COURSES=============="
for professor in scheduler.Professors:
    print professor

print "==============UNASSIGNED COURSES=============="
unassigned = givenSchedule.unassignedCourses()
for course in unassigned:
    print(course)

print len(unassigned)

print(givenSchedule)
# Iterate For the next year
# print out enrollment history values for each year
enrollHistory = history.studentEnrollmentHistory()
print "==============COURSE HISTORY=============="
for year in enrollHistory:
    print year
    print "\tEnrolled: " + str(enrollHistory[year][0]) + "\tTotal Capacity: " + str(enrollHistory[year][1]) + "\t" + str(round(float(enrollHistory[year][0])/float(enrollHistory[year][1]) * 100, 1)) + "%"

history.updateAnnualIncrease()
scheduler.prepareNextYearSchedule()
scheduler.randomScheduling(year=2016, iterations=10)

print "==============PROFESSORS AND COURSES=============="
for professor in scheduler.Professors:
    print professor

print "==============UNASSIGNED COURSES=============="
unassigned = givenSchedule.unassignedCourses()
for course in unassigned:
    print(course)

print len(unassigned)

print(givenSchedule)
# Iterate For the next year
# print out enrollment history values for each year
enrollHistory = history.studentEnrollmentHistory()
print "==============COURSE HISTORY=============="
for year in enrollHistory:
    print year
    print "\tEnrolled: " + str(enrollHistory[year][0]) + "\tTotal Capacity: " + str(enrollHistory[year][1]) + "\t" + str(round(float(enrollHistory[year][0])/float(enrollHistory[year][1]) * 100, 1)) + "%"
