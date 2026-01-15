from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Scale(Enum):
    nothing = "nothing"
    one = "one"
    two = "two"
    three = "three"
    four = "four"


############################################
# Definition of Classes
############################################

class relationworld_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class relationworld_Category(ABC):

    def __init__(self, nom: str, relationworld_Category: set["relationworld_SourceNode"] = None, relationworld_Category17: set["relationworld_Arrow"] = None, relationworld_Category20: set["relationworld_TargetNode"] = None):
        self.nom = nom
        self.relationworld_Category = relationworld_Category if relationworld_Category is not None else set()
        self.relationworld_Category17 = relationworld_Category17 if relationworld_Category17 is not None else set()
        self.relationworld_Category20 = relationworld_Category20 if relationworld_Category20 is not None else set()
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def relationworld_Category17(self):
        return self.__relationworld_Category17

    @relationworld_Category17.setter
    def relationworld_Category17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_Category__relationworld_Category17", None)
        self.__relationworld_Category17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationworld_Arrow18"):
                    opp_val = getattr(item, "relationworld_Arrow18", None)
                    
                    if opp_val == self:
                        setattr(item, "relationworld_Arrow18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationworld_Arrow18"):
                    opp_val = getattr(item, "relationworld_Arrow18", None)
                    
                    setattr(item, "relationworld_Arrow18", self)
                    

    @property
    def relationworld_Category(self):
        return self.__relationworld_Category

    @relationworld_Category.setter
    def relationworld_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_Category__relationworld_Category", None)
        self.__relationworld_Category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationworld_SourceNode15"):
                    opp_val = getattr(item, "relationworld_SourceNode15", None)
                    
                    if opp_val == self:
                        setattr(item, "relationworld_SourceNode15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationworld_SourceNode15"):
                    opp_val = getattr(item, "relationworld_SourceNode15", None)
                    
                    setattr(item, "relationworld_SourceNode15", self)
                    

    @property
    def relationworld_Category20(self):
        return self.__relationworld_Category20

    @relationworld_Category20.setter
    def relationworld_Category20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_Category__relationworld_Category20", None)
        self.__relationworld_Category20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationworld_TargetNode21"):
                    opp_val = getattr(item, "relationworld_TargetNode21", None)
                    
                    if opp_val == self:
                        setattr(item, "relationworld_TargetNode21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationworld_TargetNode21"):
                    opp_val = getattr(item, "relationworld_TargetNode21", None)
                    
                    setattr(item, "relationworld_TargetNode21", self)
                    

    def compare(self, n2: TargetNode, n1: TargetNode) -> int:
        # TODO: Implement compare method
        pass

    def affectation(self, source: TargetNode, cible: SourceNode) -> Arrow:
        # TODO: Implement affectation method
        pass

    def compare(self, n2: SourceNode, n1: SourceNode) -> int:
        # TODO: Implement compare method
        pass

