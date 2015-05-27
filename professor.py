class Professor:
    
    """
    Professor class defines a professor object.
    
    Professors are defined from a given list of faculty, and include the 
    professor's name, if they are full time or not, the number of classes they 
    can teach annually, the number of students they can advise, and up to 3
    areas of expertise.
    """

    def __init__(self, name, fullTime, classamount, students, expertise):
        self.name = name
        self.fullTime = fullTime
        self.classamount = classamount
        self.courses = []
        self.students = students
        self.expertise = expertise.split("/")
        
    def __str__(self):
        return "Name: %s \tFullTime: %s \tClassAmount: %s \tStudents: %s \t\
        Expertise: %s \n" % (self.name, self.fullTime, self.classamount, self.students, self.expertise)
        
    def __repr__(self):
        return "Name: %s \tFullTime: %s \tClassAmount: %s \tStudents: %s \t\
        Expertise: %s \n" % (self.name,self.fullTime, self.classamount, self.students, self.expertise)