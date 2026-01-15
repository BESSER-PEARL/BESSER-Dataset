from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterKind(Enum):
    UNKNOWN = "UNKNOWN"
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
    VAR = "VAR"


############################################
# Definition of Classes
############################################

class UnaryUnit:

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
class henshin_LoopUnit(UnaryUnit):

    pass
class henshin_EAttribute:

    pass
class MultiUnit:

    pass
class henshin_SequentialUnit(MultiUnit):

    def __init__(self, strict: bool, rollback: bool):
        self.strict = strict
        self.rollback = rollback
        
    @property
    def strict(self) -> bool:
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict

    @property
    def rollback(self) -> bool:
        return self.__rollback

    @rollback.setter
    def rollback(self, rollback: bool):
        self.__rollback = rollback

class henshin_PriorityUnit(MultiUnit):

    pass
class henshin_IndependentUnit(MultiUnit):

    pass
class henshin_EReference:

    pass
class henshin_EClass:

    pass
class GraphElement:

    pass
class henshin_Formula(ABC):

    def __init__(self, henshin_Formula: "henshin_Graph" = None, henshin_Formula83: "henshin_UnaryFormula" = None, henshin_Formula85: "henshin_BinaryFormula" = None, henshin_Formula88: "henshin_BinaryFormula" = None):
        self.henshin_Formula = henshin_Formula
        self.henshin_Formula83 = henshin_Formula83
        self.henshin_Formula85 = henshin_Formula85
        self.henshin_Formula88 = henshin_Formula88
        
    @property
    def henshin_Formula85(self):
        return self.__henshin_Formula85

    @henshin_Formula85.setter
    def henshin_Formula85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula85", None)
        self.__henshin_Formula85 = value
        
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
    def henshin_Formula(self):
        return self.__henshin_Formula

    @henshin_Formula.setter
    def henshin_Formula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula", None)
        self.__henshin_Formula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph40"):
                opp_val = getattr(old_value, "henshin_Graph40", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph40"):
                opp_val = getattr(value, "henshin_Graph40", None)
                setattr(value, "henshin_Graph40", self)

    @property
    def henshin_Formula88(self):
        return self.__henshin_Formula88

    @henshin_Formula88.setter
    def henshin_Formula88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula88", None)
        self.__henshin_Formula88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_BinaryFormula87"):
                opp_val = getattr(old_value, "henshin_BinaryFormula87", None)
                if opp_val == self:
                    setattr(old_value, "henshin_BinaryFormula87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_BinaryFormula87"):
                opp_val = getattr(value, "henshin_BinaryFormula87", None)
                setattr(value, "henshin_BinaryFormula87", self)

    @property
    def henshin_Formula83(self):
        return self.__henshin_Formula83

    @henshin_Formula83.setter
    def henshin_Formula83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula83", None)
        self.__henshin_Formula83 = value
        
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

    def isTrue(self) -> bool:
        # TODO: Implement isTrue method
        pass

    def isFalse(self) -> bool:
        # TODO: Implement isFalse method
        pass

class henshin_EClassifier:

    pass
class Unit:

    pass
class henshin_MultiUnit(Unit):

    pass
class henshin_UnaryUnit(Unit):

    pass
class henshin_ConditionalUnit(Unit):

    pass
class henshin_Rule(Unit):

    def __init__(self, checkDangling: bool, injectiveMatching: bool, javaImports: str, henshin_Rule: "henshin_Graph" = None, henshin_Rule17: "henshin_Graph" = None, henshin_Rule21: set["henshin_Mapping"] = None, henshin_Rule24: "henshin_Rule" = None, henshin_Rule22: set["henshin_Rule"] = None, henshin_Rule26: set["henshin_Mapping"] = None, rule: set["henshin_AttributeCondition"] = None, Rule: "henshin_AttributeCondition" = None):
        self.checkDangling = checkDangling
        self.injectiveMatching = injectiveMatching
        self.javaImports = javaImports
        self.henshin_Rule = henshin_Rule
        self.henshin_Rule17 = henshin_Rule17
        self.henshin_Rule21 = henshin_Rule21 if henshin_Rule21 is not None else set()
        self.henshin_Rule24 = henshin_Rule24
        self.henshin_Rule22 = henshin_Rule22 if henshin_Rule22 is not None else set()
        self.henshin_Rule26 = henshin_Rule26 if henshin_Rule26 is not None else set()
        self.rule = rule if rule is not None else set()
        self.Rule = Rule
        
    @property
    def injectiveMatching(self) -> bool:
        return self.__injectiveMatching

    @injectiveMatching.setter
    def injectiveMatching(self, injectiveMatching: bool):
        self.__injectiveMatching = injectiveMatching

    @property
    def checkDangling(self) -> bool:
        return self.__checkDangling

    @checkDangling.setter
    def checkDangling(self, checkDangling: bool):
        self.__checkDangling = checkDangling

    @property
    def javaImports(self) -> str:
        return self.__javaImports

    @javaImports.setter
    def javaImports(self, javaImports: str):
        self.__javaImports = javaImports

    @property
    def henshin_Rule17(self):
        return self.__henshin_Rule17

    @henshin_Rule17.setter
    def henshin_Rule17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule17", None)
        self.__henshin_Rule17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph18"):
                opp_val = getattr(old_value, "henshin_Graph18", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph18"):
                opp_val = getattr(value, "henshin_Graph18", None)
                setattr(value, "henshin_Graph18", self)

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
    def henshin_Rule22(self):
        return self.__henshin_Rule22

    @henshin_Rule22.setter
    def henshin_Rule22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule22", None)
        self.__henshin_Rule22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Rule24"):
                    opp_val = getattr(item, "henshin_Rule24", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Rule24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Rule24"):
                    opp_val = getattr(item, "henshin_Rule24", None)
                    
                    setattr(item, "henshin_Rule24", self)
                    

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
            if hasattr(old_value, "henshin_Graph15"):
                opp_val = getattr(old_value, "henshin_Graph15", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph15"):
                opp_val = getattr(value, "henshin_Graph15", None)
                setattr(value, "henshin_Graph15", self)

    @property
    def henshin_Rule24(self):
        return self.__henshin_Rule24

    @henshin_Rule24.setter
    def henshin_Rule24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule24", None)
        self.__henshin_Rule24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule22"):
                opp_val = getattr(old_value, "henshin_Rule22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule22"):
                opp_val = getattr(value, "henshin_Rule22", None)
                if opp_val is None:
                    setattr(value, "henshin_Rule22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Rule26(self):
        return self.__henshin_Rule26

    @henshin_Rule26.setter
    def henshin_Rule26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule26", None)
        self.__henshin_Rule26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Mapping27"):
                    opp_val = getattr(item, "henshin_Mapping27", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Mapping27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Mapping27"):
                    opp_val = getattr(item, "henshin_Mapping27", None)
                    
                    setattr(item, "henshin_Mapping27", self)
                    

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

    def getAllMultiRules(self) -> str:
        # TODO: Implement getAllMultiRules method
        pass

    def getKernelRule(self) -> str:
        # TODO: Implement getKernelRule method
        pass

    def getAllJavaImports(self) -> str:
        # TODO: Implement getAllJavaImports method
        pass

    def isMultiRule(self) -> bool:
        # TODO: Implement isMultiRule method
        pass

    def getRootRule(self) -> str:
        # TODO: Implement getRootRule method
        pass

    def createNode(self, type: str) -> str:
        # TODO: Implement createNode method
        pass

    def getMultiRule(self, name: str) -> str:
        # TODO: Implement getMultiRule method
        pass

    def removeNode(self, removeMapped: bool, node: str) -> bool:
        # TODO: Implement removeNode method
        pass

    def getActionNodes(self, action: str) -> str:
        # TODO: Implement getActionNodes method
        pass

    def getAllMappings(self) -> str:
        # TODO: Implement getAllMappings method
        pass

    def getActionEdges(self, action: str) -> str:
        # TODO: Implement getActionEdges method
        pass

    def removeEdge(self, edge: str, removeMapped: bool) -> bool:
        # TODO: Implement removeEdge method
        pass

    def removeAttribute(self, attribute: str, removeMapped: bool) -> bool:
        # TODO: Implement removeAttribute method
        pass

    def createEdge(self, source: str, target: str, type: str) -> str:
        # TODO: Implement createEdge method
        pass

    def getMultiRulePath(self, multiRule: str) -> str:
        # TODO: Implement getMultiRulePath method
        pass

    def getParameterNodes(self) -> str:
        # TODO: Implement getParameterNodes method
        pass

    def canCreateEdge(self, source: str, target: str, type: str) -> bool:
        # TODO: Implement canCreateEdge method
        pass

class henshin_EPackage:

    pass
class NamedElement:

    pass
class henshin_Parameter(NamedElement):

    def __init__(self, kind: str, Parameter: "henshin_Unit" = None, parameters: "henshin_Unit" = None, henshin_Parameter: "henshin_EClassifier" = None, henshin_Parameter32: "henshin_ParameterMapping" = None, henshin_Parameter35: "henshin_ParameterMapping" = None):
        self.kind = kind
        self.Parameter = Parameter
        self.parameters = parameters
        self.henshin_Parameter = henshin_Parameter
        self.henshin_Parameter32 = henshin_Parameter32
        self.henshin_Parameter35 = henshin_Parameter35
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def henshin_Parameter(self):
        return self.__henshin_Parameter

    @henshin_Parameter.setter
    def henshin_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Parameter__henshin_Parameter", None)
        self.__henshin_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_EClassifier"):
                opp_val = getattr(old_value, "henshin_EClassifier", None)
                if opp_val == self:
                    setattr(old_value, "henshin_EClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_EClassifier"):
                opp_val = getattr(value, "henshin_EClassifier", None)
                setattr(value, "henshin_EClassifier", self)

    @property
    def henshin_Parameter32(self):
        return self.__henshin_Parameter32

    @henshin_Parameter32.setter
    def henshin_Parameter32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Parameter__henshin_Parameter32", None)
        self.__henshin_Parameter32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ParameterMapping31"):
                opp_val = getattr(old_value, "henshin_ParameterMapping31", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ParameterMapping31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ParameterMapping31"):
                opp_val = getattr(value, "henshin_ParameterMapping31", None)
                setattr(value, "henshin_ParameterMapping31", self)

    @property
    def Parameter(self):
        return self.__Parameter

    @Parameter.setter
    def Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Parameter__Parameter", None)
        self.__Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "unit"):
                opp_val = getattr(old_value, "unit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "unit"):
                opp_val = getattr(value, "unit", None)
                if opp_val is None:
                    setattr(value, "unit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Parameter35(self):
        return self.__henshin_Parameter35

    @henshin_Parameter35.setter
    def henshin_Parameter35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Parameter__henshin_Parameter35", None)
        self.__henshin_Parameter35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ParameterMapping34"):
                opp_val = getattr(old_value, "henshin_ParameterMapping34", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ParameterMapping34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ParameterMapping34"):
                opp_val = getattr(value, "henshin_ParameterMapping34", None)
                setattr(value, "henshin_ParameterMapping34", self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Parameter__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Unit"):
                opp_val = getattr(old_value, "Unit", None)
                if opp_val == self:
                    setattr(old_value, "Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Unit"):
                opp_val = getattr(value, "Unit", None)
                setattr(value, "Unit", self)

class henshin_Node(GraphElement, NamedElement):

    def __init__(self, Node: "henshin_Graph" = None, henshin_Node: "henshin_EClass" = None, node: set["henshin_Attribute"] = None, nodes: "henshin_Graph" = None, target: set["henshin_Edge"] = None, source: set["henshin_Edge"] = None, Node49: "henshin_Edge" = None, Node51: "henshin_Edge" = None, Node57: "henshin_Attribute" = None, henshin_Node61: "henshin_Mapping" = None, henshin_Node64: "henshin_Mapping" = None):
        self.Node = Node
        self.henshin_Node = henshin_Node
        self.node = node if node is not None else set()
        self.nodes = nodes
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Node49 = Node49
        self.Node51 = Node51
        self.Node57 = Node57
        self.henshin_Node61 = henshin_Node61
        self.henshin_Node64 = henshin_Node64
        
    @property
    def henshin_Node61(self):
        return self.__henshin_Node61

    @henshin_Node61.setter
    def henshin_Node61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node61", None)
        self.__henshin_Node61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Mapping60"):
                opp_val = getattr(old_value, "henshin_Mapping60", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping60"):
                opp_val = getattr(value, "henshin_Mapping60", None)
                setattr(value, "henshin_Mapping60", self)

    @property
    def Node49(self):
        return self.__Node49

    @Node49.setter
    def Node49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node49", None)
        self.__Node49 = value
        
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
    def Node57(self):
        return self.__Node57

    @Node57.setter
    def Node57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node57", None)
        self.__Node57 = value
        
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
    def henshin_Node64(self):
        return self.__henshin_Node64

    @henshin_Node64.setter
    def henshin_Node64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node64", None)
        self.__henshin_Node64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Mapping63"):
                opp_val = getattr(old_value, "henshin_Mapping63", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping63"):
                opp_val = getattr(value, "henshin_Mapping63", None)
                setattr(value, "henshin_Mapping63", self)

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
                if hasattr(item, "Edge45"):
                    opp_val = getattr(item, "Edge45", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge45"):
                    opp_val = getattr(item, "Edge45", None)
                    
                    setattr(item, "Edge45", self)
                    

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
    def Node51(self):
        return self.__Node51

    @Node51.setter
    def Node51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node51", None)
        self.__Node51 = value
        
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
                if hasattr(item, "Edge47"):
                    opp_val = getattr(item, "Edge47", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge47"):
                    opp_val = getattr(item, "Edge47", None)
                    
                    setattr(item, "Edge47", self)
                    

    def getOutgoing(self, type: str, target: str) -> str:
        # TODO: Implement getOutgoing method
        pass

    def getOutgoing(self, type: str) -> str:
        # TODO: Implement getOutgoing method
        pass

    def getActionAttributes(self, action: str) -> str:
        # TODO: Implement getActionAttributes method
        pass

    def getAttribute(self, type: str) -> str:
        # TODO: Implement getAttribute method
        pass

    def getAllEdges(self) -> str:
        # TODO: Implement getAllEdges method
        pass

    def getIncoming(self, type: str) -> str:
        # TODO: Implement getIncoming method
        pass

    def getIncoming(self, type: str, source: str) -> str:
        # TODO: Implement getIncoming method
        pass

    def getActionNode(self) -> str:
        # TODO: Implement getActionNode method
        pass

class henshin_Graph(NamedElement):

    def __init__(self, henshin_Graph: "henshin_Module" = None, henshin_Graph15: "henshin_Rule" = None, henshin_Graph18: "henshin_Rule" = None, graph: set["henshin_Node"] = None, graph38: set["henshin_Edge"] = None, henshin_Graph40: "henshin_Formula" = None, Graph: "henshin_Node" = None, Graph54: "henshin_Edge" = None, henshin_Graph78: "henshin_NestedCondition" = None):
        self.henshin_Graph = henshin_Graph
        self.henshin_Graph15 = henshin_Graph15
        self.henshin_Graph18 = henshin_Graph18
        self.graph = graph if graph is not None else set()
        self.graph38 = graph38 if graph38 is not None else set()
        self.henshin_Graph40 = henshin_Graph40
        self.Graph = Graph
        self.Graph54 = Graph54
        self.henshin_Graph78 = henshin_Graph78
        
    @property
    def henshin_Graph18(self):
        return self.__henshin_Graph18

    @henshin_Graph18.setter
    def henshin_Graph18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph18", None)
        self.__henshin_Graph18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule17"):
                opp_val = getattr(old_value, "henshin_Rule17", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Rule17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule17"):
                opp_val = getattr(value, "henshin_Rule17", None)
                setattr(value, "henshin_Rule17", self)

    @property
    def graph38(self):
        return self.__graph38

    @graph38.setter
    def graph38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__graph38", None)
        self.__graph38 = value if value is not None else set()
        
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
    def henshin_Graph15(self):
        return self.__henshin_Graph15

    @henshin_Graph15.setter
    def henshin_Graph15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph15", None)
        self.__henshin_Graph15 = value
        
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
            if hasattr(old_value, "henshin_Module10"):
                opp_val = getattr(old_value, "henshin_Module10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Module10"):
                opp_val = getattr(value, "henshin_Module10", None)
                if opp_val is None:
                    setattr(value, "henshin_Module10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Graph40(self):
        return self.__henshin_Graph40

    @henshin_Graph40.setter
    def henshin_Graph40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph40", None)
        self.__henshin_Graph40 = value
        
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
    def henshin_Graph78(self):
        return self.__henshin_Graph78

    @henshin_Graph78.setter
    def henshin_Graph78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph78", None)
        self.__henshin_Graph78 = value
        
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
    def Graph54(self):
        return self.__Graph54

    @Graph54.setter
    def Graph54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__Graph54", None)
        self.__Graph54 = value
        
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

    def getNAC(self, name: str) -> str:
        # TODO: Implement getNAC method
        pass

    def getPAC(self, name: str) -> str:
        # TODO: Implement getPAC method
        pass

    def getNestedConditions(self) -> str:
        # TODO: Implement getNestedConditions method
        pass

    def removeNode(self, node: str) -> bool:
        # TODO: Implement removeNode method
        pass

    def removeEdge(self, edge: str) -> bool:
        # TODO: Implement removeEdge method
        pass

    def removeNestedCondition(self, nestedCondition: str) -> bool:
        # TODO: Implement removeNestedCondition method
        pass

    def createPAC(self, name: str) -> str:
        # TODO: Implement createPAC method
        pass

    def getEdges(self, edgeType: str) -> str:
        # TODO: Implement getEdges method
        pass

    def isLhs(self) -> bool:
        # TODO: Implement isLhs method
        pass

    def getNodes(self, nodeType: str) -> str:
        # TODO: Implement getNodes method
        pass

    def getRule(self) -> str:
        # TODO: Implement getRule method
        pass

    def isRhs(self) -> bool:
        # TODO: Implement isRhs method
        pass

    def getNode(self, name: str) -> str:
        # TODO: Implement getNode method
        pass

    def isNestedCondition(self) -> bool:
        # TODO: Implement isNestedCondition method
        pass

    def createNAC(self, name: str) -> str:
        # TODO: Implement createNAC method
        pass

    def getPACs(self) -> str:
        # TODO: Implement getPACs method
        pass

    def getNACs(self) -> str:
        # TODO: Implement getNACs method
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

class henshin_Unit(NamedElement):

    def __init__(self, activated: bool, henshin_Unit: "henshin_Module" = None, unit: set["henshin_Parameter"] = None, henshin_Unit13: set["henshin_ParameterMapping"] = None, Unit: "henshin_Parameter" = None, henshin_Unit66: "henshin_UnaryUnit" = None, henshin_Unit68: "henshin_MultiUnit" = None, henshin_Unit70: "henshin_ConditionalUnit" = None, henshin_Unit73: "henshin_ConditionalUnit" = None, henshin_Unit76: "henshin_ConditionalUnit" = None):
        self.activated = activated
        self.henshin_Unit = henshin_Unit
        self.unit = unit if unit is not None else set()
        self.henshin_Unit13 = henshin_Unit13 if henshin_Unit13 is not None else set()
        self.Unit = Unit
        self.henshin_Unit66 = henshin_Unit66
        self.henshin_Unit68 = henshin_Unit68
        self.henshin_Unit70 = henshin_Unit70
        self.henshin_Unit73 = henshin_Unit73
        self.henshin_Unit76 = henshin_Unit76
        
    @property
    def activated(self) -> bool:
        return self.__activated

    @activated.setter
    def activated(self, activated: bool):
        self.__activated = activated

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
            if hasattr(old_value, "henshin_Module8"):
                opp_val = getattr(old_value, "henshin_Module8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Module8"):
                opp_val = getattr(value, "henshin_Module8", None)
                if opp_val is None:
                    setattr(value, "henshin_Module8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Unit73(self):
        return self.__henshin_Unit73

    @henshin_Unit73.setter
    def henshin_Unit73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit73", None)
        self.__henshin_Unit73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit72"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit72", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit72"):
                opp_val = getattr(value, "henshin_ConditionalUnit72", None)
                setattr(value, "henshin_ConditionalUnit72", self)

    @property
    def henshin_Unit66(self):
        return self.__henshin_Unit66

    @henshin_Unit66.setter
    def henshin_Unit66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit66", None)
        self.__henshin_Unit66 = value
        
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
    def henshin_Unit13(self):
        return self.__henshin_Unit13

    @henshin_Unit13.setter
    def henshin_Unit13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit13", None)
        self.__henshin_Unit13 = value if value is not None else set()
        
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
    def henshin_Unit68(self):
        return self.__henshin_Unit68

    @henshin_Unit68.setter
    def henshin_Unit68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit68", None)
        self.__henshin_Unit68 = value
        
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
    def henshin_Unit70(self):
        return self.__henshin_Unit70

    @henshin_Unit70.setter
    def henshin_Unit70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit70", None)
        self.__henshin_Unit70 = value
        
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
    def henshin_Unit76(self):
        return self.__henshin_Unit76

    @henshin_Unit76.setter
    def henshin_Unit76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Unit__henshin_Unit76", None)
        self.__henshin_Unit76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit75"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit75", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit75"):
                opp_val = getattr(value, "henshin_ConditionalUnit75", None)
                setattr(value, "henshin_ConditionalUnit75", self)

    def getModule(self) -> str:
        # TODO: Implement getModule method
        pass

    def getSubUnits(self, deep: bool) -> str:
        # TODO: Implement getSubUnits method
        pass

    def getParameter(self, parameter: str) -> str:
        # TODO: Implement getParameter method
        pass

class henshin_Module(NamedElement):

    def __init__(self, Module: "henshin_Module" = None, superModule: set["henshin_Module"] = None, Module5: "henshin_Module" = None, subModules: "henshin_Module" = None, henshin_Module: set["henshin_EPackage"] = None, henshin_Module8: set["henshin_Unit"] = None, henshin_Module10: set["henshin_Graph"] = None):
        self.Module = Module
        self.superModule = superModule if superModule is not None else set()
        self.Module5 = Module5
        self.subModules = subModules
        self.henshin_Module = henshin_Module if henshin_Module is not None else set()
        self.henshin_Module8 = henshin_Module8 if henshin_Module8 is not None else set()
        self.henshin_Module10 = henshin_Module10 if henshin_Module10 is not None else set()
        
    @property
    def henshin_Module10(self):
        return self.__henshin_Module10

    @henshin_Module10.setter
    def henshin_Module10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__henshin_Module10", None)
        self.__henshin_Module10 = value if value is not None else set()
        
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
    def subModules(self):
        return self.__subModules

    @subModules.setter
    def subModules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__subModules", None)
        self.__subModules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module5"):
                opp_val = getattr(old_value, "Module5", None)
                if opp_val == self:
                    setattr(old_value, "Module5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module5"):
                opp_val = getattr(value, "Module5", None)
                setattr(value, "Module5", self)

    @property
    def henshin_Module8(self):
        return self.__henshin_Module8

    @henshin_Module8.setter
    def henshin_Module8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__henshin_Module8", None)
        self.__henshin_Module8 = value if value is not None else set()
        
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
    def Module5(self):
        return self.__Module5

    @Module5.setter
    def Module5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Module__Module5", None)
        self.__Module5 = value
        
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

    def getSubModule(self, name: str) -> str:
        # TODO: Implement getSubModule method
        pass

    def getUnit(self, name: str) -> str:
        # TODO: Implement getUnit method
        pass

class henshin_GraphElement(ABC):

    def __init__(self, action: str):
        self.action = action
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    def getGraph(self) -> str:
        # TODO: Implement getGraph method
        pass

class ModelElement:

    pass
class henshin_Mapping(ModelElement):

    pass
class henshin_Edge(GraphElement, ModelElement):

    def __init__(self, index: str, indexConstant: str, Edge: "henshin_Graph" = None, Edge45: "henshin_Node" = None, Edge47: "henshin_Node" = None, outgoing: "henshin_Node" = None, incoming: "henshin_Node" = None, henshin_Edge: "henshin_EReference" = None, edges: "henshin_Graph" = None):
        self.index = index
        self.indexConstant = indexConstant
        self.Edge = Edge
        self.Edge45 = Edge45
        self.Edge47 = Edge47
        self.outgoing = outgoing
        self.incoming = incoming
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
    def Edge45(self):
        return self.__Edge45

    @Edge45.setter
    def Edge45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__Edge45", None)
        self.__Edge45 = value
        
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
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node51"):
                opp_val = getattr(old_value, "Node51", None)
                if opp_val == self:
                    setattr(old_value, "Node51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node51"):
                opp_val = getattr(value, "Node51", None)
                setattr(value, "Node51", self)

    @property
    def Edge47(self):
        return self.__Edge47

    @Edge47.setter
    def Edge47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__Edge47", None)
        self.__Edge47 = value
        
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
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph38"):
                opp_val = getattr(old_value, "graph38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph38"):
                opp_val = getattr(value, "graph38", None)
                if opp_val is None:
                    setattr(value, "graph38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Graph54"):
                opp_val = getattr(old_value, "Graph54", None)
                if opp_val == self:
                    setattr(old_value, "Graph54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph54"):
                opp_val = getattr(value, "Graph54", None)
                setattr(value, "Graph54", self)

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
            if hasattr(old_value, "Node49"):
                opp_val = getattr(old_value, "Node49", None)
                if opp_val == self:
                    setattr(old_value, "Node49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node49"):
                opp_val = getattr(value, "Node49", None)
                setattr(value, "Node49", self)

    def getActionEdge(self) -> str:
        # TODO: Implement getActionEdge method
        pass

class henshin_UnaryFormula(Formula, ModelElement):

    pass
class henshin_ParameterMapping(ModelElement):

    pass
class henshin_Attribute(GraphElement, ModelElement):

    def __init__(self, constant: str, null: bool, value: str, Attribute: "henshin_Node" = None, attributes: "henshin_Node" = None, henshin_Attribute: "henshin_EAttribute" = None):
        self.constant = constant
        self.null = null
        self.value = value
        self.Attribute = Attribute
        self.attributes = attributes
        self.henshin_Attribute = henshin_Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def null(self) -> bool:
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null

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
            if hasattr(old_value, "Node57"):
                opp_val = getattr(old_value, "Node57", None)
                if opp_val == self:
                    setattr(old_value, "Node57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node57"):
                opp_val = getattr(value, "Node57", None)
                setattr(value, "Node57", self)

    def getActionAttribute(self) -> str:
        # TODO: Implement getActionAttribute method
        pass

class henshin_NamedElement(ModelElement):

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

class henshin_NestedCondition(ModelElement, Formula):

    def __init__(self, henshin_NestedCondition: "henshin_Graph" = None, henshin_NestedCondition80: set["henshin_Mapping"] = None):
        self.henshin_NestedCondition = henshin_NestedCondition
        self.henshin_NestedCondition80 = henshin_NestedCondition80 if henshin_NestedCondition80 is not None else set()
        
    @property
    def henshin_NestedCondition80(self):
        return self.__henshin_NestedCondition80

    @henshin_NestedCondition80.setter
    def henshin_NestedCondition80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_NestedCondition__henshin_NestedCondition80", None)
        self.__henshin_NestedCondition80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Mapping81"):
                    opp_val = getattr(item, "henshin_Mapping81", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Mapping81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Mapping81"):
                    opp_val = getattr(item, "henshin_Mapping81", None)
                    
                    setattr(item, "henshin_Mapping81", self)
                    

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
            if hasattr(old_value, "henshin_Graph78"):
                opp_val = getattr(old_value, "henshin_Graph78", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph78"):
                opp_val = getattr(value, "henshin_Graph78", None)
                setattr(value, "henshin_Graph78", self)

    def isNAC(self) -> bool:
        # TODO: Implement isNAC method
        pass

    def getHost(self) -> str:
        # TODO: Implement getHost method
        pass

    def isPAC(self) -> bool:
        # TODO: Implement isPAC method
        pass

class henshin_BinaryFormula(Formula, ModelElement):

    pass
class henshin_Annotation(ModelElement):

    def __init__(self, key: str, value: str, henshin_Annotation: "henshin_ModelElement" = None):
        self.key = key
        self.value = value
        self.henshin_Annotation = henshin_Annotation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def henshin_Annotation(self):
        return self.__henshin_Annotation

    @henshin_Annotation.setter
    def henshin_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Annotation__henshin_Annotation", None)
        self.__henshin_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ModelElement"):
                opp_val = getattr(old_value, "henshin_ModelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ModelElement"):
                opp_val = getattr(value, "henshin_ModelElement", None)
                if opp_val is None:
                    setattr(value, "henshin_ModelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class henshin_ModelElement(ABC):

    pass