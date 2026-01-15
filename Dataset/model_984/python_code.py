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
class henshin_UnaryFormula(Formula):

    pass
class henshin_BinaryFormula(Formula):

    pass
class henshin_NestedCondition(Formula):

    def __init__(self, henshin_NestedCondition: "henshin_Graph" = None, henshin_NestedCondition80: set["henshin_Mapping"] = None):
        self.henshin_NestedCondition = henshin_NestedCondition
        self.henshin_NestedCondition80 = henshin_NestedCondition80 if henshin_NestedCondition80 is not None else set()
        
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
                    

    def isPAC(self) -> bool:
        # TODO: Implement isPAC method
        pass

    def isNAC(self) -> bool:
        # TODO: Implement isNAC method
        pass

class henshin_ParameterMapping:

    pass
class henshin_EReference:

    pass
class henshin_EAttribute:

    pass
class henshin_EClass:

    pass
class GraphElement:

    pass
class henshin_GraphElement(ABC):

    def __init__(self):
        
    def getGraph(self) -> str:
        # TODO: Implement getGraph method
        pass

class henshin_Formula(ABC):

    def __init__(self, henshin_Formula: "henshin_Graph" = None, henshin_Formula83: "henshin_UnaryFormula" = None, henshin_Formula85: "henshin_BinaryFormula" = None, henshin_Formula88: "henshin_BinaryFormula" = None):
        self.henshin_Formula = henshin_Formula
        self.henshin_Formula83 = henshin_Formula83
        self.henshin_Formula85 = henshin_Formula85
        self.henshin_Formula88 = henshin_Formula88
        
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
            if hasattr(old_value, "henshin_Graph29"):
                opp_val = getattr(old_value, "henshin_Graph29", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph29"):
                opp_val = getattr(value, "henshin_Graph29", None)
                setattr(value, "henshin_Graph29", self)

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

    def stringRepresentation(self, recursive: bool) -> str:
        # TODO: Implement stringRepresentation method
        pass

class henshin_Edge(GraphElement):

    pass
class henshin_Attribute:

    def __init__(self, value: str, Attribute: "henshin_Node" = None, henshin_Attribute: "henshin_EAttribute" = None, attributes: "henshin_Node" = None):
        self.value = value
        self.Attribute = Attribute
        self.henshin_Attribute = henshin_Attribute
        self.attributes = attributes
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "Node47"):
                opp_val = getattr(old_value, "Node47", None)
                if opp_val == self:
                    setattr(old_value, "Node47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node47"):
                opp_val = getattr(value, "Node47", None)
                setattr(value, "Node47", self)

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

class henshin_EClassifier:

    pass
class henshin_Mapping:

    pass
class TransformationUnit:

    pass
