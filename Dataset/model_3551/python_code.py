from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class autocast_ConceptC:

    pass
class ConceptA:

    pass
class autocast_ConceptB(ConceptA):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class autocast_ConceptA:

    pass