from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Calculation:

    pass
class trnetvisual_ExternalCalculationCall(Calculation):

    def __init__(self, id: str, qualifiedName: str, owner116: set["trnetvisual_ExternalCalculationCallParameter"] = None, ExternalCalculationCall: "trnetvisual_ExternalCalculationCallParameter" = None):
        self.id = id
        self.qualifiedName = qualifiedName
        self.owner116 = owner116 if owner116 is not None else set()
        self.ExternalCalculationCall = ExternalCalculationCall
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def ExternalCalculationCall(self):
        return self.__ExternalCalculationCall

    @ExternalCalculationCall.setter
    def ExternalCalculationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalCalculationCall__ExternalCalculationCall", None)
        self.__ExternalCalculationCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters119"):
                opp_val = getattr(old_value, "parameters119", None)
                if opp_val == self:
                    setattr(old_value, "parameters119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters119"):
                opp_val = getattr(value, "parameters119", None)
                setattr(value, "parameters119", self)

    @property
    def owner116(self):
        return self.__owner116

    @owner116.setter
    def owner116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalCalculationCall__owner116", None)
        self.__owner116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalCalculationCallParameter117"):
                    opp_val = getattr(item, "ExternalCalculationCallParameter117", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalCalculationCallParameter117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalCalculationCallParameter117"):
                    opp_val = getattr(item, "ExternalCalculationCallParameter117", None)
                    
                    setattr(item, "ExternalCalculationCallParameter117", self)
                    

class ParameterRef:

    pass
class Action:

    pass
class trnetvisual_ExternalActionCall(Action):

    def __init__(self, id: str, qualifiedName: str, ExternalActionCall: "trnetvisual_ExternalActionCallParameter" = None, owner102: set["trnetvisual_ExternalActionCallParameter"] = None):
        self.id = id
        self.qualifiedName = qualifiedName
        self.ExternalActionCall = ExternalActionCall
        self.owner102 = owner102 if owner102 is not None else set()
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ExternalActionCall(self):
        return self.__ExternalActionCall

    @ExternalActionCall.setter
    def ExternalActionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalActionCall__ExternalActionCall", None)
        self.__ExternalActionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters112"):
                opp_val = getattr(old_value, "parameters112", None)
                if opp_val == self:
                    setattr(old_value, "parameters112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters112"):
                opp_val = getattr(value, "parameters112", None)
                setattr(value, "parameters112", self)

    @property
    def owner102(self):
        return self.__owner102

    @owner102.setter
    def owner102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalActionCall__owner102", None)
        self.__owner102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalActionCallParameter103"):
                    opp_val = getattr(item, "ExternalActionCallParameter103", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalActionCallParameter103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalActionCallParameter103"):
                    opp_val = getattr(item, "ExternalActionCallParameter103", None)
                    
                    setattr(item, "ExternalActionCallParameter103", self)
                    

class trnetvisual_ParameterRef:

    def __init__(self, index: int):
        self.index = index
        
    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

class trnetvisual_ExternalConditionCallParameter(ParameterRef):

    pass
class trnetvisual_Parameter(ABC):

    pass
class trnetvisual_ExternalAttributeCalculationCallParameter(ParameterRef):

    pass
class AttributeCalculation:

    pass
class FlowRule:

    pass
class trnetvisual_Eventually(FlowRule):

    pass
class trnetvisual_NextDerived(FlowRule):

    pass
class trnetvisual_Next(FlowRule):

    pass
class ApplicationCondition:

    pass
class trnetvisual_ExternalConditionCall(ApplicationCondition):

    def __init__(self, id: str, qualifiedName: str, owner99: set["trnetvisual_ExternalConditionCallParameter"] = None, ExternalConditionCall: "trnetvisual_ExternalConditionCallParameter" = None):
        self.id = id
        self.qualifiedName = qualifiedName
        self.owner99 = owner99 if owner99 is not None else set()
        self.ExternalConditionCall = ExternalConditionCall
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def owner99(self):
        return self.__owner99

    @owner99.setter
    def owner99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalConditionCall__owner99", None)
        self.__owner99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalConditionCallParameter100"):
                    opp_val = getattr(item, "ExternalConditionCallParameter100", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalConditionCallParameter100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalConditionCallParameter100"):
                    opp_val = getattr(item, "ExternalConditionCallParameter100", None)
                    
                    setattr(item, "ExternalConditionCallParameter100", self)
                    

    @property
    def ExternalConditionCall(self):
        return self.__ExternalConditionCall

    @ExternalConditionCall.setter
    def ExternalConditionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalConditionCall__ExternalConditionCall", None)
        self.__ExternalConditionCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters108"):
                opp_val = getattr(old_value, "parameters108", None)
                if opp_val == self:
                    setattr(old_value, "parameters108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters108"):
                opp_val = getattr(value, "parameters108", None)
                setattr(value, "parameters108", self)

class trnetvisual_ExternalCalculationCallParameter(ParameterRef):

    pass
class trnetvisual_ExternalActionCallParameter(ParameterRef):

    pass
class Result:

    pass
class trnetvisual_SomeResult(Result):

    def __init__(self, count: int):
        self.count = count
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

class trnetvisual_AnyResult(Result):

    pass
class trnetvisual_Action(ABC):

    pass
class trnetvisual_ApplicationCondition(ABC):

    pass
class Operand:

    pass
class trnetvisual_AntiOperand(Operand):

    pass
class trnetvisual_SomeOperand(Operand):

    def __init__(self, count: int):
        self.count = count
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

class trnetvisual_OptionalOperand(Operand):

    pass
class trnetvisual_AnyOperand(Operand):

    pass
class Operator:

    pass
class trnetvisual_Combinator(Operator):

    pass
class NodePattern:

    pass
class trnetvisual_OptionalNode(NodePattern):

    pass
class trnetvisual_MandatoryNode(NodePattern):

    pass
class trnetvisual_ExternalAttributeCalculationCall(AttributeCalculation):

    def __init__(self, id: str, qualifiedName: str, ExternalAttributeCalculationCall: "trnetvisual_AttributePattern" = None, attributeExternalCalculationCall: "trnetvisual_AttributePattern" = None, owner: set["trnetvisual_ExternalAttributeCalculationCallParameter"] = None, ExternalAttributeCalculationCall105: "trnetvisual_ExternalAttributeCalculationCallParameter" = None):
        self.id = id
        self.qualifiedName = qualifiedName
        self.ExternalAttributeCalculationCall = ExternalAttributeCalculationCall
        self.attributeExternalCalculationCall = attributeExternalCalculationCall
        self.owner = owner if owner is not None else set()
        self.ExternalAttributeCalculationCall105 = ExternalAttributeCalculationCall105
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ExternalAttributeCalculationCall105(self):
        return self.__ExternalAttributeCalculationCall105

    @ExternalAttributeCalculationCall105.setter
    def ExternalAttributeCalculationCall105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalAttributeCalculationCall__ExternalAttributeCalculationCall105", None)
        self.__ExternalAttributeCalculationCall105 = value
        
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
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalAttributeCalculationCall__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalAttributeCalculationCallParameter"):
                    opp_val = getattr(item, "ExternalAttributeCalculationCallParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalAttributeCalculationCallParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalAttributeCalculationCallParameter"):
                    opp_val = getattr(item, "ExternalAttributeCalculationCallParameter", None)
                    
                    setattr(item, "ExternalAttributeCalculationCallParameter", self)
                    

    @property
    def attributeExternalCalculationCall(self):
        return self.__attributeExternalCalculationCall

    @attributeExternalCalculationCall.setter
    def attributeExternalCalculationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalAttributeCalculationCall__attributeExternalCalculationCall", None)
        self.__attributeExternalCalculationCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributePattern88"):
                opp_val = getattr(old_value, "AttributePattern88", None)
                if opp_val == self:
                    setattr(old_value, "AttributePattern88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributePattern88"):
                opp_val = getattr(value, "AttributePattern88", None)
                setattr(value, "AttributePattern88", self)

    @property
    def ExternalAttributeCalculationCall(self):
        return self.__ExternalAttributeCalculationCall

    @ExternalAttributeCalculationCall.setter
    def ExternalAttributeCalculationCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_ExternalAttributeCalculationCall__ExternalAttributeCalculationCall", None)
        self.__ExternalAttributeCalculationCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "result"):
                opp_val = getattr(old_value, "result", None)
                if opp_val == self:
                    setattr(old_value, "result", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "result"):
                opp_val = getattr(value, "result", None)
                setattr(value, "result", self)

class trnetvisual_External(Operator):

    pass
class Restriction:

    pass
class trnetvisual_AttributeCalculation(Restriction):

    pass
class trnetvisual_Same(Restriction):

    pass
class trnetvisual_EdgePattern:

    def __init__(self, name: str, EdgePattern: "trnetvisual_NodePattern" = None, EdgePattern15: "trnetvisual_NodePattern" = None, outgoing: "trnetvisual_NodePattern" = None, incoming: "trnetvisual_NodePattern" = None, edges: "trnetvisual_Pattern" = None, EdgePattern42: "trnetvisual_Pattern" = None):
        self.name = name
        self.EdgePattern = EdgePattern
        self.EdgePattern15 = EdgePattern15
        self.outgoing = outgoing
        self.incoming = incoming
        self.edges = edges
        self.EdgePattern42 = EdgePattern42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EdgePattern(self):
        return self.__EdgePattern

    @EdgePattern.setter
    def EdgePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_EdgePattern__EdgePattern", None)
        self.__EdgePattern = value
        
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
    def EdgePattern15(self):
        return self.__EdgePattern15

    @EdgePattern15.setter
    def EdgePattern15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_EdgePattern__EdgePattern15", None)
        self.__EdgePattern15 = value
        
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
        old_value = getattr(self, f"_trnetvisual_EdgePattern__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodePattern35"):
                opp_val = getattr(old_value, "NodePattern35", None)
                if opp_val == self:
                    setattr(old_value, "NodePattern35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodePattern35"):
                opp_val = getattr(value, "NodePattern35", None)
                setattr(value, "NodePattern35", self)

    @property
    def EdgePattern42(self):
        return self.__EdgePattern42

    @EdgePattern42.setter
    def EdgePattern42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_EdgePattern__EdgePattern42", None)
        self.__EdgePattern42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pattern41"):
                opp_val = getattr(old_value, "pattern41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pattern41"):
                opp_val = getattr(value, "pattern41", None)
                if opp_val is None:
                    setattr(value, "pattern41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_EdgePattern__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern37"):
                opp_val = getattr(old_value, "Pattern37", None)
                if opp_val == self:
                    setattr(old_value, "Pattern37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern37"):
                opp_val = getattr(value, "Pattern37", None)
                setattr(value, "Pattern37", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_EdgePattern__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodePattern"):
                opp_val = getattr(old_value, "NodePattern", None)
                if opp_val == self:
                    setattr(old_value, "NodePattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodePattern"):
                opp_val = getattr(value, "NodePattern", None)
                setattr(value, "NodePattern", self)

class Parameter:

    pass
class trnetvisual_AttributePattern(Parameter):

    def __init__(self, name: str, expectedNumberOfDistinctValues: float, AttributePattern: "trnetvisual_NodePattern" = None, result: "trnetvisual_ExternalAttributeCalculationCall" = None, attributes: "trnetvisual_NodePattern" = None, AttributePattern88: "trnetvisual_ExternalAttributeCalculationCall" = None):
        self.name = name
        self.expectedNumberOfDistinctValues = expectedNumberOfDistinctValues
        self.AttributePattern = AttributePattern
        self.result = result
        self.attributes = attributes
        self.AttributePattern88 = AttributePattern88
        
    @property
    def expectedNumberOfDistinctValues(self) -> float:
        return self.__expectedNumberOfDistinctValues

    @expectedNumberOfDistinctValues.setter
    def expectedNumberOfDistinctValues(self, expectedNumberOfDistinctValues: float):
        self.__expectedNumberOfDistinctValues = expectedNumberOfDistinctValues

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_AttributePattern__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodePattern57"):
                opp_val = getattr(old_value, "NodePattern57", None)
                if opp_val == self:
                    setattr(old_value, "NodePattern57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodePattern57"):
                opp_val = getattr(value, "NodePattern57", None)
                setattr(value, "NodePattern57", self)

    @property
    def AttributePattern(self):
        return self.__AttributePattern

    @AttributePattern.setter
    def AttributePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_AttributePattern__AttributePattern", None)
        self.__AttributePattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownerNode"):
                opp_val = getattr(old_value, "ownerNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownerNode"):
                opp_val = getattr(value, "ownerNode", None)
                if opp_val is None:
                    setattr(value, "ownerNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_AttributePattern__result", None)
        self.__result = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExternalAttributeCalculationCall"):
                opp_val = getattr(old_value, "ExternalAttributeCalculationCall", None)
                if opp_val == self:
                    setattr(old_value, "ExternalAttributeCalculationCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExternalAttributeCalculationCall"):
                opp_val = getattr(value, "ExternalAttributeCalculationCall", None)
                setattr(value, "ExternalAttributeCalculationCall", self)

    @property
    def AttributePattern88(self):
        return self.__AttributePattern88

    @AttributePattern88.setter
    def AttributePattern88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_AttributePattern__AttributePattern88", None)
        self.__AttributePattern88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributeExternalCalculationCall"):
                opp_val = getattr(old_value, "attributeExternalCalculationCall", None)
                if opp_val == self:
                    setattr(old_value, "attributeExternalCalculationCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributeExternalCalculationCall"):
                opp_val = getattr(value, "attributeExternalCalculationCall", None)
                setattr(value, "attributeExternalCalculationCall", self)

class trnetvisual_NodePattern(Parameter):

    def __init__(self, name: str, id: str, expectedNumberOfDistinctValues: float, target24: set["trnetvisual_Keep"] = None, source26: set["trnetvisual_Keep"] = None, target29: set["trnetvisual_Different"] = None, source31: set["trnetvisual_Different"] = None, target: set["trnetvisual_EdgePattern"] = None, source: set["trnetvisual_EdgePattern"] = None, source17: set["trnetvisual_Same"] = None, target19: set["trnetvisual_Same"] = None, nodes: "trnetvisual_Pattern" = None, ownerNode: set["trnetvisual_AttributePattern"] = None, NodePattern48: "trnetvisual_Same" = None, NodePattern50: "trnetvisual_Same" = None, NodePattern52: "trnetvisual_Different" = None, NodePattern: "trnetvisual_EdgePattern" = None, NodePattern35: "trnetvisual_EdgePattern" = None, NodePattern39: "trnetvisual_Pattern" = None, NodePattern54: "trnetvisual_Different" = None, NodePattern57: "trnetvisual_AttributePattern" = None, NodePattern59: "trnetvisual_Keep" = None, NodePattern61: "trnetvisual_Keep" = None):
        self.name = name
        self.id = id
        self.expectedNumberOfDistinctValues = expectedNumberOfDistinctValues
        self.target24 = target24 if target24 is not None else set()
        self.source26 = source26 if source26 is not None else set()
        self.target29 = target29 if target29 is not None else set()
        self.source31 = source31 if source31 is not None else set()
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.source17 = source17 if source17 is not None else set()
        self.target19 = target19 if target19 is not None else set()
        self.nodes = nodes
        self.ownerNode = ownerNode if ownerNode is not None else set()
        self.NodePattern48 = NodePattern48
        self.NodePattern50 = NodePattern50
        self.NodePattern52 = NodePattern52
        self.NodePattern = NodePattern
        self.NodePattern35 = NodePattern35
        self.NodePattern39 = NodePattern39
        self.NodePattern54 = NodePattern54
        self.NodePattern57 = NodePattern57
        self.NodePattern59 = NodePattern59
        self.NodePattern61 = NodePattern61
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def expectedNumberOfDistinctValues(self) -> float:
        return self.__expectedNumberOfDistinctValues

    @expectedNumberOfDistinctValues.setter
    def expectedNumberOfDistinctValues(self, expectedNumberOfDistinctValues: float):
        self.__expectedNumberOfDistinctValues = expectedNumberOfDistinctValues

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgePattern15"):
                    opp_val = getattr(item, "EdgePattern15", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgePattern15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgePattern15"):
                    opp_val = getattr(item, "EdgePattern15", None)
                    
                    setattr(item, "EdgePattern15", self)
                    

    @property
    def NodePattern59(self):
        return self.__NodePattern59

    @NodePattern59.setter
    def NodePattern59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern59", None)
        self.__NodePattern59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keepOut"):
                opp_val = getattr(old_value, "keepOut", None)
                if opp_val == self:
                    setattr(old_value, "keepOut", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keepOut"):
                opp_val = getattr(value, "keepOut", None)
                setattr(value, "keepOut", self)

    @property
    def NodePattern(self):
        return self.__NodePattern

    @NodePattern.setter
    def NodePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern", None)
        self.__NodePattern = value
        
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
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern"):
                opp_val = getattr(old_value, "Pattern", None)
                if opp_val == self:
                    setattr(old_value, "Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern"):
                opp_val = getattr(value, "Pattern", None)
                setattr(value, "Pattern", self)

    @property
    def NodePattern39(self):
        return self.__NodePattern39

    @NodePattern39.setter
    def NodePattern39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern39", None)
        self.__NodePattern39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pattern"):
                opp_val = getattr(old_value, "pattern", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pattern"):
                opp_val = getattr(value, "pattern", None)
                if opp_val is None:
                    setattr(value, "pattern", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def NodePattern54(self):
        return self.__NodePattern54

    @NodePattern54.setter
    def NodePattern54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern54", None)
        self.__NodePattern54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "differentIn"):
                opp_val = getattr(old_value, "differentIn", None)
                if opp_val == self:
                    setattr(old_value, "differentIn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "differentIn"):
                opp_val = getattr(value, "differentIn", None)
                setattr(value, "differentIn", self)

    @property
    def NodePattern50(self):
        return self.__NodePattern50

    @NodePattern50.setter
    def NodePattern50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern50", None)
        self.__NodePattern50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sameIn"):
                opp_val = getattr(old_value, "sameIn", None)
                if opp_val == self:
                    setattr(old_value, "sameIn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sameIn"):
                opp_val = getattr(value, "sameIn", None)
                setattr(value, "sameIn", self)

    @property
    def NodePattern61(self):
        return self.__NodePattern61

    @NodePattern61.setter
    def NodePattern61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern61", None)
        self.__NodePattern61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keepIn"):
                opp_val = getattr(old_value, "keepIn", None)
                if opp_val == self:
                    setattr(old_value, "keepIn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keepIn"):
                opp_val = getattr(value, "keepIn", None)
                setattr(value, "keepIn", self)

    @property
    def ownerNode(self):
        return self.__ownerNode

    @ownerNode.setter
    def ownerNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__ownerNode", None)
        self.__ownerNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributePattern"):
                    opp_val = getattr(item, "AttributePattern", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributePattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributePattern"):
                    opp_val = getattr(item, "AttributePattern", None)
                    
                    setattr(item, "AttributePattern", self)
                    

    @property
    def target24(self):
        return self.__target24

    @target24.setter
    def target24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__target24", None)
        self.__target24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Keep"):
                    opp_val = getattr(item, "Keep", None)
                    
                    if opp_val == self:
                        setattr(item, "Keep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Keep"):
                    opp_val = getattr(item, "Keep", None)
                    
                    setattr(item, "Keep", self)
                    

    @property
    def target29(self):
        return self.__target29

    @target29.setter
    def target29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__target29", None)
        self.__target29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Different"):
                    opp_val = getattr(item, "Different", None)
                    
                    if opp_val == self:
                        setattr(item, "Different", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Different"):
                    opp_val = getattr(item, "Different", None)
                    
                    setattr(item, "Different", self)
                    

    @property
    def source17(self):
        return self.__source17

    @source17.setter
    def source17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__source17", None)
        self.__source17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Same"):
                    opp_val = getattr(item, "Same", None)
                    
                    if opp_val == self:
                        setattr(item, "Same", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Same"):
                    opp_val = getattr(item, "Same", None)
                    
                    setattr(item, "Same", self)
                    

    @property
    def NodePattern48(self):
        return self.__NodePattern48

    @NodePattern48.setter
    def NodePattern48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern48", None)
        self.__NodePattern48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sameOut"):
                opp_val = getattr(old_value, "sameOut", None)
                if opp_val == self:
                    setattr(old_value, "sameOut", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sameOut"):
                opp_val = getattr(value, "sameOut", None)
                setattr(value, "sameOut", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgePattern"):
                    opp_val = getattr(item, "EdgePattern", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgePattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgePattern"):
                    opp_val = getattr(item, "EdgePattern", None)
                    
                    setattr(item, "EdgePattern", self)
                    

    @property
    def NodePattern57(self):
        return self.__NodePattern57

    @NodePattern57.setter
    def NodePattern57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern57", None)
        self.__NodePattern57 = value
        
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
    def NodePattern35(self):
        return self.__NodePattern35

    @NodePattern35.setter
    def NodePattern35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern35", None)
        self.__NodePattern35 = value
        
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
    def source31(self):
        return self.__source31

    @source31.setter
    def source31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__source31", None)
        self.__source31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Different32"):
                    opp_val = getattr(item, "Different32", None)
                    
                    if opp_val == self:
                        setattr(item, "Different32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Different32"):
                    opp_val = getattr(item, "Different32", None)
                    
                    setattr(item, "Different32", self)
                    

    @property
    def NodePattern52(self):
        return self.__NodePattern52

    @NodePattern52.setter
    def NodePattern52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__NodePattern52", None)
        self.__NodePattern52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "differentOut"):
                opp_val = getattr(old_value, "differentOut", None)
                if opp_val == self:
                    setattr(old_value, "differentOut", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "differentOut"):
                opp_val = getattr(value, "differentOut", None)
                setattr(value, "differentOut", self)

    @property
    def source26(self):
        return self.__source26

    @source26.setter
    def source26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__source26", None)
        self.__source26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Keep27"):
                    opp_val = getattr(item, "Keep27", None)
                    
                    if opp_val == self:
                        setattr(item, "Keep27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Keep27"):
                    opp_val = getattr(item, "Keep27", None)
                    
                    setattr(item, "Keep27", self)
                    

    @property
    def target19(self):
        return self.__target19

    @target19.setter
    def target19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_NodePattern__target19", None)
        self.__target19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Same20"):
                    opp_val = getattr(item, "Same20", None)
                    
                    if opp_val == self:
                        setattr(item, "Same20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Same20"):
                    opp_val = getattr(item, "Same20", None)
                    
                    setattr(item, "Same20", self)
                    

class trnetvisual_Calculation(Parameter):

    pass
class trnetvisual_FlowRule(ABC):

    pass
class trnetvisual_Result(ABC):

    pass
class trnetvisual_Operand(ABC):

    def __init__(self, index: int, trnetvisual_Operand: "trnetvisual_TrNetModel" = None, Operand: "trnetvisual_Pattern" = None, Operand63: "trnetvisual_Operator" = None, operands: "trnetvisual_Operator" = None, outgoingOperands: "trnetvisual_Pattern" = None):
        self.index = index
        self.trnetvisual_Operand = trnetvisual_Operand
        self.Operand = Operand
        self.Operand63 = Operand63
        self.operands = operands
        self.outgoingOperands = outgoingOperands
        
    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def outgoingOperands(self):
        return self.__outgoingOperands

    @outgoingOperands.setter
    def outgoingOperands(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operand__outgoingOperands", None)
        self.__outgoingOperands = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern82"):
                opp_val = getattr(old_value, "Pattern82", None)
                if opp_val == self:
                    setattr(old_value, "Pattern82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern82"):
                opp_val = getattr(value, "Pattern82", None)
                setattr(value, "Pattern82", self)

    @property
    def operands(self):
        return self.__operands

    @operands.setter
    def operands(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operand__operands", None)
        self.__operands = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operator80"):
                opp_val = getattr(old_value, "Operator80", None)
                if opp_val == self:
                    setattr(old_value, "Operator80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operator80"):
                opp_val = getattr(value, "Operator80", None)
                setattr(value, "Operator80", self)

    @property
    def Operand63(self):
        return self.__Operand63

    @Operand63.setter
    def Operand63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operand__Operand63", None)
        self.__Operand63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operator"):
                opp_val = getattr(old_value, "operator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operator"):
                opp_val = getattr(value, "operator", None)
                if opp_val is None:
                    setattr(value, "operator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trnetvisual_Operand(self):
        return self.__trnetvisual_Operand

    @trnetvisual_Operand.setter
    def trnetvisual_Operand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operand__trnetvisual_Operand", None)
        self.__trnetvisual_Operand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnetvisual_TrNetModel6"):
                opp_val = getattr(old_value, "trnetvisual_TrNetModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnetvisual_TrNetModel6"):
                opp_val = getattr(value, "trnetvisual_TrNetModel6", None)
                if opp_val is None:
                    setattr(value, "trnetvisual_TrNetModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operand(self):
        return self.__Operand

    @Operand.setter
    def Operand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operand__Operand", None)
        self.__Operand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pattern46"):
                opp_val = getattr(old_value, "pattern46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pattern46"):
                opp_val = getattr(value, "pattern46", None)
                if opp_val is None:
                    setattr(value, "pattern46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trnetvisual_Different(Restriction):

    pass
class trnetvisual_Keep(Restriction):

    pass
class trnetvisual_Restriction(ABC):

    pass
class trnetvisual_Operator(ABC):

    def __init__(self, id: str, trnetvisual_Operator: "trnetvisual_TrNetModel" = None, operator: set["trnetvisual_Operand"] = None, operator65: set["trnetvisual_Result"] = None, source68: set["trnetvisual_FlowRule"] = None, target70: set["trnetvisual_FlowRule"] = None, trnetvisual_Operator73: set["trnetvisual_ApplicationCondition"] = None, trnetvisual_Operator75: set["trnetvisual_Action"] = None, Operator: "trnetvisual_Result" = None, Operator80: "trnetvisual_Operand" = None, Operator84: "trnetvisual_FlowRule" = None, Operator86: "trnetvisual_FlowRule" = None):
        self.id = id
        self.trnetvisual_Operator = trnetvisual_Operator
        self.operator = operator if operator is not None else set()
        self.operator65 = operator65 if operator65 is not None else set()
        self.source68 = source68 if source68 is not None else set()
        self.target70 = target70 if target70 is not None else set()
        self.trnetvisual_Operator73 = trnetvisual_Operator73 if trnetvisual_Operator73 is not None else set()
        self.trnetvisual_Operator75 = trnetvisual_Operator75 if trnetvisual_Operator75 is not None else set()
        self.Operator = Operator
        self.Operator80 = Operator80
        self.Operator84 = Operator84
        self.Operator86 = Operator86
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__operator", None)
        self.__operator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operand63"):
                    opp_val = getattr(item, "Operand63", None)
                    
                    if opp_val == self:
                        setattr(item, "Operand63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operand63"):
                    opp_val = getattr(item, "Operand63", None)
                    
                    setattr(item, "Operand63", self)
                    

    @property
    def target70(self):
        return self.__target70

    @target70.setter
    def target70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__target70", None)
        self.__target70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowRule71"):
                    opp_val = getattr(item, "FlowRule71", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowRule71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowRule71"):
                    opp_val = getattr(item, "FlowRule71", None)
                    
                    setattr(item, "FlowRule71", self)
                    

    @property
    def trnetvisual_Operator73(self):
        return self.__trnetvisual_Operator73

    @trnetvisual_Operator73.setter
    def trnetvisual_Operator73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__trnetvisual_Operator73", None)
        self.__trnetvisual_Operator73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_ApplicationCondition"):
                    opp_val = getattr(item, "trnetvisual_ApplicationCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_ApplicationCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_ApplicationCondition"):
                    opp_val = getattr(item, "trnetvisual_ApplicationCondition", None)
                    
                    setattr(item, "trnetvisual_ApplicationCondition", self)
                    

    @property
    def Operator(self):
        return self.__Operator

    @Operator.setter
    def Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__Operator", None)
        self.__Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "results"):
                opp_val = getattr(old_value, "results", None)
                if opp_val == self:
                    setattr(old_value, "results", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "results"):
                opp_val = getattr(value, "results", None)
                setattr(value, "results", self)

    @property
    def source68(self):
        return self.__source68

    @source68.setter
    def source68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__source68", None)
        self.__source68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FlowRule"):
                    opp_val = getattr(item, "FlowRule", None)
                    
                    if opp_val == self:
                        setattr(item, "FlowRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FlowRule"):
                    opp_val = getattr(item, "FlowRule", None)
                    
                    setattr(item, "FlowRule", self)
                    

    @property
    def trnetvisual_Operator(self):
        return self.__trnetvisual_Operator

    @trnetvisual_Operator.setter
    def trnetvisual_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__trnetvisual_Operator", None)
        self.__trnetvisual_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnetvisual_TrNetModel2"):
                opp_val = getattr(old_value, "trnetvisual_TrNetModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnetvisual_TrNetModel2"):
                opp_val = getattr(value, "trnetvisual_TrNetModel2", None)
                if opp_val is None:
                    setattr(value, "trnetvisual_TrNetModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Operator84(self):
        return self.__Operator84

    @Operator84.setter
    def Operator84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__Operator84", None)
        self.__Operator84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowOut"):
                opp_val = getattr(old_value, "flowOut", None)
                if opp_val == self:
                    setattr(old_value, "flowOut", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowOut"):
                opp_val = getattr(value, "flowOut", None)
                setattr(value, "flowOut", self)

    @property
    def trnetvisual_Operator75(self):
        return self.__trnetvisual_Operator75

    @trnetvisual_Operator75.setter
    def trnetvisual_Operator75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__trnetvisual_Operator75", None)
        self.__trnetvisual_Operator75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_Action"):
                    opp_val = getattr(item, "trnetvisual_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_Action"):
                    opp_val = getattr(item, "trnetvisual_Action", None)
                    
                    setattr(item, "trnetvisual_Action", self)
                    

    @property
    def Operator80(self):
        return self.__Operator80

    @Operator80.setter
    def Operator80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__Operator80", None)
        self.__Operator80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operands"):
                opp_val = getattr(old_value, "operands", None)
                if opp_val == self:
                    setattr(old_value, "operands", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operands"):
                opp_val = getattr(value, "operands", None)
                setattr(value, "operands", self)

    @property
    def operator65(self):
        return self.__operator65

    @operator65.setter
    def operator65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__operator65", None)
        self.__operator65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Result66"):
                    opp_val = getattr(item, "Result66", None)
                    
                    if opp_val == self:
                        setattr(item, "Result66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Result66"):
                    opp_val = getattr(item, "Result66", None)
                    
                    setattr(item, "Result66", self)
                    

    @property
    def Operator86(self):
        return self.__Operator86

    @Operator86.setter
    def Operator86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Operator__Operator86", None)
        self.__Operator86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowIn"):
                opp_val = getattr(old_value, "flowIn", None)
                if opp_val == self:
                    setattr(old_value, "flowIn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowIn"):
                opp_val = getattr(value, "flowIn", None)
                setattr(value, "flowIn", self)

class trnetvisual_Pattern:

    def __init__(self, id: str, expected_size: float, trnetvisual_Pattern: "trnetvisual_TrNetModel" = None, Pattern: "trnetvisual_NodePattern" = None, Pattern37: "trnetvisual_EdgePattern" = None, pattern: set["trnetvisual_NodePattern"] = None, pattern41: set["trnetvisual_EdgePattern"] = None, pattern44: set["trnetvisual_Result"] = None, pattern46: set["trnetvisual_Operand"] = None, Pattern82: "trnetvisual_Operand" = None, Pattern77: "trnetvisual_Result" = None):
        self.id = id
        self.expected_size = expected_size
        self.trnetvisual_Pattern = trnetvisual_Pattern
        self.Pattern = Pattern
        self.Pattern37 = Pattern37
        self.pattern = pattern if pattern is not None else set()
        self.pattern41 = pattern41 if pattern41 is not None else set()
        self.pattern44 = pattern44 if pattern44 is not None else set()
        self.pattern46 = pattern46 if pattern46 is not None else set()
        self.Pattern82 = Pattern82
        self.Pattern77 = Pattern77
        
    @property
    def expected_size(self) -> float:
        return self.__expected_size

    @expected_size.setter
    def expected_size(self, expected_size: float):
        self.__expected_size = expected_size

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def trnetvisual_Pattern(self):
        return self.__trnetvisual_Pattern

    @trnetvisual_Pattern.setter
    def trnetvisual_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__trnetvisual_Pattern", None)
        self.__trnetvisual_Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnetvisual_TrNetModel"):
                opp_val = getattr(old_value, "trnetvisual_TrNetModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnetvisual_TrNetModel"):
                opp_val = getattr(value, "trnetvisual_TrNetModel", None)
                if opp_val is None:
                    setattr(value, "trnetvisual_TrNetModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pattern46(self):
        return self.__pattern46

    @pattern46.setter
    def pattern46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__pattern46", None)
        self.__pattern46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operand"):
                    opp_val = getattr(item, "Operand", None)
                    
                    if opp_val == self:
                        setattr(item, "Operand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operand"):
                    opp_val = getattr(item, "Operand", None)
                    
                    setattr(item, "Operand", self)
                    

    @property
    def Pattern37(self):
        return self.__Pattern37

    @Pattern37.setter
    def Pattern37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__Pattern37", None)
        self.__Pattern37 = value
        
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
    def Pattern82(self):
        return self.__Pattern82

    @Pattern82.setter
    def Pattern82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__Pattern82", None)
        self.__Pattern82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingOperands"):
                opp_val = getattr(old_value, "outgoingOperands", None)
                if opp_val == self:
                    setattr(old_value, "outgoingOperands", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingOperands"):
                opp_val = getattr(value, "outgoingOperands", None)
                setattr(value, "outgoingOperands", self)

    @property
    def pattern41(self):
        return self.__pattern41

    @pattern41.setter
    def pattern41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__pattern41", None)
        self.__pattern41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgePattern42"):
                    opp_val = getattr(item, "EdgePattern42", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgePattern42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgePattern42"):
                    opp_val = getattr(item, "EdgePattern42", None)
                    
                    setattr(item, "EdgePattern42", self)
                    

    @property
    def pattern44(self):
        return self.__pattern44

    @pattern44.setter
    def pattern44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__pattern44", None)
        self.__pattern44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Result"):
                    opp_val = getattr(item, "Result", None)
                    
                    if opp_val == self:
                        setattr(item, "Result", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Result"):
                    opp_val = getattr(item, "Result", None)
                    
                    setattr(item, "Result", self)
                    

    @property
    def Pattern(self):
        return self.__Pattern

    @Pattern.setter
    def Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__Pattern", None)
        self.__Pattern = value
        
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
    def Pattern77(self):
        return self.__Pattern77

    @Pattern77.setter
    def Pattern77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__Pattern77", None)
        self.__Pattern77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingResults"):
                opp_val = getattr(old_value, "incomingResults", None)
                if opp_val == self:
                    setattr(old_value, "incomingResults", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingResults"):
                opp_val = getattr(value, "incomingResults", None)
                setattr(value, "incomingResults", self)

    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_Pattern__pattern", None)
        self.__pattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodePattern39"):
                    opp_val = getattr(item, "NodePattern39", None)
                    
                    if opp_val == self:
                        setattr(item, "NodePattern39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodePattern39"):
                    opp_val = getattr(item, "NodePattern39", None)
                    
                    setattr(item, "NodePattern39", self)
                    

class trnetvisual_TrNetModel:

    def __init__(self, id: str, trnetvisual_TrNetModel: set["trnetvisual_Pattern"] = None, trnetvisual_TrNetModel2: set["trnetvisual_Operator"] = None, trnetvisual_TrNetModel4: set["trnetvisual_Restriction"] = None, trnetvisual_TrNetModel6: set["trnetvisual_Operand"] = None, trnetvisual_TrNetModel8: set["trnetvisual_Result"] = None, trnetvisual_TrNetModel10: set["trnetvisual_FlowRule"] = None, trnetvisual_TrNetModel12: set["trnetvisual_Calculation"] = None):
        self.id = id
        self.trnetvisual_TrNetModel = trnetvisual_TrNetModel if trnetvisual_TrNetModel is not None else set()
        self.trnetvisual_TrNetModel2 = trnetvisual_TrNetModel2 if trnetvisual_TrNetModel2 is not None else set()
        self.trnetvisual_TrNetModel4 = trnetvisual_TrNetModel4 if trnetvisual_TrNetModel4 is not None else set()
        self.trnetvisual_TrNetModel6 = trnetvisual_TrNetModel6 if trnetvisual_TrNetModel6 is not None else set()
        self.trnetvisual_TrNetModel8 = trnetvisual_TrNetModel8 if trnetvisual_TrNetModel8 is not None else set()
        self.trnetvisual_TrNetModel10 = trnetvisual_TrNetModel10 if trnetvisual_TrNetModel10 is not None else set()
        self.trnetvisual_TrNetModel12 = trnetvisual_TrNetModel12 if trnetvisual_TrNetModel12 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def trnetvisual_TrNetModel2(self):
        return self.__trnetvisual_TrNetModel2

    @trnetvisual_TrNetModel2.setter
    def trnetvisual_TrNetModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_TrNetModel__trnetvisual_TrNetModel2", None)
        self.__trnetvisual_TrNetModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_Operator"):
                    opp_val = getattr(item, "trnetvisual_Operator", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_Operator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_Operator"):
                    opp_val = getattr(item, "trnetvisual_Operator", None)
                    
                    setattr(item, "trnetvisual_Operator", self)
                    

    @property
    def trnetvisual_TrNetModel8(self):
        return self.__trnetvisual_TrNetModel8

    @trnetvisual_TrNetModel8.setter
    def trnetvisual_TrNetModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_TrNetModel__trnetvisual_TrNetModel8", None)
        self.__trnetvisual_TrNetModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_Result"):
                    opp_val = getattr(item, "trnetvisual_Result", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_Result", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_Result"):
                    opp_val = getattr(item, "trnetvisual_Result", None)
                    
                    setattr(item, "trnetvisual_Result", self)
                    

    @property
    def trnetvisual_TrNetModel6(self):
        return self.__trnetvisual_TrNetModel6

    @trnetvisual_TrNetModel6.setter
    def trnetvisual_TrNetModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_TrNetModel__trnetvisual_TrNetModel6", None)
        self.__trnetvisual_TrNetModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_Operand"):
                    opp_val = getattr(item, "trnetvisual_Operand", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_Operand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_Operand"):
                    opp_val = getattr(item, "trnetvisual_Operand", None)
                    
                    setattr(item, "trnetvisual_Operand", self)
                    

    @property
    def trnetvisual_TrNetModel(self):
        return self.__trnetvisual_TrNetModel

    @trnetvisual_TrNetModel.setter
    def trnetvisual_TrNetModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_TrNetModel__trnetvisual_TrNetModel", None)
        self.__trnetvisual_TrNetModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_Pattern"):
                    opp_val = getattr(item, "trnetvisual_Pattern", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_Pattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_Pattern"):
                    opp_val = getattr(item, "trnetvisual_Pattern", None)
                    
                    setattr(item, "trnetvisual_Pattern", self)
                    

    @property
    def trnetvisual_TrNetModel10(self):
        return self.__trnetvisual_TrNetModel10

    @trnetvisual_TrNetModel10.setter
    def trnetvisual_TrNetModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_TrNetModel__trnetvisual_TrNetModel10", None)
        self.__trnetvisual_TrNetModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_FlowRule"):
                    opp_val = getattr(item, "trnetvisual_FlowRule", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_FlowRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_FlowRule"):
                    opp_val = getattr(item, "trnetvisual_FlowRule", None)
                    
                    setattr(item, "trnetvisual_FlowRule", self)
                    

    @property
    def trnetvisual_TrNetModel12(self):
        return self.__trnetvisual_TrNetModel12

    @trnetvisual_TrNetModel12.setter
    def trnetvisual_TrNetModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_TrNetModel__trnetvisual_TrNetModel12", None)
        self.__trnetvisual_TrNetModel12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_Calculation"):
                    opp_val = getattr(item, "trnetvisual_Calculation", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_Calculation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_Calculation"):
                    opp_val = getattr(item, "trnetvisual_Calculation", None)
                    
                    setattr(item, "trnetvisual_Calculation", self)
                    

    @property
    def trnetvisual_TrNetModel4(self):
        return self.__trnetvisual_TrNetModel4

    @trnetvisual_TrNetModel4.setter
    def trnetvisual_TrNetModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnetvisual_TrNetModel__trnetvisual_TrNetModel4", None)
        self.__trnetvisual_TrNetModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnetvisual_Restriction"):
                    opp_val = getattr(item, "trnetvisual_Restriction", None)
                    
                    if opp_val == self:
                        setattr(item, "trnetvisual_Restriction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnetvisual_Restriction"):
                    opp_val = getattr(item, "trnetvisual_Restriction", None)
                    
                    setattr(item, "trnetvisual_Restriction", self)
                    
