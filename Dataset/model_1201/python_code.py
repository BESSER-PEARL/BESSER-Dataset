from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Severity(Enum):
    critic = "critic"
    error = "error"
    warning = "warning"


############################################
# Definition of Classes
############################################

class CollectionExp:

    pass
class ACG_SequenceExp(CollectionExp):

    pass
class LiteralExp:

    pass
class ACG_IntegerExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ACG_StringExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ACG_BooleanExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ACG_CollectionExp(LiteralExp):

    pass
class ACG_OclUndefinedExp(LiteralExp):

    pass
class OperationCallExp:

    pass
class ACG_OperatorCallExp(OperationCallExp):

    pass
class PropertyCallExp:

    pass
class ACG_IteratorExp(PropertyCallExp):

    pass
class ACG_OperationCallExp(PropertyCallExp):

    pass
class ACG_NavigationExp(PropertyCallExp):

    pass
class EmitWithOperandStat:

    pass
class ACG_PushIStat(EmitWithOperandStat):

    pass
class ACG_PushStat(EmitWithOperandStat):

    pass
class EmitWithLabelRefStat:

    pass
class ACG_GotoStat(EmitWithLabelRefStat):

    pass
class ACG_IfStat(EmitWithLabelRefStat):

    pass
class LabelStat:

    pass
class ACG_SetStat(EmitWithOperandStat):

    pass
class ACG_GetStat(EmitWithOperandStat):

    pass
class ACG_SuperCallStat(EmitWithOperandStat):

    pass
class ACG_PCallStat(EmitWithOperandStat):

    pass
class ACG_CallStat(EmitWithOperandStat):

    pass
class ACG_StoreStat(EmitWithOperandStat):

    pass
class ACG_LoadStat(EmitWithOperandStat):

    pass
class ACG_PushDStat(EmitWithOperandStat):

    pass
class EmitStat:

    pass
class ACG_DeleteStat(EmitStat):

    pass
class ACG_NewStat(EmitStat):

    pass
class ACG_DupStat(EmitStat):

    pass
class ACG_PopStat(EmitStat):

    pass
class ACG_PushTStat(EmitStat):

    pass
class ACG_GetAsmStat(EmitStat):

    pass
class ACG_NewinStat(EmitStat):

    pass
class ACG_DupX1Stat(EmitStat):

    pass
class ACG_SwapStat(EmitStat):

    pass
class ACG_FindMEStat(EmitStat):

    pass
class ACG_PushFStat(EmitStat):

    pass
class ACG_EmitWithOperandStat(EmitStat):

    pass
class ACG_EndIterateStat(EmitStat):

    pass
class ACG_IterateStat(EmitStat):

    pass
class ACG_EmitWithLabelRefStat(EmitStat):

    pass
class ACG_LabelStat(EmitStat):

    def __init__(self, name: str, ACG_LabelStat: "Expression" = None):
        self.name = name
        self.ACG_LabelStat = ACG_LabelStat
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ACG_LabelStat(self):
        return self.__ACG_LabelStat

    @ACG_LabelStat.setter
    def ACG_LabelStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_LabelStat__ACG_LabelStat", None)
        self.__ACG_LabelStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression53"):
                opp_val = getattr(old_value, "Expression53", None)
                if opp_val == self:
                    setattr(old_value, "Expression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression53"):
                opp_val = getattr(value, "Expression53", None)
                setattr(value, "Expression53", self)

class Expression:

    pass
class ACG_LetExp(Expression):

    pass
class ACG_LastExp(Expression):

    pass
class ACG_IfExp(Expression):

    pass
class ACG_SelfExp(Expression):

    pass
class ACG_VariableExp(Expression):

    pass
