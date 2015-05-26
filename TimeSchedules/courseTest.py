__author__ = 'Christopher'

from CourseHistory import CourseHistory

courseManager = CourseHistory()

# read in year 2010
courseManager.readCourses("2010-01-Fall-CSS.tsv", 2010, "autumn")
courseManager.readCourses("2010-02-Spring-CSS.tsv", 2010, "spring")
courseManager.readCourses("2010-03-Winter-CSS.tsv", 2010, "winter")
courseManager.readCourses("2010-04-Summer-CSS.tsv", 2010, "summer")

# read in year 2011
courseManager.readCourses("2011-01-Fall-CSS.tsv", 2011, "autumn")
courseManager.readCourses("2011-02-Winter-CSS.tsv", 2011, "winter")
courseManager.readCourses("2011-03-Spring-CSS.tsv", 2011, "spring")
courseManager.readCourses("2011-04-Summer-CSS.tsv", 2011, "summer")

# read in year 2012
courseManager.readCourses("2012-01-Fall-CSS.tsv", 2012, "autumn")
courseManager.readCourses("2012-02-Winter-CSS.tsv", 2012, "winter")
courseManager.readCourses("2012-03-Spring-CSS.tsv", 2012, "spring")
courseManager.readCourses("2012-04-Summer-CSS.tsv", 2012, "summer")

# read in year 2013
courseManager.readCourses("2013-01-Fall-CSS.tsv", 2013, "autumn")
courseManager.readCourses("2013-02-Winter-CSS.tsv", 2013, "winter")
courseManager.readCourses("2013-03-Spring-CSS.tsv", 2013, "spring")
courseManager.readCourses("2013-04-Summer-CSS.tsv", 2013, "summer")

# read in year 2014
courseManager.readCourses("2014-01-Fall-CSS.tsv", 2014, "autumn")
courseManager.readCourses("2014-02-Winter-CSS.tsv", 2014, "winter")
courseManager.readCourses("2014-03-Spring-CSS.tsv", 2014, "spring")
courseManager.readCourses("2014-04-Summer-CSS.tsv", 2014, "summer")

# read in year 2015
courseManager.readCourses("2015-01-Fall-CSS.tsv", 2015, "autumn")
courseManager.readCourses("2015-02-Winter-CSS.tsv", 2015, "winter")
courseManager.readCourses("2015-03-Spring-CSS.tsv", 2015, "spring")


# courseManager.printData()

# Test with a time with no history
print courseManager.getCourseEnrollment(342, "1315-1515", 45, "autumn") # PASS
# Test with a time with significant history
print courseManager.getCourseEnrollment(342, "2000-2200", 45, "autumn")