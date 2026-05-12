from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Employee:

    pass
class CoachBusWithEDataType_Manager(Employee):

    pass
class CoachBusWithEDataType_SecurityGuard(Employee):

    pass
class CoachBusWithEDataType_Employee:

    def __init__(self, baseSalary: float):
        self.baseSalary = baseSalary
        
        pass
    @property
    def baseSalary(self):
        return self.__baseSalary

    @baseSalary.setter
    def baseSalary(self, baseSalary: float):
        self.__baseSalary = baseSalary

