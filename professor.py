class Professor:
    
    """
    Professor class defines a professor object.
    
    Professors are defined from a given list of faculty, and include the 
    professor's name, if they are full time or not, the number of classes they 
    can teach annually, the number of students they can advise, and up to 3
    areas of expertise.
    """

    def __init__(self, name, fullTime, classes, students, exp1, exp2, exp3):
        self.name = name
        self.fullTime = fullTime
        self.classes = classes
        self.students = students
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        
    def __str__(self):
        return "Name: %s \tFullTime: %s \tClasses: %s \tStudents: %s \t\
        Expertise1: %s \tExpertise2: %s \tExpertise3: %s \n" %  (self.name, \
        self.fullTime, self.classes, self.students, self.exp1, self.exp2, \
        self.exp3)
        
    def __repr__(self):
        return "Name: %s \tFullTime: %s \tClasses: %s \tStudents: %s \t\
        Expertise1: %s \tExpertise2: %s \tExpertise3: %s \n" %  (self.name, \
        self.fullTime, self.classes, self.students, self.exp1, self.exp2, \
        self.exp3)