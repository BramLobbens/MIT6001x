# MIT 6.00.1x Final Exam Problem 5
# solution incomplete or incorrect

class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        super().__init__(name)
        self._status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        if self._status == None:
            raise ValueError
        return self._status