from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class CoachBusWithEDataType_Employee:

    def __init__(self, id: int):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


class Employee:

    pass
class CoachBusWithEDataType_Manager(Employee):

    pass
class CoachBusWithEDataType_SecurityGuard(Employee):

    pass