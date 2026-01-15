from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UnaryFormula:

    pass
class henshin_Not(UnaryFormula):

    pass
class BinaryFormula:

    pass
class henshin_Or(BinaryFormula):

    pass
class henshin_Xor(BinaryFormula):

    pass
class henshin_And(BinaryFormula):

    pass
class Formula:

    pass
class henshin_True(Formula):

    pass
class henshin_NestedCondition(Formula):

    def __init__(self, presenceCondition: str, henshin_NestedCondition: "henshin_Graph" = None, henshin_NestedCondition79: set["henshin_Mapping"] = None):
        self.presenceCondition = presenceCondition
        self.henshin_NestedCondition = henshin_NestedCondition
        self.henshin_NestedCondition79 = henshin_NestedCondition79 if henshin_NestedCondition79 is not None else set()
        
    @property
    def presenceCondition(self) -> str:
        return self.__presenceCondition

    @presenceCondition.setter
    def presenceCondition(self, presenceCondition: str):
        self.__presenceCondition = presenceCondition

    @property
    def henshin_NestedCondition79(self):
        return self.__henshin_NestedCondition79

    @henshin_NestedCondition79.setter
    def henshin_NestedCondition79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_NestedCondition__henshin_NestedCondition79", None)
        self.__henshin_NestedCondition79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Mapping80"):
                    opp_val = getattr(item, "henshin_Mapping80", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Mapping80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Mapping80"):
                    opp_val = getattr(item, "henshin_Mapping80", None)
                    
                    setattr(item, "henshin_Mapping80", self)
                    

    @property
    def henshin_NestedCondition(self):
        return self.__henshin_NestedCondition

    @henshin_NestedCondition.setter
    def henshin_NestedCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_NestedCondition__henshin_NestedCondition", None)
        self.__henshin_NestedCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph77"):
                opp_val = getattr(old_value, "henshin_Graph77", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph77"):
                opp_val = getattr(value, "henshin_Graph77", None)
                setattr(value, "henshin_Graph77", self)

    def getHost(self) -> str:
        # TODO: Implement getHost method
        pass

    def isPAC(self) -> bool:
        # TODO: Implement isPAC method
        pass

    def isNAC(self) -> bool:
        # TODO: Implement isNAC method
        pass

class UnaryUnit:

    pass
class henshin_LoopUnit(UnaryUnit):

    pass
class henshin_IteratedUnit(UnaryUnit):

    def __init__(self, iterations: str):
        self.iterations = iterations
        
    @property
    def iterations(self) -> str:
        return self.__iterations

    @iterations.setter
    def iterations(self, iterations: str):
        self.__iterations = iterations

class henshin_BinaryFormula(Formula):

    pass
class henshin_UnaryFormula(Formula):

    pass
class henshin_EAttribute:

    pass
class henshin_EReference:

    pass
class MultiUnit:

    pass
class henshin_PriorityUnit(MultiUnit):

    pass
class henshin_SequentialUnit(MultiUnit):

    def __init__(self, strict: bool, rollback: bool):
        self.strict = strict
        self.rollback = rollback
        
    @property
    def rollback(self) -> bool:
        return self.__rollback

    @rollback.setter
    def rollback(self, rollback: bool):
        self.__rollback = rollback

    @property
    def strict(self) -> bool:
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict

class henshin_IndependentUnit(MultiUnit):

    pass
class henshin_EClass:

    pass
class GraphElement:

    pass
class henshin_Formula(ABC):

    def __init__(self, henshin_Formula: "henshin_Graph" = None, henshin_Formula82: "henshin_UnaryFormula" = None, henshin_Formula84: "henshin_BinaryFormula" = None, henshin_Formula87: "henshin_BinaryFormula" = None):
        self.henshin_Formula = henshin_Formula
        self.henshin_Formula82 = henshin_Formula82
        self.henshin_Formula84 = henshin_Formula84
        self.henshin_Formula87 = henshin_Formula87
        
    @property
    def henshin_Formula87(self):
        return self.__henshin_Formula87

    @henshin_Formula87.setter
    def henshin_Formula87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula87", None)
        self.__henshin_Formula87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_BinaryFormula86"):
                opp_val = getattr(old_value, "henshin_BinaryFormula86", None)
                if opp_val == self:
                    setattr(old_value, "henshin_BinaryFormula86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_BinaryFormula86"):
                opp_val = getattr(value, "henshin_BinaryFormula86", None)
                setattr(value, "henshin_BinaryFormula86", self)

    @property
    def henshin_Formula84(self):
        return self.__henshin_Formula84

    @henshin_Formula84.setter
    def henshin_Formula84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula84", None)
        self.__henshin_Formula84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_BinaryFormula"):
                opp_val = getattr(old_value, "henshin_BinaryFormula", None)
                if opp_val == self:
                    setattr(old_value, "henshin_BinaryFormula", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_BinaryFormula"):
                opp_val = getattr(value, "henshin_BinaryFormula", None)
                setattr(value, "henshin_BinaryFormula", self)

    @property
    def henshin_Formula82(self):
        return self.__henshin_Formula82

    @henshin_Formula82.setter
    def henshin_Formula82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula82", None)
        self.__henshin_Formula82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_UnaryFormula"):
                opp_val = getattr(old_value, "henshin_UnaryFormula", None)
                if opp_val == self:
                    setattr(old_value, "henshin_UnaryFormula", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_UnaryFormula"):
                opp_val = getattr(value, "henshin_UnaryFormula", None)
                setattr(value, "henshin_UnaryFormula", self)

    @property
    def henshin_Formula(self):
        return self.__henshin_Formula

    @henshin_Formula.setter
    def henshin_Formula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula", None)
        self.__henshin_Formula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph39"):
                opp_val = getattr(old_value, "henshin_Graph39", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph39"):
                opp_val = getattr(value, "henshin_Graph39", None)
                setattr(value, "henshin_Graph39", self)

    def isFalse(self) -> bool:
        # TODO: Implement isFalse method
        pass

    def isTrue(self) -> bool:
        # TODO: Implement isTrue method
        pass

class henshin_Edge(GraphElement):

    def __init__(self, index: str, indexConstant: str, Edge44: "henshin_Node" = None, Edge46: "henshin_Node" = None, outgoing: "henshin_Node" = None, incoming: "henshin_Node" = None, Edge: "henshin_Graph" = None, henshin_Edge: "henshin_EReference" = None, edges: "henshin_Graph" = None):
        self.index = index
        self.indexConstant = indexConstant
        self.Edge44 = Edge44
        self.Edge46 = Edge46
        self.outgoing = outgoing
        self.incoming = incoming
        self.Edge = Edge
        self.henshin_Edge = henshin_Edge
        self.edges = edges
        
    @property
    def indexConstant(self) -> str:
        return self.__indexConstant

    @indexConstant.setter
    def indexConstant(self, indexConstant: str):
        self.__indexConstant = indexConstant

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def Edge44(self):
        return self.__Edge44

    @Edge44.setter
    def Edge44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__Edge44", None)
        self.__Edge44 = value
        
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
        old_value = getattr(self, f"_henshin_Edge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node48"):
                opp_val = getattr(old_value, "Node48", None)
                if opp_val == self:
                    setattr(old_value, "Node48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node48"):
                opp_val = getattr(value, "Node48", None)
                setattr(value, "Node48", self)

    @property
    def henshin_Edge(self):
        return self.__henshin_Edge

    @henshin_Edge.setter
    def henshin_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__henshin_Edge", None)
        self.__henshin_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_EReference"):
                opp_val = getattr(old_value, "henshin_EReference", None)
                if opp_val == self:
                    setattr(old_value, "henshin_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_EReference"):
                opp_val = getattr(value, "henshin_EReference", None)
                setattr(value, "henshin_EReference", self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph53"):
                opp_val = getattr(old_value, "Graph53", None)
                if opp_val == self:
                    setattr(old_value, "Graph53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph53"):
                opp_val = getattr(value, "Graph53", None)
                setattr(value, "Graph53", self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph37"):
                opp_val = getattr(old_value, "graph37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph37"):
                opp_val = getattr(value, "graph37", None)
                if opp_val is None:
                    setattr(value, "graph37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Edge46(self):
        return self.__Edge46

    @Edge46.setter
    def Edge46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__Edge46", None)
        self.__Edge46 = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node50"):
                opp_val = getattr(old_value, "Node50", None)
                if opp_val == self:
                    setattr(old_value, "Node50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node50"):
                opp_val = getattr(value, "Node50", None)
                setattr(value, "Node50", self)

    def getActionEdge(self) -> str:
        # TODO: Implement getActionEdge method
        pass

class henshin_Attribute(GraphElement):

    def __init__(self, value: str, constant: str, null: bool, Attribute: "henshin_Node" = None, henshin_Attribute: "henshin_EAttribute" = None, attributes: "henshin_Node" = None):
        self.value = value
        self.constant = constant
        self.null = null
        self.Attribute = Attribute
        self.henshin_Attribute = henshin_Attribute
        self.attributes = attributes
        
    @property
    def null(self) -> bool:
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def constant(self) -> str:
        return self.__constant

    @constant.setter
    def constant(self, constant: str):
        self.__constant = constant

    @property
    def henshin_Attribute(self):
        return self.__henshin_Attribute

    @henshin_Attribute.setter
    def henshin_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Attribute__henshin_Attribute", None)
        self.__henshin_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_EAttribute"):
                opp_val = getattr(old_value, "henshin_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "henshin_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_EAttribute"):
                opp_val = getattr(value, "henshin_EAttribute", None)
                setattr(value, "henshin_EAttribute", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node56"):
                opp_val = getattr(old_value, "Node56", None)
                if opp_val == self:
                    setattr(old_value, "Node56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node56"):
                opp_val = getattr(value, "Node56", None)
                setattr(value, "Node56", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                if opp_val is None:
                    setattr(value, "node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getActionAttribute(self) -> str:
        # TODO: Implement getActionAttribute method
        pass

class henshin_EClassifier:

    pass
class Unit:

    pass
class henshin_MultiUnit(Unit):

    pass
class henshin_ConditionalUnit(Unit):

    pass
class henshin_UnaryUnit(Unit):

    pass
class henshin_Rule(Unit):

    def __init__(self, checkDangling: bool, injectiveMatching: bool, featureModel: str, injectiveMatchingPresenceCondition: str, henshin_Rule: "henshin_Graph" = None, henshin_Rule16: "henshin_Graph" = None, rule: set["henshin_AttributeCondition"] = None, henshin_Rule20: set["henshin_Mapping"] = None, henshin_Rule23: "henshin_Rule" = None, henshin_Rule21: set["henshin_Rule"] = None, henshin_Rule25: set["henshin_Mapping"] = None, Rule: "henshin_AttributeCondition" = None):
        self.checkDangling = checkDangling
        self.injectiveMatching = injectiveMatching
        self.featureModel = featureModel
        self.injectiveMatchingPresenceCondition = injectiveMatchingPresenceCondition
        self.henshin_Rule = henshin_Rule
        self.henshin_Rule16 = henshin_Rule16
        self.rule = rule if rule is not None else set()
        self.henshin_Rule20 = henshin_Rule20 if henshin_Rule20 is not None else set()
        self.henshin_Rule23 = henshin_Rule23
        self.henshin_Rule21 = henshin_Rule21 if henshin_Rule21 is not None else set()
        self.henshin_Rule25 = henshin_Rule25 if henshin_Rule25 is not None else set()
        self.Rule = Rule
        
    @property
    def featureModel(self) -> str:
        return self.__featureModel

    @featureModel.setter
    def featureModel(self, featureModel: str):
        self.__featureModel = featureModel

    @property
    def checkDangling(self) -> bool:
        return self.__checkDangling

    @checkDangling.setter
    def checkDangling(self, checkDangling: bool):
        self.__checkDangling = checkDangling

    @property
    def injectiveMatching(self) -> bool:
        return self.__injectiveMatching

    @injectiveMatching.setter
    def injectiveMatching(self, injectiveMatching: bool):
        self.__injectiveMatching = injectiveMatching

    @property
    def injectiveMatchingPresenceCondition(self) -> str:
        return self.__injectiveMatchingPresenceCondition

    @injectiveMatchingPresenceCondition.setter
    def injectiveMatchingPresenceCondition(self, injectiveMatchingPresenceCondition: str):
        self.__injectiveMatchingPresenceCondition = injectiveMatchingPresenceCondition

    @property
    def henshin_Rule21(self):
        return self.__henshin_Rule21

    @henshin_Rule21.setter
    def henshin_Rule21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule21", None)
        self.__henshin_Rule21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Rule23"):
                    opp_val = getattr(item, "henshin_Rule23", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Rule23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Rule23"):
                    opp_val = getattr(item, "henshin_Rule23", None)
                    
                    setattr(item, "henshin_Rule23", self)
                    

    @property
    def henshin_Rule25(self):
        return self.__henshin_Rule25

    @henshin_Rule25.setter
    def henshin_Rule25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule25", None)
        self.__henshin_Rule25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Mapping26"):
                    opp_val = getattr(item, "henshin_Mapping26", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Mapping26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Mapping26"):
                    opp_val = getattr(item, "henshin_Mapping26", None)
                    
                    setattr(item, "henshin_Mapping26", self)
                    

    @property
    def henshin_Rule16(self):
        return self.__henshin_Rule16

    @henshin_Rule16.setter
    def henshin_Rule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule16", None)
        self.__henshin_Rule16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph17"):
                opp_val = getattr(old_value, "henshin_Graph17", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph17"):
                opp_val = getattr(value, "henshin_Graph17", None)
                setattr(value, "henshin_Graph17", self)

    @property
    def henshin_Rule20(self):
        return self.__henshin_Rule20

    @henshin_Rule20.setter
    def henshin_Rule20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule20", None)
        self.__henshin_Rule20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Mapping"):
                    opp_val = getattr(item, "henshin_Mapping", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Mapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Mapping"):
                    opp_val = getattr(item, "henshin_Mapping", None)
                    
                    setattr(item, "henshin_Mapping", self)
                    

    @property
    def henshin_Rule(self):
        return self.__henshin_Rule

    @henshin_Rule.setter
    def henshin_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule", None)
        self.__henshin_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph14"):
                opp_val = getattr(old_value, "henshin_Graph14", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph14"):
                opp_val = getattr(value, "henshin_Graph14", None)
                setattr(value, "henshin_Graph14", self)

    @property
    def Rule(self):
        return self.__Rule

    @Rule.setter
    def Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__Rule", None)
        self.__Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributeConditions"):
                opp_val = getattr(old_value, "attributeConditions", None)
                if opp_val == self:
                    setattr(old_value, "attributeConditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributeConditions"):
                opp_val = getattr(value, "attributeConditions", None)
                setattr(value, "attributeConditions", self)

    @property
    def henshin_Rule23(self):
        return self.__henshin_Rule23

    @henshin_Rule23.setter
    def henshin_Rule23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule23", None)
        self.__henshin_Rule23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule21"):
                opp_val = getattr(old_value, "henshin_Rule21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule21"):
                opp_val = getattr(value, "henshin_Rule21", None)
                if opp_val is None:
                    setattr(value, "henshin_Rule21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__rule", None)
        self.__rule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeCondition"):
                    opp_val = getattr(item, "AttributeCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeCondition"):
                    opp_val = getattr(item, "AttributeCondition", None)
                    
                    setattr(item, "AttributeCondition", self)
                    

    def getKernelRule(self) -> str:
        # TODO: Implement getKernelRule method
        pass

    def getActionEdges(self, action: str) -> str:
        # TODO: Implement getActionEdges method
        pass

    def getAllMappings(self) -> str:
        # TODO: Implement getAllMappings method
        pass

    def removeNode(self, node: str, removeMapped: bool) -> bool:
        # TODO: Implement removeNode method
        pass

    def getParameterNodes(self) -> str:
        # TODO: Implement getParameterNodes method
        pass

    def removeAttribute(self, removeMapped: bool, attribute: str) -> bool:
        # TODO: Implement removeAttribute method
        pass

    def getMultiRule(self, name: str) -> str:
        # TODO: Implement getMultiRule method
        pass

    def isMultiRule(self) -> bool:
        # TODO: Implement isMultiRule method
        pass

    def createEdge(self, type: str, source: str, target: str) -> str:
        # TODO: Implement createEdge method
        pass

    def removeEdge(self, edge: str, removeMapped: bool) -> bool:
        # TODO: Implement removeEdge method
        pass

    def canCreateEdge(self, target: str, source: str, type: str) -> bool:
        # TODO: Implement canCreateEdge method
        pass

    def getRootRule(self) -> str:
        # TODO: Implement getRootRule method
        pass

    def getAllMultiRules(self) -> str:
        # TODO: Implement getAllMultiRules method
        pass

    def createNode(self, type: str) -> str:
        # TODO: Implement createNode method
        pass

    def getMultiRulePath(self, multiRule: str) -> str:
        # TODO: Implement getMultiRulePath method
        pass

    def getActionNodes(self, action: str) -> str:
        # TODO: Implement getActionNodes method
        pass

class henshin_Mapping:

    pass
class henshin_EPackage:

    pass
class NamedElement:

    pass
class henshin_AttributeCondition(NamedElement):

    def __init__(self, conditionText: str, AttributeCondition: "henshin_Rule" = None, attributeConditions: "henshin_Rule" = None):
        self.conditionText = conditionText
        self.AttributeCondition = AttributeCondition
        self.attributeConditions = attributeConditions
        
    @property
    def conditionText(self) -> str:
        return self.__conditionText

    @conditionText.setter
    def conditionText(self, conditionText: str):
        self.__conditionText = conditionText

    @property
    def AttributeCondition(self):
        return self.__AttributeCondition

    @AttributeCondition.setter
    def AttributeCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_AttributeCondition__AttributeCondition", None)
        self.__AttributeCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rule"):
                opp_val = getattr(old_value, "rule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rule"):
                opp_val = getattr(value, "rule", None)
                if opp_val is None:
                    setattr(value, "rule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def attributeConditions(self):
        return self.__attributeConditions

    @attributeConditions.setter
    def attributeConditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_AttributeCondition__attributeConditions", None)
        self.__attributeConditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rule"):
                opp_val = getattr(old_value, "Rule", None)
                if opp_val == self:
                    setattr(old_value, "Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rule"):
                opp_val = getattr(value, "Rule", None)
                setattr(value, "Rule", self)

class henshin_Node(NamedElement, GraphElement):

    def __init__(self, henshin_Node: "henshin_EClass" = None, node: set["henshin_Attribute"] = None, nodes: "henshin_Graph" = None, target: set["henshin_Edge"] = None, source: set["henshin_Edge"] = None, Node48: "henshin_Edge" = None, Node50: "henshin_Edge" = None, Node: "henshin_Graph" = None, henshin_Node60: "henshin_Mapping" = None, henshin_Node63: "henshin_Mapping" = None, Node56: "henshin_Attribute" = None):
        self.henshin_Node = henshin_Node
        self.node = node if node is not None else set()
        self.nodes = nodes
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Node48 = Node48
        self.Node50 = Node50
        self.Node = Node
        self.henshin_Node60 = henshin_Node60
        self.henshin_Node63 = henshin_Node63
        self.Node56 = Node56
        
    @property
    def henshin_Node63(self):
        return self.__henshin_Node63

    @henshin_Node63.setter
    def henshin_Node63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node63", None)
        self.__henshin_Node63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Mapping62"):
                opp_val = getattr(old_value, "henshin_Mapping62", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping62"):
                opp_val = getattr(value, "henshin_Mapping62", None)
                setattr(value, "henshin_Mapping62", self)

    @property
    def Node50(self):
        return self.__Node50

    @Node50.setter
    def Node50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node50", None)
        self.__Node50 = value
        
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
    def henshin_Node60(self):
        return self.__henshin_Node60

    @henshin_Node60.setter
    def henshin_Node60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node60", None)
        self.__henshin_Node60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Mapping59"):
                opp_val = getattr(old_value, "henshin_Mapping59", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping59"):
                opp_val = getattr(value, "henshin_Mapping59", None)
                setattr(value, "henshin_Mapping59", self)

    @property
    def henshin_Node(self):
        return self.__henshin_Node

    @henshin_Node.setter
    def henshin_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node", None)
        self.__henshin_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_EClass"):
                opp_val = getattr(old_value, "henshin_EClass", None)
                if opp_val == self:
                    setattr(old_value, "henshin_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_EClass"):
                opp_val = getattr(value, "henshin_EClass", None)
                setattr(value, "henshin_EClass", self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__node", None)
        self.__node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph"):
                opp_val = getattr(old_value, "Graph", None)
                if opp_val == self:
                    setattr(old_value, "Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph"):
                opp_val = getattr(value, "Graph", None)
                setattr(value, "Graph", self)

    @property
    def Node56(self):
        return self.__Node56

    @Node56.setter
    def Node56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node56", None)
        self.__Node56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge44"):
                    opp_val = getattr(item, "Edge44", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge44"):
                    opp_val = getattr(item, "Edge44", None)
                    
                    setattr(item, "Edge44", self)
                    

    @property
    def Node48(self):
        return self.__Node48

    @Node48.setter
    def Node48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node48", None)
        self.__Node48 = value
        
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
        old_value = getattr(self, f"_henshin_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge46"):
                    opp_val = getattr(item, "Edge46", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge46"):
                    opp_val = getattr(item, "Edge46", None)
                    
                    setattr(item, "Edge46", self)
                    

    def getAttribute(self, type: str) -> str:
        # TODO: Implement getAttribute method
        pass

    def getAllEdges(self) -> str:
        # TODO: Implement getAllEdges method
        pass

    def getActionNode(self) -> str:
        # TODO: Implement getActionNode method
        pass

    def getOutgoing(self, type: str, target: str) -> str:
        # TODO: Implement getOutgoing method
        pass

    def getOutgoing(self, type: str) -> str:
        # TODO: Implement getOutgoing method
        pass

    def getActionAttributes(self, action: str) -> str:
        # TODO: Implement getActionAttributes method
        pass

    def getIncoming(self, type: str) -> str:
        # TODO: Implement getIncoming method
        pass

    def getIncoming(self, source: str, type: str) -> str:
        # TODO: Implement getIncoming method
        pass

class henshin_Unit(NamedElement):

    def __init__(self, activated: bool, unit: set["henshin_Parameter"] = None, henshin_Unit12: set["henshin_ParameterMapping"] = None, henshin_Unit: "henshin_Module" = None, Unit: "henshin_Parameter" = None, henshin_Unit65: "henshin_UnaryUnit" = None, henshin_Unit67: "henshin_MultiUnit" = None, henshin_Unit69: "henshin_ConditionalUnit" = None, henshin_Unit72: "henshin_ConditionalUnit" = None, henshin_Unit75: "henshin_ConditionalUnit" = None):
        self.activated = activated
        self.unit = unit if unit is not None else set()
        self.henshin_Unit12 = henshin_Unit12 if henshin_Unit12 is not None else set()
        self.henshin_Unit = henshin_Unit
        self.Unit = Unit
        self.henshin_Unit65 = henshin_Unit65
        self.henshin_Unit67 = henshin_Unit67
        self.henshin_Unit69 = henshin_Unit69
        self.henshin_Unit72 = henshin_Unit72
        self.henshin_Unit75 = henshin_Unit75
        
    @property
    def activated(self) -> bool:
        return self.__activated

    @activated.setter
    def activated(self, activated: bool):
        self.__activated = activated

    @property
    def henshin_Unit69(self):
        return self.__henshin_Unit69

    @henshin_Unit69.setter
    def henshin_Unit69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit69", None)
        self.__henshin_Unit69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit"):
                opp_val = getattr(value, "henshin_ConditionalUnit", None)
                setattr(value, "henshin_ConditionalUnit", self)

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__unit", None)
        self.__unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def henshin_Unit12(self):
        return self.__henshin_Unit12

    @henshin_Unit12.setter
    def henshin_Unit12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit12", None)
        self.__henshin_Unit12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_ParameterMapping"):
                    opp_val = getattr(item, "henshin_ParameterMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_ParameterMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_ParameterMapping"):
                    opp_val = getattr(item, "henshin_ParameterMapping", None)
                    
                    setattr(item, "henshin_ParameterMapping", self)
                    

    @property
    def henshin_Unit72(self):
        return self.__henshin_Unit72

    @henshin_Unit72.setter
    def henshin_Unit72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit72", None)
        self.__henshin_Unit72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit71"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit71", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit71"):
                opp_val = getattr(value, "henshin_ConditionalUnit71", None)
                setattr(value, "henshin_ConditionalUnit71", self)

    @property
    def henshin_Unit65(self):
        return self.__henshin_Unit65

    @henshin_Unit65.setter
    def henshin_Unit65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit65", None)
        self.__henshin_Unit65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_UnaryUnit"):
                opp_val = getattr(old_value, "henshin_UnaryUnit", None)
                if opp_val == self:
                    setattr(old_value, "henshin_UnaryUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_UnaryUnit"):
                opp_val = getattr(value, "henshin_UnaryUnit", None)
                setattr(value, "henshin_UnaryUnit", self)

    @property
    def Unit(self):
        return self.__Unit

    @Unit.setter
    def Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__Unit", None)
        self.__Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    @property
    def henshin_Unit75(self):
        return self.__henshin_Unit75

    @henshin_Unit75.setter
    def henshin_Unit75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit75", None)
        self.__henshin_Unit75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit74"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit74", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit74"):
                opp_val = getattr(value, "henshin_ConditionalUnit74", None)
                setattr(value, "henshin_ConditionalUnit74", self)

    @property
    def henshin_Unit67(self):
        return self.__henshin_Unit67

    @henshin_Unit67.setter
    def henshin_Unit67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit67", None)
        self.__henshin_Unit67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_MultiUnit"):
                opp_val = getattr(old_value, "henshin_MultiUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_MultiUnit"):
                opp_val = getattr(value, "henshin_MultiUnit", None)
                if opp_val is None:
                    setattr(value, "henshin_MultiUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Unit(self):
        return self.__henshin_Unit

    @henshin_Unit.setter
    def henshin_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit", None)
        self.__henshin_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Module7"):
                opp_val = getattr(old_value, "henshin_Module7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Module7"):
                opp_val = getattr(value, "henshin_Module7", None)
                if opp_val is None:
                    setattr(value, "henshin_Module7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getModule(self) -> str:
        # TODO: Implement getModule method
        pass

    def getParameter(self, parameter: str) -> str:
        # TODO: Implement getParameter method
        pass

    def getSubUnits(self, deep: bool) -> str:
        # TODO: Implement getSubUnits method
        pass

class henshin_Module(NamedElement):

    def __init__(self, henshin_Module7: set["henshin_Unit"] = None, henshin_Module9: set["henshin_Graph"] = None, Module: "henshin_Module" = None, superModule: set["henshin_Module"] = None, Module4: "henshin_Module" = None, subModules: "henshin_Module" = None, henshin_Module: set["henshin_EPackage"] = None):
        self.henshin_Module7 = henshin_Module7 if henshin_Module7 is not None else set()
        self.henshin_Module9 = henshin_Module9 if henshin_Module9 is not None else set()
        self.Module = Module
        self.superModule = superModule if superModule is not None else set()
        self.Module4 = Module4
        self.subModules = subModules
        self.henshin_Module = henshin_Module if henshin_Module is not None else set()
        
    @property
    def subModules(self):
        return self.__subModules

    @subModules.setter
    def subModules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__subModules", None)
        self.__subModules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module4"):
                opp_val = getattr(old_value, "Module4", None)
                if opp_val == self:
                    setattr(old_value, "Module4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module4"):
                opp_val = getattr(value, "Module4", None)
                setattr(value, "Module4", self)

    @property
    def Module(self):
        return self.__Module

    @Module.setter
    def Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__Module", None)
        self.__Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superModule"):
                opp_val = getattr(old_value, "superModule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superModule"):
                opp_val = getattr(value, "superModule", None)
                if opp_val is None:
                    setattr(value, "superModule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Module4(self):
        return self.__Module4

    @Module4.setter
    def Module4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__Module4", None)
        self.__Module4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subModules"):
                opp_val = getattr(old_value, "subModules", None)
                if opp_val == self:
                    setattr(old_value, "subModules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subModules"):
                opp_val = getattr(value, "subModules", None)
                setattr(value, "subModules", self)

    @property
    def henshin_Module(self):
        return self.__henshin_Module

    @henshin_Module.setter
    def henshin_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__henshin_Module", None)
        self.__henshin_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_EPackage"):
                    opp_val = getattr(item, "henshin_EPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_EPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_EPackage"):
                    opp_val = getattr(item, "henshin_EPackage", None)
                    
                    setattr(item, "henshin_EPackage", self)
                    

    @property
    def henshin_Module7(self):
        return self.__henshin_Module7

    @henshin_Module7.setter
    def henshin_Module7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__henshin_Module7", None)
        self.__henshin_Module7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Unit"):
                    opp_val = getattr(item, "henshin_Unit", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Unit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Unit"):
                    opp_val = getattr(item, "henshin_Unit", None)
                    
                    setattr(item, "henshin_Unit", self)
                    

    @property
    def henshin_Module9(self):
        return self.__henshin_Module9

    @henshin_Module9.setter
    def henshin_Module9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__henshin_Module9", None)
        self.__henshin_Module9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Graph"):
                    opp_val = getattr(item, "henshin_Graph", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Graph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Graph"):
                    opp_val = getattr(item, "henshin_Graph", None)
                    
                    setattr(item, "henshin_Graph", self)
                    

    @property
    def superModule(self):
        return self.__superModule

    @superModule.setter
    def superModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__superModule", None)
        self.__superModule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Module"):
                    opp_val = getattr(item, "Module", None)
                    
                    if opp_val == self:
                        setattr(item, "Module", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Module"):
                    opp_val = getattr(item, "Module", None)
                    
                    setattr(item, "Module", self)
                    

    def getUnit(self, name: str) -> str:
        # TODO: Implement getUnit method
        pass

    def getSubModule(self, name: str) -> str:
        # TODO: Implement getSubModule method
        pass

class henshin_GraphElement(ABC):

    def __init__(self, action: str, presenceCondition: str):
        self.action = action
        self.presenceCondition = presenceCondition
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def presenceCondition(self) -> str:
        return self.__presenceCondition

    @presenceCondition.setter
    def presenceCondition(self, presenceCondition: str):
        self.__presenceCondition = presenceCondition

    def getGraph(self) -> str:
        # TODO: Implement getGraph method
        pass

class henshin_NamedElement(ABC):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class henshin_ParameterMapping:

    pass
class henshin_Parameter(NamedElement):

    pass
class henshin_Graph(NamedElement):

    def __init__(self, henshin_Graph: "henshin_Module" = None, henshin_Graph14: "henshin_Rule" = None, henshin_Graph17: "henshin_Rule" = None, Graph: "henshin_Node" = None, graph: set["henshin_Node"] = None, graph37: set["henshin_Edge"] = None, henshin_Graph39: "henshin_Formula" = None, Graph53: "henshin_Edge" = None, henshin_Graph77: "henshin_NestedCondition" = None):
        self.henshin_Graph = henshin_Graph
        self.henshin_Graph14 = henshin_Graph14
        self.henshin_Graph17 = henshin_Graph17
        self.Graph = Graph
        self.graph = graph if graph is not None else set()
        self.graph37 = graph37 if graph37 is not None else set()
        self.henshin_Graph39 = henshin_Graph39
        self.Graph53 = Graph53
        self.henshin_Graph77 = henshin_Graph77
        
    @property
    def henshin_Graph77(self):
        return self.__henshin_Graph77

    @henshin_Graph77.setter
    def henshin_Graph77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph77", None)
        self.__henshin_Graph77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_NestedCondition"):
                opp_val = getattr(old_value, "henshin_NestedCondition", None)
                if opp_val == self:
                    setattr(old_value, "henshin_NestedCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_NestedCondition"):
                opp_val = getattr(value, "henshin_NestedCondition", None)
                setattr(value, "henshin_NestedCondition", self)

    @property
    def graph37(self):
        return self.__graph37

    @graph37.setter
    def graph37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__graph37", None)
        self.__graph37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def henshin_Graph17(self):
        return self.__henshin_Graph17

    @henshin_Graph17.setter
    def henshin_Graph17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph17", None)
        self.__henshin_Graph17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule16"):
                opp_val = getattr(old_value, "henshin_Rule16", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Rule16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule16"):
                opp_val = getattr(value, "henshin_Rule16", None)
                setattr(value, "henshin_Rule16", self)

    @property
    def henshin_Graph14(self):
        return self.__henshin_Graph14

    @henshin_Graph14.setter
    def henshin_Graph14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph14", None)
        self.__henshin_Graph14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule"):
                opp_val = getattr(old_value, "henshin_Rule", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule"):
                opp_val = getattr(value, "henshin_Rule", None)
                setattr(value, "henshin_Rule", self)

    @property
    def henshin_Graph(self):
        return self.__henshin_Graph

    @henshin_Graph.setter
    def henshin_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph", None)
        self.__henshin_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Module9"):
                opp_val = getattr(old_value, "henshin_Module9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Module9"):
                opp_val = getattr(value, "henshin_Module9", None)
                if opp_val is None:
                    setattr(value, "henshin_Module9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Graph53(self):
        return self.__Graph53

    @Graph53.setter
    def Graph53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__Graph53", None)
        self.__Graph53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if opp_val == self:
                    setattr(old_value, "edges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                setattr(value, "edges", self)

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def henshin_Graph39(self):
        return self.__henshin_Graph39

    @henshin_Graph39.setter
    def henshin_Graph39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph39", None)
        self.__henshin_Graph39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Formula"):
                opp_val = getattr(old_value, "henshin_Formula", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Formula", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Formula"):
                opp_val = getattr(value, "henshin_Formula", None)
                setattr(value, "henshin_Formula", self)

    def getNestedConditions(self) -> str:
        # TODO: Implement getNestedConditions method
        pass

    def getNodes(self, nodeType: str) -> str:
        # TODO: Implement getNodes method
        pass

    def isRhs(self) -> bool:
        # TODO: Implement isRhs method
        pass

    def getRule(self) -> str:
        # TODO: Implement getRule method
        pass

    def isLhs(self) -> bool:
        # TODO: Implement isLhs method
        pass

    def createPAC(self, name: str) -> str:
        # TODO: Implement createPAC method
        pass

    def isNestedCondition(self) -> bool:
        # TODO: Implement isNestedCondition method
        pass

    def createNAC(self, name: str) -> str:
        # TODO: Implement createNAC method
        pass

    def getNode(self, name: str) -> str:
        # TODO: Implement getNode method
        pass

    def getPAC(self, name: str) -> str:
        # TODO: Implement getPAC method
        pass

    def getNACs(self) -> str:
        # TODO: Implement getNACs method
        pass

    def removeNestedCondition(self, nestedCondition: str) -> bool:
        # TODO: Implement removeNestedCondition method
        pass

    def removeEdge(self, edge: str) -> bool:
        # TODO: Implement removeEdge method
        pass

    def getEdges(self, edgeType: str) -> str:
        # TODO: Implement getEdges method
        pass

    def removeNode(self, node: str) -> bool:
        # TODO: Implement removeNode method
        pass

    def getNAC(self, name: str) -> str:
        # TODO: Implement getNAC method
        pass

    def getPACs(self) -> str:
        # TODO: Implement getPACs method
        pass
