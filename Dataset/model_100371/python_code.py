from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class HSM_AssociationDataStateBase:

    pass
class HSM_AssociationStateState:

    pass
class PrimitiveState:

    pass
class HSM_State(PrimitiveState):

    pass
class HSM_Init(PrimitiveState):

    pass
class HSM_StateDataRelation(PrimitiveState):

    def __init__(self, value: str, color: str, stateDataRelation: "OrState" = None, stateDataRelation47: "AssociationDataStateBase" = None):
        self.value = value
        self.color = color
        self.stateDataRelation = stateDataRelation
        self.stateDataRelation47 = stateDataRelation47
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def stateDataRelation47(self):
        return self.__stateDataRelation47

    @stateDataRelation47.setter
    def stateDataRelation47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateDataRelation__stateDataRelation47", None)
        self.__stateDataRelation47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssociationDataStateBase48"):
                opp_val = getattr(old_value, "AssociationDataStateBase48", None)
                if opp_val == self:
                    setattr(old_value, "AssociationDataStateBase48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssociationDataStateBase48"):
                opp_val = getattr(value, "AssociationDataStateBase48", None)
                setattr(value, "AssociationDataStateBase48", self)

    @property
    def stateDataRelation(self):
        return self.__stateDataRelation

    @stateDataRelation.setter
    def stateDataRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateDataRelation__stateDataRelation", None)
        self.__stateDataRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrState45"):
                opp_val = getattr(old_value, "OrState45", None)
                if opp_val == self:
                    setattr(old_value, "OrState45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrState45"):
                opp_val = getattr(value, "OrState45", None)
                setattr(value, "OrState45", self)

class Transition:

    pass
class StateDataRelation:

    pass
class AndState:

    pass
class RootFolder:

    pass
class HSM_RootFolder:

    def __init__(self, name: str, HSM_RootFolder: set["RootFolder"] = None, rootFolder: set["OrState"] = None):
        self.name = name
        self.HSM_RootFolder = HSM_RootFolder if HSM_RootFolder is not None else set()
        self.rootFolder = rootFolder if rootFolder is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def HSM_RootFolder(self):
        return self.__HSM_RootFolder

    @HSM_RootFolder.setter
    def HSM_RootFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_RootFolder__HSM_RootFolder", None)
        self.__HSM_RootFolder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RootFolder"):
                    opp_val = getattr(item, "RootFolder", None)
                    
                    if opp_val == self:
                        setattr(item, "RootFolder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RootFolder"):
                    opp_val = getattr(item, "RootFolder", None)
                    
                    setattr(item, "RootFolder", self)
                    

    @property
    def rootFolder(self):
        return self.__rootFolder

    @rootFolder.setter
    def rootFolder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_RootFolder__rootFolder", None)
        self.__rootFolder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrState18"):
                    opp_val = getattr(item, "OrState18", None)
                    
                    if opp_val == self:
                        setattr(item, "OrState18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrState18"):
                    opp_val = getattr(item, "OrState18", None)
                    
                    setattr(item, "OrState18", self)
                    

class Init:

    pass
class State:

    pass
class CompoundState:

    pass
class HSM_AndState(CompoundState):

    pass
class HSM_OrState(CompoundState):

    pass
class OrState:

    pass
class AssociationStateState:

    pass
class MgaObject:

    pass
