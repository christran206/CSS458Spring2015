class Professor:
    
    """
    Professor class defines a professor object.
    
    Professors are defined from a given list of faculty, and include the 
    professor's name, if they are full time or not, the number of classes they 
    can teach annually, the number of students they can advise, and up to 3
    areas of expertise.
    """

    def __init__(self, name, fullTime, classamount, students, expertise):
        """
        Professor object is initialized by assigning passed values
        
        Inputs:
            *name: Professors name
            *fullTime: is the professor full time or not?
            *classamount: The number of classes the professor can teach annually
            *students: The number of students the teacher can advise (capstones)
            *expertise: List of up to 3 expertises the professor can teach
        
        Returns:
            A new professor object with above defined data
        """
        self.name = name
        self.fullTime = fullTime
        self.classamount = classamount
        self.teaching = {"autumn": [], "winter": [], "spring": [], "summer": []}
        self.students = students
        self.expertise = expertise.split("/")
        
    def __str__(self):
        """
        String output method for professor object.
        
        Professor is displayed by listing their name, status, courses they can teach,
        number of students they can advise, and list of expertises
             
        """
        return "Name: %s \tFullTime: %s \tClassAmount: %s \tStudents: %s \tExpertise: %s\n" \
               "%s" % \
               (self.name, self.fullTime, self.classamount, self.students, self.expertise, self.coursesteaching())
        
    def __repr__(self):
        """
        String representation method for professor object.  Matches string output
        
        Professor is displayed by listing their name, status, courses they can teach,
        number of students they can advise, and list of expertises        
        """
        return "Name: %s \tFullTime: %s \tClassAmount: %s \tStudents: %s \tExpertise: %s\n" \
               "%s" % \
               (self.name, self.fullTime, self.classamount, self.students, self.expertise, self.coursesteaching())

    def coursesteaching(self):
        """
        Returns a string of courses that a selected professor is listed as teching.
        
        Method iterates through each quarter and appends each course a given
        professor is teaching to a string that is returned.
        
        inputs:
            None
        
        Return:
            string listing of courses this professor is assigned
        """
        
        result = ""
        for quarter in self.teaching:
            result += "=" + quarter + "\n"
            for course in self.teaching[quarter]:
                result += str(course) + "\n"
        return result