class ACG_IsAExp(Expression):

    def __init__(self, type: str, ACG_IsAExp: "Expression" = None, Expression: "ACG_Function", Expression73: "ACG_LetExp", Expression55: "ACG_EmitWithOperandStat", Expression53: "ACG_LabelStat", Expression48: "ACG_ParamStat", Expression43: "ACG_FieldStat", Expression78: "ACG_PropertyCallExp", Expression66: "ACG_IfExp", Expression63: "ACG_IfExp", Expression76: "ACG_LetExp", Expression60: "ACG_IfExp", Expression22: "ACG_VariableStat", Expression10: "ACG_Node", Expression85: "ACG_OperationCallExp", Expression27: "ACG_OperationStat", Expression39: "ACG_AnalyzeStat", Expression51: "ACG_ParamStat", Expression24: "ACG_OperationStat", Expression41: "ACG_ReportStat", Expression12: "ACG_ASMNode", Expression83: "ACG_IteratorExp", Expression8: "ACG_Attribute", Expression68: "ACG_IsAExp", Expression46: "ACG_FieldStat", Expression29: "ACG_ConditionalStat", Expression17: "ACG_ForEachStat", Expression19: "ACG_VariableStat", Expression37: "ACG_LetStat", Expression87: "ACG_CollectionExp"):
        self.type = type
        self.ACG_IsAExp = ACG_IsAExp
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ACG_IsAExp(self):
        return self.__ACG_IsAExp

    @ACG_IsAExp.setter
    def ACG_IsAExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_IsAExp__ACG_IsAExp", None)
        self.__ACG_IsAExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression68"):
                opp_val = getattr(old_value, "Expression68", None)
                if opp_val == self:
                    setattr(old_value, "Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression68"):
                opp_val = getattr(value, "Expression68", None)
                setattr(value, "Expression68", self)

class ACG_PropertyCallExp(Expression):

    def __init__(self, name: str, ACG_PropertyCallExp: "Expression" = None, Expression: "ACG_Function", Expression73: "ACG_LetExp", Expression55: "ACG_EmitWithOperandStat", Expression53: "ACG_LabelStat", Expression48: "ACG_ParamStat", Expression43: "ACG_FieldStat", Expression78: "ACG_PropertyCallExp", Expression66: "ACG_IfExp", Expression63: "ACG_IfExp", Expression76: "ACG_LetExp", Expression60: "ACG_IfExp", Expression22: "ACG_VariableStat", Expression10: "ACG_Node", Expression85: "ACG_OperationCallExp", Expression27: "ACG_OperationStat", Expression39: "ACG_AnalyzeStat", Expression51: "ACG_ParamStat", Expression24: "ACG_OperationStat", Expression41: "ACG_ReportStat", Expression12: "ACG_ASMNode", Expression83: "ACG_IteratorExp", Expression8: "ACG_Attribute", Expression68: "ACG_IsAExp", Expression46: "ACG_FieldStat", Expression29: "ACG_ConditionalStat", Expression17: "ACG_ForEachStat", Expression19: "ACG_VariableStat", Expression37: "ACG_LetStat", Expression87: "ACG_CollectionExp"):
        self.name = name
        self.ACG_PropertyCallExp = ACG_PropertyCallExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ACG_PropertyCallExp(self):
        return self.__ACG_PropertyCallExp

    @ACG_PropertyCallExp.setter
    def ACG_PropertyCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_PropertyCallExp__ACG_PropertyCallExp", None)
        self.__ACG_PropertyCallExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression78"):
                opp_val = getattr(old_value, "Expression78", None)
                if opp_val == self:
                    setattr(old_value, "Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression78"):
                opp_val = getattr(value, "Expression78", None)
                setattr(value, "Expression78", self)

class ACG_LiteralExp(Expression):

    pass
class Parameter:

    pass
class CompoundStat:

    pass
class ACG_VariableStat(CompoundStat):

    pass
class ACG_OperationStat(CompoundStat):

    pass
class ACG_ConditionalStat(CompoundStat):

    pass
class ACG_AnalyzeStat(CompoundStat):

    def __init__(self, mode: str, ACG_AnalyzeStat: "Expression" = None):
        self.mode = mode
        self.ACG_AnalyzeStat = ACG_AnalyzeStat
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def ACG_AnalyzeStat(self):
        return self.__ACG_AnalyzeStat

    @ACG_AnalyzeStat.setter
    def ACG_AnalyzeStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_AnalyzeStat__ACG_AnalyzeStat", None)
        self.__ACG_AnalyzeStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression39"):
                opp_val = getattr(old_value, "Expression39", None)
                if opp_val == self:
                    setattr(old_value, "Expression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression39"):
                opp_val = getattr(value, "Expression39", None)
                setattr(value, "Expression39", self)

class ACG_LetStat(CompoundStat):

    pass
class ACG_OnceStat(CompoundStat):

    pass
class ACG_ForEachStat(CompoundStat):

    pass
class Statement:

    pass
class ACG_ParamStat(Statement):

    pass
