from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simpleStateMachineMetaModel_Transition:

    def __init__(self, Name: str, Transition: "simpleStateMachineMetaModel_SimpleStateMachine" = None, Outgoing: "simpleStateMachineMetaModel_State" = None, Incoming: "simpleStateMachineMetaModel_State" = None, Transition13: "simpleStateMachineMetaModel_State" = None, Transition15: "simpleStateMachineMetaModel_State" = None, Transitions: "simpleStateMachineMetaModel_SimpleStateMachine" = None):
        self.Name = Name
        self.Transition = Transition
        self.Outgoing = Outgoing
        self.Incoming = Incoming
        self.Transition13 = Transition13
        self.Transition15 = Transition15
        self.Transitions = Transitions
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Incoming(self):
        return self.__Incoming

    @Incoming.setter
    def Incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_Transition__Incoming", None)
        self.__Incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State9"):
                opp_val = getattr(old_value, "State9", None)
                if opp_val == self:
                    setattr(old_value, "State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State9"):
                opp_val = getattr(value, "State9", None)
                setattr(value, "State9", self)

    @property
    def Transitions(self):
        return self.__Transitions

    @Transitions.setter
    def Transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_Transition__Transitions", None)
        self.__Transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleStateMachine5"):
                opp_val = getattr(old_value, "SimpleStateMachine5", None)
                if opp_val == self:
                    setattr(old_value, "SimpleStateMachine5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleStateMachine5"):
                opp_val = getattr(value, "SimpleStateMachine5", None)
                setattr(value, "SimpleStateMachine5", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleStateMachine2"):
                opp_val = getattr(old_value, "SimpleStateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleStateMachine2"):
                opp_val = getattr(value, "SimpleStateMachine2", None)
                if opp_val is None:
                    setattr(value, "SimpleStateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Outgoing(self):
        return self.__Outgoing

    @Outgoing.setter
    def Outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_Transition__Outgoing", None)
        self.__Outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State7"):
                opp_val = getattr(old_value, "State7", None)
                if opp_val == self:
                    setattr(old_value, "State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State7"):
                opp_val = getattr(value, "State7", None)
                setattr(value, "State7", self)

    @property
    def Transition13(self):
        return self.__Transition13

    @Transition13.setter
    def Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_Transition__Transition13", None)
        self.__Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Source"):
                opp_val = getattr(old_value, "Source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Source"):
                opp_val = getattr(value, "Source", None)
                if opp_val is None:
                    setattr(value, "Source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition15(self):
        return self.__Transition15

    @Transition15.setter
    def Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_Transition__Transition15", None)
        self.__Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Target"):
                opp_val = getattr(old_value, "Target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Target"):
                opp_val = getattr(value, "Target", None)
                if opp_val is None:
                    setattr(value, "Target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simpleStateMachineMetaModel_State:

    def __init__(self, Name: str, State: "simpleStateMachineMetaModel_SimpleStateMachine" = None, State7: "simpleStateMachineMetaModel_Transition" = None, State9: "simpleStateMachineMetaModel_Transition" = None, States: "simpleStateMachineMetaModel_SimpleStateMachine" = None, Source: set["simpleStateMachineMetaModel_Transition"] = None, Target: set["simpleStateMachineMetaModel_Transition"] = None, simpleStateMachineMetaModel_State: "simpleStateMachineMetaModel_SimpleStateMachine" = None):
        self.Name = Name
        self.State = State
        self.State7 = State7
        self.State9 = State9
        self.States = States
        self.Source = Source if Source is not None else set()
        self.Target = Target if Target is not None else set()
        self.simpleStateMachineMetaModel_State = simpleStateMachineMetaModel_State
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def States(self):
        return self.__States

    @States.setter
    def States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_State__States", None)
        self.__States = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleStateMachine11"):
                opp_val = getattr(old_value, "SimpleStateMachine11", None)
                if opp_val == self:
                    setattr(old_value, "SimpleStateMachine11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleStateMachine11"):
                opp_val = getattr(value, "SimpleStateMachine11", None)
                setattr(value, "SimpleStateMachine11", self)

    @property
    def Source(self):
        return self.__Source

    @Source.setter
    def Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_State__Source", None)
        self.__Source = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleStateMachine"):
                opp_val = getattr(old_value, "SimpleStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleStateMachine"):
                opp_val = getattr(value, "SimpleStateMachine", None)
                if opp_val is None:
                    setattr(value, "SimpleStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simpleStateMachineMetaModel_State(self):
        return self.__simpleStateMachineMetaModel_State

    @simpleStateMachineMetaModel_State.setter
    def simpleStateMachineMetaModel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_State__simpleStateMachineMetaModel_State", None)
        self.__simpleStateMachineMetaModel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleStateMachineMetaModel_SimpleStateMachine"):
                opp_val = getattr(old_value, "simpleStateMachineMetaModel_SimpleStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "simpleStateMachineMetaModel_SimpleStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleStateMachineMetaModel_SimpleStateMachine"):
                opp_val = getattr(value, "simpleStateMachineMetaModel_SimpleStateMachine", None)
                setattr(value, "simpleStateMachineMetaModel_SimpleStateMachine", self)

    @property
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_State__State9", None)
        self.__State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Incoming"):
                opp_val = getattr(old_value, "Incoming", None)
                if opp_val == self:
                    setattr(old_value, "Incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Incoming"):
                opp_val = getattr(value, "Incoming", None)
                setattr(value, "Incoming", self)

    @property
    def State7(self):
        return self.__State7

    @State7.setter
    def State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_State__State7", None)
        self.__State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Outgoing"):
                opp_val = getattr(old_value, "Outgoing", None)
                if opp_val == self:
                    setattr(old_value, "Outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Outgoing"):
                opp_val = getattr(value, "Outgoing", None)
                setattr(value, "Outgoing", self)

    @property
    def Target(self):
        return self.__Target

    @Target.setter
    def Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_State__Target", None)
        self.__Target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition15"):
                    opp_val = getattr(item, "Transition15", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition15"):
                    opp_val = getattr(item, "Transition15", None)
                    
                    setattr(item, "Transition15", self)
                    

class simpleStateMachineMetaModel_SimpleStateMachine:

    def __init__(self, Name: str, SimpleStateMachine: set["simpleStateMachineMetaModel_State"] = None, SimpleStateMachine2: set["simpleStateMachineMetaModel_Transition"] = None, SimpleStateMachine11: "simpleStateMachineMetaModel_State" = None, simpleStateMachineMetaModel_SimpleStateMachine: "simpleStateMachineMetaModel_State" = None, SimpleStateMachine5: "simpleStateMachineMetaModel_Transition" = None):
        self.Name = Name
        self.SimpleStateMachine = SimpleStateMachine if SimpleStateMachine is not None else set()
        self.SimpleStateMachine2 = SimpleStateMachine2 if SimpleStateMachine2 is not None else set()
        self.SimpleStateMachine11 = SimpleStateMachine11
        self.simpleStateMachineMetaModel_SimpleStateMachine = simpleStateMachineMetaModel_SimpleStateMachine
        self.SimpleStateMachine5 = SimpleStateMachine5
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def SimpleStateMachine(self):
        return self.__SimpleStateMachine

    @SimpleStateMachine.setter
    def SimpleStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_SimpleStateMachine__SimpleStateMachine", None)
        self.__SimpleStateMachine = value if value is not None else set()
        
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
    def simpleStateMachineMetaModel_SimpleStateMachine(self):
        return self.__simpleStateMachineMetaModel_SimpleStateMachine

    @simpleStateMachineMetaModel_SimpleStateMachine.setter
    def simpleStateMachineMetaModel_SimpleStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_SimpleStateMachine__simpleStateMachineMetaModel_SimpleStateMachine", None)
        self.__simpleStateMachineMetaModel_SimpleStateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simpleStateMachineMetaModel_State"):
                opp_val = getattr(old_value, "simpleStateMachineMetaModel_State", None)
                if opp_val == self:
                    setattr(old_value, "simpleStateMachineMetaModel_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simpleStateMachineMetaModel_State"):
                opp_val = getattr(value, "simpleStateMachineMetaModel_State", None)
                setattr(value, "simpleStateMachineMetaModel_State", self)

    @property
    def SimpleStateMachine2(self):
        return self.__SimpleStateMachine2

    @SimpleStateMachine2.setter
    def SimpleStateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_SimpleStateMachine__SimpleStateMachine2", None)
        self.__SimpleStateMachine2 = value if value is not None else set()
        
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
    def SimpleStateMachine11(self):
        return self.__SimpleStateMachine11

    @SimpleStateMachine11.setter
    def SimpleStateMachine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_SimpleStateMachine__SimpleStateMachine11", None)
        self.__SimpleStateMachine11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "States"):
                opp_val = getattr(old_value, "States", None)
                if opp_val == self:
                    setattr(old_value, "States", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "States"):
                opp_val = getattr(value, "States", None)
                setattr(value, "States", self)

    @property
    def SimpleStateMachine5(self):
        return self.__SimpleStateMachine5

    @SimpleStateMachine5.setter
    def SimpleStateMachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simpleStateMachineMetaModel_SimpleStateMachine__SimpleStateMachine5", None)
        self.__SimpleStateMachine5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transitions"):
                opp_val = getattr(old_value, "Transitions", None)
                if opp_val == self:
                    setattr(old_value, "Transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transitions"):
                opp_val = getattr(value, "Transitions", None)
                setattr(value, "Transitions", self)
