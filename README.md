#UWB Staff and Course Scheduling Simulator
##Personnel
####Christopher Tran
#####CSSE Senior
IT career of 10 years while slowly progressing into software development. Experienced with Python, GitHub, and software design for this course. 
####Kevin Parker
#####CSSE Senior
Taken linear algebra and diff eq.  New to Python, minimal experience with GitHub. 
####Jason Dailey
#####CSSE Senior
Experience with C++/#, game development (Unity, mainly C#), and back-end web-coding (Javascript and PHP). 

#Introduction
This project is to create a Software Simulation that will model the staff and course requirements for the University of Washington Bothell. The model will be based on the projected needs of program course requirements, student enrollment changes, and staff availability. The simulation will create a recommended schedule matching of professors to classes, based on model parameters and specified assumptions.

#Assumptions
* Student Enrollment is on a steady increase year over year.
* New Staff members are able to fill roles teaching programming courses.
* New Staff members gain a specialization after three quarters that will be randomly selected, but needed specializations will have a higher probability of being selected.
* New courses can be added with a random probability.
* Existing Courses can be removed with a random probability.
* Core Curriculum Courses are predefined and do not change.
* Student course registration preferences are ignored due to the unlikely chance that a student will decline a course due to preference against taking a course
** Example: Elective selection has no desired courses, student will most likely take any elective available to maintain graduation schedule
* Professors will have two non-breaking hours designated for office hours outside of teaching

#Possible additional assumptions
* Existing staff can be removed with a random probability.
* Students are able to attend any scheduled class - AM or PM.
* Students are only able to attend 1 class per time period.
* Time periods are pre-defined.
* Core courses have prerequisites that students must meet to enroll in.
* Electives do not have prerequisites.
* All teachers can teach at any time period, but are limited in the number of classes they can teach.

#Deliverables
##Simulation Flow\Logic Chart
Flow Chart describing the program overview in addition to charts describing the logic of modules in the simulation.
##Simulation Code
Complete source code for the simulation developed in Python and commented using the standards of a Doc String.
##Simulation Results
Varied results based on varied inputs of the simulation such as course addition\reduction probability and enrollment\employment changes.
##GitHub Log
Export of GitHub commit history and export of visual commit history of each member
##Project presentation
Prepared presentation before the date of scheduling demonstration using supported presentation tools such as PowerPoint, Google Docs, etc.


#Technologies
##GitHub
A tool for version control and cooperative development
##PyCharm
Python IDE with an in depth debugging tool, package management, and integrated GitHub version control
##Anaconda
Python Package specifically designed for data processing and scientific computing

#Benchmarks
##Milestone 1 – May 20th, 2015
Flowchart diagrams of major software development portions and possibly outline of objects and their interactions. If available, prototype\pseudocode for each of the diagram models.
##Milestone 2 – May 27th, 2015
Functional Simulation code that will support major components of the simulation.
##Final Project – June 1st, 2015
Fully functional simulation code and all supporting components, including testing and documentation files.
