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

class relationpattern_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class relationpattern_TargetNode(ABC):

    def __init__(self, relationpattern_TargetNode: "relationpattern_Arrow" = None, relationpattern_TargetNode21: "relationpattern_Category" = None):
        self.relationpattern_TargetNode = relationpattern_TargetNode
        self.relationpattern_TargetNode21 = relationpattern_TargetNode21
        
    @property
    def relationpattern_TargetNode(self):
        return self.__relationpattern_TargetNode

    @relationpattern_TargetNode.setter
    def relationpattern_TargetNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_TargetNode__relationpattern_TargetNode", None)
        self.__relationpattern_TargetNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_Arrow13"):
                opp_val = getattr(old_value, "relationpattern_Arrow13", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_Arrow13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_Arrow13"):
                opp_val = getattr(value, "relationpattern_Arrow13", None)
                setattr(value, "relationpattern_Arrow13", self)

    @property
    def relationpattern_TargetNode21(self):
        return self.__relationpattern_TargetNode21

    @relationpattern_TargetNode21.setter
    def relationpattern_TargetNode21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_TargetNode__relationpattern_TargetNode21", None)
        self.__relationpattern_TargetNode21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_Category20"):
                opp_val = getattr(old_value, "relationpattern_Category20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_Category20"):
                opp_val = getattr(value, "relationpattern_Category20", None)
                if opp_val is None:
                    setattr(value, "relationpattern_Category20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def succ(self) -> TargetNode:
        # TODO: Implement succ method
        pass

    def compare(self, noeud: TargetNode) -> int:
        # TODO: Implement compare method
        pass

    def pred(self) -> TargetNode:
        # TODO: Implement pred method
        pass

class relationpattern_Arrow(ABC):

    def __init__(self, relationpattern_Arrow: "relationpattern_SourceNode" = None, relationpattern_Arrow13: "relationpattern_TargetNode" = None, relationpattern_Arrow18: "relationpattern_Category" = None):
        self.relationpattern_Arrow = relationpattern_Arrow
        self.relationpattern_Arrow13 = relationpattern_Arrow13
        self.relationpattern_Arrow18 = relationpattern_Arrow18
        
    @property
    def relationpattern_Arrow18(self):
        return self.__relationpattern_Arrow18

    @relationpattern_Arrow18.setter
    def relationpattern_Arrow18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_Arrow__relationpattern_Arrow18", None)
        self.__relationpattern_Arrow18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_Category17"):
                opp_val = getattr(old_value, "relationpattern_Category17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_Category17"):
                opp_val = getattr(value, "relationpattern_Category17", None)
                if opp_val is None:
                    setattr(value, "relationpattern_Category17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationpattern_Arrow13(self):
        return self.__relationpattern_Arrow13

    @relationpattern_Arrow13.setter
    def relationpattern_Arrow13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_Arrow__relationpattern_Arrow13", None)
        self.__relationpattern_Arrow13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_TargetNode"):
                opp_val = getattr(old_value, "relationpattern_TargetNode", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_TargetNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_TargetNode"):
                opp_val = getattr(value, "relationpattern_TargetNode", None)
                setattr(value, "relationpattern_TargetNode", self)

    @property
    def relationpattern_Arrow(self):
        return self.__relationpattern_Arrow

    @relationpattern_Arrow.setter
    def relationpattern_Arrow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_Arrow__relationpattern_Arrow", None)
        self.__relationpattern_Arrow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_SourceNode"):
                opp_val = getattr(old_value, "relationpattern_SourceNode", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_SourceNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_SourceNode"):
                opp_val = getattr(value, "relationpattern_SourceNode", None)
                setattr(value, "relationpattern_SourceNode", self)

    def validate(self) -> bool:
        # TODO: Implement validate method
        pass

class relationpattern_Category(ABC):

    def __init__(self, nom: str, relationpattern_Category: set["relationpattern_SourceNode"] = None, relationpattern_Category17: set["relationpattern_Arrow"] = None, relationpattern_Category20: set["relationpattern_TargetNode"] = None):
        self.nom = nom
        self.relationpattern_Category = relationpattern_Category if relationpattern_Category is not None else set()
        self.relationpattern_Category17 = relationpattern_Category17 if relationpattern_Category17 is not None else set()
        self.relationpattern_Category20 = relationpattern_Category20 if relationpattern_Category20 is not None else set()
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def relationpattern_Category(self):
        return self.__relationpattern_Category

    @relationpattern_Category.setter
    def relationpattern_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_Category__relationpattern_Category", None)
        self.__relationpattern_Category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationpattern_SourceNode15"):
                    opp_val = getattr(item, "relationpattern_SourceNode15", None)
                    
                    if opp_val == self:
                        setattr(item, "relationpattern_SourceNode15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationpattern_SourceNode15"):
                    opp_val = getattr(item, "relationpattern_SourceNode15", None)
                    
                    setattr(item, "relationpattern_SourceNode15", self)
                    

    @property
    def relationpattern_Category17(self):
        return self.__relationpattern_Category17

    @relationpattern_Category17.setter
    def relationpattern_Category17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_Category__relationpattern_Category17", None)
        self.__relationpattern_Category17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationpattern_Arrow18"):
                    opp_val = getattr(item, "relationpattern_Arrow18", None)
                    
                    if opp_val == self:
                        setattr(item, "relationpattern_Arrow18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationpattern_Arrow18"):
                    opp_val = getattr(item, "relationpattern_Arrow18", None)
                    
                    setattr(item, "relationpattern_Arrow18", self)
                    

    @property
    def relationpattern_Category20(self):
        return self.__relationpattern_Category20

    @relationpattern_Category20.setter
    def relationpattern_Category20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_Category__relationpattern_Category20", None)
        self.__relationpattern_Category20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationpattern_TargetNode21"):
                    opp_val = getattr(item, "relationpattern_TargetNode21", None)
                    
                    if opp_val == self:
                        setattr(item, "relationpattern_TargetNode21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationpattern_TargetNode21"):
                    opp_val = getattr(item, "relationpattern_TargetNode21", None)
                    
                    setattr(item, "relationpattern_TargetNode21", self)
                    

    def compare(self, n1: TargetNode, n2: TargetNode) -> int:
        # TODO: Implement compare method
        pass

    def compare(self, n2: SourceNode, n1: SourceNode) -> int:
        # TODO: Implement compare method
        pass

    def affectation(self, source: TargetNode, cible: SourceNode) -> Arrow:
        # TODO: Implement affectation method
        pass

    def affectationInterval(self, target: TargetNode) -> SourceNode:
        # TODO: Implement affectationInterval method
        pass

class Category:

    pass
class relationpattern_World(Category):

    def __init__(self, relationpattern_World: set["relationpattern_ThingA"] = None, relationpattern_World6: set["relationpattern_ThingB"] = None, relationpattern_World9: set["relationpattern_RelatedTo"] = None):
        self.relationpattern_World = relationpattern_World if relationpattern_World is not None else set()
        self.relationpattern_World6 = relationpattern_World6 if relationpattern_World6 is not None else set()
        self.relationpattern_World9 = relationpattern_World9 if relationpattern_World9 is not None else set()
        
    @property
    def relationpattern_World9(self):
        return self.__relationpattern_World9

    @relationpattern_World9.setter
    def relationpattern_World9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_World__relationpattern_World9", None)
        self.__relationpattern_World9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationpattern_RelatedTo10"):
                    opp_val = getattr(item, "relationpattern_RelatedTo10", None)
                    
                    if opp_val == self:
                        setattr(item, "relationpattern_RelatedTo10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationpattern_RelatedTo10"):
                    opp_val = getattr(item, "relationpattern_RelatedTo10", None)
                    
                    setattr(item, "relationpattern_RelatedTo10", self)
                    

    @property
    def relationpattern_World6(self):
        return self.__relationpattern_World6

    @relationpattern_World6.setter
    def relationpattern_World6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_World__relationpattern_World6", None)
        self.__relationpattern_World6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationpattern_ThingB7"):
                    opp_val = getattr(item, "relationpattern_ThingB7", None)
                    
                    if opp_val == self:
                        setattr(item, "relationpattern_ThingB7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationpattern_ThingB7"):
                    opp_val = getattr(item, "relationpattern_ThingB7", None)
                    
                    setattr(item, "relationpattern_ThingB7", self)
                    

    @property
    def relationpattern_World(self):
        return self.__relationpattern_World

    @relationpattern_World.setter
    def relationpattern_World(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_World__relationpattern_World", None)
        self.__relationpattern_World = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "relationpattern_ThingA4"):
                    opp_val = getattr(item, "relationpattern_ThingA4", None)
                    
                    if opp_val == self:
                        setattr(item, "relationpattern_ThingA4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "relationpattern_ThingA4"):
                    opp_val = getattr(item, "relationpattern_ThingA4", None)
                    
                    setattr(item, "relationpattern_ThingA4", self)
                    

    def affectation(self, personne: str, role: str) -> str:
        # TODO: Implement affectation method
        pass

    def compare(self, role2: str, role1: str) -> int:
        # TODO: Implement compare method
        pass

    def affectationInterval(self, thingb: str) -> str:
        # TODO: Implement affectationInterval method
        pass

    def compare(self, personne1: str, personne2: str) -> int:
        # TODO: Implement compare method
        pass

class relationpattern_SourceNode(ABC):

    def __init__(self, relationpattern_SourceNode15: "relationpattern_Category" = None, relationpattern_SourceNode: "relationpattern_Arrow" = None):
        self.relationpattern_SourceNode15 = relationpattern_SourceNode15
        self.relationpattern_SourceNode = relationpattern_SourceNode
        
    @property
    def relationpattern_SourceNode(self):
        return self.__relationpattern_SourceNode

    @relationpattern_SourceNode.setter
    def relationpattern_SourceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_SourceNode__relationpattern_SourceNode", None)
        self.__relationpattern_SourceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_Arrow"):
                opp_val = getattr(old_value, "relationpattern_Arrow", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_Arrow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_Arrow"):
                opp_val = getattr(value, "relationpattern_Arrow", None)
                setattr(value, "relationpattern_Arrow", self)

    @property
    def relationpattern_SourceNode15(self):
        return self.__relationpattern_SourceNode15

    @relationpattern_SourceNode15.setter
    def relationpattern_SourceNode15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_SourceNode__relationpattern_SourceNode15", None)
        self.__relationpattern_SourceNode15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_Category"):
                opp_val = getattr(old_value, "relationpattern_Category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_Category"):
                opp_val = getattr(value, "relationpattern_Category", None)
                if opp_val is None:
                    setattr(value, "relationpattern_Category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def succ(self) -> SourceNode:
        # TODO: Implement succ method
        pass

    def pred(self) -> SourceNode:
        # TODO: Implement pred method
        pass

    def compare(self, noeud: SourceNode) -> int:
        # TODO: Implement compare method
        pass

class TargetNode:

    pass
class Arrow:

    pass
class NamedElement:

    pass
class relationpattern_RelatedTo(Arrow, NamedElement):

    def __init__(self, relationpattern_RelatedTo: "relationpattern_ThingA" = None, relationpattern_RelatedTo10: "relationpattern_World" = None, relationpattern_RelatedTo2: "relationpattern_ThingB" = None):
        self.relationpattern_RelatedTo = relationpattern_RelatedTo
        self.relationpattern_RelatedTo10 = relationpattern_RelatedTo10
        self.relationpattern_RelatedTo2 = relationpattern_RelatedTo2
        
    @property
    def relationpattern_RelatedTo(self):
        return self.__relationpattern_RelatedTo

    @relationpattern_RelatedTo.setter
    def relationpattern_RelatedTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_RelatedTo__relationpattern_RelatedTo", None)
        self.__relationpattern_RelatedTo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_ThingA"):
                opp_val = getattr(old_value, "relationpattern_ThingA", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_ThingA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_ThingA"):
                opp_val = getattr(value, "relationpattern_ThingA", None)
                setattr(value, "relationpattern_ThingA", self)

    @property
    def relationpattern_RelatedTo2(self):
        return self.__relationpattern_RelatedTo2

    @relationpattern_RelatedTo2.setter
    def relationpattern_RelatedTo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_RelatedTo__relationpattern_RelatedTo2", None)
        self.__relationpattern_RelatedTo2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_ThingB"):
                opp_val = getattr(old_value, "relationpattern_ThingB", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_ThingB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_ThingB"):
                opp_val = getattr(value, "relationpattern_ThingB", None)
                setattr(value, "relationpattern_ThingB", self)

    @property
    def relationpattern_RelatedTo10(self):
        return self.__relationpattern_RelatedTo10

    @relationpattern_RelatedTo10.setter
    def relationpattern_RelatedTo10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_RelatedTo__relationpattern_RelatedTo10", None)
        self.__relationpattern_RelatedTo10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_World9"):
                opp_val = getattr(old_value, "relationpattern_World9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_World9"):
                opp_val = getattr(value, "relationpattern_World9", None)
                if opp_val is None:
                    setattr(value, "relationpattern_World9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validate(self) -> bool:
        # TODO: Implement validate method
        pass

class relationpattern_ThingB(TargetNode, NamedElement):

    def __init__(self, step: str, relationpattern_ThingB: "relationpattern_RelatedTo" = None, relationpattern_ThingB7: "relationpattern_World" = None):
        self.step = step
        self.relationpattern_ThingB = relationpattern_ThingB
        self.relationpattern_ThingB7 = relationpattern_ThingB7
        
    @property
    def step(self) -> str:
        return self.__step

    @step.setter
    def step(self, step: str):
        self.__step = step

    @property
    def relationpattern_ThingB7(self):
        return self.__relationpattern_ThingB7

    @relationpattern_ThingB7.setter
    def relationpattern_ThingB7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_ThingB__relationpattern_ThingB7", None)
        self.__relationpattern_ThingB7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_World6"):
                opp_val = getattr(old_value, "relationpattern_World6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_World6"):
                opp_val = getattr(value, "relationpattern_World6", None)
                if opp_val is None:
                    setattr(value, "relationpattern_World6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def relationpattern_ThingB(self):
        return self.__relationpattern_ThingB

    @relationpattern_ThingB.setter
    def relationpattern_ThingB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_ThingB__relationpattern_ThingB", None)
        self.__relationpattern_ThingB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_RelatedTo2"):
                opp_val = getattr(old_value, "relationpattern_RelatedTo2", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_RelatedTo2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_RelatedTo2"):
                opp_val = getattr(value, "relationpattern_RelatedTo2", None)
                setattr(value, "relationpattern_RelatedTo2", self)

    def succ(self) -> str:
        # TODO: Implement succ method
        pass

    def pred(self) -> str:
        # TODO: Implement pred method
        pass

    def compare(self, role: str) -> int:
        # TODO: Implement compare method
        pass

class SourceNode:

    pass
class relationpattern_ThingA(SourceNode, NamedElement):

    def __init__(self, since: date, relationpattern_ThingA: "relationpattern_RelatedTo" = None, relationpattern_ThingA4: "relationpattern_World" = None):
        self.since = since
        self.relationpattern_ThingA = relationpattern_ThingA
        self.relationpattern_ThingA4 = relationpattern_ThingA4
        
    @property
    def since(self) -> date:
        return self.__since

    @since.setter
    def since(self, since: date):
        self.__since = since

    @property
    def relationpattern_ThingA(self):
        return self.__relationpattern_ThingA

    @relationpattern_ThingA.setter
    def relationpattern_ThingA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_ThingA__relationpattern_ThingA", None)
        self.__relationpattern_ThingA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_RelatedTo"):
                opp_val = getattr(old_value, "relationpattern_RelatedTo", None)
                if opp_val == self:
                    setattr(old_value, "relationpattern_RelatedTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_RelatedTo"):
                opp_val = getattr(value, "relationpattern_RelatedTo", None)
                setattr(value, "relationpattern_RelatedTo", self)

    @property
    def relationpattern_ThingA4(self):
        return self.__relationpattern_ThingA4

    @relationpattern_ThingA4.setter
    def relationpattern_ThingA4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_relationpattern_ThingA__relationpattern_ThingA4", None)
        self.__relationpattern_ThingA4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationpattern_World"):
                opp_val = getattr(old_value, "relationpattern_World", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationpattern_World"):
                opp_val = getattr(value, "relationpattern_World", None)
                if opp_val is None:
                    setattr(value, "relationpattern_World", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def pred(self) -> str:
        # TODO: Implement pred method
        pass

    def compare(self, personne: str) -> int:
        # TODO: Implement compare method
        pass

    def succ(self) -> str:
        # TODO: Implement succ method
        pass