class ACG_ReportStat(Statement):

    def __init__(self, severity: str, ACG_ReportStat: "Expression" = None, Statement: "ACG_StatementBlock", Statement32: "ACG_ConditionalStat"):
        self.severity = severity
        self.ACG_ReportStat = ACG_ReportStat
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def ACG_ReportStat(self):
        return self.__ACG_ReportStat

    @ACG_ReportStat.setter
    def ACG_ReportStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_ReportStat__ACG_ReportStat", None)
        self.__ACG_ReportStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression41"):
                opp_val = getattr(old_value, "Expression41", None)
                if opp_val == self:
                    setattr(old_value, "Expression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression41"):
                opp_val = getattr(value, "Expression41", None)
                setattr(value, "Expression41", self)

class ACG_FieldStat(Statement):

    pass
class ACG_EmitStat(Statement):

    pass
class Node:

    pass
class ACG_CodeNode(Node):

    pass
class ACG_SimpleNode(Node):

    pass
class ACG_ASMNode(Node):

    pass
class StatementBlock:

    pass
class ACG_CompoundStat(Statement, StatementBlock):

    pass
class VariableDecl:

    pass
class ACG_Parameter(VariableDecl):

    pass
class ACG:

    pass
class ACGElement:

    pass
class ACG_Attribute(ACGElement):

    def __init__(self, context: str, name: str, ACG_Attribute: "Expression" = None, : "ACG_ACG"):
        self.context = context
        self.name = name
        self.ACG_Attribute = ACG_Attribute
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ACG_Attribute(self):
        return self.__ACG_Attribute

    @ACG_Attribute.setter
    def ACG_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_Attribute__ACG_Attribute", None)
        self.__ACG_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression8"):
                opp_val = getattr(old_value, "Expression8", None)
                if opp_val == self:
                    setattr(old_value, "Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression8"):
                opp_val = getattr(value, "Expression8", None)
                setattr(value, "Expression8", self)

class ACG_Function(ACGElement):

    def __init__(self, context: str, name: str, ACG_Function: set["Parameter"] = None, ACG_Function6: "Expression" = None, : "ACG_ACG"):
        self.context = context
        self.name = name
        self.ACG_Function = ACG_Function if ACG_Function is not None else set()
        self.ACG_Function6 = ACG_Function6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def ACG_Function6(self):
        return self.__ACG_Function6

    @ACG_Function6.setter
    def ACG_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_Function__ACG_Function6", None)
        self.__ACG_Function6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression"):
                opp_val = getattr(old_value, "Expression", None)
                if opp_val == self:
                    setattr(old_value, "Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression"):
                opp_val = getattr(value, "Expression", None)
                setattr(value, "Expression", self)

    @property
    def ACG_Function(self):
        return self.__ACG_Function

    @ACG_Function.setter
    def ACG_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_Function__ACG_Function", None)
        self.__ACG_Function = value if value is not None else set()
        
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
                    

class ACG_Node(StatementBlock, ACGElement):

    def __init__(self, element: str, mode: str, ACG_Node: "Expression" = None, : "ACG_ACG"):
        self.element = element
        self.mode = mode
        self.ACG_Node = ACG_Node
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def ACG_Node(self):
        return self.__ACG_Node

    @ACG_Node.setter
    def ACG_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_Node__ACG_Node", None)
        self.__ACG_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression10"):
                opp_val = getattr(old_value, "Expression10", None)
                if opp_val == self:
                    setattr(old_value, "Expression10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression10"):
                opp_val = getattr(value, "Expression10", None)
                setattr(value, "Expression10", self)

class LocatedElement:

    pass
class ACG_Statement(LocatedElement):

    pass
class ACG_VariableDecl(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ACG_StatementBlock(LocatedElement):

    pass
class ACG_ACGElement(LocatedElement):

    pass
class ACG_Expression(LocatedElement):

    pass
class ACG_ACG(LocatedElement):

    def __init__(self, metamodel: str, startsWith: str, 0: set["ACGElement"] = None):
        self.metamodel = metamodel
        self.startsWith = startsWith
        self.0 = 0 if 0 is not None else set()
        
    @property
    def startsWith(self) -> str:
        return self.__startsWith

    @startsWith.setter
    def startsWith(self, startsWith: str):
        self.__startsWith = startsWith

    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_ACG__0", None)
        self.__0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, ""):
                    opp_val = getattr(item, "", None)
                    
                    if opp_val == self:
                        setattr(item, "", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, ""):
                    opp_val = getattr(item, "", None)
                    
                    setattr(item, "", self)
                    

class ACG_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location
