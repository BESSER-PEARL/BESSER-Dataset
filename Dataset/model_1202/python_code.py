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
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ACG_CollectionExp(LiteralExp):

    pass
class ACG_BooleanExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ACG_StringExp(LiteralExp):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ACG_OclUndefinedExp(LiteralExp):

    pass
class OperationCallExp:

    pass
class ACG_OperatorCallExp(OperationCallExp):

    pass
class PropertyCallExp:

    pass
class ACG_OperationCallExp(PropertyCallExp):

    pass
class ACG_IteratorExp(PropertyCallExp):

    pass
class ACG_NavigationExp(PropertyCallExp):

    pass
class EmitWithLabelRefStat:

    pass
class ACG_GotoStat(EmitWithLabelRefStat):

    pass
class ACG_IfStat(EmitWithLabelRefStat):

    pass
class LabelStat:

    pass
class EmitStat:

    pass
class ACG_DupStat(EmitStat):

    pass
class ACG_DeleteStat(EmitStat):

    pass
class ACG_PopStat(EmitStat):

    pass
class ACG_FindMEStat(EmitStat):

    pass
class ACG_PushFStat(EmitStat):

    pass
class ACG_EndIterateStat(EmitStat):

    pass
class ACG_SwapStat(EmitStat):

    pass
class ACG_NewStat(EmitStat):

    pass
class ACG_GetAsmStat(EmitStat):

    pass
class ACG_PushTStat(EmitStat):

    pass
class ACG_DupX1Stat(EmitStat):

    pass
class ACG_NewinStat(EmitStat):

    pass
class ACG_EmitWithLabelRefStat(EmitStat):

    pass
class ACG_EmitWithOperandStat(EmitStat):

    pass
class ACG_IterateStat(EmitStat):

    pass
class ACG_LabelStat(EmitStat):

    def __init__(self, name: str, ACG_LabelStat: "Expression" = None):
        self.name = name
        self.ACG_LabelStat = ACG_LabelStat
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "Expression51"):
                opp_val = getattr(old_value, "Expression51", None)
                if opp_val == self:
                    setattr(old_value, "Expression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression51"):
                opp_val = getattr(value, "Expression51", None)
                setattr(value, "Expression51", self)

class EmitWithOperandStat:

    pass
class ACG_SuperCallStat(EmitWithOperandStat):

    pass
class ACG_PCallStat(EmitWithOperandStat):

    pass
class ACG_LoadStat(EmitWithOperandStat):

    pass
class ACG_PushIStat(EmitWithOperandStat):

    pass
class ACG_SetStat(EmitWithOperandStat):

    pass
class ACG_PushDStat(EmitWithOperandStat):

    pass
class ACG_CallStat(EmitWithOperandStat):

    pass
class ACG_GetStat(EmitWithOperandStat):

    pass
class ACG_StoreStat(EmitWithOperandStat):

    pass
class ACG_PushStat(EmitWithOperandStat):

    pass
class CompoundStat:

    pass
class ACG_OperationStat(CompoundStat):

    pass
class ACG_VariableStat(CompoundStat):

    pass
class ACG_LetStat(CompoundStat):

    pass
class ACG_OnceStat(CompoundStat):

    pass
class ACG_ConditionalStat(CompoundStat):

    pass
class ACG_ForEachStat(CompoundStat):

    pass
class Statement:

    pass
class ACG_EmitStat(Statement):

    pass
class ACG_FieldStat(Statement):

    pass
class ACG_ParamStat(Statement):

    pass
class Node:

    pass
class ACG_CodeNode(Node):

    pass
class ACG_SimpleNode(Node):

    pass
class ACG_ASMNode(Node):

    pass
class ACG_ReportStat(Statement):

    def __init__(self, severity: str, ACG_ReportStat: "Expression" = None, Statement30: "ACG_ConditionalStat" = None, Statement: "ACG_StatementBlock" = None):
        self.severity = severity
        self.ACG_ReportStat = ACG_ReportStat
        
        pass
    @property
    def severity(self):
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
            if hasattr(old_value, "Expression39"):
                opp_val = getattr(old_value, "Expression39", None)
                if opp_val == self:
                    setattr(old_value, "Expression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression39"):
                opp_val = getattr(value, "Expression39", None)
                setattr(value, "Expression39", self)

