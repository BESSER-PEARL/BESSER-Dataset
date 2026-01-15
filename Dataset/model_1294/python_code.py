from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudoStateKind(Enum):
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
    initial = "initial"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"


############################################
# Definition of Classes
############################################

class State:

    pass
class StateMachine_FinalState(State):

    pass
class StateMachine_Transition:

    def __init__(self, kind: str, name: str, Transition: "StateMachine_Vertex" = None, Transition21: "StateMachine_Vertex" = None, StateMachine_Transition: "StateMachine_Region" = None, outgoing: "StateMachine_Vertex" = None, incoming: "StateMachine_Vertex" = None, StateMachine_Transition33: "StateMachine_Behavior" = None, StateMachine_Transition36: set["StateMachine_Trigger"] = None, StateMachine_Transition39: "StateMachine_Constraint" = None):
        self.kind = kind
        self.name = name
        self.Transition = Transition
        self.Transition21 = Transition21
        self.StateMachine_Transition = StateMachine_Transition
        self.outgoing = outgoing
        self.incoming = incoming
        self.StateMachine_Transition33 = StateMachine_Transition33
        self.StateMachine_Transition36 = StateMachine_Transition36 if StateMachine_Transition36 is not None else set()
        self.StateMachine_Transition39 = StateMachine_Transition39
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex31"):
                opp_val = getattr(old_value, "Vertex31", None)
                if opp_val == self:
                    setattr(old_value, "Vertex31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex31"):
                opp_val = getattr(value, "Vertex31", None)
                setattr(value, "Vertex31", self)

    @property
    def Transition21(self):
        return self.__Transition21

    @Transition21.setter
    def Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__Transition21", None)
        self.__Transition21 = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex"):
                opp_val = getattr(old_value, "Vertex", None)
                if opp_val == self:
                    setattr(old_value, "Vertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex"):
                opp_val = getattr(value, "Vertex", None)
                setattr(value, "Vertex", self)

    @property
    def StateMachine_Transition(self):
        return self.__StateMachine_Transition

    @StateMachine_Transition.setter
    def StateMachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition", None)
        self.__StateMachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Region25"):
                opp_val = getattr(old_value, "StateMachine_Region25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Region25"):
                opp_val = getattr(value, "StateMachine_Region25", None)
                if opp_val is None:
                    setattr(value, "StateMachine_Region25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Transition39(self):
        return self.__StateMachine_Transition39

    @StateMachine_Transition39.setter
    def StateMachine_Transition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition39", None)
        self.__StateMachine_Transition39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Constraint40"):
                opp_val = getattr(old_value, "StateMachine_Constraint40", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Constraint40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Constraint40"):
                opp_val = getattr(value, "StateMachine_Constraint40", None)
                setattr(value, "StateMachine_Constraint40", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__Transition", None)
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
    def StateMachine_Transition33(self):
        return self.__StateMachine_Transition33

    @StateMachine_Transition33.setter
    def StateMachine_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition33", None)
        self.__StateMachine_Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Behavior34"):
                opp_val = getattr(old_value, "StateMachine_Behavior34", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Behavior34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Behavior34"):
                opp_val = getattr(value, "StateMachine_Behavior34", None)
                setattr(value, "StateMachine_Behavior34", self)

    @property
    def StateMachine_Transition36(self):
        return self.__StateMachine_Transition36

    @StateMachine_Transition36.setter
    def StateMachine_Transition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Transition__StateMachine_Transition36", None)
        self.__StateMachine_Transition36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Trigger37"):
                    opp_val = getattr(item, "StateMachine_Trigger37", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Trigger37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Trigger37"):
                    opp_val = getattr(item, "StateMachine_Trigger37", None)
                    
                    setattr(item, "StateMachine_Trigger37", self)
                    

class StateMachine_Vertex:

    def __init__(self, name: str, source: set["StateMachine_Transition"] = None, target: set["StateMachine_Transition"] = None, StateMachine_Vertex: "StateMachine_Region" = None, Vertex: "StateMachine_Transition" = None, Vertex31: "StateMachine_Transition" = None):
        self.name = name
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.StateMachine_Vertex = StateMachine_Vertex
        self.Vertex = Vertex
        self.Vertex31 = Vertex31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachine_Vertex(self):
        return self.__StateMachine_Vertex

    @StateMachine_Vertex.setter
    def StateMachine_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Vertex__StateMachine_Vertex", None)
        self.__StateMachine_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Region23"):
                opp_val = getattr(old_value, "StateMachine_Region23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Region23"):
                opp_val = getattr(value, "StateMachine_Region23", None)
                if opp_val is None:
                    setattr(value, "StateMachine_Region23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Vertex31(self):
        return self.__Vertex31

    @Vertex31.setter
    def Vertex31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Vertex__Vertex31", None)
        self.__Vertex31 = value
        
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Vertex__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition21"):
                    opp_val = getattr(item, "Transition21", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition21"):
                    opp_val = getattr(item, "Transition21", None)
                    
                    setattr(item, "Transition21", self)
                    

    @property
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Vertex__Vertex", None)
        self.__Vertex = value
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Vertex__source", None)
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
                    

class Behavior:

    pass
class StateMachine_CodeBlock(Behavior):

    def __init__(self, desc: str):
        self.desc = desc
        
    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

class StateMachine_Constraint:

    def __init__(self, constraint: str, StateMachine_Constraint: "StateMachine_State" = None, StateMachine_Constraint40: "StateMachine_Transition" = None):
        self.constraint = constraint
        self.StateMachine_Constraint = StateMachine_Constraint
        self.StateMachine_Constraint40 = StateMachine_Constraint40
        
    @property
    def constraint(self) -> str:
        return self.__constraint

    @constraint.setter
    def constraint(self, constraint: str):
        self.__constraint = constraint

    @property
    def StateMachine_Constraint(self):
        return self.__StateMachine_Constraint

    @StateMachine_Constraint.setter
    def StateMachine_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Constraint__StateMachine_Constraint", None)
        self.__StateMachine_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State6"):
                opp_val = getattr(old_value, "StateMachine_State6", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State6"):
                opp_val = getattr(value, "StateMachine_State6", None)
                setattr(value, "StateMachine_State6", self)

    @property
    def StateMachine_Constraint40(self):
        return self.__StateMachine_Constraint40

    @StateMachine_Constraint40.setter
    def StateMachine_Constraint40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Constraint__StateMachine_Constraint40", None)
        self.__StateMachine_Constraint40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Transition39"):
                opp_val = getattr(old_value, "StateMachine_Transition39", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Transition39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Transition39"):
                opp_val = getattr(value, "StateMachine_Transition39", None)
                setattr(value, "StateMachine_Transition39", self)

class StateMachine_Trigger:

    def __init__(self, trigger: str, StateMachine_Trigger: "StateMachine_State" = None, StateMachine_Trigger37: "StateMachine_Transition" = None):
        self.trigger = trigger
        self.StateMachine_Trigger = StateMachine_Trigger
        self.StateMachine_Trigger37 = StateMachine_Trigger37
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def StateMachine_Trigger(self):
        return self.__StateMachine_Trigger

    @StateMachine_Trigger.setter
    def StateMachine_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Trigger__StateMachine_Trigger", None)
        self.__StateMachine_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State4"):
                opp_val = getattr(old_value, "StateMachine_State4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State4"):
                opp_val = getattr(value, "StateMachine_State4", None)
                if opp_val is None:
                    setattr(value, "StateMachine_State4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Trigger37(self):
        return self.__StateMachine_Trigger37

    @StateMachine_Trigger37.setter
    def StateMachine_Trigger37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Trigger__StateMachine_Trigger37", None)
        self.__StateMachine_Trigger37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Transition36"):
                opp_val = getattr(old_value, "StateMachine_Transition36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Transition36"):
                opp_val = getattr(value, "StateMachine_Transition36", None)
                if opp_val is None:
                    setattr(value, "StateMachine_Transition36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachine_Behavior:

    pass
class StateMachine_Region:

    def __init__(self, name: str, StateMachine_Region: "StateMachine_State" = None, StateMachine_Region27: "StateMachine_StateMachine" = None, StateMachine_Region23: set["StateMachine_Vertex"] = None, StateMachine_Region25: set["StateMachine_Transition"] = None):
        self.name = name
        self.StateMachine_Region = StateMachine_Region
        self.StateMachine_Region27 = StateMachine_Region27
        self.StateMachine_Region23 = StateMachine_Region23 if StateMachine_Region23 is not None else set()
        self.StateMachine_Region25 = StateMachine_Region25 if StateMachine_Region25 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachine_Region23(self):
        return self.__StateMachine_Region23

    @StateMachine_Region23.setter
    def StateMachine_Region23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Region__StateMachine_Region23", None)
        self.__StateMachine_Region23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Vertex"):
                    opp_val = getattr(item, "StateMachine_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Vertex"):
                    opp_val = getattr(item, "StateMachine_Vertex", None)
                    
                    setattr(item, "StateMachine_Vertex", self)
                    

    @property
    def StateMachine_Region(self):
        return self.__StateMachine_Region

    @StateMachine_Region.setter
    def StateMachine_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Region__StateMachine_Region", None)
        self.__StateMachine_Region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State"):
                opp_val = getattr(old_value, "StateMachine_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State"):
                opp_val = getattr(value, "StateMachine_State", None)
                if opp_val is None:
                    setattr(value, "StateMachine_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Region27(self):
        return self.__StateMachine_Region27

    @StateMachine_Region27.setter
    def StateMachine_Region27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Region__StateMachine_Region27", None)
        self.__StateMachine_Region27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_StateMachine"):
                opp_val = getattr(old_value, "StateMachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_StateMachine"):
                opp_val = getattr(value, "StateMachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "StateMachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_Region25(self):
        return self.__StateMachine_Region25

    @StateMachine_Region25.setter
    def StateMachine_Region25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_Region__StateMachine_Region25", None)
        self.__StateMachine_Region25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Transition"):
                    opp_val = getattr(item, "StateMachine_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Transition"):
                    opp_val = getattr(item, "StateMachine_Transition", None)
                    
                    setattr(item, "StateMachine_Transition", self)
                    

class Vertex:

    pass
class StateMachine_PseudoState(Vertex):

    def __init__(self, pseudoStateKind: str, returnValue: str, StateMachine_PseudoState: "StateMachine_State" = None, StateMachine_PseudoState18: "StateMachine_State" = None):
        self.pseudoStateKind = pseudoStateKind
        self.returnValue = returnValue
        self.StateMachine_PseudoState = StateMachine_PseudoState
        self.StateMachine_PseudoState18 = StateMachine_PseudoState18
        
    @property
    def returnValue(self) -> str:
        return self.__returnValue

    @returnValue.setter
    def returnValue(self, returnValue: str):
        self.__returnValue = returnValue

    @property
    def pseudoStateKind(self) -> str:
        return self.__pseudoStateKind

    @pseudoStateKind.setter
    def pseudoStateKind(self, pseudoStateKind: str):
        self.__pseudoStateKind = pseudoStateKind

    @property
    def StateMachine_PseudoState(self):
        return self.__StateMachine_PseudoState

    @StateMachine_PseudoState.setter
    def StateMachine_PseudoState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_PseudoState__StateMachine_PseudoState", None)
        self.__StateMachine_PseudoState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State15"):
                opp_val = getattr(old_value, "StateMachine_State15", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State15"):
                opp_val = getattr(value, "StateMachine_State15", None)
                setattr(value, "StateMachine_State15", self)

    @property
    def StateMachine_PseudoState18(self):
        return self.__StateMachine_PseudoState18

    @StateMachine_PseudoState18.setter
    def StateMachine_PseudoState18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_PseudoState__StateMachine_PseudoState18", None)
        self.__StateMachine_PseudoState18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_State17"):
                opp_val = getattr(old_value, "StateMachine_State17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_State17"):
                opp_val = getattr(value, "StateMachine_State17", None)
                if opp_val is None:
                    setattr(value, "StateMachine_State17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StateMachine_State(Vertex):

    def __init__(self, isComposite: str, isSimple: str, isSubmachineState: str, submachineState: "StateMachine_StateMachine" = None, StateMachine_State: set["StateMachine_Region"] = None, StateMachine_State2: "StateMachine_Behavior" = None, StateMachine_State4: set["StateMachine_Trigger"] = None, StateMachine_State6: "StateMachine_Constraint" = None, StateMachine_State8: "StateMachine_Behavior" = None, StateMachine_State11: "StateMachine_Behavior" = None, StateMachine_State15: "StateMachine_PseudoState" = None, State: "StateMachine_StateMachine" = None, StateMachine_State17: set["StateMachine_PseudoState"] = None):
        self.isComposite = isComposite
        self.isSimple = isSimple
        self.isSubmachineState = isSubmachineState
        self.submachineState = submachineState
        self.StateMachine_State = StateMachine_State if StateMachine_State is not None else set()
        self.StateMachine_State2 = StateMachine_State2
        self.StateMachine_State4 = StateMachine_State4 if StateMachine_State4 is not None else set()
        self.StateMachine_State6 = StateMachine_State6
        self.StateMachine_State8 = StateMachine_State8
        self.StateMachine_State11 = StateMachine_State11
        self.StateMachine_State15 = StateMachine_State15
        self.State = State
        self.StateMachine_State17 = StateMachine_State17 if StateMachine_State17 is not None else set()
        
    @property
    def isSimple(self) -> str:
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: str):
        self.__isSimple = isSimple

    @property
    def isSubmachineState(self) -> str:
        return self.__isSubmachineState

    @isSubmachineState.setter
    def isSubmachineState(self, isSubmachineState: str):
        self.__isSubmachineState = isSubmachineState

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def StateMachine_State11(self):
        return self.__StateMachine_State11

    @StateMachine_State11.setter
    def StateMachine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State11", None)
        self.__StateMachine_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Behavior12"):
                opp_val = getattr(old_value, "StateMachine_Behavior12", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Behavior12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Behavior12"):
                opp_val = getattr(value, "StateMachine_Behavior12", None)
                setattr(value, "StateMachine_Behavior12", self)

    @property
    def StateMachine_State2(self):
        return self.__StateMachine_State2

    @StateMachine_State2.setter
    def StateMachine_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State2", None)
        self.__StateMachine_State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Behavior"):
                opp_val = getattr(old_value, "StateMachine_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Behavior"):
                opp_val = getattr(value, "StateMachine_Behavior", None)
                setattr(value, "StateMachine_Behavior", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "submachine"):
                opp_val = getattr(old_value, "submachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "submachine"):
                opp_val = getattr(value, "submachine", None)
                if opp_val is None:
                    setattr(value, "submachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StateMachine_State8(self):
        return self.__StateMachine_State8

    @StateMachine_State8.setter
    def StateMachine_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State8", None)
        self.__StateMachine_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Behavior9"):
                opp_val = getattr(old_value, "StateMachine_Behavior9", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Behavior9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Behavior9"):
                opp_val = getattr(value, "StateMachine_Behavior9", None)
                setattr(value, "StateMachine_Behavior9", self)

    @property
    def submachineState(self):
        return self.__submachineState

    @submachineState.setter
    def submachineState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__submachineState", None)
        self.__submachineState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    @property
    def StateMachine_State(self):
        return self.__StateMachine_State

    @StateMachine_State.setter
    def StateMachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State", None)
        self.__StateMachine_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Region"):
                    opp_val = getattr(item, "StateMachine_Region", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Region"):
                    opp_val = getattr(item, "StateMachine_Region", None)
                    
                    setattr(item, "StateMachine_Region", self)
                    

    @property
    def StateMachine_State6(self):
        return self.__StateMachine_State6

    @StateMachine_State6.setter
    def StateMachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State6", None)
        self.__StateMachine_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_Constraint"):
                opp_val = getattr(old_value, "StateMachine_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_Constraint"):
                opp_val = getattr(value, "StateMachine_Constraint", None)
                setattr(value, "StateMachine_Constraint", self)

    @property
    def StateMachine_State4(self):
        return self.__StateMachine_State4

    @StateMachine_State4.setter
    def StateMachine_State4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State4", None)
        self.__StateMachine_State4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Trigger"):
                    opp_val = getattr(item, "StateMachine_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Trigger"):
                    opp_val = getattr(item, "StateMachine_Trigger", None)
                    
                    setattr(item, "StateMachine_Trigger", self)
                    

    @property
    def StateMachine_State17(self):
        return self.__StateMachine_State17

    @StateMachine_State17.setter
    def StateMachine_State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State17", None)
        self.__StateMachine_State17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_PseudoState18"):
                    opp_val = getattr(item, "StateMachine_PseudoState18", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_PseudoState18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_PseudoState18"):
                    opp_val = getattr(item, "StateMachine_PseudoState18", None)
                    
                    setattr(item, "StateMachine_PseudoState18", self)
                    

    @property
    def StateMachine_State15(self):
        return self.__StateMachine_State15

    @StateMachine_State15.setter
    def StateMachine_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_State__StateMachine_State15", None)
        self.__StateMachine_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine_PseudoState"):
                opp_val = getattr(old_value, "StateMachine_PseudoState", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine_PseudoState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine_PseudoState"):
                opp_val = getattr(value, "StateMachine_PseudoState", None)
                setattr(value, "StateMachine_PseudoState", self)

class StateMachine_StateMachine(Behavior):

    def __init__(self, name: str, StateMachine: "StateMachine_State" = None, StateMachine_StateMachine: set["StateMachine_Region"] = None, submachine: set["StateMachine_State"] = None):
        self.name = name
        self.StateMachine = StateMachine
        self.StateMachine_StateMachine = StateMachine_StateMachine if StateMachine_StateMachine is not None else set()
        self.submachine = submachine if submachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachine_StateMachine(self):
        return self.__StateMachine_StateMachine

    @StateMachine_StateMachine.setter
    def StateMachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_StateMachine__StateMachine_StateMachine", None)
        self.__StateMachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine_Region27"):
                    opp_val = getattr(item, "StateMachine_Region27", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine_Region27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine_Region27"):
                    opp_val = getattr(item, "StateMachine_Region27", None)
                    
                    setattr(item, "StateMachine_Region27", self)
                    

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "submachineState"):
                opp_val = getattr(old_value, "submachineState", None)
                if opp_val == self:
                    setattr(old_value, "submachineState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "submachineState"):
                opp_val = getattr(value, "submachineState", None)
                setattr(value, "submachineState", self)

    @property
    def submachine(self):
        return self.__submachine

    @submachine.setter
    def submachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StateMachine_StateMachine__submachine", None)
        self.__submachine = value if value is not None else set()
        
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
                    
