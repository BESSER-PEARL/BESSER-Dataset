from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Transition:

    def __init__(self, name: str, InverseGuard: bool, outgoingTransitions: "fsm_State" = None, fsm_Transition: set["fsm_Action"] = None, fsm_Transition33: "fsm_Guard" = None, Transition: "fsm_State" = None, Transition18: "fsm_State" = None, fsm_Transition36: "fsm_Event" = None, incomingTransitions: "fsm_State" = None):
        self.name = name
        self.InverseGuard = InverseGuard
        self.outgoingTransitions = outgoingTransitions
        self.fsm_Transition = fsm_Transition if fsm_Transition is not None else set()
        self.fsm_Transition33 = fsm_Transition33
        self.Transition = Transition
        self.Transition18 = Transition18
        self.fsm_Transition36 = fsm_Transition36
        self.incomingTransitions = incomingTransitions
        
    @property
    def InverseGuard(self) -> bool:
        return self.__InverseGuard

    @InverseGuard.setter
    def InverseGuard(self, InverseGuard: bool):
        self.__InverseGuard = InverseGuard

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Transition33(self):
        return self.__fsm_Transition33

    @fsm_Transition33.setter
    def fsm_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition33", None)
        self.__fsm_Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Guard34"):
                opp_val = getattr(old_value, "fsm_Guard34", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Guard34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Guard34"):
                opp_val = getattr(value, "fsm_Guard34", None)
                setattr(value, "fsm_Guard34", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State29"):
                opp_val = getattr(old_value, "State29", None)
                if opp_val == self:
                    setattr(old_value, "State29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State29"):
                opp_val = getattr(value, "State29", None)
                setattr(value, "State29", self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State39"):
                opp_val = getattr(old_value, "State39", None)
                if opp_val == self:
                    setattr(old_value, "State39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State39"):
                opp_val = getattr(value, "State39", None)
                setattr(value, "State39", self)

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Action31"):
                    opp_val = getattr(item, "fsm_Action31", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Action31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Action31"):
                    opp_val = getattr(item, "fsm_Action31", None)
                    
                    setattr(item, "fsm_Action31", self)
                    

    @property
    def fsm_Transition36(self):
        return self.__fsm_Transition36

    @fsm_Transition36.setter
    def fsm_Transition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition36", None)
        self.__fsm_Transition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Event37"):
                opp_val = getattr(old_value, "fsm_Event37", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Event37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Event37"):
                opp_val = getattr(value, "fsm_Event37", None)
                setattr(value, "fsm_Event37", self)

    @property
    def Transition18(self):
        return self.__Transition18

    @Transition18.setter
    def Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition18", None)
        self.__Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_StringToStringMap:

    def __init__(self, key: str, value: str, fsm_StringToStringMap: "fsm_FSM" = None, fsm_StringToStringMap45: "fsm_Message" = None, fsm_StringToStringMap48: "fsm_Message" = None):
        self.key = key
        self.value = value
        self.fsm_StringToStringMap = fsm_StringToStringMap
        self.fsm_StringToStringMap45 = fsm_StringToStringMap45
        self.fsm_StringToStringMap48 = fsm_StringToStringMap48
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def fsm_StringToStringMap(self):
        return self.__fsm_StringToStringMap

    @fsm_StringToStringMap.setter
    def fsm_StringToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StringToStringMap__fsm_StringToStringMap", None)
        self.__fsm_StringToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM14"):
                opp_val = getattr(old_value, "fsm_FSM14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM14"):
                opp_val = getattr(value, "fsm_FSM14", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_StringToStringMap48(self):
        return self.__fsm_StringToStringMap48

    @fsm_StringToStringMap48.setter
    def fsm_StringToStringMap48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StringToStringMap__fsm_StringToStringMap48", None)
        self.__fsm_StringToStringMap48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Message47"):
                opp_val = getattr(old_value, "fsm_Message47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Message47"):
                opp_val = getattr(value, "fsm_Message47", None)
                if opp_val is None:
                    setattr(value, "fsm_Message47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_StringToStringMap45(self):
        return self.__fsm_StringToStringMap45

    @fsm_StringToStringMap45.setter
    def fsm_StringToStringMap45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_StringToStringMap__fsm_StringToStringMap45", None)
        self.__fsm_StringToStringMap45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Message44"):
                opp_val = getattr(old_value, "fsm_Message44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Message44"):
                opp_val = getattr(value, "fsm_Message44", None)
                if opp_val is None:
                    setattr(value, "fsm_Message44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_Message:

    def __init__(self, name: str, fsm_Message: "fsm_FSM" = None, fsm_Message27: "fsm_State" = None, fsm_Message41: "fsm_Event" = None, fsm_Message44: set["fsm_StringToStringMap"] = None, fsm_Message47: set["fsm_StringToStringMap"] = None):
        self.name = name
        self.fsm_Message = fsm_Message
        self.fsm_Message27 = fsm_Message27
        self.fsm_Message41 = fsm_Message41
        self.fsm_Message44 = fsm_Message44 if fsm_Message44 is not None else set()
        self.fsm_Message47 = fsm_Message47 if fsm_Message47 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Message27(self):
        return self.__fsm_Message27

    @fsm_Message27.setter
    def fsm_Message27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Message__fsm_Message27", None)
        self.__fsm_Message27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State26"):
                opp_val = getattr(old_value, "fsm_State26", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State26"):
                opp_val = getattr(value, "fsm_State26", None)
                setattr(value, "fsm_State26", self)

    @property
    def fsm_Message(self):
        return self.__fsm_Message

    @fsm_Message.setter
    def fsm_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Message__fsm_Message", None)
        self.__fsm_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM12"):
                opp_val = getattr(old_value, "fsm_FSM12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM12"):
                opp_val = getattr(value, "fsm_FSM12", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Message41(self):
        return self.__fsm_Message41

    @fsm_Message41.setter
    def fsm_Message41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Message__fsm_Message41", None)
        self.__fsm_Message41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Event42"):
                opp_val = getattr(old_value, "fsm_Event42", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Event42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Event42"):
                opp_val = getattr(value, "fsm_Event42", None)
                setattr(value, "fsm_Event42", self)

    @property
    def fsm_Message44(self):
        return self.__fsm_Message44

    @fsm_Message44.setter
    def fsm_Message44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Message__fsm_Message44", None)
        self.__fsm_Message44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StringToStringMap45"):
                    opp_val = getattr(item, "fsm_StringToStringMap45", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StringToStringMap45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StringToStringMap45"):
                    opp_val = getattr(item, "fsm_StringToStringMap45", None)
                    
                    setattr(item, "fsm_StringToStringMap45", self)
                    

    @property
    def fsm_Message47(self):
        return self.__fsm_Message47

    @fsm_Message47.setter
    def fsm_Message47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Message__fsm_Message47", None)
        self.__fsm_Message47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StringToStringMap48"):
                    opp_val = getattr(item, "fsm_StringToStringMap48", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StringToStringMap48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StringToStringMap48"):
                    opp_val = getattr(item, "fsm_StringToStringMap48", None)
                    
                    setattr(item, "fsm_StringToStringMap48", self)
                    

class fsm_Guard:

    def __init__(self, name: str, fsm_Guard34: "fsm_Transition" = None, fsm_Guard: "fsm_FSM" = None):
        self.name = name
        self.fsm_Guard34 = fsm_Guard34
        self.fsm_Guard = fsm_Guard
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Guard34(self):
        return self.__fsm_Guard34

    @fsm_Guard34.setter
    def fsm_Guard34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Guard__fsm_Guard34", None)
        self.__fsm_Guard34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition33"):
                opp_val = getattr(old_value, "fsm_Transition33", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition33"):
                opp_val = getattr(value, "fsm_Transition33", None)
                setattr(value, "fsm_Transition33", self)

    @property
    def fsm_Guard(self):
        return self.__fsm_Guard

    @fsm_Guard.setter
    def fsm_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Guard__fsm_Guard", None)
        self.__fsm_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM10"):
                opp_val = getattr(old_value, "fsm_FSM10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM10"):
                opp_val = getattr(value, "fsm_FSM10", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_Action:

    def __init__(self, name: str, fsm_Action31: "fsm_Transition" = None, fsm_Action: "fsm_FSM" = None, fsm_Action21: "fsm_State" = None, fsm_Action24: "fsm_State" = None):
        self.name = name
        self.fsm_Action31 = fsm_Action31
        self.fsm_Action = fsm_Action
        self.fsm_Action21 = fsm_Action21
        self.fsm_Action24 = fsm_Action24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Action(self):
        return self.__fsm_Action

    @fsm_Action.setter
    def fsm_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action", None)
        self.__fsm_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM8"):
                opp_val = getattr(old_value, "fsm_FSM8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM8"):
                opp_val = getattr(value, "fsm_FSM8", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Action24(self):
        return self.__fsm_Action24

    @fsm_Action24.setter
    def fsm_Action24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action24", None)
        self.__fsm_Action24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State23"):
                opp_val = getattr(old_value, "fsm_State23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State23"):
                opp_val = getattr(value, "fsm_State23", None)
                if opp_val is None:
                    setattr(value, "fsm_State23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Action31(self):
        return self.__fsm_Action31

    @fsm_Action31.setter
    def fsm_Action31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action31", None)
        self.__fsm_Action31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition"):
                opp_val = getattr(old_value, "fsm_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition"):
                opp_val = getattr(value, "fsm_Transition", None)
                if opp_val is None:
                    setattr(value, "fsm_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Action21(self):
        return self.__fsm_Action21

    @fsm_Action21.setter
    def fsm_Action21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action21", None)
        self.__fsm_Action21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State20"):
                opp_val = getattr(old_value, "fsm_State20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State20"):
                opp_val = getattr(value, "fsm_State20", None)
                if opp_val is None:
                    setattr(value, "fsm_State20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fsm_State:

    def __init__(self, name: str, fsm_State: "fsm_FSM" = None, fsm_State4: "fsm_FSM" = None, State: "fsm_FSM" = None, State29: "fsm_Transition" = None, ownedStates: "fsm_FSM" = None, source: set["fsm_Transition"] = None, target: set["fsm_Transition"] = None, fsm_State20: set["fsm_Action"] = None, fsm_State23: set["fsm_Action"] = None, fsm_State26: "fsm_Message" = None, State39: "fsm_Transition" = None):
        self.name = name
        self.fsm_State = fsm_State
        self.fsm_State4 = fsm_State4
        self.State = State
        self.State29 = State29
        self.ownedStates = ownedStates
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.fsm_State20 = fsm_State20 if fsm_State20 is not None else set()
        self.fsm_State23 = fsm_State23 if fsm_State23 is not None else set()
        self.fsm_State26 = fsm_State26
        self.State39 = State39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State29(self):
        return self.__State29

    @State29.setter
    def State29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State29", None)
        self.__State29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def fsm_State4(self):
        return self.__fsm_State4

    @fsm_State4.setter
    def fsm_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State4", None)
        self.__fsm_State4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM3"):
                opp_val = getattr(old_value, "fsm_FSM3", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM3"):
                opp_val = getattr(value, "fsm_FSM3", None)
                setattr(value, "fsm_FSM3", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State23(self):
        return self.__fsm_State23

    @fsm_State23.setter
    def fsm_State23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State23", None)
        self.__fsm_State23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Action24"):
                    opp_val = getattr(item, "fsm_Action24", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Action24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Action24"):
                    opp_val = getattr(item, "fsm_Action24", None)
                    
                    setattr(item, "fsm_Action24", self)
                    

    @property
    def fsm_State26(self):
        return self.__fsm_State26

    @fsm_State26.setter
    def fsm_State26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State26", None)
        self.__fsm_State26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Message27"):
                opp_val = getattr(old_value, "fsm_Message27", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Message27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Message27"):
                opp_val = getattr(value, "fsm_Message27", None)
                setattr(value, "fsm_Message27", self)

    @property
    def ownedStates(self):
        return self.__ownedStates

    @ownedStates.setter
    def ownedStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__ownedStates", None)
        self.__ownedStates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM"):
                opp_val = getattr(old_value, "FSM", None)
                if opp_val == self:
                    setattr(old_value, "FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM"):
                opp_val = getattr(value, "FSM", None)
                setattr(value, "FSM", self)

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
    def State39(self):
        return self.__State39

    @State39.setter
    def State39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State39", None)
        self.__State39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def fsm_State20(self):
        return self.__fsm_State20

    @fsm_State20.setter
    def fsm_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State20", None)
        self.__fsm_State20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Action21"):
                    opp_val = getattr(item, "fsm_Action21", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Action21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Action21"):
                    opp_val = getattr(item, "fsm_Action21", None)
                    
                    setattr(item, "fsm_Action21", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition18"):
                    opp_val = getattr(item, "Transition18", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition18"):
                    opp_val = getattr(item, "Transition18", None)
                    
                    setattr(item, "Transition18", self)
                    

class fsm_FSM:

    def __init__(self, isServer: bool, name: str, groupId: str, fsm_FSM: "fsm_State" = None, fsm_FSM3: "fsm_State" = None, fsm_FSM6: set["fsm_Event"] = None, owningFSM: set["fsm_State"] = None, fsm_FSM8: set["fsm_Action"] = None, fsm_FSM10: set["fsm_Guard"] = None, fsm_FSM12: set["fsm_Message"] = None, fsm_FSM14: set["fsm_StringToStringMap"] = None, FSM: "fsm_State" = None):
        self.isServer = isServer
        self.name = name
        self.groupId = groupId
        self.fsm_FSM = fsm_FSM
        self.fsm_FSM3 = fsm_FSM3
        self.fsm_FSM6 = fsm_FSM6 if fsm_FSM6 is not None else set()
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.fsm_FSM8 = fsm_FSM8 if fsm_FSM8 is not None else set()
        self.fsm_FSM10 = fsm_FSM10 if fsm_FSM10 is not None else set()
        self.fsm_FSM12 = fsm_FSM12 if fsm_FSM12 is not None else set()
        self.fsm_FSM14 = fsm_FSM14 if fsm_FSM14 is not None else set()
        self.FSM = FSM
        
    @property
    def groupId(self) -> str:
        return self.__groupId

    @groupId.setter
    def groupId(self, groupId: str):
        self.__groupId = groupId

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isServer(self) -> bool:
        return self.__isServer

    @isServer.setter
    def isServer(self, isServer: bool):
        self.__isServer = isServer

    @property
    def fsm_FSM14(self):
        return self.__fsm_FSM14

    @fsm_FSM14.setter
    def fsm_FSM14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM14", None)
        self.__fsm_FSM14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_StringToStringMap"):
                    opp_val = getattr(item, "fsm_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_StringToStringMap"):
                    opp_val = getattr(item, "fsm_StringToStringMap", None)
                    
                    setattr(item, "fsm_StringToStringMap", self)
                    

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__FSM", None)
        self.__FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedStates"):
                opp_val = getattr(old_value, "ownedStates", None)
                if opp_val == self:
                    setattr(old_value, "ownedStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedStates"):
                opp_val = getattr(value, "ownedStates", None)
                setattr(value, "ownedStates", self)

    @property
    def fsm_FSM10(self):
        return self.__fsm_FSM10

    @fsm_FSM10.setter
    def fsm_FSM10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM10", None)
        self.__fsm_FSM10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Guard"):
                    opp_val = getattr(item, "fsm_Guard", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Guard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Guard"):
                    opp_val = getattr(item, "fsm_Guard", None)
                    
                    setattr(item, "fsm_Guard", self)
                    

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__owningFSM", None)
        self.__owningFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def fsm_FSM3(self):
        return self.__fsm_FSM3

    @fsm_FSM3.setter
    def fsm_FSM3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM3", None)
        self.__fsm_FSM3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State4"):
                opp_val = getattr(old_value, "fsm_State4", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State4"):
                opp_val = getattr(value, "fsm_State4", None)
                setattr(value, "fsm_State4", self)

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
    def fsm_FSM8(self):
        return self.__fsm_FSM8

    @fsm_FSM8.setter
    def fsm_FSM8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM8", None)
        self.__fsm_FSM8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Action"):
                    opp_val = getattr(item, "fsm_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Action"):
                    opp_val = getattr(item, "fsm_Action", None)
                    
                    setattr(item, "fsm_Action", self)
                    

    @property
    def fsm_FSM6(self):
        return self.__fsm_FSM6

    @fsm_FSM6.setter
    def fsm_FSM6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM6", None)
        self.__fsm_FSM6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Event"):
                    opp_val = getattr(item, "fsm_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Event"):
                    opp_val = getattr(item, "fsm_Event", None)
                    
                    setattr(item, "fsm_Event", self)
                    

    @property
    def fsm_FSM12(self):
        return self.__fsm_FSM12

    @fsm_FSM12.setter
    def fsm_FSM12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM12", None)
        self.__fsm_FSM12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fsm_Message"):
                    opp_val = getattr(item, "fsm_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "fsm_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fsm_Message"):
                    opp_val = getattr(item, "fsm_Message", None)
                    
                    setattr(item, "fsm_Message", self)
                    

class fsm_Event:

    def __init__(self, name: str, fsm_Event: "fsm_FSM" = None, fsm_Event37: "fsm_Transition" = None, fsm_Event42: "fsm_Message" = None):
        self.name = name
        self.fsm_Event = fsm_Event
        self.fsm_Event37 = fsm_Event37
        self.fsm_Event42 = fsm_Event42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fsm_Event37(self):
        return self.__fsm_Event37

    @fsm_Event37.setter
    def fsm_Event37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Event__fsm_Event37", None)
        self.__fsm_Event37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition36"):
                opp_val = getattr(old_value, "fsm_Transition36", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition36"):
                opp_val = getattr(value, "fsm_Transition36", None)
                setattr(value, "fsm_Transition36", self)

    @property
    def fsm_Event42(self):
        return self.__fsm_Event42

    @fsm_Event42.setter
    def fsm_Event42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Event__fsm_Event42", None)
        self.__fsm_Event42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Message41"):
                opp_val = getattr(old_value, "fsm_Message41", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Message41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Message41"):
                opp_val = getattr(value, "fsm_Message41", None)
                setattr(value, "fsm_Message41", self)

    @property
    def fsm_Event(self):
        return self.__fsm_Event

    @fsm_Event.setter
    def fsm_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Event__fsm_Event", None)
        self.__fsm_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM6"):
                opp_val = getattr(old_value, "fsm_FSM6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM6"):
                opp_val = getattr(value, "fsm_FSM6", None)
                if opp_val is None:
                    setattr(value, "fsm_FSM6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
