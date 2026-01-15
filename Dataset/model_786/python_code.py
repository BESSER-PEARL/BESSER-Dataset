from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_State:

    def __init__(self, name: str, fsm_State5: "fsm_FSM" = None, 8: "fsm_FSM" = None, 11: set["fsm_Transition"] = None, 14: set["fsm_Transition"] = None, 18: "fsm_Transition" = None, 1: "fsm_FSM" = None, fsm_State: "fsm_FSM" = None, 21: "fsm_Transition" = None, fsm_State24: "fsm_RuntimeConcept1" = None):
        self.name = name
        self.fsm_State5 = fsm_State5
        self.8 = 8
        self.11 = 11 if 11 is not None else set()
        self.14 = 14 if 14 is not None else set()
        self.18 = 18
        self.1 = 1
        self.fsm_State = fsm_State
        self.21 = 21
        self.fsm_State24 = fsm_State24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 21(self):
        return self.__21

    @21.setter
    def 21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__21", None)
        self.__21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "20"):
                opp_val = getattr(old_value, "20", None)
                if opp_val == self:
                    setattr(old_value, "20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "20"):
                opp_val = getattr(value, "20", None)
                setattr(value, "20", self)

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM"):
                opp_val = getattr(old_value, "fsm_FSM", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM"):
                opp_val = getattr(value, "fsm_FSM", None)
                setattr(value, "fsm_FSM", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__1", None)
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
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "17"):
                opp_val = getattr(old_value, "17", None)
                if opp_val == self:
                    setattr(old_value, "17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "17"):
                opp_val = getattr(value, "17", None)
                setattr(value, "17", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__14", None)
        self.__14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    if opp_val == self:
                        setattr(item, "15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "15"):
                    opp_val = getattr(item, "15", None)
                    
                    setattr(item, "15", self)
                    

    @property
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if opp_val == self:
                    setattr(old_value, "9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                setattr(value, "9", self)

    @property
    def fsm_State5(self):
        return self.__fsm_State5

    @fsm_State5.setter
    def fsm_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State5", None)
        self.__fsm_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM4"):
                opp_val = getattr(old_value, "fsm_FSM4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM4"):
                opp_val = getattr(value, "fsm_FSM4", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State24(self):
        return self.__fsm_State24

    @fsm_State24.setter
    def fsm_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State24", None)
        self.__fsm_State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_RuntimeConcept123"):
                opp_val = getattr(old_value, "fsm_RuntimeConcept123", None)
                if opp_val == self:
                    setattr(old_value, "fsm_RuntimeConcept123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_RuntimeConcept123"):
                opp_val = getattr(value, "fsm_RuntimeConcept123", None)
                setattr(value, "fsm_RuntimeConcept123", self)

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__11", None)
        self.__11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    if opp_val == self:
                        setattr(item, "12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "12"):
                    opp_val = getattr(item, "12", None)
                    
                    setattr(item, "12", self)
                    

class fsm_FSM:

    pass
class fsm_Transition:

    def __init__(self, input: str, output: str, 12: "fsm_State" = None, 15: "fsm_State" = None, 17: "fsm_State" = None, 20: "fsm_State" = None):
        self.input = input
        self.output = output
        self.12 = 12
        self.15 = 15
        self.17 = 17
        self.20 = 20
        
    @property
    def output(self) -> str:
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output

    @property
    def input(self) -> str:
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

    @property
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__17", None)
        self.__17 = value
        
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

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "11"):
                opp_val = getattr(old_value, "11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "11"):
                opp_val = getattr(value, "11", None)
                if opp_val is None:
                    setattr(value, "11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 15(self):
        return self.__15

    @15.setter
    def 15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__15", None)
        self.__15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                if opp_val is None:
                    setattr(value, "14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_RuntimeConcept1:

    def __init__(self, foo: int, fsm_RuntimeConcept1: "fsm_RuntimeConcept2" = None, fsm_RuntimeConcept123: "fsm_State" = None):
        self.foo = foo
        self.fsm_RuntimeConcept1 = fsm_RuntimeConcept1
        self.fsm_RuntimeConcept123 = fsm_RuntimeConcept123
        
    @property
    def foo(self) -> int:
        return self.__foo

    @foo.setter
    def foo(self, foo: int):
        self.__foo = foo

    @property
    def fsm_RuntimeConcept1(self):
        return self.__fsm_RuntimeConcept1

    @fsm_RuntimeConcept1.setter
    def fsm_RuntimeConcept1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RuntimeConcept1__fsm_RuntimeConcept1", None)
        self.__fsm_RuntimeConcept1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_RuntimeConcept2"):
                opp_val = getattr(old_value, "fsm_RuntimeConcept2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_RuntimeConcept2"):
                opp_val = getattr(value, "fsm_RuntimeConcept2", None)
                if opp_val is None:
                    setattr(value, "fsm_RuntimeConcept2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_RuntimeConcept123(self):
        return self.__fsm_RuntimeConcept123

    @fsm_RuntimeConcept123.setter
    def fsm_RuntimeConcept123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RuntimeConcept1__fsm_RuntimeConcept123", None)
        self.__fsm_RuntimeConcept123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State24"):
                opp_val = getattr(old_value, "fsm_State24", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State24"):
                opp_val = getattr(value, "fsm_State24", None)
                setattr(value, "fsm_State24", self)

class fsm_RuntimeConcept2:

    def __init__(self, bar: str, fsm_RuntimeConcept2: set["fsm_RuntimeConcept1"] = None):
        self.bar = bar
        self.fsm_RuntimeConcept2 = fsm_RuntimeConcept2 if fsm_RuntimeConcept2 is not None else set()
        
    @property
    def bar(self) -> str:
        return self.__bar

    @bar.setter
    def bar(self, bar: str):
        self.__bar = bar

    @property
    def fsm_RuntimeConcept2(self):
        return self.__fsm_RuntimeConcept2

    @fsm_RuntimeConcept2.setter
    def fsm_RuntimeConcept2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_RuntimeConcept2__fsm_RuntimeConcept2", None)
        self.__fsm_RuntimeConcept2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_RuntimeConcept1"):
                    opp_val = getattr(item, "fsm_RuntimeConcept1", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_RuntimeConcept1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_RuntimeConcept1"):
                    opp_val = getattr(item, "fsm_RuntimeConcept1", None)
                    
                    setattr(item, "fsm_RuntimeConcept1", self)
                    
