from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Pseudostate:

    pass
class finitestatemachines_Join2(Pseudostate):

    pass
class finitestatemachines_Fork(Pseudostate):

    pass
class finitestatemachines_Trigger2:

    def __init__(self, expression: str, finitestatemachines_Trigger2: "finitestatemachines_Transition2" = None):
        self.expression = expression
        self.finitestatemachines_Trigger2 = finitestatemachines_Trigger2
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def finitestatemachines_Trigger2(self):
        return self.__finitestatemachines_Trigger2

    @finitestatemachines_Trigger2.setter
    def finitestatemachines_Trigger2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Trigger2__finitestatemachines_Trigger2", None)
        self.__finitestatemachines_Trigger2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finitestatemachines_Transition2"):
                opp_val = getattr(old_value, "finitestatemachines_Transition2", None)
                if opp_val == self:
                    setattr(old_value, "finitestatemachines_Transition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finitestatemachines_Transition2"):
                opp_val = getattr(value, "finitestatemachines_Transition2", None)
                setattr(value, "finitestatemachines_Transition2", self)

class State2:

    pass
class finitestatemachines_InitialState(State2):

    pass
class finitestatemachines_Pseudostate(State2):

    pass
class Transition2:

    pass
class finitestatemachines_TimedTransition(Transition2):

    def __init__(self, duration: int):
        self.duration = duration
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

class finitestatemachines_FinalState(State2):

    pass
class finitestatemachines_NamedElement:

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
class finitestatemachines_State2(NamedElement):

    def __init__(self, finalTime: int, initialTime2: int, 1: "finitestatemachines_StateMachine" = None, 6: set["finitestatemachines_Transition2"] = None, 9: set["finitestatemachines_Transition2"] = None, 12: "finitestatemachines_StateMachine" = None, 16: "finitestatemachines_Transition2" = None, 19: "finitestatemachines_Transition2" = None):
        self.finalTime = finalTime
        self.initialTime2 = initialTime2
        self.1 = 1
        self.6 = 6 if 6 is not None else set()
        self.9 = 9 if 9 is not None else set()
        self.12 = 12
        self.16 = 16
        self.19 = 19
        
    @property
    def initialTime2(self) -> int:
        return self.__initialTime2

    @initialTime2.setter
    def initialTime2(self, initialTime2: int):
        self.__initialTime2 = initialTime2

    @property
    def finalTime(self) -> int:
        return self.__finalTime

    @finalTime.setter
    def finalTime(self, finalTime: int):
        self.__finalTime = finalTime

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__12", None)
        self.__12 = value
        
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

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__9", None)
        self.__9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    if opp_val == self:
                        setattr(item, "10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    setattr(item, "10", self)
                    

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__16", None)
        self.__16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "15"):
                opp_val = getattr(old_value, "15", None)
                if opp_val == self:
                    setattr(old_value, "15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "15"):
                opp_val = getattr(value, "15", None)
                setattr(value, "15", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__1", None)
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
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_State2__19", None)
        self.__19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "18"):
                opp_val = getattr(old_value, "18", None)
                if opp_val == self:
                    setattr(old_value, "18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "18"):
                opp_val = getattr(value, "18", None)
                setattr(value, "18", self)

class finitestatemachines_Transition2(NamedElement):

    def __init__(self, initialTime: int, finalTime2: int, 4: "finitestatemachines_StateMachine" = None, 7: "finitestatemachines_State2" = None, 10: "finitestatemachines_State2" = None, 15: "finitestatemachines_State2" = None, 18: "finitestatemachines_State2" = None, finitestatemachines_Transition2: "finitestatemachines_Trigger2" = None, 22: "finitestatemachines_StateMachine" = None):
        self.initialTime = initialTime
        self.finalTime2 = finalTime2
        self.4 = 4
        self.7 = 7
        self.10 = 10
        self.15 = 15
        self.18 = 18
        self.finitestatemachines_Transition2 = finitestatemachines_Transition2
        self.22 = 22
        
    @property
    def initialTime(self) -> int:
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime

    @property
    def finalTime2(self) -> int:
        return self.__finalTime2

    @finalTime2.setter
    def finalTime2(self, finalTime2: int):
        self.__finalTime2 = finalTime2

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                if opp_val is None:
                    setattr(value, "3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__10", None)
        self.__10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                if opp_val is None:
                    setattr(value, "9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "19"):
                opp_val = getattr(old_value, "19", None)
                if opp_val == self:
                    setattr(old_value, "19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "19"):
                opp_val = getattr(value, "19", None)
                setattr(value, "19", self)

    @property
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__15", None)
        self.__15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "16"):
                opp_val = getattr(old_value, "16", None)
                if opp_val == self:
                    setattr(old_value, "16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "16"):
                opp_val = getattr(value, "16", None)
                setattr(value, "16", self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                if opp_val is None:
                    setattr(value, "6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def finitestatemachines_Transition2(self):
        return self.__finitestatemachines_Transition2

    @finitestatemachines_Transition2.setter
    def finitestatemachines_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__finitestatemachines_Transition2", None)
        self.__finitestatemachines_Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "finitestatemachines_Trigger2"):
                opp_val = getattr(old_value, "finitestatemachines_Trigger2", None)
                if opp_val == self:
                    setattr(old_value, "finitestatemachines_Trigger2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "finitestatemachines_Trigger2"):
                opp_val = getattr(value, "finitestatemachines_Trigger2", None)
                setattr(value, "finitestatemachines_Trigger2", self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_finitestatemachines_Transition2__22", None)
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

class finitestatemachines_StateMachine(NamedElement):

    pass