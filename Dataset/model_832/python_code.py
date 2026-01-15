from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Guard:

    pass
class tfsmextended_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class tfsmextended_EventGuard(Guard):

    pass
class tfsmextended_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, tfsmextended_TemporalGuard: "tfsmextended_FSMClock" = None):
        self.afterDuration = afterDuration
        self.tfsmextended_TemporalGuard = tfsmextended_TemporalGuard
        
    @property
    def afterDuration(self) -> int:
        return self.__afterDuration

    @afterDuration.setter
    def afterDuration(self, afterDuration: int):
        self.__afterDuration = afterDuration

    @property
    def tfsmextended_TemporalGuard(self):
        return self.__tfsmextended_TemporalGuard

    @tfsmextended_TemporalGuard.setter
    def tfsmextended_TemporalGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TemporalGuard__tfsmextended_TemporalGuard", None)
        self.__tfsmextended_TemporalGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_FSMClock33"):
                opp_val = getattr(old_value, "tfsmextended_FSMClock33", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_FSMClock33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_FSMClock33"):
                opp_val = getattr(value, "tfsmextended_FSMClock33", None)
                setattr(value, "tfsmextended_FSMClock33", self)

class tfsmextended_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class tfsmextended_Guard(NamedElement):

    pass
class tfsmextended_TimedSystem(NamedElement):

    pass
class tfsmextended_State(NamedElement):

    def __init__(self, tfsmextended_State: "tfsmextended_TFSM" = None, tfsmextended_State11: "tfsmextended_TFSM" = None, 1: "tfsmextended_TFSM" = None, 13: "tfsmextended_TFSM" = None, 16: set["tfsmextended_Transition"] = None, 19: set["tfsmextended_Transition"] = None, 23: "tfsmextended_Transition" = None, 26: "tfsmextended_Transition" = None):
        self.tfsmextended_State = tfsmextended_State
        self.tfsmextended_State11 = tfsmextended_State11
        self.1 = 1
        self.13 = 13
        self.16 = 16 if 16 is not None else set()
        self.19 = 19 if 19 is not None else set()
        self.23 = 23
        self.26 = 26
        
    @property
    def tfsmextended_State(self):
        return self.__tfsmextended_State

    @tfsmextended_State.setter
    def tfsmextended_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__tfsmextended_State", None)
        self.__tfsmextended_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM"):
                opp_val = getattr(old_value, "tfsmextended_TFSM", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM"):
                opp_val = getattr(value, "tfsmextended_TFSM", None)
                setattr(value, "tfsmextended_TFSM", self)

    @property
    def 23(self):
        return self.__23

    @23.setter
    def 23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__23", None)
        self.__23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "22"):
                opp_val = getattr(old_value, "22", None)
                if opp_val == self:
                    setattr(old_value, "22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "22"):
                opp_val = getattr(value, "22", None)
                setattr(value, "22", self)

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__16", None)
        self.__16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    if opp_val == self:
                        setattr(item, "17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "17"):
                    opp_val = getattr(item, "17", None)
                    
                    setattr(item, "17", self)
                    

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__19", None)
        self.__19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    if opp_val == self:
                        setattr(item, "20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    setattr(item, "20", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_State11(self):
        return self.__tfsmextended_State11

    @tfsmextended_State11.setter
    def tfsmextended_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__tfsmextended_State11", None)
        self.__tfsmextended_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM10"):
                opp_val = getattr(old_value, "tfsmextended_TFSM10", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TFSM10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM10"):
                opp_val = getattr(value, "tfsmextended_TFSM10", None)
                setattr(value, "tfsmextended_TFSM10", self)

    @property
    def 26(self):
        return self.__26

    @26.setter
    def 26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__26", None)
        self.__26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "25"):
                opp_val = getattr(old_value, "25", None)
                if opp_val == self:
                    setattr(old_value, "25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "25"):
                opp_val = getattr(value, "25", None)
                setattr(value, "25", self)

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if opp_val == self:
                    setattr(old_value, "14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                setattr(value, "14", self)

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

    def onLeave(self):
        # TODO: Implement onLeave method
        pass

class tfsmextended_TFSM(NamedElement):

    def __init__(self, : set["tfsmextended_State"] = None, tfsmextended_TFSM: "tfsmextended_State" = None, tfsmextended_TFSM4: set["tfsmextended_FSMEvent"] = None, tfsmextended_TFSM6: "tfsmextended_FSMClock" = None, tfsmextended_TFSM8: set["tfsmextended_Transition"] = None, tfsmextended_TFSM10: "tfsmextended_State" = None, 14: "tfsmextended_State" = None, tfsmextended_TFSM40: "tfsmextended_TimedSystem" = None):
        self. =  if  is not None else set()
        self.tfsmextended_TFSM = tfsmextended_TFSM
        self.tfsmextended_TFSM4 = tfsmextended_TFSM4 if tfsmextended_TFSM4 is not None else set()
        self.tfsmextended_TFSM6 = tfsmextended_TFSM6
        self.tfsmextended_TFSM8 = tfsmextended_TFSM8 if tfsmextended_TFSM8 is not None else set()
        self.tfsmextended_TFSM10 = tfsmextended_TFSM10
        self.14 = 14
        self.tfsmextended_TFSM40 = tfsmextended_TFSM40
        
    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

    @property
    def tfsmextended_TFSM8(self):
        return self.__tfsmextended_TFSM8

    @tfsmextended_TFSM8.setter
    def tfsmextended_TFSM8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM8", None)
        self.__tfsmextended_TFSM8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_Transition"):
                    opp_val = getattr(item, "tfsmextended_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_Transition"):
                    opp_val = getattr(item, "tfsmextended_Transition", None)
                    
                    setattr(item, "tfsmextended_Transition", self)
                    

    @property
    def tfsmextended_TFSM10(self):
        return self.__tfsmextended_TFSM10

    @tfsmextended_TFSM10.setter
    def tfsmextended_TFSM10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM10", None)
        self.__tfsmextended_TFSM10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_State11"):
                opp_val = getattr(old_value, "tfsmextended_State11", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_State11"):
                opp_val = getattr(value, "tfsmextended_State11", None)
                setattr(value, "tfsmextended_State11", self)

    @property
    def tfsmextended_TFSM(self):
        return self.__tfsmextended_TFSM

    @tfsmextended_TFSM.setter
    def tfsmextended_TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM", None)
        self.__tfsmextended_TFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_State"):
                opp_val = getattr(old_value, "tfsmextended_State", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_State"):
                opp_val = getattr(value, "tfsmextended_State", None)
                setattr(value, "tfsmextended_State", self)

    @property
    def tfsmextended_TFSM4(self):
        return self.__tfsmextended_TFSM4

    @tfsmextended_TFSM4.setter
    def tfsmextended_TFSM4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM4", None)
        self.__tfsmextended_TFSM4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_FSMEvent"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_FSMEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_FSMEvent"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent", None)
                    
                    setattr(item, "tfsmextended_FSMEvent", self)
                    

    @property
    def tfsmextended_TFSM6(self):
        return self.__tfsmextended_TFSM6

    @tfsmextended_TFSM6.setter
    def tfsmextended_TFSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM6", None)
        self.__tfsmextended_TFSM6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_FSMClock"):
                opp_val = getattr(old_value, "tfsmextended_FSMClock", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_FSMClock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_FSMClock"):
                opp_val = getattr(value, "tfsmextended_FSMClock", None)
                setattr(value, "tfsmextended_FSMClock", self)

    @property
    def tfsmextended_TFSM40(self):
        return self.__tfsmextended_TFSM40

    @tfsmextended_TFSM40.setter
    def tfsmextended_TFSM40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM40", None)
        self.__tfsmextended_TFSM40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TimedSystem"):
                opp_val = getattr(old_value, "tfsmextended_TimedSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TimedSystem"):
                opp_val = getattr(value, "tfsmextended_TimedSystem", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TimedSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

    def init(self):
        # TODO: Implement init method
        pass

class tfsmextended_Transition(NamedElement):

    def __init__(self, action: str, tfsmextended_Transition: "tfsmextended_TFSM" = None, tfsmextended_Transition28: "tfsmextended_Guard" = None, tfsmextended_Transition30: set["tfsmextended_FSMEvent"] = None, 17: "tfsmextended_State" = None, 20: "tfsmextended_State" = None, 22: "tfsmextended_State" = None, 25: "tfsmextended_State" = None, tfsmextended_Transition38: "tfsmextended_FSMEvent" = None):
        self.action = action
        self.tfsmextended_Transition = tfsmextended_Transition
        self.tfsmextended_Transition28 = tfsmextended_Transition28
        self.tfsmextended_Transition30 = tfsmextended_Transition30 if tfsmextended_Transition30 is not None else set()
        self.17 = 17
        self.20 = 20
        self.22 = 22
        self.25 = 25
        self.tfsmextended_Transition38 = tfsmextended_Transition38
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                if opp_val is None:
                    setattr(value, "16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_Transition38(self):
        return self.__tfsmextended_Transition38

    @tfsmextended_Transition38.setter
    def tfsmextended_Transition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition38", None)
        self.__tfsmextended_Transition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_FSMEvent37"):
                opp_val = getattr(old_value, "tfsmextended_FSMEvent37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_FSMEvent37"):
                opp_val = getattr(value, "tfsmextended_FSMEvent37", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_FSMEvent37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_Transition(self):
        return self.__tfsmextended_Transition

    @tfsmextended_Transition.setter
    def tfsmextended_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition", None)
        self.__tfsmextended_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM8"):
                opp_val = getattr(old_value, "tfsmextended_TFSM8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM8"):
                opp_val = getattr(value, "tfsmextended_TFSM8", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TFSM8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__22", None)
        self.__22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "23"):
                opp_val = getattr(old_value, "23", None)
                if opp_val == self:
                    setattr(old_value, "23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "23"):
                opp_val = getattr(value, "23", None)
                setattr(value, "23", self)

    @property
    def 25(self):
        return self.__25

    @25.setter
    def 25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__25", None)
        self.__25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "26"):
                opp_val = getattr(old_value, "26", None)
                if opp_val == self:
                    setattr(old_value, "26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "26"):
                opp_val = getattr(value, "26", None)
                setattr(value, "26", self)

    @property
    def tfsmextended_Transition30(self):
        return self.__tfsmextended_Transition30

    @tfsmextended_Transition30.setter
    def tfsmextended_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition30", None)
        self.__tfsmextended_Transition30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_FSMEvent31"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent31", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_FSMEvent31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_FSMEvent31"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent31", None)
                    
                    setattr(item, "tfsmextended_FSMEvent31", self)
                    

    @property
    def tfsmextended_Transition28(self):
        return self.__tfsmextended_Transition28

    @tfsmextended_Transition28.setter
    def tfsmextended_Transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition28", None)
        self.__tfsmextended_Transition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_Guard"):
                opp_val = getattr(old_value, "tfsmextended_Guard", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_Guard"):
                opp_val = getattr(value, "tfsmextended_Guard", None)
                setattr(value, "tfsmextended_Guard", self)

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "19"):
                opp_val = getattr(old_value, "19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "19"):
                opp_val = getattr(value, "19", None)
                if opp_val is None:
                    setattr(value, "19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fire(self):
        # TODO: Implement fire method
        pass

class tfsmextended_FSMClock(NamedElement):

    def __init__(self, numberOfTicks: str, tfsmextended_FSMClock: "tfsmextended_TFSM" = None, tfsmextended_FSMClock43: "tfsmextended_TimedSystem" = None, tfsmextended_FSMClock33: "tfsmextended_TemporalGuard" = None):
        self.numberOfTicks = numberOfTicks
        self.tfsmextended_FSMClock = tfsmextended_FSMClock
        self.tfsmextended_FSMClock43 = tfsmextended_FSMClock43
        self.tfsmextended_FSMClock33 = tfsmextended_FSMClock33
        
    @property
    def numberOfTicks(self) -> str:
        return self.__numberOfTicks

    @numberOfTicks.setter
    def numberOfTicks(self, numberOfTicks: str):
        self.__numberOfTicks = numberOfTicks

    @property
    def tfsmextended_FSMClock43(self):
        return self.__tfsmextended_FSMClock43

    @tfsmextended_FSMClock43.setter
    def tfsmextended_FSMClock43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMClock__tfsmextended_FSMClock43", None)
        self.__tfsmextended_FSMClock43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TimedSystem42"):
                opp_val = getattr(old_value, "tfsmextended_TimedSystem42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TimedSystem42"):
                opp_val = getattr(value, "tfsmextended_TimedSystem42", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TimedSystem42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_FSMClock(self):
        return self.__tfsmextended_FSMClock

    @tfsmextended_FSMClock.setter
    def tfsmextended_FSMClock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMClock__tfsmextended_FSMClock", None)
        self.__tfsmextended_FSMClock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM6"):
                opp_val = getattr(old_value, "tfsmextended_TFSM6", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TFSM6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM6"):
                opp_val = getattr(value, "tfsmextended_TFSM6", None)
                setattr(value, "tfsmextended_TFSM6", self)

    @property
    def tfsmextended_FSMClock33(self):
        return self.__tfsmextended_FSMClock33

    @tfsmextended_FSMClock33.setter
    def tfsmextended_FSMClock33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMClock__tfsmextended_FSMClock33", None)
        self.__tfsmextended_FSMClock33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TemporalGuard"):
                opp_val = getattr(old_value, "tfsmextended_TemporalGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TemporalGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TemporalGuard"):
                opp_val = getattr(value, "tfsmextended_TemporalGuard", None)
                setattr(value, "tfsmextended_TemporalGuard", self)

    def ticks(self):
        # TODO: Implement ticks method
        pass

class tfsmextended_FSMEvent(NamedElement):

    def __init__(self, isTriggered: str, tfsmextended_FSMEvent: "tfsmextended_TFSM" = None, tfsmextended_FSMEvent31: "tfsmextended_Transition" = None, tfsmextended_FSMEvent46: "tfsmextended_TimedSystem" = None, tfsmextended_FSMEvent35: "tfsmextended_EventGuard" = None, tfsmextended_FSMEvent37: set["tfsmextended_Transition"] = None):
        self.isTriggered = isTriggered
        self.tfsmextended_FSMEvent = tfsmextended_FSMEvent
        self.tfsmextended_FSMEvent31 = tfsmextended_FSMEvent31
        self.tfsmextended_FSMEvent46 = tfsmextended_FSMEvent46
        self.tfsmextended_FSMEvent35 = tfsmextended_FSMEvent35
        self.tfsmextended_FSMEvent37 = tfsmextended_FSMEvent37 if tfsmextended_FSMEvent37 is not None else set()
        
    @property
    def isTriggered(self) -> str:
        return self.__isTriggered

    @isTriggered.setter
    def isTriggered(self, isTriggered: str):
        self.__isTriggered = isTriggered

    @property
    def tfsmextended_FSMEvent(self):
        return self.__tfsmextended_FSMEvent

    @tfsmextended_FSMEvent.setter
    def tfsmextended_FSMEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent", None)
        self.__tfsmextended_FSMEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM4"):
                opp_val = getattr(old_value, "tfsmextended_TFSM4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM4"):
                opp_val = getattr(value, "tfsmextended_TFSM4", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TFSM4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_FSMEvent37(self):
        return self.__tfsmextended_FSMEvent37

    @tfsmextended_FSMEvent37.setter
    def tfsmextended_FSMEvent37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent37", None)
        self.__tfsmextended_FSMEvent37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_Transition38"):
                    opp_val = getattr(item, "tfsmextended_Transition38", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_Transition38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_Transition38"):
                    opp_val = getattr(item, "tfsmextended_Transition38", None)
                    
                    setattr(item, "tfsmextended_Transition38", self)
                    

    @property
    def tfsmextended_FSMEvent46(self):
        return self.__tfsmextended_FSMEvent46

    @tfsmextended_FSMEvent46.setter
    def tfsmextended_FSMEvent46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent46", None)
        self.__tfsmextended_FSMEvent46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TimedSystem45"):
                opp_val = getattr(old_value, "tfsmextended_TimedSystem45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TimedSystem45"):
                opp_val = getattr(value, "tfsmextended_TimedSystem45", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TimedSystem45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_FSMEvent35(self):
        return self.__tfsmextended_FSMEvent35

    @tfsmextended_FSMEvent35.setter
    def tfsmextended_FSMEvent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent35", None)
        self.__tfsmextended_FSMEvent35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_EventGuard"):
                opp_val = getattr(old_value, "tfsmextended_EventGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_EventGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_EventGuard"):
                opp_val = getattr(value, "tfsmextended_EventGuard", None)
                setattr(value, "tfsmextended_EventGuard", self)

    @property
    def tfsmextended_FSMEvent31(self):
        return self.__tfsmextended_FSMEvent31

    @tfsmextended_FSMEvent31.setter
    def tfsmextended_FSMEvent31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent31", None)
        self.__tfsmextended_FSMEvent31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_Transition30"):
                opp_val = getattr(old_value, "tfsmextended_Transition30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_Transition30"):
                opp_val = getattr(value, "tfsmextended_Transition30", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_Transition30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def unTrigger(self):
        # TODO: Implement unTrigger method
        pass

    def trigger(self):
        # TODO: Implement trigger method
        pass
