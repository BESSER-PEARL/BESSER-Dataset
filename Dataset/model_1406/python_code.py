from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SMACHStateOutcomes(Enum):
    succeeded = "succeeded"
    preempted = "preempted"
    aborted = "aborted"
class SMACHGoalTypes(Enum):
    static_goal = "static_goal"
    userdata_goal = "userdata_goal"


############################################
# Definition of Classes
############################################

class ActionClient:

    pass
class ServiceClient:

    pass
class SMACHState:

    pass
class smach_InitStraightState(SMACHState):

    pass
class smach_ServiceState(ServiceClient, SMACHState):

    pass
class smach_ActionState(SMACHState, ActionClient):

    pass
class smach_SMACHState:

    def __init__(self, goal: str, goal_type: str, remap_overwrite: str, smach_SMACHState9: "smach_SMACHTransition" = None, smach_SMACHState12: "smach_SMACHTransition" = None, smach_SMACHState: "smach_SMACHStateMachine" = None):
        self.goal = goal
        self.goal_type = goal_type
        self.remap_overwrite = remap_overwrite
        self.smach_SMACHState9 = smach_SMACHState9
        self.smach_SMACHState12 = smach_SMACHState12
        self.smach_SMACHState = smach_SMACHState
        
    @property
    def goal_type(self) -> str:
        return self.__goal_type

    @goal_type.setter
    def goal_type(self, goal_type: str):
        self.__goal_type = goal_type

    @property
    def goal(self) -> str:
        return self.__goal

    @goal.setter
    def goal(self, goal: str):
        self.__goal = goal

    @property
    def remap_overwrite(self) -> str:
        return self.__remap_overwrite

    @remap_overwrite.setter
    def remap_overwrite(self, remap_overwrite: str):
        self.__remap_overwrite = remap_overwrite

    @property
    def smach_SMACHState9(self):
        return self.__smach_SMACHState9

    @smach_SMACHState9.setter
    def smach_SMACHState9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHState__smach_SMACHState9", None)
        self.__smach_SMACHState9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smach_SMACHTransition8"):
                opp_val = getattr(old_value, "smach_SMACHTransition8", None)
                if opp_val == self:
                    setattr(old_value, "smach_SMACHTransition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smach_SMACHTransition8"):
                opp_val = getattr(value, "smach_SMACHTransition8", None)
                setattr(value, "smach_SMACHTransition8", self)

    @property
    def smach_SMACHState12(self):
        return self.__smach_SMACHState12

    @smach_SMACHState12.setter
    def smach_SMACHState12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHState__smach_SMACHState12", None)
        self.__smach_SMACHState12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smach_SMACHTransition11"):
                opp_val = getattr(old_value, "smach_SMACHTransition11", None)
                if opp_val == self:
                    setattr(old_value, "smach_SMACHTransition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smach_SMACHTransition11"):
                opp_val = getattr(value, "smach_SMACHTransition11", None)
                setattr(value, "smach_SMACHTransition11", self)

    @property
    def smach_SMACHState(self):
        return self.__smach_SMACHState

    @smach_SMACHState.setter
    def smach_SMACHState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHState__smach_SMACHState", None)
        self.__smach_SMACHState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smach_SMACHStateMachine"):
                opp_val = getattr(old_value, "smach_SMACHStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smach_SMACHStateMachine"):
                opp_val = getattr(value, "smach_SMACHStateMachine", None)
                if opp_val is None:
                    setattr(value, "smach_SMACHStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class smach_SMACHStateMachine(Node):

    def __init__(self, SkillInterface: bool, smach_SMACHStateMachine2: set["smach_SMACHTransition"] = None, smach_SMACHStateMachine4: set["smach_FinalState"] = None, smach_SMACHStateMachine6: set["smach_InitActionState"] = None, smach_SMACHStateMachine: set["smach_SMACHState"] = None):
        self.SkillInterface = SkillInterface
        self.smach_SMACHStateMachine2 = smach_SMACHStateMachine2 if smach_SMACHStateMachine2 is not None else set()
        self.smach_SMACHStateMachine4 = smach_SMACHStateMachine4 if smach_SMACHStateMachine4 is not None else set()
        self.smach_SMACHStateMachine6 = smach_SMACHStateMachine6 if smach_SMACHStateMachine6 is not None else set()
        self.smach_SMACHStateMachine = smach_SMACHStateMachine if smach_SMACHStateMachine is not None else set()
        
    @property
    def SkillInterface(self) -> bool:
        return self.__SkillInterface

    @SkillInterface.setter
    def SkillInterface(self, SkillInterface: bool):
        self.__SkillInterface = SkillInterface

    @property
    def smach_SMACHStateMachine(self):
        return self.__smach_SMACHStateMachine

    @smach_SMACHStateMachine.setter
    def smach_SMACHStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHStateMachine__smach_SMACHStateMachine", None)
        self.__smach_SMACHStateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smach_SMACHState"):
                    opp_val = getattr(item, "smach_SMACHState", None)
                    
                    if opp_val == self:
                        setattr(item, "smach_SMACHState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smach_SMACHState"):
                    opp_val = getattr(item, "smach_SMACHState", None)
                    
                    setattr(item, "smach_SMACHState", self)
                    

    @property
    def smach_SMACHStateMachine6(self):
        return self.__smach_SMACHStateMachine6

    @smach_SMACHStateMachine6.setter
    def smach_SMACHStateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHStateMachine__smach_SMACHStateMachine6", None)
        self.__smach_SMACHStateMachine6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smach_InitActionState"):
                    opp_val = getattr(item, "smach_InitActionState", None)
                    
                    if opp_val == self:
                        setattr(item, "smach_InitActionState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smach_InitActionState"):
                    opp_val = getattr(item, "smach_InitActionState", None)
                    
                    setattr(item, "smach_InitActionState", self)
                    

    @property
    def smach_SMACHStateMachine2(self):
        return self.__smach_SMACHStateMachine2

    @smach_SMACHStateMachine2.setter
    def smach_SMACHStateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHStateMachine__smach_SMACHStateMachine2", None)
        self.__smach_SMACHStateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smach_SMACHTransition"):
                    opp_val = getattr(item, "smach_SMACHTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "smach_SMACHTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smach_SMACHTransition"):
                    opp_val = getattr(item, "smach_SMACHTransition", None)
                    
                    setattr(item, "smach_SMACHTransition", self)
                    

    @property
    def smach_SMACHStateMachine4(self):
        return self.__smach_SMACHStateMachine4

    @smach_SMACHStateMachine4.setter
    def smach_SMACHStateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHStateMachine__smach_SMACHStateMachine4", None)
        self.__smach_SMACHStateMachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smach_FinalState"):
                    opp_val = getattr(item, "smach_FinalState", None)
                    
                    if opp_val == self:
                        setattr(item, "smach_FinalState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smach_FinalState"):
                    opp_val = getattr(item, "smach_FinalState", None)
                    
                    setattr(item, "smach_FinalState", self)
                    

class smach_InitActionState(SMACHState):

    pass
class smach_FinalState(SMACHState):

    def __init__(self, type: str, smach_FinalState: "smach_SMACHStateMachine" = None):
        self.type = type
        self.smach_FinalState = smach_FinalState
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def smach_FinalState(self):
        return self.__smach_FinalState

    @smach_FinalState.setter
    def smach_FinalState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_FinalState__smach_FinalState", None)
        self.__smach_FinalState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smach_SMACHStateMachine4"):
                opp_val = getattr(old_value, "smach_SMACHStateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smach_SMACHStateMachine4"):
                opp_val = getattr(value, "smach_SMACHStateMachine4", None)
                if opp_val is None:
                    setattr(value, "smach_SMACHStateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smach_SMACHTransition:

    def __init__(self, name: str, smach_SMACHTransition: "smach_SMACHStateMachine" = None, smach_SMACHTransition8: "smach_SMACHState" = None, smach_SMACHTransition11: "smach_SMACHState" = None):
        self.name = name
        self.smach_SMACHTransition = smach_SMACHTransition
        self.smach_SMACHTransition8 = smach_SMACHTransition8
        self.smach_SMACHTransition11 = smach_SMACHTransition11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smach_SMACHTransition11(self):
        return self.__smach_SMACHTransition11

    @smach_SMACHTransition11.setter
    def smach_SMACHTransition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHTransition__smach_SMACHTransition11", None)
        self.__smach_SMACHTransition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smach_SMACHState12"):
                opp_val = getattr(old_value, "smach_SMACHState12", None)
                if opp_val == self:
                    setattr(old_value, "smach_SMACHState12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smach_SMACHState12"):
                opp_val = getattr(value, "smach_SMACHState12", None)
                setattr(value, "smach_SMACHState12", self)

    @property
    def smach_SMACHTransition(self):
        return self.__smach_SMACHTransition

    @smach_SMACHTransition.setter
    def smach_SMACHTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHTransition__smach_SMACHTransition", None)
        self.__smach_SMACHTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smach_SMACHStateMachine2"):
                opp_val = getattr(old_value, "smach_SMACHStateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smach_SMACHStateMachine2"):
                opp_val = getattr(value, "smach_SMACHStateMachine2", None)
                if opp_val is None:
                    setattr(value, "smach_SMACHStateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smach_SMACHTransition8(self):
        return self.__smach_SMACHTransition8

    @smach_SMACHTransition8.setter
    def smach_SMACHTransition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smach_SMACHTransition__smach_SMACHTransition8", None)
        self.__smach_SMACHTransition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smach_SMACHState9"):
                opp_val = getattr(old_value, "smach_SMACHState9", None)
                if opp_val == self:
                    setattr(old_value, "smach_SMACHState9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smach_SMACHState9"):
                opp_val = getattr(value, "smach_SMACHState9", None)
                setattr(value, "smach_SMACHState9", self)
