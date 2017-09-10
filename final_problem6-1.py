# MIT 6.00.1x Final Exam Problem 6-1

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

print(e.say('the sky is blue'))
print(le.say('the sky is blue'))
print(le.lecture('the sky is blue'))
print(pe.say('the sky is blue'))
print(pe.lecture('the sky is blue'))
print('\n')
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))