class relationworld_TargetNode(ABC):

    def __init__(self, relationworld_TargetNode: "relationworld_Arrow" = None, relationworld_TargetNode21: "relationworld_Category" = None):
        self.relationworld_TargetNode = relationworld_TargetNode
        self.relationworld_TargetNode21 = relationworld_TargetNode21
        
    @property
    def relationworld_TargetNode21(self):
        return self.__relationworld_TargetNode21

    @relationworld_TargetNode21.setter
    def relationworld_TargetNode21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_TargetNode__relationworld_TargetNode21", None)
        self.__relationworld_TargetNode21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_Category20"):
                opp_val = getattr(old_value, "relationworld_Category20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_Category20"):
                opp_val = getattr(value, "relationworld_Category20", None)
                if opp_val is None:
                    setattr(value, "relationworld_Category20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationworld_TargetNode(self):
        return self.__relationworld_TargetNode

    @relationworld_TargetNode.setter
    def relationworld_TargetNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_TargetNode__relationworld_TargetNode", None)
        self.__relationworld_TargetNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_Arrow13"):
                opp_val = getattr(old_value, "relationworld_Arrow13", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_Arrow13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_Arrow13"):
                opp_val = getattr(value, "relationworld_Arrow13", None)
                setattr(value, "relationworld_Arrow13", self)

    def pred(self) -> TargetNode:
        # TODO: Implement pred method
        pass

    def succ(self) -> TargetNode:
        # TODO: Implement succ method
        pass

    def compare(self, noeud: TargetNode) -> int:
        # TODO: Implement compare method
        pass

class relationworld_Arrow(ABC):

    def __init__(self, relationworld_Arrow: "relationworld_SourceNode" = None, relationworld_Arrow13: "relationworld_TargetNode" = None, relationworld_Arrow18: "relationworld_Category" = None):
        self.relationworld_Arrow = relationworld_Arrow
        self.relationworld_Arrow13 = relationworld_Arrow13
        self.relationworld_Arrow18 = relationworld_Arrow18
        
    @property
    def relationworld_Arrow13(self):
        return self.__relationworld_Arrow13

    @relationworld_Arrow13.setter
    def relationworld_Arrow13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_Arrow__relationworld_Arrow13", None)
        self.__relationworld_Arrow13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_TargetNode"):
                opp_val = getattr(old_value, "relationworld_TargetNode", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_TargetNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_TargetNode"):
                opp_val = getattr(value, "relationworld_TargetNode", None)
                setattr(value, "relationworld_TargetNode", self)

    @property
    def relationworld_Arrow18(self):
        return self.__relationworld_Arrow18

    @relationworld_Arrow18.setter
    def relationworld_Arrow18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_Arrow__relationworld_Arrow18", None)
        self.__relationworld_Arrow18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_Category17"):
                opp_val = getattr(old_value, "relationworld_Category17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_Category17"):
                opp_val = getattr(value, "relationworld_Category17", None)
                if opp_val is None:
                    setattr(value, "relationworld_Category17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationworld_Arrow(self):
        return self.__relationworld_Arrow

    @relationworld_Arrow.setter
    def relationworld_Arrow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_Arrow__relationworld_Arrow", None)
        self.__relationworld_Arrow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_SourceNode"):
                opp_val = getattr(old_value, "relationworld_SourceNode", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_SourceNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_SourceNode"):
                opp_val = getattr(value, "relationworld_SourceNode", None)
                setattr(value, "relationworld_SourceNode", self)

    def validate(self) -> bool:
        # TODO: Implement validate method
        pass

class relationworld_SourceNode(ABC):

    def __init__(self, relationworld_SourceNode: "relationworld_Arrow" = None, relationworld_SourceNode15: "relationworld_Category" = None):
        self.relationworld_SourceNode = relationworld_SourceNode
        self.relationworld_SourceNode15 = relationworld_SourceNode15
        
    @property
    def relationworld_SourceNode15(self):
        return self.__relationworld_SourceNode15

    @relationworld_SourceNode15.setter
    def relationworld_SourceNode15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_SourceNode__relationworld_SourceNode15", None)
        self.__relationworld_SourceNode15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_Category"):
                opp_val = getattr(old_value, "relationworld_Category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_Category"):
                opp_val = getattr(value, "relationworld_Category", None)
                if opp_val is None:
                    setattr(value, "relationworld_Category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationworld_SourceNode(self):
        return self.__relationworld_SourceNode

    @relationworld_SourceNode.setter
    def relationworld_SourceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_SourceNode__relationworld_SourceNode", None)
        self.__relationworld_SourceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_Arrow"):
                opp_val = getattr(old_value, "relationworld_Arrow", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_Arrow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_Arrow"):
                opp_val = getattr(value, "relationworld_Arrow", None)
                setattr(value, "relationworld_Arrow", self)

    def compare(self, noeud: SourceNode) -> int:
        # TODO: Implement compare method
        pass

    def succ(self) -> SourceNode:
        # TODO: Implement succ method
        pass

    def pred(self) -> SourceNode:
        # TODO: Implement pred method
        pass

class Category:

    pass
class relationworld_World(Category):

    def __init__(self, relationworld_World6: set["relationworld_ThingB"] = None, relationworld_World9: set["relationworld_RelatedTo"] = None, relationworld_World: set["relationworld_ThingA"] = None):
        self.relationworld_World6 = relationworld_World6 if relationworld_World6 is not None else set()
        self.relationworld_World9 = relationworld_World9 if relationworld_World9 is not None else set()
        self.relationworld_World = relationworld_World if relationworld_World is not None else set()
        
    @property
    def relationworld_World(self):
        return self.__relationworld_World

    @relationworld_World.setter
    def relationworld_World(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_World__relationworld_World", None)
        self.__relationworld_World = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationworld_ThingA4"):
                    opp_val = getattr(item, "relationworld_ThingA4", None)
                    
                    if opp_val == self:
                        setattr(item, "relationworld_ThingA4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationworld_ThingA4"):
                    opp_val = getattr(item, "relationworld_ThingA4", None)
                    
                    setattr(item, "relationworld_ThingA4", self)
                    

    @property
    def relationworld_World9(self):
        return self.__relationworld_World9

    @relationworld_World9.setter
    def relationworld_World9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_World__relationworld_World9", None)
        self.__relationworld_World9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationworld_RelatedTo10"):
                    opp_val = getattr(item, "relationworld_RelatedTo10", None)
                    
                    if opp_val == self:
                        setattr(item, "relationworld_RelatedTo10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationworld_RelatedTo10"):
                    opp_val = getattr(item, "relationworld_RelatedTo10", None)
                    
                    setattr(item, "relationworld_RelatedTo10", self)
                    

    @property
    def relationworld_World6(self):
        return self.__relationworld_World6

    @relationworld_World6.setter
    def relationworld_World6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_World__relationworld_World6", None)
        self.__relationworld_World6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationworld_ThingB7"):
                    opp_val = getattr(item, "relationworld_ThingB7", None)
                    
                    if opp_val == self:
                        setattr(item, "relationworld_ThingB7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationworld_ThingB7"):
                    opp_val = getattr(item, "relationworld_ThingB7", None)
                    
                    setattr(item, "relationworld_ThingB7", self)
                    

    def affectation(self, role: str, personne: str) -> str:
        # TODO: Implement affectation method
        pass

    def compare(self, personne1: str, personne2: str) -> int:
        # TODO: Implement compare method
        pass

    def compare(self, role1: str, role2: str) -> int:
        # TODO: Implement compare method
        pass

class SourceNode:

    pass
class Arrow:

    pass
class TargetNode:

    pass
class NamedElement:

    pass
class relationworld_ThingA(NamedElement, SourceNode):

    def __init__(self, since: date, relationworld_ThingA: "relationworld_RelatedTo" = None, relationworld_ThingA4: "relationworld_World" = None):
        self.since = since
        self.relationworld_ThingA = relationworld_ThingA
        self.relationworld_ThingA4 = relationworld_ThingA4
        
    @property
    def since(self) -> date:
        return self.__since

    @since.setter
    def since(self, since: date):
        self.__since = since

    @property
    def relationworld_ThingA4(self):
        return self.__relationworld_ThingA4

    @relationworld_ThingA4.setter
    def relationworld_ThingA4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_ThingA__relationworld_ThingA4", None)
        self.__relationworld_ThingA4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_World"):
                opp_val = getattr(old_value, "relationworld_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_World"):
                opp_val = getattr(value, "relationworld_World", None)
                if opp_val is None:
                    setattr(value, "relationworld_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationworld_ThingA(self):
        return self.__relationworld_ThingA

    @relationworld_ThingA.setter
    def relationworld_ThingA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_ThingA__relationworld_ThingA", None)
        self.__relationworld_ThingA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_RelatedTo"):
                opp_val = getattr(old_value, "relationworld_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_RelatedTo"):
                opp_val = getattr(value, "relationworld_RelatedTo", None)
                setattr(value, "relationworld_RelatedTo", self)

    def pred(self) -> str:
        # TODO: Implement pred method
        pass

    def succ(self) -> str:
        # TODO: Implement succ method
        pass

    def compare(self, personne: str) -> int:
        # TODO: Implement compare method
        pass

class relationworld_RelatedTo(NamedElement, Arrow):

    def __init__(self, relationworld_RelatedTo: "relationworld_ThingA" = None, relationworld_RelatedTo2: "relationworld_ThingB" = None, relationworld_RelatedTo10: "relationworld_World" = None):
        self.relationworld_RelatedTo = relationworld_RelatedTo
        self.relationworld_RelatedTo2 = relationworld_RelatedTo2
        self.relationworld_RelatedTo10 = relationworld_RelatedTo10
        
    @property
    def relationworld_RelatedTo(self):
        return self.__relationworld_RelatedTo

    @relationworld_RelatedTo.setter
    def relationworld_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_RelatedTo__relationworld_RelatedTo", None)
        self.__relationworld_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_ThingA"):
                opp_val = getattr(old_value, "relationworld_ThingA", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_ThingA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_ThingA"):
                opp_val = getattr(value, "relationworld_ThingA", None)
                setattr(value, "relationworld_ThingA", self)

    @property
    def relationworld_RelatedTo10(self):
        return self.__relationworld_RelatedTo10

    @relationworld_RelatedTo10.setter
    def relationworld_RelatedTo10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_RelatedTo__relationworld_RelatedTo10", None)
        self.__relationworld_RelatedTo10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_World9"):
                opp_val = getattr(old_value, "relationworld_World9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_World9"):
                opp_val = getattr(value, "relationworld_World9", None)
                if opp_val is None:
                    setattr(value, "relationworld_World9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationworld_RelatedTo2(self):
        return self.__relationworld_RelatedTo2

    @relationworld_RelatedTo2.setter
    def relationworld_RelatedTo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_RelatedTo__relationworld_RelatedTo2", None)
        self.__relationworld_RelatedTo2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_ThingB"):
                opp_val = getattr(old_value, "relationworld_ThingB", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_ThingB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_ThingB"):
                opp_val = getattr(value, "relationworld_ThingB", None)
                setattr(value, "relationworld_ThingB", self)

    def validate(self) -> bool:
        # TODO: Implement validate method
        pass

class relationworld_ThingB(NamedElement, TargetNode):

    def __init__(self, step: str, relationworld_ThingB: "relationworld_RelatedTo" = None, relationworld_ThingB7: "relationworld_World" = None):
        self.step = step
        self.relationworld_ThingB = relationworld_ThingB
        self.relationworld_ThingB7 = relationworld_ThingB7
        
    @property
    def step(self) -> str:
        return self.__step

    @step.setter
    def step(self, step: str):
        self.__step = step

    @property
    def relationworld_ThingB(self):
        return self.__relationworld_ThingB

    @relationworld_ThingB.setter
    def relationworld_ThingB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_ThingB__relationworld_ThingB", None)
        self.__relationworld_ThingB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_RelatedTo2"):
                opp_val = getattr(old_value, "relationworld_RelatedTo2", None)
                if opp_val == self:
                    setattr(old_value, "relationworld_RelatedTo2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_RelatedTo2"):
                opp_val = getattr(value, "relationworld_RelatedTo2", None)
                setattr(value, "relationworld_RelatedTo2", self)

    @property
    def relationworld_ThingB7(self):
        return self.__relationworld_ThingB7

    @relationworld_ThingB7.setter
    def relationworld_ThingB7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationworld_ThingB__relationworld_ThingB7", None)
        self.__relationworld_ThingB7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationworld_World6"):
                opp_val = getattr(old_value, "relationworld_World6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationworld_World6"):
                opp_val = getattr(value, "relationworld_World6", None)
                if opp_val is None:
                    setattr(value, "relationworld_World6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def succ(self) -> str:
        # TODO: Implement succ method
        pass

    def pred(self) -> str:
        # TODO: Implement pred method
        pass

    def compare(self, role: str) -> int:
        # TODO: Implement compare method
        pass
