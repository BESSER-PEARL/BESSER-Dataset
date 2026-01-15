from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SuperClass:

    pass
class overloads_SubClass(SuperClass):

    def __init__(self):
        
    def overloaded(self, par: SuperClass) -> str:
        # TODO: Implement overloaded method
        pass

    def notOverloaded(self, par: SuperClass) -> str:
        # TODO: Implement notOverloaded method
        pass

class overloads_SuperClass:

    def __init__(self):
        
    def overloaded(self, par: str) -> str:
        # TODO: Implement overloaded method
        pass

    def notOverloaded(self, par: str) -> str:
        # TODO: Implement notOverloaded method
        pass
