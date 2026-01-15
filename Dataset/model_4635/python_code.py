from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FlowRule:

    pass
class trnet_Eventually(FlowRule):

    pass
class trnet_NextDerived(FlowRule):

    pass
class trnet_Next(FlowRule):

    pass
class ExpressionOperator:

    pass
class trnet_Equality(ExpressionOperator):

    pass
class NodePattern:

    pass
class trnet_OptionalNode(NodePattern):

    pass
class trnet_MandatoryNode(NodePattern):

    pass
class Result:

    pass
class trnet_AnyResult(Result):

    pass
class trnet_SomeResult(Result):

    def __init__(self, count: int):
        self.count = count
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

class Operand:

    pass
class trnet_OptionalOperand(Operand):

    pass
class trnet_AnyOperand(Operand):

    pass
class trnet_AntiOperand(Operand):

    pass
class trnet_SomeOperand(Operand):

    def __init__(self, count: int):
        self.count = count
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

class Expression:

    pass
class trnet_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class trnet_ExpressionOperator(ABC):

    pass
class trnet_Expression(ABC):

    pass
class Restriction:

    pass
class trnet_Restriction(ABC):

    pass
class Operator:

    pass
class trnet_Union(Operator):

    pass
class trnet_External(Operator):

    pass
class trnet_Combinator(Operator):

    pass
class trnet_Same(Restriction):

    pass
class trnet_Result(ABC):

    pass
