from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class complexStateMachineMetaModel_CompositeState(State):

    pass
class complexStateMachineMetaModel_ComplexStateMachine:

    def __init__(self, Name: str, ComplexStateMachine: set["complexStateMachineMetaModel_State"] = None, ComplexStateMachine2: set["complexStateMachineMetaModel_Transition"] = None, complexStateMachineMetaModel_ComplexStateMachine: "complexStateMachineMetaModel_State" = None, ComplexStateMachine5: "complexStateMachineMetaModel_Transition" = None, ComplexStateMachine11: "complexStateMachineMetaModel_State" = None):
        self.Name = Name
        self.ComplexStateMachine = ComplexStateMachine if ComplexStateMachine is not None else set()
        self.ComplexStateMachine2 = ComplexStateMachine2 if ComplexStateMachine2 is not None else set()
        self.complexStateMachineMetaModel_ComplexStateMachine = complexStateMachineMetaModel_ComplexStateMachine
        self.ComplexStateMachine5 = ComplexStateMachine5
        self.ComplexStateMachine11 = ComplexStateMachine11
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def complexStateMachineMetaModel_ComplexStateMachine(self):
        return self.__complexStateMachineMetaModel_ComplexStateMachine

    @complexStateMachineMetaModel_ComplexStateMachine.setter
    def complexStateMachineMetaModel_ComplexStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_ComplexStateMachine__complexStateMachineMetaModel_ComplexStateMachine", None)
        self.__complexStateMachineMetaModel_ComplexStateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complexStateMachineMetaModel_State"):
                opp_val = getattr(old_value, "complexStateMachineMetaModel_State", None)
                if opp_val == self:
                    setattr(old_value, "complexStateMachineMetaModel_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complexStateMachineMetaModel_State"):
                opp_val = getattr(value, "complexStateMachineMetaModel_State", None)
                setattr(value, "complexStateMachineMetaModel_State", self)

    @property
    def ComplexStateMachine(self):
        return self.__ComplexStateMachine

    @ComplexStateMachine.setter
    def ComplexStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_ComplexStateMachine__ComplexStateMachine", None)
        self.__ComplexStateMachine = value if value is not None else set()
        
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
    def ComplexStateMachine11(self):
        return self.__ComplexStateMachine11

    @ComplexStateMachine11.setter
    def ComplexStateMachine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_ComplexStateMachine__ComplexStateMachine11", None)
        self.__ComplexStateMachine11 = value
        
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
    def ComplexStateMachine2(self):
        return self.__ComplexStateMachine2

    @ComplexStateMachine2.setter
    def ComplexStateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_ComplexStateMachine__ComplexStateMachine2", None)
        self.__ComplexStateMachine2 = value if value is not None else set()
        
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
    def ComplexStateMachine5(self):
        return self.__ComplexStateMachine5

    @ComplexStateMachine5.setter
    def ComplexStateMachine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_ComplexStateMachine__ComplexStateMachine5", None)
        self.__ComplexStateMachine5 = value
        
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

