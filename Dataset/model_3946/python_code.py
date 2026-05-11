from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Initial:

    pass
class PathExp_Initialtwo(Initial):

    pass
class PathExp_InitialOne(Initial):

    pass
class PathExp_NonReferencedClass:

    pass
class Transition:

    pass
class State:

    pass
class Element:

    pass
class PathExp_PathExp(Element):

    pass
class PathExp_Element:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PathExp_Internal(State):

    def __init__(self, attr: int, State: "PathExp_PathExp" = None, State9: "PathExp_Transition" = None, State11: "PathExp_Transition" = None):
        self.attr = attr
        
        pass
    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, attr: int):
        self.__attr = attr


class PathExp_Final(State):

    def __init__(self, bool_attr: bool, State: "PathExp_PathExp" = None, State9: "PathExp_Transition" = None, State11: "PathExp_Transition" = None):
        self.bool_attr = bool_attr
        
        pass
    @property
    def bool_attr(self):
        return self.__bool_attr

    @bool_attr.setter
    def bool_attr(self, bool_attr: bool):
        self.__bool_attr = bool_attr


class PathExp_Initial(State):

    def __init__(self, bool_attr: bool, State: "PathExp_PathExp" = None, State9: "PathExp_Transition" = None, State11: "PathExp_Transition" = None):
        self.bool_attr = bool_attr
        
        pass
    @property
    def bool_attr(self):
        return self.__bool_attr

    @bool_attr.setter
    def bool_attr(self, bool_attr: bool):
        self.__bool_attr = bool_attr


class PathExp_Transition(Element):

    pass
class PathExp:

    pass
class PathExp_State:

    pass