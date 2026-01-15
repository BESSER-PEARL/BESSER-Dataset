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

    def __init__(self, negated: bool, henshin_NestedCondition: "henshin_Graph" = None, henshin_NestedCondition82: set["henshin_Mapping"] = None):
        self.negated = negated
        self.henshin_NestedCondition = henshin_NestedCondition
        self.henshin_NestedCondition82 = henshin_NestedCondition82 if henshin_NestedCondition82 is not None else set()
        
    @property
    def negated(self) -> bool:
        return self.__negated

    @negated.setter
    def negated(self, negated: bool):
        self.__negated = negated

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
            if hasattr(old_value, "henshin_Graph80"):
                opp_val = getattr(old_value, "henshin_Graph80", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph80"):
                opp_val = getattr(value, "henshin_Graph80", None)
                setattr(value, "henshin_Graph80", self)

    @property
    def henshin_NestedCondition82(self):
        return self.__henshin_NestedCondition82

    @henshin_NestedCondition82.setter
    def henshin_NestedCondition82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_NestedCondition__henshin_NestedCondition82", None)
        self.__henshin_NestedCondition82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "henshin_Mapping83"):
                    opp_val = getattr(item, "henshin_Mapping83", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_Mapping83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_Mapping83"):
                    opp_val = getattr(item, "henshin_Mapping83", None)
                    
                    setattr(item, "henshin_Mapping83", self)
                    

class henshin_EReference:

    pass
class henshin_ParameterMapping:

    pass
class GraphElement:

    pass
class henshin_EAttribute:

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
            if hasattr(old_value, "Node40"):
                opp_val = getattr(old_value, "Node40", None)
                if opp_val == self:
                    setattr(old_value, "Node40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node40"):
                opp_val = getattr(value, "Node40", None)
                setattr(value, "Node40", self)

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

class henshin_EClass:

    pass
class henshin_GraphElement(ABC):

    def __init__(self):
        
    def getGraph(self) -> str:
        # TODO: Implement getGraph method
        pass

class henshin_Formula(ABC):

    def __init__(self, henshin_Formula: "henshin_Graph" = None, henshin_Formula90: "henshin_BinaryFormula" = None, henshin_Formula85: "henshin_UnaryFormula" = None, henshin_Formula87: "henshin_BinaryFormula" = None):
        self.henshin_Formula = henshin_Formula
        self.henshin_Formula90 = henshin_Formula90
        self.henshin_Formula85 = henshin_Formula85
        self.henshin_Formula87 = henshin_Formula87
        
    @property
    def henshin_Formula90(self):
        return self.__henshin_Formula90

    @henshin_Formula90.setter
    def henshin_Formula90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula90", None)
        self.__henshin_Formula90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_BinaryFormula89"):
                opp_val = getattr(old_value, "henshin_BinaryFormula89", None)
                if opp_val == self:
                    setattr(old_value, "henshin_BinaryFormula89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_BinaryFormula89"):
                opp_val = getattr(value, "henshin_BinaryFormula89", None)
                setattr(value, "henshin_BinaryFormula89", self)

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
            if hasattr(old_value, "henshin_Graph22"):
                opp_val = getattr(old_value, "henshin_Graph22", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph22"):
                opp_val = getattr(value, "henshin_Graph22", None)
                setattr(value, "henshin_Graph22", self)

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
    def henshin_Formula87(self):
        return self.__henshin_Formula87

    @henshin_Formula87.setter
    def henshin_Formula87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Formula__henshin_Formula87", None)
        self.__henshin_Formula87 = value
        
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

    def stringRepresentation(self, recursive: bool) -> str:
        # TODO: Implement stringRepresentation method
        pass

class henshin_Edge(GraphElement):

    pass
class henshin_EPackage:

    pass
class henshin_Mapping:

    pass
class TransformationUnit:

    pass
class henshin_ConditionalUnit(TransformationUnit):

    pass
class henshin_AmalgamationUnit(TransformationUnit):

    pass
class henshin_CountedUnit(TransformationUnit):

    def __init__(self, count: int, henshin_CountedUnit: "henshin_TransformationUnit" = None):
        self.count = count
        self.henshin_CountedUnit = henshin_CountedUnit
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def henshin_CountedUnit(self):
        return self.__henshin_CountedUnit

    @henshin_CountedUnit.setter
    def henshin_CountedUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_CountedUnit__henshin_CountedUnit", None)
        self.__henshin_CountedUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_TransformationUnit78"):
                opp_val = getattr(old_value, "henshin_TransformationUnit78", None)
                if opp_val == self:
                    setattr(old_value, "henshin_TransformationUnit78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_TransformationUnit78"):
                opp_val = getattr(value, "henshin_TransformationUnit78", None)
                setattr(value, "henshin_TransformationUnit78", self)

class henshin_SequentialUnit(TransformationUnit):

    def __init__(self, strict: bool, rollback: bool, henshin_SequentialUnit: set["henshin_TransformationUnit"] = None):
        self.strict = strict
        self.rollback = rollback
        self.henshin_SequentialUnit = henshin_SequentialUnit if henshin_SequentialUnit is not None else set()
        
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
                if hasattr(item, "henshin_TransformationUnit55"):
                    opp_val = getattr(item, "henshin_TransformationUnit55", None)
                    
                    if opp_val == self:
                        setattr(item, "henshin_TransformationUnit55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "henshin_TransformationUnit55"):
                    opp_val = getattr(item, "henshin_TransformationUnit55", None)
                    
                    setattr(item, "henshin_TransformationUnit55", self)
                    

class henshin_IndependentUnit(TransformationUnit):

    pass
class henshin_PriorityUnit(TransformationUnit):

    pass
class henshin_Rule(TransformationUnit):

    def __init__(self, henshin_Rule: "henshin_Graph" = None, henshin_Rule9: "henshin_Graph" = None, rule: set["henshin_AttributeCondition"] = None, henshin_Rule13: set["henshin_Mapping"] = None, rules: "henshin_TransformationSystem" = None, Rule16: "henshin_AttributeCondition" = None, Rule: "henshin_TransformationSystem" = None, henshin_Rule67: "henshin_AmalgamationUnit" = None, henshin_Rule70: "henshin_AmalgamationUnit" = None):
        self.henshin_Rule = henshin_Rule
        self.henshin_Rule9 = henshin_Rule9
        self.rule = rule if rule is not None else set()
        self.henshin_Rule13 = henshin_Rule13 if henshin_Rule13 is not None else set()
        self.rules = rules
        self.Rule16 = Rule16
        self.Rule = Rule
        self.henshin_Rule67 = henshin_Rule67
        self.henshin_Rule70 = henshin_Rule70
        
    @property
    def henshin_Rule67(self):
        return self.__henshin_Rule67

    @henshin_Rule67.setter
    def henshin_Rule67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule67", None)
        self.__henshin_Rule67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_AmalgamationUnit"):
                opp_val = getattr(old_value, "henshin_AmalgamationUnit", None)
                if opp_val == self:
                    setattr(old_value, "henshin_AmalgamationUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_AmalgamationUnit"):
                opp_val = getattr(value, "henshin_AmalgamationUnit", None)
                setattr(value, "henshin_AmalgamationUnit", self)

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
            if hasattr(old_value, "henshin_Graph7"):
                opp_val = getattr(old_value, "henshin_Graph7", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph7"):
                opp_val = getattr(value, "henshin_Graph7", None)
                setattr(value, "henshin_Graph7", self)

    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__rules", None)
        self.__rules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransformationSystem"):
                opp_val = getattr(old_value, "TransformationSystem", None)
                if opp_val == self:
                    setattr(old_value, "TransformationSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransformationSystem"):
                opp_val = getattr(value, "TransformationSystem", None)
                setattr(value, "TransformationSystem", self)

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
            if hasattr(old_value, "transformationSystem"):
                opp_val = getattr(old_value, "transformationSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transformationSystem"):
                opp_val = getattr(value, "transformationSystem", None)
                if opp_val is None:
                    setattr(value, "transformationSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Rule13(self):
        return self.__henshin_Rule13

    @henshin_Rule13.setter
    def henshin_Rule13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule13", None)
        self.__henshin_Rule13 = value if value is not None else set()
        
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
    def henshin_Rule9(self):
        return self.__henshin_Rule9

    @henshin_Rule9.setter
    def henshin_Rule9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule9", None)
        self.__henshin_Rule9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Graph10"):
                opp_val = getattr(old_value, "henshin_Graph10", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Graph10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Graph10"):
                opp_val = getattr(value, "henshin_Graph10", None)
                setattr(value, "henshin_Graph10", self)

    @property
    def henshin_Rule70(self):
        return self.__henshin_Rule70

    @henshin_Rule70.setter
    def henshin_Rule70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__henshin_Rule70", None)
        self.__henshin_Rule70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_AmalgamationUnit69"):
                opp_val = getattr(old_value, "henshin_AmalgamationUnit69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_AmalgamationUnit69"):
                opp_val = getattr(value, "henshin_AmalgamationUnit69", None)
                if opp_val is None:
                    setattr(value, "henshin_AmalgamationUnit69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rule16(self):
        return self.__Rule16

    @Rule16.setter
    def Rule16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Rule__Rule16", None)
        self.__Rule16 = value
        
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

    def getNodeByName(self, isLhs: bool, nodename: str) -> str:
        # TODO: Implement getNodeByName method
        pass

    def containsMapping(self, sourceNode: str, targetNode: str) -> bool:
        # TODO: Implement containsMapping method
        pass

class NamedElement:

    pass
class henshin_Graph(NamedElement):

    def __init__(self, henshin_Graph: "henshin_TransformationSystem" = None, henshin_Graph7: "henshin_Rule" = None, henshin_Graph10: "henshin_Rule" = None, graph: set["henshin_Node"] = None, graph20: set["henshin_Edge"] = None, henshin_Graph22: "henshin_Formula" = None, Graph: "henshin_Node" = None, Graph48: "henshin_Edge" = None, henshin_Graph80: "henshin_NestedCondition" = None):
        self.henshin_Graph = henshin_Graph
        self.henshin_Graph7 = henshin_Graph7
        self.henshin_Graph10 = henshin_Graph10
        self.graph = graph if graph is not None else set()
        self.graph20 = graph20 if graph20 is not None else set()
        self.henshin_Graph22 = henshin_Graph22
        self.Graph = Graph
        self.Graph48 = Graph48
        self.henshin_Graph80 = henshin_Graph80
        
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
            if hasattr(old_value, "henshin_TransformationSystem3"):
                opp_val = getattr(old_value, "henshin_TransformationSystem3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_TransformationSystem3"):
                opp_val = getattr(value, "henshin_TransformationSystem3", None)
                if opp_val is None:
                    setattr(value, "henshin_TransformationSystem3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_Graph80(self):
        return self.__henshin_Graph80

    @henshin_Graph80.setter
    def henshin_Graph80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph80", None)
        self.__henshin_Graph80 = value
        
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
    def Graph48(self):
        return self.__Graph48

    @Graph48.setter
    def Graph48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__Graph48", None)
        self.__Graph48 = value
        
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
    def henshin_Graph22(self):
        return self.__henshin_Graph22

    @henshin_Graph22.setter
    def henshin_Graph22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph22", None)
        self.__henshin_Graph22 = value
        
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
    def graph20(self):
        return self.__graph20

    @graph20.setter
    def graph20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__graph20", None)
        self.__graph20 = value if value is not None else set()
        
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
    def henshin_Graph7(self):
        return self.__henshin_Graph7

    @henshin_Graph7.setter
    def henshin_Graph7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph7", None)
        self.__henshin_Graph7 = value
        
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
    def henshin_Graph10(self):
        return self.__henshin_Graph10

    @henshin_Graph10.setter
    def henshin_Graph10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Graph__henshin_Graph10", None)
        self.__henshin_Graph10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Rule9"):
                opp_val = getattr(old_value, "henshin_Rule9", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Rule9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Rule9"):
                opp_val = getattr(value, "henshin_Rule9", None)
                setattr(value, "henshin_Rule9", self)

    def removeEdge(self, edge: str):
        # TODO: Implement removeEdge method
        pass

    def getContainerRule(self) -> str:
        # TODO: Implement getContainerRule method
        pass

    def removeNode(self, node: str):
        # TODO: Implement removeNode method
        pass

    def findEdgesByType(self, edgeType: str) -> str:
        # TODO: Implement findEdgesByType method
        pass

    def findNodesByType(self, nodeType: str) -> str:
        # TODO: Implement findNodesByType method
        pass

class henshin_Node(GraphElement, NamedElement):

    def __init__(self, Node: "henshin_Graph" = None, henshin_Node: "henshin_Mapping" = None, henshin_Node27: "henshin_Mapping" = None, henshin_Node29: "henshin_EClass" = None, node: set["henshin_Attribute"] = None, nodes: "henshin_Graph" = None, target: set["henshin_Edge"] = None, source: set["henshin_Edge"] = None, henshin_Node37: set["henshin_Edge"] = None, Node40: "henshin_Attribute" = None, Node42: "henshin_Edge" = None, Node44: "henshin_Edge" = None):
        self.Node = Node
        self.henshin_Node = henshin_Node
        self.henshin_Node27 = henshin_Node27
        self.henshin_Node29 = henshin_Node29
        self.node = node if node is not None else set()
        self.nodes = nodes
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.henshin_Node37 = henshin_Node37 if henshin_Node37 is not None else set()
        self.Node40 = Node40
        self.Node42 = Node42
        self.Node44 = Node44
        
    @property
    def henshin_Node29(self):
        return self.__henshin_Node29

    @henshin_Node29.setter
    def henshin_Node29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node29", None)
        self.__henshin_Node29 = value
        
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
    def Node44(self):
        return self.__Node44

    @Node44.setter
    def Node44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node44", None)
        self.__Node44 = value
        
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
    def henshin_Node27(self):
        return self.__henshin_Node27

    @henshin_Node27.setter
    def henshin_Node27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node27", None)
        self.__henshin_Node27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_Mapping26"):
                opp_val = getattr(old_value, "henshin_Mapping26", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping26"):
                opp_val = getattr(value, "henshin_Mapping26", None)
                setattr(value, "henshin_Mapping26", self)

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
                if hasattr(item, "Edge33"):
                    opp_val = getattr(item, "Edge33", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge33"):
                    opp_val = getattr(item, "Edge33", None)
                    
                    setattr(item, "Edge33", self)
                    

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
            if hasattr(old_value, "henshin_Mapping24"):
                opp_val = getattr(old_value, "henshin_Mapping24", None)
                if opp_val == self:
                    setattr(old_value, "henshin_Mapping24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_Mapping24"):
                opp_val = getattr(value, "henshin_Mapping24", None)
                setattr(value, "henshin_Mapping24", self)

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
                if hasattr(item, "Edge35"):
                    opp_val = getattr(item, "Edge35", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge35"):
                    opp_val = getattr(item, "Edge35", None)
                    
                    setattr(item, "Edge35", self)
                    

    @property
    def henshin_Node37(self):
        return self.__henshin_Node37

    @henshin_Node37.setter
    def henshin_Node37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__henshin_Node37", None)
        self.__henshin_Node37 = value if value is not None else set()
        
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
    def Node42(self):
        return self.__Node42

    @Node42.setter
    def Node42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node42", None)
        self.__Node42 = value
        
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
    def Node40(self):
        return self.__Node40

    @Node40.setter
    def Node40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_Node__Node40", None)
        self.__Node40 = value
        
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

    def findAttributeByType(self, attributeType: str) -> str:
        # TODO: Implement findAttributeByType method
        pass

    def findIncomingEdgeByType(self, sourceNode: str, edgeType: str) -> str:
        # TODO: Implement findIncomingEdgeByType method
        pass

    def findOutgoingEdgeByType(self, edgeType: str, targetNode: str) -> str:
        # TODO: Implement findOutgoingEdgeByType method
        pass

    def findOutgoingEdgesByType(self, edgeType: str) -> str:
        # TODO: Implement findOutgoingEdgesByType method
        pass

    def findIncomingEdgesByType(self, edgeType: str) -> str:
        # TODO: Implement findIncomingEdgesByType method
        pass

class DescribedElement:

    pass
class henshin_Parameter(NamedElement, DescribedElement):

    pass
class henshin_TransformationUnit(NamedElement, DescribedElement):

    def __init__(self, activated: bool, henshin_TransformationUnit: "henshin_TransformationSystem" = None, TransformationUnit: "henshin_Parameter" = None, unit: set["henshin_Parameter"] = None, henshin_TransformationUnit51: set["henshin_ParameterMapping"] = None, henshin_TransformationUnit53: "henshin_IndependentUnit" = None, henshin_TransformationUnit55: "henshin_SequentialUnit" = None, henshin_TransformationUnit57: "henshin_ConditionalUnit" = None, henshin_TransformationUnit78: "henshin_CountedUnit" = None, henshin_TransformationUnit60: "henshin_ConditionalUnit" = None, henshin_TransformationUnit63: "henshin_ConditionalUnit" = None, henshin_TransformationUnit65: "henshin_PriorityUnit" = None):
        self.activated = activated
        self.henshin_TransformationUnit = henshin_TransformationUnit
        self.TransformationUnit = TransformationUnit
        self.unit = unit if unit is not None else set()
        self.henshin_TransformationUnit51 = henshin_TransformationUnit51 if henshin_TransformationUnit51 is not None else set()
        self.henshin_TransformationUnit53 = henshin_TransformationUnit53
        self.henshin_TransformationUnit55 = henshin_TransformationUnit55
        self.henshin_TransformationUnit57 = henshin_TransformationUnit57
        self.henshin_TransformationUnit78 = henshin_TransformationUnit78
        self.henshin_TransformationUnit60 = henshin_TransformationUnit60
        self.henshin_TransformationUnit63 = henshin_TransformationUnit63
        self.henshin_TransformationUnit65 = henshin_TransformationUnit65
        
    @property
    def activated(self) -> bool:
        return self.__activated

    @activated.setter
    def activated(self, activated: bool):
        self.__activated = activated

    @property
    def henshin_TransformationUnit55(self):
        return self.__henshin_TransformationUnit55

    @henshin_TransformationUnit55.setter
    def henshin_TransformationUnit55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit55", None)
        self.__henshin_TransformationUnit55 = value
        
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
    def henshin_TransformationUnit51(self):
        return self.__henshin_TransformationUnit51

    @henshin_TransformationUnit51.setter
    def henshin_TransformationUnit51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit51", None)
        self.__henshin_TransformationUnit51 = value if value is not None else set()
        
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
    def henshin_TransformationUnit57(self):
        return self.__henshin_TransformationUnit57

    @henshin_TransformationUnit57.setter
    def henshin_TransformationUnit57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit57", None)
        self.__henshin_TransformationUnit57 = value
        
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
    def henshin_TransformationUnit63(self):
        return self.__henshin_TransformationUnit63

    @henshin_TransformationUnit63.setter
    def henshin_TransformationUnit63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit63", None)
        self.__henshin_TransformationUnit63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit62"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit62", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit62"):
                opp_val = getattr(value, "henshin_ConditionalUnit62", None)
                setattr(value, "henshin_ConditionalUnit62", self)

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
            if hasattr(old_value, "henshin_TransformationSystem5"):
                opp_val = getattr(old_value, "henshin_TransformationSystem5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_TransformationSystem5"):
                opp_val = getattr(value, "henshin_TransformationSystem5", None)
                if opp_val is None:
                    setattr(value, "henshin_TransformationSystem5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def henshin_TransformationUnit65(self):
        return self.__henshin_TransformationUnit65

    @henshin_TransformationUnit65.setter
    def henshin_TransformationUnit65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit65", None)
        self.__henshin_TransformationUnit65 = value
        
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
    def henshin_TransformationUnit60(self):
        return self.__henshin_TransformationUnit60

    @henshin_TransformationUnit60.setter
    def henshin_TransformationUnit60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit60", None)
        self.__henshin_TransformationUnit60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_ConditionalUnit59"):
                opp_val = getattr(old_value, "henshin_ConditionalUnit59", None)
                if opp_val == self:
                    setattr(old_value, "henshin_ConditionalUnit59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_ConditionalUnit59"):
                opp_val = getattr(value, "henshin_ConditionalUnit59", None)
                setattr(value, "henshin_ConditionalUnit59", self)

    @property
    def henshin_TransformationUnit53(self):
        return self.__henshin_TransformationUnit53

    @henshin_TransformationUnit53.setter
    def henshin_TransformationUnit53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit53", None)
        self.__henshin_TransformationUnit53 = value
        
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
    def henshin_TransformationUnit78(self):
        return self.__henshin_TransformationUnit78

    @henshin_TransformationUnit78.setter
    def henshin_TransformationUnit78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationUnit__henshin_TransformationUnit78", None)
        self.__henshin_TransformationUnit78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "henshin_CountedUnit"):
                opp_val = getattr(old_value, "henshin_CountedUnit", None)
                if opp_val == self:
                    setattr(old_value, "henshin_CountedUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "henshin_CountedUnit"):
                opp_val = getattr(value, "henshin_CountedUnit", None)
                setattr(value, "henshin_CountedUnit", self)

    def getSubUnits(self, deep: bool) -> TransformationUnit:
        # TODO: Implement getSubUnits method
        pass

    def getParameterByName(self, parametername: str) -> str:
        # TODO: Implement getParameterByName method
        pass

class henshin_AttributeCondition(NamedElement, DescribedElement):

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
            if hasattr(old_value, "Rule16"):
                opp_val = getattr(old_value, "Rule16", None)
                if opp_val == self:
                    setattr(old_value, "Rule16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rule16"):
                opp_val = getattr(value, "Rule16", None)
                setattr(value, "Rule16", self)

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

class henshin_TransformationSystem(NamedElement, DescribedElement):

    def __init__(self, henshin_TransformationSystem3: set["henshin_Graph"] = None, henshin_TransformationSystem5: set["henshin_TransformationUnit"] = None, TransformationSystem: "henshin_Rule" = None, transformationSystem: set["henshin_Rule"] = None, henshin_TransformationSystem: set["henshin_EPackage"] = None):
        self.henshin_TransformationSystem3 = henshin_TransformationSystem3 if henshin_TransformationSystem3 is not None else set()
        self.henshin_TransformationSystem5 = henshin_TransformationSystem5 if henshin_TransformationSystem5 is not None else set()
        self.TransformationSystem = TransformationSystem
        self.transformationSystem = transformationSystem if transformationSystem is not None else set()
        self.henshin_TransformationSystem = henshin_TransformationSystem if henshin_TransformationSystem is not None else set()
        
    @property
    def henshin_TransformationSystem3(self):
        return self.__henshin_TransformationSystem3

    @henshin_TransformationSystem3.setter
    def henshin_TransformationSystem3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__henshin_TransformationSystem3", None)
        self.__henshin_TransformationSystem3 = value if value is not None else set()
        
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
    def TransformationSystem(self):
        return self.__TransformationSystem

    @TransformationSystem.setter
    def TransformationSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__TransformationSystem", None)
        self.__TransformationSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules"):
                opp_val = getattr(old_value, "rules", None)
                if opp_val == self:
                    setattr(old_value, "rules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules"):
                opp_val = getattr(value, "rules", None)
                setattr(value, "rules", self)

    @property
    def transformationSystem(self):
        return self.__transformationSystem

    @transformationSystem.setter
    def transformationSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__transformationSystem", None)
        self.__transformationSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    setattr(item, "Rule", self)
                    

    @property
    def henshin_TransformationSystem5(self):
        return self.__henshin_TransformationSystem5

    @henshin_TransformationSystem5.setter
    def henshin_TransformationSystem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_henshin_TransformationSystem__henshin_TransformationSystem5", None)
        self.__henshin_TransformationSystem5 = value if value is not None else set()
        
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
                    

    def findRuleByName(self, ruleName: str) -> str:
        # TODO: Implement findRuleByName method
        pass

    def findUnitByName(self, unitName: str) -> str:
        # TODO: Implement findUnitByName method
        pass

class henshin_DescribedElement(ABC):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class henshin_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