class complexStateMachineMetaModel_Transition:

    def __init__(self, Name: str, Transition: "complexStateMachineMetaModel_ComplexStateMachine" = None, Transitions: "complexStateMachineMetaModel_ComplexStateMachine" = None, Outgoing: "complexStateMachineMetaModel_State" = None, Incoming: "complexStateMachineMetaModel_State" = None, Transition13: "complexStateMachineMetaModel_State" = None, Transition15: "complexStateMachineMetaModel_State" = None):
        self.Name = Name
        self.Transition = Transition
        self.Transitions = Transitions
        self.Outgoing = Outgoing
        self.Incoming = Incoming
        self.Transition13 = Transition13
        self.Transition15 = Transition15
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Transitions(self):
        return self.__Transitions

    @Transitions.setter
    def Transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_Transition__Transitions", None)
        self.__Transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComplexStateMachine5"):
                opp_val = getattr(old_value, "ComplexStateMachine5", None)
                if opp_val == self:
                    setattr(old_value, "ComplexStateMachine5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComplexStateMachine5"):
                opp_val = getattr(value, "ComplexStateMachine5", None)
                setattr(value, "ComplexStateMachine5", self)

    @property
    def Transition13(self):
        return self.__Transition13

    @Transition13.setter
    def Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_Transition__Transition13", None)
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
    def Outgoing(self):
        return self.__Outgoing

    @Outgoing.setter
    def Outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_Transition__Outgoing", None)
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
    def Transition15(self):
        return self.__Transition15

    @Transition15.setter
    def Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_Transition__Transition15", None)
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

    @property
    def Incoming(self):
        return self.__Incoming

    @Incoming.setter
    def Incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_Transition__Incoming", None)
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComplexStateMachine2"):
                opp_val = getattr(old_value, "ComplexStateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComplexStateMachine2"):
                opp_val = getattr(value, "ComplexStateMachine2", None)
                if opp_val is None:
                    setattr(value, "ComplexStateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class complexStateMachineMetaModel_State:

    def __init__(self, Name: str, State: "complexStateMachineMetaModel_ComplexStateMachine" = None, complexStateMachineMetaModel_State: "complexStateMachineMetaModel_ComplexStateMachine" = None, State7: "complexStateMachineMetaModel_Transition" = None, State9: "complexStateMachineMetaModel_Transition" = None, States: "complexStateMachineMetaModel_ComplexStateMachine" = None, Source: set["complexStateMachineMetaModel_Transition"] = None, Target: set["complexStateMachineMetaModel_Transition"] = None, States17: "complexStateMachineMetaModel_CompositeState" = None, State20: "complexStateMachineMetaModel_CompositeState" = None, complexStateMachineMetaModel_State22: "complexStateMachineMetaModel_CompositeState" = None):
        self.Name = Name
        self.State = State
        self.complexStateMachineMetaModel_State = complexStateMachineMetaModel_State
        self.State7 = State7
        self.State9 = State9
        self.States = States
        self.Source = Source if Source is not None else set()
        self.Target = Target if Target is not None else set()
        self.States17 = States17
        self.State20 = State20
        self.complexStateMachineMetaModel_State22 = complexStateMachineMetaModel_State22
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def State9(self):
        return self.__State9

    @State9.setter
    def State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__State9", None)
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComplexStateMachine"):
                opp_val = getattr(old_value, "ComplexStateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComplexStateMachine"):
                opp_val = getattr(value, "ComplexStateMachine", None)
                if opp_val is None:
                    setattr(value, "ComplexStateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def complexStateMachineMetaModel_State(self):
        return self.__complexStateMachineMetaModel_State

    @complexStateMachineMetaModel_State.setter
    def complexStateMachineMetaModel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__complexStateMachineMetaModel_State", None)
        self.__complexStateMachineMetaModel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complexStateMachineMetaModel_ComplexStateMachine"):
                opp_val = getattr(old_value, "complexStateMachineMetaModel_ComplexStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "complexStateMachineMetaModel_ComplexStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complexStateMachineMetaModel_ComplexStateMachine"):
                opp_val = getattr(value, "complexStateMachineMetaModel_ComplexStateMachine", None)
                setattr(value, "complexStateMachineMetaModel_ComplexStateMachine", self)

    @property
    def State7(self):
        return self.__State7

    @State7.setter
    def State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__State7", None)
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
    def States(self):
        return self.__States

    @States.setter
    def States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__States", None)
        self.__States = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComplexStateMachine11"):
                opp_val = getattr(old_value, "ComplexStateMachine11", None)
                if opp_val == self:
                    setattr(old_value, "ComplexStateMachine11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComplexStateMachine11"):
                opp_val = getattr(value, "ComplexStateMachine11", None)
                setattr(value, "ComplexStateMachine11", self)

    @property
    def Source(self):
        return self.__Source

    @Source.setter
    def Source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__Source", None)
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
    def States17(self):
        return self.__States17

    @States17.setter
    def States17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__States17", None)
        self.__States17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeState"):
                opp_val = getattr(old_value, "CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeState"):
                opp_val = getattr(value, "CompositeState", None)
                setattr(value, "CompositeState", self)

    @property
    def complexStateMachineMetaModel_State22(self):
        return self.__complexStateMachineMetaModel_State22

    @complexStateMachineMetaModel_State22.setter
    def complexStateMachineMetaModel_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__complexStateMachineMetaModel_State22", None)
        self.__complexStateMachineMetaModel_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "complexStateMachineMetaModel_CompositeState"):
                opp_val = getattr(old_value, "complexStateMachineMetaModel_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "complexStateMachineMetaModel_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "complexStateMachineMetaModel_CompositeState"):
                opp_val = getattr(value, "complexStateMachineMetaModel_CompositeState", None)
                setattr(value, "complexStateMachineMetaModel_CompositeState", self)

    @property
    def State20(self):
        return self.__State20

    @State20.setter
    def State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__State20", None)
        self.__State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeState19"):
                opp_val = getattr(old_value, "CompositeState19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeState19"):
                opp_val = getattr(value, "CompositeState19", None)
                if opp_val is None:
                    setattr(value, "CompositeState19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Target(self):
        return self.__Target

    @Target.setter
    def Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_complexStateMachineMetaModel_State__Target", None)
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
                    