class ACG_AnalyzeStat(CompoundStat):

    def __init__(self, mode: str, ACG_AnalyzeStat: "Expression" = None):
        self.mode = mode
        self.ACG_AnalyzeStat = ACG_AnalyzeStat
        
        pass
    @property
    def mode(self):
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
            if hasattr(old_value, "Expression37"):
                opp_val = getattr(old_value, "Expression37", None)
                if opp_val == self:
                    setattr(old_value, "Expression37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression37"):
                opp_val = getattr(value, "Expression37", None)
                setattr(value, "Expression37", self)

class Expression:

    pass
class ACG_SelfExp(Expression):

    pass
class ACG_LastExp(Expression):

    pass
class ACG_LiteralExp(Expression):

    pass
class ACG_PropertyCallExp(Expression):

    def __init__(self, name: str, ACG_PropertyCallExp: "Expression" = None, Expression74: "ACG_LetExp" = None, Expression37: "ACG_AnalyzeStat" = None, Expression51: "ACG_LabelStat" = None, Expression46: "ACG_ParamStat" = None, Expression66: "ACG_IsAExp" = None, Expression41: "ACG_FieldStat" = None, Expression64: "ACG_IfExp" = None, Expression39: "ACG_ReportStat" = None, Expression25: "ACG_OperationStat" = None, Expression61: "ACG_IfExp" = None, Expression83: "ACG_OperationCallExp" = None, Expression10: "ACG_ASMNode" = None, Expression81: "ACG_IteratorExp" = None, Expression35: "ACG_LetStat" = None, Expression8: "ACG_Node" = None, Expression85: "ACG_CollectionExp" = None, Expression58: "ACG_IfExp" = None, Expression22: "ACG_OperationStat" = None, Expression27: "ACG_ConditionalStat" = None, Expression53: "ACG_EmitWithOperandStat" = None, Expression44: "ACG_FieldStat" = None, Expression6: "ACG_Attribute" = None, Expression17: "ACG_VariableStat" = None, Expression15: "ACG_ForEachStat" = None, Expression49: "ACG_ParamStat" = None, Expression20: "ACG_VariableStat" = None, Expression76: "ACG_PropertyCallExp" = None, Expression: "ACG_Function" = None, Expression71: "ACG_LetExp" = None):
        self.name = name
        self.ACG_PropertyCallExp = ACG_PropertyCallExp
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "Expression76"):
                opp_val = getattr(old_value, "Expression76", None)
                if opp_val == self:
                    setattr(old_value, "Expression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression76"):
                opp_val = getattr(value, "Expression76", None)
                setattr(value, "Expression76", self)

class ACG_IsAExp(Expression):

    def __init__(self, type: str, ACG_IsAExp: "Expression" = None, Expression74: "ACG_LetExp" = None, Expression37: "ACG_AnalyzeStat" = None, Expression51: "ACG_LabelStat" = None, Expression46: "ACG_ParamStat" = None, Expression66: "ACG_IsAExp" = None, Expression41: "ACG_FieldStat" = None, Expression64: "ACG_IfExp" = None, Expression39: "ACG_ReportStat" = None, Expression25: "ACG_OperationStat" = None, Expression61: "ACG_IfExp" = None, Expression83: "ACG_OperationCallExp" = None, Expression10: "ACG_ASMNode" = None, Expression81: "ACG_IteratorExp" = None, Expression35: "ACG_LetStat" = None, Expression8: "ACG_Node" = None, Expression85: "ACG_CollectionExp" = None, Expression58: "ACG_IfExp" = None, Expression22: "ACG_OperationStat" = None, Expression27: "ACG_ConditionalStat" = None, Expression53: "ACG_EmitWithOperandStat" = None, Expression44: "ACG_FieldStat" = None, Expression6: "ACG_Attribute" = None, Expression17: "ACG_VariableStat" = None, Expression15: "ACG_ForEachStat" = None, Expression49: "ACG_ParamStat" = None, Expression20: "ACG_VariableStat" = None, Expression76: "ACG_PropertyCallExp" = None, Expression: "ACG_Function" = None, Expression71: "ACG_LetExp" = None):
        self.type = type
        self.ACG_IsAExp = ACG_IsAExp
        
        pass
    @property
    def type(self):
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
            if hasattr(old_value, "Expression66"):
                opp_val = getattr(old_value, "Expression66", None)
                if opp_val == self:
                    setattr(old_value, "Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression66"):
                opp_val = getattr(value, "Expression66", None)
                setattr(value, "Expression66", self)