class henshin_SequentialUnit(TransformationUnit):

    def __init__(self, strict: bool, rollback: bool, henshin_SequentialUnit: set["henshin_TransformationUnit"] = None):
        self.strict = strict
        self.rollback = rollback
        self.henshin_SequentialUnit = henshin_SequentialUnit if henshin_SequentialUnit is not None else set()
        
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

    @property
    def henshin_SequentialUnit(self):
        return self.__henshin_SequentialUnit

    @henshin_SequentialUnit.setter
    def henshin_SequentialUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_SequentialUnit__henshin_SequentialUnit", None)
        self.__henshin_SequentialUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_TransformationUnit62"):
                    opp_val = getattr(item, "henshin_TransformationUnit62", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_TransformationUnit62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_TransformationUnit62"):
                    opp_val = getattr(item, "henshin_TransformationUnit62", None)
                    
                    setattr(item, "henshin_TransformationUnit62", self)
                    

class henshin_PriorityUnit(TransformationUnit):

    pass
class henshin_IndependentUnit(TransformationUnit):

    pass
class henshin_ConditionalUnit(TransformationUnit):

    pass
class henshin_LoopUnit(TransformationUnit):

    pass
class henshin_IteratedUnit(TransformationUnit):

    def __init__(self, iterations: str, henshin_IteratedUnit: "henshin_TransformationUnit" = None):
        self.iterations = iterations
        self.henshin_IteratedUnit = henshin_IteratedUnit
        
    @property
    def iterations(self) -> str:
        return self.__iterations

    @iterations.setter
    def iterations(self, iterations: str):
        self.__iterations = iterations

    @property
    def henshin_IteratedUnit(self):
        return self.__henshin_IteratedUnit

    @henshin_IteratedUnit.setter
    def henshin_IteratedUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_IteratedUnit__henshin_IteratedUnit", None)
        self.__henshin_IteratedUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_TransformationUnit74"):
                opp_val = getattr(old_value, "henshin_TransformationUnit74", None)
                if opp_val == self:
                    setattr(old_value, "henshin_TransformationUnit74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_TransformationUnit74"):
                opp_val = getattr(value, "henshin_TransformationUnit74", None)
                setattr(value, "henshin_TransformationUnit74", self)

class henshin_EPackage:

    pass
class henshin_Rule(TransformationUnit):

    def __init__(self, checkDangling: bool, injectiveMatching: bool, henshin_Rule: "henshin_TransformationSystem" = None, henshin_Rule8: "henshin_Graph" = None, henshin_Rule11: "henshin_Graph" = None, rule: set["henshin_AttributeCondition"] = None, henshin_Rule15: set["henshin_Mapping"] = None, henshin_Rule18: "henshin_Rule" = None, henshin_Rule16: set["henshin_Rule"] = None, henshin_Rule20: set["henshin_Mapping"] = None, Rule: "henshin_AttributeCondition" = None):
        self.checkDangling = checkDangling
        self.injectiveMatching = injectiveMatching
        self.henshin_Rule = henshin_Rule
        self.henshin_Rule8 = henshin_Rule8
        self.henshin_Rule11 = henshin_Rule11
        self.rule = rule if rule is not None else set()
        self.henshin_Rule15 = henshin_Rule15 if henshin_Rule15 is not None else set()
        self.henshin_Rule18 = henshin_Rule18
        self.henshin_Rule16 = henshin_Rule16 if henshin_Rule16 is not None else set()
        self.henshin_Rule20 = henshin_Rule20 if henshin_Rule20 is not None else set()
        self.Rule = Rule
        
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
    def henshin_Rule18(self):
        return self.__henshin_Rule18

    @henshin_Rule18.setter
    def henshin_Rule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule18", None)
        self.__henshin_Rule18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule16"):
                opp_val = getattr(old_value, "henshin_Rule16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule16"):
                opp_val = getattr(value, "henshin_Rule16", None)
                if opp_val is None:
                    setattr(value, "henshin_Rule16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Rule11(self):
        return self.__henshin_Rule11

    @henshin_Rule11.setter
    def henshin_Rule11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule11", None)
        self.__henshin_Rule11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph12"):
                opp_val = getattr(old_value, "henshin_Graph12", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph12"):
                opp_val = getattr(value, "henshin_Graph12", None)
                setattr(value, "henshin_Graph12", self)

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
    def henshin_Rule15(self):
        return self.__henshin_Rule15

    @henshin_Rule15.setter
    def henshin_Rule15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule15", None)
        self.__henshin_Rule15 = value if value is not None else set()
        
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
                if hasattr(item, "henshin_Mapping21"):
                    opp_val = getattr(item, "henshin_Mapping21", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Mapping21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Mapping21"):
                    opp_val = getattr(item, "henshin_Mapping21", None)
                    
                    setattr(item, "henshin_Mapping21", self)
                    

    @property
    def henshin_Rule8(self):
        return self.__henshin_Rule8

    @henshin_Rule8.setter
    def henshin_Rule8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule8", None)
        self.__henshin_Rule8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph9"):
                opp_val = getattr(old_value, "henshin_Graph9", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph9"):
                opp_val = getattr(value, "henshin_Graph9", None)
                setattr(value, "henshin_Graph9", self)

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
            if hasattr(old_value, "henshin_TransformationSystem"):
                opp_val = getattr(old_value, "henshin_TransformationSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_TransformationSystem"):
                opp_val = getattr(value, "henshin_TransformationSystem", None)
                if opp_val is None:
                    setattr(value, "henshin_TransformationSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Rule16(self):
        return self.__henshin_Rule16

    @henshin_Rule16.setter
    def henshin_Rule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule16", None)
        self.__henshin_Rule16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Rule18"):
                    opp_val = getattr(item, "henshin_Rule18", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Rule18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Rule18"):
                    opp_val = getattr(item, "henshin_Rule18", None)
                    
                    setattr(item, "henshin_Rule18", self)
                    

    def containsMapping(self, sourceNode: str, targetNode: str) -> bool:
        # TODO: Implement containsMapping method
        pass

    def getTransformationSystem(self) -> str:
        # TODO: Implement getTransformationSystem method
        pass

    def getAllMultiRules(self) -> str:
        # TODO: Implement getAllMultiRules method
        pass

    def containsMultiMapping(self, targetNode: str, sourceNode: str) -> bool:
        # TODO: Implement containsMultiMapping method
        pass

    def getMultiRule(self, name: str) -> str:
        # TODO: Implement getMultiRule method
        pass

    def getNode(self, nodename: str, isLhs: bool) -> str:
        # TODO: Implement getNode method
        pass

    def removeNode(self, node: str, removeMapped: bool):
        # TODO: Implement removeNode method
        pass

    def getKernelRule(self) -> str:
        # TODO: Implement getKernelRule method
        pass

    def removeEdge(self, removeMapped: bool, edge: str):
        # TODO: Implement removeEdge method
        pass

    def getRootKernelRule(self) -> str:
        # TODO: Implement getRootKernelRule method
        pass

class NamedElement:

    pass
class henshin_Node(GraphElement, NamedElement):

    def __init__(self, Node: "henshin_Graph" = None, henshin_Node: "henshin_Mapping" = None, henshin_Node34: "henshin_Mapping" = None, henshin_Node36: "henshin_EClass" = None, node: set["henshin_Attribute"] = None, nodes: "henshin_Graph" = None, target: set["henshin_Edge"] = None, source: set["henshin_Edge"] = None, henshin_Node44: set["henshin_Edge"] = None, Node47: "henshin_Attribute" = None, Node49: "henshin_Edge" = None, Node51: "henshin_Edge" = None):
        self.Node = Node
        self.henshin_Node = henshin_Node
        self.henshin_Node34 = henshin_Node34
        self.henshin_Node36 = henshin_Node36
        self.node = node if node is not None else set()
        self.nodes = nodes
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.henshin_Node44 = henshin_Node44 if henshin_Node44 is not None else set()
        self.Node47 = Node47
        self.Node49 = Node49
        self.Node51 = Node51
        
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
            if hasattr(old_value, "henshin_Mapping31"):
                opp_val = getattr(old_value, "henshin_Mapping31", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping31"):
                opp_val = getattr(value, "henshin_Mapping31", None)
                setattr(value, "henshin_Mapping31", self)

    @property
    def Node47(self):
        return self.__Node47

    @Node47.setter
    def Node47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node47", None)
        self.__Node47 = value
        
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
    def henshin_Node36(self):
        return self.__henshin_Node36

    @henshin_Node36.setter
    def henshin_Node36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node36", None)
        self.__henshin_Node36 = value
        
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
    def henshin_Node34(self):
        return self.__henshin_Node34

    @henshin_Node34.setter
    def henshin_Node34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node34", None)
        self.__henshin_Node34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Mapping33"):
                opp_val = getattr(old_value, "henshin_Mapping33", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping33"):
                opp_val = getattr(value, "henshin_Mapping33", None)
                setattr(value, "henshin_Mapping33", self)

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
                if hasattr(item, "Edge40"):
                    opp_val = getattr(item, "Edge40", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge40"):
                    opp_val = getattr(item, "Edge40", None)
                    
                    setattr(item, "Edge40", self)
                    

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
    def henshin_Node44(self):
        return self.__henshin_Node44

    @henshin_Node44.setter
    def henshin_Node44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node44", None)
        self.__henshin_Node44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Edge"):
                    opp_val = getattr(item, "henshin_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Edge"):
                    opp_val = getattr(item, "henshin_Edge", None)
                    
                    setattr(item, "henshin_Edge", self)
                    

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
                if hasattr(item, "Edge42"):
                    opp_val = getattr(item, "Edge42", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge42"):
                    opp_val = getattr(item, "Edge42", None)
                    
                    setattr(item, "Edge42", self)
                    

    def getAttribute(self, type: str) -> str:
        # TODO: Implement getAttribute method
        pass

    def getIncoming(self, source: str, type: str) -> str:
        # TODO: Implement getIncoming method
        pass

    def getOutgoing(self, type: str) -> str:
        # TODO: Implement getOutgoing method
        pass

    def getIncoming(self, type: str) -> str:
        # TODO: Implement getIncoming method
        pass

    def getOutgoing(self, type: str, target: str) -> str:
        # TODO: Implement getOutgoing method
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

class henshin_Graph(NamedElement):

    def __init__(self, henshin_Graph: "henshin_TransformationSystem" = None, henshin_Graph9: "henshin_Rule" = None, henshin_Graph12: "henshin_Rule" = None, graph: set["henshin_Node"] = None, graph27: set["henshin_Edge"] = None, henshin_Graph29: "henshin_Formula" = None, Graph: "henshin_Node" = None, Graph55: "henshin_Edge" = None, henshin_Graph78: "henshin_NestedCondition" = None):
        self.henshin_Graph = henshin_Graph
        self.henshin_Graph9 = henshin_Graph9
        self.henshin_Graph12 = henshin_Graph12
        self.graph = graph if graph is not None else set()
        self.graph27 = graph27 if graph27 is not None else set()
        self.henshin_Graph29 = henshin_Graph29
        self.Graph = Graph
        self.Graph55 = Graph55
        self.henshin_Graph78 = henshin_Graph78
        
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
    def Graph55(self):
        return self.__Graph55

    @Graph55.setter
    def Graph55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__Graph55", None)
        self.__Graph55 = value
        
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
    def henshin_Graph29(self):
        return self.__henshin_Graph29

    @henshin_Graph29.setter
    def henshin_Graph29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph29", None)
        self.__henshin_Graph29 = value
        
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
    def henshin_Graph12(self):
        return self.__henshin_Graph12

    @henshin_Graph12.setter
    def henshin_Graph12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph12", None)
        self.__henshin_Graph12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule11"):
                opp_val = getattr(old_value, "henshin_Rule11", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Rule11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule11"):
                opp_val = getattr(value, "henshin_Rule11", None)
                setattr(value, "henshin_Rule11", self)

    @property
    def graph27(self):
        return self.__graph27

    @graph27.setter
    def graph27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__graph27", None)
        self.__graph27 = value if value is not None else set()
        
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
    def henshin_Graph(self):
        return self.__henshin_Graph

    @henshin_Graph.setter
    def henshin_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph", None)
        self.__henshin_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_TransformationSystem6"):
                opp_val = getattr(old_value, "henshin_TransformationSystem6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_TransformationSystem6"):
                opp_val = getattr(value, "henshin_TransformationSystem6", None)
                if opp_val is None:
                    setattr(value, "henshin_TransformationSystem6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def henshin_Graph9(self):
        return self.__henshin_Graph9

    @henshin_Graph9.setter
    def henshin_Graph9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph9", None)
        self.__henshin_Graph9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule8"):
                opp_val = getattr(old_value, "henshin_Rule8", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Rule8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule8"):
                opp_val = getattr(value, "henshin_Rule8", None)
                setattr(value, "henshin_Rule8", self)

    def getNodes(self, nodeType: str) -> str:
        # TODO: Implement getNodes method
        pass

    def removeNode(self, node: str):
        # TODO: Implement removeNode method
        pass

    def isRhs(self) -> bool:
        # TODO: Implement isRhs method
        pass

    def isNestedCondition(self) -> bool:
        # TODO: Implement isNestedCondition method
        pass

    def isLhs(self) -> bool:
        # TODO: Implement isLhs method
        pass

    def getEdges(self, edgeType: str) -> str:
        # TODO: Implement getEdges method
        pass

    def removeEdge(self, edge: str):
        # TODO: Implement removeEdge method
        pass

    def getContainerRule(self) -> str:
        # TODO: Implement getContainerRule method
        pass

class henshin_Parameter(NamedElement):

    pass
class henshin_TransformationUnit(NamedElement):

    def __init__(self, activated: bool, henshin_TransformationUnit: "henshin_TransformationSystem" = None, TransformationUnit: "henshin_Parameter" = None, unit: set["henshin_Parameter"] = None, henshin_TransformationUnit58: set["henshin_ParameterMapping"] = None, henshin_TransformationUnit60: "henshin_IndependentUnit" = None, henshin_TransformationUnit62: "henshin_SequentialUnit" = None, henshin_TransformationUnit64: "henshin_ConditionalUnit" = None, henshin_TransformationUnit67: "henshin_ConditionalUnit" = None, henshin_TransformationUnit70: "henshin_ConditionalUnit" = None, henshin_TransformationUnit72: "henshin_PriorityUnit" = None, henshin_TransformationUnit74: "henshin_IteratedUnit" = None, henshin_TransformationUnit76: "henshin_LoopUnit" = None):
        self.activated = activated
        self.henshin_TransformationUnit = henshin_TransformationUnit
        self.TransformationUnit = TransformationUnit
        self.unit = unit if unit is not None else set()
        self.henshin_TransformationUnit58 = henshin_TransformationUnit58 if henshin_TransformationUnit58 is not None else set()
        self.henshin_TransformationUnit60 = henshin_TransformationUnit60
        self.henshin_TransformationUnit62 = henshin_TransformationUnit62
        self.henshin_TransformationUnit64 = henshin_TransformationUnit64
        self.henshin_TransformationUnit67 = henshin_TransformationUnit67
        self.henshin_TransformationUnit70 = henshin_TransformationUnit70
        self.henshin_TransformationUnit72 = henshin_TransformationUnit72
        self.henshin_TransformationUnit74 = henshin_TransformationUnit74
        self.henshin_TransformationUnit76 = henshin_TransformationUnit76
        
    @property
    def activated(self) -> bool:
        return self.__activated

    @activated.setter
    def activated(self, activated: bool):
        self.__activated = activated

    @property
    def henshin_TransformationUnit58(self):
        return self.__henshin_TransformationUnit58

    @henshin_TransformationUnit58.setter
    def henshin_TransformationUnit58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit58", None)
        self.__henshin_TransformationUnit58 = value if value is not None else set()
        
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
    def henshin_TransformationUnit74(self):
        return self.__henshin_TransformationUnit74

    @henshin_TransformationUnit74.setter
    def henshin_TransformationUnit74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit74", None)
        self.__henshin_TransformationUnit74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_IteratedUnit"):
                opp_val = getattr(old_value, "henshin_IteratedUnit", None)
                if opp_val == self:
                    setattr(old_value, "henshin_IteratedUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_IteratedUnit"):
                opp_val = getattr(value, "henshin_IteratedUnit", None)
                setattr(value, "henshin_IteratedUnit", self)

    @property
    def henshin_TransformationUnit67(self):
        return self.__henshin_TransformationUnit67

    @henshin_TransformationUnit67.setter
    def henshin_TransformationUnit67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit67", None)
        self.__henshin_TransformationUnit67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit66"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit66", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit66"):
                opp_val = getattr(value, "henshin_ConditionalUnit66", None)
                setattr(value, "henshin_ConditionalUnit66", self)

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__unit", None)
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
    def henshin_TransformationUnit(self):
        return self.__henshin_TransformationUnit

    @henshin_TransformationUnit.setter
    def henshin_TransformationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit", None)
        self.__henshin_TransformationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_TransformationSystem4"):
                opp_val = getattr(old_value, "henshin_TransformationSystem4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_TransformationSystem4"):
                opp_val = getattr(value, "henshin_TransformationSystem4", None)
                if opp_val is None:
                    setattr(value, "henshin_TransformationSystem4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_TransformationUnit64(self):
        return self.__henshin_TransformationUnit64

    @henshin_TransformationUnit64.setter
    def henshin_TransformationUnit64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit64", None)
        self.__henshin_TransformationUnit64 = value
        
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
    def henshin_TransformationUnit62(self):
        return self.__henshin_TransformationUnit62

    @henshin_TransformationUnit62.setter
    def henshin_TransformationUnit62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit62", None)
        self.__henshin_TransformationUnit62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_SequentialUnit"):
                opp_val = getattr(old_value, "henshin_SequentialUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_SequentialUnit"):
                opp_val = getattr(value, "henshin_SequentialUnit", None)
                if opp_val is None:
                    setattr(value, "henshin_SequentialUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_TransformationUnit60(self):
        return self.__henshin_TransformationUnit60

    @henshin_TransformationUnit60.setter
    def henshin_TransformationUnit60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit60", None)
        self.__henshin_TransformationUnit60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_IndependentUnit"):
                opp_val = getattr(old_value, "henshin_IndependentUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_IndependentUnit"):
                opp_val = getattr(value, "henshin_IndependentUnit", None)
                if opp_val is None:
                    setattr(value, "henshin_IndependentUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_TransformationUnit76(self):
        return self.__henshin_TransformationUnit76

    @henshin_TransformationUnit76.setter
    def henshin_TransformationUnit76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit76", None)
        self.__henshin_TransformationUnit76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_LoopUnit"):
                opp_val = getattr(old_value, "henshin_LoopUnit", None)
                if opp_val == self:
                    setattr(old_value, "henshin_LoopUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_LoopUnit"):
                opp_val = getattr(value, "henshin_LoopUnit", None)
                setattr(value, "henshin_LoopUnit", self)

    @property
    def TransformationUnit(self):
        return self.__TransformationUnit

    @TransformationUnit.setter
    def TransformationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__TransformationUnit", None)
        self.__TransformationUnit = value
        
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
    def henshin_TransformationUnit72(self):
        return self.__henshin_TransformationUnit72

    @henshin_TransformationUnit72.setter
    def henshin_TransformationUnit72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit72", None)
        self.__henshin_TransformationUnit72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_PriorityUnit"):
                opp_val = getattr(old_value, "henshin_PriorityUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_PriorityUnit"):
                opp_val = getattr(value, "henshin_PriorityUnit", None)
                if opp_val is None:
                    setattr(value, "henshin_PriorityUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_TransformationUnit70(self):
        return self.__henshin_TransformationUnit70

    @henshin_TransformationUnit70.setter
    def henshin_TransformationUnit70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit70", None)
        self.__henshin_TransformationUnit70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit69"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit69", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit69"):
                opp_val = getattr(value, "henshin_ConditionalUnit69", None)
                setattr(value, "henshin_ConditionalUnit69", self)

    def getSubUnits(self, deep: bool) -> TransformationUnit:
        # TODO: Implement getSubUnits method
        pass

    def getParameter(self, parameter: str) -> str:
        # TODO: Implement getParameter method
        pass

class henshin_TransformationSystem(NamedElement):

    def __init__(self, henshin_TransformationSystem: set["henshin_Rule"] = None, henshin_TransformationSystem2: set["henshin_EPackage"] = None, henshin_TransformationSystem4: set["henshin_TransformationUnit"] = None, henshin_TransformationSystem6: set["henshin_Graph"] = None):
        self.henshin_TransformationSystem = henshin_TransformationSystem if henshin_TransformationSystem is not None else set()
        self.henshin_TransformationSystem2 = henshin_TransformationSystem2 if henshin_TransformationSystem2 is not None else set()
        self.henshin_TransformationSystem4 = henshin_TransformationSystem4 if henshin_TransformationSystem4 is not None else set()
        self.henshin_TransformationSystem6 = henshin_TransformationSystem6 if henshin_TransformationSystem6 is not None else set()
        
    @property
    def henshin_TransformationSystem(self):
        return self.__henshin_TransformationSystem

    @henshin_TransformationSystem.setter
    def henshin_TransformationSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__henshin_TransformationSystem", None)
        self.__henshin_TransformationSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Rule"):
                    opp_val = getattr(item, "henshin_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Rule"):
                    opp_val = getattr(item, "henshin_Rule", None)
                    
                    setattr(item, "henshin_Rule", self)
                    

    @property
    def henshin_TransformationSystem4(self):
        return self.__henshin_TransformationSystem4

    @henshin_TransformationSystem4.setter
    def henshin_TransformationSystem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__henshin_TransformationSystem4", None)
        self.__henshin_TransformationSystem4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_TransformationUnit"):
                    opp_val = getattr(item, "henshin_TransformationUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_TransformationUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_TransformationUnit"):
                    opp_val = getattr(item, "henshin_TransformationUnit", None)
                    
                    setattr(item, "henshin_TransformationUnit", self)
                    

    @property
    def henshin_TransformationSystem2(self):
        return self.__henshin_TransformationSystem2

    @henshin_TransformationSystem2.setter
    def henshin_TransformationSystem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__henshin_TransformationSystem2", None)
        self.__henshin_TransformationSystem2 = value if value is not None else set()
        
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
    def henshin_TransformationSystem6(self):
        return self.__henshin_TransformationSystem6

    @henshin_TransformationSystem6.setter
    def henshin_TransformationSystem6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__henshin_TransformationSystem6", None)
        self.__henshin_TransformationSystem6 = value if value is not None else set()
        
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
                    

    def getTransformationUnit(self, unitName: str) -> str:
        # TODO: Implement getTransformationUnit method
        pass

    def getRule(self, ruleName: str) -> str:
        # TODO: Implement getRule method
        pass

class henshin_NamedElement(ABC):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
