from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Thing:

    pass
class simplestatechart_Variable(Thing):

    def __init__(self, type: str, value: str, simplestatechart_Variable: "simplestatechart_State" = None):
        self.type = type
        self.value = value
        self.simplestatechart_Variable = simplestatechart_Variable
        
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
    def simplestatechart_Variable(self):
        return self.__simplestatechart_Variable

    @simplestatechart_Variable.setter
    def simplestatechart_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_Variable__simplestatechart_Variable", None)
        self.__simplestatechart_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_State14"):
                opp_val = getattr(old_value, "simplestatechart_State14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_State14"):
                opp_val = getattr(value, "simplestatechart_State14", None)
                if opp_val is None:
                    setattr(value, "simplestatechart_State14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplestatechart_NamedElement(ABC):

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
class simplestatechart_State(NamedElement):

    def __init__(self, label: str, type: str, activity: str, simplestatechart_State: "simplestatechart_Transition" = None, simplestatechart_State6: "simplestatechart_Transition" = None, simplestatechart_State9: "simplestatechart_State" = None, simplestatechart_State7: set["simplestatechart_State"] = None, simplestatechart_State14: set["simplestatechart_Variable"] = None, simplestatechart_State16: set["simplestatechart_Transition"] = None, simplestatechart_State12: "simplestatechart_State" = None, simplestatechart_State10: "simplestatechart_State" = None):
        self.label = label
        self.type = type
        self.activity = activity
        self.simplestatechart_State = simplestatechart_State
        self.simplestatechart_State6 = simplestatechart_State6
        self.simplestatechart_State9 = simplestatechart_State9
        self.simplestatechart_State7 = simplestatechart_State7 if simplestatechart_State7 is not None else set()
        self.simplestatechart_State14 = simplestatechart_State14 if simplestatechart_State14 is not None else set()
        self.simplestatechart_State16 = simplestatechart_State16 if simplestatechart_State16 is not None else set()
        self.simplestatechart_State12 = simplestatechart_State12
        self.simplestatechart_State10 = simplestatechart_State10
        
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
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def simplestatechart_State14(self):
        return self.__simplestatechart_State14

    @simplestatechart_State14.setter
    def simplestatechart_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State14", None)
        self.__simplestatechart_State14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplestatechart_Variable"):
                    opp_val = getattr(item, "simplestatechart_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "simplestatechart_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplestatechart_Variable"):
                    opp_val = getattr(item, "simplestatechart_Variable", None)
                    
                    setattr(item, "simplestatechart_Variable", self)
                    

    @property
    def simplestatechart_State10(self):
        return self.__simplestatechart_State10

    @simplestatechart_State10.setter
    def simplestatechart_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State10", None)
        self.__simplestatechart_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_State12"):
                opp_val = getattr(old_value, "simplestatechart_State12", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_State12"):
                opp_val = getattr(value, "simplestatechart_State12", None)
                setattr(value, "simplestatechart_State12", self)

    @property
    def simplestatechart_State(self):
        return self.__simplestatechart_State

    @simplestatechart_State.setter
    def simplestatechart_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State", None)
        self.__simplestatechart_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_Transition"):
                opp_val = getattr(old_value, "simplestatechart_Transition", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_Transition"):
                opp_val = getattr(value, "simplestatechart_Transition", None)
                setattr(value, "simplestatechart_Transition", self)

    @property
    def simplestatechart_State9(self):
        return self.__simplestatechart_State9

    @simplestatechart_State9.setter
    def simplestatechart_State9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State9", None)
        self.__simplestatechart_State9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_State7"):
                opp_val = getattr(old_value, "simplestatechart_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_State7"):
                opp_val = getattr(value, "simplestatechart_State7", None)
                if opp_val is None:
                    setattr(value, "simplestatechart_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplestatechart_State12(self):
        return self.__simplestatechart_State12

    @simplestatechart_State12.setter
    def simplestatechart_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State12", None)
        self.__simplestatechart_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_State10"):
                opp_val = getattr(old_value, "simplestatechart_State10", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_State10"):
                opp_val = getattr(value, "simplestatechart_State10", None)
                setattr(value, "simplestatechart_State10", self)

    @property
    def simplestatechart_State6(self):
        return self.__simplestatechart_State6

    @simplestatechart_State6.setter
    def simplestatechart_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State6", None)
        self.__simplestatechart_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_Transition5"):
                opp_val = getattr(old_value, "simplestatechart_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_Transition5"):
                opp_val = getattr(value, "simplestatechart_Transition5", None)
                setattr(value, "simplestatechart_Transition5", self)

    @property
    def simplestatechart_State7(self):
        return self.__simplestatechart_State7

    @simplestatechart_State7.setter
    def simplestatechart_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State7", None)
        self.__simplestatechart_State7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplestatechart_State9"):
                    opp_val = getattr(item, "simplestatechart_State9", None)
                    
                    if opp_val == self:
                        setattr(item, "simplestatechart_State9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplestatechart_State9"):
                    opp_val = getattr(item, "simplestatechart_State9", None)
                    
                    setattr(item, "simplestatechart_State9", self)
                    

    @property
    def simplestatechart_State16(self):
        return self.__simplestatechart_State16

    @simplestatechart_State16.setter
    def simplestatechart_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_State__simplestatechart_State16", None)
        self.__simplestatechart_State16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplestatechart_Transition17"):
                    opp_val = getattr(item, "simplestatechart_Transition17", None)
                    
                    if opp_val == self:
                        setattr(item, "simplestatechart_Transition17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplestatechart_Transition17"):
                    opp_val = getattr(item, "simplestatechart_Transition17", None)
                    
                    setattr(item, "simplestatechart_Transition17", self)
                    

class simplestatechart_RelatedTo(NamedElement):

    def __init__(self, since: str, relations: "simplestatechart_Thing" = None, simplestatechart_RelatedTo: "simplestatechart_Thing" = None, RelatedTo: "simplestatechart_Thing" = None):
        self.since = since
        self.relations = relations
        self.simplestatechart_RelatedTo = simplestatechart_RelatedTo
        self.RelatedTo = RelatedTo
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def RelatedTo(self):
        return self.__RelatedTo

    @RelatedTo.setter
    def RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_RelatedTo__RelatedTo", None)
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
    def simplestatechart_RelatedTo(self):
        return self.__simplestatechart_RelatedTo

    @simplestatechart_RelatedTo.setter
    def simplestatechart_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_RelatedTo__simplestatechart_RelatedTo", None)
        self.__simplestatechart_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_Thing"):
                opp_val = getattr(old_value, "simplestatechart_Thing", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_Thing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_Thing"):
                opp_val = getattr(value, "simplestatechart_Thing", None)
                setattr(value, "simplestatechart_Thing", self)

    @property
    def relations(self):
        return self.__relations

    @relations.setter
    def relations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_RelatedTo__relations", None)
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

class simplestatechart_Transition(NamedElement):

    def __init__(self, expression: str, simplestatechart_Transition: "simplestatechart_State" = None, simplestatechart_Transition5: "simplestatechart_State" = None, simplestatechart_Transition17: "simplestatechart_State" = None):
        self.expression = expression
        self.simplestatechart_Transition = simplestatechart_Transition
        self.simplestatechart_Transition5 = simplestatechart_Transition5
        self.simplestatechart_Transition17 = simplestatechart_Transition17
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def simplestatechart_Transition17(self):
        return self.__simplestatechart_Transition17

    @simplestatechart_Transition17.setter
    def simplestatechart_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_Transition__simplestatechart_Transition17", None)
        self.__simplestatechart_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_State16"):
                opp_val = getattr(old_value, "simplestatechart_State16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_State16"):
                opp_val = getattr(value, "simplestatechart_State16", None)
                if opp_val is None:
                    setattr(value, "simplestatechart_State16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplestatechart_Transition5(self):
        return self.__simplestatechart_Transition5

    @simplestatechart_Transition5.setter
    def simplestatechart_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_Transition__simplestatechart_Transition5", None)
        self.__simplestatechart_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_State6"):
                opp_val = getattr(old_value, "simplestatechart_State6", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_State6"):
                opp_val = getattr(value, "simplestatechart_State6", None)
                setattr(value, "simplestatechart_State6", self)

    @property
    def simplestatechart_Transition(self):
        return self.__simplestatechart_Transition

    @simplestatechart_Transition.setter
    def simplestatechart_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_Transition__simplestatechart_Transition", None)
        self.__simplestatechart_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_State"):
                opp_val = getattr(old_value, "simplestatechart_State", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_State"):
                opp_val = getattr(value, "simplestatechart_State", None)
                setattr(value, "simplestatechart_State", self)

class simplestatechart_Thing(NamedElement):

    def __init__(self, id: int, Thing: "simplestatechart_RelatedTo" = None, simplestatechart_Thing: "simplestatechart_RelatedTo" = None, fromThing: set["simplestatechart_RelatedTo"] = None):
        self.id = id
        self.Thing = Thing
        self.simplestatechart_Thing = simplestatechart_Thing
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
        old_value = getattr(self, f"_simplestatechart_Thing__Thing", None)
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
    def fromThing(self):
        return self.__fromThing

    @fromThing.setter
    def fromThing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_Thing__fromThing", None)
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
                    

    @property
    def simplestatechart_Thing(self):
        return self.__simplestatechart_Thing

    @simplestatechart_Thing.setter
    def simplestatechart_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplestatechart_Thing__simplestatechart_Thing", None)
        self.__simplestatechart_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplestatechart_RelatedTo"):
                opp_val = getattr(old_value, "simplestatechart_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "simplestatechart_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplestatechart_RelatedTo"):
                opp_val = getattr(value, "simplestatechart_RelatedTo", None)
                setattr(value, "simplestatechart_RelatedTo", self)
