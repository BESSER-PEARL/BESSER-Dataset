from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_System:

    pass
class fsm_Buffer:

    def __init__(self, initialValue: str, name: str, currentValues: str, Buffer: "fsm_FSM" = None, Buffer5: "fsm_FSM" = None, inputBuffer: "fsm_FSM" = None, outputBuffer: "fsm_FSM" = None, fsm_Buffer: "fsm_System" = None):
        self.initialValue = initialValue
        self.name = name
        self.currentValues = currentValues
        self.Buffer = Buffer
        self.Buffer5 = Buffer5
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer
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
    def outputBuffer(self):
        return self.__outputBuffer

    @outputBuffer.setter
    def outputBuffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__outputBuffer", None)
        self.__outputBuffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM18"):
                opp_val = getattr(old_value, "FSM18", None)
                if opp_val == self:
                    setattr(old_value, "FSM18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM18"):
                opp_val = getattr(value, "FSM18", None)
                setattr(value, "FSM18", self)

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
            if hasattr(old_value, "fsm_System28"):
                opp_val = getattr(old_value, "fsm_System28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_System28"):
                opp_val = getattr(value, "fsm_System28", None)
                if opp_val is None:
                    setattr(value, "fsm_System28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inputBuffer(self):
        return self.__inputBuffer

    @inputBuffer.setter
    def inputBuffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__inputBuffer", None)
        self.__inputBuffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM16"):
                opp_val = getattr(old_value, "FSM16", None)
                if opp_val == self:
                    setattr(old_value, "FSM16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM16"):
                opp_val = getattr(value, "FSM16", None)
                setattr(value, "FSM16", self)

    @property
    def Buffer5(self):
        return self.__Buffer5

    @Buffer5.setter
    def Buffer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__Buffer5", None)
        self.__Buffer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingFSM"):
                opp_val = getattr(old_value, "incomingFSM", None)
                if opp_val == self:
                    setattr(old_value, "incomingFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingFSM"):
                opp_val = getattr(value, "incomingFSM", None)
                setattr(value, "incomingFSM", self)

    @property
    def Buffer(self):
        return self.__Buffer

    @Buffer.setter
    def Buffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Buffer__Buffer", None)
        self.__Buffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingFSM"):
                opp_val = getattr(old_value, "outgoingFSM", None)
                if opp_val == self:
                    setattr(old_value, "outgoingFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingFSM"):
                opp_val = getattr(value, "outgoingFSM", None)
                setattr(value, "outgoingFSM", self)

class fsm_Transition:

    def __init__(self, name: str, trigger: str, action: str, Transition11: "fsm_State" = None, Transition13: "fsm_State" = None, Transition: "fsm_FSM" = None, incoming: "fsm_State" = None, outgoing: "fsm_State" = None, ownedTransitions: "fsm_FSM" = None):
        self.name = name
        self.trigger = trigger
        self.action = action
        self.Transition11 = Transition11
        self.Transition13 = Transition13
        self.Transition = Transition
        self.incoming = incoming
        self.outgoing = outgoing
        self.ownedTransitions = ownedTransitions
        
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
    def ownedTransitions(self):
        return self.__ownedTransitions

    @ownedTransitions.setter
    def ownedTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__ownedTransitions", None)
        self.__ownedTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM24"):
                opp_val = getattr(old_value, "FSM24", None)
                if opp_val == self:
                    setattr(old_value, "FSM24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM24"):
                opp_val = getattr(value, "FSM24", None)
                setattr(value, "FSM24", self)

    @property
    def Transition13(self):
        return self.__Transition13

    @Transition13.setter
    def Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition13", None)
        self.__Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "src"):
                opp_val = getattr(old_value, "src", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "src"):
                opp_val = getattr(value, "src", None)
                if opp_val is None:
                    setattr(value, "src", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State20"):
                opp_val = getattr(old_value, "State20", None)
                if opp_val == self:
                    setattr(old_value, "State20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State20"):
                opp_val = getattr(value, "State20", None)
                setattr(value, "State20", self)

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
            if hasattr(old_value, "fsm2"):
                opp_val = getattr(old_value, "fsm2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm2"):
                opp_val = getattr(value, "fsm2", None)
                if opp_val is None:
                    setattr(value, "fsm2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition11(self):
        return self.__Transition11

    @Transition11.setter
    def Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition11", None)
        self.__Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tgt"):
                opp_val = getattr(old_value, "tgt", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tgt"):
                opp_val = getattr(value, "tgt", None)
                if opp_val is None:
                    setattr(value, "tgt", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State22"):
                opp_val = getattr(old_value, "State22", None)
                if opp_val == self:
                    setattr(old_value, "State22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State22"):
                opp_val = getattr(value, "State22", None)
                setattr(value, "State22", self)

class fsm_State:

    def __init__(self, name: str, tgt: set["fsm_Transition"] = None, src: set["fsm_Transition"] = None, ownedStates: "fsm_FSM" = None, State: "fsm_FSM" = None, fsm_State: "fsm_FSM" = None, fsm_State9: "fsm_FSM" = None, State20: "fsm_Transition" = None, State22: "fsm_Transition" = None):
        self.name = name
        self.tgt = tgt if tgt is not None else set()
        self.src = src if src is not None else set()
        self.ownedStates = ownedStates
        self.State = State
        self.fsm_State = fsm_State
        self.fsm_State9 = fsm_State9
        self.State20 = State20
        self.State22 = State22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State20(self):
        return self.__State20

    @State20.setter
    def State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State20", None)
        self.__State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

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
    def State22(self):
        return self.__State22

    @State22.setter
    def State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State22", None)
        self.__State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

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
            if hasattr(old_value, "fsm"):
                opp_val = getattr(old_value, "fsm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm"):
                opp_val = getattr(value, "fsm", None)
                if opp_val is None:
                    setattr(value, "fsm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition13"):
                    opp_val = getattr(item, "Transition13", None)
                    
                    setattr(item, "Transition13", self)
                    

    @property
    def tgt(self):
        return self.__tgt

    @tgt.setter
    def tgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__tgt", None)
        self.__tgt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition11"):
                    opp_val = getattr(item, "Transition11", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition11"):
                    opp_val = getattr(item, "Transition11", None)
                    
                    setattr(item, "Transition11", self)
                    

    @property
    def fsm_State9(self):
        return self.__fsm_State9

    @fsm_State9.setter
    def fsm_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State9", None)
        self.__fsm_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_FSM8"):
                opp_val = getattr(old_value, "fsm_FSM8", None)
                if opp_val == self:
                    setattr(old_value, "fsm_FSM8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_FSM8"):
                opp_val = getattr(value, "fsm_FSM8", None)
                setattr(value, "fsm_FSM8", self)

class fsm_FSM:

    def __init__(self, underProcessTrigger: str, consummedString: str, name: str, FSM: "fsm_State" = None, fsm: set["fsm_State"] = None, fsm2: set["fsm_Transition"] = None, outgoingFSM: "fsm_Buffer" = None, incomingFSM: "fsm_Buffer" = None, fsm_FSM: "fsm_State" = None, fsm_FSM8: "fsm_State" = None, FSM16: "fsm_Buffer" = None, FSM18: "fsm_Buffer" = None, FSM24: "fsm_Transition" = None, fsm_FSM26: "fsm_System" = None):
        self.underProcessTrigger = underProcessTrigger
        self.consummedString = consummedString
        self.name = name
        self.FSM = FSM
        self.fsm = fsm if fsm is not None else set()
        self.fsm2 = fsm2 if fsm2 is not None else set()
        self.outgoingFSM = outgoingFSM
        self.incomingFSM = incomingFSM
        self.fsm_FSM = fsm_FSM
        self.fsm_FSM8 = fsm_FSM8
        self.FSM16 = FSM16
        self.FSM18 = FSM18
        self.FSM24 = FSM24
        self.fsm_FSM26 = fsm_FSM26
        
    @property
    def underProcessTrigger(self) -> str:
        return self.__underProcessTrigger

    @underProcessTrigger.setter
    def underProcessTrigger(self, underProcessTrigger: str):
        self.__underProcessTrigger = underProcessTrigger

    @property
    def consummedString(self) -> str:
        return self.__consummedString

    @consummedString.setter
    def consummedString(self, consummedString: str):
        self.__consummedString = consummedString

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def outgoingFSM(self):
        return self.__outgoingFSM

    @outgoingFSM.setter
    def outgoingFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__outgoingFSM", None)
        self.__outgoingFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Buffer"):
                opp_val = getattr(old_value, "Buffer", None)
                if opp_val == self:
                    setattr(old_value, "Buffer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Buffer"):
                opp_val = getattr(value, "Buffer", None)
                setattr(value, "Buffer", self)

    @property
    def fsm_FSM26(self):
        return self.__fsm_FSM26

    @fsm_FSM26.setter
    def fsm_FSM26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM26", None)
        self.__fsm_FSM26 = value
        
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
    def fsm(self):
        return self.__fsm

    @fsm.setter
    def fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm", None)
        self.__fsm = value if value is not None else set()
        
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
    def FSM24(self):
        return self.__FSM24

    @FSM24.setter
    def FSM24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__FSM24", None)
        self.__FSM24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedTransitions"):
                opp_val = getattr(old_value, "ownedTransitions", None)
                if opp_val == self:
                    setattr(old_value, "ownedTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedTransitions"):
                opp_val = getattr(value, "ownedTransitions", None)
                setattr(value, "ownedTransitions", self)

    @property
    def incomingFSM(self):
        return self.__incomingFSM

    @incomingFSM.setter
    def incomingFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__incomingFSM", None)
        self.__incomingFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Buffer5"):
                opp_val = getattr(old_value, "Buffer5", None)
                if opp_val == self:
                    setattr(old_value, "Buffer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Buffer5"):
                opp_val = getattr(value, "Buffer5", None)
                setattr(value, "Buffer5", self)

    @property
    def FSM16(self):
        return self.__FSM16

    @FSM16.setter
    def FSM16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__FSM16", None)
        self.__FSM16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inputBuffer"):
                opp_val = getattr(old_value, "inputBuffer", None)
                if opp_val == self:
                    setattr(old_value, "inputBuffer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inputBuffer"):
                opp_val = getattr(value, "inputBuffer", None)
                setattr(value, "inputBuffer", self)

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
    def fsm2(self):
        return self.__fsm2

    @fsm2.setter
    def fsm2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm2", None)
        self.__fsm2 = value if value is not None else set()
        
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
    def FSM18(self):
        return self.__FSM18

    @FSM18.setter
    def FSM18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__FSM18", None)
        self.__FSM18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outputBuffer"):
                opp_val = getattr(old_value, "outputBuffer", None)
                if opp_val == self:
                    setattr(old_value, "outputBuffer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outputBuffer"):
                opp_val = getattr(value, "outputBuffer", None)
                setattr(value, "outputBuffer", self)

    @property
    def fsm_FSM8(self):
        return self.__fsm_FSM8

    @fsm_FSM8.setter
    def fsm_FSM8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_FSM__fsm_FSM8", None)
        self.__fsm_FSM8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_State9"):
                opp_val = getattr(old_value, "fsm_State9", None)
                if opp_val == self:
                    setattr(old_value, "fsm_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_State9"):
                opp_val = getattr(value, "fsm_State9", None)
                setattr(value, "fsm_State9", self)
