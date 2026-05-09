from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hfsmReq_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class NamedElement:

    pass
class hfsmReq_Transition(NamedElement):

    pass
class hfsmReq_AbstractState(NamedElement):

    pass
class hfsmReq_Region(NamedElement):

    pass
class AbstractState:

    pass
class hfsmReq_State(AbstractState):

    pass