from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dependencies_Edge:

    def __init__(self, referredTo: bool, equal: bool, dependencies_Edge18: "dependencies_SimpleTerm" = None, dependencies_Edge20: "dependencies_RightTerm" = None, dependencies_Edge: "dependencies_Vertex" = None):
        self.referredTo = referredTo
        self.equal = equal
        self.dependencies_Edge18 = dependencies_Edge18
        self.dependencies_Edge20 = dependencies_Edge20
        self.dependencies_Edge = dependencies_Edge
        
    @property
    def referredTo(self) -> bool:
        return self.__referredTo

    @referredTo.setter
    def referredTo(self, referredTo: bool):
        self.__referredTo = referredTo

    @property
    def equal(self) -> bool:
        return self.__equal

    @equal.setter
    def equal(self, equal: bool):
        self.__equal = equal

    @property
    def dependencies_Edge(self):
        return self.__dependencies_Edge

    @dependencies_Edge.setter
    def dependencies_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_Edge__dependencies_Edge", None)
        self.__dependencies_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_Vertex"):
                opp_val = getattr(old_value, "dependencies_Vertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_Vertex"):
                opp_val = getattr(value, "dependencies_Vertex", None)
                if opp_val is None:
                    setattr(value, "dependencies_Vertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dependencies_Edge18(self):
        return self.__dependencies_Edge18

    @dependencies_Edge18.setter
    def dependencies_Edge18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_Edge__dependencies_Edge18", None)
        self.__dependencies_Edge18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_SimpleTerm"):
                opp_val = getattr(old_value, "dependencies_SimpleTerm", None)
                if opp_val == self:
                    setattr(old_value, "dependencies_SimpleTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_SimpleTerm"):
                opp_val = getattr(value, "dependencies_SimpleTerm", None)
                setattr(value, "dependencies_SimpleTerm", self)

    @property
    def dependencies_Edge20(self):
        return self.__dependencies_Edge20

    @dependencies_Edge20.setter
    def dependencies_Edge20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_Edge__dependencies_Edge20", None)
        self.__dependencies_Edge20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_RightTerm"):
                opp_val = getattr(old_value, "dependencies_RightTerm", None)
                if opp_val == self:
                    setattr(old_value, "dependencies_RightTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_RightTerm"):
                opp_val = getattr(value, "dependencies_RightTerm", None)
                setattr(value, "dependencies_RightTerm", self)

class dependencies_Vertex(ABC):

    pass
class dependencies_EClass:

    pass
class Vertex:

    pass
class Block:

    pass
class dependencies_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dependencies_Operation:

    def __init__(self, operationType: str, dependencies_Operation: "dependencies_RightTerm" = None, dependencies_Operation33: set["dependencies_RightTerm"] = None):
        self.operationType = operationType
        self.dependencies_Operation = dependencies_Operation
        self.dependencies_Operation33 = dependencies_Operation33 if dependencies_Operation33 is not None else set()
        
    @property
    def operationType(self) -> str:
        return self.__operationType

    @operationType.setter
    def operationType(self, operationType: str):
        self.__operationType = operationType

    @property
    def dependencies_Operation(self):
        return self.__dependencies_Operation

    @dependencies_Operation.setter
    def dependencies_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_Operation__dependencies_Operation", None)
        self.__dependencies_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_RightTerm28"):
                opp_val = getattr(old_value, "dependencies_RightTerm28", None)
                if opp_val == self:
                    setattr(old_value, "dependencies_RightTerm28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_RightTerm28"):
                opp_val = getattr(value, "dependencies_RightTerm28", None)
                setattr(value, "dependencies_RightTerm28", self)

    @property
    def dependencies_Operation33(self):
        return self.__dependencies_Operation33

    @dependencies_Operation33.setter
    def dependencies_Operation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_Operation__dependencies_Operation33", None)
        self.__dependencies_Operation33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencies_RightTerm34"):
                    opp_val = getattr(item, "dependencies_RightTerm34", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencies_RightTerm34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencies_RightTerm34"):
                    opp_val = getattr(item, "dependencies_RightTerm34", None)
                    
                    setattr(item, "dependencies_RightTerm34", self)
                    

class Term:

    pass
class dependencies_Term(ABC):

    pass
class dependencies_RightTerm(Term):

    def __init__(self, value: str, dependencies_RightTerm: "dependencies_Edge" = None, dependencies_RightTerm28: "dependencies_Operation" = None, dependencies_RightTerm30: set["dependencies_SimpleTerm"] = None, dependencies_RightTerm34: "dependencies_Operation" = None):
        self.value = value
        self.dependencies_RightTerm = dependencies_RightTerm
        self.dependencies_RightTerm28 = dependencies_RightTerm28
        self.dependencies_RightTerm30 = dependencies_RightTerm30 if dependencies_RightTerm30 is not None else set()
        self.dependencies_RightTerm34 = dependencies_RightTerm34
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def dependencies_RightTerm(self):
        return self.__dependencies_RightTerm

    @dependencies_RightTerm.setter
    def dependencies_RightTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_RightTerm__dependencies_RightTerm", None)
        self.__dependencies_RightTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_Edge20"):
                opp_val = getattr(old_value, "dependencies_Edge20", None)
                if opp_val == self:
                    setattr(old_value, "dependencies_Edge20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_Edge20"):
                opp_val = getattr(value, "dependencies_Edge20", None)
                setattr(value, "dependencies_Edge20", self)

    @property
    def dependencies_RightTerm34(self):
        return self.__dependencies_RightTerm34

    @dependencies_RightTerm34.setter
    def dependencies_RightTerm34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_RightTerm__dependencies_RightTerm34", None)
        self.__dependencies_RightTerm34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_Operation33"):
                opp_val = getattr(old_value, "dependencies_Operation33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_Operation33"):
                opp_val = getattr(value, "dependencies_Operation33", None)
                if opp_val is None:
                    setattr(value, "dependencies_Operation33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dependencies_RightTerm30(self):
        return self.__dependencies_RightTerm30

    @dependencies_RightTerm30.setter
    def dependencies_RightTerm30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_RightTerm__dependencies_RightTerm30", None)
        self.__dependencies_RightTerm30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencies_SimpleTerm31"):
                    opp_val = getattr(item, "dependencies_SimpleTerm31", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencies_SimpleTerm31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencies_SimpleTerm31"):
                    opp_val = getattr(item, "dependencies_SimpleTerm31", None)
                    
                    setattr(item, "dependencies_SimpleTerm31", self)
                    

    @property
    def dependencies_RightTerm28(self):
        return self.__dependencies_RightTerm28

    @dependencies_RightTerm28.setter
    def dependencies_RightTerm28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_RightTerm__dependencies_RightTerm28", None)
        self.__dependencies_RightTerm28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_Operation"):
                opp_val = getattr(old_value, "dependencies_Operation", None)
                if opp_val == self:
                    setattr(old_value, "dependencies_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_Operation"):
                opp_val = getattr(value, "dependencies_Operation", None)
                setattr(value, "dependencies_Operation", self)

class dependencies_SimpleTerm(Term):

    pass
class dependencies_Block(ABC):

    pass
class dependencies_RCPackage:

    pass
class dependencies_Create(Block):

    pass
class dependencies_SemiRequired(Block):

    pass
class dependencies_Required(Block):

    pass
class dependencies_EPackage:

    pass
class dependencies_Equivalence(Vertex):

    pass
class NamedElement:

    pass
class dependencies_CoreClass(NamedElement, Vertex):

    pass
class dependencies_Domain(NamedElement):

    pass
class dependencies_Graph(NamedElement):

    def __init__(self, priority: str, dependencies_Graph: set["dependencies_Domain"] = None, dependencies_Graph2: "dependencies_Equivalence" = None):
        self.priority = priority
        self.dependencies_Graph = dependencies_Graph if dependencies_Graph is not None else set()
        self.dependencies_Graph2 = dependencies_Graph2
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def dependencies_Graph2(self):
        return self.__dependencies_Graph2

    @dependencies_Graph2.setter
    def dependencies_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_Graph__dependencies_Graph2", None)
        self.__dependencies_Graph2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies_Equivalence"):
                opp_val = getattr(old_value, "dependencies_Equivalence", None)
                if opp_val == self:
                    setattr(old_value, "dependencies_Equivalence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies_Equivalence"):
                opp_val = getattr(value, "dependencies_Equivalence", None)
                setattr(value, "dependencies_Equivalence", self)

    @property
    def dependencies_Graph(self):
        return self.__dependencies_Graph

    @dependencies_Graph.setter
    def dependencies_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dependencies_Graph__dependencies_Graph", None)
        self.__dependencies_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dependencies_Domain"):
                    opp_val = getattr(item, "dependencies_Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "dependencies_Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dependencies_Domain"):
                    opp_val = getattr(item, "dependencies_Domain", None)
                    
                    setattr(item, "dependencies_Domain", self)
                    
