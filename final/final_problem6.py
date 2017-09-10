# MIT 6.00.1x Final Exam Problem 6

class ArrogantProfessor(Professor): 
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff