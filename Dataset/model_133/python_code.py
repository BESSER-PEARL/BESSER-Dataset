from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ShiftOp:

    pass
class ast_RightShiftOp(ShiftOp):

    pass
class ast_ZeroExtensionRightShiftOp(ShiftOp):

    pass
class ast_LeftShiftOp(ShiftOp):

    pass
class DivisionOp:

    pass
class ast_RemainderOp(DivisionOp):

    pass
class ast_DivideOp(DivisionOp):

    pass
class ClassifierOp:

    pass
class ast_InstanceOfOp(ClassifierOp):

    pass
class ast_CastOp(ClassifierOp):

    pass
class Literal:

    pass
class ast_CharacterLiteral(Literal):

    pass
class ast_IntegerLiteral(Literal):

    pass
class ast_NullReference(Literal):

    pass
class ast_FloatLiteral(Literal):

    pass
class ast_StringLiteral(Literal):

    pass
class ast_LongIntegerLiteral(Literal):

    pass
class ast_DoubleLiteral(Literal):

    pass
class ast_BooleanLiteral(Literal):

    pass
class UnaryOp:

    pass
class ast_LogicalComplementOp(UnaryOp):

    pass
class ast_PostfixDecrementOp(UnaryOp):

    pass
class ast_UnaryMinusOp(UnaryOp):

    pass
class ast_UnaryPlusOp(UnaryOp):

    pass
class ast_PrefixDecrementOp(UnaryOp):

    pass
class ast_PostfixIncrementOp(UnaryOp):

    pass
class ast_PrefixIncrementOp(UnaryOp):

    pass
class ast_BitwiseComplementOp(UnaryOp):

    pass
class BinaryOp:

    pass
class ast_LessThenOp(BinaryOp):

    pass
class ast_BitwiseOrOp(BinaryOp):

    pass
class ast_BitwiseXorOp(BinaryOp):

    pass
class ast_ConditionalOrOp(BinaryOp):

    pass
class ast_ConditionalAndOp(BinaryOp):

    pass
class ast_NotEqualOp(BinaryOp):

    pass
class ast_GreaterOrEqualOp(BinaryOp):

    pass
class ast_EqualOp(BinaryOp):

    pass
class ast_GreaterThenOp(BinaryOp):

    pass
class ast_LessOrEqualOp(BinaryOp):

    pass
class ast_BitwiseAndOp(BinaryOp):

    pass
class AssignmentOperation:

    pass
class ast_PlusAssignmentOp(AssignmentOperation):

    pass
class ast_MultiplyAssignmentOp(AssignmentOperation):

    pass
class ast_DivideAssignmentOp(AssignmentOperation):

    pass
class ast_BitwiseOrAssignmentOp(AssignmentOperation):

    pass
class ast_LeftShiftAssignmentOp(AssignmentOperation):

    pass
class ast_RemainderAssignmentOp(AssignmentOperation):

    pass
class ast_BitwiseAndAssignmentOp(AssignmentOperation):

    pass
class ast_RightShiftAssignmentOp(AssignmentOperation):

    pass
class ast_BitwiseXorAssignmentOp(AssignmentOperation):

    pass
class ast_MinusAssignmentOp(AssignmentOperation):

    pass
class ast_ZeroExtensionRightShiftAssignmentOp(AssignmentOperation):

    pass
class ast_AssignmentOp(AssignmentOperation):

    pass
class Expression:

    pass
class ast_BinaryOp(Expression):

    pass
class ast_ApplyRoundOp(Expression):

    pass
class ast_ApplySquareOp(Expression):

    pass
class ast_DivisionOp(Expression):

    pass
class ast_Literal(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ast_PrimitiveType(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ast_ShiftOp(Expression):

    pass
class ast_WildcardType(Expression):

    pass
class ast_IdentityOp(Expression):

    pass
class ast_SuperReference(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ast_ThisReference(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ast_ArrayConstructor(Expression):

    pass
class ast_AssignmentOperation(Expression):

    pass
class ast_NewOp(Expression):

    pass
class ast_ClassifierOp(Expression):

    pass
class ast_PlusOp(Expression):

    pass
class ast_MinusOp(Expression):

    pass
class ast_RangeExpression(Expression):

    pass
class ast_UnaryOp(Expression):

    pass
class ast_MultiplyOp(Expression):

    pass
class ast_ConditionalOp(Expression):

    pass
class ast_AccessOp(Expression):

    pass
class ScopeStatement:

    pass
class ast_TryStatement(ScopeStatement):

    pass
class ast_SynchronizedStatement(ScopeStatement):

    pass
class SwitchPart:

    pass
class ast_SwitchDefaultPart(SwitchPart):

    pass
class ast_SwitchCasePart(SwitchPart):

    pass
class LabeledStatement:

    pass
class ast_SwitchStatement(LabeledStatement):

    pass
class ast_LoopStatement(LabeledStatement):

    pass
class MethodContentStatement:

    pass
class ast_JumpStatement(MethodContentStatement):

    pass
class ast_EmptyStatement(MethodContentStatement):

    pass
class ast_ScopeStatement(MethodContentStatement):

    pass
class ast_AssertStatement(MethodContentStatement):

    pass
class ast_ReturnStatement(MethodContentStatement):

    pass
class ast_ThrowStatement(MethodContentStatement):

    pass
class ast_MethodClassifier(MethodContentStatement):

    pass
class ast_IfStatement(MethodContentStatement):

    pass
class ast_LabeledStatement(MethodContentStatement):

    pass
class ast_LocalVarStatement(MethodContentStatement):

    pass
class JumpStatement:

    pass
class ast_BreakStatement(JumpStatement):

    pass
class ast_ExpressionStatement(MethodContentStatement):

    pass
class ConditionalLoop:

    pass
class ast_WhileStatement(ConditionalLoop):

    pass
class ast_ForStatement(ConditionalLoop):

    pass
class ast_DoWhileStatement(ConditionalLoop):

    pass
class ast_ContinueStatement(JumpStatement):

    pass
class LoopStatement:

    pass
class ast_ForeachStatement(LoopStatement):

    pass
class ast_ConditionalLoop(LoopStatement):

    pass
class TopLevelStatement:

    pass
class ast_TopLevelClassifier(TopLevelStatement):

    pass
class ast_PackageStatement(TopLevelStatement):

    pass
class ast_ImportStatement(TopLevelStatement):

    pass
class ClassifierStatement:

    pass
class ast_InterfaceStatement(ClassifierStatement):

    pass
class ast_AttributeDefinition(ClassifierStatement):

    pass
class ast_ImplemenationClassifierStatement(ClassifierStatement):

    pass
class ImplemenationClassifierStatement:

    pass
class ast_EnumStatement(ImplemenationClassifierStatement):

    pass
class ast_ClassStatement(ImplemenationClassifierStatement):

    pass
class InitStatement:

    pass
class ast_StaticInitStatement(InitStatement):

    pass
class ast_InstanceInitStatement(InitStatement):

    pass
class EJBase:

    pass
class ast_ClassifierStatement(EJBase):

    pass
class ast_IfThenPart(EJBase):

    pass
class ast_NamedElement(EJBase):

    pass
class ast_ClassifierMemberStatement(EJBase):

    pass
class ast_TopLevelStatement(EJBase):

    pass
class ast_SwitchPart(EJBase):

    pass
class ast_CatchPart(EJBase):

    pass
class ast_MethodContentStatement(EJBase):

    pass
class ast_ClassBlock(EJBase):

    pass
class ClassifierMemberStatement:

    pass
class ast_Feature(ClassifierMemberStatement):

    pass
class ast_InitStatement(ClassifierMemberStatement):

    pass
class ast_InnerClassifier(ClassifierMemberStatement):

    pass
class ast_EnumLiteral(ClassifierMemberStatement):

    pass
class ast_MethodBlock(MethodContentStatement):

    pass
class BehaviorFeature:

    pass
class ast_MethodStatement(BehaviorFeature):

    pass
class ast_ConstructorStatement(BehaviorFeature):

    pass
class ast_EJElement(ABC):

    def __init__(self, startLine: int, endLine: int, startColumn: int, endColumn: int, startOffset: str, endOffset: str):
        self.startLine = startLine
        self.endLine = endLine
        self.startColumn = startColumn
        self.endColumn = endColumn
        self.startOffset = startOffset
        self.endOffset = endOffset
        
    @property
    def startLine(self) -> int:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine

    @property
    def endOffset(self) -> str:
        return self.__endOffset

    @endOffset.setter
    def endOffset(self, endOffset: str):
        self.__endOffset = endOffset

    @property
    def startColumn(self) -> int:
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: int):
        self.__startColumn = startColumn

    @property
    def startOffset(self) -> str:
        return self.__startOffset

    @startOffset.setter
    def startOffset(self, startOffset: str):
        self.__startOffset = startOffset

    @property
    def endColumn(self) -> int:
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn

    @property
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

class ast_Identifier(Expression):

    def __init__(self, value: str, escapedValue: str, quotedValue: str, ast_Identifier: "ast_BehaviorFeature" = None, ast_Identifier32: "ast_EnumLiteral" = None, ast_Identifier77: "ast_ClassifierStatement" = None, ast_Identifier273: "ast_NamedElement" = None):
        self.value = value
        self.escapedValue = escapedValue
        self.quotedValue = quotedValue
        self.ast_Identifier = ast_Identifier
        self.ast_Identifier32 = ast_Identifier32
        self.ast_Identifier77 = ast_Identifier77
        self.ast_Identifier273 = ast_Identifier273
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def quotedValue(self) -> str:
        return self.__quotedValue

    @quotedValue.setter
    def quotedValue(self, quotedValue: str):
        self.__quotedValue = quotedValue

    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

    @property
    def ast_Identifier273(self):
        return self.__ast_Identifier273

    @ast_Identifier273.setter
    def ast_Identifier273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Identifier__ast_Identifier273", None)
        self.__ast_Identifier273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_NamedElement"):
                opp_val = getattr(old_value, "ast_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "ast_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_NamedElement"):
                opp_val = getattr(value, "ast_NamedElement", None)
                setattr(value, "ast_NamedElement", self)

    @property
    def ast_Identifier77(self):
        return self.__ast_Identifier77

    @ast_Identifier77.setter
    def ast_Identifier77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Identifier__ast_Identifier77", None)
        self.__ast_Identifier77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ClassifierStatement76"):
                opp_val = getattr(old_value, "ast_ClassifierStatement76", None)
                if opp_val == self:
                    setattr(old_value, "ast_ClassifierStatement76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ClassifierStatement76"):
                opp_val = getattr(value, "ast_ClassifierStatement76", None)
                setattr(value, "ast_ClassifierStatement76", self)

    @property
    def ast_Identifier(self):
        return self.__ast_Identifier

    @ast_Identifier.setter
    def ast_Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Identifier__ast_Identifier", None)
        self.__ast_Identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_BehaviorFeature19"):
                opp_val = getattr(old_value, "ast_BehaviorFeature19", None)
                if opp_val == self:
                    setattr(old_value, "ast_BehaviorFeature19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_BehaviorFeature19"):
                opp_val = getattr(value, "ast_BehaviorFeature19", None)
                setattr(value, "ast_BehaviorFeature19", self)

    @property
    def ast_Identifier32(self):
        return self.__ast_Identifier32

    @ast_Identifier32.setter
    def ast_Identifier32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Identifier__ast_Identifier32", None)
        self.__ast_Identifier32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_EnumLiteral31"):
                opp_val = getattr(old_value, "ast_EnumLiteral31", None)
                if opp_val == self:
                    setattr(old_value, "ast_EnumLiteral31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_EnumLiteral31"):
                opp_val = getattr(value, "ast_EnumLiteral31", None)
                setattr(value, "ast_EnumLiteral31", self)

class Feature:

    pass
class ast_FieldStatement(Feature):

    pass
class ast_BehaviorFeature(Feature):

    pass
class ast_Expression(EJBase):

    pass
class NamedElement:

    pass
class ast_Variable(NamedElement):

    pass
class ast_TemplateParameter(NamedElement):

    pass
class ast_Parameter(NamedElement):

    pass
class EJElement:

    pass
class ast_Modifier(EJElement):

    def __init__(self, value: str, ast_Modifier: "ast_Parameter" = None, ast_Modifier37: "ast_Feature" = None, ast_Modifier40: "ast_Feature" = None, ast_Modifier45: "ast_FieldStatement" = None, ast_Modifier48: "ast_FieldStatement" = None, ast_Modifier43: "ast_Feature" = None, ast_Modifier65: "ast_MethodStatement" = None, ast_Modifier68: "ast_MethodStatement" = None, ast_Modifier71: "ast_MethodStatement" = None, ast_Modifier74: "ast_MethodStatement" = None, ast_Modifier80: "ast_ClassifierStatement" = None, ast_Modifier88: "ast_ClassStatement" = None, ast_Modifier96: "ast_ImplemenationClassifierStatement" = None, ast_Modifier99: "ast_ImplemenationClassifierStatement" = None, ast_Modifier106: "ast_ImportStatement" = None, ast_Modifier109: "ast_ImportStatement" = None, ast_Modifier102: "ast_ImplemenationClassifierStatement" = None, ast_Modifier163: "ast_LocalVarStatement" = None):
        self.value = value
        self.ast_Modifier = ast_Modifier
        self.ast_Modifier37 = ast_Modifier37
        self.ast_Modifier40 = ast_Modifier40
        self.ast_Modifier45 = ast_Modifier45
        self.ast_Modifier48 = ast_Modifier48
        self.ast_Modifier43 = ast_Modifier43
        self.ast_Modifier65 = ast_Modifier65
        self.ast_Modifier68 = ast_Modifier68
        self.ast_Modifier71 = ast_Modifier71
        self.ast_Modifier74 = ast_Modifier74
        self.ast_Modifier80 = ast_Modifier80
        self.ast_Modifier88 = ast_Modifier88
        self.ast_Modifier96 = ast_Modifier96
        self.ast_Modifier99 = ast_Modifier99
        self.ast_Modifier106 = ast_Modifier106
        self.ast_Modifier109 = ast_Modifier109
        self.ast_Modifier102 = ast_Modifier102
        self.ast_Modifier163 = ast_Modifier163
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ast_Modifier74(self):
        return self.__ast_Modifier74

    @ast_Modifier74.setter
    def ast_Modifier74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier74", None)
        self.__ast_Modifier74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodStatement73"):
                opp_val = getattr(old_value, "ast_MethodStatement73", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodStatement73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodStatement73"):
                opp_val = getattr(value, "ast_MethodStatement73", None)
                setattr(value, "ast_MethodStatement73", self)

    @property
    def ast_Modifier37(self):
        return self.__ast_Modifier37

    @ast_Modifier37.setter
    def ast_Modifier37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier37", None)
        self.__ast_Modifier37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Feature"):
                opp_val = getattr(old_value, "ast_Feature", None)
                if opp_val == self:
                    setattr(old_value, "ast_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Feature"):
                opp_val = getattr(value, "ast_Feature", None)
                setattr(value, "ast_Feature", self)

    @property
    def ast_Modifier80(self):
        return self.__ast_Modifier80

    @ast_Modifier80.setter
    def ast_Modifier80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier80", None)
        self.__ast_Modifier80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ClassifierStatement79"):
                opp_val = getattr(old_value, "ast_ClassifierStatement79", None)
                if opp_val == self:
                    setattr(old_value, "ast_ClassifierStatement79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ClassifierStatement79"):
                opp_val = getattr(value, "ast_ClassifierStatement79", None)
                setattr(value, "ast_ClassifierStatement79", self)

    @property
    def ast_Modifier106(self):
        return self.__ast_Modifier106

    @ast_Modifier106.setter
    def ast_Modifier106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier106", None)
        self.__ast_Modifier106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ImportStatement"):
                opp_val = getattr(old_value, "ast_ImportStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_ImportStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ImportStatement"):
                opp_val = getattr(value, "ast_ImportStatement", None)
                setattr(value, "ast_ImportStatement", self)

    @property
    def ast_Modifier109(self):
        return self.__ast_Modifier109

    @ast_Modifier109.setter
    def ast_Modifier109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier109", None)
        self.__ast_Modifier109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ImportStatement108"):
                opp_val = getattr(old_value, "ast_ImportStatement108", None)
                if opp_val == self:
                    setattr(old_value, "ast_ImportStatement108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ImportStatement108"):
                opp_val = getattr(value, "ast_ImportStatement108", None)
                setattr(value, "ast_ImportStatement108", self)

    @property
    def ast_Modifier88(self):
        return self.__ast_Modifier88

    @ast_Modifier88.setter
    def ast_Modifier88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier88", None)
        self.__ast_Modifier88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ClassStatement"):
                opp_val = getattr(old_value, "ast_ClassStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_ClassStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ClassStatement"):
                opp_val = getattr(value, "ast_ClassStatement", None)
                setattr(value, "ast_ClassStatement", self)

    @property
    def ast_Modifier43(self):
        return self.__ast_Modifier43

    @ast_Modifier43.setter
    def ast_Modifier43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier43", None)
        self.__ast_Modifier43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Feature42"):
                opp_val = getattr(old_value, "ast_Feature42", None)
                if opp_val == self:
                    setattr(old_value, "ast_Feature42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Feature42"):
                opp_val = getattr(value, "ast_Feature42", None)
                setattr(value, "ast_Feature42", self)

    @property
    def ast_Modifier99(self):
        return self.__ast_Modifier99

    @ast_Modifier99.setter
    def ast_Modifier99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier99", None)
        self.__ast_Modifier99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ImplemenationClassifierStatement98"):
                opp_val = getattr(old_value, "ast_ImplemenationClassifierStatement98", None)
                if opp_val == self:
                    setattr(old_value, "ast_ImplemenationClassifierStatement98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ImplemenationClassifierStatement98"):
                opp_val = getattr(value, "ast_ImplemenationClassifierStatement98", None)
                setattr(value, "ast_ImplemenationClassifierStatement98", self)

    @property
    def ast_Modifier96(self):
        return self.__ast_Modifier96

    @ast_Modifier96.setter
    def ast_Modifier96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier96", None)
        self.__ast_Modifier96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ImplemenationClassifierStatement"):
                opp_val = getattr(old_value, "ast_ImplemenationClassifierStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_ImplemenationClassifierStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ImplemenationClassifierStatement"):
                opp_val = getattr(value, "ast_ImplemenationClassifierStatement", None)
                setattr(value, "ast_ImplemenationClassifierStatement", self)

    @property
    def ast_Modifier163(self):
        return self.__ast_Modifier163

    @ast_Modifier163.setter
    def ast_Modifier163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier163", None)
        self.__ast_Modifier163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_LocalVarStatement162"):
                opp_val = getattr(old_value, "ast_LocalVarStatement162", None)
                if opp_val == self:
                    setattr(old_value, "ast_LocalVarStatement162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_LocalVarStatement162"):
                opp_val = getattr(value, "ast_LocalVarStatement162", None)
                setattr(value, "ast_LocalVarStatement162", self)

    @property
    def ast_Modifier48(self):
        return self.__ast_Modifier48

    @ast_Modifier48.setter
    def ast_Modifier48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier48", None)
        self.__ast_Modifier48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FieldStatement47"):
                opp_val = getattr(old_value, "ast_FieldStatement47", None)
                if opp_val == self:
                    setattr(old_value, "ast_FieldStatement47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FieldStatement47"):
                opp_val = getattr(value, "ast_FieldStatement47", None)
                setattr(value, "ast_FieldStatement47", self)

    @property
    def ast_Modifier40(self):
        return self.__ast_Modifier40

    @ast_Modifier40.setter
    def ast_Modifier40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier40", None)
        self.__ast_Modifier40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Feature39"):
                opp_val = getattr(old_value, "ast_Feature39", None)
                if opp_val == self:
                    setattr(old_value, "ast_Feature39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Feature39"):
                opp_val = getattr(value, "ast_Feature39", None)
                setattr(value, "ast_Feature39", self)

    @property
    def ast_Modifier68(self):
        return self.__ast_Modifier68

    @ast_Modifier68.setter
    def ast_Modifier68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier68", None)
        self.__ast_Modifier68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodStatement67"):
                opp_val = getattr(old_value, "ast_MethodStatement67", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodStatement67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodStatement67"):
                opp_val = getattr(value, "ast_MethodStatement67", None)
                setattr(value, "ast_MethodStatement67", self)

    @property
    def ast_Modifier71(self):
        return self.__ast_Modifier71

    @ast_Modifier71.setter
    def ast_Modifier71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier71", None)
        self.__ast_Modifier71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodStatement70"):
                opp_val = getattr(old_value, "ast_MethodStatement70", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodStatement70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodStatement70"):
                opp_val = getattr(value, "ast_MethodStatement70", None)
                setattr(value, "ast_MethodStatement70", self)

    @property
    def ast_Modifier(self):
        return self.__ast_Modifier

    @ast_Modifier.setter
    def ast_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier", None)
        self.__ast_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Parameter"):
                opp_val = getattr(old_value, "ast_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "ast_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Parameter"):
                opp_val = getattr(value, "ast_Parameter", None)
                setattr(value, "ast_Parameter", self)

    @property
    def ast_Modifier45(self):
        return self.__ast_Modifier45

    @ast_Modifier45.setter
    def ast_Modifier45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier45", None)
        self.__ast_Modifier45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FieldStatement"):
                opp_val = getattr(old_value, "ast_FieldStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_FieldStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FieldStatement"):
                opp_val = getattr(value, "ast_FieldStatement", None)
                setattr(value, "ast_FieldStatement", self)

    @property
    def ast_Modifier102(self):
        return self.__ast_Modifier102

    @ast_Modifier102.setter
    def ast_Modifier102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier102", None)
        self.__ast_Modifier102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ImplemenationClassifierStatement101"):
                opp_val = getattr(old_value, "ast_ImplemenationClassifierStatement101", None)
                if opp_val == self:
                    setattr(old_value, "ast_ImplemenationClassifierStatement101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ImplemenationClassifierStatement101"):
                opp_val = getattr(value, "ast_ImplemenationClassifierStatement101", None)
                setattr(value, "ast_ImplemenationClassifierStatement101", self)

    @property
    def ast_Modifier65(self):
        return self.__ast_Modifier65

    @ast_Modifier65.setter
    def ast_Modifier65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Modifier__ast_Modifier65", None)
        self.__ast_Modifier65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodStatement64"):
                opp_val = getattr(old_value, "ast_MethodStatement64", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodStatement64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodStatement64"):
                opp_val = getattr(value, "ast_MethodStatement64", None)
                setattr(value, "ast_MethodStatement64", self)

class ast_DocumentationLine(EJElement):

    def __init__(self, text: str, ast_DocumentationLine: "ast_EJBase" = None):
        self.text = text
        self.ast_DocumentationLine = ast_DocumentationLine
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ast_DocumentationLine(self):
        return self.__ast_DocumentationLine

    @ast_DocumentationLine.setter
    def ast_DocumentationLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_DocumentationLine__ast_DocumentationLine", None)
        self.__ast_DocumentationLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_EJBase"):
                opp_val = getattr(old_value, "ast_EJBase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_EJBase"):
                opp_val = getattr(value, "ast_EJBase", None)
                if opp_val is None:
                    setattr(value, "ast_EJBase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ast_SwitchDefaultPartRef(EJElement):

    pass
class ast_AttributeSet(EJElement):

    pass
class ast_Label(EJElement):

    def __init__(self, name: str, ast_Label: "ast_JumpStatement" = None, ast_Label160: "ast_LabeledStatement" = None):
        self.name = name
        self.ast_Label = ast_Label
        self.ast_Label160 = ast_Label160
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ast_Label(self):
        return self.__ast_Label

    @ast_Label.setter
    def ast_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Label__ast_Label", None)
        self.__ast_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_JumpStatement"):
                opp_val = getattr(old_value, "ast_JumpStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_JumpStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_JumpStatement"):
                opp_val = getattr(value, "ast_JumpStatement", None)
                setattr(value, "ast_JumpStatement", self)

    @property
    def ast_Label160(self):
        return self.__ast_Label160

    @ast_Label160.setter
    def ast_Label160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Label__ast_Label160", None)
        self.__ast_Label160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_LabeledStatement"):
                opp_val = getattr(old_value, "ast_LabeledStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_LabeledStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_LabeledStatement"):
                opp_val = getattr(value, "ast_LabeledStatement", None)
                setattr(value, "ast_LabeledStatement", self)

class ast_EJBase(EJElement):

    pass