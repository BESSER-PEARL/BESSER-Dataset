from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Initial:

    pass
class PathExp_InitialOne(Initial):

    pass
class PathExp_NonReferencedClass:

    pass
class PathExp_Initialtwo(Initial):

    pass
class PathExp:

    pass
class PathExp_State:

    pass
class Transition:

    pass
class State:

    pass
class PathExp_Initial(State):

    def __init__(self, bool_attr: bool, State: "PathExp_PathExp", #13: "PathExp_Transition", #10: "PathExp_Transition"):
        self.bool_attr = bool_attr
        
    @property
    def bool_attr(self) -> bool:
        return self.__bool_attr

    @bool_attr.setter
    def bool_attr(self, bool_attr: bool):
        self.__bool_attr = bool_attr

class PathExp_Internal(State):

    def __init__(self, attr: int, State: "PathExp_PathExp", #13: "PathExp_Transition", #10: "PathExp_Transition"):
        self.attr = attr
        
    @property
    def attr(self) -> int:
        return self.__attr

    @attr.setter
    def attr(self, attr: int):
        self.__attr = attr

class PathExp_Final(State):

    def __init__(self, bool_attr: bool, State: "PathExp_PathExp", #13: "PathExp_Transition", #10: "PathExp_Transition"):
        self.bool_attr = bool_attr
        
    @property
    def bool_attr(self) -> bool:
        return self.__bool_attr

    @bool_attr.setter
    def bool_attr(self, bool_attr: bool):
        self.__bool_attr = bool_attr

class Element:

    pass
class PathExp_Transition(Element):

    pass
class PathExp_PathExp(Element):

    pass
class PathExp_Element:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