class HSM_Transition(MgaObject):

    def __init__(self, action: str, isSync: str, guard: str, trigger: str, transition: "OrState" = None, transition14: "AssociationStateState" = None):
        self.action = action
        self.isSync = isSync
        self.guard = guard
        self.trigger = trigger
        self.transition = transition
        self.transition14 = transition14
        
        pass
    @property
    def guard(self):
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard


    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger


    @property
    def isSync(self):
        return self.__isSync

    @isSync.setter
    def isSync(self, isSync: str):
        self.__isSync = isSync


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def transition14(self):
        return self.__transition14

    @transition14.setter
    def transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__transition14", None)
        self.__transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssociationStateState15"):
                opp_val = getattr(old_value, "AssociationStateState15", None)
                if opp_val == self:
                    setattr(old_value, "AssociationStateState15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssociationStateState15"):
                opp_val = getattr(value, "AssociationStateState15", None)
                setattr(value, "AssociationStateState15", self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrState12"):
                opp_val = getattr(old_value, "OrState12", None)
                if opp_val == self:
                    setattr(old_value, "OrState12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrState12"):
                opp_val = getattr(value, "OrState12", None)
                setattr(value, "OrState12", self)

class HSM_StateDateRelation(MgaObject):

    def __init__(self, value: str, color: str):
        self.value = value
        self.color = color
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class HSM_StateBase(MgaObject):

    def __init__(self, defaultTransition: str, marked: str, srcTransition: set["AssociationStateState"] = None, stateBase: set["DataVar"] = None, stateBase5: "AssociationDataStateBase" = None, dstTransition: set["AssociationStateState"] = None):
        self.defaultTransition = defaultTransition
        self.marked = marked
        self.srcTransition = srcTransition if srcTransition is not None else set()
        self.stateBase = stateBase if stateBase is not None else set()
        self.stateBase5 = stateBase5
        self.dstTransition = dstTransition if dstTransition is not None else set()
        
        pass
    @property
    def defaultTransition(self):
        return self.__defaultTransition

    @defaultTransition.setter
    def defaultTransition(self, defaultTransition: str):
        self.__defaultTransition = defaultTransition


    @property
    def marked(self):
        return self.__marked

    @marked.setter
    def marked(self, marked: str):
        self.__marked = marked


    @property
    def stateBase5(self):
        return self.__stateBase5

    @stateBase5.setter
    def stateBase5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateBase__stateBase5", None)
        self.__stateBase5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssociationDataStateBase"):
                opp_val = getattr(old_value, "AssociationDataStateBase", None)
                if opp_val == self:
                    setattr(old_value, "AssociationDataStateBase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssociationDataStateBase"):
                opp_val = getattr(value, "AssociationDataStateBase", None)
                setattr(value, "AssociationDataStateBase", self)

    @property
    def stateBase(self):
        return self.__stateBase

    @stateBase.setter
    def stateBase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateBase__stateBase", None)
        self.__stateBase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataVar"):
                    opp_val = getattr(item, "DataVar", None)
                    
                    if opp_val == self:
                        setattr(item, "DataVar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataVar"):
                    opp_val = getattr(item, "DataVar", None)
                    
                    setattr(item, "DataVar", self)
                    

    @property
    def srcTransition(self):
        return self.__srcTransition

    @srcTransition.setter
    def srcTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateBase__srcTransition", None)
        self.__srcTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssociationStateState2"):
                    opp_val = getattr(item, "AssociationStateState2", None)
                    
                    if opp_val == self:
                        setattr(item, "AssociationStateState2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssociationStateState2"):
                    opp_val = getattr(item, "AssociationStateState2", None)
                    
                    setattr(item, "AssociationStateState2", self)
                    

    @property
    def dstTransition(self):
        return self.__dstTransition

    @dstTransition.setter
    def dstTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSM_StateBase__dstTransition", None)
        self.__dstTransition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssociationStateState"):
                    opp_val = getattr(item, "AssociationStateState", None)
                    
                    if opp_val == self:
                        setattr(item, "AssociationStateState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssociationStateState"):
                    opp_val = getattr(item, "AssociationStateState", None)
                    
                    setattr(item, "AssociationStateState", self)
                    

class StateBase:

    pass
class HSM_CompoundState(StateBase):

    pass
class HSM_PrimitiveState(StateBase):

    pass
class HSM_DataVar(MgaObject):

    pass
class AssociationDataStateBase:

    pass
class DataVar:

    pass
class HSM_MgaObject:

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

