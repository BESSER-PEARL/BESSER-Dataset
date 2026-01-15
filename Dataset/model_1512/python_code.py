from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_System:

    pass
class model_Buffer:

    def __init__(self, initialValue: str, name: str, Buffer: "model_FSM" = None, Buffer5: "model_FSM" = None, inputBuffer: "model_FSM" = None, outputBuffer: "model_FSM" = None, model_Buffer: "model_System" = None):
        self.initialValue = initialValue
        self.name = name
        self.Buffer = Buffer
        self.Buffer5 = Buffer5
        self.inputBuffer = inputBuffer
        self.outputBuffer = outputBuffer
        self.model_Buffer = model_Buffer
        
    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def outputBuffer(self):
        return self.__outputBuffer

    @outputBuffer.setter
    def outputBuffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Buffer__outputBuffer", None)
        self.__outputBuffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM15"):
                opp_val = getattr(old_value, "FSM15", None)
                if opp_val == self:
                    setattr(old_value, "FSM15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM15"):
                opp_val = getattr(value, "FSM15", None)
                setattr(value, "FSM15", self)

    @property
    def Buffer5(self):
        return self.__Buffer5

    @Buffer5.setter
    def Buffer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Buffer__Buffer5", None)
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
    def inputBuffer(self):
        return self.__inputBuffer

    @inputBuffer.setter
    def inputBuffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Buffer__inputBuffer", None)
        self.__inputBuffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM13"):
                opp_val = getattr(old_value, "FSM13", None)
                if opp_val == self:
                    setattr(old_value, "FSM13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM13"):
                opp_val = getattr(value, "FSM13", None)
                setattr(value, "FSM13", self)

    @property
    def Buffer(self):
        return self.__Buffer

    @Buffer.setter
    def Buffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Buffer__Buffer", None)
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

    @property
    def model_Buffer(self):
        return self.__model_Buffer

    @model_Buffer.setter
    def model_Buffer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Buffer__model_Buffer", None)
        self.__model_Buffer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_System25"):
                opp_val = getattr(old_value, "model_System25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_System25"):
                opp_val = getattr(value, "model_System25", None)
                if opp_val is None:
                    setattr(value, "model_System25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Transition:

    def __init__(self, name: str, trigger: str, action: str, Transition: "model_FSM" = None, Transition8: "model_State" = None, Transition10: "model_State" = None, incoming: "model_State" = None, outgoing: "model_State" = None, ownedTransitions: "model_FSM" = None):
        self.name = name
        self.trigger = trigger
        self.action = action
        self.Transition = Transition
        self.Transition8 = Transition8
        self.Transition10 = Transition10
        self.incoming = incoming
        self.outgoing = outgoing
        self.ownedTransitions = ownedTransitions
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

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
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__Transition8", None)
        self.__Transition8 = value
        
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
    def ownedTransitions(self):
        return self.__ownedTransitions

    @ownedTransitions.setter
    def ownedTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__ownedTransitions", None)
        self.__ownedTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FSM21"):
                opp_val = getattr(old_value, "FSM21", None)
                if opp_val == self:
                    setattr(old_value, "FSM21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FSM21"):
                opp_val = getattr(value, "FSM21", None)
                setattr(value, "FSM21", self)

    @property
    def Transition10(self):
        return self.__Transition10

    @Transition10.setter
    def Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__Transition10", None)
        self.__Transition10 = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__Transition", None)
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State19"):
                opp_val = getattr(old_value, "State19", None)
                if opp_val == self:
                    setattr(old_value, "State19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State19"):
                opp_val = getattr(value, "State19", None)
                setattr(value, "State19", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State17"):
                opp_val = getattr(old_value, "State17", None)
                if opp_val == self:
                    setattr(old_value, "State17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State17"):
                opp_val = getattr(value, "State17", None)
                setattr(value, "State17", self)

class model_State:

    def __init__(self, name: str, State: "model_FSM" = None, model_State: "model_FSM" = None, tgt: set["model_Transition"] = None, src: set["model_Transition"] = None, ownedStates: "model_FSM" = None, State17: "model_Transition" = None, State19: "model_Transition" = None):
        self.name = name
        self.State = State
        self.model_State = model_State
        self.tgt = tgt if tgt is not None else set()
        self.src = src if src is not None else set()
        self.ownedStates = ownedStates
        self.State17 = State17
        self.State19 = State19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State", None)
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
    def State17(self):
        return self.__State17

    @State17.setter
    def State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State17", None)
        self.__State17 = value
        
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
    def tgt(self):
        return self.__tgt

    @tgt.setter
    def tgt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__tgt", None)
        self.__tgt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    setattr(item, "Transition8", self)
                    

    @property
    def State19(self):
        return self.__State19

    @State19.setter
    def State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__State19", None)
        self.__State19 = value
        
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
    def ownedStates(self):
        return self.__ownedStates

    @ownedStates.setter
    def ownedStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__ownedStates", None)
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
    def src(self):
        return self.__src

    @src.setter
    def src(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__src", None)
        self.__src = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition10"):
                    opp_val = getattr(item, "Transition10", None)
                    
                    setattr(item, "Transition10", self)
                    

    @property
    def model_State(self):
        return self.__model_State

    @model_State.setter
    def model_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_State__model_State", None)
        self.__model_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FSM"):
                opp_val = getattr(old_value, "model_FSM", None)
                if opp_val == self:
                    setattr(old_value, "model_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FSM"):
                opp_val = getattr(value, "model_FSM", None)
                setattr(value, "model_FSM", self)

class model_FSM:

    def __init__(self, name: str, fsm: set["model_State"] = None, fsm2: set["model_Transition"] = None, outgoingFSM: "model_Buffer" = None, FSM15: "model_Buffer" = None, incomingFSM: "model_Buffer" = None, model_FSM: "model_State" = None, FSM: "model_State" = None, FSM13: "model_Buffer" = None, FSM21: "model_Transition" = None, model_FSM23: "model_System" = None):
        self.name = name
        self.fsm = fsm if fsm is not None else set()
        self.fsm2 = fsm2 if fsm2 is not None else set()
        self.outgoingFSM = outgoingFSM
        self.FSM15 = FSM15
        self.incomingFSM = incomingFSM
        self.model_FSM = model_FSM
        self.FSM = FSM
        self.FSM13 = FSM13
        self.FSM21 = FSM21
        self.model_FSM23 = model_FSM23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def incomingFSM(self):
        return self.__incomingFSM

    @incomingFSM.setter
    def incomingFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__incomingFSM", None)
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
    def model_FSM23(self):
        return self.__model_FSM23

    @model_FSM23.setter
    def model_FSM23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__model_FSM23", None)
        self.__model_FSM23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_System"):
                opp_val = getattr(old_value, "model_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_System"):
                opp_val = getattr(value, "model_System", None)
                if opp_val is None:
                    setattr(value, "model_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FSM(self):
        return self.__FSM

    @FSM.setter
    def FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__FSM", None)
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
        old_value = getattr(self, f"_model_FSM__fsm2", None)
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
    def FSM15(self):
        return self.__FSM15

    @FSM15.setter
    def FSM15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__FSM15", None)
        self.__FSM15 = value
        
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
    def model_FSM(self):
        return self.__model_FSM

    @model_FSM.setter
    def model_FSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__model_FSM", None)
        self.__model_FSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_State"):
                opp_val = getattr(old_value, "model_State", None)
                if opp_val == self:
                    setattr(old_value, "model_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_State"):
                opp_val = getattr(value, "model_State", None)
                setattr(value, "model_State", self)

    @property
    def outgoingFSM(self):
        return self.__outgoingFSM

    @outgoingFSM.setter
    def outgoingFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__outgoingFSM", None)
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
    def FSM21(self):
        return self.__FSM21

    @FSM21.setter
    def FSM21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__FSM21", None)
        self.__FSM21 = value
        
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
    def FSM13(self):
        return self.__FSM13

    @FSM13.setter
    def FSM13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__FSM13", None)
        self.__FSM13 = value
        
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
    def fsm(self):
        return self.__fsm

    @fsm.setter
    def fsm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FSM__fsm", None)
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
                    

    def run(self):
        # TODO: Implement run method
        pass
