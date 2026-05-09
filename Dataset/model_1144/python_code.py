from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TrgCompositeState:

    pass
class TrgTransition:

    pass
class jointPackage_HSM2FSM_TrgStateMachine:

    def __init__(self, name: str, stateMachine22: set["TrgTransition"] = None, stateMachine24: set["TrgAbstractState"] = None):
        self.name = name
        self.stateMachine22 = stateMachine22 if stateMachine22 is not None else set()
        self.stateMachine24 = stateMachine24 if stateMachine24 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def stateMachine24(self):
        return self.__stateMachine24

    @stateMachine24.setter
    def stateMachine24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgStateMachine__stateMachine24", None)
        self.__stateMachine24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgAbstractState"):
                    opp_val = getattr(item, "TrgAbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgAbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgAbstractState"):
                    opp_val = getattr(item, "TrgAbstractState", None)
                    
                    setattr(item, "TrgAbstractState", self)
                    

    @property
    def stateMachine22(self):
        return self.__stateMachine22

    @stateMachine22.setter
    def stateMachine22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgStateMachine__stateMachine22", None)
        self.__stateMachine22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgTransition"):
                    opp_val = getattr(item, "TrgTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgTransition"):
                    opp_val = getattr(item, "TrgTransition", None)
                    
                    setattr(item, "TrgTransition", self)
                    

class TrgStateMachine:

    pass
class jointPackage_HSM2FSM_TrgRoot:

    pass
class SrcCompositeState:

    pass
class jointPackage_HSM2FSM_SrcAbstractState(ABC):

    def __init__(self, name: str, states: "SrcStateMachine" = None, states17: "SrcCompositeState" = None):
        self.name = name
        self.states = states
        self.states17 = states17
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcAbstractState__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcStateMachine15"):
                opp_val = getattr(old_value, "SrcStateMachine15", None)
                if opp_val == self:
                    setattr(old_value, "SrcStateMachine15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcStateMachine15"):
                opp_val = getattr(value, "SrcStateMachine15", None)
                setattr(value, "SrcStateMachine15", self)

    @property
    def states17(self):
        return self.__states17

    @states17.setter
    def states17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcAbstractState__states17", None)
        self.__states17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcCompositeState"):
                opp_val = getattr(old_value, "SrcCompositeState", None)
                if opp_val == self:
                    setattr(old_value, "SrcCompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcCompositeState"):
                opp_val = getattr(value, "SrcCompositeState", None)
                setattr(value, "SrcCompositeState", self)

class jointPackage_HSM2FSM_SrcTransition:

    def __init__(self, label: str, transitions: "SrcStateMachine" = None, jointPackage_HSM2FSM_SrcTransition: "SrcAbstractState" = None, jointPackage_HSM2FSM_SrcTransition12: "SrcAbstractState" = None):
        self.label = label
        self.transitions = transitions
        self.jointPackage_HSM2FSM_SrcTransition = jointPackage_HSM2FSM_SrcTransition
        self.jointPackage_HSM2FSM_SrcTransition12 = jointPackage_HSM2FSM_SrcTransition12
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcTransition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcStateMachine8"):
                opp_val = getattr(old_value, "SrcStateMachine8", None)
                if opp_val == self:
                    setattr(old_value, "SrcStateMachine8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcStateMachine8"):
                opp_val = getattr(value, "SrcStateMachine8", None)
                setattr(value, "SrcStateMachine8", self)

    @property
    def jointPackage_HSM2FSM_SrcTransition(self):
        return self.__jointPackage_HSM2FSM_SrcTransition

    @jointPackage_HSM2FSM_SrcTransition.setter
    def jointPackage_HSM2FSM_SrcTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcTransition__jointPackage_HSM2FSM_SrcTransition", None)
        self.__jointPackage_HSM2FSM_SrcTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcAbstractState10"):
                opp_val = getattr(old_value, "SrcAbstractState10", None)
                if opp_val == self:
                    setattr(old_value, "SrcAbstractState10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcAbstractState10"):
                opp_val = getattr(value, "SrcAbstractState10", None)
                setattr(value, "SrcAbstractState10", self)

    @property
    def jointPackage_HSM2FSM_SrcTransition12(self):
        return self.__jointPackage_HSM2FSM_SrcTransition12

    @jointPackage_HSM2FSM_SrcTransition12.setter
    def jointPackage_HSM2FSM_SrcTransition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcTransition__jointPackage_HSM2FSM_SrcTransition12", None)
        self.__jointPackage_HSM2FSM_SrcTransition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcAbstractState13"):
                opp_val = getattr(old_value, "SrcAbstractState13", None)
                if opp_val == self:
                    setattr(old_value, "SrcAbstractState13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcAbstractState13"):
                opp_val = getattr(value, "SrcAbstractState13", None)
                setattr(value, "SrcAbstractState13", self)

class SrcAbstractState:

    pass
class jointPackage_HSM2FSM_SrcInitialState(SrcAbstractState):

    pass
class jointPackage_HSM2FSM_SrcRegularState(SrcAbstractState):

    pass
class jointPackage_HSM2FSM_SrcCompositeState(SrcAbstractState):

    pass
class SrcTransition:

    pass
