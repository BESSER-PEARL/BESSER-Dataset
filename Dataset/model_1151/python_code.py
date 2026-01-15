from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class myFirstEditorCustom_EndState(State):

    pass
class myFirstEditorCustom_StartState(State):

    pass
class myFirstEditorCustom_StateMachine:

    def __init__(self, name: str, myFirstEditorCustom_StateMachine: set["myFirstEditorCustom_State"] = None, myFirstEditorCustom_StateMachine2: set["myFirstEditorCustom_Transition"] = None):
        self.name = name
        self.myFirstEditorCustom_StateMachine = myFirstEditorCustom_StateMachine if myFirstEditorCustom_StateMachine is not None else set()
        self.myFirstEditorCustom_StateMachine2 = myFirstEditorCustom_StateMachine2 if myFirstEditorCustom_StateMachine2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myFirstEditorCustom_StateMachine2(self):
        return self.__myFirstEditorCustom_StateMachine2

    @myFirstEditorCustom_StateMachine2.setter
    def myFirstEditorCustom_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_StateMachine__myFirstEditorCustom_StateMachine2", None)
        self.__myFirstEditorCustom_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myFirstEditorCustom_Transition"):
                    opp_val = getattr(item, "myFirstEditorCustom_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "myFirstEditorCustom_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myFirstEditorCustom_Transition"):
                    opp_val = getattr(item, "myFirstEditorCustom_Transition", None)
                    
                    setattr(item, "myFirstEditorCustom_Transition", self)
                    

    @property
    def myFirstEditorCustom_StateMachine(self):
        return self.__myFirstEditorCustom_StateMachine

    @myFirstEditorCustom_StateMachine.setter
    def myFirstEditorCustom_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_StateMachine__myFirstEditorCustom_StateMachine", None)
        self.__myFirstEditorCustom_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myFirstEditorCustom_State"):
                    opp_val = getattr(item, "myFirstEditorCustom_State", None)
                    
                    if opp_val == self:
                        setattr(item, "myFirstEditorCustom_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myFirstEditorCustom_State"):
                    opp_val = getattr(item, "myFirstEditorCustom_State", None)
                    
                    setattr(item, "myFirstEditorCustom_State", self)
                    

class myFirstEditorCustom_Transition:

    def __init__(self, name: str, myFirstEditorCustom_Transition: "myFirstEditorCustom_StateMachine" = None, Transition: "myFirstEditorCustom_State" = None, Transition5: "myFirstEditorCustom_State" = None, out: "myFirstEditorCustom_State" = None, in: "myFirstEditorCustom_State" = None):
        self.name = name
        self.myFirstEditorCustom_Transition = myFirstEditorCustom_Transition
        self.Transition = Transition
        self.Transition5 = Transition5
        self.out = out
        self.in = in
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def out(self):
        return self.__out

    @out.setter
    def out(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_Transition__out", None)
        self.__out = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_Transition__Transition5", None)
        self.__Transition5 = value
        
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
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_Transition__Transition", None)
        self.__Transition = value
        
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

    @property
    def in(self):
        return self.__in

    @in.setter
    def in(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_Transition__in", None)
        self.__in = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State8"):
                opp_val = getattr(old_value, "State8", None)
                if opp_val == self:
                    setattr(old_value, "State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State8"):
                opp_val = getattr(value, "State8", None)
                setattr(value, "State8", self)

    @property
    def myFirstEditorCustom_Transition(self):
        return self.__myFirstEditorCustom_Transition

    @myFirstEditorCustom_Transition.setter
    def myFirstEditorCustom_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_Transition__myFirstEditorCustom_Transition", None)
        self.__myFirstEditorCustom_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myFirstEditorCustom_StateMachine2"):
                opp_val = getattr(old_value, "myFirstEditorCustom_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myFirstEditorCustom_StateMachine2"):
                opp_val = getattr(value, "myFirstEditorCustom_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "myFirstEditorCustom_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myFirstEditorCustom_State:

    def __init__(self, name: str, type: str, myFirstEditorCustom_State: "myFirstEditorCustom_StateMachine" = None, target: set["myFirstEditorCustom_Transition"] = None, source: set["myFirstEditorCustom_Transition"] = None, State: "myFirstEditorCustom_Transition" = None, State8: "myFirstEditorCustom_Transition" = None):
        self.name = name
        self.type = type
        self.myFirstEditorCustom_State = myFirstEditorCustom_State
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.State = State
        self.State8 = State8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def State8(self):
        return self.__State8

    @State8.setter
    def State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_State__State8", None)
        self.__State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

    @property
    def myFirstEditorCustom_State(self):
        return self.__myFirstEditorCustom_State

    @myFirstEditorCustom_State.setter
    def myFirstEditorCustom_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_State__myFirstEditorCustom_State", None)
        self.__myFirstEditorCustom_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myFirstEditorCustom_StateMachine"):
                opp_val = getattr(old_value, "myFirstEditorCustom_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myFirstEditorCustom_StateMachine"):
                opp_val = getattr(value, "myFirstEditorCustom_StateMachine", None)
                if opp_val is None:
                    setattr(value, "myFirstEditorCustom_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myFirstEditorCustom_State__target", None)
        self.__target = value if value is not None else set()
        
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
                    
