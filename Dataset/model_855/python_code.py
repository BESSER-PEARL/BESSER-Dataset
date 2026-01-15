from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_System:

    pass
class fsm_Buffer:

    def __init__(self, initialValue: str, name: str, currentValues: str, 7: "fsm_FSM" = None, 10: "fsm_FSM" = None, 25: "fsm_FSM" = None, 28: "fsm_FSM" = None, fsm_Buffer: "fsm_System" = None):
        self.initialValue = initialValue
        self.name = name
        self.currentValues = currentValues
        self.7 = 7
        self.10 = 10
        self.25 = 25
        self.28 = 28
        self.fsm_Buffer = fsm_Buffer
        
    @property
    def currentValues(self) -> str:
        return self.__currentValues

    @currentValues.setter
    def currentValues(self, currentValues: str):
        self.__currentValues = currentValues

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def fsm_Buffer(self):
        return self.__fsm_Buffer

    @fsm_Buffer.setter
    def fsm_Buffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__fsm_Buffer", None)
        self.__fsm_Buffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_System42"):
                opp_val = getattr(old_value, "fsm_System42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_System42"):
                opp_val = getattr(value, "fsm_System42", None)
                if opp_val is None:
                    setattr(value, "fsm_System42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 28(self):
        return self.__28

    @28.setter
    def 28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__28", None)
        self.__28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

    @property
    def 25(self):
        return self.__25

    @25.setter
    def 25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__25", None)
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
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__10", None)
        self.__10 = value
        
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
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if opp_val == self:
                    setattr(old_value, "6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                setattr(value, "6", self)

class fsm_Transition:

    def __init__(self, name: str, trigger: str, action: str, 4: "fsm_FSM" = None, 17: "fsm_State" = None, 20: "fsm_State" = None, 31: "fsm_State" = None, 34: "fsm_State" = None, 37: "fsm_FSM" = None):
        self.name = name
        self.trigger = trigger
        self.action = action
        self.4 = 4
        self.17 = 17
        self.20 = 20
        self.31 = 31
        self.34 = 34
        self.37 = 37
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__4", None)
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
    def 34(self):
        return self.__34

    @34.setter
    def 34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__34", None)
        self.__34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "35"):
                opp_val = getattr(old_value, "35", None)
                if opp_val == self:
                    setattr(old_value, "35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "35"):
                opp_val = getattr(value, "35", None)
                setattr(value, "35", self)

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

    @property
    def 37(self):
        return self.__37

    @37.setter
    def 37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__37", None)
        self.__37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "38"):
                opp_val = getattr(old_value, "38", None)
                if opp_val == self:
                    setattr(old_value, "38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "38"):
                opp_val = getattr(value, "38", None)
                setattr(value, "38", self)

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
    def 31(self):
        return self.__31

    @31.setter
    def 31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__31", None)
        self.__31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "32"):
                opp_val = getattr(old_value, "32", None)
                if opp_val == self:
                    setattr(old_value, "32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "32"):
                opp_val = getattr(value, "32", None)
                setattr(value, "32", self)

class fsm_State:

    def __init__(self, name: str, 1: "fsm_FSM" = None, fsm_State: "fsm_FSM" = None, fsm_State14: "fsm_FSM" = None, 16: set["fsm_Transition"] = None, 19: set["fsm_Transition"] = None, 22: "fsm_FSM" = None, 32: "fsm_Transition" = None, 35: "fsm_Transition" = None):
        self.name = name
        self.1 = 1
        self.fsm_State = fsm_State
        self.fsm_State14 = fsm_State14
        self.16 = 16 if 16 is not None else set()
        self.19 = 19 if 19 is not None else set()
        self.22 = 22
        self.32 = 32
        self.35 = 35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 16(self):
        return self.__16

    @16.setter
    def 16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__16", None)
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
    def 32(self):
        return self.__32

    @32.setter
    def 32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__32", None)
        self.__32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "31"):
                opp_val = getattr(old_value, "31", None)
                if opp_val == self:
                    setattr(old_value, "31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "31"):
                opp_val = getattr(value, "31", None)
                setattr(value, "31", self)

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
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__19", None)
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
    def 35(self):
        return self.__35

    @35.setter
    def 35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__35", None)
        self.__35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "34"):
                opp_val = getattr(old_value, "34", None)
                if opp_val == self:
                    setattr(old_value, "34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "34"):
                opp_val = getattr(value, "34", None)
                setattr(value, "34", self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__22", None)
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
    def fsm_State14(self):
        return self.__fsm_State14

    @fsm_State14.setter
    def fsm_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State14", None)
        self.__fsm_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM13"):
                opp_val = getattr(old_value, "fsm_FSM13", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM13"):
                opp_val = getattr(value, "fsm_FSM13", None)
                setattr(value, "fsm_FSM13", self)

class fsm_FSM:

    def __init__(self, name: str, underProcessTrigger: str, consummedString: str, : set["fsm_State"] = None, 3: set["fsm_Transition"] = None, 6: "fsm_Buffer" = None, 9: "fsm_Buffer" = None, fsm_FSM: "fsm_State" = None, fsm_FSM13: "fsm_State" = None, 23: "fsm_State" = None, 26: "fsm_Buffer" = None, 29: "fsm_Buffer" = None, 38: "fsm_Transition" = None, fsm_FSM40: "fsm_System" = None):
        self.name = name
        self.underProcessTrigger = underProcessTrigger
        self.consummedString = consummedString
        self. =  if  is not None else set()
        self.3 = 3 if 3 is not None else set()
        self.6 = 6
        self.9 = 9
        self.fsm_FSM = fsm_FSM
        self.fsm_FSM13 = fsm_FSM13
        self.23 = 23
        self.26 = 26
        self.29 = 29
        self.38 = 38
        self.fsm_FSM40 = fsm_FSM40
        
    @property
    def consummedString(self) -> str:
        return self.__consummedString

    @consummedString.setter
    def consummedString(self, consummedString: str):
        self.__consummedString = consummedString

    @property
    def underProcessTrigger(self) -> str:
        return self.__underProcessTrigger

    @underProcessTrigger.setter
    def underProcessTrigger(self, underProcessTrigger: str):
        self.__underProcessTrigger = underProcessTrigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__6", None)
        self.__6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if opp_val == self:
                    setattr(old_value, "7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                setattr(value, "7", self)

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__9", None)
        self.__9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if opp_val == self:
                    setattr(old_value, "10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                setattr(value, "10", self)

    @property
    def 29(self):
        return self.__29

    @29.setter
    def 29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__29", None)
        self.__29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "28"):
                opp_val = getattr(old_value, "28", None)
                if opp_val == self:
                    setattr(old_value, "28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "28"):
                opp_val = getattr(value, "28", None)
                setattr(value, "28", self)

    @property
    def 23(self):
        return self.__23

    @23.setter
    def 23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__23", None)
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
    def 26(self):
        return self.__26

    @26.setter
    def 26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__26", None)
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
    def fsm_FSM40(self):
        return self.__fsm_FSM40

    @fsm_FSM40.setter
    def fsm_FSM40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM40", None)
        self.__fsm_FSM40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_System"):
                opp_val = getattr(old_value, "fsm_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_System"):
                opp_val = getattr(value, "fsm_System", None)
                if opp_val is None:
                    setattr(value, "fsm_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__", None)
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
    def fsm_FSM(self):
        return self.__fsm_FSM

    @fsm_FSM.setter
    def fsm_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM", None)
        self.__fsm_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State"):
                opp_val = getattr(old_value, "fsm_State", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State"):
                opp_val = getattr(value, "fsm_State", None)
                setattr(value, "fsm_State", self)

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__3", None)
        self.__3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    

    @property
    def 38(self):
        return self.__38

    @38.setter
    def 38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__38", None)
        self.__38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "37"):
                opp_val = getattr(old_value, "37", None)
                if opp_val == self:
                    setattr(old_value, "37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "37"):
                opp_val = getattr(value, "37", None)
                setattr(value, "37", self)

    @property
    def fsm_FSM13(self):
        return self.__fsm_FSM13

    @fsm_FSM13.setter
    def fsm_FSM13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM13", None)
        self.__fsm_FSM13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State14"):
                opp_val = getattr(old_value, "fsm_State14", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State14"):
                opp_val = getattr(value, "fsm_State14", None)
                setattr(value, "fsm_State14", self)