class jointPackage_HSM2FSM_SrcStateMachine:

    def __init__(self, name: str, stateMachine: set["SrcTransition"] = None, stateMachine6: set["SrcAbstractState"] = None):
        self.name = name
        self.stateMachine = stateMachine if stateMachine is not None else set()
        self.stateMachine6 = stateMachine6 if stateMachine6 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def stateMachine6(self):
        return self.__stateMachine6

    @stateMachine6.setter
    def stateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcStateMachine__stateMachine6", None)
        self.__stateMachine6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcAbstractState"):
                    opp_val = getattr(item, "SrcAbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcAbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcAbstractState"):
                    opp_val = getattr(item, "SrcAbstractState", None)
                    
                    setattr(item, "SrcAbstractState", self)
                    

    @property
    def stateMachine(self):
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcStateMachine__stateMachine", None)
        self.__stateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcTransition"):
                    opp_val = getattr(item, "SrcTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcTransition"):
                    opp_val = getattr(item, "SrcTransition", None)
                    
                    setattr(item, "SrcTransition", self)
                    

class jointPackage_HSM2FSM_TrgAbstractState(ABC):

    def __init__(self, name: str, states34: "TrgStateMachine" = None, states37: "TrgCompositeState" = None):
        self.name = name
        self.states34 = states34
        self.states37 = states37
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def states37(self):
        return self.__states37

    @states37.setter
    def states37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgAbstractState__states37", None)
        self.__states37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgCompositeState"):
                opp_val = getattr(old_value, "TrgCompositeState", None)
                if opp_val == self:
                    setattr(old_value, "TrgCompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgCompositeState"):
                opp_val = getattr(value, "TrgCompositeState", None)
                setattr(value, "TrgCompositeState", self)

    @property
    def states34(self):
        return self.__states34

    @states34.setter
    def states34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgAbstractState__states34", None)
        self.__states34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgStateMachine35"):
                opp_val = getattr(old_value, "TrgStateMachine35", None)
                if opp_val == self:
                    setattr(old_value, "TrgStateMachine35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgStateMachine35"):
                opp_val = getattr(value, "TrgStateMachine35", None)
                setattr(value, "TrgStateMachine35", self)

class jointPackage_HSM2FSM_TrgTransition:

    def __init__(self, label: str, transitions26: "TrgStateMachine" = None, jointPackage_HSM2FSM_TrgTransition: "TrgAbstractState" = None, jointPackage_HSM2FSM_TrgTransition31: "TrgAbstractState" = None):
        self.label = label
        self.transitions26 = transitions26
        self.jointPackage_HSM2FSM_TrgTransition = jointPackage_HSM2FSM_TrgTransition
        self.jointPackage_HSM2FSM_TrgTransition31 = jointPackage_HSM2FSM_TrgTransition31
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def transitions26(self):
        return self.__transitions26

    @transitions26.setter
    def transitions26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgTransition__transitions26", None)
        self.__transitions26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgStateMachine27"):
                opp_val = getattr(old_value, "TrgStateMachine27", None)
                if opp_val == self:
                    setattr(old_value, "TrgStateMachine27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgStateMachine27"):
                opp_val = getattr(value, "TrgStateMachine27", None)
                setattr(value, "TrgStateMachine27", self)

    @property
    def jointPackage_HSM2FSM_TrgTransition31(self):
        return self.__jointPackage_HSM2FSM_TrgTransition31

    @jointPackage_HSM2FSM_TrgTransition31.setter
    def jointPackage_HSM2FSM_TrgTransition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgTransition__jointPackage_HSM2FSM_TrgTransition31", None)
        self.__jointPackage_HSM2FSM_TrgTransition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgAbstractState32"):
                opp_val = getattr(old_value, "TrgAbstractState32", None)
                if opp_val == self:
                    setattr(old_value, "TrgAbstractState32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgAbstractState32"):
                opp_val = getattr(value, "TrgAbstractState32", None)
                setattr(value, "TrgAbstractState32", self)

    @property
    def jointPackage_HSM2FSM_TrgTransition(self):
        return self.__jointPackage_HSM2FSM_TrgTransition

    @jointPackage_HSM2FSM_TrgTransition.setter
    def jointPackage_HSM2FSM_TrgTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgTransition__jointPackage_HSM2FSM_TrgTransition", None)
        self.__jointPackage_HSM2FSM_TrgTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgAbstractState29"):
                opp_val = getattr(old_value, "TrgAbstractState29", None)
                if opp_val == self:
                    setattr(old_value, "TrgAbstractState29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgAbstractState29"):
                opp_val = getattr(value, "TrgAbstractState29", None)
                setattr(value, "TrgAbstractState29", self)

class TrgAbstractState:

    pass
class jointPackage_HSM2FSM_TrgRegularState(TrgAbstractState):

    pass
class jointPackage_HSM2FSM_TrgInitialState(TrgAbstractState):

    pass
class jointPackage_HSM2FSM_TrgCompositeState(TrgAbstractState):

    pass
class jointPackage_HSM2FSM_JointMM:

    pass
class SrcStateMachine:

    pass
class jointPackage_HSM2FSM_SrcRoot:

    pass
class TrgRoot:

    pass
class SrcRoot:

    pass