class ACG_IfExp(Expression):

    pass
class ACG_LetExp(Expression):

    pass
class ACG_VariableExp(Expression):

    pass
class Parameter:

    pass
class ACG:

    pass
class ACGElement:

    pass
class ACG_Attribute(ACGElement):

    def __init__(self, context: str, name: str, ACG_Attribute: "Expression" = None, ACGElement: "ACG_ACG" = None):
        self.context = context
        self.name = name
        self.ACG_Attribute = ACG_Attribute
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


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
            if hasattr(old_value, "Expression6"):
                opp_val = getattr(old_value, "Expression6", None)
                if opp_val == self:
                    setattr(old_value, "Expression6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression6"):
                opp_val = getattr(value, "Expression6", None)
                setattr(value, "Expression6", self)

class ACG_Function(ACGElement):

    def __init__(self, context: str, name: str, ACG_Function: set["Parameter"] = None, ACG_Function4: "Expression" = None, ACGElement: "ACG_ACG" = None):
        self.context = context
        self.name = name
        self.ACG_Function = ACG_Function if ACG_Function is not None else set()
        self.ACG_Function4 = ACG_Function4
        
        pass
    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ACG_Function4(self):
        return self.__ACG_Function4

    @ACG_Function4.setter
    def ACG_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_Function__ACG_Function4", None)
        self.__ACG_Function4 = value
        
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
                    

class LocatedElement:

    pass
class ACG_Statement(LocatedElement):

    pass
class ACG_VariableDecl(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ACG_ACGElement(LocatedElement):

    pass
class ACG_Expression(LocatedElement):

    pass
class ACG_StatementBlock(LocatedElement):

    pass
class ACG_ACG(LocatedElement):

    def __init__(self, metamodel: str, startsWith: str, acg: set["ACGElement"] = None):
        self.metamodel = metamodel
        self.startsWith = startsWith
        self.acg = acg if acg is not None else set()
        
        pass
    @property
    def startsWith(self):
        return self.__startsWith

    @startsWith.setter
    def startsWith(self, startsWith: str):
        self.__startsWith = startsWith


    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel


    @property
    def acg(self):
        return self.__acg

    @acg.setter
    def acg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACG_ACG__acg", None)
        self.__acg = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ACGElement"):
                    opp_val = getattr(item, "ACGElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ACGElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ACGElement"):
                    opp_val = getattr(item, "ACGElement", None)
                    
                    setattr(item, "ACGElement", self)
                    

class ACG_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


class StatementBlock:

    pass
class ACG_CompoundStat(StatementBlock, Statement):

    pass
class ACG_Node(StatementBlock, ACGElement):

    def __init__(self, element: str, mode: str, ACG_Node: "Expression" = None, ACGElement: "ACG_ACG" = None):
        self.element = element
        self.mode = mode
        self.ACG_Node = ACG_Node
        
        pass
    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element


    @property
    def mode(self):
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
            if hasattr(old_value, "Expression8"):
                opp_val = getattr(old_value, "Expression8", None)
                if opp_val == self:
                    setattr(old_value, "Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression8"):
                opp_val = getattr(value, "Expression8", None)
                setattr(value, "Expression8", self)

class VariableDecl:

    pass
class ACG_Parameter(VariableDecl):

    pass