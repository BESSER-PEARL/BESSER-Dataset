from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FSM_RootFolder:

    def __init__(self, name: str, RootFolder: "FSM_StateMachine" = None, FSM_RootFolder: "FSM_RootFolder" = None, FSM_RootFolder14: set["FSM_RootFolder"] = None, rootFolder: set["FSM_StateMachine"] = None):
        self.name = name
        self.RootFolder = RootFolder
        self.FSM_RootFolder = FSM_RootFolder
        self.FSM_RootFolder14 = FSM_RootFolder14 if FSM_RootFolder14 is not None else set()
        self.rootFolder = rootFolder if rootFolder is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RootFolder(self):
        return self.__RootFolder

    @RootFolder.setter
    def RootFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_RootFolder__RootFolder", None)
        self.__RootFolder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine"):
                opp_val = getattr(old_value, "stateMachine", None)
                if opp_val == self:
                    setattr(old_value, "stateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine"):
                opp_val = getattr(value, "stateMachine", None)
                setattr(value, "stateMachine", self)

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
                    

    @property
    def FSM_RootFolder14(self):
        return self.__FSM_RootFolder14

    @FSM_RootFolder14.setter
    def FSM_RootFolder14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_RootFolder__FSM_RootFolder14", None)
        self.__FSM_RootFolder14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSM_RootFolder"):
                    opp_val = getattr(item, "FSM_RootFolder", None)
                    
                    if opp_val == self:
                        setattr(item, "FSM_RootFolder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSM_RootFolder"):
                    opp_val = getattr(item, "FSM_RootFolder", None)
                    
                    setattr(item, "FSM_RootFolder", self)
                    

    @property
    def FSM_RootFolder(self):
        return self.__FSM_RootFolder

    @FSM_RootFolder.setter
    def FSM_RootFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FSM_RootFolder__FSM_RootFolder", None)
        self.__FSM_RootFolder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM_RootFolder14"):
                opp_val = getattr(old_value, "FSM_RootFolder14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM_RootFolder14"):
                opp_val = getattr(value, "FSM_RootFolder14", None)
                if opp_val is None:
                    setattr(value, "FSM_RootFolder14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FSM_AssociationStateState:

    pass
class MgaObject:

    pass
class FSM_StateMachine(MgaObject):

    pass
class FSM_State(MgaObject):

    pass
class FSM_Transition(MgaObject):

    pass
class FSM_MgaObject:

    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
