from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FSM_AssociationStateState:

    pass
class FSM_RootFolder:

    def __init__(self, name: str, FSM_RootFolder: set["RootFolder"] = None, rootFolder: set["StateMachine"] = None):
        self.name = name
        self.FSM_RootFolder = FSM_RootFolder if FSM_RootFolder is not None else set()
        self.rootFolder = rootFolder if rootFolder is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def FSM_RootFolder(self):
        return self.__FSM_RootFolder

    @FSM_RootFolder.setter
    def FSM_RootFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_RootFolder__FSM_RootFolder", None)
        self.__FSM_RootFolder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootFolder15"):
                    opp_val = getattr(item, "RootFolder15", None)
                    
                    if opp_val == self:
                        setattr(item, "RootFolder15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootFolder15"):
                    opp_val = getattr(item, "RootFolder15", None)
                    
                    setattr(item, "RootFolder15", self)
                    

    @property
    def rootFolder(self):
        return self.__rootFolder

    @rootFolder.setter
    def rootFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_RootFolder__rootFolder", None)
        self.__rootFolder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine17"):
                    opp_val = getattr(item, "StateMachine17", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine17"):
                    opp_val = getattr(item, "StateMachine17", None)
                    
                    setattr(item, "StateMachine17", self)
                    

class Transition:

    pass
class State:

    pass
class RootFolder:

    pass
class AssociationStateState:

    pass
class StateMachine:

    pass
class MgaObject:

    pass
class FSM_State(MgaObject):

    pass
class FSM_StateMachine(MgaObject):

    pass
class FSM_Transition(MgaObject):

    pass
class FSM_MgaObject:

    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

