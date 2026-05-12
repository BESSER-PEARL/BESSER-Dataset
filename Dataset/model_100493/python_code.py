from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BehaviorKind(Enum):
    ACTIVITY = "ACTIVITY"
    STATE_MACHINE = "STATE_MACHINE"
    OPAQUE_BEHAVIOR = "OPAQUE_BEHAVIOR"


############################################
# Definition of Classes
############################################

class umlState_ExitRule:

    def __init__(self, kind: str, behaviorName: str, umlState_ExitRule: "umlState_StateRule" = None):
        self.kind = kind
        self.behaviorName = behaviorName
        self.umlState_ExitRule = umlState_ExitRule
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def behaviorName(self):
        return self.__behaviorName

    @behaviorName.setter
    def behaviorName(self, behaviorName: str):
        self.__behaviorName = behaviorName


    @property
    def umlState_ExitRule(self):
        return self.__umlState_ExitRule

    @umlState_ExitRule.setter
    def umlState_ExitRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlState_ExitRule__umlState_ExitRule", None)
        self.__umlState_ExitRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlState_StateRule6"):
                opp_val = getattr(old_value, "umlState_StateRule6", None)
                if opp_val == self:
                    setattr(old_value, "umlState_StateRule6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlState_StateRule6"):
                opp_val = getattr(value, "umlState_StateRule6", None)
                setattr(value, "umlState_StateRule6", self)

class umlState_Namespace:

    pass
class umlState_StateMachine:

    pass
class umlState_QualifiedName:

    pass
class umlState_DoRule:

    def __init__(self, kind: str, behaviorName: str, umlState_DoRule: "umlState_StateRule" = None):
        self.kind = kind
        self.behaviorName = behaviorName
        self.umlState_DoRule = umlState_DoRule
        
        pass
    @property
    def behaviorName(self):
        return self.__behaviorName

    @behaviorName.setter
    def behaviorName(self, behaviorName: str):
        self.__behaviorName = behaviorName


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def umlState_DoRule(self):
        return self.__umlState_DoRule

    @umlState_DoRule.setter
    def umlState_DoRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlState_DoRule__umlState_DoRule", None)
        self.__umlState_DoRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlState_StateRule4"):
                opp_val = getattr(old_value, "umlState_StateRule4", None)
                if opp_val == self:
                    setattr(old_value, "umlState_StateRule4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlState_StateRule4"):
                opp_val = getattr(value, "umlState_StateRule4", None)
                setattr(value, "umlState_StateRule4", self)

class umlState_EntryRule:

    def __init__(self, kind: str, behaviorName: str, umlState_EntryRule: "umlState_StateRule" = None):
        self.kind = kind
        self.behaviorName = behaviorName
        self.umlState_EntryRule = umlState_EntryRule
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def behaviorName(self):
        return self.__behaviorName

    @behaviorName.setter
    def behaviorName(self, behaviorName: str):
        self.__behaviorName = behaviorName


    @property
    def umlState_EntryRule(self):
        return self.__umlState_EntryRule

    @umlState_EntryRule.setter
    def umlState_EntryRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlState_EntryRule__umlState_EntryRule", None)
        self.__umlState_EntryRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlState_StateRule2"):
                opp_val = getattr(old_value, "umlState_StateRule2", None)
                if opp_val == self:
                    setattr(old_value, "umlState_StateRule2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlState_StateRule2"):
                opp_val = getattr(value, "umlState_StateRule2", None)
                setattr(value, "umlState_StateRule2", self)

class umlState_SubmachineRule:

    pass
class umlState_StateRule:

    def __init__(self, name: str, umlState_StateRule: "umlState_SubmachineRule" = None, umlState_StateRule2: "umlState_EntryRule" = None, umlState_StateRule4: "umlState_DoRule" = None, umlState_StateRule6: "umlState_ExitRule" = None):
        self.name = name
        self.umlState_StateRule = umlState_StateRule
        self.umlState_StateRule2 = umlState_StateRule2
        self.umlState_StateRule4 = umlState_StateRule4
        self.umlState_StateRule6 = umlState_StateRule6
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def umlState_StateRule6(self):
        return self.__umlState_StateRule6

    @umlState_StateRule6.setter
    def umlState_StateRule6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlState_StateRule__umlState_StateRule6", None)
        self.__umlState_StateRule6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlState_ExitRule"):
                opp_val = getattr(old_value, "umlState_ExitRule", None)
                if opp_val == self:
                    setattr(old_value, "umlState_ExitRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlState_ExitRule"):
                opp_val = getattr(value, "umlState_ExitRule", None)
                setattr(value, "umlState_ExitRule", self)

    @property
    def umlState_StateRule(self):
        return self.__umlState_StateRule

    @umlState_StateRule.setter
    def umlState_StateRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlState_StateRule__umlState_StateRule", None)
        self.__umlState_StateRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlState_SubmachineRule"):
                opp_val = getattr(old_value, "umlState_SubmachineRule", None)
                if opp_val == self:
                    setattr(old_value, "umlState_SubmachineRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlState_SubmachineRule"):
                opp_val = getattr(value, "umlState_SubmachineRule", None)
                setattr(value, "umlState_SubmachineRule", self)

    @property
    def umlState_StateRule2(self):
        return self.__umlState_StateRule2

    @umlState_StateRule2.setter
    def umlState_StateRule2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlState_StateRule__umlState_StateRule2", None)
        self.__umlState_StateRule2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlState_EntryRule"):
                opp_val = getattr(old_value, "umlState_EntryRule", None)
                if opp_val == self:
                    setattr(old_value, "umlState_EntryRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlState_EntryRule"):
                opp_val = getattr(value, "umlState_EntryRule", None)
                setattr(value, "umlState_EntryRule", self)

    @property
    def umlState_StateRule4(self):
        return self.__umlState_StateRule4

    @umlState_StateRule4.setter
    def umlState_StateRule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlState_StateRule__umlState_StateRule4", None)
        self.__umlState_StateRule4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlState_DoRule"):
                opp_val = getattr(old_value, "umlState_DoRule", None)
                if opp_val == self:
                    setattr(old_value, "umlState_DoRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlState_DoRule"):
                opp_val = getattr(value, "umlState_DoRule", None)
                setattr(value, "umlState_DoRule", self)