class trnet_Operand(ABC):

    def __init__(self, index: int, Operand: "trnet_Pattern" = None, outgoingOperands: "trnet_Pattern" = None, operands: "trnet_Operator" = None, Operand40: "trnet_Operator" = None):
        self.index = index
        self.Operand = Operand
        self.outgoingOperands = outgoingOperands
        self.operands = operands
        self.Operand40 = Operand40
        
    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def Operand40(self):
        return self.__Operand40

    @Operand40.setter
    def Operand40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operand__Operand40", None)
        self.__Operand40 = value
        
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
    def operands(self):
        return self.__operands

    @operands.setter
    def operands(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operand__operands", None)
        self.__operands = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operator"):
                opp_val = getattr(old_value, "Operator", None)
                if opp_val == self:
                    setattr(old_value, "Operator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operator"):
                opp_val = getattr(value, "Operator", None)
                setattr(value, "Operator", self)

    @property
    def outgoingOperands(self):
        return self.__outgoingOperands

    @outgoingOperands.setter
    def outgoingOperands(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operand__outgoingOperands", None)
        self.__outgoingOperands = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern58"):
                opp_val = getattr(old_value, "Pattern58", None)
                if opp_val == self:
                    setattr(old_value, "Pattern58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern58"):
                opp_val = getattr(value, "Pattern58", None)
                setattr(value, "Pattern58", self)

    @property
    def Operand(self):
        return self.__Operand

    @Operand.setter
    def Operand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operand__Operand", None)
        self.__Operand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pattern36"):
                opp_val = getattr(old_value, "pattern36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pattern36"):
                opp_val = getattr(value, "pattern36", None)
                if opp_val is None:
                    setattr(value, "pattern36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trnet_Keep(Restriction):

    pass
class trnet_Different(Restriction):

    pass
class trnet_AttributePattern:

    def __init__(self, name: str, trnet_AttributePattern: "trnet_NodePattern" = None, trnet_AttributePattern50: "trnet_Expression" = None, trnet_AttributePattern52: "trnet_ExpressionOperator" = None):
        self.name = name
        self.trnet_AttributePattern = trnet_AttributePattern
        self.trnet_AttributePattern50 = trnet_AttributePattern50
        self.trnet_AttributePattern52 = trnet_AttributePattern52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trnet_AttributePattern(self):
        return self.__trnet_AttributePattern

    @trnet_AttributePattern.setter
    def trnet_AttributePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_AttributePattern__trnet_AttributePattern", None)
        self.__trnet_AttributePattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnet_NodePattern"):
                opp_val = getattr(old_value, "trnet_NodePattern", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnet_NodePattern"):
                opp_val = getattr(value, "trnet_NodePattern", None)
                if opp_val is None:
                    setattr(value, "trnet_NodePattern", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trnet_AttributePattern50(self):
        return self.__trnet_AttributePattern50

    @trnet_AttributePattern50.setter
    def trnet_AttributePattern50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_AttributePattern__trnet_AttributePattern50", None)
        self.__trnet_AttributePattern50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnet_Expression"):
                opp_val = getattr(old_value, "trnet_Expression", None)
                if opp_val == self:
                    setattr(old_value, "trnet_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnet_Expression"):
                opp_val = getattr(value, "trnet_Expression", None)
                setattr(value, "trnet_Expression", self)

    @property
    def trnet_AttributePattern52(self):
        return self.__trnet_AttributePattern52

    @trnet_AttributePattern52.setter
    def trnet_AttributePattern52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_AttributePattern__trnet_AttributePattern52", None)
        self.__trnet_AttributePattern52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnet_ExpressionOperator"):
                opp_val = getattr(old_value, "trnet_ExpressionOperator", None)
                if opp_val == self:
                    setattr(old_value, "trnet_ExpressionOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnet_ExpressionOperator"):
                opp_val = getattr(value, "trnet_ExpressionOperator", None)
                setattr(value, "trnet_ExpressionOperator", self)

class trnet_EdgePattern:

    def __init__(self, name: str, EdgePattern: "trnet_NodePattern" = None, EdgePattern7: "trnet_NodePattern" = None, outgoing: "trnet_NodePattern" = None, incoming: "trnet_NodePattern" = None, edges: "trnet_Pattern" = None, EdgePattern34: "trnet_Pattern" = None):
        self.name = name
        self.EdgePattern = EdgePattern
        self.EdgePattern7 = EdgePattern7
        self.outgoing = outgoing
        self.incoming = incoming
        self.edges = edges
        self.EdgePattern34 = EdgePattern34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_EdgePattern__outgoing", None)
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

    @property
    def EdgePattern34(self):
        return self.__EdgePattern34

    @EdgePattern34.setter
    def EdgePattern34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_EdgePattern__EdgePattern34", None)
        self.__EdgePattern34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pattern33"):
                opp_val = getattr(old_value, "pattern33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pattern33"):
                opp_val = getattr(value, "pattern33", None)
                if opp_val is None:
                    setattr(value, "pattern33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_EdgePattern__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern29"):
                opp_val = getattr(old_value, "Pattern29", None)
                if opp_val == self:
                    setattr(old_value, "Pattern29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern29"):
                opp_val = getattr(value, "Pattern29", None)
                setattr(value, "Pattern29", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_EdgePattern__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodePattern27"):
                opp_val = getattr(old_value, "NodePattern27", None)
                if opp_val == self:
                    setattr(old_value, "NodePattern27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodePattern27"):
                opp_val = getattr(value, "NodePattern27", None)
                setattr(value, "NodePattern27", self)

    @property
    def EdgePattern7(self):
        return self.__EdgePattern7

    @EdgePattern7.setter
    def EdgePattern7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_EdgePattern__EdgePattern7", None)
        self.__EdgePattern7 = value
        
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
    def EdgePattern(self):
        return self.__EdgePattern

    @EdgePattern.setter
    def EdgePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_EdgePattern__EdgePattern", None)
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

class trnet_NodePattern(ABC):

    def __init__(self, name: str, id: str, target: set["trnet_EdgePattern"] = None, source: set["trnet_EdgePattern"] = None, nodes: "trnet_Pattern" = None, trnet_NodePattern: set["trnet_AttributePattern"] = None, target16: set["trnet_Different"] = None, source18: set["trnet_Different"] = None, target21: set["trnet_Keep"] = None, source23: set["trnet_Keep"] = None, NodePattern: "trnet_EdgePattern" = None, NodePattern27: "trnet_EdgePattern" = None, NodePattern31: "trnet_Pattern" = None, source9: set["trnet_Same"] = None, target11: set["trnet_Same"] = None, NodePattern46: "trnet_Same" = None, NodePattern48: "trnet_Same" = None, NodePattern54: "trnet_Keep" = None, NodePattern56: "trnet_Keep" = None, NodePattern65: "trnet_Different" = None, NodePattern67: "trnet_Different" = None):
        self.name = name
        self.id = id
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.nodes = nodes
        self.trnet_NodePattern = trnet_NodePattern if trnet_NodePattern is not None else set()
        self.target16 = target16 if target16 is not None else set()
        self.source18 = source18 if source18 is not None else set()
        self.target21 = target21 if target21 is not None else set()
        self.source23 = source23 if source23 is not None else set()
        self.NodePattern = NodePattern
        self.NodePattern27 = NodePattern27
        self.NodePattern31 = NodePattern31
        self.source9 = source9 if source9 is not None else set()
        self.target11 = target11 if target11 is not None else set()
        self.NodePattern46 = NodePattern46
        self.NodePattern48 = NodePattern48
        self.NodePattern54 = NodePattern54
        self.NodePattern56 = NodePattern56
        self.NodePattern65 = NodePattern65
        self.NodePattern67 = NodePattern67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def NodePattern(self):
        return self.__NodePattern

    @NodePattern.setter
    def NodePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern", None)
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
    def source9(self):
        return self.__source9

    @source9.setter
    def source9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__source9", None)
        self.__source9 = value if value is not None else set()
        
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
    def target11(self):
        return self.__target11

    @target11.setter
    def target11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__target11", None)
        self.__target11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Same12"):
                    opp_val = getattr(item, "Same12", None)
                    
                    if opp_val == self:
                        setattr(item, "Same12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Same12"):
                    opp_val = getattr(item, "Same12", None)
                    
                    setattr(item, "Same12", self)
                    

    @property
    def source18(self):
        return self.__source18

    @source18.setter
    def source18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__source18", None)
        self.__source18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Different19"):
                    opp_val = getattr(item, "Different19", None)
                    
                    if opp_val == self:
                        setattr(item, "Different19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Different19"):
                    opp_val = getattr(item, "Different19", None)
                    
                    setattr(item, "Different19", self)
                    

    @property
    def NodePattern56(self):
        return self.__NodePattern56

    @NodePattern56.setter
    def NodePattern56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern56", None)
        self.__NodePattern56 = value
        
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
    def trnet_NodePattern(self):
        return self.__trnet_NodePattern

    @trnet_NodePattern.setter
    def trnet_NodePattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__trnet_NodePattern", None)
        self.__trnet_NodePattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnet_AttributePattern"):
                    opp_val = getattr(item, "trnet_AttributePattern", None)
                    
                    if opp_val == self:
                        setattr(item, "trnet_AttributePattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnet_AttributePattern"):
                    opp_val = getattr(item, "trnet_AttributePattern", None)
                    
                    setattr(item, "trnet_AttributePattern", self)
                    

    @property
    def NodePattern46(self):
        return self.__NodePattern46

    @NodePattern46.setter
    def NodePattern46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern46", None)
        self.__NodePattern46 = value
        
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
    def NodePattern31(self):
        return self.__NodePattern31

    @NodePattern31.setter
    def NodePattern31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern31", None)
        self.__NodePattern31 = value
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgePattern7"):
                    opp_val = getattr(item, "EdgePattern7", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgePattern7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgePattern7"):
                    opp_val = getattr(item, "EdgePattern7", None)
                    
                    setattr(item, "EdgePattern7", self)
                    

    @property
    def NodePattern65(self):
        return self.__NodePattern65

    @NodePattern65.setter
    def NodePattern65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern65", None)
        self.__NodePattern65 = value
        
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
    def NodePattern67(self):
        return self.__NodePattern67

    @NodePattern67.setter
    def NodePattern67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern67", None)
        self.__NodePattern67 = value
        
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
    def NodePattern54(self):
        return self.__NodePattern54

    @NodePattern54.setter
    def NodePattern54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern54", None)
        self.__NodePattern54 = value
        
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
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__nodes", None)
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__target", None)
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
    def NodePattern48(self):
        return self.__NodePattern48

    @NodePattern48.setter
    def NodePattern48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern48", None)
        self.__NodePattern48 = value
        
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
    def NodePattern27(self):
        return self.__NodePattern27

    @NodePattern27.setter
    def NodePattern27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__NodePattern27", None)
        self.__NodePattern27 = value
        
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
    def source23(self):
        return self.__source23

    @source23.setter
    def source23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__source23", None)
        self.__source23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Keep24"):
                    opp_val = getattr(item, "Keep24", None)
                    
                    if opp_val == self:
                        setattr(item, "Keep24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Keep24"):
                    opp_val = getattr(item, "Keep24", None)
                    
                    setattr(item, "Keep24", self)
                    

    @property
    def target16(self):
        return self.__target16

    @target16.setter
    def target16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__target16", None)
        self.__target16 = value if value is not None else set()
        
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
    def target21(self):
        return self.__target21

    @target21.setter
    def target21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_NodePattern__target21", None)
        self.__target21 = value if value is not None else set()
        
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
                    

class trnet_FlowRule(ABC):

    pass
class trnet_Operator(ABC):

    def __init__(self, id: str, trnet_Operator: "trnet_TrNetModel" = None, Operator: "trnet_Operand" = None, operator: set["trnet_Operand"] = None, operator42: set["trnet_Result"] = None, Operator63: "trnet_Result" = None):
        self.id = id
        self.trnet_Operator = trnet_Operator
        self.Operator = Operator
        self.operator = operator if operator is not None else set()
        self.operator42 = operator42 if operator42 is not None else set()
        self.Operator63 = Operator63
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def operator42(self):
        return self.__operator42

    @operator42.setter
    def operator42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operator__operator42", None)
        self.__operator42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Result43"):
                    opp_val = getattr(item, "Result43", None)
                    
                    if opp_val == self:
                        setattr(item, "Result43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Result43"):
                    opp_val = getattr(item, "Result43", None)
                    
                    setattr(item, "Result43", self)
                    

    @property
    def Operator63(self):
        return self.__Operator63

    @Operator63.setter
    def Operator63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operator__Operator63", None)
        self.__Operator63 = value
        
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
    def Operator(self):
        return self.__Operator

    @Operator.setter
    def Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operator__Operator", None)
        self.__Operator = value
        
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
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operator__operator", None)
        self.__operator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operand40"):
                    opp_val = getattr(item, "Operand40", None)
                    
                    if opp_val == self:
                        setattr(item, "Operand40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operand40"):
                    opp_val = getattr(item, "Operand40", None)
                    
                    setattr(item, "Operand40", self)
                    

    @property
    def trnet_Operator(self):
        return self.__trnet_Operator

    @trnet_Operator.setter
    def trnet_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Operator__trnet_Operator", None)
        self.__trnet_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnet_TrNetModel2"):
                opp_val = getattr(old_value, "trnet_TrNetModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnet_TrNetModel2"):
                opp_val = getattr(value, "trnet_TrNetModel2", None)
                if opp_val is None:
                    setattr(value, "trnet_TrNetModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trnet_Pattern:

    def __init__(self, id: str, expected_size: int, trnet_Pattern: "trnet_TrNetModel" = None, Pattern: "trnet_NodePattern" = None, Pattern29: "trnet_EdgePattern" = None, pattern: set["trnet_NodePattern"] = None, pattern33: set["trnet_EdgePattern"] = None, pattern36: set["trnet_Operand"] = None, pattern38: set["trnet_Result"] = None, Pattern58: "trnet_Operand" = None, Pattern61: "trnet_Result" = None):
        self.id = id
        self.expected_size = expected_size
        self.trnet_Pattern = trnet_Pattern
        self.Pattern = Pattern
        self.Pattern29 = Pattern29
        self.pattern = pattern if pattern is not None else set()
        self.pattern33 = pattern33 if pattern33 is not None else set()
        self.pattern36 = pattern36 if pattern36 is not None else set()
        self.pattern38 = pattern38 if pattern38 is not None else set()
        self.Pattern58 = Pattern58
        self.Pattern61 = Pattern61
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def expected_size(self) -> int:
        return self.__expected_size

    @expected_size.setter
    def expected_size(self, expected_size: int):
        self.__expected_size = expected_size

    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__pattern", None)
        self.__pattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodePattern31"):
                    opp_val = getattr(item, "NodePattern31", None)
                    
                    if opp_val == self:
                        setattr(item, "NodePattern31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodePattern31"):
                    opp_val = getattr(item, "NodePattern31", None)
                    
                    setattr(item, "NodePattern31", self)
                    

    @property
    def Pattern29(self):
        return self.__Pattern29

    @Pattern29.setter
    def Pattern29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__Pattern29", None)
        self.__Pattern29 = value
        
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
    def pattern36(self):
        return self.__pattern36

    @pattern36.setter
    def pattern36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__pattern36", None)
        self.__pattern36 = value if value is not None else set()
        
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
    def pattern38(self):
        return self.__pattern38

    @pattern38.setter
    def pattern38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__pattern38", None)
        self.__pattern38 = value if value is not None else set()
        
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
    def pattern33(self):
        return self.__pattern33

    @pattern33.setter
    def pattern33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__pattern33", None)
        self.__pattern33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgePattern34"):
                    opp_val = getattr(item, "EdgePattern34", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgePattern34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgePattern34"):
                    opp_val = getattr(item, "EdgePattern34", None)
                    
                    setattr(item, "EdgePattern34", self)
                    

    @property
    def Pattern61(self):
        return self.__Pattern61

    @Pattern61.setter
    def Pattern61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__Pattern61", None)
        self.__Pattern61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incommingResults"):
                opp_val = getattr(old_value, "incommingResults", None)
                if opp_val == self:
                    setattr(old_value, "incommingResults", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incommingResults"):
                opp_val = getattr(value, "incommingResults", None)
                setattr(value, "incommingResults", self)

    @property
    def Pattern58(self):
        return self.__Pattern58

    @Pattern58.setter
    def Pattern58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__Pattern58", None)
        self.__Pattern58 = value
        
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
    def Pattern(self):
        return self.__Pattern

    @Pattern.setter
    def Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__Pattern", None)
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
    def trnet_Pattern(self):
        return self.__trnet_Pattern

    @trnet_Pattern.setter
    def trnet_Pattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_Pattern__trnet_Pattern", None)
        self.__trnet_Pattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnet_TrNetModel"):
                opp_val = getattr(old_value, "trnet_TrNetModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnet_TrNetModel"):
                opp_val = getattr(value, "trnet_TrNetModel", None)
                if opp_val is None:
                    setattr(value, "trnet_TrNetModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trnet_TrNetModel:

    def __init__(self, id: str, trnet_TrNetModel: set["trnet_Pattern"] = None, trnet_TrNetModel2: set["trnet_Operator"] = None, trnet_TrNetModel4: set["trnet_FlowRule"] = None, trnet_TrNetModel72: "trnet_FlowRule" = None, trnet_TrNetModel75: "trnet_FlowRule" = None):
        self.id = id
        self.trnet_TrNetModel = trnet_TrNetModel if trnet_TrNetModel is not None else set()
        self.trnet_TrNetModel2 = trnet_TrNetModel2 if trnet_TrNetModel2 is not None else set()
        self.trnet_TrNetModel4 = trnet_TrNetModel4 if trnet_TrNetModel4 is not None else set()
        self.trnet_TrNetModel72 = trnet_TrNetModel72
        self.trnet_TrNetModel75 = trnet_TrNetModel75
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def trnet_TrNetModel4(self):
        return self.__trnet_TrNetModel4

    @trnet_TrNetModel4.setter
    def trnet_TrNetModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_TrNetModel__trnet_TrNetModel4", None)
        self.__trnet_TrNetModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnet_FlowRule"):
                    opp_val = getattr(item, "trnet_FlowRule", None)
                    
                    if opp_val == self:
                        setattr(item, "trnet_FlowRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnet_FlowRule"):
                    opp_val = getattr(item, "trnet_FlowRule", None)
                    
                    setattr(item, "trnet_FlowRule", self)
                    

    @property
    def trnet_TrNetModel2(self):
        return self.__trnet_TrNetModel2

    @trnet_TrNetModel2.setter
    def trnet_TrNetModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_TrNetModel__trnet_TrNetModel2", None)
        self.__trnet_TrNetModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnet_Operator"):
                    opp_val = getattr(item, "trnet_Operator", None)
                    
                    if opp_val == self:
                        setattr(item, "trnet_Operator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnet_Operator"):
                    opp_val = getattr(item, "trnet_Operator", None)
                    
                    setattr(item, "trnet_Operator", self)
                    

    @property
    def trnet_TrNetModel72(self):
        return self.__trnet_TrNetModel72

    @trnet_TrNetModel72.setter
    def trnet_TrNetModel72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_TrNetModel__trnet_TrNetModel72", None)
        self.__trnet_TrNetModel72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnet_FlowRule71"):
                opp_val = getattr(old_value, "trnet_FlowRule71", None)
                if opp_val == self:
                    setattr(old_value, "trnet_FlowRule71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnet_FlowRule71"):
                opp_val = getattr(value, "trnet_FlowRule71", None)
                setattr(value, "trnet_FlowRule71", self)

    @property
    def trnet_TrNetModel(self):
        return self.__trnet_TrNetModel

    @trnet_TrNetModel.setter
    def trnet_TrNetModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_TrNetModel__trnet_TrNetModel", None)
        self.__trnet_TrNetModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trnet_Pattern"):
                    opp_val = getattr(item, "trnet_Pattern", None)
                    
                    if opp_val == self:
                        setattr(item, "trnet_Pattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trnet_Pattern"):
                    opp_val = getattr(item, "trnet_Pattern", None)
                    
                    setattr(item, "trnet_Pattern", self)
                    

    @property
    def trnet_TrNetModel75(self):
        return self.__trnet_TrNetModel75

    @trnet_TrNetModel75.setter
    def trnet_TrNetModel75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trnet_TrNetModel__trnet_TrNetModel75", None)
        self.__trnet_TrNetModel75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trnet_FlowRule74"):
                opp_val = getattr(old_value, "trnet_FlowRule74", None)
                if opp_val == self:
                    setattr(old_value, "trnet_FlowRule74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trnet_FlowRule74"):
                opp_val = getattr(value, "trnet_FlowRule74", None)
                setattr(value, "trnet_FlowRule74", self)
