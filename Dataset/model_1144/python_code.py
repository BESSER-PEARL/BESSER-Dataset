from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SrcCompositeState:

    pass
class jointPackage_HSM2FSM_SrcAbstractState(ABC):

    def __init__(self, name: str, 016: "SrcStateMachine" = None, 019: "SrcCompositeState" = None):
        self.name = name
        self.016 = 016
        self.019 = 019
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 019(self):
        return self.__019

    @019.setter
    def 019(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcAbstractState__019", None)
        self.__019 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#20"):
                opp_val = getattr(old_value, "#20", None)
                if opp_val == self:
                    setattr(old_value, "#20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#20"):
                opp_val = getattr(value, "#20", None)
                setattr(value, "#20", self)

    @property
    def 016(self):
        return self.__016

    @016.setter
    def 016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcAbstractState__016", None)
        self.__016 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#17"):
                opp_val = getattr(old_value, "#17", None)
                if opp_val == self:
                    setattr(old_value, "#17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#17"):
                opp_val = getattr(value, "#17", None)
                setattr(value, "#17", self)

class TrgCompositeState:

    pass
class jointPackage_HSM2FSM_TrgAbstractState(ABC):

    def __init__(self, name: str, 039: "TrgStateMachine" = None, 042: "TrgCompositeState" = None):
        self.name = name
        self.039 = 039
        self.042 = 042
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 042(self):
        return self.__042

    @042.setter
    def 042(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgAbstractState__042", None)
        self.__042 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#43"):
                opp_val = getattr(old_value, "#43", None)
                if opp_val == self:
                    setattr(old_value, "#43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#43"):
                opp_val = getattr(value, "#43", None)
                setattr(value, "#43", self)

    @property
    def 039(self):
        return self.__039

    @039.setter
    def 039(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgAbstractState__039", None)
        self.__039 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#40"):
                opp_val = getattr(old_value, "#40", None)
                if opp_val == self:
                    setattr(old_value, "#40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#40"):
                opp_val = getattr(value, "#40", None)
                setattr(value, "#40", self)

class jointPackage_HSM2FSM_TrgTransition:

    def __init__(self, label: str, 032: "TrgStateMachine" = None, jointPackage_HSM2FSM_TrgTransition: "TrgAbstractState" = None, jointPackage_HSM2FSM_TrgTransition36: "TrgAbstractState" = None):
        self.label = label
        self.032 = 032
        self.jointPackage_HSM2FSM_TrgTransition = jointPackage_HSM2FSM_TrgTransition
        self.jointPackage_HSM2FSM_TrgTransition36 = jointPackage_HSM2FSM_TrgTransition36
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def jointPackage_HSM2FSM_TrgTransition36(self):
        return self.__jointPackage_HSM2FSM_TrgTransition36

    @jointPackage_HSM2FSM_TrgTransition36.setter
    def jointPackage_HSM2FSM_TrgTransition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgTransition__jointPackage_HSM2FSM_TrgTransition36", None)
        self.__jointPackage_HSM2FSM_TrgTransition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgAbstractState37"):
                opp_val = getattr(old_value, "TrgAbstractState37", None)
                if opp_val == self:
                    setattr(old_value, "TrgAbstractState37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgAbstractState37"):
                opp_val = getattr(value, "TrgAbstractState37", None)
                setattr(value, "TrgAbstractState37", self)

    @property
    def 032(self):
        return self.__032

    @032.setter
    def 032(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgTransition__032", None)
        self.__032 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#33"):
                opp_val = getattr(old_value, "#33", None)
                if opp_val == self:
                    setattr(old_value, "#33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#33"):
                opp_val = getattr(value, "#33", None)
                setattr(value, "#33", self)

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
            if hasattr(old_value, "TrgAbstractState"):
                opp_val = getattr(old_value, "TrgAbstractState", None)
                if opp_val == self:
                    setattr(old_value, "TrgAbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgAbstractState"):
                opp_val = getattr(value, "TrgAbstractState", None)
                setattr(value, "TrgAbstractState", self)

class TrgAbstractState:

    pass
class jointPackage_HSM2FSM_TrgCompositeState(TrgAbstractState):

    pass
class jointPackage_HSM2FSM_TrgRegularState(TrgAbstractState):

    pass
class jointPackage_HSM2FSM_TrgInitialState(TrgAbstractState):

    pass
class TrgTransition:

    pass
class jointPackage_HSM2FSM_TrgStateMachine:

    def __init__(self, name: str, 026: set["TrgTransition"] = None, 029: set["TrgAbstractState"] = None):
        self.name = name
        self.026 = 026 if 026 is not None else set()
        self.029 = 029 if 029 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 029(self):
        return self.__029

    @029.setter
    def 029(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgStateMachine__029", None)
        self.__029 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#30"):
                    opp_val = getattr(item, "#30", None)
                    
                    if opp_val == self:
                        setattr(item, "#30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#30"):
                    opp_val = getattr(item, "#30", None)
                    
                    setattr(item, "#30", self)
                    

    @property
    def 026(self):
        return self.__026

    @026.setter
    def 026(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_TrgStateMachine__026", None)
        self.__026 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#27"):
                    opp_val = getattr(item, "#27", None)
                    
                    if opp_val == self:
                        setattr(item, "#27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#27"):
                    opp_val = getattr(item, "#27", None)
                    
                    setattr(item, "#27", self)
                    

class TrgStateMachine:

    pass
class jointPackage_HSM2FSM_TrgRoot:

    pass
class jointPackage_HSM2FSM_SrcTransition:

    def __init__(self, label: str, 09: "SrcStateMachine" = None, jointPackage_HSM2FSM_SrcTransition: "SrcAbstractState" = None, jointPackage_HSM2FSM_SrcTransition13: "SrcAbstractState" = None):
        self.label = label
        self.09 = 09
        self.jointPackage_HSM2FSM_SrcTransition = jointPackage_HSM2FSM_SrcTransition
        self.jointPackage_HSM2FSM_SrcTransition13 = jointPackage_HSM2FSM_SrcTransition13
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def 09(self):
        return self.__09

    @09.setter
    def 09(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcTransition__09", None)
        self.__09 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#10"):
                opp_val = getattr(old_value, "#10", None)
                if opp_val == self:
                    setattr(old_value, "#10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#10"):
                opp_val = getattr(value, "#10", None)
                setattr(value, "#10", self)

    @property
    def jointPackage_HSM2FSM_SrcTransition13(self):
        return self.__jointPackage_HSM2FSM_SrcTransition13

    @jointPackage_HSM2FSM_SrcTransition13.setter
    def jointPackage_HSM2FSM_SrcTransition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcTransition__jointPackage_HSM2FSM_SrcTransition13", None)
        self.__jointPackage_HSM2FSM_SrcTransition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcAbstractState14"):
                opp_val = getattr(old_value, "SrcAbstractState14", None)
                if opp_val == self:
                    setattr(old_value, "SrcAbstractState14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcAbstractState14"):
                opp_val = getattr(value, "SrcAbstractState14", None)
                setattr(value, "SrcAbstractState14", self)

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
            if hasattr(old_value, "SrcAbstractState"):
                opp_val = getattr(old_value, "SrcAbstractState", None)
                if opp_val == self:
                    setattr(old_value, "SrcAbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcAbstractState"):
                opp_val = getattr(value, "SrcAbstractState", None)
                setattr(value, "SrcAbstractState", self)

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

    def __init__(self, name: str, 0: set["SrcTransition"] = None, 06: set["SrcAbstractState"] = None):
        self.name = name
        self.0 = 0 if 0 is not None else set()
        self.06 = 06 if 06 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 06(self):
        return self.__06

    @06.setter
    def 06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcStateMachine__06", None)
        self.__06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    if opp_val == self:
                        setattr(item, "#7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    setattr(item, "#7", self)
                    

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_HSM2FSM_SrcStateMachine__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class SrcStateMachine:

    pass
class jointPackage_HSM2FSM_SrcRoot:

    pass
class TrgRoot:

    pass
class SrcRoot:

    pass
class jointPackage_HSM2FSM_JointMM:

    pass