from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Thing:

    pass
class simple200_Variable(Thing):

    def __init__(self, type: str, value: str, simple200_Variable: "simple200_State" = None):
        self.type = type
        self.value = value
        self.simple200_Variable = simple200_Variable
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def simple200_Variable(self):
        return self.__simple200_Variable

    @simple200_Variable.setter
    def simple200_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_Variable__simple200_Variable", None)
        self.__simple200_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_State12"):
                opp_val = getattr(old_value, "simple200_State12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_State12"):
                opp_val = getattr(value, "simple200_State12", None)
                if opp_val is None:
                    setattr(value, "simple200_State12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simple200_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class simple200_State(NamedElement):

    def __init__(self, label: str, type: str, activity: str, simple200_State7: "simple200_State" = None, simple200_State5: set["simple200_State"] = None, simple200_State10: "simple200_State" = None, simple200_State8: "simple200_State" = None, simple200_State12: set["simple200_Variable"] = None, source: set["simple200_Transition"] = None, State: "simple200_Transition" = None, simple200_State: "simple200_Transition" = None):
        self.label = label
        self.type = type
        self.activity = activity
        self.simple200_State7 = simple200_State7
        self.simple200_State5 = simple200_State5 if simple200_State5 is not None else set()
        self.simple200_State10 = simple200_State10
        self.simple200_State8 = simple200_State8
        self.simple200_State12 = simple200_State12 if simple200_State12 is not None else set()
        self.source = source if source is not None else set()
        self.State = State
        self.simple200_State = simple200_State
        
    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def simple200_State7(self):
        return self.__simple200_State7

    @simple200_State7.setter
    def simple200_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__simple200_State7", None)
        self.__simple200_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_State5"):
                opp_val = getattr(old_value, "simple200_State5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_State5"):
                opp_val = getattr(value, "simple200_State5", None)
                if opp_val is None:
                    setattr(value, "simple200_State5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def simple200_State12(self):
        return self.__simple200_State12

    @simple200_State12.setter
    def simple200_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__simple200_State12", None)
        self.__simple200_State12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simple200_Variable"):
                    opp_val = getattr(item, "simple200_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "simple200_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simple200_Variable"):
                    opp_val = getattr(item, "simple200_Variable", None)
                    
                    setattr(item, "simple200_Variable", self)
                    

    @property
    def simple200_State(self):
        return self.__simple200_State

    @simple200_State.setter
    def simple200_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__simple200_State", None)
        self.__simple200_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_Transition"):
                opp_val = getattr(old_value, "simple200_Transition", None)
                if opp_val == self:
                    setattr(old_value, "simple200_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_Transition"):
                opp_val = getattr(value, "simple200_Transition", None)
                setattr(value, "simple200_Transition", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__source", None)
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
    def simple200_State5(self):
        return self.__simple200_State5

    @simple200_State5.setter
    def simple200_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__simple200_State5", None)
        self.__simple200_State5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simple200_State7"):
                    opp_val = getattr(item, "simple200_State7", None)
                    
                    if opp_val == self:
                        setattr(item, "simple200_State7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simple200_State7"):
                    opp_val = getattr(item, "simple200_State7", None)
                    
                    setattr(item, "simple200_State7", self)
                    

    @property
    def simple200_State10(self):
        return self.__simple200_State10

    @simple200_State10.setter
    def simple200_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__simple200_State10", None)
        self.__simple200_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_State8"):
                opp_val = getattr(old_value, "simple200_State8", None)
                if opp_val == self:
                    setattr(old_value, "simple200_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_State8"):
                opp_val = getattr(value, "simple200_State8", None)
                setattr(value, "simple200_State8", self)

    @property
    def simple200_State8(self):
        return self.__simple200_State8

    @simple200_State8.setter
    def simple200_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_State__simple200_State8", None)
        self.__simple200_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_State10"):
                opp_val = getattr(old_value, "simple200_State10", None)
                if opp_val == self:
                    setattr(old_value, "simple200_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_State10"):
                opp_val = getattr(value, "simple200_State10", None)
                setattr(value, "simple200_State10", self)

class simple200_RelatedTo(NamedElement):

    def __init__(self, since: str, relations: "simple200_Thing" = None, simple200_RelatedTo: "simple200_Thing" = None, RelatedTo: "simple200_Thing" = None):
        self.since = since
        self.relations = relations
        self.simple200_RelatedTo = simple200_RelatedTo
        self.RelatedTo = RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def simple200_RelatedTo(self):
        return self.__simple200_RelatedTo

    @simple200_RelatedTo.setter
    def simple200_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_RelatedTo__simple200_RelatedTo", None)
        self.__simple200_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_Thing"):
                opp_val = getattr(old_value, "simple200_Thing", None)
                if opp_val == self:
                    setattr(old_value, "simple200_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_Thing"):
                opp_val = getattr(value, "simple200_Thing", None)
                setattr(value, "simple200_Thing", self)

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_RelatedTo__RelatedTo", None)
        self.__RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fromThing"):
                opp_val = getattr(old_value, "fromThing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fromThing"):
                opp_val = getattr(value, "fromThing", None)
                if opp_val is None:
                    setattr(value, "fromThing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_RelatedTo__relations", None)
        self.__relations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Thing"):
                opp_val = getattr(old_value, "Thing", None)
                if opp_val == self:
                    setattr(old_value, "Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Thing"):
                opp_val = getattr(value, "Thing", None)
                setattr(value, "Thing", self)

class simple200_Transition(NamedElement):

    def __init__(self, expression: str, Transition: "simple200_State" = None, transitions: "simple200_State" = None, simple200_Transition: "simple200_State" = None):
        self.expression = expression
        self.Transition = Transition
        self.transitions = transitions
        self.simple200_Transition = simple200_Transition
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def simple200_Transition(self):
        return self.__simple200_Transition

    @simple200_Transition.setter
    def simple200_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_Transition__simple200_Transition", None)
        self.__simple200_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_State"):
                opp_val = getattr(old_value, "simple200_State", None)
                if opp_val == self:
                    setattr(old_value, "simple200_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_State"):
                opp_val = getattr(value, "simple200_State", None)
                setattr(value, "simple200_State", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_Transition__Transition", None)
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
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_Transition__transitions", None)
        self.__transitions = value
        
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

class simple200_Thing(NamedElement):

    def __init__(self, id: int, Thing: "simple200_RelatedTo" = None, simple200_Thing: "simple200_RelatedTo" = None, fromThing: set["simple200_RelatedTo"] = None):
        self.id = id
        self.Thing = Thing
        self.simple200_Thing = simple200_Thing
        self.fromThing = fromThing if fromThing is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relations"):
                opp_val = getattr(old_value, "relations", None)
                if opp_val == self:
                    setattr(old_value, "relations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relations"):
                opp_val = getattr(value, "relations", None)
                setattr(value, "relations", self)

    @property
    def simple200_Thing(self):
        return self.__simple200_Thing

    @simple200_Thing.setter
    def simple200_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_Thing__simple200_Thing", None)
        self.__simple200_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple200_RelatedTo"):
                opp_val = getattr(old_value, "simple200_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "simple200_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple200_RelatedTo"):
                opp_val = getattr(value, "simple200_RelatedTo", None)
                setattr(value, "simple200_RelatedTo", self)

    @property
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple200_Thing__fromThing", None)
        self.__fromThing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    if opp_val == self:
                        setattr(item, "RelatedTo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelatedTo"):
                    opp_val = getattr(item, "RelatedTo", None)
                    
                    setattr(item, "RelatedTo", self)
                    
