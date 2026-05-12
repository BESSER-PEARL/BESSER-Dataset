from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simplefsm_State:

    def __init__(self, name: str, action: str, owningState: set["simplefsm_Transition"] = None, states: "simplefsm_SimpleFiniteStateMachine" = None, State: "simplefsm_SimpleFiniteStateMachine" = None, simplefsm_State: "simplefsm_Transition" = None, State5: "simplefsm_Transition" = None):
        self.name = name
        self.action = action
        self.owningState = owningState if owningState is not None else set()
        self.states = states
        self.State = State
        self.simplefsm_State = simplefsm_State
        self.State5 = State5
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def State5(self):
        return self.__State5

    @State5.setter
    def State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__State5", None)
        self.__State5 = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__State", None)
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
    def owningState(self):
        return self.__owningState

    @owningState.setter
    def owningState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__owningState", None)
        self.__owningState = value if value is not None else set()
        
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
    def simplefsm_State(self):
        return self.__simplefsm_State

    @simplefsm_State.setter
    def simplefsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__simplefsm_State", None)
        self.__simplefsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplefsm_Transition"):
                opp_val = getattr(old_value, "simplefsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "simplefsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplefsm_Transition"):
                opp_val = getattr(value, "simplefsm_Transition", None)
                setattr(value, "simplefsm_Transition", self)

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleFiniteStateMachine"):
                opp_val = getattr(old_value, "SimpleFiniteStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "SimpleFiniteStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleFiniteStateMachine"):
                opp_val = getattr(value, "SimpleFiniteStateMachine", None)
                setattr(value, "SimpleFiniteStateMachine", self)

class simplefsm_SimpleFiniteStateMachine:

    def __init__(self, name: str, SimpleFiniteStateMachine: "simplefsm_State" = None, owningFSM: set["simplefsm_State"] = None):
        self.name = name
        self.SimpleFiniteStateMachine = SimpleFiniteStateMachine
        self.owningFSM = owningFSM if owningFSM is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def SimpleFiniteStateMachine(self):
        return self.__SimpleFiniteStateMachine

    @SimpleFiniteStateMachine.setter
    def SimpleFiniteStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_SimpleFiniteStateMachine__SimpleFiniteStateMachine", None)
        self.__SimpleFiniteStateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "states"):
                opp_val = getattr(old_value, "states", None)
                if opp_val == self:
                    setattr(old_value, "states", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "states"):
                opp_val = getattr(value, "states", None)
                setattr(value, "states", self)

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_SimpleFiniteStateMachine__owningFSM", None)
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
                    

class simplefsm_Transition:

    def __init__(self, name: str, event: str, Transition: "simplefsm_State" = None, simplefsm_Transition: "simplefsm_State" = None, outgoingTransitions: "simplefsm_State" = None):
        self.name = name
        self.event = event
        self.Transition = Transition
        self.simplefsm_Transition = simplefsm_Transition
        self.outgoingTransitions = outgoingTransitions
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event


    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningState"):
                opp_val = getattr(old_value, "owningState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningState"):
                opp_val = getattr(value, "owningState", None)
                if opp_val is None:
                    setattr(value, "owningState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplefsm_Transition(self):
        return self.__simplefsm_Transition

    @simplefsm_Transition.setter
    def simplefsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_Transition__simplefsm_Transition", None)
        self.__simplefsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplefsm_State"):
                opp_val = getattr(old_value, "simplefsm_State", None)
                if opp_val == self:
                    setattr(old_value, "simplefsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplefsm_State"):
                opp_val = getattr(value, "simplefsm_State", None)
                setattr(value, "simplefsm_State", self)

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplefsm_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State5"):
                opp_val = getattr(old_value, "State5", None)
                if opp_val == self:
                    setattr(old_value, "State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State5"):
                opp_val = getattr(value, "State5", None)
                setattr(value, "State5", self)
